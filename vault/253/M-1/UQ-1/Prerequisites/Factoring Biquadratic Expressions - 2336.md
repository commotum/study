# Factoring Biquadratic Expressions

<!--
lesson-id: 2336
topic-code: MF2.2.2.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Factoring Biquadratic Expressions as Perfect Squares](#factoring-biquadratic-expressions-as-perfect-squares)
- [Factoring Biquadratic Expressions as Quadratic Trinomials](#factoring-biquadratic-expressions-as-quadratic-trinomials)
- [Factoring Biquadratic Expressions as Quadratic Trinomials With Leading Coefficients](#factoring-biquadratic-expressions-as-quadratic-trinomials-with-leading-coefficients)

## Prerequisites

- [Factoring Perfect Square Trinomials With Leading Coefficients](<../../../../MA/Mathematical-Foundations/MF1/11. Polynomials/11.2. Factoring Polynomials/Lessons/11.2.4. Factoring Perfect Square Trinomials With Leading Coefficients.md>)
- [Further Factoring Trinomials With Leading Coefficients](<../../../../MA/Mathematical-Foundations/MF1/11. Polynomials/11.2. Factoring Polynomials/Lessons/11.2.9. Further Factoring Trinomials With Leading Coefficients.md>)

---

<a id="introduction"></a>
## Introduction

Suppose that we want to factor the following trinomial:
$t^4+4t^2+3$.

This trinomial is a quartic, but it can also be viewed as a quadratic "in disguise." To see this, notice that if we introduce a new variable $z=t^2$, then we can rewrite the trinomial as a quadratic in terms of $z$:

$$
\begin{aligned}
t^{4} + 4t^{2} + 3 &=  \\
(t^{2})^{2} + 4(t^{2}) + 3 &=  \\
&= z^{2} + 4z + 3
\end{aligned}
$$

Now, we can factor the quadratic, and then rewrite the final expression in terms of $t$:

$$
\begin{aligned}
z^{2} + 4z + 3 &=  \\
(z + 1)(z + 3) &=  \\
&= (t^{2} + 1)(t^{2} + 3)
\end{aligned}
$$

Therefore, $t^4+4t^2+3$ factors into $(t^2+1)(t^2+3)$. We can double-check this result by multiplying it out:

$$
\begin{aligned}
(t^{2} + 1)(t^{2} + 3) &=  \\
t^{2}(t^{2} + 3) + 1(t^{2} + 3) &=  \\
t^{4} + 3t^{2} + t^{2} + 3 &=  \\
&= t^{4} + 4t^{2} + 3 \mid ✓
\end{aligned}
$$

---

<a id="factoring-biquadratic-expressions-as-perfect-squares"></a>
## Factoring Biquadratic Expressions as Perfect Squares

**Example:** Factor $x^4-4x^2+4$.

**Explanation**

We can introduce a new variable $z=x^2$ and then rewrite the trinomial as a quadratic in terms of $z$:

$$
\begin{aligned}
x^{4} - 4x^{2} + 4 &=  \\
(x^{2})^{2} - 4(x^{2}) + 4 &=  \\
&= z^{2} - 4z + 4
\end{aligned}
$$

Now, we can factor the quadratic as the square of a difference, and then rewrite the final expression in terms of $x$:

$$
\begin{aligned}
z^{2} - 4z + 4 &=  \\
(z - 2)^{2} &=  \\
&= (x^{2} - 2)^{2}
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Factor $4x^{4} + 4x^{2} + 1$.
options:
- id: a
  content: |-
    $(x^{2} + 2)^{2}$
- id: b
  content: |-
    $(x + 1)^{4}$
- id: c
  content: |-
    $(4x^{2} + 1)^{2}$
- id: d
  correct: true
  content: |-
    $(2x^{2} + 1)^{2}$
- id: e
  content: |-
    $(2x + 1)^{4}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Factor $y^{4} + 6y^{2} + 9$.
options:
- id: a
  content: |-
    $(y^{2} - 3)^{2}$
- id: b
  content: |-
    $(y - 3)^{2}$
- id: c
  content: |-
    $(y^{2} + 3y)^{2}$
- id: d
  content: |-
    $(y + 3)^{2}$
- id: e
  correct: true
  content: |-
    $(y^{2} + 3)^{2}$
```

---

<a id="factoring-biquadratic-expressions-as-quadratic-trinomials"></a>
## Factoring Biquadratic Expressions as Quadratic Trinomials

**Example:** Factor $t^4 - t^2 - 2$.

**Explanation**

We can introduce a new variable $z = t^2$ and then rewrite the trinomial as a quadratic in terms of $z$:

$$
\begin{aligned}
t^{4} - t^{2} - 2 &=  \\
(t^{2})^{2} - t^{2} - 2 &=  \\
&= z^{2} - z - 2
\end{aligned}
$$

Now, we can factor the quadratic, and then rewrite the final expression in terms of $t$:

$$
\begin{aligned}
z^{2} - z - 2 &=  \\
(z + 1)(z - 2) &=  \\
&= (t^{2} + 1)(t^{2} - 2)
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Factor $x^{4} - x^{2} - 6$.
options:
- id: a
  content: |-
    $(x^{2} - 2)(x^{2} - 3)$
- id: b
  content: |-
    $(x^{2} - 2)(x^{2} + 3)$
- id: c
  content: |-
    $(x + 2)(x - 3)$
- id: d
  content: |-
    $(x - 2)(x + 3)$
- id: e
  correct: true
  content: |-
    $(x^{2} + 2)(x^{2} - 3)$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Factor $q^{4} + 5q^{2} + 6$.
options:
- id: a
  content: |-
    $(q^{2} + 2)(q^{2} - 3)$
- id: b
  content: |-
    $(q^{2} - 2)^{2}$
- id: c
  correct: true
  content: |-
    $(q^{2} + 2)(q^{2} + 3)$
- id: d
  content: |-
    $(q^{2} + 3)^{2}$
- id: e
  content: |-
    $(q^{2} - 2)(q^{2} - 3)$
```

---

<a id="factoring-biquadratic-expressions-as-quadratic-trinomials-with-leading-coefficients"></a>
## Factoring Biquadratic Expressions as Quadratic Trinomials With Leading Coefficients

**Example:** Factor $2p^4 + 5p^2 + 3$.

**Explanation**

We can introduce a new variable $t = p^2$ and then rewrite the trinomial as a quadratic in terms of $t$:

$$
\begin{aligned}
2p^{4} + 5p^{2} + 3 &=  \\
2(p^{2})^{2} + 5p^{2} + 3 &=  \\
&= 2t^{2} + 5t + 3
\end{aligned}
$$

Now, we can factor the quadratic, and then rewrite the final expression in terms of $p$:

$$
\begin{aligned}
2t^{2} + 5t + 3 &=  \\
(t + 1)(2t + 3) &=  \\
&= (p^{2} + 1)(2p^{2} + 3)
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Factor $2w^{4} + 9w^{2} - 5$.
options:
- id: a
  content: |-
    $(2w - 1)(w + 5)$
- id: b
  content: |-
    $(2w^{2} + 1)(w^{2} - 5)$
- id: c
  content: |-
    $(2w - 1)(w^{2} + 5)$
- id: d
  correct: true
  content: |-
    $(2w^{2} - 1)(w^{2} + 5)$
- id: e
  content: |-
    $2(w^{2} - 1)(w^{2} + 5)$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Factor $3y^{4} + 10y^{2} + 3$.
options:
- id: a
  content: |-
    $(y^{2} + 1)(3y^{2} + 2)$
- id: b
  content: |-
    $(3y + 1)^{4}$
- id: c
  content: |-
    $(2y + 3)^{4}$
- id: d
  content: |-
    $(y^{2} + 2)(3y^{2} + 1)$
- id: e
  correct: true
  content: |-
    $(y^{2} + 3)(3y^{2} + 1)$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
