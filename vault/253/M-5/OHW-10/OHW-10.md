## Prerequisites

- [Lesson-Name](<Prerequisites/Lesson-Path>)
- [Lesson-Name](<Prerequisites/Lesson-Path>)
- [Lesson-Name](<Prerequisites/Lesson-Path>)

## Lessons

- [Lesson-Name](<Lessons/Lesson-Path>)
- [Lesson-Name](<Lessons/Lesson-Path>)
- [Lesson-Name](<Lessons/Lesson-Path>)

---
## Problem 1

Find the fifth-degree Taylor polynomial $P_5(x)$ for

$$
f(x)=\ln(1+x)
$$

about $c=0$. Give exact coefficients.

---
## Problem 2

Find the fifth-degree Taylor polynomial $P_5(x)$ for

$$
f(x)=3\cos(x)
$$

about $c=\frac{\pi}{2}$. Give exact coefficients.

---
## Problem 3

Find the fifth-degree Taylor polynomial $P_5(x)$ for

$$
f(x)=5e^{-x}
$$

about $c=0$. Give exact coefficients.

---
## Problem 4

Find the fifth-degree Taylor polynomial $P_5(x)$ for

$$
f(x)=\frac{1}{1+x}
$$

about $c=0$. Give exact coefficients.

---
## Problem 5

Find the fifth-degree Taylor polynomial $P_5(x)$ for

$$
f(x)=11xe^x
$$

about $c=1$. Give exact coefficients.

---
## Problem 6

Let $P_6(x)$ be the sixth-degree Taylor polynomial for $y=\cos(x)$ about $0$.

1. Find $P_6(x)$ exactly.
2. Choose the graph that correctly compares curve 1, $y=\cos(x)$, with curve 2, $y=P_6(x)$.
3. Use $P_6(x)$ to approximate $\cos\left(\frac{\pi}{15}\right)$ to three decimal places.
4. Give an upper bound for the absolute error $|E|$.
5. Determine the interval of $x$-values for which the approximation error is at most $0.0001$. Give interval endpoints to three decimal places.

---
## Problem 7

Let $P_3(x)$ be the third-degree Taylor polynomial for $y=e^x$ about $0$.

1. Find $P_3(x)$ exactly.
2. Choose the graph that correctly compares curve 1, $y=e^x$, with curve 2, $y=P_3(x)$.
3. Use $P_3(x)$ to approximate $e^{2/5}$ to four decimal places.
4. Find the approximation error to four decimal places.
5. Determine the interval of $x$-values for which the approximation error is at most $0.0001$. Give interval endpoints to four decimal places.

---
## Problem 8

Let

$$
y=\frac{1}{\sqrt{4+x}}.
$$

1. Choose the Maclaurin series for $y$.

   - $\displaystyle \frac12\sum_{k=0}^{\infty}\binom{-\frac12}{k}\left(\frac{x}{4}\right)^k$
   - $\displaystyle \sum_{k=0}^{\infty}\binom{-\frac12}{k}\left(\frac{x}{4}\right)^k$
   - $\displaystyle \frac12\sum_{k=0}^{\infty}\binom{-\frac12}{k}x^k$
   - $\displaystyle \frac12\sum_{k=0}^{\infty}\binom{k}{-\frac12}\left(\frac{x}{4}\right)^k$
   - $\displaystyle \frac12\sum_{k=0}^{\infty}\left(\frac{x}{4}\right)^k$

2. Find the interval of convergence.
3. Find the third-degree Taylor polynomial $P_3(x)$ about $0$.
4. Choose the graph that correctly compares $y$ with $P_3(x)$.
5. Use $P_3(x)$ to approximate $\frac{1}{\sqrt{4.4}}$ to five decimal places, then give the approximation error in scientific notation to four significant figures.

---
## Problem 9

Let

$$
y=\frac{1}{4-x}.
$$

1. Choose the Maclaurin series for $y$.

   - $\displaystyle \frac14\sum_{k=0}^{\infty}x^k$
   - $\displaystyle \sum_{k=0}^{\infty}\left(\frac{x}{4}\right)^k$
   - $\displaystyle \frac14\sum_{k=0}^{\infty}\left(\frac{x}{4}\right)^k$
   - $\displaystyle 4\sum_{k=0}^{\infty}x^k$
   - $\displaystyle 4\sum_{k=0}^{\infty}\left(\frac{x}{4}\right)^k$

2. Find the interval of convergence.
3. Find the third-degree Taylor polynomial $P_3(x)$ about $0$.
4. Choose the graph that correctly compares $y$ with $P_3(x)$.

---
## Problem 10

Approximate the integral using the first four terms of the relevant Maclaurin series. Give the result to three decimal places.

$$
\int_0^1 \cos\left(x^{15}\right)\,dx
$$

---
## Problem 11

Approximate the integral using the first four terms of the relevant Maclaurin series. Give the result to three decimal places.

$$
\int_0^{1/7}\sqrt[3]{1+x^6}\,dx
$$

---
## Problem 12

Approximate the integral using the first four terms of the relevant Maclaurin series. Give the result to three decimal places.

$$
\int_0^{1/7}\sqrt[6]{1+x}\,dx
$$

---
## Problem 13

Use the recursive formula

$$
\ln(N+1)=\ln(N)+2\left[
\frac{1}{2N+1}
+\frac13\left(\frac{1}{2N+1}\right)^3
+\frac15\left(\frac{1}{2N+1}\right)^5
+\cdots
\right]
$$

to estimate $\ln(8)$ using only the first three terms inside the brackets. Give the result to five decimal places.

---
## Problem 14

For each calculation, determine how many terms $N$ of the Maclaurin series are required so that the error is at most $0.001$. Give whole-number answers.

1. $F(x)=\sin(x)$ at $x=6^\circ$
2. $F(x)=\cos(x)$ at $x=12^\circ$
3. $F(x)=\tan^{-1}(x)$ at $x=0.15$

---
## Problem 15

Gregory's series for $\pi$ converges slowly. Use

$$
\tan^{-1}(1)=\tan^{-1}\left(\frac12\right)+\tan^{-1}\left(\frac13\right)
$$

together with Gregory's series evaluated at $x=\frac12$ and $x=\frac13$ to approximate $\pi$ using the first four terms. Give an exact fractional expression.

---
## Problem 16

The graphs of $y=\cot(x)$ and $y=\lambda x$ intersect near $x=\frac{\pi}{2}$ when $\lambda$ is small. Let

$$
f(x)=\cot(x)-\lambda x.
$$

1. Find the second-degree Taylor polynomial $P_2(x)$ for $f$ about $\frac{\pi}{2}$.
2. Use $P_2(x)$ to obtain an approximate solution of $\cot(x)=\lambda x$.

Use exact symbolic notation and include the parameter $\lambda$ where needed.
