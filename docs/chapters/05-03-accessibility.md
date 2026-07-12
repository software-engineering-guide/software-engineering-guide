# 5.3 Accessibility

## Overview and motivation

[Accessibility](https://en.wikipedia.org/wiki/Accessibility) (often shortened to "a11y") is the practice of building software that people with disabilities can perceive, understand, navigate, and use. That includes people who are blind or have low vision, who are deaf or hard of hearing, who have motor impairments, who have cognitive or learning differences, and who face temporary or situational limits such as a broken arm, bright sunlight, or a noisy room. Roughly one in five people has a disability, and everyone benefits from accessible design at some point. This is not a niche accommodation. It is a baseline of quality.

For large teams, accessibility has to be built into the system, not left to individual good intentions. When many teams ship into one product, a single inaccessible component (an unlabelled form field, a colour-only status indicator, a keyboard trap in a modal) can lock disabled users out of an entire journey. Building accessibility into shared components, design tokens, testing pipelines, and definitions of done is the only way to make it reliable at scale. Retrofitting it after the fact is expensive and error-prone. Designing it in is cheap and durable.

For government, accessibility is a legal requirement and a civic obligation, not a nice-to-have. Public services must serve every member of the public, and disabled citizens often have no alternative provider: if the government website is inaccessible, they cannot get their benefit, licence, or vote another way. Laws and standards around the world make accessibility mandatory for public bodies, and increasingly for the private sector too. This chapter treats accessibility as three things at once: a legal duty, an ethical duty, and simply good design.

*See also:* chapter 5.2 (UI design and design systems), chapter 5.6 (frontend engineering), and chapter 5.1 (UX foundations).

## Key principles

- Accessibility is a baseline quality attribute, like security and performance, not an optional feature.
- The POUR principles: interfaces must be Perceivable, Operable, Understandable, and Robust.
- [Semantic HTML](https://en.wikipedia.org/wiki/Semantic_HTML) first; use [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) only to fill genuine gaps, never as a substitute for native elements.
- Everything usable with a mouse must be usable with a keyboard alone.
- Do not convey information by colour, shape, or position alone.
- Automated tools catch only a fraction of issues; manual and [assistive-technology](https://en.wikipedia.org/wiki/Assistive_technology) testing are essential.
- Accessible design is better design for everyone (the ["curb-cut effect,"](https://en.wikipedia.org/wiki/Curb_cut) where features built for disabled people benefit all users).
- Design and test with disabled people, not just for them.

## Recommendations

### Design and build to WCAG, targeting the current standard

The [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) are the international reference. WCAG 2.1 and 2.2 are organized under the four POUR principles, with testable success criteria at conformance levels A, AA, and AAA. Target Level AA as your baseline; it is what most laws reference. WCAG 2.2 adds criteria for focus visibility, target size, and reducing cognitive load. WCAG 3.0 is an emerging successor, structured differently and still in development. Keep an eye on it, but build to 2.2 AA today. Treat the guidelines as a floor, not a ceiling: passing every criterion does not guarantee a genuinely usable experience.

### Use semantic HTML and correct ARIA

Native HTML elements (buttons, links, form controls, headings, lists, landmarks) come with built-in accessibility semantics, keyboard behaviour, and assistive-technology support. Use them first. Reach for ARIA (Accessible Rich Internet Applications) roles, states, and properties only to describe custom widgets that HTML cannot express, and follow the ARIA Authoring Practices. The first rule of ARIA is simple: don't use ARIA if a native element will do. Incorrect ARIA is worse than none: it actively misleads [screen readers](https://en.wikipedia.org/wiki/Screen_reader). Give the page a logical heading structure, meaningful labels, alternative text for images, captions and transcripts for media, and a programmatic link between each label and its control.

### Guarantee keyboard and assistive-technology operability

Every interactive element must be reachable and operable with the keyboard alone, in a logical order, with a clearly visible focus indicator. Avoid keyboard traps. Manage focus deliberately when content changes: move focus to a dialog when it opens, return it when the dialog closes, and announce dynamic updates through live regions. Test with real assistive technologies, including screen readers on desktop and mobile, screen magnification, voice control, and switch access. And respect user preferences such as reduced motion and increased contrast.

### Test with automated tools, manual review, and real users

Automated accessibility scanners are valuable, and they should run in the pipeline on every change. But studies consistently show they catch only a minority of real issues, roughly a third. The rest need human judgment: keyboard walkthroughs, screen-reader testing, contrast checks, and asking whether the content is actually understandable. Most important of all, include people with disabilities in usability testing. Build accessibility acceptance criteria into the definition of done, so issues get caught per story rather than in a pre-launch audit.

### Make accessibility organizational, not heroic

Bake accessibility into the design system so components ship accessible by default. Offer training so designers, engineers, content authors, and product managers each know what they are responsible for. Establish an accessibility standard, an owner or centre of excellence, and a remediation process. Publish an accessibility statement and give users a way to report barriers. And procure accessibly: require vendors and third-party components to conform, and to provide evidence (such as an accessibility conformance report).

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Build accessibility in from the start | Cheapest, durable, better for everyone | Requires upfront training and discipline |
| Retrofit / remediate later | Defers effort, unblocks a quick launch | Far more expensive, fragile, legal exposure in the interim |
| Automated testing only | Fast, cheap, catches regressions in CI | Misses ~two-thirds of issues; false confidence |
| Manual + assistive-tech testing | Catches real usability barriers | Slower, needs skilled testers and devices |
| Testing with disabled users | Ground truth on real experience | Recruiting effort and cost, must be done respectfully |

The central trade-off is upfront discipline versus deferred cost. Accessibility built in is inexpensive and improves quality for everyone; accessibility retrofitted under legal pressure is expensive, incomplete, and stressful. In the long run there is no real trade-off against "speed": inaccessible software simply does not work for a fifth of your users. That is a defect, not a saving.

## Questions to discuss with your team

1. **Do accessibility regressions fail our build the way a broken test does, and if not, why not?** Automated scanners catch only about a third of issues, but the ones they do catch (missing labels, contrast failures, unlabelled controls) are cheap to catch in CI and expensive to find in a pre-launch audit. Treating a regression as a build failure is what moves accessibility from heroic individual effort to a reliable system property, which is the only thing that works when many teams ship into one product. Decide which checks are blocking, which are advisory, and who can override a failure. Bring your current scanner results and your definition of done to the meeting. If accessibility criteria are not written into the definition of done per story, they will be deprioritized the moment a deadline tightens.

2. **What is our rule for custom widgets, and who reviews the ARIA before it ships?** Native HTML elements come with keyboard behaviour and assistive-technology support for free, and incorrect ARIA is worse than none because it actively misleads screen readers. Agree that semantic HTML is the default and that any custom widget (a bespoke dropdown, date picker, or modal) requires a keyboard and screen-reader walkthrough before merge, following the ARIA Authoring Practices. This matters most for the interactive components many teams reuse, because one broken modal with a keyboard trap can lock disabled users out of an entire journey. Bring a list of your custom widgets and ask which have been tested with an actual screen reader. Any that have not are liabilities hiding in shared code.

3. **What is our policy on accessibility overlays, and does anyone believe they are a real fix?** Overlays are marketed as a one-line script that makes a site conformant, and they are tempting when legal pressure arrives and a deadline looms. They do not deliver genuine conformance, they can worsen the experience for assistive-technology users, and for government they leave the underlying legal duty unmet. Decide explicitly that you will invest in semantic markup, keyboard support, and testing with disabled people rather than buy a widget that papers over the problem. Bring the cost of an overlay subscription and compare it against building accessibility into your components and pipeline once. Framing this early prevents a panicked procurement decision later that spends money and fixes nothing.

4. **Are disabled people part of our design and testing, or are we still designing for an imagined user we invented?** Automated scanners and even expert audits tell you whether markup conforms; they do not tell you whether a blind user can actually finish your checkout or a person with a cognitive disability can understand your error messages. Involving disabled participants is the only source of ground truth, and it changes what you build, but it raises real questions about how you recruit fairly, how you compensate people for their time, and how you avoid treating one participant as a spokesperson for every disability. Bring your current research roster, your recruitment and payment practices, and an honest count of how many studies in the last year included disabled participants. For a large organization, a recurring panel with fair compensation and coverage across vision, hearing, motor, and cognitive needs is what turns this from a one-off gesture into a dependable input; in government, involving the public you serve is often part of the legal and civic obligation, not an optional nicety.

5. **When we buy or embed a third-party component, do we require proof of accessibility, and who checks it?** Much of what ships in a large product is not written in-house: a date picker from a library, a payments widget in an iframe, a charting package, a whole SaaS module. A single inaccessible embedded component can fail an entire journey no matter how clean your own code is, and once it is wired in, replacing it is expensive. Decide that accessibility is a procurement requirement, that vendors must supply an accessibility conformance report (a document such as a VPAT that states how a product measures against WCAG), and that someone technical validates the claim rather than filing it. Bring an inventory of your third-party components and ask which have current, credible conformance evidence. In enterprise and government purchasing, write WCAG 2.2 AA conformance and a right to remediation into the contract, because a promise made before signing is far cheaper to enforce than a barrier discovered after go-live.

6. **What is our target conformance level, who owns it, and how do we keep it current as standards move?** WCAG 2.2 AA is today's floor and most laws reference it, but 2.2 added criteria many teams have not adopted, and WCAG 3.0 is coming with a different structure. Without a named owner, the standard drifts: different teams target different versions, nobody tracks the gap, and conformance quietly rots between audits. Decide the exact version and level you build to, who has authority to raise it, and how new criteria reach the design system and the definition of done. Bring your current stated target, evidence of where teams actually meet it, and a short roadmap for adopting 2.2 criteria you have skipped. For a large or public organization, an accessibility owner or centre of excellence, a published accessibility statement, and a documented plan for the next standard version are what let you answer a regulator or a court with evidence rather than good intentions.

## Sector lens

**Startup.** Speed favours you here, because accessibility is cheapest when the codebase is small. Add an automated scanner to CI and a keyboard walkthrough to your pull-request checklist from the first sprint, and lean on semantic HTML so you get keyboard and screen-reader support for free. Skip overlays and heavy tooling; the payoff is that when a customer's procurement team asks for a conformance report mid-sale, you can answer in days instead of scrambling.

**Small business.** With no accessibility specialist and a tight budget, buy accessibility rather than build it: choose a platform, theme, or component library that already conforms and states so, and prefer vendors who publish an accessibility statement. Cover the high-value basics yourself with free tools, keyboard-only checks, a contrast checker, and clear labels on every field, because those catch the failures that most often exclude customers. Treat a wrong or unusable automated flow as a lost customer, since a small business rarely offers an assisted channel to fall back on.

**Enterprise.** At scale the work is making accessibility a system property across many teams. Ship accessible components by default in the design system, gate regressions in CI, and stand up an owner or centre of excellence with a remediation process and training for designers, engineers, and content authors. Track conformance over time as a metric, write WCAG conformance into procurement, and manage third-party components as a portfolio so one embedded widget cannot quietly fail a shared journey.

**Government.** Accessibility is a legal mandate and a civic duty, since disabled citizens often have no alternative provider for a benefit, licence, or vote. Build to the standard your jurisdiction cites (for example Section 508, EN 301 549, or the European Accessibility Act mapped to WCAG 2.2 AA), publish an accessibility statement with a route to report barriers, and test with the disabled public you serve. Reject overlays as a substitute for real conformance, and require vendors to supply credible evidence and a right to remediation in the contract.

## Examples

**Startup.** A three-person startup building a hiring tool added an accessibility scanner to their build and a quick keyboard walkthrough to their pull-request checklist from the very first sprint, reasoning it was cheaper to stay accessible than to fix it later. When a mid-size customer's procurement team asked for an accessibility conformance report during a sales cycle, the startup already used semantic HTML, labelled every field, and had visible focus everywhere, so they answered in days instead of scrambling. That readiness won a deal that a competitor lost on the same requirement.

**Enterprise.** A large retailer faced a class-action lawsuit because blind customers could not complete checkout with a screen reader. Beyond the settlement and legal fees, the company had to remediate under a court-supervised timeline. Afterward it rebuilt accessibility into its design system and CI pipeline, added screen-reader testing to the definition of done, and trained its teams. The rebuilt, accessible checkout also improved conversion and reduced support contacts for everyone: the fixes that helped screen-reader users (clear labels, error messages, logical order) helped all users.

**Government.** A public benefits agency was legally required to meet WCAG 2.1 AA for its online application. Early testing with blind and low-vision users, keyboard-only users, and users with cognitive disabilities revealed that a colour-only "required field" indicator, an inaccessible date picker, and unannounced validation errors were blocking people from finishing. Fixing these, through semantic markup, visible focus, live-region error announcements, and [plain-language](https://en.wikipedia.org/wiki/Plain_language) help, let disabled citizens apply on their own for the first time. That reduced reliance on in-person help and lowered cost to serve, while meeting the legal mandate.

## Business case: motivations, ROI, and TCO

The business case rests on market reach, legal risk, cost to serve, and quality. Disabled people and their families control significant spending power; excluding them forfeits it. Accessible services reduce the need for expensive assisted channels (phone and in-person help), which is a direct operational saving, especially for government. And because accessibility improvements (clear labels, keyboard support, readable content, robust markup) help everyone, they typically raise overall completion and satisfaction.

On TCO, the adoption cost is training, tooling, and building accessibility into components and pipelines, all modest when you do it from the start. The cost of not adopting is severe and comes from several directions: legal liability (lawsuits, settlements, court-ordered remediation, regulatory penalties), the far higher expense of retrofitting under deadline pressure, reputational damage, and the ongoing cost of serving excluded users through more expensive channels. Retrofitting typically costs several times what designing-in would have.

To make the case to leadership, lead with the legal obligation where it applies (it is non-negotiable for government and increasingly for the private sector). Then quantify the addressable population you are excluding, the assisted-channel cost of that exclusion, and the "curb-cut" gains for all users. Position accessibility as risk management plus quality, not charity.

## Anti-patterns and pitfalls

- **Accessibility as a pre-launch checkbox**: an audit at the end instead of continuous practice, guaranteeing expensive last-minute rework.
- **"Div soup"**: non-semantic markup with click handlers on generic elements, invisible to assistive technology.
- **ARIA misuse**: bolting ARIA onto broken markup, which misleads screen readers more than plain markup would.
- **Colour-only information**: status shown by colour alone, invisible to colour-blind users.
- **Invisible focus**: removing focus outlines for aesthetics, stranding keyboard users.
- **Keyboard traps**: modals and widgets that trap or lose focus.
- **Automated-scan complacency**: passing a scanner and assuming the product is accessible.
- **Accessibility overlays**: third-party "one-line fix" widgets that do not deliver real conformance and can worsen the experience.
- **Excluding disabled users from research**: designing for an imagined disabled user instead of testing with real ones.

## Maturity model

**Level 1: Initiate.** No accessibility practice. Issues are discovered only when a user complains or a lawsuit arrives, and response is reactive. Markup is non-semantic and untested, and no one owns the problem.

**Level 2: Develop.** Awareness exists and some teams act on it: an automated scanner in a build here, a keyboard walkthrough there, a pre-launch audit before a big release. Practice is basic and inconsistent across teams, accessibility is still a late-stage checklist, and it is frequently deprioritized under schedule pressure.

**Level 3: Standardize.** WCAG 2.2 AA is the documented standard, enforced organization-wide. Accessibility is built into the design system so components ship accessible by default, tested automatically and manually, and written into the definition of done. Teams are trained, an owner or centre of excellence exists, and a remediation process is defined.

**Level 4: Manage.** Accessibility is measured and controlled with data against baselines. The organization tracks conformance metrics over time (scanner pass rates, the count of open barriers by severity, screen-reader test coverage of critical journeys, and time-to-remediate), reports them per team on a dashboard, and treats regressions as build failures rather than advisory warnings. Targets are set against a baseline and progress is reviewed, so a team that slips is visible before an audit finds it.

**Level 5: Orchestrate.** Accessibility is continuously improved and integrated across the organization. Disabled people are part of research and testing on a recurring basis, and accessibility is embedded in procurement, design tokens, and CI. The organization adapts as standards move (adopting new WCAG criteria and preparing for WCAG 3.0), and it influences vendors and partners so the whole supply chain conforms.

## Ideas for discussion

- How do you keep accessibility from being deprioritized when deadlines tighten?
- What is the right mix of automated, manual, and user testing for your risk profile?
- How should accessibility conformance be written into vendor contracts and procurement?
- How do you handle the gap between WCAG conformance and genuine usability for disabled people?
- How should teams prepare for WCAG 3.0 while building to 2.2 today?
- How do you fairly and respectfully recruit and compensate disabled participants for research?

## Key takeaways

- Accessibility is a baseline quality attribute and, for government, a legal requirement.
- Design to WCAG 2.2 AA as a floor; use the POUR principles as a mental model.
- Semantic HTML first; ARIA only to fill real gaps, done correctly.
- Automated tools catch about a third of issues; manual and assistive-technology testing are essential.
- Test with disabled people, not just for them.
- Building accessibility in is cheap and durable; retrofitting is expensive and fragile.
- Accessible design is better design for everyone: the curb-cut effect is real.

## References and further reading

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
