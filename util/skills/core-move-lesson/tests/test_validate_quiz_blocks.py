#!/usr/bin/env python3
"""Regression tests for the core-move quiz-block validator."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_quiz_blocks import Issue, validate_file  # noqa: E402


class QuizBlockFieldTests(unittest.TestCase):
    def validate_issues(self, markdown: str) -> list[Issue]:
        args = SimpleNamespace(
            allow_no_quiz=False,
            allow_raw_mcq=False,
            require_radio_practice=False,
            strict_ids=False,
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "lesson.md"
            path.write_text(markdown, encoding="utf-8")
            issues, _ = validate_file(path, args)
        return issues

    def validate(self, markdown: str) -> list[str]:
        return [issue.message for issue in self.validate_issues(markdown)]

    def test_radio_rejects_root_feedback(self) -> None:
        issues = self.validate(
            """```quiz
type: radio
content: Question?
options:
- content: A
  correct: true
- content: B
feedback: This belongs on an option.
```
"""
        )
        self.assertIn("unknown top-level field for radio quiz: feedback", issues)

    def test_radio_accepts_option_feedback(self) -> None:
        issues = self.validate(
            """```quiz
type: radio
content: Question?
options:
- content: A
  correct: true
  feedback: Correct.
- content: B
  feedback: Try again.
```
"""
        )
        self.assertEqual([], issues)

    def test_radio_accepts_common_root_fields(self) -> None:
        issues = self.validate(
            """```quiz
type: radio
id: q-1
content: Question?
gated: true
shuffle: true
options:
- content: A
  correct: true
- content: B
```
"""
        )
        self.assertEqual([], issues)

    def test_quoted_root_feedback_is_still_rejected(self) -> None:
        markdown = """```quiz
type: radio
content: Question?
options:
- content: A
  correct: true
- content: B
"feedback": This belongs on an option.
```
"""
        issues = self.validate_issues(markdown)
        feedback_issue = next(issue for issue in issues if "feedback" in issue.message)
        self.assertEqual("unknown top-level field for radio quiz: feedback", feedback_issue.message)
        self.assertEqual(8, feedback_issue.line)

    def test_blank_accepts_root_feedback(self) -> None:
        issues = self.validate(
            """```quiz
type: blank
content: The answer is ==42==.
feedback: Check the arithmetic.
require_exact: false
```
"""
        )
        self.assertEqual([], issues)

    def test_radio_rejects_blank_only_require_exact(self) -> None:
        issues = self.validate(
            """```quiz
type: radio
content: Question?
require_exact: false
options:
- content: A
  correct: true
- content: B
```
"""
        )
        self.assertIn("unknown top-level field for radio quiz: require_exact", issues)

    def test_free_accepts_root_feedback_and_correct(self) -> None:
        issues = self.validate(
            """```quiz
type: free
content: Explain the result.
correct: A reference answer.
feedback: Compare signs and units.
```
"""
        )
        self.assertEqual([], issues)


if __name__ == "__main__":
    unittest.main()
