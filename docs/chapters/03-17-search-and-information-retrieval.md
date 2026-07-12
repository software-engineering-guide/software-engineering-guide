# 3.17 Search and information retrieval

## Overview and motivation

Sooner or later, someone types a few words into a box and expects your system to find the right thing. That box is deceptively simple. Behind it sits one of the oldest and richest disciplines in computing: [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), the science of finding relevant items in a large collection from an imprecise request. Search is not a feature you bolt onto a product late; it is a system concern with its own data model, its own failure modes, its own scaling story, and its own way of being wrong. When search is good, people find what they need and barely notice. When search is bad, they leave, or worse, they conclude the thing they wanted does not exist.

This chapter treats search as first-class architecture. It sits alongside the data and storage decisions of chapter 3.4, because a search index is a specialized store optimized for query, distinct from the system of record that owns the truth. It leans on the caching and delivery ideas of chapter 3.15, because search results and suggestions are latency-sensitive and cacheable. And it now overlaps heavily with the generative artificial intelligence work of chapter 6.3, because modern retrieval feeds large language models the context they need to answer well.

For large teams, search is where relevance, freshness, and scale collide. An enterprise catalog with tens of millions of items, a government records portal answerable to the public, a support knowledge base that must surface the one article that resolves a ticket: each demands that search be measured, tuned, and operated with the same rigor as any other production system. The stakes are concrete. A tax authority whose search cannot find the right form at filing deadline, or a health portal that buries the relevant guidance under noise, fails its users in a way that erodes trust in the institution behind it.

## Key principles

- Treat the search index as a derived store, separate from your system of record.
- Relevance is a measurable quality, not a matter of taste; judge it with data.
- Match how people actually type: misspelled, terse, and ambiguous.
- Combine lexical and semantic retrieval; neither alone covers every query.
- Design the indexing pipeline for freshness, not just for the initial load.
- Evaluate offline with judgments and online with real behavior, and use both.
- Scale search deliberately with shards and replicas, and observe it like any service.

## Recommendations

### Start with the inverted index and analysis pipeline

