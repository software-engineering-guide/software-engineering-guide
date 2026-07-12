# 5.10 Data visualization design

## Overview and motivation

A chart is an argument made of ink. When you plot data, you are choosing what a reader will notice first, what they will compare, and what conclusion they will reach in the two seconds before they move on. Do it well and a hard question answers itself: the trend is obvious, the outlier jumps out, the two groups clearly differ. Do it badly and the same data misleads, confuses, or simply bores, and the decision it was meant to inform gets made on vibes instead. [Data visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization) is the design craft of turning numbers into pictures that let people see what the numbers mean.

This chapter is about that craft: choosing the right chart, encoding data honestly, using colour and layout so the eye lands where it should, and keeping the whole thing accessible. It sits inside Part 5 because a chart is an interface, and it inherits everything from the rest of the part. It builds on the [user experience](https://en.wikipedia.org/wiki/User_experience) (UX) foundations of chapter 5.1, borrows tokens and components from the design systems of chapter 5.2, must satisfy the accessibility duties of chapter 5.3, and speaks in the plain, purposeful voice of the content design in chapter 5.4. It deliberately stays out of the plumbing. The data pipelines, warehouses, and reporting tools of analytics and business intelligence (chapter 7.3) are a different subject, as is the broader decision science and data culture of chapter 7.5. Here you learn how to make the picture good, wherever the data comes from.

For large teams, the stakes are coordination and trust. When every squad styles its own charts, a company ends up with fifty dialects of "revenue over time," each with different axes, colours, and rounding, and executives learn to distrust all of them. In enterprise settings, a misleading dashboard drives real budget the wrong way. In government, a public chart is an act of communication with citizens and a matter of the stakeholder communication in chapter 10.16: a truncated axis on a public-health graphic can panic or falsely reassure millions, and accessibility is a legal duty, not a preference. Good visualization design is how data earns the right to be believed.

## Key principles

- Start from the question the reader has, then pick the chart that answers it.
- Match the visual encoding to the data type: position for precise comparison, hue for categories.
- Maximize the share of ink that carries data; delete decoration that carries none.
- Use pre-attentive attributes deliberately so the eye lands on the point first.
- Choose palettes by data role (sequential, diverging, categorical) and keep them colour-blind-safe.
- Never rely on colour alone; provide text, structure, and a table fallback.
- Tell the truth about scale: no truncated axes, no misleading areas, no gratuitous dual axes.
- Annotate the insight; do not make the reader hunt for it.

## Recommendations

### Start from the question, then choose the chart

Every good chart begins with a question, not a dataset. Before you reach for a chart type, name the reader's question in one sentence, then match it to a task. Comparison ("which is bigger?") wants a [bar chart](https://en.wikipedia.org/wiki/Bar_chart), where lengths sit on a common baseline and the eye ranks them effortlessly. Trend over time ("which way is it going?") wants a [line chart](https://en.wikipedia.org/wiki/Line_chart), because a connected line reads as continuous change. Distribution ("how is it spread?") wants a histogram or box plot, which show shape, centre, and outliers. Part-to-whole ("what share is each piece?") is usually served better by a stacked bar than a pie, because people compare lengths far more accurately than angles; reserve the [pie chart](https://en.wikipedia.org/wiki/Pie_chart) for two or three slices where the split is the whole story. Relationship ("do these two move together?") wants a [scatter plot](https://en.wikipedia.org/wiki/Scatter_plot), the one chart that reveals correlation and clusters at a glance.

The discipline is to let the question pick the chart, never the reverse. A chart type chosen because it looks impressive (a 3D exploded pie, a radar chart, a donut with a number in the hole) is a decision made for the designer's benefit, not the reader's. When a table would answer the question faster (a reader who needs exact figures for four rows does not need a chart at all), use the table. The chart is justified only when a picture reveals a pattern that digits on a grid would hide.

### Match visual encoding to the data

A chart works by mapping data to visual properties, and those properties are not equal. Decades of perception research rank them. Position along a common scale is the most accurate channel humans have, which is why bars and dots on a shared axis beat everything else for comparison. Length comes next, then angle and slope, then area, then colour intensity, and finally hue, which is nearly useless for judging quantity but excellent for labelling categories. Spend your most precise channel on your most important quantity.

Match the channel to the data type too. Quantitative data (counts, amounts, durations) belongs on position, length, or a sequential colour ramp. Ordinal data (small, medium, large) can use ordered size or a light-to-dark ramp. Categorical data (region, product line, party) belongs on hue or shape, never on a size that implies one category is "more" than another. The classic error is encoding a category as a rainbow so that the reader's eye invents an order that the data does not have. Encode quantity where the eye reads quantity, and identity where the eye reads identity.

### Pursue graphical excellence: maximize data-ink

Edward Tufte gave visualization its clearest design ethic, and it is worth internalizing. His central measure is the [data-ink ratio](https://en.wikipedia.org/wiki/Data-ink_ratio): of all the ink (or pixels) on the page, what fraction actually encodes data? Everything else (heavy gridlines, boxed borders, drop shadows, background fills, redundant legends, decorative 3D) is a tax on the reader's attention. Tufte calls this decoration chartjunk, and the instruction is blunt: erase it. Lighten gridlines until they whisper, drop the chart border, label data directly instead of forcing a trip to a legend, and let the data stand almost alone. A chart is finished not when there is nothing left to add but when there is nothing left to remove without losing meaning.

One Tufte idea earns special mention for teams: small multiples. Instead of cramming eight series into one tangled line chart, draw eight small charts in a grid, each with the same axes and scale, one per series. The eye scans the grid and spots the odd one out instantly, because every panel is directly comparable. Small multiples turn "too many lines to read" into "a page you can skim," and they scale far better than piling more colour and more legend entries onto a single overloaded plot.

### Use pre-attentive attributes and visual hierarchy

Some visual differences register before conscious attention, in a fraction of a second, without the reader "looking for" them. These pre-attentive attributes (a single red dot among grey ones, one longer bar, one item set apart in space) are the most powerful tool you have for directing the eye. Use them on purpose. If the point of the chart is that one region is falling behind, colour that region and grey the rest; the reader sees the message before they read the title. If everything is bright and bold, nothing is, because contrast is relative and a page of emphasis is a page of noise.

This is visual hierarchy applied to data: decide the one thing the reader should notice first, and spend your strongest signal there. Title and annotation state the takeaway in words. Colour and weight point to the evidence. Everything supporting (axes, gridlines, secondary series) recedes to grey so the foreground can speak. A chart without hierarchy asks the reader to do the designer's job of figuring out what matters.

### Choose colour by role, and make it colour-blind-safe

Colour is the channel most often misused, so treat it as a system with three families. A sequential palette runs light to dark in one hue and encodes quantity that goes from low to high (population density, revenue). A diverging palette has two hues meeting at a neutral midpoint and encodes deviation from a centre (temperature anomaly, profit and loss around zero, survey agreement around neutral). A categorical palette is a set of distinct hues for labelling groups with no order; keep it to roughly seven colours, because beyond that the reader cannot tell them apart. Picking the wrong family (a categorical rainbow for a quantity, a sequential ramp for unordered categories) fights the reader's perception.

Then make it accessible, because roughly one in twelve men has some form of [colour blindness](https://en.wikipedia.org/wiki/Color_blindness). Red and green are the classic trap: a red-bad, green-good chart is invisible to the most common deficiency. Choose colour-blind-safe palettes (blue-to-orange diverging schemes and the well-tested categorical sets from tools like ColorBrewer are safe starting points), and verify by simulating the common deficiencies before you ship. Check contrast too, so that text and marks meet the ratios required by the accessibility standards in chapter 5.3. Colour should reinforce a message that already survives without it.

### Do not rely on colour alone; provide alternatives

Accessibility in data viz goes past palette choice. The core rule from the [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) is that colour must never be the only way information is conveyed. So pair colour with a second cue: direct labels, distinct shapes or markers on a scatter, different line styles (solid, dashed) on a line chart, or a text label on the important bar. A reader who cannot distinguish your hues should still get the full message from the redundant encoding.

Provide a genuine text alternative and a fallback. A chart image needs alt text that states the takeaway, not "chart of sales," and a longer description or a caption that names the trend. Wherever practical, offer the underlying data as an accessible table, so a screen-reader user and a spreadsheet-minded analyst both get the numbers directly. This mirrors the "solve it once in a component" discipline of chapter 5.2: build accessible chart components with proper roles, keyboard focus for interactive elements, and a table view built in, so every team inherits accessibility rather than reinventing it per dashboard.

### Know whether you are exploring, explaining, or monitoring

Charts serve three different jobs, and confusing them produces bad work. Exploratory visualization is for you, the analyst, hunting through data for what is interesting; it can be fast, dense, and ugly, because the audience is one expert who will iterate. Explanatory visualization is for an audience, communicating a specific finding you already understand; it is deliberate, annotated, and stripped to a single message, and it belongs in the storytelling of chapter 10.16. A dashboard is a third thing: a persistent, glanceable display for monitoring known metrics over time, optimized for "is anything wrong right now?" rather than for a one-time argument.

Match the design to the job. An explanatory chart with a headline and one highlighted series is wrong for a monitoring dashboard, where the reader needs many metrics at a glance and consistent placement so their eye learns the layout. A dashboard crammed with narrative annotation is exhausting to check every morning. And an exploratory notebook full of raw plots should never be handed to an executive as if it were an explanation. Decide the job first; the design follows.

### Never mislead: honest scales, honest areas

The fastest way to destroy trust is a chart that lies while looking truthful. The most common lie is the truncated axis: starting a bar chart's y-axis at 90 instead of 0 turns a 2% difference into a cliff, because bar length no longer maps to value. Bars must start at zero, always; line charts, which encode change rather than magnitude, may use a non-zero baseline if you label it clearly. The second trap is the dual axis: two y-scales on one chart let you manufacture any correlation you like by sliding the scales, and readers rarely notice. Prefer two aligned charts or an indexed view instead. The third is misleading area: when you scale an icon or bubble by both width and height to represent a value, the area grows as the square and wildly overstates the difference; scale by area, not by side length.

Treat these as integrity rules, not style preferences. A chart is a claim you are asking the reader to trust, and every one of these distortions exploits how perception works to make a small thing look big or an unrelated thing look linked. The government and enterprise examples below show how expensive that betrayal becomes when the audience is the public or the board.

### Annotate the insight and add interactivity with restraint

A chart that makes the reader find the point is only half done. Annotate it: a title that states the finding ("Signups doubled after the March launch") rather than the topic ("Signups over time"), a callout on the key event, a reference line for the target or the average. Annotation is where the design in chapter 5.4 meets the picture; the words carry the argument and the marks provide the proof.

Interactivity earns its place only when it answers a real follow-up question. Tooltips for exact values, filtering to a segment, and drill-down into a detail all help when the reader has a next question the static chart cannot hold. But interactivity is a cost: it hides information behind a hover, fails on touch and for keyboard users, and can drag performance to a crawl. On the web, watch the render budget from chapter 5.6: tens of thousands of points want canvas or an aggregated view, not tens of thousands of individual document elements. Make the default, static view tell the whole core story, and let interaction reveal the depth beneath it.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Build viz in your product | Full control of design, accessibility, interaction | Costs engineering time; you own performance and maintenance |
| Use a BI tool's charts | Fast, cheap, connected to the warehouse | Generic look; limited accessibility and annotation control |
| Interactive charts | Answers follow-up questions; explore in place | Slower, harder to make accessible, fails on print and touch |
| Static charts | Fast, accessible, print-ready, unambiguous | Cannot answer the reader's next question |
| Dashboard | Glanceable monitoring of many known metrics | Poor for a one-time argument; tempts metric sprawl |
| Explanatory chart | Delivers one message with force | Wrong for monitoring or open-ended exploration |
| Rich colour and effects | Eye-catching; feels polished | Chartjunk; hurts data-ink ratio and accessibility |

The recurring tension is expressiveness versus honesty and clarity. Every feature that makes a chart richer (a second axis, a colour gradient, a 3D perspective, an animation) also adds a way to mislead or to bury the point. Resolve it by defaulting to less: the simplest chart that answers the question, in the fewest colours, with the scale that tells the truth. Add expressiveness only when a specific reader question demands it, and pay the accessibility and performance cost knowingly. The other standing trade-off is build versus buy. A BI tool gets a chart on a screen in minutes and is the right choice for internal monitoring; a viz embedded in a customer-facing product usually needs the design, accessibility, and performance control that only a purpose-built component gives you.

## Questions to discuss with your team

1. **Do our charts share one visual language, or does every team invent its own?** When each squad picks its own colours, axis conventions, rounding, and chart types, the organization accumulates dialects that quietly undermine trust: two dashboards showing "active users" with different scales and different greens teach executives that the data cannot be relied on. Bring three charts of the same metric from three teams and lay them side by side. The gaps you find (a truncated axis here, a rainbow of categories there, revenue in thousands on one and millions on another) are the argument for a shared chart component library with agreed palettes, default axis rules, and accessibility built in, governed like the design system in chapter 5.2. The goal is that any chart in the company reads correctly on sight, because the grammar is shared.

2. **Would our most important charts survive a colour-blind reader and a screen reader?** Accessibility in data viz is easy to skip because the charts still look fine to the people who built them, and that is exactly the trap. Take the three charts your leadership sees most often and run them through a colour-blindness simulator, then try to understand them with the screen off, using only the alt text and any table fallback. If a red-green status chart goes flat, if the alt text says "chart" and nothing more, or if there is no way to reach the underlying numbers without a mouse, you have found a group of readers you are currently excluding, which in public-sector work is a legal exposure under the standards in chapter 5.3. Decide who owns fixing it and whether the fix belongs in a shared component so it is solved once.

3. **For each chart that drives a decision, can we point to the question it answers and confirm it does not mislead?** Many charts exist because someone once made them, not because they answer a live question, and some of the most-watched ones distort scale without anyone noticing. Walk through the charts on your main dashboards and, for each, name the decision it informs and check its integrity: bars from zero, no gratuitous dual axis, areas scaled honestly, a title that states a finding rather than a topic. The charts that answer no current question are candidates for deletion, and the ones that mislead are candidates for urgent repair, because a chart that quietly overstates a difference is worse than no chart at all. This connects directly to the decision culture of chapter 7.5: a team that trusts its charts makes faster, better-grounded calls.

4. **When a team needs a chart, do we reach first for the BI tool's built-in charts or for a governed component library, and who decides which?** The pull towards the BI tool is real: it is fast, cheap, and already wired to the warehouse, so most monitoring dashboards belong there. But its generic defaults are where dialects and chartjunk creep in, and its accessibility and annotation controls are usually weak, which matters most for the customer-facing and public charts that carry your reputation. For a large organization the danger is that the default is never decided, so each team drifts to whatever is easiest and the estate fragments. Bring an inventory of where charts are actually built today, a few side-by-side examples from the BI tool versus a purpose-built component, and the accessibility gaps in each. In enterprise and government settings, fold in the procurement reality: you are often locked into one BI platform for years, so know exactly which charts it can render honestly and accessibly and which need a governed component, before the contract, not after.

5. **Who is allowed to publish a chart to an external or executive audience, and what review does it pass first?** Self-serve analytics is a genuine good, but it means a misleading chart can reach the board or the public without a second pair of eyes, and a truncated axis or an unlabelled spike on a public graphic is far harder to unwind than to prevent. The tension is speed and autonomy against integrity and trust: gate too hard and people route around you, gate too little and you ship the chart that panics a market or a constituency. Bring the current publishing path for your most visible charts, examples that reached an outside audience without review, and evidence of whether method and uncertainty are annotated on the chart itself. In public-sector and regulated work this is acute: an official statistic is a communication with citizens and a matter of the stakeholder trust in chapter 10.16, so name who signs off, what integrity and accessibility checklist they apply, and where the accountability sits when a chart misleads.

6. **Where have we added interactivity, and does the default static view still tell the whole story without a mouse?** Interactivity is seductive and expensive: it hides values behind a hover, breaks on touch and for keyboard users, and can drag the render budget to a crawl on large datasets, as chapter 5.6 warns. The competing consideration is that a real follow-up question (an exact value, a drill-down, a filtered segment) is sometimes worth the cost, so the aim is restraint rather than prohibition. Bring the list of interactive charts you ship, the results of trying each one with the mouse away and on a phone, and the performance numbers when the data grows to tens of thousands of points. For enterprise and government audiences the accessibility angle is a legal duty under the standards in chapter 5.3, and charts are read on kiosks, printouts, and assistive technology, so the static, annotated default has to carry the core message and interaction can only add depth beneath it.

## Sector lens

**Startup.** Speed wins, so lean on the charts already inside your BI tool or a lightweight charting library rather than building a viz component estate you cannot staff. The one cheap decision that pays off later is to pick a single colour-blind-safe palette and a bars-from-zero habit on day one, so you do not accumulate a dozen dialects of the same metric before you have ten customers. Prefer a static, annotated chart that states its finding over an interactive one you will not have time to make accessible.

**Small business.** With no data specialist and a tight budget, treat visualization as something you get from tools you already pay for: the spreadsheet, the analytics SaaS, the dashboard in your CRM. Learn the handful of integrity rules that matter (bars start at zero, no rainbow for a quantity, no pie with nine slices) and apply a ready-made colour-blind-safe palette rather than commissioning a custom one. Buy the chart, do not build it, and reserve your attention for reading it correctly.

**Enterprise.** The problem is consistency across many teams, so govern visualization like a design system: a shared chart component library with agreed sequential, diverging, and categorical palettes, honest axis defaults, standard number formatting, and accessibility baked in. Enforce it with visual-regression and integrity checks in the delivery pipeline of chapter 8.1, so a chart that truncates an axis or fails contrast is blocked before it ships. The payoff is that a chart from any team reads correctly on sight and leadership stops asking which version of a number to believe.

**Government.** Every public chart is an act of communication and subject to public accountability, so honest scales and WCAG accessibility are duties, not preferences. Mandate bars from zero, area encoded by area, colour-blind-safe palettes, plain-language titles that state the finding, and a downloadable accessible table beside every chart. Annotate method and uncertainty on the chart itself so a controversial figure cannot be reduced to a misleading headline, and make sure any BI tool you procure can meet these standards, since the obligation is yours regardless of the vendor.

## Examples

**Startup.** A ten-person analytics startup ships a customer-facing usage dashboard. The first version uses a BI tool's default theme: a rainbow of category colours, gridlines everywhere, and a pie chart with nine slices no one can read. Users complain the numbers feel untrustworthy. The team rebuilds it as embedded components with a small colour-blind-safe palette, replaces the pie with a sorted bar chart, lightens the gridlines, and adds direct labels so the legend disappears. They set titles that state findings and add alt text and a table toggle to every chart. Engagement with the dashboard rises because customers can finally read it at a glance, and the cleaner design becomes a selling point in demos.

**Enterprise.** A multinational bank has hundreds of internal dashboards built by dozens of teams, each with its own colours and axis habits, and executives routinely distrust them because the same metric looks different in every deck. The company introduces a governed chart library on top of its BI platform: agreed sequential, diverging, and categorical palettes; a firm rule that bar axes start at zero; standard number formatting; and accessibility baked into every component. A visual-regression check in the delivery pipeline of chapter 8.1 blocks charts that violate the standards. Within a year, a chart from any team reads correctly on sight, and leadership stops asking "which version of this number should I believe?"

**Government.** A national statistics agency publishes public data on the economy, health, and population, and its charts are read by journalists, policymakers, and citizens who cannot verify the underlying figures. The agency treats every chart as a communication with the public and a matter of the stakeholder trust in chapter 10.16. It mandates honest scales (bars from zero, no misleading dual axes, area encoded by area), colour-blind-safe diverging palettes for regional comparisons, plain-language titles that state the finding, and a downloadable accessible table beside every chart to satisfy WCAG. When a controversial figure is published, the annotation explains the method and the uncertainty on the chart itself, so a truncated axis or an unlabelled spike can never become a misleading headline that erodes public confidence.

## Business case: motivations, ROI, and TCO

The return on good visualization design is faster, better decisions and fewer expensive mistakes. A dashboard that reveals a problem at a glance shortens the time from signal to action, and a chart that tells the truth prevents budget from chasing an illusion that a truncated axis manufactured. These gains are hard to put on an invoice, but they are real: every leadership meeting spent arguing about which chart to believe, every strategy built on a misread trend, and every customer who churns because your product's analytics were unreadable is a cost that clear design removes. Where charts drive real money, as in the bank example, the value of trusted numbers dwarfs the cost of building them well.

The cost to adopt is mostly one-time and shared. You define agreed palettes, axis and formatting rules, and accessibility defaults, then encode them in a chart component library so teams inherit them rather than re-deciding per dashboard. The ongoing cost of ownership is real but modest: maintaining the library, keeping it accessible as standards evolve, and resisting the sprawl of one-off custom charts. The cost of neglect compounds quietly: inconsistent, misleading, inaccessible charts erode trust in all your data, invite legal risk in regulated and public-sector settings, and push people back to raw spreadsheets, which wastes the entire investment in the analytics stack of chapter 7.3. To make the case to leadership, tie visualization quality to outcomes they already track: decision speed, trust in reporting, and, in the public sector, accessibility compliance.

## Anti-patterns and pitfalls

- **Truncated bar axis:** starting bars above zero so a small difference looks like a chasm; the single most common chart lie.
- **Gratuitous dual axis:** two y-scales on one chart, sliding to manufacture any correlation the author wants to show.
- **Misleading area:** scaling an icon or bubble by side length so its area, and the perceived value, grows as the square.
- **Rainbow for quantity:** encoding an ordered quantity with unordered categorical hues, so the eye cannot read magnitude.
- **Pie with many slices:** more than three slices, forcing readers to compare angles they cannot judge; use a sorted bar.
- **Chartjunk:** heavy gridlines, borders, 3D, and drop shadows that lower the data-ink ratio and bury the signal.
- **Colour as the only cue:** red-green status with no label or shape, invisible to colour-blind readers and screen readers.
- **Legend hunting:** forcing a trip to a distant legend where a direct label on the line or bar would do.
- **Everything emphasized:** every series bold and bright, so contrast collapses and nothing stands out.
- **Chart where a table wins:** a picture for four exact numbers a reader needs to read precisely.

## Maturity model

- **Level 1, Initiate:** Charts are made ad hoc in whatever tool is handy. Colours, axes, and formats vary by author, truncated axes and rainbow categories are common, accessibility is unconsidered, and readers distrust the results.
- **Level 2, Develop:** Some teams adopt basic practices, but they are inconsistent across the organization. Bars start at zero in places, obvious chartjunk is discouraged in review, and a house palette exists on a few teams, yet another team down the hall still ships a nine-slice pie and a red-green status chart.
- **Level 3, Standardize:** A shared chart component library encodes agreed sequential, diverging, and categorical palettes, honest axis rules, standard formatting, and accessibility (colour-blind-safe, alt text, table fallback). The standards are documented and enforced org-wide, and explanatory, exploratory, and dashboard uses are distinguished by design.
- **Level 4, Manage:** Visualization quality is measured and controlled against baselines. Accessibility and chart-integrity checks run in the delivery pipeline and report pass rates; the share of charts with bars from zero, contrast-compliant colour, and a table fallback is tracked as a metric; comprehension is tested with real readers against a baseline; and the count of divergent dialects of each key metric is watched as it trends towards one. Charts that violate the standards are caught before release, and the numbers, not opinion, drive where the library needs work.
- **Level 5, Orchestrate:** Visualization is continuously improved and integrated across the organization. Standards adapt as accessibility requirements and reader needs change, the palettes, components, and conventions are refined from measured evidence, annotation and narrative are the norm, and the practice is woven into the analytics and decision culture so a chart from any team reads correctly on sight and the visual language evolves as the organization learns.

## Ideas for discussion

1. Which chart on your main dashboard would look different if its axis started at zero, and does that change the story?
2. Pick your most important chart: does its message survive in greyscale, and if not, what redundant cue would fix it?
3. Where are you using an interactive chart when a static, annotated one would tell the whole story faster?
4. Do your chart titles state findings or topics, and who would notice if a headline number quietly reversed?
5. Which of your charts answers no current decision, and what would it take to delete it without anyone missing it?
6. When should a team build a viz in the product versus use the BI tool, and do you have a written rule for choosing?

## Key takeaways

- Start from the reader's question, then pick the chart: bars for comparison, lines for trend, scatter for relationship, histogram for distribution, sorted bars over pies for part-to-whole.
- Match the encoding to the data: spend position and length on your most important quantity, and use hue for categories, never for magnitude.
- Pursue graphical excellence: maximize the data-ink ratio, delete chartjunk, use small multiples, and direct the eye with pre-attentive contrast and clear hierarchy.
- Treat colour as a system (sequential, diverging, categorical), keep it colour-blind-safe, and never rely on colour alone; provide labels, alt text, and a table fallback.
- Tell the truth about scale (bars from zero, honest areas, no gratuitous dual axes), annotate the insight, and add interactivity only when a real follow-up question demands it.

## References and further reading

- Edward R. Tufte, *The Visual Display of Quantitative Information*
- Edward R. Tufte, *Envisioning Information*
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten*
- Stephen Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals*
- Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication*
- Alberto Cairo, *How Charts Lie: Getting Smarter about Visual Information*
- William S. Cleveland, *The Elements of Graphing Data*
- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps*
- Tamara Munzner, *Visualization Analysis and Design*
- Cynthia A. Brewer, ColorBrewer: Color Advice for Cartography (colorbrewer2.org)
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*
