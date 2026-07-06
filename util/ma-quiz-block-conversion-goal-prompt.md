# MA Quiz Block Conversion Goal Prompt

Copy/paste the text block below to start a fresh Codex goal.

```text
Goal: Finish converting Math Academy multiple-choice questions in /Users/jake/Developer/study/vault/MA to the obsidian-quiz-blocks radio format, mark correct answers, and keep all markdown copies plus CSV ledgers consistent. Optimize for the true intent: finish the conversion efficiently without doom-looping, using scripts for mechanical edits and bounded read-only sub-agents for manual solving where useful.

Repo and scope:
- Repo root: /Users/jake/Developer/study
- Primary vault scope: /Users/jake/Developer/study/vault/MA
- Plugin format reference: /Users/jake/Developer/study/plugins/obsidian-quiz-blocks
- Target: multiple-choice questions in Math Academy lesson markdown under vault/MA.
- Discover the current group/course structure from disk; do not hardcode an old group list.
- Do not expand into free-response/select-list cleanup unless it directly blocks MCQ conversion.

Non-negotiable rules:
- Disk state is authoritative. Recount from files at the start of every continuation.
- Do not trust chat-memory counts except as hints.
- Separate structural conversion from answer solving.
- Unknown answers use the existing marker: MA_ANSWER_MISSING.
- Manual-solving queue must be built only from blocks that still contain MA_ANSWER_MISSING.
- Do not search for answer keys. The source data does not contain answer keys.
- Image-answer-bank MCQs are deterministic: the correct option is the option whose answer image id/index is 1.
- Do not manually solve deterministic image-answer-bank MCQs; apply the image id rule.
- Manual solving means solving from the prompt/options/local images only.
- If a prompt appears inconsistent with every displayed option, record a skip reason and move on.
- Do not revert unrelated dirty work.

Key files and scripts:
- Global ledger: vault/MA/questions.csv
- Group ledgers: vault/MA/<group>/questions.csv
- Missing-answer queue: util/ma_missing_answer_queue.csv
- Skip ledger for bad/inconsistent options: util/ma_answer_skips.csv
- Structural converter: util/convert_mcq_to_quiz.py
- Mass structural driver: util/mass_convert_ma_mcqs.py
- Deterministic image answer converter: util/convert_image_answer_mcqs.py
- Missing-answer queue builder: util/build_ma_missing_answer_queue.py
- Batch answer applier: util/apply_ma_answer_batch.py
- Goal prompt: util/ma-quiz-block-conversion-goal-prompt.md

Ledger fields to maintain:
- quiz-block-format
- quiz-block-type
- quiz-answer-labels
- quiz-updated-courses
- quiz-status
- quiz-answer-source
- quiz-answer-rule

Best order of execution:

1. Recount current progress from disk.
   - Read vault/MA/questions.csv.
   - Read every vault/MA/<group>/questions.csv discovered on disk.
   - Report:
     MCQ converted-and-verified / total MCQ
     MCQ needs-answer
     MCQ blank/unconverted
     all-question converted-and-verified / total all questions
     per-group MCQ counts
   - Run:
     python3 util/build_ma_missing_answer_queue.py
   - Report queue row count and unique topic-id/question-id count.

2. Run mechanical audits before editing.
   - Raw checklist MCQs:
     rg -n "^- \[[ xX]\] [A-Za-z]\." vault/MA -g '*.md'
   - Deterministic image-answer questions still unmarked:
     python3 util/convert_image_answer_mcqs.py vault/MA --dry-run --summary-only --report-json /private/tmp/ma_image_answer_check.json
   - Scoped whitespace/syntax check:
     git diff --check -- vault/MA util

3. Finish structural conversion first.
   - Use util/mass_convert_ma_mcqs.py and util/convert_mcq_to_quiz.py where possible.
   - Convert raw MCQs into obsidian-quiz-blocks radio format.
   - If the correct answer is not known during conversion, leave MA_ANSWER_MISSING.
   - Structurally converted but unsolved MCQs should have:
     quiz-block-format=obsidian-quiz-blocks
     quiz-block-type=radio
     quiz-status=needs-answer
   - Do not set converted-and-verified until exactly one correct answer is marked.

4. Auto-mark deterministic image-answer-bank MCQs.
   - Use util/convert_image_answer_mcqs.py or a narrow script that applies the same rule.
   - Correct answer rule: answer image id/index 1.
   - Expected verified ledger state:
     quiz-answer-labels=<correct label>
     quiz-answer-source=image-id
     quiz-answer-rule=answer-image-id-1
     quiz-status=converted-and-verified

5. Build the manual-answer queue from remaining missing markers.
   - Run:
     python3 util/build_ma_missing_answer_queue.py
   - Queue rows should preserve lesson path, topic id, question id, prompt, options, local image paths if present, and copied course/group locations.
   - Use source metadata to map question_number to question_id when needed. Do not assume CSV row order.

6. Use sub-agents surgically for manual solving when helpful.
   - Discover multi-agent tools with tool_search if needed.
   - Agents are read-only: they solve and report answers, they do not edit files.
   - Assign small batches by lesson/topic/course cluster.
   - Tell agents not to search for answer keys.
   - Ask agents to return only:
     topic-id:question-id=label | short reasoning | confidence
   - Main agent applies all edits centrally with scripts.
   - Manually review low-confidence, ambiguous, or conflicting answers before applying.

7. Apply answers in batches.
   - Prefer:
     python3 util/apply_ma_answer_batch.py --answer TOPIC_ID:QUESTION_ID=LABEL --answer TOPIC_ID:QUESTION_ID=LABEL
   - The applier should update every copied lesson block plus global/group ledgers.
   - Final verified ledger state should be:
     quiz-block-format=obsidian-quiz-blocks
     quiz-block-type=radio
     quiz-answer-labels=<correct label>
     quiz-status=converted-and-verified
     quiz-answer-source=manual or image-id
     quiz-answer-rule=label or answer-image-id-1
   - quiz-updated-courses should reflect actual updated course copies.

8. Audit every applied batch.
   - Re-run:
     python3 util/build_ma_missing_answer_queue.py
   - For each applied topic/question id, verify:
     no MA_ANSWER_MISSING remains for that id
     exactly one correct: true exists in every copied quiz block
     vault/MA/questions.csv matches the selected answer
     every relevant group questions.csv matches the selected answer
     quiz-answer-source/rule/status are correct
   - Run:
     git diff --check -- vault/MA util
   - If full git diff --check reports unrelated files outside vault/MA/util, note them but do not touch them unless asked.

9. Handle inconsistent or blocked questions without stalling.
   - If solving gives an answer that is not among the displayed options, append a row to util/ma_answer_skips.csv with topic-id, question-id, and a concise reason.
   - Leave MA_ANSWER_MISSING in that block.
   - Continue with the next batch.
   - Do not repeatedly revisit the same blocked lesson.

10. Report progress in useful units.
   - Report MCQ converted-and-verified / total MCQ.
   - Report MCQ needs-answer remaining.
   - Report MCQ blank/unconverted remaining.
   - Report queue unique id count.
   - Report batch throughput: answers applied, files changed, queue decrease, audits passed.

Definition of done:
- All imported Math Academy MCQs found under vault/MA are in obsidian-quiz-blocks radio format.
- All deterministic image-answer-bank MCQs are marked using answer-image-id-1.
- All answerable non-image MCQs are manually solved and marked.
- vault/MA/questions.csv and every group questions.csv agree with the markdown.
- No MA_ANSWER_MISSING remains except explicitly documented skipped questions in util/ma_answer_skips.csv.
- Scoped verification passes:
  git diff --check -- vault/MA util
```
