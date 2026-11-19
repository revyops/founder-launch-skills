---
name: report-format
description: Makes every page or document Claude builds read like a calm, tabbed dashboard. Use when building or redesigning a report, dashboard, scorecard, explainer, process doc, plan, memo or any shareable HTML page, or when asked for "a report", "a dashboard", "make this page look clean" or "add tabs and charts". Covers tabs, KPI strip, expandable rows with time series, tooltips, colours, tables, light and dark mode and phone width.
---

# Report format: every page reads like a dashboard

## What this does

A report exists to make a decision or trigger an action. This skill makes each page look calm, open on the answer, and let the reader go from a total to its history in one click without leaving the page. It applies to every page or document you build, not only reports: explainers, process docs, plans, memos and playbooks too.

## Steps

1. Work out the decision or action the page serves, and who reads it (a busy operator).
2. Put the data in one embedded JSON block. Render functions read from it. For a report that repeats, keep template, data file and build script separate, so a scheduled run only swaps the data.
3. Build the skeleton below: small header, the answer in one or two sentences, sticky tabs, filter row, content, footer.
4. Add the core patterns that fit the data (KPI strip, expandable rows, tooltips, "how this is counted").
5. Apply the visual system (tokens, light and dark, fonts, phone width).
6. Escape all text that comes from a source system before inserting it into HTML.
7. Run the done-check.

## The page skeleton (in this order)

1. **Header strip.** Eyebrow `Owner or client, report type, source` (mono, uppercase, muted). Then an H1 that names the period or subject ("Week of 5-11 Oct"). Right-aligned controls: period picker, a status chip (Draft or Posted), and actions. Nothing else above the tabs: an eyebrow, a title, one sentence of subheadline and an owner and updated line.
2. **The answer in one or two sentences.** Bold the headline number and its comparison ("**88 new subscriptions**, up on the prior 3-week average of 81"). Never open on method.
3. **Tab bar.** Sticky, scrolls sideways on phones, never wraps. 3-7 tabs with count badges (`1 live`, `5`, warning colour when something needs attention). Arrow keys move between tabs. Link by `#tab` hash and remember the last tab in `localStorage`, wrapped in try/catch. A typical set:
   - **Overview or Scorecard:** KPI strip, one main trend chart, the numbers table.
   - **Breakdown tabs:** by channel, by person, by type. Each is a table whose rows expand.
   - **Needs a look, Watch list or Review queue:** the action list, worst first.
   - **Changes or Log:** what changed, when, who.
   - **Past reports or Archive:** every earlier day or week, read-only.
   - **Methodology:** fixed for every period. When it runs, what a day or week is, where each number comes from, what the report cannot see yet.
4. **Filter row** directly above the content it affects, one line: date presets (`Today, This week, Last 4 weeks, Month to date, Custom`), From and To inputs, a scope control, and a note saying which tabs it applies to. Give the row a clear gap (about 8 px by 14 px) so a note never sits tight against the buttons. Use one shared flex, wrap, centred rule for every control row.
5. **Footer.** Sources and when they were read, in one small paragraph.

**Context goes in the first tab,** never in the header: "What we're trying to do", "Overview" or "About", with cards that jump to each other tab. One tab per category of content (status groups, phases, teams, channels), each with a count badge. Open decisions, methodology and sources get their own tabs. Inside a tab, items are collapsed rows that open into detail, with an Open all and Close all button.

**Subtabs** (a segmented control under the tab bar) are for one tab with several views. A report that covers several teams may add one **team bar** above the tabs (an underlined text row such as `Sales team, Support team, Finance`). The tab row then shows only that team's tabs. Each team remembers its last tab, sums its tabs' badges and hides filters that do not apply. A team with many tabs may group them under a pill row. Never go deeper than team bar, group, tab, subtab.

**One line under a tab title.** A tab opens on one short sentence saying what it measures. Filter definitions, date ranges, start dates and caveats go in an ⓘ or the "How this is counted" note, never in a paragraph above the content. Subtab notes are a few words.

## Core patterns

- **KPI strip.** 4-6 tiles. Each has a mono caps label, a big number, a comparison (versus the prior period and the same period last year), the change on its own second line, and a sparkline. A tile that needs attention takes the warning colour. A joined-cell totals strip (number, label, small note) works for daily reports.
- **Change colours: plus is green, minus is red.** On every page, chart, table and tile. A percentage or other plus or minus change is coloured by its sign only: green for a plus, red for a minus, neutral for zero. Do this even for measures where lower is better. In a tile the change always sits on its own line under the comparison, in the same place on every tile. Tile text rules such as `.stat span { color: muted }` override a plain `.up` class, so scope the colour to the panel (`#panel .up`) and check the computed colour in the browser.
- **Expandable rows open into a time series (the signature pattern).** Any row in a summary table (a channel, a person, a funnel stage, a ticket type) opens a detail row spanning the table. The detail holds a chart of that row over the selected range (daily up to 6 weeks, weekly beyond, 12 weeks as the weekly default), a granularity toggle (Daily, Weekly, Monthly), a chart-type toggle when useful (Line, Bar), the target or limit as a dashed line where one exists, and a one-line meta row (current value, gap to target, weeks over). For team reports draw one line per person plus a **Team total** series, with the team total in the tooltip footer. Offer an **Expand all** button. Detail charts are 200-320 px tall.
- **Every expandable row shows a chevron.** A row that opens (table row, list row, card) has a `›` at the start of its first cell that rotates 90 degrees when open, a pointer cursor, a hover tint, `tabindex="0"` with Enter and Space, and `aria-expanded`. A line saying "click a row" is not a substitute. Write one rule on the shared row class, not per table, so new tables get it:
  ```css
  tr.rfr { cursor: pointer; } tr.rfr:hover td { background: var(--sunk); }
  tr.rfr td:first-child::before { content: "›"; display: inline-block; width: 14px; color: var(--muted); transition: transform .15s; }
  tr.rfr.open td:first-child::before { transform: rotate(90deg); }
  ```
  Before publishing, check that every clickable row on the page has it.
