# Limits of Power Functions, and the Constant Rule for Limits

<!--
lesson-id: 1716
topic-code: MF2.11.2.1
-->

## Table of Contents

- [Introduction](#introduction)
- [Computing a Limit Using Direct Substitution](#computing-a-limit-using-direct-substitution)
- [The Limit of a Constant Function](#the-limit-of-a-constant-function)
- [Computing the Limit of a Constant Function](#computing-the-limit-of-a-constant-function)
- [The Constant Rule for Limits](#the-constant-rule-for-limits)
- [Using the Constant Rule to Compute a Limit Algebraically](#using-the-constant-rule-to-compute-a-limit-algebraically)
- [Using the Constant Rule to Compute the Limit of a Function Given a Graph](#using-the-constant-rule-to-compute-the-limit-of-a-function-given-a-graph)

## Prerequisites

- [Finding the Existence of a Limit Using One-Sided Limits](<../../../../MA/Mathematical-Foundations/MF2/11. Limits & Continuity/11.1. Estimating Limits from Graphs/Lessons/11.1.3. Finding the Existence of a Limit Using One-Sided Limits.md>)

---

<a id="introduction"></a>
## Introduction

For any power function

$$
f(x) = x^n
$$

we can compute the limit $\lim\limits_{x \to a} x^n$ by substituting $x=a$ directly into the limit:

$$
\lim\limits_{x \to a} x^n = a^n \,
$$

For example, to compute $\lim\limits_{x \to 3} x^2$, we can substitute $x=3$ directly into the limit:

$$
\lim\limits_{x \to 3} x^2 = 3^2 = 9 \,
$$

We can verify this result by graphing the function

$$
f(x)=x^2
$$

and checking the left and right-sided limits.

![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/80774891e577dc84f744644b3b3a434a.png>)

Looking at the graph, we compute the left and right-sided limits:

- Left-sided limit: $\hspace{.25cm} \lim\limits_{x \to 3^-} x^2 = 9$
- Right-sided limit: $\hspace{.25cm} \lim\limits_{x \to 3^+} x^2 = 9$

Since the left and right-sided limits both evaluate to $9$, we conclude that

$$
\lim\limits_{x \to 3} x^2 = 9 \,
$$

---

<a id="computing-a-limit-using-direct-substitution"></a>
## Computing a Limit Using Direct Substitution

**Example:** Find $\lim_\limits{x\rightarrow (-1/2)} x^3$.

**Explanation**

Substituting

$$
x=-\dfrac{1}{2}
$$

directly into the limit, we find

$$
\begin{aligned}
lim_(x → (-1/2))x^{3} &= (-\frac{1}{2})^{3} \\
&=-\frac{1}{2^{3}} \\
&=-\frac{1}{8}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Find $lim_(x → - 2)x^{5}$.
options:
- id: a
  content: |-
    $-96$
- id: b
  content: |-
    $96$
- id: c
  content: |-
    $-24$
- id: d
  content: |-
    $12$
- id: e
  content: |-
    $-32$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Find $lim_(x → 3)x^{4}$.
options:
- id: a
  content: |-
    $64$
- id: b
  content: |-
    $27$
- id: c
  content: |-
    $9$
- id: d
  content: |-
    $81$
  correct: true
- id: e
  content: |-
    $12$
```

---

<a id="the-limit-of-a-constant-function"></a>
## The Limit of a Constant Function

For any constant function

$$
f(x)=c
$$

the limit $\lim_\limits{x\rightarrow a} c$ will match the value of the constant:

$$
\lim_\limits{x\rightarrow a} c=c \,
$$

For example, the limit $\lim_\limits{x\rightarrow 2} 1$ is just the value of the constant, $1$:

$$
\lim_\limits{x\rightarrow 2} 1 = 1
$$

We can verify this result by graphing the function

$$
f(x) = 1
$$

![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/99a2e48f6b089ca604ad9784978ca02f.png>)

Looking at the graph, we compute the left and right-sided limits:

- Left-sided limit: $\hspace{.25cm} \lim\limits_{x \to 2^-} 1 = 1$
- Right-sided limit: $\hspace{.25cm} \lim\limits_{x \to 2^+} 1 = 1$

Since the left and right-sided limits both evaluate to $1$, we conclude that

$$
\lim\limits_{x \to 2} 1 = 1 \,
$$

---

<a id="computing-the-limit-of-a-constant-function"></a>
## Computing the Limit of a Constant Function

**Example:** Evaluate $\lim_\limits{x\,\rightarrow \,-4} \sqrt{7}$.

**Explanation**

As $x$ approaches $-4$, the function

$$
f(x)=\sqrt 7
$$

remains equal to $\sqrt{7}$. Therefore, we have

$$
\lim_\limits{x\,\rightarrow\, -4} \sqrt{7}=\sqrt{7}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Evaluate $lim_(x → - \sqrt{2})π$.
options:
- id: a
  content: |-
    $π$
  correct: true
- id: b
  content: |-
    $-\sqrt{2}$
- id: c
  content: |-
    $- π$
- id: d
  content: |-
    $-\sqrt{2}π$
- id: e
  content: |-
    $\sqrt{2}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Evaluate $lim_(y → π/3)3$.
options:
- id: a
  content: |-
    $π$
- id: b
  content: |-
    $\frac{π}{3}$
- id: c
  content: |-
    $\frac{π}{9}$
- id: d
  content: |-
    $3$
  correct: true
- id: e
  content: |-
    $3π$
```

---

<a id="the-constant-rule-for-limits"></a>
## The Constant Rule for Limits

The **constant rule for limits** states that if $c$ is a constant, and

$$
\lim_\limits{x\rightarrow a}f(x)=L
$$

then

$$
\lim_\limits{x\rightarrow a}c\cdot f(x) = c\cdot \lim_\limits{x\rightarrow a}f(x)=c\cdot L
$$

For example, to compute $\lim_\limits{x\rightarrow 2}5x^3$, we just factor the constant $5$ out of the limit and then substitute:

$$
\begin{aligned} \lim_\limits{x\rightarrow 2}{\color{blue}5}x^3 &= {\color{blue}5} \lim_\limits{x\rightarrow 2}x^3 \\[5pt] &= {\color{blue}5}\cdot 2^3 \\[5pt] &= 40 \end{aligned}
$$

Similarly, consider the graph of the function $y=f(x)$ below. Suppose we know that

$$
\displaystyle{\lim_{x \rightarrow \,1} cf(x) = 10}
$$

where $c$ is a real constant. Let's find the value of $c$.

![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/c4bbbe0545c8db61cc85595057b4fb03.png>)

From the figure above, we get that

$$
\displaystyle{\lim_{x \rightarrow \, 1} f(x)} = 5
$$

Therefore,

$$
\begin{aligned}
lim_(x → 1)cf(x) &= 10 \\
c \cdot lim_(x → 1)f(x) &= 10 \\
c \cdot 5 &= 10 \\
c &= 2
\end{aligned}
$$

---

<a id="using-the-constant-rule-to-compute-a-limit-algebraically"></a>
## Using the Constant Rule to Compute a Limit Algebraically

**Example:** Given that $\displaystyle \lim_{y\rightarrow \sqrt{7}/2} Cy^2=14$, where $C$ is a real constant, what is the value of $C$?

**Explanation**

We factor the constant out of the limit and evaluate the remaining limit, as follows:

$$
\begin{aligned} \displaystyle \lim_{y\rightarrow \sqrt{7}/2} Cy^2&=14 \\ C\cdot\displaystyle \lim_{y\rightarrow \sqrt{7}/2} y^2&=14 \\ C\left(\dfrac{\sqrt{7}}{2}\right)^2&=14\ \dfrac{7C}{4}&=14 \\ C&=8 \end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Given that $lim_(x → \sqrt{2})Cx^{6} = 8$, where $C$ is a real constant, what is the value of $C$?
options:
- id: a
  content: |-
    $1$
  correct: true
- id: b
  content: |-
    $2$
- id: c
  content: |-
    $\frac{1}{4}$
- id: d
  content: |-
    $\frac{1}{8}$
- id: e
  content: |-
    $\frac{1}{2}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Find $lim_(y → 3)\frac{5y^{2}}{3}$.
options:
- id: a
  content: |-
    $15$
  correct: true
- id: b
  content: |-
    $\frac{5}{3}$
- id: c
  content: |-
    $9$
- id: d
  content: |-
    $45$
- id: e
  content: |-
    $10$
```

---

<a id="using-the-constant-rule-to-compute-the-limit-of-a-function-given-a-graph"></a>
## Using the Constant Rule to Compute the Limit of a Function Given a Graph

**Example:** The figure below shows the graph of $y=f(x)$. Evaluate $\lim_\limits{x \rightarrow \,0} \Bigl(-2.5f(x)\Bigr)$.

![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/a7f8750a28cdc0a0af8a34991e6a0836.png>)

**Explanation**

From the graph we get that

$$
\lim_\limits{x\to 0}f(x)=2
$$

Therefore,

$$
\begin{aligned}
lim_(x → 0)(-2.5f(x)) &= (-2.5) \cdot lim_(x → 0)f(x) \\
&= (-2.5) \cdot 2 \\
&=-5
\end{aligned}
$$

---

**Question 7**

```quiz
type: radio
id: ma-35398
content: |-
  ![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/q-35398.png>)
  
  The figure above shows the graph of $y = f(x)$. Evaluate $lim_(x → 0)\sqrt{7}f(x)$.
options:
- id: a
  content: |-
    $0$
- id: b
  content: |-
    $-\sqrt{7}$
- id: c
  content: |-
    $2\sqrt{7}$
  correct: true
- id: d
  content: |-
    $\sqrt{7}$
- id: e
  content: |-
    $-2\sqrt{7}$
```

---

**Question 8**

```quiz
type: radio
id: ma-35397
content: |-
  ![](<../Source/Limits of Power Functions, and the Constant Rule for Limits - 1716/Images/q-35397.png>)
  
  The figure above shows the graph of $y = f(x)$. Evaluate $lim_(x → 1)(-6f(x))$.
options:
- id: a
  content: |-
    $-6$
- id: b
  content: |-
    $-30$
  correct: true
- id: c
  content: |-
    $-1$
- id: d
  content: |-
    $-3$
- id: e
  content: |-
    $-18$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
