# Solving Logarithmic Equations by Combining the Laws of Logarithms

<!--
lesson-id: 3832
topic-code: MF2.5.4.4
-->

## Table of Contents

- [Introduction](#introduction)
- [Solving Equations Using the Power and Product Rules](#solving-equations-using-the-power-and-product-rules)
- [Solving Equations Using the Power and Quotient Rules](#solving-equations-using-the-power-and-quotient-rules)
- [Solving Equations Resulting in Rational Equations Using the Quotient Rule](#solving-equations-resulting-in-rational-equations-using-the-quotient-rule)

## Prerequisites

- [Combining the Laws of Logarithms](<../../5.2. The Laws of Logarithms/Lessons/5.2.4. Combining the Laws of Logarithms.md>)
- [Solving Equations With Even Exponents Using the Nth Root Method](<../../../../AG1/1. Equations & Inequalities/1.4. Nonlinear Equations/Lessons/1.4.3. Solving Equations With Even Exponents Using the Nth Root Method.md>)
- [Solving Logarithmic Equations Using the Laws of Logarithms](<5.4.3. Solving Logarithmic Equations Using the Laws of Logarithms.md>)
- [Solving Equations With Odd Exponents Using the Nth Root Method](<../../../../AG1/1. Equations & Inequalities/1.4. Nonlinear Equations/Lessons/1.4.2. Solving Equations With Odd Exponents Using the Nth Root Method.md>)

---

<a id="introduction"></a>
## Introduction

Let's remind ourselves of the laws of logarithms:

> **Product Rule**:
> $\qquad$ $\log_b(xy) = \log_b(x) + \log_b(y)$
> **Quotient Rule:**
> $\qquad$ $\log_b\left(\dfrac x y\right) = \log_b(x) - \log_b(y)$
> **Power Rule**:
> $\qquad$ $\log_b\left(x^n\right) = n\log_b(x)$

Sometimes, we need to combine two or more of these laws to solve a logarithmic equation. Let's see an example.

---

<a id="solving-equations-using-the-power-and-product-rules"></a>
## Solving Equations Using the Power and Product Rules

**Example:** Solve the equation $\dfrac{1}{2}\log_2 \left(4x^4\right) + \log_2 x= 1$.

**Explanation**

Notice that the logarithms share the same base.

First, we apply the power rule to the *first* term to make the coefficient in front of each logarithm the same:

$$
\begin{aligned}
\frac{1}{2}\log_{2} (4x^{4}) + \log_{2} x &= 1 \\
\log_{2} ((4x^{4})^{1/2}) + \log_{2} x &= 1 \\
\log_{2} (2x^{2}) + \log_{2} x &= 1
\end{aligned}
$$

Next, we combine the logarithms using the product rule. This gives

$$
\begin{aligned}
\log_{2} (2x^{2} \cdot x) &= 1 \\
\log_{2} (2x^{3}) &= 1
\end{aligned}
$$

Writing this equation in its equivalent exponential form, we get

$$
\begin{aligned}
2^{\log_{2} (2x^{3})} &= 2^{1} \\
2x^{3} &= 2
\end{aligned}
$$

Now, we solve this equation for $x$ using the usual methods.

$$
\begin{aligned}
x^{3} &= 1 \\
\sqrt[3]{x^{3}} &= \sqrt[3]{1} \\
x &= 1
\end{aligned}
$$

Let's now check for an extraneous solution by substituting back into the original equation:

Substituting $x=1$ back into the original equation, we get

$$
\begin{aligned}
\frac{1}{2}\log_{2} (4 \cdot 1^{4}) + \log_{2} 1 &= ^(?)1 \\
\frac{1}{2}\log_{2} 4 + \log_{2} 1 &= ^(?)1 \\
\frac{1}{2}\log_{2} 4 + 0 &= ^(?)1 \\
\log_{2} (4^{1/2}) &= ^(?)1 \\
\log_{2} (2) &= ^(?)1 \\
1 &= 1.✓
\end{aligned}
$$

Therefore, $x=1$ is a valid solution.

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Solve the equation $\log_{8} 2 + 2\log_{8} (2x) = 1$.
options:
- id: a
  content: |-
    $x = ± 2$
- id: b
  content: |-
    $x = 0$ only
- id: c
  correct: true
  content: |-
    $x = 1$ only
- id: d
  content: |-
    $x = ± 1$
- id: e
  content: |-
    No solutions
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Solve the equation $\log_{3} (72x) + 2\log_{3} x = 2$.
options:
- id: a
  content: |-
    $x = ± \frac{1}{2}$
- id: b
  content: |-
    No solutions
- id: c
  content: |-
    $x = ± 1$
- id: d
  correct: true
  content: |-
    $x = \frac{1}{2}$ only
- id: e
  content: |-
    $x = 1$
```

---

<a id="solving-equations-using-the-power-and-quotient-rules"></a>
## Solving Equations Using the Power and Quotient Rules

**Example:** Solve the equation $\log_2 (4x) - 2\log_2\left(x^2\right) = 1$.

**Explanation**

Notice that the logarithms share the same base.

First, we apply the power rule to the first term to make the coefficient in front of each logarithm the same:

$$
\begin{aligned}
\log_{2} (4x) - 2\log_{2} (x^{2}) = 1 \\
&= \log_{2} (4x) - \log_{2} ((x^{2})^{2}) = 1 \\
\log_{2} (4x) - \log_{2} (x^{4}) &= 1
\end{aligned}
$$

Next, we combine the logarithms using the quotient rule. This gives

$$
\begin{aligned}
\log_{2} (\frac{4x}{x^{4}}) &= 1 \\
\log_{2} (\frac{4}{x^{3}}) &= 1
\end{aligned}
$$

Writing this equation in its equivalent exponential form, we get

$$
\begin{aligned}
\frac{4}{x^{3}} &= 2^{1} \\
\frac{4}{x^{3}} &= 2
\end{aligned}
$$

Now, we solve this rational equation for $x$ using the usual methods.

$$
\begin{aligned}
\frac{4}{x^{3}} &= 2 \\
x^{3} \cdot \frac{4}{x^{3}} &= x^{3} \cdot 2 \\
x^{3} \cdot \frac{4}{x^{3}} &= 2x^{3} \\
2x^{3} &= 4 \\
x^{3} &= 2 \\
x &= \sqrt[3]{2}
\end{aligned}
$$

Let's now check for an extraneous solution by substituting back into the original equation:

Substituting

$$
x=\sqrt[3]{2}
$$

back into the original equation, we get

$$
\begin{aligned}
\log_{2} (4(\sqrt[3]{2})) - 2\log_{2} ((\sqrt[3]{2})^{2}) &= ^(?)1 \\
\log_{2} (4(\sqrt[3]{2})) - \log_{2} ((\sqrt[3]{2})^{2})^{2} &= ^(?)1 \\
\log_{2} (4(\sqrt[3]{2})) - \log_{2} ((\sqrt[3]{2})^{4}) &= ^(?)1 \\
\log_{2} (4(\sqrt[3]{2})) - \log_{2} (2(\sqrt[3]{2})) &= ^(?)1 \\
\log_{2} (\frac{4\sqrt[3]{2}}{2\sqrt[3]{2}}) &= ^(?)1 \\
\log_{2} (\frac{4\sqrt[3]{2}}{2\sqrt[3]{2}}) &= ^(?)1 \\
\log_{2} (\frac{4}{2}) &= ^(?)1 \\
\log_{2} (2) &= ^(?)1 \\
1 &= 1.✓
\end{aligned}
$$

Therefore,

$$
x=\sqrt[3]{2}
$$

is a valid solution.

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Solve the equation $2\log_{8} 4 - \log_{8} (x^{2}) = 1$.
options:
- id: a
  content: |-
    $x = \sqrt{2}$
- id: b
  correct: true
  content: |-
    $x = ± \sqrt{2}$
- id: c
  content: |-
    $x = ± 2$
- id: d
  content: |-
    $x =-\sqrt{2}$
- id: e
  content: |-
    $x = 2$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Solve the equation $2\log_{4} (4x^{2}) - \log_{4} (2x) = 3$.
options:
- id: a
  content: |-
    $x = 3$ only
- id: b
  content: |-
    $x = ± 2$
- id: c
  correct: true
  content: |-
    $x = 2$ only
- id: d
  content: |-
    $x = 3$ only
- id: e
  content: |-
    $x = ± \sqrt{2}$
```

---

<a id="solving-equations-resulting-in-rational-equations-using-the-quotient-rule"></a>
## Solving Equations Resulting in Rational Equations Using the Quotient Rule

**Example:** Solve the equation $2\log_3 (\sqrt 2x) - \log_3(x - 1) = \log_3 (3x)$.

**Explanation**

Notice that the logarithms share the same base.

First, we apply the power rule to the *first* term to make the coefficient in front of each logarithm the same:

$$
\begin{aligned}
2\log_{3} (\sqrt{2}x) - \log_{3} (x - 1) &= \log_{3} (3x) \\
\log_{3} (\sqrt{2}x)^{2} - \log_{3} (x - 1) &= \log_{3} (3x) \\
\log_{3} (2x^{2}) - \log_{3} (x - 1) &= \log_{3} (3x)
\end{aligned}
$$

Next, we combine the logarithms on the left-hand side using the quotient rule:

$$
\begin{aligned}
\log_{3} (\frac{2x^{2}}{x - 1}) &= \log_{3} (3x)
\end{aligned}
$$

Now, we solve the equation for $x$ using the usual methods.

$$
\begin{aligned}
\frac{2x^{2}}{x - 1} &= 3x \\
(x - 1) \cdot \frac{2x^{2}}{x - 1} &= (x - 1) \cdot (3x) \\
(x - 1) \cdot \frac{2x^{2}}{x - 1} &= (x - 1) \cdot (3x) \\
2x^{2} &= 3x^{2} - 3x \\
x^{2} - 3x &= 0 \\
x(x - 3) &= 0
\end{aligned}
$$

So, $x = 0$ and $x =3$.

Let's now check for extraneous solutions by substituting them back into the original equation:

- Substituting $x=0$ back into the original equation, we get
$2\log_{3} (\sqrt{2} \cdot 0) - \log_{3} (0 - 1)|=^(?)\log_{3} (3 \cdot 0); 2\log_{3} (0) - \log_{3} (-1)|=^(?)\log_{3} (0).\cdot$
This statement is false because $\log_3 (0)$ and $\log_3 (-1)$ are undefined. Therefore, $x=0$ is not a valid solution.

- Substituting $x=3$ back into the original equation, we get
$2\log_{3} (3\sqrt{2}) - \log_{3} (3 - 1)|=^(?)\log_{3} (3 \cdot 3); \log_{3} (3\sqrt{2})^{2} - \log_{3} (2)|=^(?)\log_{3} (9); \log_{3} (18) - \log_{3} (2)|=^(?)\log_{3} (9); \log_{3} (\frac{18}{2})|=^(?)\log_{3} (9); \log_{3} (9)|= \log_{3} (9).✓$
Therefore, $x=3$ is a valid solution.

Therefore, the correct answer is "$x=3$ only".

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Solve the equation $\log_{4} (x + 1) - \log_{4} (\frac{1}{3 - x}) = 1$.
options:
- id: a
  content: |-
    $x = ± 2$
- id: b
  content: |-
    $x = 2$ only
- id: c
  content: |-
    $x =-1$ and $x = 2$
- id: d
  content: |-
    $x = ± 1$
- id: e
  correct: true
  content: |-
    $x = 1$ only
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Solve the equation $2\log_{3} x - \log_{3} (4 - x) = \log_{3} 2$.
options:
- id: a
  content: |-
    $x = 2$ and $x = 4$
- id: b
  content: |-
    $x = 2$ and $x =-4$
- id: c
  correct: true
  content: |-
    $x = 2$ only
- id: d
  content: |-
    $x = 4$ only
- id: e
  content: |-
    $x =-2$ and $x = 4$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF2/Home|Home]]
[[MA/Mathematical-Foundations/MF2/0. Table of Contents/TOC|Table of Contents]]
