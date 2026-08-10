# Recognizing a Constant Multiple of a Power Sequence

## Table of Contents

- [Introduction](#introduction)
- [Pair Each Term With Its Index](#pair-each-term-with-its-index)
- [Test a Power Benchmark](#test-a-power-benchmark)
- [Write and Verify the Formula](#write-and-verify-the-formula)
- [Distinguish Power Patterns From Geometric Patterns](#distinguish-power-patterns-from-geometric-patterns)
- [Summary](#summary)

## Prerequisites

- [Introduction to Sequences](<Introduction to Sequences - 2271.md>)
- Evaluate expressions such as $2n^3$ at positive integer values of $n$.

---

<a id="introduction"></a>
## Introduction

When a sequence is given as a list, the position of each term is an input:

$$
1\mapsto s_1,\qquad 2\mapsto s_2,\qquad 3\mapsto s_3,\ldots
$$

For a sequence that appears to follow a power pattern, test a simple benchmark such as $n^2$ or $n^3$. If

$$
\frac{s_n}{n^p}
$$

has the same value for every listed term, call that constant $c$. The explicit formula is then

$$
s_n=cn^p.
$$

The key is to compare every term with the power of its own index—not merely to look at how large the terms are.

---

<a id="pair-each-term-with-its-index"></a>
## Pair Each Term With Its Index

**Example:** Find an explicit formula for the sequence

$$
3,24,81,192,375,\ldots
$$

**Explanation**

First pair each term with its index and write the cubic benchmark beside it.

| $n$ | $s_n$ | $n^3$ | $s_n/n^3$ |
| ---: | ---: | ---: | ---: |
| $1$ | $3$ | $1$ | $3$ |
| $2$ | $24$ | $8$ | $3$ |
| $3$ | $81$ | $27$ | $3$ |
| $4$ | $192$ | $64$ | $3$ |
| $5$ | $375$ | $125$ | $3$ |

Every term is $3$ times the cube of its index, so

$$
s_n=3n^3.
$$

```quiz
type: radio
id: problem-3-q1
content: |-
  Which formula generates the sequence

  $$4,32,108,256,500,\ldots?$$
options:
- id: problem-3-q1-a
  content: |-
    $s_n=4n^2$
- id: problem-3-q1-b
  content: |-
    $s_n=4n^3$
  correct: true
- id: problem-3-q1-c
  content: |-
    $s_n=n^4$
- id: problem-3-q1-d
  content: |-
    $s_n=4^n$
- id: problem-3-q1-e
  content: |-
    $s_n=4(n-1)^3$
```

---

<a id="test-a-power-benchmark"></a>
## Test a Power Benchmark

**Example:** Decide whether

$$
5,40,135,320,625,\ldots
$$

is a constant multiple of $n^2$ or $n^3$.

**Explanation**

Use a term beyond the first, because $1^2=1^3=1$ cannot distinguish the powers. At $n=2$,

$$
\frac{s_2}{2^2}=\frac{40}{4}=10,
\qquad
\frac{s_2}{2^3}=\frac{40}{8}=5.
$$

The cubic test gives the possible scale factor $5$. Check another index:

$$
\frac{s_3}{3^3}=\frac{135}{27}=5.
$$

Continuing the check shows the same factor, so the formula is

$$
s_n=5n^3.
$$

One matching term suggests a rule; several matching terms verify that it fits the displayed pattern.

```quiz
type: radio
id: problem-3-q2
content: |-
  The sequence $6,24,54,96,150,\ldots$ is a constant multiple of which benchmark?
options:
- id: problem-3-q2-a
  content: |-
    $n$
- id: problem-3-q2-b
  content: |-
    $n^2$
  correct: true
- id: problem-3-q2-c
  content: |-
    $n^3$
- id: problem-3-q2-d
  content: |-
    $2^n$
- id: problem-3-q2-e
  content: |-
    $n+2$
```

---

<a id="write-and-verify-the-formula"></a>
## Write and Verify the Formula

**Example:** The first terms of a sequence are

$$
2,16,54,128,250,\ldots
$$

Find a formula for $s_n$.

**Explanation**

Compare each term with $n^3$:

| $n$ | $s_n$ | $n^3$ | $s_n/n^3$ |
| ---: | ---: | ---: | ---: |
| $1$ | $2$ | $1$ | $2$ |
| $2$ | $16$ | $8$ | $2$ |
| $3$ | $54$ | $27$ | $2$ |
| $4$ | $128$ | $64$ | $2$ |
| $5$ | $250$ | $125$ | $2$ |

The normalized value is always $2$, so

$$
\boxed{s_n=2n^3}.
$$

Finally, substitute at least two indices into the proposed formula:

$$
s_2=2(2^3)=16,
\qquad
s_5=2(5^3)=250.
$$

Both outputs match the listed terms.

```quiz
type: radio
id: problem-3-q3
content: |-
  Assuming the displayed pattern continues, which formula generates

  $$-2,-16,-54,-128,-250,\ldots?$$
options:
- id: problem-3-q3-a
  content: |-
    $s_n=-2n^2$
- id: problem-3-q3-b
  content: |-
    $s_n=2(-n)^2$
- id: problem-3-q3-c
  content: |-
    $s_n=-2n^3$
  correct: true
- id: problem-3-q3-d
  content: |-
    $s_n=(-2n)^3$
- id: problem-3-q3-e
  content: |-
    $s_n=-2^n$
```

---

<a id="distinguish-power-patterns-from-geometric-patterns"></a>
## Distinguish Power Patterns From Geometric Patterns

**Example:** Explain why

$$
2,16,54,128,250,\ldots
$$

is not geometric even though its formula contains a power.

**Explanation**

In a geometric sequence, the index appears in the exponent, as in $ar^{n-1}$, and consecutive terms have a constant ratio. Here,

$$
\frac{16}{2}=8
\qquad\text{but}\qquad
\frac{54}{16}=\frac{27}{8},
$$

so the consecutive-term ratio is not constant.

For $s_n=2n^3$, the index is the base being cubed. The useful constant is instead

$$
\frac{s_n}{n^3}=2.
$$

```quiz
type: radio
id: problem-3-q4
content: |-
  Which observation correctly supports the formula $a_n=7n^3$?
options:
- id: problem-3-q4-a
  content: |-
    The difference $a_n-a_{n-1}$ is always $7$.
- id: problem-3-q4-b
  content: |-
    The ratio $a_n/a_{n-1}$ is always $7$.
- id: problem-3-q4-c
  content: |-
    The ratio $a_n/n^3$ is always $7$.
  correct: true
- id: problem-3-q4-d
  content: |-
    The value $a_n- n^3$ is always $7$.
- id: problem-3-q4-e
  content: |-
    The value $a_n/3^n$ is always $7$.
```

---

<a id="summary"></a>
## Summary

When listed terms resemble powers of their positions:

1. Pair each term $s_n$ with its index $n$.
2. Test a benchmark such as $n^2$ or $n^3$.
3. Compute $s_n/n^p$ for several listed terms.
4. If the quotient is the same constant $c$, write $s_n=cn^p$.
5. Substitute multiple indices to verify the formula.

The main trap is confusing a power sequence such as $cn^3$ with a geometric sequence such as $cr^n$. In $cn^3$, the index is the base; in $cr^n$, the index is the exponent.
