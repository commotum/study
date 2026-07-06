# MA Quiz Block Conversion Goal Prompt

Copy/paste the text block below to start a fresh Codex goal.

```text
Goal: Finish converting Math Academy multiple-choice questions in /Users/jake/Developer/study/vault/MA to the obsidian-quiz-blocks radio format, mark correct answers, and keep the markdown plus CSV ledgers consistent. Optimize for completing the true task without doom-looping: use scripts for mechanical conversion, use sub-agents for bounded manual solving, and do not search for answer keys that are not present.

Repo and scope:
- Repo root: /Users/jake/Developer/study
- Primary vault scope: /Users/jake/Developer/study/vault/MA
- Plugin format reference: plugins/obsidian-quiz-blocks
- Primary target: multiple-choice questions only.
- Do not expand into free-response/select-list cleanup unless it is directly adjacent, trivial, and does not slow MCQ completion.

Important known rules:
- Disk state is authoritative. Recount from files at the start of every continuation.
- Separate structural conversion from answer solving.
- Unknown answers should use the existing missing marker: MA_ANSWER_MISSING.
- The manual-solving queue should be built only from quiz blocks that still contain MA_ANSWER_MISSING.
- Do not search for answer keys. The source data does not contain answer keys.
- Image-answer-bank MCQs use the deterministic rule: the correct option is the option whose answer image id is 1.
- Manual solving means solving the math from the question/options/local images, not digging for hidden keys.

Key files and scripts:
- Global ledger: vault/MA/questions.csv
- Group ledgers: vault/MA/<group>/questions.csv
- Current missing-answer queue: util/ma_missing_answer_queue.csv
- Structural converter: util/convert_mcq_to_quiz.py
- Mass structural driver: util/mass_convert_ma_mcqs.py
- Deterministic image answer converter: util/convert_image_answer_mcqs.py
- Missing-answer queue builder: util/build_ma_missing_answer_queue.py
- Batch answer applier: util/apply_ma_answer_batch.py
- Older/smaller answer marker if useful: util/mark_quiz_answers.py

Ledger fields to maintain:
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

Execution order:

1. Recount current progress from disk.
   - Read vault/MA/questions.csv and all vault/MA/<group>/questions.csv files.
   - Report MCQ converted-and-verified, MCQ needs-answer, MCQ blank/unconverted, and all-question totals as secondary context.
   - Run util/build_ma_missing_answer_queue.py before reporting the active queue size.
   - Do not trust prior chat-memory counts except as hints.

2. Audit for mechanical leftovers.
   - Check for raw checklist MCQs:
     rg -n "^- \[[ xX]\] [A-Za-z]\." vault/MA -g '*.md'
   - Check for deterministic image-answer questions still unmarked:
     python3 util/convert_image_answer_mcqs.py vault/MA --dry-run --summary-only --report-json /private/tmp/ma_image_answer_check.json
   - Check for malformed fence artifacts such as ```--- if relevant.
   - Run scoped whitespace checks:
     git diff --check -- vault/MA util

3. Finish structural conversion before manual solving.
   - Use util/mass_convert_ma_mcqs.py and util/convert_mcq_to_quiz.py where possible.
   - Convert raw MCQs into obsidian-quiz-blocks radio format.
   - If no answer is known, leave MA_ANSWER_MISSING in the block.
   - For structurally converted but unsolved MCQs, ledger state should be:
     quiz-block-format=obsidian-quiz-blocks
     quiz-block-type=radio
     quiz-status=needs-answer
   - Do not mark quiz-status=converted-and-verified until exactly one correct answer is marked.

4. Auto-mark deterministic image-answer-bank MCQs.
   - Use util/convert_image_answer_mcqs.py or a narrow script using the same rule.
   - Correct answer rule: answer image id 1.
   - These require no manual solving.
   - Ledger state should be:
     quiz-answer-labels=<correct label>
     quiz-answer-source=image-id
     quiz-answer-rule=answer-image-id-1
     quiz-status=converted-and-verified

5. Build the manual-answer queue.
   - Run:
     python3 util/build_ma_missing_answer_queue.py
   - The queue should come only from MA_ANSWER_MISSING blocks.
   - Queue rows should preserve lesson path, topic id, question id, prompt, options, image paths if present, and copied course/group locations.
   - Use source JSON/question metadata to map question_number to question_id when needed. Do not assume CSV row order.

6. Use sub-agents for manual solving when available.
   - Discover multi-agent tools with tool_search if they are not already loaded.
   - Agents are read-only: they solve and report answers, they do not edit files.
   - Assign small batches by topic/lesson so context stays focused.
   - Ask agents to return only:
     topic-id:question-id=label | short reasoning | confidence
   - Main agent applies all edits centrally with scripts.
   - If an agent gives low confidence or conflicting reasoning, manually solve that item before applying.

7. Apply answers in batches.
   - Prefer util/apply_ma_answer_batch.py, for example:
     python3 util/apply_ma_answer_batch.py --answer TOPIC_ID:QUESTION_ID=LABEL --answer TOPIC_ID:QUESTION_ID=LABEL
   - The applier should update all copied lesson blocks plus global/group ledgers.
   - Final verified ledger state should be:
     quiz-block-format=obsidian-quiz-blocks
     quiz-block-type=radio
     quiz-answer-labels=<correct label>
     quiz-status=converted-and-verified
     quiz-answer-source=manual or image-id
     quiz-answer-rule=label or answer-image-id-1
   - quiz-updated-courses should reflect actual updated course copies.

8. Audit every completed batch.
   - Re-run util/build_ma_missing_answer_queue.py.
   - For each applied question id, verify:
     exactly one correct: true in every copied quiz block
     no MA_ANSWER_MISSING remains for that id
     global and group ledgers match the selected answer
     quiz-answer-source/rule/status are correct
   - Run:
     git diff --check -- vault/MA util
   - If full git diff --check reports unrelated files outside vault/MA/util, note them but do not touch them unless explicitly asked.

9. Avoid loops and preserve throughput.
   - Do not repeatedly revisit the same blocked lesson.
   - If a file/topic cannot be converted or solved from available prompt/images, record a skip reason and continue.
   - Work in batches, report batch throughput, and keep the next queue ready.
   - The useful progress metric is MCQ converted-and-verified / total MCQ rows, plus MCQ needs-answer remaining.

Definition of done:
- All imported Math Academy multiple-choice lesson questions found under vault/MA are in obsidian-quiz-blocks radio format.
- All deterministic image-answer-bank MCQs are marked using the answer-image-id-1 rule.
- All remaining answerable MCQs are manually solved and marked.
- vault/MA/questions.csv and group questions.csv files agree with the markdown.
- No MA_ANSWER_MISSING remains except explicitly documented blocked/skipped questions.
- Scoped verification passes for vault/MA and util.
```
