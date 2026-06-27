# Quiz Blocks Demo

These examples cover each documented Quiz Blocks question type. Open this note in Obsidian reading/preview mode with the Quiz Blocks plugin enabled to try them interactively.

## `radio` - Single Correct Option

```quiz
type: radio
content: >-
  Which planet is known as the Red Planet?

options:
- content: Venus
  feedback: Venus is often called Earth's twin because of its similar size.

- content: Mars
  correct: true
  feedback: Mars looks reddish because iron minerals in its soil oxidize.

- content: Jupiter
  feedback: Jupiter is the largest planet in the solar system.
```

## `checkbox` - Multiple Correct Options

```quiz
type: checkbox
content: >-
  Which of these are valid Markdown emphasis styles?

options:
- content: "**bold**"
  correct: true
  feedback: Double asterisks create bold text.

- content: "*italic*"
  correct: true
  feedback: Single asterisks create italic text.

- content: "==highlight=="
  correct: true
  feedback: Obsidian supports double equals for highlighted text.

- content: "//underline//"
  feedback: This is not standard Markdown emphasis syntax.
```

## `select` - Multiple Questions Sharing Options

```quiz
type: select
content: >-
  Select the capital city for each country.

options:
- id: paris
  content: Paris
- id: ottawa
  content: Ottawa
- id: lisbon
  content: Lisbon
- id: tokyo
  content: Tokyo

questions:
- content: France
  correct_option: paris

- content: Canada
  correct_option: ottawa

- content: Portugal
  correct_option: lisbon
```

## `multi-select` - Multiple Questions With Separate Options

```quiz
type: multi-select
content: >-
  Choose the correct answer for each dropdown. Each dropdown has its own option list.

questions:
- content: Select 1
  options:
  - id: pi
    content: '$\pi$'
  - id: minus-one
    content: '$-1$'
  - id: zero
    content: '$0$'
  - id: one
    content: '$1$'
  correct_option: pi

- content: Select 2
  options:
  - id: not-orthogonal
    content: are not orthogonal
  - id: orthogonal
    content: are orthogonal
  correct_option: orthogonal
```

## `noodle` - Connect Questions With Options

```quiz
type: noodle
content: >-
  Connect each country with its capital.

options:
- content: Ottawa
- content: Tokyo
- content: Nairobi
- content: Lisbon

questions:
- content: Canada
  correct: Ottawa

- content: Japan
  correct: Tokyo

- content: Kenya
  correct: Nairobi

- content: Portugal
  correct: Lisbon
```

## `free` - Free Text With Optional Reference Answer

```quiz
type: free
content: >-
  In your own words, what is active recall?

correct: >-
  Active recall is the practice of retrieving information from memory instead of only rereading or reviewing it.
```

## `blank` - Fill In The Gaps

```quiz
type: blank
content: |-
  The chemical symbol for water is ==H2O==.

  Water freezes at ==0 degrees Celsius== under standard atmospheric pressure.

  In Markdown, a link is written with ==square brackets== for the label and ==parentheses== for the URL.

feedback: >-
  Text wrapped in double equals becomes the hidden answer for each gap.
```

## `blank` - Reveal Answers Without Exact Matching

```quiz
type: blank
require_exact: false
content: |-
  The derivative of $x^2$ is ==$2x$==.

  The simplified form of $\frac{x^2}{x}$ is ==$x$==, assuming $x \ne 0$.
```

## Notes

### `radio`

- Issue: Selecting an answer before pressing **Check** originally had no visible state, so it looked like clicks were not registering.
- Resolution: The selected radio now fills with the Obsidian accent color and uses a contrasting inner dot. The graded red/green states still appear after **Check**.
- Follow-up fix: The option text wrapper was changed to valid flex markup so font-size changes do not make the radio and text look vertically misaligned.

### `checkbox`

- Issue: Checkbox selections also had no clear pre-check state.
- Resolution: Selected checkboxes now fill with the Obsidian accent color before **Check**, while keeping the existing graded red/green states after **Check**.
- Follow-up fix: The option text wrapper was changed from an invalid inline wrapper around block markdown to a normal block flex item, matching the radio alignment fix.

