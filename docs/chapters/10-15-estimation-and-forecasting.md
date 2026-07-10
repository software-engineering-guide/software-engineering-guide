# 10.15 Estimation and forecasting

## Overview and motivation

Every software team is asked the same question: when will it be done? Behind that question sits [software development effort estimation](https://en.wikipedia.org/wiki/Software_development_effort_estimation), the practice of predicting how much work something will take before you have done it. It is one of the hardest things we do, and one of the easiest to do badly. The trouble is that software is discovery work. You are building something that has never existed, and much of what you will learn about the problem only becomes visible while you build. Predicting the effort of learning is genuinely different from predicting the effort of repeating a known task.

Why treat this as its own discipline rather than a corner of project management (chapter 10.6)? Because the failures are so consistent and so expensive. Teams routinely commit to single dates they have no evidence for, then defend those dates long past the point where reality has contradicted them. Leaders confuse an estimate with a promise. Contracts freeze a number produced in an afternoon and hold people to it for a year. The result is late delivery, eroded trust, and a culture where nobody says what they actually believe. Getting this right is less about better math and more about honesty: separating what you know from what you hope, and communicating uncertainty as uncertainty.

The stakes rise sharply in enterprise and government settings. Enterprises fund portfolios of interlocking initiatives against annual budgets and expect firm numbers to allocate capital (chapter 10.1). Governments make public commitments under appropriations rules, sign fixed-price contracts, and answer to legislators when a date slips. In both worlds the pressure to produce a confident single number is immense, and the deep uncertainty that makes that number unreliable does not vanish because someone important wants certainty. This chapter argues for a different posture: estimate when it helps you decide, forecast with evidence rather than optimism, and tell the truth about the range.

## Key principles

- **An estimate is a prediction, not a promise.** Keep it separate from targets and commitments.
- **Uncertainty is real, so express it.** A range with a probability beats a false single date.
- **The past predicts the future better than optimism does.** Prefer measured history to fresh guesses.
- **Decompose to understand, forecast to commit.** Small slices reduce both risk and the need to estimate.
- **Take the outside view.** Compare to similar past efforts before trusting your inside story.
- **Re-forecast continuously.** A prediction made once and never updated is decoration.
- **Estimate only when the answer will change a decision.** Otherwise it is waste.

## Recommendations

### Separate the estimate, the target, and the commitment

The single most useful move in this entire chapter costs nothing: keep three ideas distinct. An **estimate** is your honest prediction of how long something will take, with its uncertainty attached. A **target** is a business objective you would like to hit, such as a trade-show launch or a regulatory deadline. A **commitment** is a promise you make to someone else that you intend to keep. These are three different things, and collapsing them is how projects start lying to themselves. When a leader hears "about three to five months" and writes down "three months," and the sales team promises a customer "twelve weeks," an estimate has silently become a commitment without anyone deciding to accept the risk.

Say which one you are giving, every time. If asked for a date, answer with an estimate expressed as a range, then let the business set a target against it and decide, deliberately, what to commit to. A commitment should be a choice made with eyes open, weighing the estimate's uncertainty against the cost of missing. This discipline connects directly to how your organization makes and records decisions (chapter 1.5): a commitment is a decision, and it deserves a decision's rigor rather than a hallway nod.

### Understand why estimates are wrong, and in which direction

Software estimates are not randomly wrong. They are wrong in predictable, systematic ways, and knowing the pattern lets you correct for it. Early in any effort you sit inside the [cone of uncertainty](https://en.wikipedia.org/wiki/Cone_of_Uncertainty): at the outset your estimate can easily be off by a factor of four in either direction, and the range only narrows as you build and learn. Committing to a precise number at the wide mouth of the cone is committing to a figure you cannot yet support.

On top of that structural uncertainty sits a human bias. The [planning fallacy](https://en.wikipedia.org/wiki/Planning_fallacy) is our reliable tendency to underestimate the time, cost, and risk of our own plans while imagining the best case. We picture the happy path, forget the interruptions and the integration surprises and the sick days, and produce a number that assumes nothing goes wrong. Padding is the usual defensive response, but padding added by feel is just a second guess stacked on the first, and it gets negotiated away the moment schedules tighten. The cure is not more willpower; it is method. Base predictions on what similar work actually took, not on how this work feels from the inside.

### Use decomposition and expert judgment, and know their limits

The workhorse techniques are worth knowing and worth bounding. **Decomposition** breaks a large deliverable into smaller pieces you can reason about, then rolls the pieces up. It helps because people estimate small, familiar things far better than large, vague ones, and because summing many independent items lets some overestimates cancel some underestimates. Its limit is that decomposition misses the work between the boxes: integration, coordination, and the tasks you did not think to list. **Expert judgment** and estimation by **analogy** ("this is like the reporting module we built last year, which took two months") are fast and often surprisingly good, but they inherit the estimator's optimism and blind spots.

For anything you must put a number on, prefer [three-point estimation](https://en.wikipedia.org/wiki/Three-point_estimation), which asks for an optimistic, a most-likely, and a pessimistic figure and combines them, often as the PERT weighted average (optimistic plus four times most-likely plus pessimistic, divided by six). The value is not the precise formula. It is that three-point estimation forces you to state your uncertainty out loud and produces a range instead of a false point. Relative sizing methods such as **story points** and **t-shirt sizes** (small, medium, large, extra-large) sidestep the trap of predicting exact hours by comparing items to each other. They work well for ordering and rough capacity, but treat them as inputs to a forecast, not as currency. Points are not hours, and multiplying velocity by points to produce a date reintroduces every problem relative sizing was meant to avoid.

### Forecast probabilistically from your own flow data

Here is the shift that changes everything: stop asking people to guess how long work will take, and start measuring how fast your team actually finishes work. Your delivery pipeline (chapter 11.2) already produces the data you need. If you track [throughput](https://en.wikipedia.org/wiki/Throughput), the number of items your team completes per week, you can forecast the future from the past instead of from hope. A team that has closed six to eleven items a week for the last three months will, with high probability, take roughly four to seven weeks to finish forty remaining items. That forecast rests on evidence, and it updates itself every week as new data arrives.

The rigorous version runs a [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation: sample from your historical weekly throughput thousands of times to build a distribution of possible finish dates, then read off the answer as a probability. "We are 85% likely to finish by March 14, and 50% likely by February 28" is a vastly more useful and more honest statement than "it will be done March 1." This approach connects directly to queueing theory (chapter 11.3): lead time equals work in progress divided by throughput, so the same flow metrics that govern how work moves also govern when it will arrive. Probabilistic forecasting needs history and a reasonably stable process, which is exactly why it rewards teams that keep work small and flow steady. It also quietly removes most of the estimation ceremony, because you no longer need to size each item to know when the batch will land.

### Take the outside view for large programs

For big, long, expensive programs, individual estimates and even flow forecasts can mislead, because a novel program has no throughput history yet and its inside story is exactly where the planning fallacy bites hardest. The antidote is [reference class forecasting](https://en.wikipedia.org/wiki/Reference_class_forecasting): find a reference class of similar completed efforts, look at how long and how much they actually took, and place your program in that distribution before you trust your own bottom-up plan. If comparable platform replacements at your company have overrun their initial estimates by 60% on average, that number is better evidence about yours than the tidy plan your team just assembled. The outside view feels deflating, and that is precisely its worth: it counters the optimism that every fresh plan carries. Use it for portfolio funding and megaprogram budgeting (chapter 10.1), where the cost of a systematic overrun is measured in millions and in credibility.

### Estimate less by slicing smaller, and sequence by cost of delay

Sometimes the right amount of estimation is almost none. The **#NoEstimates** argument, at its reasonable core, observes that if you slice work into pieces small enough that each takes a day or two, the estimate of any single piece stops mattering. You simply count throughput and forecast from the count. When slices are uniform and small, elaborate sizing is waste: it consumes effort producing precision that the forecast does not need. This is not an argument against thinking ahead. It is an argument for making individual predictions cheap by making individual pieces small.

What still needs a decision is order. When you cannot do everything at once, sequence by **cost of delay**: the value you lose for each unit of time a given piece of work is late. A feature that unlocks a large contract next quarter has a high cost of delay and should jump ahead of a nice-to-have with none, even if the nice-to-have is easier. Weighing cost of delay against effort (the "weighted shortest job first" heuristic from lean thinking) tells you what to do next far more reliably than a backlog sorted by gut feel. Notice that this reframes the whole conversation: instead of "when will everything be done," which invites false precision, you ask "what is the most valuable thing to finish next," which you can actually answer.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Single-date estimate** | Simple; what stakeholders ask for | Precisely wrong; hides risk; becomes an accidental commitment |
| **Three-point / PERT estimate** | Forces uncertainty into the open; cheap | Still a guess; the formula implies false rigor |
| **Story points / t-shirt sizes** | Fast; good for ordering and rough capacity | Not hours; velocity math sneaks single dates back in |
| **Probabilistic flow forecast** | Evidence-based; self-updating; honest ranges | Needs history and stable flow; less "certain"-looking |
| **Reference class forecasting** | Corrects optimism on big programs | Needs comparable past efforts; deflating to hear |
| **#NoEstimates (small slices)** | Removes waste; forecast by counting | Needs disciplined slicing; unsettling to funders who want a number |

The central tension is **the certainty people want versus the honesty the work demands**. Funders, executives, contracts, and legislators ask for a firm single date because a single date is easy to budget, promise, and defend. Software rarely supports one. Resolve the tension not by fabricating certainty and not by refusing to answer, but by answering in the currency of probability: a range with confidence levels, re-forecast as evidence arrives. Pair it with small slices so that early, real deliveries replace distant, imaginary ones as the thing people trust. A demoed increment is worth more than any estimate.

## Questions to discuss with your team

1. **When someone asks you for a date, are you giving an estimate, a target, or a commitment, and does everyone in the room know which?** This is the question that prevents the most damage for the least effort. In most organizations these three collapse into one number the moment it leaves the team's mouth, and nobody decided to accept the risk that a prediction became a promise. Bring a real example: take your last committed deadline and trace it backward to the conversation where it was first uttered, and ask whether it was ever anything but a hopeful guess wearing a suit. The answer should change your language permanently, so that estimates go out as ranges, targets are named as business wishes, and commitments are made deliberately with the uncertainty weighed and recorded as a decision (chapter 1.5). If your team cannot point to where a commitment was consciously accepted, you are making promises by accident.

2. **Could you forecast your next release from measured throughput instead of from fresh estimates, and what is stopping you?** Most teams already have the data to answer "when will it be done" empirically, sitting unused in the tool that tracks their work. If you know how many items your team has completed per week over the last quarter, you can simulate a finish-date distribution and quote a probability rather than a wish. Bring your actual throughput history and your remaining item count, and compare the flow-based forecast to whatever date the team estimated by feel; the gap is usually instructive. If the blocker is that your items are wildly different sizes or your flow is erratic, that is itself the finding, because unstable flow is a delivery problem worth fixing regardless (chapters 11.2, 11.3). Moving from estimation to measurement is often less a tooling change than a decision to trust your own history over your optimism.

3. **For your largest current program, have you taken the outside view, or only built up an inside plan?** Big programs are where optimism compounds into expensive overruns, and where a confident bottom-up plan is most seductive and least reliable. The discipline is to name a reference class of similar completed efforts inside or outside your organization, find what they actually cost and how long they actually took, and locate your program honestly in that distribution before you defend your own numbers. Bring the data: how have comparable initiatives here overrun their first estimates, and does your current plan quietly assume you will beat every one of them? If it does, you are betting on being exceptional, which is a bet the base rates reliably lose. The outside view will make your forecast less flattering and far more defensible to the funders and auditors who will remember the number you gave (chapter 10.1).

## Examples

**Startup.** A nine-person startup preparing its Series A demo needs to know whether a key integration will be ready. Rather than let the founders promise investors a date, the lead quotes an estimate as a range and explains the cone of uncertainty behind it. The team has been closing five to nine backlog items a week, so they run a quick Monte Carlo forecast on the remaining work and report "80% likely by the third week of the quarter, even odds a week earlier." They slice the integration into two-day pieces so no single estimate matters much, sequence by cost of delay to build the investor-visible path first, and re-forecast every Friday. Investors get an honest, narrowing projection instead of a confident number that would have slipped.

**Enterprise.** A retailer replacing its order-management platform must fund the program through an annual capital cycle that demands a number. The program office resists the urge to defend the tidy bottom-up plan and instead builds a reference class from three comparable platform replacements, two internal and one publicly documented, which overran their initial estimates by 50% to 80%. They fund against the outside-view figure, express the schedule as a probability range rather than a fixed go-live, and stand up flow metrics from the first delivering team so that within a quarter the guess is replaced by a throughput-based forecast that updates monthly. When one stream runs hot, the re-forecast shows it early, and leadership rebalances rather than discovering the slip at the deadline.

**Government.** An agency modernizing a benefits system operates under appropriations and public scrutiny, where a missed public date is a headline. Instead of a single fixed-price, fixed-scope contract anchored to one distant milestone, it procures modular increments and commits publicly to a valuable core delivered early, with later scope expressed as a funded range rather than a promise. Program leaders brief oversight bodies using probabilistic forecasts and reference-class comparisons, explaining confidence levels in plain language, so that a "70% by September" is understood as exactly that. Demoed working increments become the evidence the public trusts, which is sturdier than any estimate a contractor could sign.

## Business case: motivations, ROI, and TCO

The return on honest estimation and forecasting is dominated by avoided catastrophe. Large software efforts overrun or fail far more often than they hit an original fixed plan, and the losses compound: sunk cost, foregone value from late delivery, emergency spending to recover, and the erosion of trust that follows a broken public commitment. The practices here (separating estimate from commitment, forecasting from real throughput, taking the outside view on big programs) are the ones that move a program off that failure curve. You are not buying a more accurate crystal ball. You are buying earlier, truer information about where you stand, which lets you correct while correction is still cheap.

On total cost of ownership, the shift from estimation ceremony to measured forecasting usually lowers cost rather than raising it. Elaborate up-front estimation is expensive to produce and decays the moment work begins, whereas a throughput-based forecast is nearly free once your delivery pipeline emits the data. Both extremes cost money: over-estimating (endless sizing meetings producing precision nobody uses) and under-forecasting (committing blind and paying for the overrun later). To make the case to leadership, put the fully loaded cost of your last major overrun next to the near-zero cost of tracking throughput and quoting ranges, and show how an outside-view forecast would have set a fundable expectation from the start.

## Anti-patterns and pitfalls

- **Single-date commitments:** a range collapsed to one number, then defended past the evidence.
- **Estimate laundering:** a hopeful guess passed up the chain until it hardens into a contractual promise.
- **Velocity as a schedule engine:** multiplying story points by velocity to manufacture a precise date.
- **Padding by feel:** a second guess stacked on the first, negotiated away under pressure.
- **Inside view only:** trusting a fresh bottom-up plan while ignoring what similar programs actually took.
- **Estimating everything:** sizing tiny, uniform slices whose individual estimates change no decision.
- **Frozen forecasts:** a prediction made once at kickoff and never updated as reality arrives.
- **Precision theater:** quoting hours to two decimals at the wide mouth of the cone of uncertainty.

## Maturity model

- **Level 1, Initial:** Estimates are single dates produced by gut feel and treated as promises; no distinction between estimate, target, and commitment; overruns surprise everyone and are blamed on the team.
- **Level 2, Managed:** Some structured estimation exists (decomposition, story points); estimates are still single numbers; velocity is used to project dates; forecasts are made once and rarely revisited.
- **Level 3, Defined:** Estimates are expressed as ranges with stated uncertainty; estimate, target, and commitment are kept distinct; teams track throughput and re-forecast regularly; large programs use reference-class comparisons.
- **Level 4, Optimizing:** Probabilistic forecasting from flow data is routine and updated continuously; commitments are deliberate decisions weighing confidence against cost; work is sliced small enough that estimation is minimal; cost of delay drives sequence; forecasts are trusted because history has shown them honest.

## Ideas for discussion

1. What would change in your organization if every estimate had to leave the team as a range with a confidence level, and single dates were forbidden?
2. Where are you spending effort estimating work that is already small and uniform enough to forecast by counting?
3. If you fed your last two quarters of throughput into a Monte Carlo simulation, would the forecast agree with the dates you actually committed to?
4. For your biggest program, what is the honest reference class, and how badly does the base rate contradict your current plan?
5. How does your team decide sequence today, and would ordering explicitly by cost of delay change what you build next?
6. When a commitment is accepted in your organization, is the uncertainty recorded as part of the decision, or does it vanish the moment the date is written down?

## Key takeaways

- Keep the **estimate, the target, and the commitment** distinct; collapsing them is how projects start lying to themselves.
- Estimates are systematically wrong in known directions: the **cone of uncertainty** widens early work, and the **planning fallacy** makes optimism the default.
- Prefer **probabilistic forecasting from measured throughput** over fresh guesses; quote ranges and confidence levels, and re-forecast continuously.
- Take the **outside view** with reference-class forecasting on large programs, where optimism is most expensive (chapter 10.1).
- **Slice small** so individual estimates stop mattering, and **sequence by cost of delay** rather than gut feel.
- Estimate only when it changes a decision; otherwise it is waste. See chapters 10.6 (project management), 11.2 (delivery), 11.3 (queueing theory), and 1.5 (decision-making and governance).

## References and further reading

- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* and *When Will It Be Done?* (probabilistic forecasting from flow data).
- Troy Magennis, *Forecasting and Simulating Software Development Projects* (Monte Carlo methods).
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done* (reference class forecasting and megaprojects).
- Daniel Kahneman, *Thinking, Fast and Slow* (the planning fallacy and the outside view).
- Donald Reinertsen, *The Principles of Product Development Flow* (cost of delay and queue economics).
- Vasco Duarte, *NoEstimates: How to Measure Project Progress Without Estimating*.
- Frederick Brooks, *The Mythical Man-Month* (why software schedules go wrong).
- Todd Little, "Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty" (*IEEE Software*, 2006).
