# 5.8 Design research and usability testing

## Overview and motivation

[User research](https://en.wikipedia.org/wiki/User_research) is the discipline of learning about the people you build for: their goals, contexts, tasks, and the obstacles that trip them up. Its core value is risk reduction. The most expensive mistake in software is not a bug or a missed deadline; it is building the wrong thing well, then discovering after launch that nobody needed it or nobody could use it. Research buys down that risk cheaply, before you have poured engineering into a direction that turns out to be wrong. Chapter 5.1 lays the UX foundations; this chapter goes deep on the two engines that keep those foundations honest, generative research that tells you what to build and evaluative research that tells you whether what you built actually works.

For large teams the stakes multiply. When many squads ship into one product, each is making bets about users every sprint, and without a shared research habit those bets are just opinions wearing the costume of confidence. A small, steady stream of evidence gives everyone the same reality to argue from, so debates end in "let us go watch a few users" rather than in whoever has the most seniority or the loudest voice. Research also travels: one well-run study can correct the assumptions of a dozen teams at once, if you capture and share it well.

Enterprise and government raise the bar again. Enterprise software often has captive users who cannot quit, so unusable tools get paid for in errors, training, and lost hours rather than in churn you can see on a dashboard. Government services reach the whole public, including people in crisis, on old phones, with low digital confidence, or with no other option. Many national digital service standards now make user research mandatory for exactly this reason, because a form nobody can finish denies people benefits they are entitled to. Here research is not a nicety. It is how you keep a public promise.

## Key principles

- Research reduces the risk of building the wrong thing; it is cheapest before you build, not after.
- Generative research finds the right problem; evaluative research checks the solution. You need both.
- Watch what people do, not just what they say; stated preference and real behavior diverge.
- Qualitative methods explain why; quantitative methods size how many. Pair them.
- Small and continuous beats rare and heavyweight. A few users every week outlearns one big study a year.
- Your findings are only as representative as your participants, so recruit deliberately, including disabled and hard-to-reach users.
- Insight that lives in one team's slide deck is lost. Capture research so the whole organization can reuse it.
- Bias creeps in through leading questions and wishful synthesis; design against it on purpose.

## Recommendations

### Separate generative research from evaluative research

Be explicit about which question you are asking, because the methods differ. Generative (or discovery) research is open-ended and explores a problem space before you have a solution: What are people actually trying to accomplish? Where does the current experience hurt? What do they work around? Evaluative research tests a specific design against a task: Can people complete it, and where do they stumble? Confusing the two wastes both. Running a tightly scripted [usability testing](https://en.wikipedia.org/wiki/Usability_testing) session when you still do not understand the problem gives you polished answers to the wrong question, while an unstructured chat when you need to validate a checkout flow leaves you guessing. Name the research question first, then pick the method, and feed generative findings into product discovery (chapter 10.14) where the roadmap is actually shaped.

### Match the method to the question

There is no all-purpose method, only fits. User interviews surface motivations, mental models, and history, and they are your workhorse for discovery. [Contextual inquiry](https://en.wikipedia.org/wiki/Contextual_inquiry), where you observe people doing real work in their own environment, reveals the workarounds and interruptions that people never mention in a conference room. Surveys measure attitudes and frequencies across a large population but cannot explain the reasons behind them, and they punish sloppy question design brutally. [Card sorting](https://en.wikipedia.org/wiki/Card_sorting) and tree testing derive and validate information architecture from users' mental models: card sorting asks people to group and label concepts, while tree testing checks whether they can find things in a proposed structure. Diary studies capture behavior that unfolds over days or weeks, such as onboarding or habit formation, that no single session can see. A simple heuristic: use interviews and contextual inquiry to understand people, card sorting and tree testing to structure information, surveys and diary studies to see across time and scale, and usability testing to check a design.

### Run usability tests early, often, and small

Usability testing is the single highest-leverage evaluative method, and you can start it with paper sketches long before code exists. The well-known heuristic is that about five users per round uncover the majority of the severe, obvious usability problems, so you are better off running three rounds of five as the design evolves than one grand study of fifteen at the end. Understand the heuristic's limits, though. Five users is enough only for a single homogeneous group discovering big problems; it does not measure success rates, does not cover distinct user segments (each meaningfully different group needs its own handful), and does not catch rare-but-severe issues. Choose moderated testing when you want to probe reasoning, adapt on the fly, and handle complex or sensitive tasks, and unmoderated testing when you want speed, volume, geographic reach, and lower cost for straightforward flows. Most mature teams run both: moderated to understand, unmoderated to confirm at scale.

### Write tasks and questions that do not lead the witness

Your study is only as trustworthy as your protocol, and the fastest way to ruin it is to telegraph the answer you hope for. Give participants realistic goals, not instructions: say "you have just moved house and need to update your address" rather than "click the Edit Profile button and change your address." Ask about past behavior instead of future intentions, because "would you use this?" reliably produces polite lies while "tell me about the last time you did this" produces facts. Avoid questions that assume their own conclusion, and stay alert to [confirmation bias](https://en.wikipedia.org/wiki/Confirmation_bias), the human tendency to notice and remember evidence that supports what you already believe. The researcher who wrote the design should not silently coach participants toward success, and the team watching should record what happened before debating what it means. When you separate the design and communication of tasks from the design of the product (chapter 5.4), you get cleaner signal.

### Recruit participants who actually represent your users

Findings inherit the bias of your recruiting. If you only ever test with confident, connected, tech-comfortable volunteers, you will ship something that works beautifully for people who barely needed help and fails the people who needed it most. Define your segments, then recruit against them deliberately, including disabled users who rely on assistive technology (chapter 5.3) and hard-to-reach groups such as people in crisis, people with low digital confidence, older users, and those on slow connections or old devices. Reaching these participants takes more effort and often partnership with community organizations, appropriate incentives, and flexible logistics, but skipping it does not make the users disappear; it just moves the discovery to production, where it is far more expensive and far more harmful. Screen carefully so you get real members of a segment rather than professional testers who game the incentives.

### Synthesize findings into decisions, not just reports

Raw observations are not insight. The work of synthesis is turning a pile of session notes into a small number of decisions the team can act on. Affinity mapping, clustering individual observations into themes (the practice behind the [affinity diagram](https://en.wikipedia.org/wiki/Affinity_diagram)), is the standard move for making patterns visible across sessions. For interview-heavy studies, a light [thematic analysis](https://en.wikipedia.org/wiki/Thematic_analysis) keeps you honest about which themes are actually supported by the data. Roll durable patterns up into the shared models from chapter 5.1, evidence-based personas and journey maps, so insight compounds instead of evaporating. The test of good synthesis is simple: did a decision change? A study that produces a beautiful deck and no altered roadmap item was theater. End every study with a short, ranked list of findings and a recommended action for each.

### Triangulate qualitative research with analytics and experimentation

Qualitative research and quantitative data answer different halves of the same question, and each covers the other's blind spot. Research explains why users behave as they do but sees only the handful of people in the room; analytics and experimentation (chapter 7.4) see the whole population but cannot explain motivation or catch the problems of people who never became users. Use them as a loop: analytics shows a drop-off, research explains it, a redesign addresses it, and an experiment measures whether the fix moved the number. When qualitative and quantitative signals disagree, treat the contradiction as a clue rather than a nuisance, because usually one of them is measuring something you did not realize you were measuring. Neither source is the boss of the other; the decision comes from reading them together.

### Build research operations so research scales

As soon as more than a couple of teams do research, the bottleneck stops being method and becomes logistics: recruiting, scheduling, consent, incentives, note storage, and finding last quarter's study before someone reruns it. Research operations (ResearchOps) is the practice of making that machinery reliable. Invest in a searchable insight repository so findings are tagged, discoverable, and reusable across teams; a participant management system that respects consent, privacy, and how often you contact people; and a regular research cadence so studies are a steady habit rather than a scramble. Democratizing research, letting non-researchers run some studies, is worth doing but only with guardrails: templates, training, and review, so you scale the volume of learning without scaling the volume of bad protocols and biased conclusions.

## Trade-offs: pros and cons

| Method | Best for | Pros | Cons |
| --- | --- | --- | --- |
| User interviews | Discovery, motivations | Deep why, flexible, cheap to start | Small N, prone to interviewer bias |
| Contextual inquiry | Real-world behavior | Reveals workarounds and context | Time-consuming, hard to schedule |
| Surveys | Attitudes at scale | Large N, quantifiable | Cannot explain why, easy to write badly |
| Card sorting and tree testing | Information architecture | Grounds structure in mental models | Narrow scope, needs careful analysis |
| Diary studies | Behavior over time | Captures longitudinal patterns | High dropout, participant effort |
| Moderated usability testing | Understanding a design | Probing, adaptive, rich | Slower, costlier, scheduler-heavy |
| Unmoderated usability testing | Confirming at scale | Fast, cheap, geographically broad | No follow-up, shallow on complex tasks |

The central tension is depth versus scale, and the resolution is sequencing rather than choosing. Use deep, qualitative, small-N methods to understand and to generate hypotheses, then use broad, quantitative methods to size and confirm them. A second tension is speed versus rigor: continuous lightweight research keeps the team learning every week, but the same speed that makes it valuable makes it easy to cut corners on recruiting and protocol. Resolve it by matching rigor to reversibility. Spend real methodological care on decisions that are expensive to undo (core flows, information architecture, platform bets) and move fast and loose on the details you can change next sprint.

## Questions to discuss with your team

1. **When we make a product bet, what is the smallest piece of research that would change our mind, and are we willing to run it before we commit?** Teams love research in principle and skip it under deadline pressure, so the real question is whether evidence has any authority over the roadmap at all. Decide in advance what would count as disconfirming evidence, because a study you will ignore regardless of outcome is a waste of everyone's time and a form of theater. This matters most for decisions that are expensive to reverse, where a week of discovery is trivial next to months of building the wrong thing. Bring a current decision and name, out loud, the finding that would make you change course. If no finding could change it, you are not doing research, you are collecting reassurance, and you should either commit honestly or open the decision back up.

2. **Do the people we test with actually look like the people who use the product, especially the ones who struggle most?** It is comfortable to recruit confident, connected, available volunteers, and that comfort produces a flattering and false read of how usable your product really is. The users who most need the software to work well, disabled users, people in crisis, people with low digital confidence, are usually the hardest to recruit, so they quietly fall out of the sample unless you fight for them. Pull the participant demographics from your last three studies and lay them next to your real user base or your public-service obligations. If they skew toward easy-to-reach users, your confidence is misplaced, and you should fix the recruiting pipeline, partner with community organizations, and adjust incentives before you trust another round of findings.

3. **Where do our research findings live, and could another team find and reuse them six months from now?** In a large organization the same question gets researched again and again because nobody could find the answer the first team already paid for, which is pure waste dressed up as diligence. Decide who owns the insight repository, how studies get tagged and summarized, and what the minimum viable write-up is so that capturing a finding is fast enough that people actually do it. Consider what happens to consent and participant privacy as findings get reused and shared, because reuse without care is a compliance and trust problem. Bring one recent decision and try to trace the evidence behind it. If you cannot find the study in under a few minutes, your research is evaporating faster than you are producing it.

## Examples

**Startup.** A six-person startup building expense software for freelancers was convinced the killer feature was automated receipt scanning, and had built a rough version. Before investing further, two founders ran five moderated usability sessions with real freelancers using paper prototypes, framing tasks as goals ("log the coffee you just expensed") rather than instructions. Four of the five ignored scanning entirely and hand-typed amounts, because their real anxiety was not data entry speed but whether an expense would survive a tax audit. The team pivoted the product around audit-ready categorization and a clear paper trail, ran two more small rounds as they iterated, and turned a stalling free trial into paying subscribers, all for the cost of a week of sketches and conversations.

**Enterprise.** A global logistics company was standardizing warehouse software across sites and set up a permanent research operations function to keep dozens of product squads honest. They built a tagged insight repository, a managed panel of warehouse staff who had consented to periodic sessions, and a fortnightly research cadence. When two squads independently proposed redesigning the same scanning workflow, a search of the repository surfaced a contextual inquiry from the previous quarter showing that gloves and cold-store conditions, not screen layout, drove most scan errors. That single reused finding redirected both squads toward larger tap targets and glove-friendly interactions, avoided duplicated discovery, and measurably cut mis-scans once shipped.

**Government.** A national health service redesigning its appointment-booking service treated user research as mandatory under its digital service standard, not optional. Alongside moderated usability testing with a demographically broad sample, the team ran assisted-digital sessions with people who normally rely on a relative or a library assistant, and recruited disabled participants using screen readers and switch access (chapter 5.3) through partnerships with charities. Testing revealed that clinical jargon in section headings caused older and lower-confidence users to abandon before reaching a real barrier. Restructuring content around patients' plain-language goals, then confirming the gain with an unmoderated study at scale and a live analytics comparison (chapter 7.4), raised successful self-service bookings and reduced call-center load, improving both cost to serve and equity of access.

## Business case: motivations, ROI, and TCO

The return on research comes from three levers. First, avoided waste: catching a wrong direction during a week of discovery instead of after a quarter of engineering is the largest and most under-counted saving, precisely because the wasted build never happens and so never appears on a report. Second, higher success: more users completing valuable tasks, which shows up as conversion in consumer products and as productivity and fewer errors in enterprise settings where users are captive. Third, lower cost to serve: usable services generate fewer support contacts, less training, and fewer downstream mistakes to correct.

Total cost of ownership has to weigh the cost of doing research against the cost of skipping it. The costs of doing it are visible and modest: researchers, recruiting and incentives, tooling, a repository, and time in the schedule. The costs of skipping it are larger but scattered across other budgets: abandoned transactions, support tickets, training days, expensive late redesigns, failed launches, and, in the public sector, exclusion of citizens and the legal and reputational exposure that follows. Because these costs hide in support, training, and operations rather than in the product line, leadership routinely underestimates them, which is exactly why research looks optional right up until a launch fails.

To make the case, tie research to numbers executives already watch: completion and conversion rates, cost per transaction, support volume, training time, and error and rework rates. Run one small, instrumented before-and-after on a real flow, show the movement, and extrapolate across the portfolio. Frame research as risk reduction on irreversible decisions, the language that resonates with finance and governance stakeholders who may never read a usability report but understand a bet that could go wrong.

## Anti-patterns and pitfalls

- **Research theater**: studies run to justify a decision already made, with findings quietly ignored when inconvenient.
- **Leading the witness**: tasks and questions that telegraph the desired answer, producing flattering data that means nothing.
- **Confirmation-biased synthesis**: hearing only the observations that fit the plan and discarding the rest.
- **The five-users fallacy**: treating "about five users" as a universal law, ignoring that it assumes one segment and only finds severe issues, not success rates.
- **Convenience recruiting**: testing whoever is easy to reach, so disabled and hard-to-reach users vanish from the sample.
- **Stated-preference trust**: believing "yes, I would use that" instead of watching what people actually do.
- **Insight graveyards**: findings buried in one team's slides, so the same question gets researched over and over.
- **Democratization without guardrails**: letting anyone run studies with no templates or review, scaling biased protocols and shaky conclusions.
- **Qualitative-versus-quantitative tribalism**: picking a favorite data source and dismissing the other instead of triangulating.

## Maturity model

- **Level 1, Initial:** Research is ad hoc or absent. Decisions rest on opinion and seniority. Usability testing, if it happens, is a one-off before launch with whoever is handy, and findings rarely change anything.
- **Level 2, Managed:** Some teams run usability tests and occasional interviews, but recruiting is convenient, protocols are informal, and insights live in scattered decks. Research is a phase that gets cut under schedule pressure.
- **Level 3, Defined:** Generative and evaluative research run continuously and feed prioritization. Recruiting targets real segments including disabled and hard-to-reach users. A searchable insight repository exists, synthesis produces ranked decisions, and research operations manage cadence and participants.
- **Level 4, Optimizing:** Research is a continuous, triangulated loop with analytics and experimentation, closing from insight to shipped change to measured effect. Democratized research runs safely within guardrails, findings compound across the organization, and research demonstrably shapes strategy, not just screens.

## Ideas for discussion

1. How much discovery is "enough" before committing to a build, and who has the authority to say when you have learned enough?
2. When analytics and interviews tell you opposite stories about the same feature, how should the team decide which to act on?
3. Where is the line between responsibly democratizing research and letting untrained enthusiasm produce biased studies at scale?
4. How do you measure the return on a study whose value is a mistake you therefore never made and can never point to?
5. What is the ethical way to research with people in crisis or in vulnerable circumstances without adding to their burden?
6. Should mandatory user research, as in government service standards, be a gate that can block a launch, and who enforces it?

## Key takeaways

- Research exists to reduce the risk of building the wrong thing, and it is cheapest before you build.
- Separate generative research (find the right problem) from evaluative research (check the solution); pick the method from the question.
- "About five users" finds most severe issues in one segment per round, but it does not measure success or cover distinct groups.
- Write tasks as realistic goals, ask about past behavior, and design against leading questions and confirmation bias.
- Recruit participants who truly represent your users, including disabled and hard-to-reach people, or your findings are quietly false.
- Synthesize into ranked decisions, not decks; the test is whether a decision actually changed.
- Triangulate qualitative research with analytics and experimentation, and capture findings in a shared repository so learning compounds.

## References and further reading

- Erika Hall, *Just Enough Research*
- Steve Krug, *Rocket Surgery Made Easy*
- Jakob Nielsen, *Usability Engineering*
- Mike Kuniavsky, *Observing the User Experience*
- Steve Portigal, *Interviewing Users*
- Tomer Sharon, *Validating Product Ideas: Through Lean User Research*
- Hugh Beyer and Karen Holtzblatt, *Contextual Design*
- Donna Spencer, *Card Sorting: Designing Usable Categories*
- Kathy Baxter, Catherine Courage, and Kelly Caine, *Understanding Your Users*
- Kate Towsey, *Research That Scales: The Research Operations Handbook*
- Nielsen Norman Group, articles on usability testing, sample size, and research methods
- UK Government Digital Service, *Service Manual*: user research guidance
