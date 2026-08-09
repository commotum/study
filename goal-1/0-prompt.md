# Copy-Paste Goal Prompt

```text
Work through /Users/jake/Developer/study/goal-1/0-plan.md using the repeatable protocol and stage template in /Users/jake/Developer/study/goal-1/0-loop.md.

The objective is to add an optional live visual math editor to `type: blank` in the Obsidian Quiz Blocks plugin. A math-enabled blank must turn ordinary keyboard input such as `2/3`, `sqrt(x+1)`, and `x^2` into editable structured notation inside the input itself. Existing blank blocks must remain plain text by default.

Work on the existing `master` line; do not require a separate feature branch. Treat /Users/jake/Developer/obsidian-quiz-blocks as the implementation source of truth and update the study submodule only to a tested committed revision. Preserve `==answer==` authoring with keyboard-friendly text, deterministic and honestly documented exact matching, `require_exact: false` reveal behavior, root-level `feedback`, saved-state compatibility, accessibility, and existing Math Academy quiz blocks. Do not substitute a preview for a real editor, silently change legacy blanks, force LaTeX authoring, or claim symbolic equivalence without implementing and proving it.

At each stage: inspect and sync current files and tests; update 0-plan.md with current facts; select the first incomplete stage; create or refresh its stage file; implement only that stage; add requirement-specific and no-cheating checks; run focused tests plus the appropriate full plugin, build, authoring-validator, corpus, Obsidian, and diff verification; record evidence in the stage file; and fold results back into 0-plan.md before continuing.

Completion means the original objective is genuinely achieved: the opt-in visual editor works in Obsidian, legacy text blanks remain compatible, grading/reveal/feedback/reset/persistence are verified, runtime and authoring tooling agree, tests and corpus checks pass, and the tested revision is synchronized through the intended copies. Carry every unresolved issue forward as explicit next work rather than declaring a partial substitute complete.
```
