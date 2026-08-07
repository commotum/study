# PHY 212 Study Vault

This directory is the course study vault for Physics 212. It keeps the original
course activity organized chronologically while turning each problem into a
focused, reusable lesson that can be tracked across assignments and quiz study
guides.

## Directory map

```text
212/
├── Home.md
├── 0. Table of Contents/
│   └── TOC.md
├── topics.csv
├── prerequisites.csv
├── Lecture-Files/
└── M1/ ... M6/
    └── YYYY-MM-DD-UNIT-NAME/
        ├── YYYY-MM-DD-UNIT-NAME.md
        ├── Lessons/
        ├── Prerequisites/
        ├── Source/
        │   └── Images/
        ├── Study-Guide.md
        ├── Cheat-Sheet.md
        └── Reference/
```

Not every unit contains every optional directory or file.

## Top-level files

### `Home.md`

The course dashboard. It contains the next-topic queue, course and module
progress, study-guide progress, and completion history. Sections enclosed by
`update-progress` comments are generated and should not be edited by hand.

### `0. Table of Contents/TOC.md`

The full Obsidian lesson checklist, grouped by module and dated unit. The
`check-progress` block and lesson checkboxes connect the chronological vault to
the progress-tracking workflow.

### `topics.csv`

The machine-readable lesson registry. Each registered lesson has a stable topic
ID, module-local topic number, display name, Markdown path, and owning
assignment. The same identifiers appear in lesson comments:

```text
lesson-id: 212-M5-037
topic-code: MTH212.M5.37
```

The human-facing course title uses `PHY 212` or `Physics 212`; existing registry
and topic-code fields use `MTH-212` and `MTH212` and should be preserved unless
the metadata schema is deliberately migrated.

### `prerequisites.csv`

The dependency registry for topic-to-topic prerequisite relationships. The file
is currently scaffolded with the columns `topic,requires`.

### `Lecture-Files/`

Empty naming templates for raw transcripts, cleaned transcripts, and lecture
notes before they are placed in a dated lecture unit.

## Modules and dated units

`M1` through `M6` are course modules. Within each module, folders are dated so
that the original course sequence remains visible.

| Pattern | Meaning |
|---|---|
| `YYYY-MM-DD-M5-3` | Lecture or class meeting within a module |
| `YYYY-MM-DD-HW-7` | Homework assignment |
| `YYYY-MM-DD-PQ-3` | Practice quiz |
| `YYYY-MM-DD-Q-3` | Quiz-preparation collection |

The folder name and its main Markdown filename normally match exactly.

## Standard unit anatomy

### Main unit note

The matching Markdown file is the student-facing problem set. Problems use
`## Problem N` headings and Obsidian `quiz` code blocks. Common quiz types are
`radio`, `blank`, `checkbox`, and `free`. Separators between problems use `---`.

The main note should contain the cleaned question, answer configuration, useful
feedback, equations, and links to local images. It is the place to practice the
original assignment or lecture questions, not the place for a full tutorial.

### `Lessons/`

Each original problem normally maps to `Lessons/Problem-N.md`. A lesson teaches
the problem's core move rather than merely presenting its answer. A typical
lesson contains:

1. A descriptive skill-based title.
2. Stable `lesson-id` and `topic-code` metadata in an HTML comment.
3. A table of contents and prerequisite list.
4. A short conceptual progression with worked examples.
5. Embedded quiz-block practice with targeted feedback.
6. An application back to the original problem.
7. A concise summary.

Lessons should be self-contained enough to study independently, while images
remain stored with the owning dated unit.

Quiz-preparation units may also contain named lessons for important syllabus
gaps that do not correspond directly to a numbered problem. Quiz 2 additionally
contains an `Examples/` library beneath `Lessons/`; those example files support
the registered group lessons and are not independent catalog topics.

### `Prerequisites/`

Reserved for local copies of prerequisite lessons when an assignment needs
supporting knowledge from outside its own problem set. These directories are
present in several assignment skeletons but are not yet populated in this
course.

### `Source/`

Keeps source material separate from the cleaned study surface. Lecture units
typically contain:

```text
Source/
├── Raw-Transcript.md
├── Lecture-Transcript.md
├── Lecture-Notes.md
├── M5-3-PRE.md
├── M5-3-LEC.md
└── Images/
```

`Raw-Transcript.md` preserves the initial capture. `Lecture-Transcript.md` and
`Lecture-Notes.md` are cleaned references. `PRE` and `LEC` files contain the
normalized pre-class and in-class quiz blocks that are composed into the main
unit note.

Homework and practice-quiz sources may instead use a nested assignment-named
folder under `Source/`, especially when preserving an imported assignment and
its images together.

### Images

Images live below the owning unit's `Source/` tree. The main unit note links from
its own directory, for example:

```markdown
![](<Source/Images/example.png>)
```

A lesson links one directory upward, for example:

```markdown
![](<../Source/Images/example.png>)
```

Use semantic, problem-specific filenames and reuse an existing image rather than
creating duplicates.

## Quiz-preparation collections

Quiz folders build a curated study path over lessons that remain in their
original lecture, homework, and practice-quiz units.

- `Study-Guide.md` orders lessons into a learnable progression and records why
  each lesson is included.
- `Cheat-Sheet.md` is a compact formula and relationship reference.
- `Reference/` contains scope audits, derivations, priority notes, summaries,
  and other preparation artifacts.
- `Lessons/` holds only genuine quiz-specific gap lessons or grouped synthesis
  lessons.

Study-guide membership and progress sections enclosed by `update-progress`
comments are generated or maintained by the progress workflow.

## Content flow

For a lecture unit:

```text
raw transcript
    → cleaned transcript and lecture notes
    → normalized PRE and LEC quiz blocks
    → combined dated unit note
    → one focused lesson per problem
    → topics.csv, TOC.md, and Home.md progress views
```

For homework or a practice quiz:

```text
imported assignment and images
    → cleaned dated problem set
    → one focused lesson per problem
    → topics.csv, TOC.md, and Home.md progress views
```

## Adding a new unit

1. Place the unit in the correct module using the established dated naming
   convention.
2. Keep imported or captured material under `Source/`.
3. Normalize the questions into the matching main Markdown file.
4. Store images under the unit's `Source/` tree and use relative links.
5. Create one focused lesson for each problem that needs instruction.
6. Assign stable lesson metadata and register new lessons in `topics.csv`.
7. Update or regenerate the table of contents and progress views.
8. If the unit contributes to a quiz, link its lessons from the relevant study
   guide instead of copying them.

## Current scaffolding

- `M6/` is ready for future course material.
- The prerequisite registry and local `Prerequisites/` folders are ready for a
  future dependency workflow.
- Some homework main notes still contain skeleton lesson-link placeholders;
  lesson files and the central topic registry are the authoritative references
  until those indexes are filled.

