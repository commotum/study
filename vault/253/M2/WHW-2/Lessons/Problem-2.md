# Limits of Nonlinear Recursive Sequences by Fixed Points

## Table of Contents

- [Introduction](#introduction)
- [Replace Consecutive Terms by One Limit](#replace-consecutive-terms-by-one-limit)
- [Solve the Fixed-Point Equation](#solve-the-fixed-point-equation)
- [Choose the Compatible Fixed Point](#choose-the-compatible-fixed-point)
- [Apply the Method to the Homework Recurrence](#apply-the-method-to-the-homework-recurrence)
- [Summary](#summary)

## Prerequisites

- Compute terms from a recursive formula.
- Interpret $\lim_{n\to\infty}a_n=L$.
- Solve a quadratic equation by factoring or the quadratic formula.
- Compare exact radical expressions with simple bounds.

---

<a id="introduction"></a>
## Introduction

When a recurrence has the form

$$
a_{n+1}=f(a_n),
$$

and its terms appear to settle toward one number, the reusable move is to **replace both $a_n$ and $a_{n+1}$ by the same proposed limit $L$**. This gives the fixed-point equation

$$
L=f(L).
$$

The recognition cue is a recursive sequence together with a request for its end behavior. The equation may produce more than one candidate, so solving it is not the last step: the candidate must also agree with the values and bounds of the actual sequence.

This method identifies the limit only after convergence is known or justified. In the homework example, we will also verify that the sequence is increasing and bounded above.

---

<a id="replace-consecutive-terms-by-one-limit"></a>
## Replace Consecutive Terms by One Limit

**Example:** Suppose $b_{n+1}=3+\dfrac{4}{b_n}$ and the sequence converges to $L$. Write the equation that $L$ must satisfy.

**Explanation**

Moving the index from $n$ to $n+1$ does not change the limit of a convergent sequence. Therefore,

$$
\lim_{n\to\infty}b_n=L
\qquad\text{and}\qquad
\lim_{n\to\infty}b_{n+1}=L.
$$

Replace both consecutive terms by $L$ while preserving the recurrence:

$$
L=3+\frac{4}{L}.
$$

The common trap is to replace only $b_{n+1}$ by $L$ and leave $b_n$ in the equation. At the limit, both terms approach the same number.

```quiz
type: radio
id: whw2-p2-fixed-equation
content: |-
  Suppose $c_{n+1}=5-\dfrac{6}{c_n}$ and $c_n$ converges to $L$. Which fixed-point equation must $L$ satisfy?
options:
- id: a
  content: |-
    $L=5-\dfrac{6}{L}$
  correct: true
- id: b
  content: |-
    $L=5-\dfrac{6}{n}$
- id: c
  content: |-
    $L+1=5-\dfrac{6}{L}$
- id: d
  content: |-
    $L=5-6L$
- id: e
  content: |-
    $L=\dfrac{5-6}{L}$
```

---

<a id="solve-the-fixed-point-equation"></a>
## Solve the Fixed-Point Equation

**Example:** Find the possible limits satisfying

$$
L=3+\frac{4}{L}.
$$

**Explanation**

First note that $L\ne0$, because the reciprocal $4/L$ must be defined. Multiply by $L$ and put the resulting quadratic into standard form:

$$
\begin{aligned}
L&=3+\frac{4}{L},\\
L^2&=3L+4,\\
L^2-3L-4&=0,\\
(L-4)(L+1)&=0.
\end{aligned}
$$

Thus the fixed-point candidates are

$$
L=4 \qquad\text{or}\qquad L=-1.
$$

These are candidates, not automatically two possible answers for a particular starting value.

```quiz
type: radio
id: whw2-p2-solve-fixed-equation
content: |-
  What are the fixed-point candidates for $c_{n+1}=5-\dfrac{6}{c_n}$?
options:
- id: a
  content: |-
    $L=2$ and $L=3$
  correct: true
- id: b
  content: |-
    $L=-2$ and $L=-3$
- id: c
  content: |-
    $L=1$ and $L=6$
- id: d
  content: |-
    $L=5$ only
- id: e
  content: |-
    $L=\dfrac{5\pm\sqrt{31}}{2}$
```

---

<a id="choose-the-compatible-fixed-point"></a>
## Choose the Compatible Fixed Point

**Example:** Let $d_1=1$ and

$$
d_{n+1}=3-\frac{1}{d_n}.
$$

If this sequence converges, which fixed point is compatible with its terms?

**Explanation**

The fixed-point equation gives

$$
\begin{aligned}
L&=3-\frac{1}{L},\\
L^2-3L+1&=0,\\
L&=\frac{3\pm\sqrt5}{2}.
\end{aligned}
$$

Now use a range that the recurrence preserves. Since $d_1=1$ and, whenever $d_n\ge1$,

$$
d_{n+1}=3-\frac1{d_n}\ge2,
$$

every term is at least $1$. But

$$
\frac{3-\sqrt5}{2}<1,
$$

so the smaller fixed point is incompatible with the sequence. The compatible candidate is

$$
L=\frac{3+\sqrt5}{2}.
$$

Do not select a root merely because it has a plus sign. Select it because the behavior of the actual sequence rules out the other candidate.

```quiz
type: radio
id: whw2-p2-select-root
content: |-
  A convergent recursive sequence has fixed-point candidates $1$ and $4$. It is known that every term after the first lies in the interval $(3,4)$. Which conclusion is justified?
options:
- id: a
  content: |-
    Its limit is $4$ because $1$ is outside the preserved range.
  correct: true
- id: b
  content: |-
    Its limit is $1$ because $1$ is the smaller root.
- id: c
  content: |-
    Its limit is $3$ because $3$ is an endpoint of the interval.
- id: d
  content: |-
    Its limit is $5$ because $1+4=5$.
- id: e
  content: |-
    Both $1$ and $4$ are limits of the same sequence.
```

---

<a id="apply-the-method-to-the-homework-recurrence"></a>
## Apply the Method to the Homework Recurrence

**Example:** Let

$$
a_1=1,
\qquad
a_{n+1}=4-\frac1{a_n}.
$$

List the first five terms and determine the end behavior.

**Explanation**

Apply the recurrence one term at a time:

$$
\begin{aligned}
a_1&=1,\\
a_2&=4-\frac11=3,\\
a_3&=4-\frac13=\frac{11}{3},\\
a_4&=4-\frac{1}{11/3}=4-\frac3{11}=\frac{41}{11},\\
a_5&=4-\frac{1}{41/11}=4-\frac{11}{41}=\frac{153}{41}.
\end{aligned}
$$

If the sequence converges to $L$, then

$$
\begin{aligned}
L&=4-\frac1L,\\
L^2-4L+1&=0,\\
L&=\frac{4\pm\sqrt{16-4}}{2}
=2\pm\sqrt3.
\end{aligned}
$$

Let

$$
\alpha=2-\sqrt3,
\qquad
\beta=2+\sqrt3.
$$

The starting value satisfies $\alpha<a_1<\beta$. If $\alpha<a_n<\beta$, compare the next term with each fixed point directly:

$$
\begin{aligned}
a_{n+1}-\alpha
&=f(a_n)-f(\alpha)
=\frac{a_n-\alpha}{\alpha a_n}>0,\\
\beta-a_{n+1}
&=f(\beta)-f(a_n)
=\frac{\beta-a_n}{\beta a_n}>0.
\end{aligned}
$$

Thus $\alpha<a_{n+1}<\beta$, so every term remains between the two fixed points. Within that interval,

$$
a_{n+1}-a_n
=4-\frac1{a_n}-a_n
=\frac{(\beta-a_n)(a_n-\alpha)}{a_n}>0.
$$

Thus $(a_n)$ is increasing and bounded above by $\beta$, so it converges. Its limit cannot be $\alpha$ because every term is at least $a_1=1>\alpha$. Therefore,

$$
\boxed{\lim_{n\to\infty}a_{n+1}=2+\sqrt3}.
$$

The index shift does not change the result: $a_n$ and $a_{n+1}$ have the same limit.

```quiz
type: radio
id: whw2-p2-full-process
content: |-
  Let $x_1=1$ and $x_{n+1}=3-\dfrac1{x_n}$. The sequence is increasing and bounded above. What is $\displaystyle\lim_{n\to\infty}x_n$?
options:
- id: a
  content: |-
    $\dfrac{3+\sqrt5}{2}$
  correct: true
- id: b
  content: |-
    $\dfrac{3-\sqrt5}{2}$
- id: c
  content: |-
    $3$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    The sequence diverges.
```

---

<a id="summary"></a>
## Summary

For a recurrence $a_{n+1}=f(a_n)$:

1. Compute the requested initial terms one at a time.
2. If convergence is known or justified, set both $a_n$ and $a_{n+1}$ equal to $L$.
3. Solve the fixed-point equation $L=f(L)$.
4. Treat every solution as a candidate.
5. Use signs, preserved bounds, monotonicity, or the observed term range to reject incompatible candidates.

The main trap is stopping after solving the fixed-point equation. A fixed point is only a possible limit; the sequence's actual behavior determines which candidate it can approach.