- **Tooltips wherever a number lives.** Charts show a crosshair and a tooltip listing every series sorted by value, then a bold Total or Team line. Column headers get a dotted underline and an `ⓘ`, and hover or focus shows a plain-English definition (what it is, where it comes from, what red means). The ⓘ sits to the right of the header text, vertically centred: wrap the label and button in an inline-flex span with `white-space: nowrap`, so it never wraps onto a second line. Never rely on the native `title` attribute: it does not show in many embedded viewers. Use an `ⓘ <button>` with one shared `position: fixed` popover (`role="tooltip"`, `aria-describedby`) shown on mouseover, focusin and click or tap, closed by Escape, scroll or a tap elsewhere. A tapped one stays open. KPI tile labels get one too.
- **"How this is counted" as collapsible bullets.** A `<details>` under each table with a `›` summary. Inside: short H4 groups of 2-5 bullets, bold term first then the definition. Never paragraphs of method in the main view.
- **Status is a pill and a side bar, never colour alone.** Pills with text (`On track, Watch, Concern, Critical`; `Live, Approved, Queued`; grades `A+` to `F`). Cards and list rows get a 4-6 px left colour bar by level. The same levels and colours throughout. In a status diagram, live is green, never grey. Amber means ready and not started. A dashed grey outline means not built.
- **Cards and List toggle** for per-person or per-item audits. Cards show a name, a headline number top-right, a proportional bar, flag pills, key facts in an aligned two-column `dl`, and "More details" collapsed. List shows one row per item with the same bar, expanding to details.
- **Approval pipelines are stage sub-tabs.** Anything someone approves sits in exactly one stage, shown as sub-tabs in order with count badges: `Review`, `Changes requested`, `Approved`, `In use`, `Finished`, `Library`. Approving moves the item on, and it never just vanishes from Review. Requesting changes requires a note. Each item keeps its history as `{at, action, note, by}`. Under the note say what happens next and when. A request never sits silent. Live items have no review buttons. A failed save says "did not save ... Nothing changed".
- **Action lists, worst first.** Each item has a level chip, a bold title with the number, one muted sentence of evidence, and, where a human sends something, a ready-to-send draft in a grey box with a **Copy** button.
- **Period navigation and archive.** Daily: ‹ prev, date, next › with a permalink hash (`#YYYY-MM-DD`). Weekly: a dropdown of report weeks. Past periods are frozen and never edited.
- **"Does it pay?" is grouped bars plus a verdict, never a bare scatter.** Group results into 2-4 bands (grade letters, score bands, speed buckets). Show one card per result with a bar per band (best on top, with average and count) and a pill that carries the gap: `Yes, +11 pts`, `Not so far, -18%`, `Leaning yes` or `Leaning no` (a real-sized gap, not proven yet), `No clear gap` (only when the gap is within 2 points or 5%), `Too early`. Put r and p in the ⓘ, and keep a scatter and table collapsed below.
- **Certainty where numbers are estimated.** A grade pill (A+ at 95% or more, A 90-94, B 80-89, C 65-79, D 50-64, F under 50) with a hover reason, and a Methodology table explaining the scale.
- **Cross-references are links.** A code or name that points elsewhere on the page jumps there, flashes it and offers "← Back to ...". Compact grids name their axis ("Funnel stage →" over numbered columns, full name on hover) and group long lists into collapsed sections with a summary row and Expand all.
- **Summary for chat.** A daily or weekly report may have a short text version (headline numbers, needs-a-look bullets, a link with `#date`), previewed inside a collapsed `<details>` and copyable. Never post it anywhere without the user's yes.
- **Locked pages.** If a page's data is encrypted behind a password, ask once per browser. After a good unlock, store the derived key (never the password) in `localStorage` in try/catch, open with it next time, and show a **Lock this page** link that clears it. Keep the salt fixed per page across rebuilds.

## Charts

