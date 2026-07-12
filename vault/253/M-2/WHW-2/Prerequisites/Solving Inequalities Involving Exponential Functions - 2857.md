# Solving Inequalities Involving Exponential Functions

<!--
lesson-id: 2857
topic-code: MF3.2.1.12
-->

## Table of Contents

- [Introduction](#introduction)
- [Solving an Inequality When the Base of the Exponential is Greater Than One](#solving-an-inequality-when-the-base-of-the-exponential-is-greater-than-one)
- [The Case When the Base of the Exponential is Between Zero and One](#the-case-when-the-base-of-the-exponential-is-between-zero-and-one)
- [Solving an Inequality When the Base of the Exponential is Between Zero and One](#solving-an-inequality-when-the-base-of-the-exponential-is-between-zero-and-one)
- [Comparing an Exponential to Zero or a Negative Number](#comparing-an-exponential-to-zero-or-a-negative-number)
- [Solving an Inequality When the Exponential is Compared to Zero or a Negative Number](#solving-an-inequality-when-the-exponential-is-compared-to-zero-or-a-negative-number)
- [Equations with Exponential Functions on Both Sides](#equations-with-exponential-functions-on-both-sides)
- [Solving an Inequality with Exponential Functions on Both Sides](#solving-an-inequality-with-exponential-functions-on-both-sides)

## Prerequisites

- [Combining the Laws of Logarithms](<../../../../MA/Mathematical-Foundations/MF2/5. Exponentials & Logarithms/5.2. The Laws of Logarithms/Lessons/5.2.4. Combining the Laws of Logarithms.md>)
- [Solving Exponential Equations With Different Bases Using Logarithms](<../../../../MA/Mathematical-Foundations/MF2/5. Exponentials & Logarithms/5.3. Exponential Equations/Lessons/5.3.4. Solving Exponential Equations With Different Bases Using Logarithms.md>)
- [Further Solving Linear Inequalities](<../../../../MA/Mathematical-Foundations/MF1/5. Equations & Inequalities/5.6. Solving Linear Inequalities/Lessons/5.6.7. Further Solving Linear Inequalities.md>)

---

<a id="introduction"></a>
## Introduction

When we have an exponential function in an inequality and the base of the exponential is greater than $1$, we can take the logarithm of both sides of the inequality.

For example, to solve the inequality

$$
2^x < 3
$$

we can take the logarithm (base $2$) of both sides and get

$$
\begin{bmatrix}\log_{2} (2^{x}) & < \log_{2} (3) \\ x & < \log_{2} (3)\end{bmatrix}
$$

The reason why we're allowed to take a logarithm of both sides of an inequality is that taking a logarithm preserves the order of numbers. That is to say, if $a < b$, then $\log_n (a) < \log_n (b)$, provided that $n > 1$ and $a,b>0$.

To see this concretely, consider the following order of numbers:

$$
0.5 < 1 < 2 < 3
$$

If we take the logarithm (base $2$) of all the numbers above, they stay in the same order:

$$
\underbrace{-1}_{\log_2(0.5)} < \underbrace{0}_{\log_2(1)} < \underbrace{1}_{\log_2(2)} < \underbrace{\,\, 1.585 \,\,}_{\log_2(3)}
$$

---

<a id="solving-an-inequality-when-the-base-of-the-exponential-is-greater-than-one"></a>
## Solving an Inequality When the Base of the Exponential is Greater Than One

**Example:** Solve the inequality $4e^x - 5 > 0$.

**Explanation**

Isolating the exponential term, we find

$$
\begin{bmatrix}4e^{x} - 5 & > 0 \\ 4e^{x} & > 5 \\ e^{x} & > \frac{5}{4}\end{bmatrix}
$$

Then, taking the natural logarithm of both sides and applying the laws of logarithms, we get

$$
\begin{bmatrix}\ln (e^{x}) & > \ln (\frac{5}{4}) \\ x & > \ln 5 - \ln 4\end{bmatrix}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-276944
content: |-
  Solve the inequality $2 \cdot 8^{2x} < \frac{1}{3}$.
options:
- id: a
  correct: true
  content: |-
    $x < \frac{-\ln 6}{2\ln 8}$
- id: b
  content: |-
    $x > \frac{-\ln 6}{2\ln 8}$
- id: c
  content: |-
    $x < \frac{\ln 6}{2\ln 8}$
- id: d
  content: |-
    $x < \frac{-\ln 3}{2\ln 8}$
- id: e
  content: |-
    $x > \frac{\ln 6}{2\ln 8}$
```

---

**Question 2:**

```quiz
type: radio
id: ma-87581
content: |-
  Solve the inequality $3e^{x} - 4 < 0$.
options:
- id: a
  content: |-
    $x < \ln 3 + \ln 4$
- id: b
  content: |-
    $x < \ln 3 - \ln 4$
- id: c
  content: |-
    $x > \ln 3 - \ln 4$
- id: d
  content: |-
    $x > \ln 4 - \ln 3$
- id: e
  correct: true
  content: |-
    $x < \ln 4 - \ln 3$
```

---

<a id="the-case-when-the-base-of-the-exponential-is-between-zero-and-one"></a>
## The Case When the Base of the Exponential is Between Zero and One

When we have an exponential function in an inequality and the base of the exponential is *less* than $1$, we can't take a logarithm of both sides using that same base. To see why not, consider the following inequality:

$$
\dfrac{1}{2} \lt 1
$$

If we take a logarithm with base

$$
\dfrac{1}{2}
$$

of both sides, then we get a false statement:

$$
\begin{bmatrix}\log_{\frac{1}{2}} (\frac{1}{2}) & ≮\log_{\frac{1}{2}} (1) \\ 1 & ≮0\end{bmatrix}
$$

However, we can get around this problem by always taking a logarithm with a base that's *greater* than $1$, such as the natural logarithm $\ln$, which has base

$$
e \approx 2.71 \,
$$

Then we can use the laws of logarithms to simplify the result.

For example, consider the following inequality:

$$
\left(\dfrac{2}{3} \right)^x < 5
$$

We can't take

$$
\log_\frac{2}{3}
$$

of both sides, but we can take the natural logarithm of both sides and simplify the result using the laws of logarithms:

$$
\begin{bmatrix}\ln [(\frac{2}{3})^{x}] & < \ln 5 \\ x\ln (\frac{2}{3}) & < \ln 5 \\ x(\ln 2 - \ln 3) & < \ln 5\end{bmatrix}
$$

Lastly, note that $\ln 2 - \ln 3$ is a negative quantity, so when we divide both sides by it, we need to flip the inequality:

$$
x \mid > \frac{\ln 5}{\ln 2 - \ln 3}
$$

---

<a id="solving-an-inequality-when-the-base-of-the-exponential-is-between-zero-and-one"></a>
## Solving an Inequality When the Base of the Exponential is Between Zero and One

**Example:** Solve the inequality $5 \cdot \left(\dfrac{3}{4} \right)^x + 2 \geq 12$.

**Explanation**

Isolating the exponential term, we find

$$
\begin{bmatrix}5 \cdot (\frac{3}{4})^{x} + 2 & \ge 12 \\ 5 \cdot (\frac{3}{4})^{x} & \ge 10 \\ (\frac{3}{4})^{x} & \ge 2\end{bmatrix}
$$

Then, taking the natural logarithm of both sides and applying the laws of logarithms, we get

$$
\begin{bmatrix}\ln [(\frac{3}{4})^{x}] & \ge \ln 2 \\ x\ln (\frac{3}{4}) & \ge \ln 2 \\ x(\ln 3 - \ln 4) & \ge \ln 2\end{bmatrix}
$$

Lastly, note that $\ln 3 - \ln 4$ is a negative quantity, so when we divide both sides by it, we need to flip the inequality:

$$
x \mid \le \frac{\ln 2}{\ln 3 - \ln 4}
$$

---

**Question 3:**

```quiz
type: radio
id: ma-87583
content: |-
  Solve the inequality $3 \cdot (\frac{2}{7})^{x} + 1 \ge 16$.
options:
- id: a
  content: |-
    $x \ge \frac{\ln 5}{\ln 2 - \ln 7}$
- id: b
  content: |-
    $x \le \frac{\ln 7}{\ln 5 - \ln 2}$
- id: c
  content: |-
    $x \ge \frac{\ln 2}{\ln 5 + \ln 7}$
- id: d
  correct: true
  content: |-
    $x \le \frac{\ln 5}{\ln 2 - \ln 7}$
- id: e
  content: |-
    $x \le \frac{\ln 2}{\ln 5 - \ln 7}$
```

---

**Question 4:**

```quiz
type: radio
id: ma-87584
content: |-
  Solve the inequality $(0.3)^{x - 2} - 6 \le 0$.
options:
- id: a
  correct: true
  content: |-
    $x \ge (\ln (6))/(\ln (0.3)) + 2$
- id: b
  content: |-
    $x \le (\ln (0.3))/(\ln (6)) - 2$
- id: c
  content: |-
    $x \le (\ln (6))/(\ln (0.3)) + 2$
- id: d
  content: |-
    $x \ge (\ln (0.3))/(\ln (6)) - 2$
- id: e
  content: |-
    $x \le \ln (6) - \ln (0.3) + 2$
```

---

<a id="comparing-an-exponential-to-zero-or-a-negative-number"></a>
## Comparing an Exponential to Zero or a Negative Number

Sometimes we might not be able to find the logarithm of both sides of inequality due to a negative number. For example, this happens in the following inequality:

$$
3^{x-1} \geq -5
$$

We can't take the logarithm of both sides because $\ln (-5)$ is not a real number. In general, a logarithm of a negative number is not a real number.

What we can do instead, though, is realize that a power of a positive number is always greater than $0$. In particular, in our situation, we have

$$
3^{x-1} > 0
$$

for all values of $x$ because any power of $3$ is positive.

So, because $3^{x-1} > 0$ for all values of $x$, we have

$$
3^{x-1} \geq -5
$$

for all values of $x$, and we conclude that the solution consists of all real numbers.

**Note:** If the inequality were flipped, i.e.,

$$
3^{x-1} \leq -5
$$

then the inequality would have no real solution. The reasoning is the same: because any power of $3$ is positive, we must have $3^{x-1} > 0$ for all values of $x$, so we can never have

$$
3^{x-1} \leq -5
$$

In general, if we have an inequality that compares a power of a positive number to zero or a negative number, it will always be the case that either the solution consists of all real numbers, or there is no real solution.

---

<a id="solving-an-inequality-when-the-exponential-is-compared-to-zero-or-a-negative-number"></a>
## Solving an Inequality When the Exponential is Compared to Zero or a Negative Number

**Example:** Solve the inequality $4 \cdot 3^{8-x} + 12 > 0$.

**Explanation**

Isolating the exponential term, we find

$$
\begin{bmatrix}4 \cdot 3^{8 - x} + 12 & > 0 \\ 4 \cdot 3^{8 - x} & > - 12 \\ 3^{8 - x} & > - 3\end{bmatrix}
$$

Because a power of a positive number is always greater than $0$, we must have

$$
3^{8-x} > 0
$$

for all values of $x$.

Therefore, the inequality $3^{8-x} > -3$ is satisfied for all real values of $x$.

---

**Question 5:**

```quiz
type: radio
id: ma-87594
content: |-
  Solve the inequality $2 \cdot 5^{3 - x} + 4 > 0$.
options:
- id: a
  content: |-
    no solutions
- id: b
  content: |-
    $x > 3 - \log_{5} (2)$
- id: c
  content: |-
    $x < 3 - \log_{5} (2)$
- id: d
  content: |-
    $x > \log_{5} (2) - 3$
- id: e
  correct: true
  content: |-
    all real numbers
```

---

**Question 6:**

```quiz
type: radio
id: ma-87595
content: |-
  Solve the inequality $9 - e^{4x} > 10$.
options:
- id: a
  content: |-
    all real numbers
- id: b
  content: |-
    $x < \frac{1}{4}$
- id: c
  content: |-
    $x > - \frac{1}{4}$
- id: d
  content: |-
    $x < - \frac{1}{4}$
- id: e
  correct: true
  content: |-
    no solutions
```

---

<a id="equations-with-exponential-functions-on-both-sides"></a>
## Equations with Exponential Functions on Both Sides

When an inequality has exponential functions on both sides, we can often solve it by taking a logarithm of both sides and applying the laws of logarithms.

For example, consider the inequality

$$
2^{x} < 3^{1-x}
$$

Taking the natural logarithm of both sides and applying the laws of logarithms, we solve the equation as follows:

$$
\begin{bmatrix}\ln (2^{x}) & < \ln (3^{1 - x}) \\ x\ln 2 & < (1 - x)\ln 3 \\ x\ln 2 & < \ln 3 - x\ln 3 \\ x\ln 2 + x\ln 3 & < \ln 3 \\ x(\ln 2 + \ln 3) & < \ln 3 \\ x & < \frac{\ln 3}{\ln 2 + \ln 3}\end{bmatrix}
$$

**Note:** Other times, it's possible to run into cases where there is no real solution, or where the solution is all real numbers. For example, consider the following equation:
$2^{x} < -3^{1-x}$

Since $2^x$ is always positive and $-3^{1-x}$ is always negative, we always have $2^x > -3^{1-x}$. This means the above inequality has no real solutions.

---

<a id="solving-an-inequality-with-exponential-functions-on-both-sides"></a>
## Solving an Inequality with Exponential Functions on Both Sides

**Example:** Solve the inequality $3 \cdot 5^x < 7^{3-x}$.

**Explanation**

Taking the natural logarithm of both sides and applying the laws of logarithms, we get the following:

$$
\begin{bmatrix}3 \cdot 5^{x} & < 7^{3 - x} \\ \ln (3 \cdot 5^{x}) & < \ln (7^{3 - x}) \\ \ln 3 + \ln (5^{x}) & < \ln (7^{3 - x}) \\ \ln 3 + x\ln 5 & < (3 - x)\ln 7 \\ \ln 3 + x\ln 5 & < 3\ln 7 - x\ln 7 \\ x\ln 5 + x\ln 7 & < 3\ln 7 - \ln 3 \\ x(\ln 5 + \ln 7) & < 3\ln 7 - \ln 3 \\ x & < \frac{3\ln 7 - \ln 3}{\ln 5 + \ln 7}\end{bmatrix}
$$

---

**Question 7:**

```quiz
type: radio
id: ma-87597
content: |-
  Solve the inequality $-3^{2x + 5} \le 7^{x}$.
options:
- id: a
  content: |-
    $x \le \frac{7\ln 5}{2\ln 3}$
- id: b
  content: |-
    $x \le \frac{2\ln 5}{7\ln 3}$
- id: c
  content: |-
    $x \ge \frac{2\ln 7}{5\ln 3}$
- id: d
  content: |-
    no solutions
- id: e
  correct: true
  content: |-
    all real numbers
```

---

**Question 8:**

```quiz
type: radio
id: ma-87596
content: |-
  Solve the inequality $2 \cdot 3^{x} < 5^{1 - x}$.
options:
- id: a
  content: |-
    $x > \frac{\ln 5 - \ln 2}{\ln 3 + \ln 5}$
- id: b
  content: |-
    $x < \frac{\ln 2 + \ln 5}{\ln 3 + \ln 5}$
- id: c
  content: |-
    $x > \frac{\ln 5 - \ln 2}{\ln 5 - \ln 3}$
- id: d
  content: |-
    $x < \frac{\ln 5 - \ln 2}{\ln 5 - \ln 3}$
- id: e
  correct: true
  content: |-
    $x < \frac{\ln 5 - \ln 2}{\ln 3 + \ln 5}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