### `select`

- Issue: The select quiz previously used the name `choice`, which was less clear than the actual UI control.
- Resolution: The quiz type was renamed to `select`. The old `choice` type is no longer kept as an alias, so quiz blocks should use `type: select`.
- Issue: The select quiz rendered as a code block because YAML parsed unquoted `True` and `False` as booleans, while the schema expected option content to already be text.
- Resolution: The schema now coerces scalar text fields, including strings, numbers, and booleans, into display text. The sample also quotes `"True"` and `"False"` so their capitalization is preserved.
- Issue: The dropdown initially defaulted to the first option instead of the placeholder.
- Resolution: Each dropdown now starts with an empty value mapped to the disabled `Select an answer` placeholder.
- Issue: The placeholder looked like a normal selected answer.
- Resolution: The placeholder uses muted text color while keeping the custom dropdown aligned with Obsidian theme styling.
- Feedback theme: Dropdown feedback appears only after pressing **Check**. The selected answer keeps the same dropdown shape, but is marked green using the "right" theme when correct and red using the "wrong" theme when incorrect. Because the dropdown always has a single selected answer, there is no missed/unselected state. When the selected answer is wrong, the correct answer is shown beneath the dropdown as regular red feedback text, not as a second boxed answer. Any per-question feedback text is displayed under the dropdown after checking, with correct feedback styled in the green "right" theme and wrong feedback styled in the red "wrong" theme, matching the checkbox feedback style.
- Follow-up fix: Select-style quizzes now use a custom dropdown so option labels can render inline Markdown and LaTeX. The dropdown opens inside the quiz block, wraps long labels, and keeps a fixed-size chevron.

### `noodle`

- Status: Mostly working during testing.
- Known warning: `svelte-check` reports an existing accessibility warning because the main noodle container has pointer handlers without an ARIA role.
- Resolution: No behavior change has been made yet; this is still a follow-up cleanup item.

### `free`

- Status: Working during testing.
- Issue: The free-response quiz previously used the name `text`, which sounded more like a formatting primitive than a question type.
- Resolution: The quiz type was renamed to `free`. The old `text` type is no longer kept as an alias, so quiz blocks should use `type: free`.

### `blank`

- Issue: The fill-in-the-blank quiz previously used the name `prompt`, which was too generic and sounded like an Obsidian command palette prompt.
- Resolution: The quiz type was renamed to `blank`. The old `prompt` type is no longer kept as an alias, so quiz blocks should use `type: blank`.
- Issue: Blanks originally rendered as hidden highlighted text instead of editable fields.
- Resolution: Text wrapped in `==double equals==` now renders as an inline input field. After pressing **Check**, each blank is marked green or red, and incorrect blanks show the expected answer in red.

### Helpful Obsidian documentation

- `Build a plugin.md`: Most useful for the basic local-install loop. It explains that Obsidian loads a plugin from a folder inside `.obsidian/plugins`, that the built plugin output is `main.js`, and that `manifest.json` changes require restarting Obsidian. This was the key setup reference for building our repo version and copying `main.js`, `styles.css`, and `manifest.json` into the vault plugin folder.
- `Development workflow.md`: Most useful for understanding why each code change needs a plugin reload before it appears in Obsidian. It confirmed the practical test loop: rebuild, reinstall/copy the artifacts, then disable/enable the plugin or restart Obsidian.
- `Anatomy of a plugin.md`: Useful for orientation rather than the specific visual bugs. It explains the plugin lifecycle, especially that setup happens in `onload()` and cleanup happens in `onunload()`. That matched this repo's structure where `src/main.ts` registers the `quiz` Markdown code block processor.
- `Use Svelte in your plugin.md`: Useful for understanding the component side of the repo. It explains that Svelte components are compiled into the plugin bundle and mounted into Obsidian UI elements, which is exactly how the `Quiz*.svelte` components render inside the processed quiz block.
- `User interface/HTML elements.md`: Potentially useful for future UI cleanup, but not central to these fixes. The current bugs were mostly Svelte state, schema parsing, custom dropdown behavior, and CSS feedback styling rather than Obsidian-specific HTML APIs.
