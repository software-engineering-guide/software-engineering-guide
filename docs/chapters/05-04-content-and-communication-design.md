# 5.4 Content and communication design

## Overview and motivation

Content and communication design is the work of shaping the words, messages, and information a product uses to help people act. It covers [content strategy](https://en.wikipedia.org/wiki/Content_strategy) (what content should exist, for whom, and why), UX writing and microcopy (the labels, buttons, hints, and error messages inside an interface), and the communications that reach users through email, notifications, and other channels. Words are interface. For most software, the content is the product experience far more than the visuals are.

For large teams, content is a coordination and trust problem. When many teams write independently, terminology drifts apart, tone lurches from friendly to bureaucratic screen to screen, and the same concept picks up three different names. Users lose the thread, and they lose confidence. A shared content strategy fixes this. A voice-and-tone guide, a controlled vocabulary, and reusable patterns for errors and empty states do for words what a design system does for pixels: they let independent teams produce a coherent, trustworthy whole.

In enterprise and government, clear content is often a legal and ethical requirement, not a matter of style. [Plain-language](https://en.wikipedia.org/wiki/Plain_language) laws require public communications to be understandable by the people who have to act on them. Poorly worded content in a benefits form, a medical instruction, or a security warning can cause real harm: a missed deadline, a wrong dose, a fraud victim. And in an era of manipulative ["dark patterns"](https://en.wikipedia.org/wiki/Dark_pattern) (interface designs that trick or pressure people into choices against their own interest), how a product presents choices is a matter of trust, safety, and increasingly of regulation.

## Key principles

- Words are UI; content is a core part of the experience, not filler added later.
- Write for the reader's goal and context, in plain language, at the moment they need it.
- Clarity over cleverness; a confused user is not delighted by a witty error message.
- Consistency of terminology and tone reduces cognitive load and builds trust.
- Good defaults and helpful empty states guide people to success.
- Honesty by design: never trick, pressure, or shame users into choices.
- Content should be structured and reusable, not hard-coded and duplicated.
- Design communications for the whole multi-channel journey, respecting attention.

## Recommendations

### Establish a content strategy and voice

Start by deciding who the content is for, what jobs it helps them do, and how it should sound. Write a voice-and-tone guide with concrete examples, and a terminology glossary ([controlled vocabulary](https://en.wikipedia.org/wiki/Controlled_vocabulary)) so the same thing is always called the same thing. Let tone follow context: reassuring in an error, calm in a security warning, celebratory in a success. Voice stays constant; tone flexes. Treat content as a managed asset, with owners, review, and a lifecycle, not as text typed into a field at the last minute.

### Write microcopy that helps people act

Label buttons with the action they perform ("Submit application," not "OK"). Write hints and helper text that head off errors before they happen. Front-load the important words so people scanning the screen still get the point. Use the second person and the active voice. Keep sentences short and specific. Every piece of microcopy should reduce uncertainty about what will happen and what to do next.

### Make plain language the standard, and meet legal requirements

Write at a [reading level](https://en.wikipedia.org/wiki/Readability) that fits your entire audience, not the authors. Prefer common words, short sentences, and concrete instructions; expand jargon and acronyms on first use, or avoid them. In the public sector, plain language is frequently required by law and by policy: follow the applicable plain-language standards, and test comprehension with real users, including people with lower literacy and non-native speakers. Plain language is not "dumbing down." Expert readers prefer clear, efficient text too.

### Design error messages, empty states, and defaults deliberately

An error message should say what went wrong, why, and how to fix it, in plain language, without blame and without codes the user cannot act on. Keep the user's input, and put the message right where the problem is. Empty states are an onboarding opportunity: explain what belongs here and how to add it, instead of showing a blank void. Choose helpful, safe defaults so most users succeed without changing anything, and make the default the option that serves the user's interest, not just the business's.

### Design for trust and safety; avoid dark patterns

Present choices honestly and symmetrically: unsubscribing should be as easy as subscribing, and declining should be as prominent as accepting. Do not use confirmshaming ("No thanks, I don't like saving money"), pre-checked consent, hidden costs, fake urgency, or roach-motel flows that are easy to enter and hard to leave. Beyond the ethics, many of these patterns are now illegal under consumer-protection and privacy law. Take special care with communications about security, privacy, and money, because that is where manipulation does the most harm and where scammers imitate legitimate messaging.

### Design multi-channel communications coherently

Email, push notifications, SMS, and in-app messages are part of one journey. Coordinate them so users are not spammed or contradicted across channels. Respect attention: notify only when it is timely and useful, let users control frequency and channel, and make every message accessible and plain. Ensure transactional communications (receipts, alerts, deadlines) are reliable, clear, and hard to confuse with [phishing](https://en.wikipedia.org/wiki/Phishing): consistent sender identity and formatting help users trust genuine messages.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Centralized content strategy | Consistency, trust, reuse | Overhead, can slow teams if it becomes a bottleneck |
| Plain language everywhere | Comprehension, inclusion, legal compliance | Effort to rewrite; specialists may resist losing jargon |
| Playful, branded voice | Personality, memorability | Can misfire in errors, high-stakes, or diverse audiences |
| Strong defaults | Most users succeed effortlessly | Risk of nudging; must be set in the user's interest |
| Rich multi-channel messaging | Timely, engaging | Easily becomes noise; privacy and consent burden |

The core tension is between brand personality and clarity, and between engagement and respect for attention. Context resolves it. Let voice add warmth where stakes are low, and prioritize plain, calm clarity where stakes are high (errors, money, security, legal). On defaults and messaging, the ethical line is simple: does the design serve the user's genuine interest, or exploit their inattention?

## Questions to discuss with your team

1. **Are error messages, empty states, and defaults shared patterns in our design system, or reinvented on every screen?** These are the highest-leverage moments in the whole experience: a good error says what went wrong, why, and how to fix it without blame or an unactionable code, and a good empty state teaches people what belongs there instead of showing a void. When each team writes these from scratch you get "Error 500" in one place and a helpful message in another, and users lose confidence. Decide whether these patterns live in the design system alongside the components, with agreed structures and example copy. Bring three real error messages and three empty states from your product and read them aloud. If any blames the user or offers no path to recovery, you have found your first backlog item.

2. **Is our content structured and reusable, or hard-coded and duplicated across screens?** Copy typed directly into a component cannot be updated consistently, cannot be reviewed, and cannot be localized without a code change, which quietly blocks every future market and every wording fix. This becomes acute at scale, where the same concept picks up three names because there is no glossary and no single source. Decide how content is stored, who owns the controlled vocabulary, and how a wording change propagates without a deploy per screen. Bring an example of a term your product spells or names inconsistently and trace how many places you would have to edit. If the answer is "search and replace by hand," your content is trapped in code.

3. **When do content designers enter the workflow, and who has authority to block a manipulative flow?** If content is an afterthought (lorem ipsum until launch, then whatever fits the box) the words that carry most of the experience get the least thought, and dark patterns slip in under growth pressure because no one owns honesty. Agree that content is a design input from the start, with a voice-and-tone guide and review in the workflow, and name who can stop a confirmshaming or pre-checked-consent flow before it ships. This is now a legal question as well as an ethical one, because consumer-protection and privacy law increasingly outlaw these patterns. Bring a recent flow and ask whether declining is as easy and as prominent as accepting. If it is not, decide today who is accountable for fixing it.

4. **What reading level are we actually writing to, and how do we know real users understand our highest-stakes content?** Plain language is easy to claim and hard to prove: authors write at their own comprehension level, and the readers who most need clarity, people with lower literacy and non-native speakers, are the least represented in the room. For a large organization the stakes compound, because one confusing benefits letter or security warning is copied to millions of recipients before anyone measures whether it lands. Decide a target reading level for your whole audience, expand or ban jargon on first use, and commit to comprehension testing with real people rather than trusting a readability score alone. Bring your three highest-traffic communications and the evidence that someone outside the authoring team can act on them correctly. In enterprise and government settings, add the applicable plain-language law or policy and be honest about which documents would fail an audit today.

5. **Who governs how, when, and how often we message users across email, push, SMS, and in-app, so the whole journey stays coherent?** When each team owns its own channel, users get spammed, contradicted, and eventually trained to ignore or unsubscribe from everything, including the transactional messages that actually matter. Coordinating the journey means agreeing frequency caps, giving users real control over channel and consent, and holding a consistent sender identity so genuine messages are hard to confuse with phishing that imitates them. Bring a log of every message a single user could receive in a busy week and count the duplicates, the contradictions, and the ones that could be mistaken for a scam. The competing pull is engagement pressure, since growth teams always want another touchpoint and respect for attention has no immediate metric. In enterprise and government contexts, add the consent and privacy obligations that turn unsolicited messaging into legal exposure, and name who can veto a campaign that abuses the channel.

6. **How do we measure whether our content is working, and where does brand voice yield entirely to plain clarity?** Content that is never measured drifts on taste, and the loudest stakeholder wins the wording rather than the user. Tie content to real signals, support-ticket categories, completion and conversion funnels, error and appeal rates, and unsubscribe and complaint rates, so a rewrite is judged by outcome instead of preference. At the same time, agree where voice must give way: a witty error, a jokey money message, or a playful security warning erodes trust exactly when the stakes are highest. Bring a high-traffic flow, the metric it moves, and a proposed line between where personality helps and where calm clarity is mandatory. For a large or public organization, name who owns that line and how a proven improvement propagates across teams, rather than winning one screen and losing the rest.

## Sector lens

**Startup.** With no writer and two engineers, treat content as a founder task, not a hire. Spend a day on the highest-leverage words: name buttons for their action, turn the empty dashboard into a first-run tutorial, and make errors say what to fix. Write a one-page voice guide so the tone stays plain as you grow, and skip the glossary and content platform until inconsistency actually hurts.

**Small business.** With no content designer and a tight budget, lean on the plain-language and microcopy conventions built into the tools you already use, and buy templates for transactional email rather than crafting them from scratch. Prioritize the few screens that lose customers, an empty state, a checkout error, a cancellation flow, and keep declining as easy as accepting so you stay clear of dark-pattern law. Run a free readability checker over anything customer-facing before it ships.

**Enterprise.** The problem is coherence across many teams: a shared voice-and-tone guide, a controlled vocabulary so one concept keeps one name, and error, empty-state, and default patterns that live in the design system beside the components. Store content in version control, structured and localizable rather than hard-coded, give it owners and review, and coordinate multi-channel messaging so users are not spammed or contradicted. Govern honesty centrally so no team ships confirmshaming or pre-checked consent under growth pressure.

**Government.** Plain language is often a legal duty, not a preference, so follow the applicable standards and test comprehension with real recipients, including people with lower literacy and non-native speakers. Lead every notice with the action and the deadline, strip the jargon, and make each communication clearly identify its sender so people do not mistake it for a scam. Keep choices honest and symmetric, publish the content standards you hold yourself to, and give people a plain route to question a decision they do not understand.

## Examples

**Startup.** A small startup with no writers noticed most trial users signed up, saw an empty dashboard, and never came back. One founder spent a day rewriting the microcopy: the empty state now explained what to add and offered a one-click sample project, buttons named their action instead of saying "OK," and error messages said what went wrong and how to fix it. Activation climbed noticeably the next week, and the same founder wrote a one-page voice guide so the whole team would keep the tone plain and consistent as they grew.

**Enterprise.** A SaaS company rewrote its onboarding, error messages, and empty states around clear, action-oriented microcopy and a documented voice guide. Support tickets for "how do I..." questions dropped, activation improved because empty states now taught users what to do, and trial-to-paid conversion rose. The company also removed a confirmshaming cancellation flow after it damaged trust and drew criticism, replacing it with a straightforward, symmetric cancel path, which, counterintuitively, improved reputation and win-backs.

**Government.** An agency rewrote a benefits eligibility letter that recipients routinely misread, causing missed appointments and wrongful loss of benefits. Applying plain-language standards, the team led with the action required and the deadline, removed legal jargon, and tested comprehension with real recipients including non-native speakers. Comprehension rose sharply and missed-deadline rates fell, reducing appeals and casework. Because the letter now clearly identified itself and its sender, recipients were also less likely to mistake it for a scam.

## Business case: motivations, ROI, and TCO

Content quality drives measurable outcomes: higher task completion and conversion, lower support volume, fewer errors and appeals, and greater trust and retention. Clear microcopy and helpful defaults reduce the number of people who get stuck and contact support or abandon. Plain-language communications reduce downstream cost: fewer confused calls, fewer mistakes to correct, fewer appeals in government contexts. Trustworthy, non-manipulative design protects reputation and reduces legal exposure as dark-pattern regulation tightens.

On TCO, the adoption cost is modest: content designers or trained writers, a voice guide and glossary, and review in the workflow. The cost of not adopting is diffuse and large: support and call-centre load, abandoned transactions, error correction, appeals, regulatory penalties for manipulative patterns or non-compliant communications, and eroded trust. These costs land in support and operations rather than the product budget, so leadership tends to underweight them.

To make the case, connect content work to support-ticket categories, completion and conversion funnels, error and appeal rates, and unsubscribe or complaint rates. A small rewrite of a high-traffic flow or a high-volume communication usually produces a clear, attributable improvement, and that is what justifies scaling the practice.

## Anti-patterns and pitfalls

- **Content as an afterthought**: lorem ipsum until launch, then whatever fits the box.
- **Jargon and internal language**: writing from the org's perspective, not the user's.
- **Blaming, unhelpful errors**: "Error 500" or "Invalid input" with no path to recovery.
- **Blank empty states**: a void where guidance should be.
- **Dark patterns**: confirmshaming, pre-checked consent, hidden costs, roach motels, fake urgency.
- **Inconsistent terminology**: three names for one concept across the product.
- **Notification spam**: over-messaging that trains users to ignore or unsubscribe.
- **Untested readability**: assuming content is clear without testing with real users.
- **Hard-coded, duplicated copy**: impossible to update or localize consistently.

## Maturity model

**Level 1: Initiate.** No content practice. Words are written ad hoc by whoever builds the screen, reacting to whatever the box needs at the moment. Terminology and tone are inconsistent, errors blame the user or show unactionable codes, and empty states are a blank void.

**Level 2: Develop.** A style guide or some voice notes may exist, and a few teams have picked up plain-language habits. Content is still a late-stage, per-team activity with little reuse and little testing, so quality and consistency vary widely from one squad to the next.

**Level 3: Standardize.** A content strategy, voice-and-tone guide, and controlled vocabulary are documented and used across teams. Plain language is the standard and, where required, compliant; errors, empty states, and defaults follow shared patterns; content is structured, reviewed, and reusable rather than hard-coded per screen.

**Level 4: Manage.** Content is measured against outcomes with data. Readability and comprehension-test results, support-ticket categories, completion and conversion funnels, error and appeal rates, and unsubscribe and complaint rates are tracked against baselines, and each content change is judged on whether it moves those numbers. Dark patterns are audited against a documented policy, and multi-channel message frequency is monitored against agreed caps.

**Level 5: Orchestrate.** Content is continuously improved and integrated across the organization. Patterns live in the design system, localized and accessible by default; the controlled vocabulary keeps one name per concept everywhere; multi-channel communications are coordinated and user-controlled; and the practice adapts as regulation, audience, and channels shift, retiring and rewriting content on evidence rather than opinion.

## Ideas for discussion

- Where should brand voice yield entirely to plain clarity, and who decides the line?
- How do you enforce a no-dark-patterns policy when growth teams are pressured on metrics?
- How do you keep terminology consistent across many teams without bottlenecking them?
- What reading level is right for a service used by the entire public?
- How should notification frequency and channel control be governed across the organization?
- How do you make genuine communications distinguishable from phishing that imitates them?

## Key takeaways

- Content is core UI; design words with the same rigour as visuals.
- Plain language improves comprehension for everyone and is often legally required.
- Errors, empty states, and defaults are high-leverage moments: design them to help.
- Avoid dark patterns: present choices honestly and symmetrically; they are increasingly illegal.
- Consistent terminology and tone build trust and reduce cognitive load.
- Coordinate multi-channel communications and respect user attention and control.
- Content quality shows up directly in support volume, completion, errors, and trust.

## References and further reading

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson and Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton and Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (dark patterns research)
- U.S. Federal Plain Language Guidelines and PlainLanguage.gov
- UK Government Digital Service, content design and style guidance
- Nielsen Norman Group, articles on error messages, microcopy, and readability
