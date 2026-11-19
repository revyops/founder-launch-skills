---
name: meta-ads
description: Launch defaults and a pre-publish check for Meta (Facebook and Instagram) ads. Gives a settings table, a naming convention by funnel stage, UTM rules, a like-for-like test checklist and a check before anything goes live. Use when building, duplicating, auditing or testing a Meta campaign, ad set or ad, or when someone says "check my Meta campaign before I publish". Claude prepares; the user publishes.
---

# Meta ads: launch defaults and a check before anything goes live

## Rules for you

- **You prepare. The user publishes.** Never publish, switch on, switch off or edit a live campaign, and never change a budget or spend limit. Build or review drafts, then hand the user exact steps.
- Say which defaults you applied and which you left as found.
- One variable per test. Everything else matches the control.
- Never delete. Pause, and name the change in a log.
- Judge results on your own source of truth (sales or bookings), not only on what Meta reports.
- Do not ask for passwords. The user signs in.

## 1. Default settings

These are starting points. Change one only when you have a reason and write the reason down.

| Area | Default | Why |
|---|---|---|
| Objective | Match the business goal: leads for a lead form or booked call, sales for a shop, app promotion for installs | Meta optimises toward the objective you pick |
| Optimisation event | The deepest event that can reach about 50 a week per ad set. Quick check: daily spend needed is about 50 times cost per event, divided by 7. If you cannot afford it, use the next event up and expect "learning limited" | Meta needs volume to learn |
| Budget level | Ad set level, daily budget. Match the control's budget type in tests | Easier to read and compare |
| Budget changes | Small steps (10 to 20 percent), not more often than every 3 to 4 days | Big edits restart learning |
| Bidding | Highest volume, no cost cap at small budgets | Caps starve small budgets |
| Audience | Broad: location and age only, no interest stacking. Let the creative do the targeting | Meta finds buyers from signals. Narrow stacks cost more |
| Locations | The places you can serve | |
| Placements | Automatic placements. Turn off Audience Network if you see junk traffic or cheap clicks with no conversions | |
| Creative volume | Several genuinely different concepts per ad set, in 4:5 and 9:16, refreshed regularly | Concept difference beats small tweaks |
| Creative for each placement | Make a 9:16 version for Reels and Stories. Do not crop a landscape video | Cropped video looks wrong and loses the hook |
| Advantage+ creative enhancements | **Off by default on every ad.** Check each ad, not the summary screen | They can change your image, text, music or framing without you seeing it. Turn one on only as a deliberate test |
| AI-generated media | Off unless approved. Each ad should show zero generated media | |
| Special ad category | Declare one when the ad falls in it (jobs, housing, credit, financial products, social issues) | Meta's rule |
| URL parameters | Every ad, button and image carries UTMs (see section 3) | You cannot learn without attribution |

## 2. Naming convention by funnel stage

Lowercase, underscores, no spaces or hyphens.

- **Campaign:** `<brand>_<test>_<stage>_<format>`
- **Ad set:** `<test>_<arm>_<stage>_<creative type>`
- **Ad:** `<creative id>_<short name>`

Stages, one per campaign:

| Stage | Audience |
|---|---|
| `tofu` | Cold. Never saw you |
| `mofu` | Visited a page but did not opt in |
| `bofu` | Opted in but has not bought |
| `cust` | Already a customer |

Tests go in a new campaign named with a `test_` prefix and their own budget. Do not switch off or edit a live campaign to make room.

## 3. UTMs on every ad

Put these in the URL parameters field of every ad, not in the website URL:

`utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}`

- Keep Facebook and Instagram apart (the source tag does this).
- Do not use plain `social` as the medium. That is usually your organic traffic.
- Meta fixes the name tags at first publish. If you rename later, type the literal names into the URL parameters and read each ad back.

## 4. Like-for-like test checklist (test versus control)

Open both editors and read every setting. Do not trust summaries.

- [ ] Objective and conversion location
- [ ] Budget level, type (daily or lifetime), amount, any budget sharing
- [ ] Bid strategy and any cost goal
- [ ] Optimisation event (usually the one thing allowed to differ)
- [ ] Audience settings and locations
- [ ] Placements
- [ ] Same ads on, including copies with duplicate names
- [ ] Every Advantage+ creative toggle, ad by ad
- [ ] AI-generated media count and translation settings
- [ ] Schedule: start and end dates
- [ ] Run at least 14 days, sized from your real baseline, with the stop rule written before launch

## 5. Check before anything goes live

Run this and hand the user a pass or fail list. Do not publish.

1. **Tracking.** The pixel or conversion event fires on the right page, once per action. Use Events Manager and a real test. Check no old rule fires the same event somewhere else. If you use both browser and server events, confirm they are de-duplicated.
2. **Links.** Click each ad's URL. It opens the right page, on a phone too. The UTMs are present and spelled as in section 3.
3. **Copy and creative match.** The text, headline and button say what the landing page says. The image or video is the approved one, in the right size for each placement.
4. **Enhancements.** Every ad shows enhancements off and zero generated media.
5. **Names.** Campaign, ad set and ad names follow section 2.
6. **Spend.** Budget and schedule are what the user approved. No account or campaign spending limit unless the user wants delivery to stop at a figure.
7. **The control is untouched.** Status, budget and ads match what they were. Opening a live ad set can create an empty draft, so untick any stray row in the publish list.
8. **Nothing to change mid-test.** Write down what will not be edited until the test ends. Changes go on a duplicate.
9. **Ads policy.** Nothing that would be rejected: personal-attribute wording, before-and-after claims, wrong special ad category.

Then say: "Ready for you to publish. Here are the steps." and list them.

## 6. After launch

- Let the test run its planned length before judging it. Early days are noisy.
- Read results against your own sales or bookings data, then against break-even.
- If an ad is rejected, read Meta's reason, fix the cause on a duplicate, and pause rather than delete the original.
