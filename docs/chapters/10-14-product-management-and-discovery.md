# 10.14 Product management and discovery

## Overview and motivation

[Product management](https://en.wikipedia.org/wiki/Product_management) is the discipline of deciding *what* to build and *why*, and being accountable for whether it works. A product manager owns the problem, the customer, and the outcome. They do not own the schedule, the ticket queue, or the feature checklist handed down from a stakeholder. That distinction is the whole chapter in one sentence. When product management collapses into project coordination or order-taking, a team becomes a feature factory: it ships constantly, hits its velocity numbers, and moves no business metric. The role exists to prevent exactly that.

For large teams, weak product management is quietly the most expensive failure mode there is. Engineering can be superb, delivery can be fast, and the whole machine can still spend a year building the wrong thing with great efficiency. The cost never appears on an engineering dashboard. It shows up as flat revenue, churned customers, and a backlog of features nobody uses but everybody must now maintain. Good product management makes that risk visible before you commit the money, by insisting that goals be explicit, measurable, and tied to a real customer problem.

Enterprise and government settings raise the stakes and change the shape of the work. Enterprises are increasingly moving from a project operating model (fund a project, ship it, disband the team) to a product operating model (fund durable teams that own outcomes over years), and treating internal platforms as products with real customers. Governments are learning the same lesson under the banner of user-centred design: fund services, not projects, and measure whether citizens are actually served. This chapter is about the mindset and the mechanics that make that shift real. It pairs closely with chapter 11.1 (the discovery pipeline), which details the pipeline machinery; here we focus on the role, the strategy, and the daily habits of discovery.

## Key principles

- **Own the what and the why.** Product managers are accountable for outcomes, not for coordinating tasks.
- **Outcomes over outputs.** Shipping is a cost, not a result. The result is a changed customer or business metric.
- **Know the customer and the problem better than anyone.** Strategy without customer contact is guesswork.
- **Discovery is continuous, not a phase.** You talk to customers every week, in parallel with delivery.
- **Prioritization frameworks are aids to judgment, not oracles.** Numbers inform the call; they do not make it.
- **Roadmaps are statements of intent, not dated promises.** Commit to problems firmly and solutions loosely.
- **Empower the trio.** Product, design, and engineering decide together; a product manager alone decides badly.

## Recommendations

### Own the what and the why, and let the team own the how

The clearest test of whether product management is healthy is who owns which question. The product manager owns *what problem we are solving* and *why it matters now*. Design owns *how it should feel* for the user. Engineering owns *how we build it*. When a product manager starts dictating solutions, deadlines, and implementation, they have become a project manager wearing a product title, and they have taken away the very autonomy that makes an empowered team effective (chapter 5.1 covers the design partnership, chapter 10.7 covers the agile delivery model).

An empowered product team, sometimes called the product trio, works as product, design, and engineering together, given a problem to solve rather than a feature to build. This is the difference between "increase 30-day retention for new users" and "build the notification centre by March." The first empowers the team to find the best solution and holds them to a result. The second reduces them to a delivery arm and quietly transfers the risk of being wrong onto the person who wrote the requirement. If you want accountability for outcomes, you have to give away control of outputs.

### Set a product vision and strategy grounded in the customer

A [product strategy](https://en.wikipedia.org/wiki/Product_strategy) is a small set of hard choices about which customers you serve, which problems you solve for them, and, just as importantly, which you refuse. Vision is the durable picture of the world you are trying to create, usually two to five years out. Strategy is the sequence of moves that gets you there. Without both, prioritization degenerates into whoever argues loudest, and the roadmap becomes a list of everyone's pet features stapled together.

Strategy is impossible without deep, first-hand knowledge of the customer and the problem. A product manager who cannot describe, in specific detail, who the customer is, what job they are trying to get done, and where they currently struggle, is not ready to prioritize anything. This is not a survey you commission once. It is a standing habit of contact. The best product leaders can recount last week's customer conversation from memory, not last quarter's research deck. When you know the problem cold, most prioritization arguments dissolve, because the team can reason from evidence instead of opinion.

### Manage to outcomes and escape the feature factory

The feature factory is what you get when success is defined as "we shipped it." Teams measure velocity, count releases, and celebrate launches, while the metrics that pay the bills sit flat. The antidote is to define success as an outcome (a change in customer or business behaviour) and to attach a measure to it before you build. This is where product management meets objectives and key results (chapter 11.4): objectives describe the change you want, key results measure it, and a key result phrased as "launch feature X" is a task in disguise.

Watch for the tells. If your roadmap is a list of features with no stated outcome, if nobody can say what metric a shipped feature moved, if the retrospective never asks "did it work" but only "did we ship it," you are in a feature factory. Escaping it is mostly a matter of discipline: refuse to accept work framed as a solution until someone states the problem and the measure. Product analytics and controlled experiments (chapter 7.4) give you the instrument panel to tell a real outcome from a comfortable story.

### Run continuous discovery alongside delivery

Continuous product discovery means that every week, in parallel with delivery, the team is learning from customers and testing the assumptions behind what it plans to build. The model is dual-track: a discovery track de-risks ideas while a delivery track builds the validated ones, and the two run continuously rather than as sequential phases (chapter 11.1 details the pipeline). The practical commitment behind it is small and relentless: talk to customers every single week, even when you are busy, especially when you are busy.

A useful backbone for this is the opportunity-solution tree: you start from a desired outcome, branch into the customer opportunities (needs, pain points, desires) that could move it, branch again into candidate solutions for each opportunity, and then into the assumption tests that would tell you whether a solution works. The tree keeps the team honest about *why* a given feature is on the table and forces you to compare opportunities rather than fall in love with the first solution. Before committing engineering, you test the riskiest assumption with the cheapest experiment: an interview, a prototype, a fake-door test, an A/B test. The output of discovery is not a feature list. It is a stream of validated, measurable bets ready for delivery.

### Use prioritization frameworks as aids to judgment, not oracles

Prioritization frameworks bring useful structure to a messy decision, and every one of them is wrong if you treat its number as truth. **RICE** scores each idea by Reach (how many users), Impact, Confidence, and Effort, then ranks by (Reach x Impact x Confidence) / Effort. **Weighted scoring** rates options against several weighted criteria. **Cost of delay** asks what each week of waiting costs you, which is often the sharpest lens for sequencing. The [Kano model](https://en.wikipedia.org/wiki/Kano_model) sorts features into basic expectations, performance needs, and delighters, reminding you that not all satisfaction is linear.

Use them to expose your assumptions and to make trade-offs discussable, not to abdicate the decision. The Confidence term in RICE and the estimates in weighted scoring are judgment calls dressed as arithmetic, and a false precision can launder a bad bet into a ranked list that looks objective. Run the numbers, then ask whether the ranking matches your strategy and your customer knowledge. If it does not, trust the judgment and interrogate the inputs. The framework is a thinking aid; you are still the one who has to be right.

### Treat roadmaps as statements of intent

A dated roadmap that promises specific features on specific quarters is a fiction that everyone signs and nobody can keep, because it fixes the one thing (the solution) that discovery is supposed to keep learning about. Prefer a **now / next / later** roadmap: what we are working on now, what is likely next, and what we are considering later, expressed as problems and outcomes rather than committed features with dates. This communicates direction honestly while preserving the freedom to change the solution as evidence arrives.

The underlying move is to commit firmly to problems and outcomes, and loosely to solutions. Stakeholders who demand date-certain feature commitments are usually asking for predictability, which is reasonable; give it to them at the level of outcomes and timeframes ("we will meaningfully reduce onboarding drop-off this half") rather than at the level of specific features you have not yet validated. When you must give a hard date, tie it to a valuable outcome and let the scope of the solution flex, exactly as chapter 10.6 recommends for project delivery.

### Validate desirability, viability, feasibility, and usability

Before you commit real investment, a product idea has to clear four risks. **Desirability**: do customers actually want it? **Viability**: does it work for the business (legal, financial, brand, sales)? **Feasibility**: can engineering build it with the time and technology available? **Usability**: can people actually use it? The trio is built to cover these: product leads on viability, design on usability, engineering on feasibility, and desirability is everyone's problem. Skip one and it comes back as a launch that customers ignore, legal blocks, engineering cannot ship, or users cannot figure out.

This is also the frame for build, buy, or partner decisions. If a capability is core to your differentiation, build it. If it is necessary but undifferentiated (billing, authentication, email delivery), strongly favour buying or partnering, because every feature you build carries a perpetual tail of maintenance, security surface, and cognitive load. A [minimum viable product](https://en.wikipedia.org/wiki/Minimum_viable_product) (MVP) is the cheapest thing that tests your riskiest assumption, not a stripped-down version 1.0 you ship and forget; keep it honest by asking what you will learn, not just what you will launch.

### Know product-market fit and invest in product operations

[Product-market fit](https://en.wikipedia.org/wiki/Product/market_fit) is the moment a product satisfies a strong market demand, and you usually feel it before you can prove it: retention curves flatten instead of decaying to zero, usage grows by word of mouth, customers would be genuinely upset to lose the product, and you struggle to keep up with demand rather than to create it. Before fit, your job is to find it, and almost nothing else matters. After fit, your job changes to scaling and defending it. Confusing the two phases (scaling before you have fit, or still searching after you have it) is a classic and expensive mistake.

As the number of product teams grows, invest in **product operations**: the shared research, data, tooling, and practices that let many teams do discovery well without each reinventing it. Product ops keeps the customer-interview cadence staffed, the analytics trustworthy, the roadmap format consistent, and the OKR rhythm running. In an enterprise moving to a product operating model, and in a platform-as-product organization where internal platforms have real internal customers, product ops is what keeps the model coherent across dozens of teams rather than letting it fragment into local habits.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Empowered product team (outcomes)** | Owns results; finds better solutions; motivated | Needs senior talent and real trust; harder to direct top-down |
| **Feature-team / order-taking model** | Predictable output; easy to manage and contract | Ships wrong things efficiently; no one owns the result |
| **Continuous discovery** | De-risks bets weekly; fast learning; less waste | Requires research capacity and discipline; harder to schedule |
| **Heavy up-front requirements** | Comforting to funders; clear scope | Assumptions untested; late feedback; big-bang risk |
| **Now/next/later roadmap** | Honest about uncertainty; preserves learning | Frustrates stakeholders who want dated feature commitments |
| **Dated feature roadmap** | Feels predictable; easy to communicate | Promises what you cannot know; rewards output over outcome |
| **Prioritization by framework score** | Structured, discussable, reduces politics | False precision; can launder a bad bet as objective |

The central tension is **commitment versus learning**. Budgets, contracts, and executives want firm commitments, which pulls toward dated feature roadmaps and up-front requirements. Good products need room to discover, which pulls toward outcomes and continuous experiments. Resolve it the same way throughout this guide: commit firmly to problems, outcomes, and timeframes, and hold specific solutions loosely. That gives leadership the predictability they actually need (measurable progress on the things that matter) without forcing the team to promise features it has not yet validated.

## Questions to discuss with your team

1. **Does your product manager own an outcome, or a backlog?** This is the single most revealing question about how your team really operates. If the product manager is measured on shipping the roadmap, chasing stakeholder requests, and keeping the sprint full, you have a project coordinator with a product title, and no one is actually accountable for whether the work moves a metric. Bring evidence: look at your product manager's last three deliverables and ask what customer or business outcome each was supposed to change, and whether anyone checked. In a large organization the stakes compound, because a single team pointed at outputs can burn multiple quarters building features that test well in demos and change nothing in production. The answer should reshape both what you measure the product manager on and how much control over solutions you are willing to give the team. If nobody owns an outcome, fix that before you argue about the roadmap.

2. **When did someone on this team last talk to a customer, and was it this week?** Continuous discovery lives or dies on this habit, and it is the first thing to get cut when delivery pressure rises, which is precisely when you most need it. Teams that stop talking to customers do not notice they have gone blind; they simply start reasoning from internal opinion and old research, growing more confident and less correct. Bring the actual log: count how many of your last ten features went through a documented assumption and a cheap test before build, versus straight from a stakeholder's mouth into the backlog. For enterprise and government teams, where one misaligned initiative can waste many team-quarters and, in the public sector, real public trust, name who is accountable for keeping the weekly customer contact alive. If the honest answer is "not this week" or "not sure," you are flying on assumptions and calling it strategy.

3. **What would it take to move from a project operating model to a product operating model, and what is stopping you?** Many enterprises still fund temporary projects, staff them, ship, and disband the team, which destroys the durable ownership and customer knowledge that good product work depends on. Shifting to durable teams that own outcomes over years, including treating internal platforms as products with real customers, is a change to funding, org design, and governance, not just a change of job titles. Bring evidence: trace how one current initiative is funded and staffed, and ask what happens to the accumulated learning when the project ends and the team scatters. The competing consideration is real, because annual project budgeting and procurement rules exist for legitimate accountability reasons, and you have to satisfy them, not ignore them. The answer should identify the smallest concrete step (one persistent team owning one outcome with a stable budget) that proves the model before you try to convert the whole portfolio (chapter 10.1).

4. **When we run a prioritization framework, is it informing the decision or just ratifying one already made?** RICE, weighted scoring, and cost of delay are useful precisely because they force assumptions into the open, and they turn corrosive the moment a number becomes an excuse to stop thinking. The competing consideration is real: frameworks reduce politics and give a defensible paper trail, which large organizations genuinely need, yet the Confidence and Impact terms are judgment dressed as arithmetic and can launder a bad bet into an objective-looking rank. Bring your last few prioritization decisions and check two things: whether anyone ever overrode the score when strategy or customer knowledge disagreed, and whether the highest-paid person's preference quietly set the inputs that produced the ranking. In enterprise and government settings, where a scored backlog often becomes the artefact shown to steering committees and auditors, name who is allowed to override the number and on what grounds, because a framework nobody can overrule has stopped being a thinking aid and become a rubber stamp.

5. **What have we promised stakeholders as dated features, and could we restate those commitments as outcomes without losing their trust?** Dated feature roadmaps feel like predictability and are usually fiction, because they fix the solution that discovery is supposed to keep learning about, and in a large organization every such promise ripples into dependent teams, marketing plans, and executive expectations. The tension is legitimate: funders and stakeholders want certainty for reasons of budgeting and accountability, so you cannot simply refuse to commit; you have to give predictability at the level of outcomes and timeframes instead of unvalidated features. Bring the current roadmap and mark each item as either an outcome you can commit to or a specific solution you are guessing at, then draft how you would restate the guesses as now/next/later problems. For enterprise and public-sector teams bound by annual budgets and procurement milestones, identify which commitments are genuinely contractual versus merely habitual, because the habitual ones are where you can trade false precision for honest direction, and the contractual ones are where you must negotiate the commitment to an outcome rather than a feature.

6. **Where are we building undifferentiated capability we could buy or partner for, and who decides?** Every feature you build carries a perpetual tail of maintenance, security surface, and support load, so hand-rolling billing, authentication, or email delivery spends your scarcest capacity on work that does not differentiate you (chapter 10.4). The competing consideration is that "buy" trades control and fit for speed and lower ownership cost, and sometimes a capability you assumed was commodity is actually core to your advantage, so the desirability-viability-feasibility-usability lens has to be applied honestly rather than as cover for a preference. Bring an inventory of what your teams are currently building in-house, mark each as core differentiator or undifferentiated plumbing, and estimate the ongoing ownership cost of the plumbing against a vendor alternative. In enterprise and government contexts, fold in procurement rules, data-residency and security requirements, and vendor lock-in and exit terms, because the build-buy-partner decision there is not just an engineering trade-off but a compliance and accountability one, and the person who owns it should be able to defend the choice to an auditor.

## Sector lens

**Startup.** With little runway, discovery is survival, not process. One founder wears the product hat, talks to customers every week without ceremony, and runs the cheapest possible tests (a fake-door button, five interviews) before committing either engineer to a build. Skip heavy frameworks and dated roadmaps; the whole company can hold the strategy in its head, so spend the discipline on refusing to build the loud request until someone states the problem and the metric.

**Small business.** You have no dedicated product manager, so product thinking is a habit the owner or a lead engineer carries alongside other duties. Frame most build-versus-buy calls toward buying: undifferentiated capability like booking, payments, or email belongs to a vendor, and your scarce attention goes to the one or two things that actually win customers. Keep a lightweight now/next/later list rather than a formal roadmap, and treat a single leading metric (repeat purchases, no-shows) as your outcome instead of a full OKR apparatus.

**Enterprise.** The work is coordinating many product teams without letting the model fragment: durable trios owning outcomes, a consistent roadmap format, and product operations keeping the interview cadence, analytics, and OKR rhythm coherent across dozens of teams. Governance and audit want traceability, so make outcomes, prioritization rationale, and kill decisions legible rather than reverting to dated feature promises that satisfy a committee but reward output over impact. Manage the shift from project funding to a product operating model deliberately, because org design and budgeting change slower than job titles.

**Government.** Procurement rules, transparency, and public accountability shape every choice. Fund durable service teams rather than fixed-scope projects, define success as a citizen outcome (time-to-apply, self-service completion) that oversight bodies can verify, and treat user-centred design and accessibility standards as hard requirements tested with real applicants, including assistive-technology users. Publish outcomes and progress plainly so scrutiny sees public value, and structure build-versus-buy and vendor contracts around data portability and exit so a supplier choice today does not become a decade of lock-in.

## Examples

**Startup.** A six-person startup building a scheduling tool for independent clinics resists the temptation to build the big "online booking" feature three loud customers keep requesting. The founder-product manager runs a week of discovery instead: five clinic-owner interviews, a fake-door button on the marketing site, and one leading metric (percentage of appointments that end in a no-show). The evidence says no-shows, not booking, are the real pain, so the team frames a single outcome (cut no-shows below 10% for pilot clinics this quarter), ships a small deposit-and-reminder MVP to test the riskiest assumption, and kills the booking feature before writing a line of it. The roadmap is a now/next/later list, not a dated plan, and the whole team can recount last week's customer call from memory.

**Enterprise.** A retail bank moves its payments group from a project model to a product model: one durable trio (product, design, engineering) owns "everyday payments feel instant" as a standing outcome with a stable annual budget, rather than a series of chartered projects. The team runs weekly customer interviews and maintains an opportunity-solution tree, uses RICE to sequence candidate solutions but overrides the ranking when cost-of-delay analysis shows a latency fix matters more, and publishes a now/next/later roadmap to stakeholders instead of dated feature promises. Two proposed features die in discovery for failing to move the leading indicators, saving an estimated two quarters of build effort, and product operations keeps the interview cadence and analytics trustworthy across the bank's fifteen product teams.

**Government.** A national agency modernizing benefits applications adopts the public-sector product mindset championed by digital service teams: it funds a durable service team, not a fixed-scope project, and defines success as a citizen outcome (cut median time-to-apply from 40 to 15 minutes and raise successful self-service completion from 55% to 85%) rather than delivered modules. User-centred design is non-negotiable: the team runs moderated usability testing with real applicants, including assistive-technology users, before every release, and treats accessibility standards as hard requirements. Because the roadmap is framed as outcomes and the team owns the service over years, oversight bodies see measurable public value instead of a spend report, and the agency can ship useful capability early rather than betting everything on one distant go-live (chapters 11.1, 5.1).

## Business case: motivations, ROI, and TCO

The return on real product management is dominated by **avoided waste**. Controlled-experiment programmes at large technology firms repeatedly find that a large share of built features, often cited around half, produce no measurable improvement or actively harm the target metric. If even a quarter of a team's capacity goes to ideas that continuous discovery would have killed cheaply, the discipline pays for itself many times over: a week of customer interviews and a fake-door test costs almost nothing against a quarter of engineering, plus the perpetual maintenance of a feature nobody uses. The primary cost of a feature factory is not the features it ships. It is the opportunity cost of the outcomes it never moved.

On **total cost of ownership**, every shipped feature is a standing liability: maintenance, testing, security surface, support load, and cognitive weight on everyone who has to navigate the product (chapter 10.4). Product management lowers that cost in two ways. It kills bad ideas in discovery, avoiding not just the build but the entire tail of ownership. And it steers build-buy-partner decisions toward buying undifferentiated capability, so your team's finite capacity goes to what actually differentiates you. The shift from a project operating model to a product operating model adds a further, subtler return: durable teams retain customer knowledge and codebase context that project teams throw away every time they disband and re-form.

To make the case to leadership, change the conversation from "how much are we shipping" to "how much are we moving the metrics that matter," and show two or three concrete examples of expensive features that moved nothing. The adoption cost is modest: research capacity, a discovery cadence, an outcome-based roadmap, and the discipline to define success before building. The risk of *not* investing is silent, uncounted, and compounding, because a feature factory looks productive right up until you notice the business has not moved.

## Anti-patterns and pitfalls

- **The feature factory:** success defined as "we shipped it," with velocity celebrated while business metrics sit flat.
- **Product manager as project manager:** owning the schedule and the ticket queue instead of the problem and the outcome.
- **Product manager as feature secretary:** transcribing stakeholder requests into a backlog with no problem or measure attached.
- **Roadmap as a dated feature promise:** committing to specific solutions on specific quarters you cannot yet validate.
- **Discovery as a one-time phase:** a discovery sprint up front, then months of building with no further customer contact.
- **HiPPO-driven prioritization:** the highest-paid person's opinion overrides evidence, and frameworks become theatre to ratify it.
- **Framework worship:** treating a RICE or weighted score as truth, letting false precision launder a bad bet.
- **Building undifferentiated infrastructure:** hand-rolling billing or auth that a vendor would provide better and cheaper.
- **Scaling before product-market fit:** pouring money into growth on a product the market does not yet strongly want.
- **Internal platform with no product owner:** a platform team building what it finds interesting rather than what its internal customers need.

## Maturity model

- **Level 1, Initiate:** Product management is order-taking and reactive. A dated feature roadmap is handed down; success is shipping it. No stated outcomes, no regular customer contact, and no one accountable for whether the work moved a metric.
- **Level 2, Develop:** Basic product practices appear but are inconsistent across teams. Outcomes and OKRs exist for some teams, yet goals are often output-shaped and roadmaps are still feature lists. Discovery happens occasionally, usually as an up-front phase, and prioritization uses a framework, sometimes as cover for the loudest voice.
- **Level 3, Standardize:** Empowered trios own outcomes, and the practice is documented and expected org-wide. Roadmaps are now/next/later statements of intent; continuous discovery is a staffed, weekly habit with documented assumption tests; prioritization frameworks inform judgment rather than replace it; and product-market fit is understood and tracked as a shared standard rather than a local habit.
- **Level 4, Manage:** The practice is measured and controlled against baselines. Each team tracks leading and lagging outcome metrics against a stated baseline, and post-launch every feature is checked against a pre-registered success metric with a kill threshold enforced on evidence, not opinion. Discovery health is instrumented too (interview cadence met, assumptions tested before build, ideas killed in discovery versus shipped), product-market-fit signals such as retention curves and would-be-disappointed scores are quantified, and framework inputs like RICE Confidence are calibrated against how bets actually turned out.
- **Level 5, Orchestrate:** A product operating model runs across the portfolio and is continuously improved and integrated with funding and strategy. Durable teams own outcomes over years and internal platforms are managed as products; discovery and delivery loop continuously; outcome data steers investment and rebalances the portfolio adaptively; product operations keeps the practice coherent at scale; and leadership manages a portfolio of outcomes, routinely retiring, re-scoping, and reprioritizing bets as evidence and the market shift.

## Ideas for discussion

1. Look at your current roadmap: how many items state a measurable outcome versus just a feature and a date?
2. Who on your team owns the customer relationship well enough to recount last week's conversation from memory?
3. Which of your recent features would you have killed if you had run a cheap experiment on the riskiest assumption first?
4. Where are you building undifferentiated capability that you could buy or partner for, and what is it costing you?
5. Do you have product-market fit, and how would you actually know, rather than assume?
6. What is the smallest step you could take toward a product operating model, and what governance obstacle stands in the way?

## Key takeaways

- Product management owns the **what** and the **why**, and is accountable for **outcomes**, not for coordinating tasks or transcribing requests.
- Escape the **feature factory** by defining success as a measured change in customer or business behaviour before you build.
- Run **continuous discovery** alongside delivery: talk to customers every week and test the riskiest assumption with the cheapest experiment (chapter 11.1).
- Use **prioritization frameworks** (RICE, weighted scoring, cost of delay, Kano) as aids to judgment, never as oracles.
- Treat **roadmaps as statements of intent** (now/next/later): commit firmly to problems and outcomes, loosely to solutions.
- Empower the **trio** and validate **desirability, viability, feasibility, and usability** before you invest (chapter 5.1).
- In enterprise and government, shift from a **project operating model** to a **product operating model**, fund services not projects, and invest in **product operations** (chapters 10.1, 11.4).

## References and further reading

- Marty Cagan, *Inspired* and *Empowered* (empowered product teams, the product operating model).
- Marty Cagan and Chris Jones, *Transformed* (moving to a product operating model).
- Teresa Torres, *Continuous Discovery Habits* (opportunity-solution trees, weekly customer contact).
- Melissa Perri, *Escaping the Build Trap* (outcomes over outputs, product operations).
- Roman Pichler, *Strategize* (product vision, strategy, and roadmaps).
- C. Todd Lombardo, Bruce McCarthy, Evan Ryan, and Michael Connors, *Product Roadmaps Relaunched* (now/next/later roadmaps).
- Dan Olsen, *The Lean Product Playbook* (product-market fit).
- Eric Ries, *The Lean Startup* (minimum viable product, build-measure-learn).
- Noriaki Kano et al., "Attractive Quality and Must-Be Quality" (*Journal of the Japanese Society for Quality Control*, 1984): origin of the Kano model.
- Melissa Perri and Denise Tilles, *Product Operations* (scaling product practice).
- U.S. Digital Service, *Digital Services Playbook*; UK Government Digital Service, *Government Design Principles* and *Service Standard* (public-sector, user-centered product delivery).
