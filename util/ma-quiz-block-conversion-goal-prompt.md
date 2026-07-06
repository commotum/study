# MA Quiz Block Conversion Goal Prompt

Use this as the goal prompt for a fresh Codex session:

```text
Goal: Finish converting Math Academy multiple-choice questions in /Users/jake/Developer/study/vault/MA to the obsidian-quiz-blocks radio format, with correct answers marked and ledgers updated, without doom-looping on manual solving.

Context:
- Repo root: /Users/jake/Developer/study
- Vault root: /Users/jake/Developer/study/vault/MA
- Plugin format already reviewed in plugins/obsidian-quiz-blocks.
- Existing helper scripts:
  - util/convert_mcq_to_quiz.py
  - util/mark_quiz_answers.py
  - util/convert_image_answer_mcqs.py
- Global ledger: vault/MA/questions.csv
- Group ledgers: vault/MA/<group>/questions.csv
- The CSV fields use hyphenated names, including:
  - topic-id
  - step-id
  - question-id
  - question-type
  - answer-cardinality
  - quiz-block-format
  - quiz-block-type
  - quiz-answer-labels
  - quiz-updated-courses
  - quiz-status
  - quiz-answer-source
  - quiz-answer-rule

Operating principle:
Separate structural conversion from answer solving. Do not manually solve questions while converting markdown shape. First get every mechanically recognizable MCQ into quiz-block format with a missing-answer marker, then solve only the remaining answer queue.

Required execution order:

1. Recount current progress from disk.
   - Read vault/MA/questions.csv and group questions.csv files.
   - Report converted MCQ rows, remaining MCQ rows, and total converted rows.
   - Treat disk state as authoritative; do not rely on prior chat memory.

2. Mass-convert MCQs structurally.
   - Use scripts where possible, especially util/convert_mcq_to_quiz.py.
   - Convert raw checklist/list MCQs to obsidian-quiz-blocks radio format.
   - If the correct answer is not known, leave the established missing marker, e.g. MA_ANSWER_MISSING.
   - For structurally converted but unsolved questions, update ledgers only to an intermediate state:
     - quiz-block-format=obsidian-quiz-blocks
     - quiz-block-type=radio
     - quiz-status=needs-answer
   - Do not mark quiz-status=converted-and-verified until an answer is actually marked.

3. Auto-mark deterministic image answer-bank questions.
   - For image-option MCQs where the established rule applies, the correct answer is the option whose answer image id is 1.
   - Use util/convert_image_answer_mcqs.py or a narrow script built on the same rule.
   - These require no manual solving.
   - Set ledger fields:
     - quiz-answer-source=image-id
     - quiz-answer-rule=answer-image-id-1
     - quiz-status=converted-and-verified

4. Build a missing-answer work queue.
   - Search only for quiz blocks containing MA_ANSWER_MISSING.
   - Queue entries should include:
     - lesson path
     - group/course copy paths that must be updated together
     - topic id
     - question id
     - prompt text
     - options
     - local prompt/image paths, if present
   - Use source JSON to map question_number -> question_id. Do not assume ledger row order.

5. Use sub-agents for manual solving when available.
   - Use tool_search to discover multi-agent tools if they are not already loaded.
   - Sub-agents should be read-only by default.
   - Assign agents small batches by lesson/topic.
   - Agent output should be only:
     - question-id -> answer label
     - short reasoning
     - uncertainty flags
   - Agents should not edit markdown or CSV files.
   - The main agent applies all edits centrally and surgically.

6. Do not search for answer keys.
   - There are no answer keys available in the local source data.
   - Do not waste time digging for keys.
   - For deterministic image-answer-bank questions, use the image id rule.
   - For all other missing answers, solve manually from the prompt, options, and local images.

7. Apply answers in batches.
   - Use util/mark_quiz_answers.py where possible.
   - Update both global and group ledgers.
   - Final verified ledger fields should be:
     - quiz-block-format=obsidian-quiz-blocks
     - quiz-block-type=radio
     - quiz-answer-labels=<correct label>
     - quiz-status=converted-and-verified
     - quiz-answer-source=manual or image-id
     - quiz-answer-rule=label or answer-image-id-1
   - quiz-updated-courses should list the actual updated course copies.

8. Audit every completed batch.
   - Check no MA_ANSWER_MISSING remains in completed files.
   - Check exactly one correct: true per radio quiz block.
   - Check no raw checklist MCQs remain in files claimed complete.
   - Check markdown trailing whitespace in touched files.
   - Check global and group ledgers agree with the markdown.
   - Run scoped git diff --check when practical.

9. Keep scope disciplined.
   - Primary scope is multiple-choice questions.
   - Do not expand into free-response/select-list cleanup unless those rows are already represented as radio quiz blocks in the touched lesson and marking them is trivial.
   - If a topic has no imported lesson path, skip it with a note and continue.
   - Do not repeatedly revisit the same blocked file. Record it in a skip list with the reason.

10. Progress reporting.
   - Report progress in terms of MCQ rows converted/verified and MCQ rows remaining.
   - Include all-question totals only as secondary context.
   - Report batch throughput and blockers.

Definition of done:
- All imported MA multiple-choice lesson questions that can be found in vault/MA are in obsidian-quiz-blocks radio format.
- All deterministic image-answer-bank MCQs are marked using the answer-image-id-1 rule.
- All remaining MCQs with available prompts/images are manually solved and marked.
- Global and group questions.csv ledgers agree with the markdown files.
- No MA_ANSWER_MISSING remains except for explicitly documented blocked/skipped questions.
```
