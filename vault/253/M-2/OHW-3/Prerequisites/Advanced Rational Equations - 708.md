# Advanced Rational Equations

<!--
lesson-id: 708
topic-code: MF2.6.2.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Solving Rational Equations Using the Lowest Common Denominator](#solving-rational-equations-using-the-lowest-common-denominator)
- [Solving Rational Equations by Factoring](#solving-rational-equations-by-factoring)
- [Solving Rational Equations by Factoring a Quadratic Trinomial](#solving-rational-equations-by-factoring-a-quadratic-trinomial)
- [Solving a Rational Equations by Factoring a Quadratic Denominator With No Constant Term](#solving-a-rational-equations-by-factoring-a-quadratic-denominator-with-no-constant-term)

## Prerequisites

- [Rational Equations With Three Terms](<6.2.1. Rational Equations With Three Terms.md>)
- [The Least Common Multiple of Two Polynomials](<../../../2. Polynomials/2.1. Polynomials/Lessons/2.1.3. The Least Common Multiple of Two Polynomials.md>)

---

<a id="introduction"></a>
## Introduction

Suppose we want to solve the following rational equation.

$$
\dfrac{1} {2(s+3)} =\dfrac{1}{s-1}-\dfrac{3} {(s+3)(s-1)}
$$

Notice that each of the denominators in our equation is either a binomial or product of binomials.

From here, we make the following observations:

- The least common denominator of our equation is given by
$\textrm{LCM}\big(2(s+3),\: s-1,\: (s+3)(s-1) \big) = 2(s+3)(s-1)$.
- The values $s=-3$ and $s=1$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$
\begin{aligned}
(1)/(2(s + 3)) &= \frac{1}{s - 1} - (3)/((s + 3)(s - 1)) \\
2(s + 3)(s - 1) \cdot (1)/(2(s + 3)) &= 2(s + 3)(s - 1) \cdot (\frac{1}{s - 1} - (3)/((s + 3)(s - 1))) \\
(2(s + 3)(s - 1))/(2(s + 3)) &= (2(s + 3)(s - 1))/(s - 1) - (6(s + 3)(s - 1))/((s + 3)(s - 1)) \\
(2(s + 3)(s - 1))/(2(s + 3)) &= (2(s + 3)(s - 1))/(s - 1) - (6(s + 3)(s - 1))/((s + 3)(s - 1))
\end{aligned}
$$

After canceling, we are left with the equation

$$
(s-1)= 2(s+3)-6
$$

Solving this equation for $s$, we get the following:

$$
\begin{aligned}
(s - 1) &= 2(s + 3) - 6 \\
s - 1 &= 2s + 6 - 6 \\
s - 1 &= 2s \\
s - 2s &= 1 \\
- s &= 1 \\
s &= -1
\end{aligned}
$$

So, $s=-1$ is a *potential* solution.

We now need to check this value against the prohibited solutions $s=-3$ and $s=1$ mentioned earlier. Now, since

$$
-1\neq -3
$$

and

$$
-1\neq 1
$$

we have that $s=-1$ is indeed a valid solution.

Therefore, we conclude that the solution to our original equation is $s=-1$.

---

<a id="solving-rational-equations-using-the-lowest-common-denominator"></a>
## Solving Rational Equations Using the Lowest Common Denominator

**Example:** Solve the equation $\dfrac{4} {x - 2} - \dfrac{8} {x(x - 2)} = \dfrac {3} {x}$.

**Explanation**

We make the following observations:

- The least common denominator of our equation is given by
$\textrm{LCM}\big(x-2,\: x(x-2),\: x \big) = x(x-2)$.
- The values $x = 0$ and $x=2$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$
\begin{aligned}
\frac{4}{x - 2} - (8)/(x(x - 2)) &= \frac{3}{x} \\
x(x - 2) \cdot (\frac{4}{x - 2} - (8)/(x(x - 2))) &= x(x - 2) \cdot \frac{3}{x} \\
(4x(x - 2))/(x - 2) - (8x(x - 2))/(x(x - 2)) &= (3x(x - 2))/(x) \\
(4x(x - 2))/(x - 2) - (8x(x - 2))/(x(x - 2)) &= (3x(x - 2))/(x) \\
4x - 8 &= 3(x - 2)
\end{aligned}
$$

Solving this equation for $x$, we get the following:

$$
\begin{aligned}
4x - 8 &= 3(x - 2) \\
4x - 8 &= 3x - 6 \\
4x - 3x &= -6 + 8 \\
x &= 2
\end{aligned}
$$

However, since $x=2$ is not a valid solution, we conclude that our equation has no solutions.

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Solve the equation $\frac{1}{4x} + (1)/(2x(3x + 1)) = \frac{1}{3x + 1}$.
options:
- id: a
  content: |-
    $x =-3$
- id: b
  content: |-
    No solutions
- id: c
  content: |-
    $x = 2$
- id: d
  content: |-
    $x = 1$
- id: e
  content: |-
    $x = 3$
  correct: true
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Solve the equation $\frac{3}{z - 1} - (3)/(z(z - 1)) = \frac{2}{z}$.
options:
- id: a
  content: |-
    $z =-2$
- id: b
  content: |-
    $z = 1$
- id: c
  content: |-
    No solutions
  correct: true
- id: d
  content: |-
    $z =-1$
- id: e
  content: |-
    $z = 3$
```

---

<a id="solving-rational-equations-by-factoring"></a>
## Solving Rational Equations by Factoring

When a rational equation contains a quadratic denominator, it's often helpful to factor this denominator first. By doing so, we may spot the least common denominator of the equation, leading to a more straightforward solution.

For example, consider the following equation:

$$
\dfrac{1}{x-1}+\dfrac{2}{x-2}=\dfrac{5}{x^2-3x+2}
$$

Notice that the right-hand side of our equation contains a term with a quadratic denominator. This denominator can be factored, giving us the equation

$$
\dfrac{1}{x-1}+\dfrac{2}{x-2}=\dfrac{5}{(x-1)(x-2)}\,
$$

We now make the following observations:

- The least common denominator is given by
$LCM(x - 1, x - 2, (x - 1)(x - 2)) = (x - 1)(x - 2)$.
- The values $x=1$ and $x=2$ *cannot* be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify the equation as follows:

$$
\begin{aligned}
(x - 1)(x - 2) \cdot (\frac{1}{x - 1} + \frac{2}{x - 2}) &= (x - 1)(x - 2) \cdot ((5)/((x - 1)(x - 2))) \\
((x - 1)(x - 2))/(x - 1) + (2(x - 1)(x - 2))/(x - 2) &= (5(x - 1)(x - 2))/((x - 1)(x - 2)) \\
((x - 1) \cdot (x - 2))/(x - 1) + (2(x - 1) \cdot (x - 2))/(x - 2) &= (5(x - 1)(x - 2))/((x - 1)(x - 2)) \\
(x - 2) + 2(x - 1) &= 5
\end{aligned}
$$

Solving this equation for $x$, we get the following:

$$
\begin{aligned}
(x - 2) + 2(x - 1) &= 5 \\
x - 2 + 2x - 2 &= 5 \\
3x - 4 &= 5 \\
3x &= 9 \\
x &= 3
\end{aligned}
$$

Since

$$
3\neq 1
$$

and

$$
3\neq 2
$$

we conclude that $x=3$ is a valid solution.

Therefore, the solution to our original equation is $x=3$.

---

<a id="solving-rational-equations-by-factoring-a-quadratic-trinomial"></a>
## Solving Rational Equations by Factoring a Quadratic Trinomial

**Example:** Solve the equation $\dfrac{3}{k-3} -\dfrac {2}{k-2} = \dfrac{2}{k^2-5k+6}$.

**Explanation**

First, we factor the quadratic denominator, giving us the equation

$$
\dfrac{3}{k-3} -\dfrac {2}{k-2} = \dfrac{2}{(k-2)(k-3)}
$$

We now make the following observations:

- The least common denominator of our equation is given by
$\textrm{LCM}\big(k-2, k-3, (k-2)(k-3) \big) = (k-2)(k-3)$.
- The values $k=2$ and $k=3$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal to zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$
\begin{aligned}
\frac{3}{k - 3} - \frac{2}{k - 2} &= (2)/((k - 2)(k - 3)) \\
(k - 2)(k - 3) \cdot (\frac{3}{k - 3} - \frac{2}{k - 2}) &= (k - 2)(k - 3) \cdot (2)/((k - 2)(k - 3)) \\
(3(k - 2)(k - 3))/(k - 3) - (2(k - 2)(k - 3))/(k - 2) &= (2(k - 2)(k - 3))/((k - 2)(k - 3)) \\
(3(k - 2) \cdot (k - 3))/(k - 3) - (2 \cdot (k - 2) \cdot (k - 3))/(k - 2) &= (2 \cdot (k - 2)(k - 3))/((k - 2)(k - 3)) \\
3(k - 2) - 2(k - 3) &= 2
\end{aligned}
$$

Solving this equation for $k$, we get the following:

$$
\begin{aligned}
3(k - 2) - 2(k - 3) &= 2 \\
3k - 6 - 2k + 6 &= 2 \\
k &= 2
\end{aligned}
$$

However, since $k=2$ is not a valid solution, our equation has no solutions.

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Solve the equation $\frac{1}{S + 1} + \frac{2}{S - 1} = \frac{1}{S^{2} - 1}$.
options:
- id: a
  content: |-
    $S = 3$
- id: b
  content: |-
    $S =-2$
- id: c
  content: |-
    No solutions
- id: d
  content: |-
    $S =-4$
- id: e
  content: |-
    $S = 0$
  correct: true
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Solve the equation $\frac{5}{y + 9} = \frac{7}{y - 4} - \frac{65}{y^{2} + 5y - 36}$.
options:
- id: a
  content: |-
    $y = \frac{3}{2}$
- id: b
  content: |-
    $y = 9$
- id: c
  content: |-
    $y = 23$
- id: d
  content: |-
    No solutions
  correct: true
- id: e
  content: |-
    $y = 2$
```

---

<a id="solving-a-rational-equations-by-factoring-a-quadratic-denominator-with-no-constant-term"></a>
## Solving a Rational Equations by Factoring a Quadratic Denominator With No Constant Term

**Example:** Solve the equation $\dfrac{3}{u+1} - \dfrac{1}{3u} =\dfrac{5}{u^2 +u}$.

**Explanation**

First, we factor the quadratic denominator, giving us the equation

$$
\dfrac{3}{u+1} - \dfrac{1}{3u} =\dfrac{5}{u(u+1)}
$$

We now make the following observations:

- The least common denominator of our equation is given by
$\textrm{LCM}\big(3u, \:u+1, \: u(u+1) \big) = 3u(u+1)$.
- The values $u=-1$ and $u=0$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$
\begin{aligned}
\frac{3}{u + 1} - \frac{1}{3u} &= (5)/(u(u + 1)) \\
3u(u + 1) \cdot (\frac{3}{u + 1} - \frac{1}{3u}) &= 3u(u + 1) \cdot (5)/(u(u + 1)) \\
(9u(u + 1))/(u + 1) - (3u(u + 1))/(3u) &= (15u(u + 1))/(u(u + 1)) \\
(9u \cdot (u + 1))/(u + 1) - (3u \cdot (u + 1))/(3u) &= (15 \cdot u(u + 1))/(u(u + 1)) \\
9u - (u + 1) &= 15
\end{aligned}
$$

Solving this equation for $u$, we get the following:

$$
\begin{aligned}
9u - (u + 1) &= 15 \\
9u - u - 1 &= 15 \\
8u &= 16 \\
u &= 2
\end{aligned}
$$

Since

$$
2\neq -1
$$

and

$$
2\neq 0
$$

we conclude that $u=2$ is a valid solution.

Therefore, the solution to our original equation is $u=2$.

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  Solve the equation $\frac{11}{T} - \frac{4}{2T - 1} = \frac{1}{2T^{2} - T}$.
options:
- id: a
  content: |-
    $T = 2$
- id: b
  content: |-
    $T = \frac{2}{3}$
  correct: true
- id: c
  content: |-
    No solutions
- id: d
  content: |-
    $T = 1$
- id: e
  content: |-
    $T = \frac{1}{2}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  Solve the equation $\frac{3}{y + 5} + \frac{1}{2y} = \frac{5}{2y^{2} + 10y}$.
options:
- id: a
  content: |-
    $y = 5$
- id: b
  content: |-
    No solutions
  correct: true
- id: c
  content: |-
    $y = 2$
- id: d
  content: |-
    $y =-2$
- id: e
  content: |-
    $y = 1$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF2/Home|Home]]
[[MA/Mathematical-Foundations/MF2/0. Table of Contents/TOC|Table of Contents]]
