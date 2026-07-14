# Summing a Telescoping Series from Consecutive Factors

## Table of Contents

- [Introduction](#introduction)
- [Rewrite the Term as a Difference](#rewrite-the-term-as-a-difference)
- [Expose the Cancellation in a Partial Sum](#expose-the-cancellation-in-a-partial-sum)
- [Take the Limit of the Partial Sums](#take-the-limit-of-the-partial-sums)
- [Check the Denominator Gap](#check-the-denominator-gap)
- [Summary](#summary)

## Prerequisites

- Add and subtract rational expressions with linear denominators.
- Interpret the $N$th partial sum $s_N$ as the sum of the first $N$ terms.
- Use $\displaystyle \lim_{N\to\infty}\frac{1}{N+c}=0$ for a constant $c$.

---

<a id="introduction"></a>
## Introduction

When a series term has a denominator made from consecutive linear factors, look for a difference of consecutive reciprocals. For example,

$$
\frac{1}{(n+1)(n+2)}
=\frac{1}{n+1}-\frac{1}{n+2}.
$$

This rewrite makes neighboring terms cancel, so the series is called **telescoping**. The series converges only when the limit of its partial sums is a finite number. The reliable procedure is:

1. rewrite the summand as a difference;
2. form the finite partial sum $s_N$;
3. display enough terms to verify the cancellation;
4. simplify $s_N$ and take its limit.

---

<a id="rewrite-the-term-as-a-difference"></a>
## Rewrite the Term as a Difference

**Example:** Rewrite $\displaystyle \frac{1}{(n+3)(n+4)}$ as a difference of two fractions.

**Explanation**

The factors differ by $1$, so try the reciprocal of the first factor minus the reciprocal of the second:

$$
\frac{1}{n+3}-\frac{1}{n+4}
=\frac{(n+4)-(n+3)}{(n+3)(n+4)}
=\frac{1}{(n+3)(n+4)}.
$$

Combining the proposed difference is a quick way to check both its order and its sign.

```quiz
type: radio
id: problem-4-rewrite-1
content: |-
  Which decomposition is equal to $\dfrac{1}{(n+5)(n+6)}$?
options:
- id: rewrite-a
  content: |-
    $\dfrac{1}{n+5}-\dfrac{1}{n+6}$
  correct: true
- id: rewrite-b
  content: |-
    $\dfrac{1}{n+6}-\dfrac{1}{n+5}$
- id: rewrite-c
  content: |-
    $\dfrac{1}{n+5}+\dfrac{1}{n+6}$
- id: rewrite-d
  content: |-
    $\dfrac{1}{n+5}-\dfrac{1}{n+5}$
```

---

<a id="expose-the-cancellation-in-a-partial-sum"></a>
## Expose the Cancellation in a Partial Sum

**Example:** Find the $N$th partial sum of

$$
\sum_{n=1}^{\infty}\frac{1}{(n+2)(n+3)}.
$$

**Explanation**

First rewrite the summand, but keep the sum finite:

$$
s_N=\sum_{n=1}^{N}\left(\frac{1}{n+2}-\frac{1}{n+3}\right).
$$

Now display the first few and final terms:

$$
\begin{aligned}
s_N
&=\left(\frac13-\frac14\right)
+\left(\frac14-\frac15\right)
+\cdots
+\left(\frac{1}{N+2}-\frac{1}{N+3}\right)\\
&=\frac13-\frac{1}{N+3}.
\end{aligned}
$$

Every middle reciprocal appears once positively and once negatively. Only the first positive term and the last negative term survive.

For boundary bookkeeping, evaluate the first positive fraction at $n=1$ and the last negative fraction at $n=N$. This avoids the common error of keeping the last positive fraction instead.

```quiz
type: radio
id: problem-4-cancel-1
content: |-
  Let $s_N=\displaystyle\sum_{n=1}^{N}\dfrac{1}{(n+4)(n+5)}$. Which formula results after cancellation?
options:
- id: cancel-a
  content: |-
    $s_N=\dfrac15-\dfrac{1}{N+5}$
  correct: true
- id: cancel-b
  content: |-
    $s_N=\dfrac14-\dfrac{1}{N+4}$
  feedback: |-
    These are not the boundary terms obtained by substituting $n=1$ and $n=N$.
- id: cancel-c
  content: |-
    $s_N=\dfrac15+\dfrac{1}{N+5}$
  feedback: |-
    The final surviving term comes from subtraction, so its sign is negative.
- id: cancel-d
  content: |-
    $s_N=\dfrac{1}{N+4}-\dfrac{1}{N+5}$
  feedback: |-
    The first positive boundary term $1/5$ does not cancel.
```

---

<a id="take-the-limit-of-the-partial-sums"></a>
## Take the Limit of the Partial Sums

**Example:** Determine whether

$$
\sum_{n=1}^{\infty}\frac{1}{(n+1)(n+2)}
$$

converges, and find its sum if it does.

**Explanation**

Use the consecutive-factor decomposition:

$$
\frac{1}{(n+1)(n+2)}
=\frac{1}{n+1}-\frac{1}{n+2}.
$$

Then the $N$th partial sum is

$$
\begin{aligned}
s_N
&=\left(\frac12-\frac13\right)
+\left(\frac13-\frac14\right)
+\cdots
+\left(\frac{1}{N+1}-\frac{1}{N+2}\right)\\
&=\frac12-\frac{1}{N+2}.
\end{aligned}
$$

Because $\displaystyle \frac{1}{N+2}\to 0$,

$$
\sum_{n=1}^{\infty}\frac{1}{(n+1)(n+2)}
=\lim_{N\to\infty}s_N
=\frac12.
$$

The limit is finite, so the series is **convergent**, with sum $\boxed{\frac12}$.

```quiz
type: radio
id: problem-4-limit-1
content: |-
  Determine the sum of $\displaystyle\sum_{n=1}^{\infty}\dfrac{2}{(n+2)(n+3)}$.
options:
- id: limit-a
  content: |-
    The series converges to $\dfrac23$.
  correct: true
- id: limit-b
  content: |-
    The series converges to $\dfrac13$.
- id: limit-c
  content: |-
    The series converges to $2$.
- id: limit-d
  content: |-
    The series diverges because it has infinitely many positive terms.
  feedback: |-
    Infinitely many positive terms can have a finite sum; the partial-sum limit decides convergence.
```

```quiz
type: radio
id: problem-4-convergence-reason-1
content: |-
  Which statement is sufficient to prove that a telescoping series converges to $L$?
options:
- id: reason-a
  content: |-
    Its terms approach $0$.
  feedback: |-
    This condition is necessary but not sufficient for convergence.
- id: reason-b
  content: |-
    Its terms are all positive.
- id: reason-c
  content: |-
    Its $N$th partial sum satisfies $\displaystyle\lim_{N\to\infty}s_N=L$, where $L$ is finite.
  correct: true
- id: reason-d
  content: |-
    Its partial sums contain fractions whose denominators grow.
```

---

<a id="check-the-denominator-gap"></a>
## Check the Denominator Gap

**Example:** Rewrite $\displaystyle \frac{1}{(n+1)(n+3)}$ as a difference of reciprocals.

**Explanation**

The factors now differ by $2$. A direct difference produces a numerator of $2$:

$$
\frac{1}{n+1}-\frac{1}{n+3}
=\frac{2}{(n+1)(n+3)}.
$$

Therefore, divide the difference by the gap:

$$
\frac{1}{(n+1)(n+3)}
=\frac12\left(\frac{1}{n+1}-\frac{1}{n+3}\right).
$$

The common trap is to assume the coefficient is always $1$. Combine the fractions to check the numerator before summing.

```quiz
type: radio
id: problem-4-gap-1
content: |-
  Which decomposition is equal to $\dfrac{1}{(n+2)(n+5)}$?
options:
- id: gap-a
  content: |-
    $\dfrac13\left(\dfrac{1}{n+2}-\dfrac{1}{n+5}\right)$
  correct: true
- id: gap-b
  content: |-
    $\dfrac{1}{n+2}-\dfrac{1}{n+5}$
- id: gap-c
  content: |-
    $3\left(\dfrac{1}{n+2}-\dfrac{1}{n+5}\right)$
- id: gap-d
  content: |-
    $\dfrac13\left(\dfrac{1}{n+5}-\dfrac{1}{n+2}\right)$
```

---

<a id="summary"></a>
## Summary

When the summand contains two shifted linear factors, try a difference of their reciprocals.

1. Check the rewrite by recombining the fractions; the denominator gap may create a coefficient.
2. Replace the infinite series temporarily with the finite partial sum $s_N$.
3. Write the boundary terms and cancel only terms that appear with opposite signs.
4. Take $\displaystyle \lim_{N\to\infty}s_N$. A finite limit means the series converges to that value.

The fact that the individual terms approach $0$ does not by itself prove convergence; the limit must be taken on the partial sums.

For the assigned series, $s_N=\dfrac12-\dfrac{1}{N+2}$, so the series converges to $\boxed{\dfrac12}$.
