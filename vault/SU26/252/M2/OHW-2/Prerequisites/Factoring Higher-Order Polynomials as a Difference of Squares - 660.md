# Factoring Higher-Order Polynomials as a Difference of Squares

<!--
lesson-id: 660
topic-code: MF2.2.2.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Factoring a Polynomial as a Difference of Squares](#factoring-a-polynomial-as-a-difference-of-squares)
- [Factoring a Polynomial With Leading Coefficients as a Difference of Squares](#factoring-a-polynomial-with-leading-coefficients-as-a-difference-of-squares)
- [Factoring a Polynomial With Multiple Variables as a Difference of Squares](#factoring-a-polynomial-with-multiple-variables-as-a-difference-of-squares)

## Prerequisites

- [Factoring Differences of Squares](<../../../../MA/Mathematical-Foundations/MF1/11. Polynomials/11.2. Factoring Polynomials/Lessons/11.2.5. Factoring Differences of Squares.md>)

---

<a id="introduction"></a>
## Introduction

We know how to factor a difference of squares, like $x^2-4$, but how do we factor an expression like $x^4-16$?

It turns out, we can use the exact same method!

First, let's rewrite the quartics as perfect squares:

$$
\begin{aligned}
x^{4} - 16 &= (x^{2})^{2} - (4)^{2}
\end{aligned}
$$

Now, our expression resembles a difference of squares, which can be factored as follows:

$$
a^2 - b^2 = (a+b)(a-b)
$$

Using $a=x^2$ and $b=4$ in the above formula, we can factor our expression as follows:

$$
x^4 - 16 = (x^2 + 4) (x^2 -4)
$$

We can check that it is correct by doing the multiplication:

$$
\begin{aligned}
(x^{2} + 4)(x^{2} - 4) &= x^{4} - 4x^{2} + 4x^{2} - 4^{2} \\
&= x^{4} - 4^{2} \\
&= x^{4} - 16✓
\end{aligned}
$$

Note that we can factor the expression further since it contains another difference of squares,

$$
x^2-4=(x)^2-(2)^2
$$

Factoring this difference of squares as well, we get the following final result:

$$
\begin{aligned}
x^{4} - 16 &= (x^{2} + 4)(x^{2} - 4) \\
&= (x^{2} + 4)(x + 2)(x - 2)
\end{aligned}
$$

---

<a id="factoring-a-polynomial-as-a-difference-of-squares"></a>
## Factoring a Polynomial as a Difference of Squares

**Example:** Factor the expression $y^4 - 81$.

**Explanation**

The difference of squares formula is given by

$$
a^2 - b^2 = (a+b)(a-b)
$$

Notice that our expression can be written as a difference of squares:

$$
y^4 - 81 = \left(y^2\right)^2 - 9^2
$$

Now, we factor our expression using the difference of squares formula:

$$
\left(y^2\right)^2 - 9^2 = (y^2 + 9)(y^2 - 9)
$$

Finally, we notice that the expression in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$
\begin{aligned}
(y^{2} + 9)(y^{2} - 9) &= (y^{2} + 9)(y^{2} - 3^{2}) \\
&= (y^{2} + 9)(y + 3)(y - 3)
\end{aligned}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Factor the expression $p^{4} - 1$.
options:
- id: a
  content: |-
    $(p^{2} + 1)(p + 1)(p - 1)$
  correct: true
- id: b
  content: |-
    $(p - 1)^{4}$
- id: c
  content: |-
    $(p + 1)^{4}$
- id: d
  content: |-
    $(p^{2} + 1)(p + 1)^{2}$
- id: e
  content: |-
    $(p^{2} + 1)(p - 1)^{2}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Factor the expression $16 - x^{4}$.
options:
- id: a
  content: |-
    $(2 + x)^{4}$
- id: b
  content: |-
    $(2 - x)^{4}$
- id: c
  content: |-
    $(4 + x^{2})(2 - x)^{2}$
- id: d
  content: |-
    $(4 + x^{2})(2 + x)(2 - x)$
  correct: true
- id: e
  content: |-
    $(2 + x^{2})(4 + x)(4 - x)$
```

---

<a id="factoring-a-polynomial-with-leading-coefficients-as-a-difference-of-squares"></a>
## Factoring a Polynomial With Leading Coefficients as a Difference of Squares

**Example:** Factor the expression $2m^4-32$.

**Explanation**

The difference of squares formula is given by

$$
a^2 - b^2 = (a+b)(a-b)
$$

Notice that all of the terms have a common factor of $2$. To simplify the computation, we can factor out the $2$, as follows:

$$
2m^4 - 32 = 2(m^4 - 16)
$$

The expression in parentheses can be written as a difference of squares:

$$
2(m^4 - 16) = 2\left(\left(m^2\right)^2 -4^2\right)
$$

Now, we factor our expression using the difference of squares formula:

$$
2\left(\left(m^2\right)^2 -4^2\right) = 2(m^2+4)(m^2-4)
$$

Finally, we notice that the expression $m^2-4$ in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$
\begin{aligned}
2(m^{2} + 4)(m^{2} - 4) &= 2(m^{2} + 4)(m^{2} - 2^{2}) \\
&= 2(m^{2} + 4)(m + 2)(m - 2)
\end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Factor the expression $81 - 16x^{4}$.
options:
- id: a
  content: |-
    $(9 + 4x^{2})(3 + 2x)(3 - 2x)$
  correct: true
- id: b
  content: |-
    $(3 - 2x)^{4}$
- id: c
  content: |-
    $(3 + 2x)^{4}$
- id: d
  content: |-
    $(9 + 4x^{2})(3 + 2x)^{2}$
- id: e
  content: |-
    $(9 + 4x^{2})(3 - 2x)^{2}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Factor the expression $81x^{4} - 1$.
options:
- id: a
  content: |-
    $(3x - 1)^{4}$
- id: b
  content: |-
    $(9x - 1)^{4}$
- id: c
  content: |-
    $(3x^{2} + 1)(9x + 1)(9x - 1)$
- id: d
  content: |-
    $(9x^{2} + 1)(3x + 1)(3x - 1)$
  correct: true
- id: e
  content: |-
    $(3x + 1)^{4}$
```

---

<a id="factoring-a-polynomial-with-multiple-variables-as-a-difference-of-squares"></a>
## Factoring a Polynomial With Multiple Variables as a Difference of Squares

**Example:** Factor the expression $16x^4 - y^4$.

**Explanation**

The difference of squares formula is given by

$$
a^2 - b^2 = (a+b)(a-b)
$$

Notice that our expression can be written as a difference of squares:

$$
16x^4 - y^4 = \left(4x^2\right)^2 -\left(y^2\right)^2
$$

Now, we factor our expression using the difference of squares formula:

$$
\left(4x^2\right)^2 - \left(y^2\right)^2 = (4x^2+y^2)(4x^2 - y^2)
$$

Finally, we notice that the expression $4x^2-y^2$ in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$
\begin{aligned}
(4x^{2} + y^{2})(4x^{2} - y^{2}) &= (4x^{2} + y^{2})((2x)^{2} - y^{2}) \\
&= (4x^{2} + y^{2})(2x + y)(2x - y)
\end{aligned}
$$

---

**Question 5**

```quiz
type: radio
id: q-5
content: |-
  Factor the expression $u^{4} - 625v^{4}$.
  
  *Hint: You may wish to make use of the fact that $625 = 25^{2}$.*
options:
- id: a
  content: |-
    $(u^{2} + 25v^{2})^{2}$
- id: b
  content: |-
    $(u + 5v)^{4}$
- id: c
  content: |-
    $(u^{2} + 25v^{2})(u + 5v)(u - 5v)$
  correct: true
- id: d
  content: |-
    $(u + 25v)(u + 5v)(u - 5v)$
- id: e
  content: |-
    $(u - 5v)^{4}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Factor the expression $p^{4} - (2q)^{4}$.
options:
- id: a
  content: |-
    $(p^{2} + 4q^{2})(p + 2q)(p - 2q)$
  correct: true
- id: b
  content: |-
    $(p^{2} + q^{2})(p + q)(p - q)$
- id: c
  content: |-
    $(p + 2q)^{4}$
- id: d
  content: |-
    $(p - 2q)^{4}$
- id: e
  content: |-
    $(p^{2} + q^{2})(p - q)^{2}$
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