- Chart.js 4.4.1 from cdnjs, or hand-rolled SVG for small static charts.
- Line for trends, stacked bar for composition per period, horizontal bars for type or mix. Never dual axes. Never pie charts.
- Compare to something on every trend: last year (grey, dashed), the prior average or the target line.
- Annotate events (a dashed vertical line and a short label such as "Pricing change, ~9 Sep"). Draw part periods lighter and say so in the tooltip.
- Each entity (a person, a channel) keeps one colour across every chart and filter. Show at most 8 series and fold the rest into Other. Clicking a legend chip or a person's column header hides that series in every chart.
- Every chart offers **Show as a table** in a collapsed `<details>`.

## Tables

- **Closed rows fit without "...".** A closed row holds only short values: a name, a pill, a count like "5/11", a date like "7 Nov". Put sentences (next steps, notes, number lists) in the opened detail. If most rows would end in "...", drop or shorten that column.
- Sticky header row and sticky first column on any table that scrolls, inside a scroll box with a max height near the viewport.
- Names stay on one line. Headers may wrap to two lines with `<br>` to keep columns narrow.
- Numbers right-aligned, in tabular figures (mono). A bold Total row with a heavy top rule.
- **Time runs left to right.** In a table of periods (years, quarters, months, cohorts), the periods are the columns, in the chart's x-axis order, and the measures go down the first column, grouped (dollars before multiples and percentages). Total column last. Extended or estimated periods are greyed and tagged. A period opens its detail from its column header, shown below the table. More than about 12 periods may stay as expandable rows.
- **Funnel tables: each rate sits right after the count it comes from.** Columns in funnel order so the arithmetic reads left to right: `Came due, Held, Show rate, Rejected, Accepted, Accept rate, Won, Win rate`. Never group rates at the end. Put the formula in the header tooltip or the "how this is counted" note.
- **Show rate = held divided by came due.** "Came due" means meetings whose date has passed, whatever their status. Canceled, no-show and never-updated meetings count against the rate. Future meetings are left out. Never held divided by (held plus no-show). A "Came due" column sits right before Held.
- **Win rate = won divided by accepted** (what the closer accepted), never won divided by (won plus lost). Open deals count as not won yet. A breakdown of accepted (lost, open, won) must add up to the accepted count.
- Group rows (mono caps, tinted) section a long table. Sort the default view by what matters, worst first or biggest first.

## Visual system

- Define colours as tokens on `:root` for light. Redefine them under `@media (prefers-color-scheme: dark)` with `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. Give `body` an explicit background.
- Palette: off-white background, white panels, 1 px hairline borders, 8 px radius, one accent colour, and status pairs (good, warn, bad, note), each with a soft background.
- Type: a display face for headings (Archivo 800 or similar), a clean sans for body (IBM Plex Sans or Public Sans), mono for labels, numbers and eyebrows (IBM Plex Mono or JetBrains Mono). Load from Google Fonts only.
- Density: 14-15 px body, 20-24 px between sections, prose capped near 72ch, page max width 880 px (daily) to 1180 px (wide tables).
- Phone width: 16 px gutters, tabs scroll sideways, the KPI grid collapses to 2 columns, tables scroll inside their own box, no horizontal page scroll.
- **Dropdowns.** Never ship the native select arrow, because it sits against the right border. Use one shared rule listing every select on the page (list each selector so it outranks any earlier `background` shorthand), placed after the inputs' own rules:
  ```css
  /* Every dropdown: own chevron, 14px in from the right edge, 40px right padding */
  select,.filters select{-webkit-appearance:none;appearance:none;padding-right:40px;cursor:pointer;
    background-image:linear-gradient(45deg,transparent 50%,var(--ink-2) 50%),linear-gradient(135deg,var(--ink-2) 50%,transparent 50%);
    background-position:calc(100% - 19px) 55%,calc(100% - 14px) 55%;background-size:5px 5px;background-repeat:no-repeat}
  ```
  Keep `background-color`, not the `background` shorthand, on any later select rule, or the chevron disappears. Give selects the same border, radius and font as the page's other inputs.

## Writing inside reports

- Plain English for a busy operator. Name things the way the team does. If the `copy-doctrine` skill is installed, follow it.
- Lead every section with the conclusion and put evidence after. Each tile, card and list item gets a one-line takeaway, not a paragraph.
- Every number states its period and source somewhere reachable (subtitle, tooltip or Methodology). Say "not read" rather than estimate silently.
- Internal notes (calibration, decisions about people) never appear on a page shared with the people being measured.

## Done-check

Open the page in a browser and check each of these. Fix any failure before sharing.

- Every tab opens. Count badges match the contents.
- Every expandable row has a chevron, opens, and shows its chart. Expand all works.
- Hover a chart: the tooltip lists every series and a total. Hover or tap a column header ⓘ: the definition shows.
- Plus is green and minus is red everywhere, checked in the browser's computed style.
- Dark mode and light mode both look deliberate. Dropdowns show their own chevron.
- Phone width (375 px): no horizontal page scroll, tabs scroll, tables scroll inside their box.
- Closed table rows have no "...".
- The footer names sources and read times. The lede states the answer with its comparison.
- Tell the user what changed in a few lines, with the file or link.