The engine at the heart of classic search is the [inverted index](https://en.wikipedia.org/wiki/Inverted_index): a map from each term to the list of documents that contain it, the mirror image of a document that lists its terms. Ask for "invoice refund" and the engine intersects the posting list for "invoice" with the posting list for "refund" in milliseconds, no matter how many millions of documents you hold. This data structure is why search feels instant, and understanding it explains most of what search does and does not do well.

The index is only as good as the text you feed it, and that is the job of the [analyzer](https://en.wikipedia.org/wiki/Text_normalization). Analysis runs in stages. First, [tokenization](https://en.wikipedia.org/wiki/Lexical_analysis) splits a stream of text into terms, which is harder than splitting on spaces once you meet punctuation, hyphenation, and languages such as Chinese that do not delimit words. Then normalization lowercases, strips accents, and folds variants. Then [stemming](https://en.wikipedia.org/wiki/Stemming) or its more precise cousin lemmatization reduces "running," "ran," and "runs" toward a common root so a query for one matches the others. Stop-word handling, synonym expansion, and language detection round it out. The rule that saves you pain: index-time analysis and query-time analysis must agree, because a term is only found if both sides normalize it the same way.

### Understand relevance ranking before you tune it

Finding the matching documents is the easy half. Ordering them so the best one sits at the top is the hard half, and it is called ranking. The traditional workhorse is [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), short for term frequency times inverse document frequency: a term counts for more when it appears often in a document (term frequency) and when it is rare across the whole collection (inverse document frequency), so "photosynthesis" outweighs "the." Most modern engines default to [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25), a refinement that saturates term frequency (the tenth occurrence adds little over the ninth) and normalizes for document length so long documents do not win by sheer size. You do not need to derive the formula, but you should know that a knob exists, that it has principled defaults, and that changing it changes which results rank first.

Judge quality with two words from the field. [Precision](https://en.wikipedia.org/wiki/Precision_and_recall) is the fraction of returned results that are relevant; recall is the fraction of all relevant results that you returned. They trade against each other. Loosen the query to catch every possible match and precision falls as noise creeps in; tighten it for a clean result set and recall falls as good matches drop out. Every relevance decision, from typo tolerance to synonym expansion, is a bet on where along that curve your users want to be, and the answer differs for a legal archive (favor recall, miss nothing) versus a storefront (favor precision, show winners).

### Invest in query understanding

Users do not type the way your documents are written. They misspell, abbreviate, search for a synonym you never indexed, and cram three intents into four words. Query understanding is the layer that bridges that gap, and it repays investment more than almost anything else. Add curated and mined synonyms so "laptop" finds "notebook" and "heart attack" finds "myocardial infarction." Add typo tolerance through [edit distance](https://en.wikipedia.org/wiki/Levenshtein_distance), the number of single-character changes between two strings, so "reciept" still finds receipts. Detect entities and intent so "flights to Paris under $500" routes to the right filters rather than a bag of words.

Handle the hardest queries deliberately. A search for a rare exact string, such as an order number or a statute citation, wants an exact match and no clever expansion. A vague natural-language question wants the opposite. Route these differently rather than forcing one behavior on both. And always design the [zero-results](https://en.wikipedia.org/wiki/Faceted_search) case: when a query returns nothing, relax it, suggest alternatives, or fall back to a broader match, because an empty page is the fastest way to lose a user.

### Add facets, autocomplete, and structured filtering

Search is more than a ranked list. [Faceted search](https://en.wikipedia.org/wiki/Faceted_search) lets users narrow results by structured attributes: brand, price range, department, date, document type. Facets turn an overwhelming result set into a guided conversation, and they double as navigation. They depend on your data being cleanly attributed, which is a data-quality investment upstream of search, and they interact with ranking, because a filter changes the candidate set the ranker sees.

Autocomplete and suggestions shape the query before it is even submitted. A good suggester proposes real, high-value queries as the user types, corrects spelling early, and surfaces popular or trending intents. It is latency-critical (every keystroke is a request) and benefits directly from the caching patterns of chapter 3.15. Suggestions also steer people toward queries you handle well, which quietly raises overall relevance. Treat the suggester as its own small index with its own ranking, tuned on query logs rather than document content.

### Combine lexical and vector search

Classic search matches words. It cannot tell that "car" and "automobile" mean the same thing unless you told it, and it stumbles on questions phrased in ways your documents never use. [Vector search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) addresses this by representing text as an [embedding](https://en.wikipedia.org/wiki/Word_embedding), a dense numeric vector produced by a machine-learning model such that similar meanings land near each other in the vector space. Retrieval then becomes a nearest-neighbor search in that space, and because exact nearest-neighbor is too slow at scale, engines use approximate nearest neighbor (ANN) algorithms that trade a sliver of accuracy for large speed gains. Semantic search of this kind finds the right document even when it shares no words with the query.

Neither approach wins everywhere. Lexical search excels at exact terms, names, codes, and rare keywords; it is transparent and cheap to explain. Vector search excels at meaning, paraphrase, and natural-language questions, but it can miss an exact identifier and is harder to debug. The strong default for serious systems is [hybrid search](https://en.wikipedia.org/wiki/Learning_to_rank): run both and fuse the results, often with a technique such as reciprocal rank fusion that blends two ranked lists without needing their scores to be comparable. Hybrid gives you the precision of keywords and the recall of semantics, and it degrades gracefully when either side is weak.

### Connect search to retrieval-augmented generation

The fastest-growing consumer of search is not a human reading a result list; it is a language model. [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) grounds a generative model in your data by retrieving relevant passages and placing them in the model's context so it answers from your facts rather than its training memory. The generation quality of chapter 6.3 depends directly on retrieval quality: feed the model the wrong passages and it will confidently synthesize a wrong answer. Everything in this chapter (chunking text into passages, ranking them well, fusing lexical and vector signals, keeping the index fresh) is precisely the retrieval half of RAG. If your organization is building on large language models, your search system is the foundation, and improving recall on the right passages often helps the assistant more than swapping the model.

### Build an indexing pipeline for freshness

An index is a copy, and a copy drifts. The indexing pipeline is the machinery that keeps the search index in step with the system of record: reading source changes, running analysis and embedding, and writing to the index, ideally as a stream rather than a nightly batch. This is a data-engineering concern (chapter 7.2), and the same care about ordering, retries, and idempotence from chapter 3.3 applies, because an out-of-order update can resurrect a deleted document. Decide your freshness target explicitly. A price or inventory count may need to be searchable within seconds; an archived policy document can lag by hours. Support full reindexing for schema and analyzer changes, and design it to run without downtime, typically by building a new index and switching an alias atomically once it is ready.

### Tune relevance with evaluation, not opinion

Relevance arguments are unwinnable by assertion, so replace opinion with measurement. Offline, build a judgment list: a set of representative queries paired with human ratings of which results are relevant, and score your ranking against it with a metric such as [NDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) (normalized discounted cumulative gain), which rewards putting highly relevant results near the top and discounts those buried lower. Offline evaluation lets you compare two ranking configurations before either touches a user. Online, watch real behavior: click-through rate, the position of clicked results, query reformulations, zero-result rate, and conversions. Run controlled experiments (chapter 7.4) so a relevance change is proven against a holdout rather than shipped on a hunch. Use both, because offline metrics are fast but idealized, while online metrics are real but slow and noisy. The mature loop mines query logs to grow the judgment list, so evaluation improves as you learn.

### Scale with shards and replicas, and observe everything

Search scales along two axes. [Sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) splits one index across machines by partitioning documents, so a query fans out to every shard and the partial results merge; this lets an index grow past what one machine holds and spreads indexing load. Replicas copy each shard so read traffic spreads across copies and the loss of a node does not lose data; replicas serve query throughput and provide resilience. More shards raise fan-out cost per query, so size them to your data, not to a round number. Operate search with the observability of chapter 9.2: track query latency percentiles (the tail matters more than the average), indexing lag, cache hit rates, error rates, and, as first-class signals, relevance metrics such as zero-result rate and click position. A search system that is fast but returns poor results is failing silently, and only relevance telemetry will tell you.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Lexical (BM25) search | Exact terms, codes, names; transparent; cheap | Blind to synonyms and paraphrase without tuning |
| Vector (semantic) search | Understands meaning and questions; strong recall | Misses exact IDs; costly to compute; harder to debug |
| Hybrid search | Precision of keywords plus recall of semantics | More moving parts; fusion needs tuning and testing |
| Aggressive typo and synonym expansion | Higher recall; forgiving of real users | Precision falls; noisy results if unchecked |
| Real-time indexing | Fresh results within seconds | Higher cost and complexity than batch |
| More shards | Larger indexes; parallel indexing | Higher per-query fan-out and coordination cost |
| Offline evaluation (judgment lists) | Fast, repeatable, safe to iterate | Idealized; may not match real user behavior |
| Online evaluation (click metrics, tests) | Reflects real users and intent | Slow, noisy, needs traffic and experiment discipline |

The recurring tension is precision versus recall, and it hides inside every knob. Loosen matching, expand synonyms, and lean on semantics, and you catch more at the cost of noise; tighten everything and you are clean but you miss things. There is no universal setting, only the right setting for a given collection and audience, discovered by measurement. The second tension is freshness versus cost: real-time indexing and hybrid retrieval both buy quality with compute and complexity. Resolve both the same way, by tying each decision to an evaluation metric and a user outcome rather than to intuition, so you can see what a change actually bought you.

## Questions to discuss with your team

1. **How do we measure search relevance today, and would we notice if it got worse?** Many teams cannot answer this, which means their relevance is whatever the defaults produced and they are flying blind to regressions. Bring your current signals: do you have a judgment list, do you track zero-result rate and click position, could you compare two ranking configurations objectively? The gap between "search feels fine" and "here is our NDCG on a hundred graded queries, and here is last month's trend" is the gap between guessing and engineering. The action that follows is to build even a small judgment list and instrument click behavior, because you cannot tune what you cannot measure, and every relevance change you ship blind is a change you cannot defend.

2. **Where do lexical and semantic retrieval each fail us, and should we go hybrid?** Pure keyword search quietly fails on paraphrased questions and synonyms, while pure vector search quietly fails on exact identifiers and rare terms, and most teams have only ever run one of the two. Bring a set of real queries that returned poor results and classify why each failed: was it a missing synonym, a spelling error, a semantic mismatch, or a missing exact match? The pattern in those failures tells you whether hybrid search would help and where to spend effort first. This matters more if you are feeding a language model, because retrieval failures become confident wrong answers, and the cost of a bad result rises sharply when a generative layer sits on top of it.

3. **What is our freshness requirement, and does our indexing pipeline actually meet it?** Freshness is usually assumed rather than specified, so teams discover the mismatch during an incident when a deleted item keeps appearing or a price update lags by hours. Bring the real numbers: how long from a change in the system of record to that change being searchable, and how does that compare to what different parts of your catalog actually need? The answer will likely differ by data type, and naming it forces the pipeline decisions about streaming versus batch, ordering, and reindexing. An index that is stale in ways your users can see undermines trust in the whole product, and a freshness target you have never measured is a target you are probably missing.

## Examples

**Startup.** A ten-person software company adds search to its support knowledge base so customers can self-serve. They begin with BM25 defaults and quickly hit the ceiling: users ask questions in plain language that share no keywords with the articles. They add vector embeddings and fuse the two with reciprocal rank fusion, and deflection improves overnight. To tune, they mine their own query logs, label a few hundred query-article pairs, and track click position weekly. When they later add an in-product assistant, the same retrieval layer becomes the RAG backend, so the search investment pays off twice.

**Enterprise.** A global retailer runs product search over tens of millions of items across dozens of markets and languages. The index is sharded for size and replicated for throughput, with per-language analyzers handling tokenization and stemming correctly for each market. Faceted navigation by brand, price, and availability turns huge result sets into guided browsing, and autocomplete steers shoppers toward high-converting queries. Relevance is a funded team with judgment lists per market and continuous online experiments; a ranking change ships only after it beats the control on conversion. A real-time indexing pipeline keeps price and stock searchable within seconds, because a sold-out item ranked first is a lost sale and a support ticket.

**Government.** A national agency publishes regulations, forms, and guidance that the public must be able to find, often under legal obligation and at deadline-driven peak load. The team favors recall and transparency: citizens searching for a benefit must not miss the relevant form, and the agency must be able to explain why a result appeared, which pushes them toward interpretable lexical ranking augmented, carefully, with synonyms for the plain-language terms people use instead of official titles. Accessibility and multilingual support are requirements, not extras. The index reindexes without downtime behind an alias when policy documents change, and zero-result queries are logged and reviewed as a signal of unmet public need.

## Business case: motivations, ROI, and TCO

Search sits directly on the path to value. In commerce, a measurable share of revenue flows through the search box, and users who search convert at higher rates than those who only browse, so a few points of relevance improvement translate into real money. In support and internal tools, better search deflects tickets, shortens handle times, and recovers the hours knowledge workers lose hunting for documents. In the public sector, effective search is a service-quality and equity issue: people who cannot find the right form or guidance cannot exercise a right or meet an obligation. These outcomes are quantifiable, which is exactly why search deserves funded evaluation rather than best-effort defaults.

The total cost of ownership goes well past the license or the cluster. You pay for the compute and storage of the index and its replicas, for embedding generation if you go semantic, for the indexing pipeline that keeps it fresh, and, most of all, for the ongoing human work of relevance tuning and evaluation. That last cost is the one teams underestimate and the one that most determines success, because search is never finished: catalogs change, language drifts, and yesterday's tuning decays. Buying a managed search or vector service can lower operational cost and speed you up, at the price of some control and potential lock-in, a classic build-versus-buy call to weigh against your scale and differentiation. The strongest business case ties a specific relevance metric to a specific outcome, funds the evaluation loop, and treats search as a product that is measured and improved, not a component that is installed and forgotten.

## Anti-patterns and pitfalls

- **Mismatched analysis:** index-time and query-time analyzers disagree, so terms silently fail to match and results vanish with no error.
- **Relevance by opinion:** ranking tuned by whoever argues hardest, with no judgment list, no metrics, and no way to catch regressions.
- **Vector-only faith:** replacing keyword search entirely with embeddings, then failing on exact IDs, codes, and rare terms.
- **Ignoring zero results:** letting empty result pages stand instead of relaxing, suggesting, or falling back, and losing the user.
- **Stale index:** a nightly batch pipeline serving prices, stock, or deletions that users can see are wrong.
- **Reindex downtime:** rebuilding in place instead of behind an alias, taking search offline during every schema change.
- **Untuned defaults forever:** shipping out-of-the-box BM25 and never revisiting it as the collection and audience evolve.
- **No relevance telemetry:** monitoring latency and errors but not zero-result rate or click position, so poor results fail silently.
- **Overzealous expansion:** stacking synonyms and typo tolerance until precision collapses and every query returns noise.

## Maturity model

- **Level 1, Initial:** Search is a default database query or an untuned engine with stock settings. There is no relevance measurement, no query-understanding layer, and freshness is whatever a batch job produces. Poor results are noticed only when users complain.
- **Level 2, Managed:** A real search engine is in place with sensible analysis, BM25 ranking, and basic facets and autocomplete. Some synonyms and typo tolerance exist. The team watches latency and errors and has begun logging zero-result queries, but relevance is still tuned by opinion.
- **Level 3, Defined:** Relevance is measured with a judgment list and NDCG offline and click metrics online. Hybrid lexical-plus-vector retrieval is in production where it helps. The indexing pipeline meets a stated freshness target and reindexes without downtime. Sharding and replication are sized deliberately, and relevance metrics are monitored alongside operational ones.
- **Level 4, Optimizing:** Search improvement is a continuous, experiment-driven loop. Judgment lists grow from mined query logs, ranking changes ship only after winning controlled tests, and query understanding adapts to real language. Retrieval is tuned as the foundation for downstream generative applications, and the whole system is observed end to end for both speed and relevance.

## Ideas for discussion

1. What fraction of your searches return zero results or lead to a reformulation, and what do those queries reveal about unmet need?
2. If you replaced keyword search with pure vector search tomorrow, which queries would break, and how would you know before your users did?
3. Who owns relevance in your organization, and do they have a judgment list and metrics, or only opinions and anecdotes?
4. How long is the delay from a change in your system of record to that change being searchable, and is that acceptable for every data type?
5. If a language model consumes your search results, does your retrieval quality meet the higher bar that a generative answer demands?
6. How would you defend a ranking change to a skeptical stakeholder: with an experiment result, or with a story?

## Key takeaways

- Treat search as a first-class system: a derived index with its own data model, pipeline, scaling, and failure modes, separate from your system of record.
- Master the fundamentals (inverted index, matched analysis, BM25 ranking, precision versus recall) before reaching for anything fancier.
- Invest in query understanding (synonyms, typo tolerance, intent, and a real zero-results plan) because users never type the way your documents read.
- Default to hybrid retrieval that fuses lexical and vector search, and remember that this same retrieval layer is the foundation of retrieval-augmented generation.
- Replace opinion with measurement: judgment lists and NDCG offline, click metrics and controlled experiments online, and relevance telemetry monitored like any production signal.

## References and further reading

- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze, *Introduction to Information Retrieval*
- Stephen E. Robertson and Hugo Zaragoza, *The Probabilistic Relevance Framework: BM25 and Beyond*
- Ricardo Baeza-Yates and Berthier Ribeiro-Neto, *Modern Information Retrieval: The Concepts and Technology behind Search*
- Doug Turnbull and John Berryman, *Relevant Search: With Applications for Solr and Elasticsearch*
- Trey Grainger, Doug Turnbull, and Max Irwin, *AI-Powered Search*
- Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- Jeff Johnson, Matthijs Douze, and Hervé Jégou, "Billion-Scale Similarity Search with GPUs"
- Kalervo Järvelin and Jaana Kekäläinen, "Cumulated Gain-Based Evaluation of IR Techniques"
