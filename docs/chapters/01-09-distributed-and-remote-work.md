# 1.9 Distributed and remote work

## Overview and motivation

Where your people sit, and how their locations shape the way work flows, is now a first-class design decision, not an afterthought about desks. Teams sit somewhere on a spectrum: **co-located** (everyone in one building), **[remote](https://en.wikipedia.org/wiki/Remote_work)** (everyone working from wherever they are), and **hybrid** (a mix, often the same people some days in an office and some days out). Each point on that spectrum demands a different operating model. The mistake large organizations make is picking a location policy and assuming the way of working can stay the same. It cannot.

This chapter takes an opinionated stance: at scale, design for distribution as the default, make asynchronous work the baseline, and treat writing as the primary way you communicate. This is the same conclusion chapter 1.4 (ways of working) reaches from the delivery angle, and it rests on the values of chapter 1.1 and the documentation practice of chapter 2.7. A thousand people spread across a dozen time zones cannot coordinate through meetings and hallway conversations. Whether or not you call yourself "remote," a large team is already distributed, and the organizations that thrive are the ones that admit it and build for it.

Enterprises and government feel this most sharply. Enterprises chase global talent pools, run follow-the-sun operations, and argue internally over return-to-office mandates while paying for half-empty real estate. Government agencies operate under formal telework policy, must reconcile remote flexibility with on-site requirements for classified systems or in-person citizen services, and carry a duty to keep access equitable across a workforce with uneven home connectivity. The recommendations below help you choose a position on the spectrum deliberately and build the practices that make it work.

## Key principles

- Distribution is a spectrum: choose your position deliberately, then design the practices to match.
- Async-first is the default; synchronous time is a scarce resource spent on purpose.
- Writing is the primary medium, and documentation is the source of truth (chapter 2.7).
- Measure outcomes, not hours or presence. Trust is the operating assumption.
- Design timezone overlap and written handoffs on purpose, not by accident.
- In hybrid, hold one standard for everyone, or the remote half becomes second class.
- Belonging and secure access are built, not assumed.

## Recommendations

### Choose a point on the spectrum and commit to it

Do not drift into a location model by accident. Decide, and write it down. A **co-located** team can lean on synchronous rhythm and shared physical context. A **fully distributed** team must invest in writing, tooling, and overlap design. The genuinely hard case is **hybrid**, because it tempts you to run co-located habits (the impromptu whiteboard, the decision made at lunch) while half the team cannot see them. Pick "office-first," "remote-first," or a clearly defined hybrid, and align hiring (chapter 1.8), compensation, and meeting norms to that choice. A stated policy beats an ambiguous one even if the ambiguous one sounds more flexible.

### Make asynchronous the default operating mode

Treat asynchronous work, communication that does not require both parties present at once, as the baseline, and synchronous time as the exception you justify. Most updates, proposals, and reviews can be a written document that people read and respond to on their own schedule. Reserve live time for what genuinely needs it: building relationships, resolving ambiguity fast, sensitive conversations, and a few high-bandwidth design debates. When you invert this default, so that decisions happen in meetings and documents merely record them, you exclude everyone who was not in the room and everyone in the wrong time zone.

### Write things down, and make the document the source of truth

Distributed work runs on writing. Design docs, [architecture decision records](https://en.wikipedia.org/wiki/Architectural_decision), thorough tickets, and written status updates let someone in another time zone contribute fully and let a new joiner onboard by reading rather than by interrupting. The rule is simple: if a decision is not written down, it did not happen. This is the documentation discipline of chapter 2.7 applied to how the team itself operates. It costs real writing habit that not everyone has yet, and that investment is precisely what buys you scale.

### Design timezone overlap and handoffs on purpose

Spread across [time zones](https://en.wikipedia.org/wiki/Time_zone), you have two choices, and you should make them explicitly. Either cluster a team within a few hours of overlap, or run a true **[follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun)** model where work passes between regions. Follow-the-sun only works when handoffs are written and complete, never verbal, so the receiving region can act without waiting for the sending region to wake up. Define a small block of overlapping **core hours** for the synchronous contact you do need, and rotate the pain of inconvenient times fairly instead of always taxing the same region. Team topology (chapter 1.2) matters here: cut dependencies so that teams needing tight real-time collaboration are not scattered across incompatible clocks.

### Decide which decisions need synchronous time

Not every decision deserves a meeting, and not every decision can survive without one. Route routine, reversible, or well-framed choices through written proposals with a comment period, connecting to the decision-making practice of chapter 1.5. Reserve synchronous discussion for decisions that are contentious, ambiguous, high-stakes, or emotionally charged, where a live conversation genuinely converges faster than a document thread. Name which is which so people stop defaulting to "let's set up a call" for things a paragraph could settle.

### Keep meetings clean and always recorded

The meetings you do hold should earn their place. Give each one an agenda and a written outcome, invite only who is needed, and default to recording and summarizing so the people who could not attend can catch up. A recorded, summarized meeting becomes an asynchronous artifact, which widens who can benefit from it. Protect large blocks of focus time from meeting fragmentation, and be suspicious of any recurring meeting that produces no decisions or notes.

### Measure outcomes, not hours or presence

Remote work exposes a management reflex worth naming and rejecting: measuring activity because you cannot see the person. Judge people by the outcomes they deliver, not by hours logged, green status dots, or messages sent. Surveillance tooling that counts keystrokes corrodes trust and rewards performing busyness over doing work. Set clear goals, make progress visible through the work itself, and extend the trust that lets adults manage their own time. This is the outcome-over-utilization stance of chapter 1.4, applied to people rather than process.

### Build belonging and onboard deliberately when remote

Belonging does not happen by proximity when there is no proximity, so build it. Structured onboarding matters more remotely, because a new hire cannot absorb norms by osmosis: pair them with a buddy, give them a written first-week path, and make early wins reachable by reading rather than by cornering someone. This is the onboarding of chapter 1.8 with the ambient learning removed and replaced by explicit design. Invest in low-stakes social connection and, where budget allows, occasional in-person gatherings that build the relationships remote work then sustains.

### Secure remote access without a trusted perimeter

When people work from anywhere on any network, the old model of a trusted office network stops protecting you. Adopt a **[zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)** posture, where no device or user is trusted by default and every access request is verified regardless of location, together with checks on device health (patch level, disk encryption, managed status) before granting access. This is the remote-access application of the infrastructure and cloud security practice in chapter 4.3. Done well, it makes secure remote work seamless; done badly, it pushes people toward insecure workarounds.

### In hybrid, hold one standard so you avoid a two-tier culture

Hybrid's central danger is a two-tier culture: the office group makes decisions and forms bonds while the remote group receives summaries and misses out. Counter it deliberately. When any participant is remote, everyone joins the call individually so no one is a face on a distant screen. Put decisions in writing regardless of where they were made. Watch for **proximity bias**, the tendency to favor the people you physically see when assigning work, credit, and promotions, which quietly disadvantages remote staff in the evaluation and advancement practices of chapter 1.3. If you cannot hold one standard for both groups, you are running two cultures and calling it one.

## Trade-offs: pros and cons

| Model | Pros | Cons |
| --- | --- | --- |
| Co-located | High-bandwidth, fast informal coordination, easy belonging | Small local talent pool; costly real estate; excludes remote contributors |
| Fully distributed / remote-first | Widest talent pool; async scales; durable written record | Demands writing discipline and tooling; belonging must be engineered |
| Hybrid | Flexibility; some in-person collaboration | Two-tier culture and proximity bias unless actively managed |
| Follow-the-sun | Around-the-clock progress; global coverage | Fragile without complete written handoffs; coordination overhead |
| Async-first communication | Inclusive across time zones; durable; fewer meetings | Slower for ambiguous topics; needs writing habit |

The overarching tension is bandwidth versus reach. Co-located, synchronous work maximizes the richness of any single interaction, at the cost of who can participate and when. Distributed, asynchronous work maximizes reach, durability, and inclusion, at the cost of some immediacy and a real investment in writing. For most large organizations the resolution is the same: default to distributed and asynchronous to get scale and inclusion, then buy back the high-bandwidth moments deliberately through overlap hours and occasional gatherings, rather than the reverse.

## Questions to discuss with your team

1. **Where on the co-located-to-distributed spectrum are you actually operating, and does your way of working match it?** Many teams claim one model and run another: a "remote-first" company whose real decisions happen in a headquarters hallway, or a "hybrid" team with no shared standard at all. The competing considerations are real, because co-located work is genuinely higher-bandwidth while distributed work reaches more talent and scales better across time zones. Bring evidence: where do your decisions actually get made, who is routinely absent from them, and how much of your knowledge lives only in someone's memory? For a large enterprise or government program blending staff, contractors, and vendors across regions, the honest answer usually points toward async-first whether or not leadership has said so. The answer should produce an explicit, written policy that your hiring, meetings, and tooling then align to.

2. **What do you measure to know someone is doing good work, and would it survive if you could not see them at all?** Remote work strips away the visual cues managers lean on, and the tempting fix, activity tracking and presence monitoring, rewards the appearance of work over its substance. The competing pull is genuine accountability: leadership does need confidence that outcomes are landing. Bring your current signals to the table and sort them into outcomes (shipped results, resolved problems) versus proxies (hours online, messages sent, green dots). For enterprises weighing return-to-office mandates and governments bound by telework rules, this question decides whether flexibility is real or merely tolerated. If your only evidence of productivity is presence, you have not yet learned to manage outcomes, and the change should be in your goals and visibility, not your surveillance.

3. **How will you keep hybrid from splitting into an in-office in-group and a remote out-group?** Proximity bias is well documented and quiet: the people a manager sees get more of the interesting work, more informal mentoring, and, over time, more promotions, while equally capable remote colleagues fall behind through no fault of their own. The tension is that in-person time has real value for relationships and hard conversations, so the answer is not to ban offices. Bring data on who attends in person, who gets stretch assignments, and who has been promoted lately, then look for a pattern that tracks location rather than merit. In government, this connects to equity of access, because staff with worse home connectivity or caregiving constraints are disproportionately the remote group. Decide concrete countermeasures: everyone dials in individually when anyone is remote, decisions are written down, and promotion criteria are audited for a location skew.

## Examples

**Startup.** A twelve-person startup hires across five countries from day one and declares itself remote-first in writing. Every decision lands in a document, every meeting is recorded and summarized, and the team holds two overlapping core hours that rotate quarterly so no region always draws the early call. When they add an engineer in a new time zone, onboarding is mostly reading, and the async habit absorbs the growth without changing. They deliberately skip the daily synchronous standup, replacing it with a written update, and it is the one ritual they never miss having.

**Enterprise.** A multinational software company runs a follow-the-sun support and engineering operation across three regions and is fighting over a return-to-office mandate. It resolves the tension by separating questions: it keeps a remote-first default for individual work, invests in complete written handoffs so each region can resume where the last left off, and reserves office space for occasional team gatherings rather than mandated daily attendance. It adopts a zero-trust access model (chapter 4.3) so people work securely from anywhere, and it audits promotion rates by location after a manager notices the office cohort advancing faster, correcting a proximity bias before it hardened. Half-used floors are given up, and the real-estate savings fund travel for in-person offsites.

**Government.** A federal agency operates under a formal telework policy while running systems that mix routine casework with classified processing. Staff on unclassified citizen-facing services work distributed, with written handoffs and recorded decisions, while classified work stays on-site in a secure facility, and the agency is explicit about which tasks fall where. It provisions equipment and connectivity stipends so that eligibility for telework does not depend on who happens to have good home internet, treating equity of access as a requirement rather than a perk. Secure remote access follows a zero-trust model with device-posture checks. Required progress reports come straight from the shared boards and documents, so oversight is satisfied as a byproduct of how the distributed teams already work.

## Business case: motivations, ROI, and TCO

The economic case for distributed work has three main drivers. The first is the **talent pool**: hiring beyond commuting distance widens your candidate reach by orders of magnitude, which is decisive for scarce skills and for building diverse teams. The second is **real estate**: office space is one of the largest fixed costs a large employer carries, and a genuine remote or hybrid model lets you shed or repurpose much of it. The third is **flow and inclusion**: an async-first, docs-first operating model shrinks the meeting load and lets people in every time zone contribute fully, which raises throughput across the whole workforce (chapter 1.4).

Set these against the total cost of ownership. Distributed work is not free: it requires tooling, security investment for remote access, a stipend or equipment budget for home setups, occasional travel for in-person gatherings, and, most of all, the cultural investment in writing and deliberate onboarding. Those are modest against the savings, and against the cost of the status quo. The cost of getting it wrong shows up as regretted attrition when a clumsy return-to-office mandate drives out your best distributed hires, as excluded remote contributors, and as a two-tier culture that quietly wastes half your talent. To make the case to leadership, put the real-estate line item next to the talent-pool expansion and the attrition risk, and measure outcomes, delivery lead time, retention, hiring reach, rather than office occupancy.

## Anti-patterns and pitfalls

- **Remote in name only:** declaring remote-first while real decisions happen in a headquarters hallway, excluding everyone not physically present.
- **Meeting-first defaulting:** reaching for a call for things a written paragraph would settle, taxing every other time zone.
- **Surveillance over trust:** keystroke logging and presence monitoring that reward performing busyness and corrode the trust remote work depends on.
- **Undocumented decisions:** knowledge trapped in memory and past calls, unreachable to anyone who was not there.
- **Proximity bias in promotion:** favoring the people a manager can see when assigning work and advancement, disadvantaging remote staff.
- **Two-tier hybrid:** a room of people plus a few faces on a screen, where the room makes the decisions.
- **Follow-the-sun with verbal handoffs:** passing work between regions without complete written context, so the next region stalls.
- **Blanket return-to-office mandates:** imposed without a reason tied to the work, driving out distributed talent hired in good faith.
- **Ignoring equity of access:** treating telework eligibility as a perk when home connectivity and space are unevenly distributed.

## Maturity model

- **Level 1, Initial:** Location policy is unstated or contradictory. Communication is meeting-driven and undocumented; remote participants are an afterthought on a screen. Productivity is judged by presence, and belonging is left to chance.
- **Level 2, Managed:** A location model exists on paper, and some teams write things down, but meetings remain the default and handoffs are inconsistent. Hybrid meetings still favor the room, and proximity bias goes unexamined. Remote access is bolted on rather than designed.
- **Level 3, Defined:** Async-first is the norm, documentation is the source of truth (chapter 2.7), and meetings are agenda-driven, recorded, and summarized. Core hours and written handoffs are deliberate; onboarding is structured for remote joiners (chapter 1.8); zero-trust access is standard (chapter 4.3); and one standard governs hybrid participation.
- **Level 4, Optimizing:** The organization tunes its distribution model from outcome data, not presence. Timezone overlap and team topology are designed together (chapter 1.2); promotion is audited for proximity bias (chapter 1.3); belonging is actively built; and distributed, hybrid, and follow-the-sun teams collaborate smoothly with equity of access treated as a requirement.

## Ideas for discussion

1. If you wrote down your true location policy today, would it match what leadership says it is, and what would change if it did?
2. Which of your recurring meetings would survive being replaced by a written document plus a comment period?
3. Whose time zone bears the cost of your synchronous meetings, and how could you share that cost more fairly?
4. Would your evidence that someone is doing good work survive if you could never see them online at all?
5. In your last few promotion rounds, did location predict advancement more than it should have?
6. If you run any follow-the-sun handoff, could the receiving region act on it without waiting for the sending region to wake up?

## Key takeaways

- Distribution is a spectrum from co-located to hybrid to fully remote; choose a position deliberately and align your practices to it.
- Default to asynchronous, and treat synchronous time as a scarce resource for ambiguity, relationships, and high-stakes decisions.
- Make writing the primary medium and documentation the source of truth (chapter 2.7); an unwritten decision did not happen.
- Design timezone overlap and complete written handoffs on purpose; rotate the burden of inconvenient hours fairly.
- Measure outcomes, not hours or presence, and extend the trust that remote work depends on.
- In hybrid, hold one standard for everyone and audit for proximity bias, or you will build a two-tier culture (chapters 1.3, 1.8).
- Secure remote access with a zero-trust posture and device-health checks (chapter 4.3), and treat equity of access as a requirement.

## References and further reading

- Sam Lauer and Darren Murph, GitLab, *The Remote Playbook* (public guidance on all-remote, async-first working).
- Nicholas Bloom et al., "Does Working from Home Work? Evidence from a Chinese Experiment" (*Quarterly Journal of Economics*, 2015).
- Jason Fried and David Heinemeier Hansson, *Remote: Office Not Required*.
- Sid Sijbrandij and the GitLab team, *The GitLab Handbook* (public documentation of remote-first operations).
- Automattic, "How We Work" and Matt Mullenweg's writing on distributed work and the five levels of autonomy.
- Cal Newport, *Deep Work* (protecting focus in a communication-saturated environment).
- Erica Dhawan, *Digital Body Language* (communicating clearly across digital and distributed channels).
- Tsedal Neeley, *Remote Work Revolution: Succeeding from Anywhere*.
- National Institute of Standards and Technology (NIST), Special Publication 800-207, *Zero Trust Architecture*.
- U.S. Office of Personnel Management (OPM), *Guide to Telework in the Federal Government* (public-sector telework policy).
