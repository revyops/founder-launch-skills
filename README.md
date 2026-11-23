# 9 launch skills for Claude Code

> Built while launching [RevyOps, the AI CRM for Claude](https://revyops.com/waitlist?utm_source=github&utm_medium=referral&utm_campaign=launch&utm_content=skills-readme). **[Join the waitlist →](https://revyops.com/waitlist?utm_source=github&utm_medium=referral&utm_campaign=launch&utm_content=skills-readme)**

A skill is a file Claude reads before it does a job. It follows the same method every time, so you never explain the job twice. These are the nine I use to launch my CRM.

## Install

**Claude Code plugin (recommended).** In Claude Code, run:

```
/plugin marketplace add revyops/founder-launch-skills
/plugin install launch-skills@revyops
```

**Or copy the files.** Download this repo and copy the folders inside `skills/` into `~/.claude/skills/` (all your projects) or `.claude/skills/` in one project.

Then ask Claude for the job in plain words ("turn today into post ideas", "edit this clip into a Short"). It picks the right skill by itself. You can also type `/` and the skill's name.

## The skills

### Create
| Skill | What it does |
|---|---|
| [content-ideas](skills/content-ideas) | Turns your work day into post ideas, each with a hook and the beats. |
| [video-scripts](skills/video-scripts) | Scripts a long video as one main loop and up to seven small ones, plus a Short from each. |
| [video-editing](skills/video-editing) | Raw phone clip to a captioned 9:16 Short, with ffmpeg and Whisper. Optional relight step puts the speaker in a better room with studio light. |

### Publish
| Skill | What it does |
|---|---|
| [copy-doctrine](skills/copy-doctrine) | Plain English with no AI tells. Drafts and audits any copy. |
| [report-format](skills/report-format) | Every page or report reads like a clear dashboard: tabs, KPI strip, rows that open into charts. |
| [social-posting](skills/social-posting) | Posts, comment replies and "comment WORD" keyword posts on LinkedIn, at a human pace. |

### Sell
| Skill | What it does |
|---|---|
| [gtm-playbook](skills/gtm-playbook) | Starter GTM: write your ICP, score fit 1 to 5, split your list into lead pools. |
| [meta-ads](skills/meta-ads) | Launch defaults for Meta ads and a check before anything goes live. |
| [ai-onboarding](skills/ai-onboarding) | Gets you or your team set up on Claude, one step at a time. |

## Make them yours

Each skill is a plain Markdown file. Open it, change the rules to fit how you work, and Claude follows your version. Keep the ones you use; delete the rest.

## Want these running on your CRM data?

The skills work best when Claude can see your whole pipeline: every contact, email, call and post engagement in one place. That's what I'm building with RevyOps, the AI CRM for Claude.

**[Join the waitlist →](https://revyops.com/waitlist?utm_source=github&utm_medium=referral&utm_campaign=launch&utm_content=skills-readme)**

## Licence

MIT. Use them, change them and share them, including in paid work. Keep the copyright line. See [LICENSE](LICENSE).
