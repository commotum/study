# Approximating Areas With the Right Riemann Sum

<!--
lesson-id: 1281
topic-code: MF3.9.1.2
-->

## Table of Contents

- [Introduction](#introduction)
- [A General Formula for the Right Riemann Sum](#a-general-formula-for-the-right-riemann-sum)
- [Using the Right Riemann Sum With Regular Step Size](#using-the-right-riemann-sum-with-regular-step-size)
- [Solving for an Unknown Given the Value of a Right Riemann Sum With Regular Step Size](#solving-for-an-unknown-given-the-value-of-a-right-riemann-sum-with-regular-step-size)
- [Overestimates and Underestimates](#overestimates-and-underestimates)
- [Determining Whether a Right Riemann Sum is an Overestimate or Underestimate](#determining-whether-a-right-riemann-sum-is-an-overestimate-or-underestimate)
- [Right Riemann Sums with Irregular Step Size](#right-riemann-sums-with-irregular-step-size)
- [Using the Right Riemann Sum With Irregular Step Size](#using-the-right-riemann-sum-with-irregular-step-size)

## Prerequisites

- [Graphs of General Quadratic Functions](<../../../../MA/Mathematical-Foundations/MF2/1. Quadratics/1.2. Quadratic Functions/Lessons/1.2.3. Graphs of General Quadratic Functions.md>)
- [Areas of Rectangles and Squares](<../../../../MA/Mathematical-Foundations/MF1/13. Polygons/13.3. Area and Perimeter/Lessons/13.3.1. Areas of Rectangles and Squares.md>)
- [Increasing and Decreasing Functions](<../../../../MA/Mathematical-Foundations/MF1/8. Functions/8.1. Functions/Lessons/8.1.10. Increasing and Decreasing Functions.md>)

---

<a id="introduction"></a>
## Introduction

Suppose that we wish to find the area $\mathcal{A}$ under the curve $y=x^2$ between the $x$-values $x=1$ and $x=4$, as shown below.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/29139937c3a52324919577e8973a538e.png>)

We can approximate the area using, for instance, the area of three rectangles, each with a width equal to $1$.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/13b2995c70bd99847493e9ace4e179ce.png>)

So, we find the area of each rectangle and then add them all together.

$$
\begin{aligned}
\mathcal{A} &\approx
\overbrace{\overbrace{f(2)}^{\text{height}} \cdot \underbrace{1}_{\text{width}}}^{\text{1st rectangle}}
+
\overbrace{\overbrace{f(3)}^{\text{height}} \cdot \underbrace{1}_{\text{width}}}^{\text{2nd rectangle}}
+
\overbrace{\overbrace{f(4)}^{\text{height}} \cdot \underbrace{1}_{\text{width}}}^{\text{3rd rectangle}} \\
&= [2^2 \cdot 1] + [3^2 \cdot 1] + [4^2 \cdot 1] \\
&= 4 + 9 + 16 \\
&= 29
\end{aligned}
$$

Here, we approximated the area using a **right Riemann sum**, which means that the top-*right* corner of each rectangle touches the curve.

Because the function is *strictly increasing* over the interval $[1,4]$, the rectangles reach *above* the function, which means our approximation is an *overestimate* of the actual area (see the picture above).

---

<a id="a-general-formula-for-the-right-riemann-sum"></a>
## A General Formula for the Right Riemann Sum

In general, the area $\mathcal{A}$ under the curve $y=f(x)$ over the interval $[a,b]$ can be approximated using a right Riemann sum by calculating the area of each rectangle and adding them together.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/b557451067ef766d284853bb5854864a.png>)

We can write this mathematically as

$$
\mathcal{A} \approx f(x_1)\Delta x + f(x_2)\Delta x + f(x_3)\Delta x + \cdots + f(x_n)\Delta x
$$

where $n$ is the number of rectangles and the step size $\Delta x$ is given by

$$
\Delta x=\dfrac{b-a}{n}
$$

We can simplify by factoring out the $\Delta x$, which gives the following general formula:

$$
\begin{aligned}
\mathcal{A} &\approx \left(f(x_1) + f(x_2) + f(x_3) + \cdots + f(x_n)\right)\Delta x \\
&= \left(\sum_{i=1}^{n} f(x_i)\right)\Delta x
\end{aligned}
$$

---

<a id="using-the-right-riemann-sum-with-regular-step-size"></a>
## Using the Right Riemann Sum With Regular Step Size

**Example:** Estimate the area under the curve $y=(2x-4)^2+2$ over the interval $[0,2]$ using a right Riemann sum with step size $\Delta x=0.5$.

**Explanation**

Let's sketch our situation.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/f2863cae66429a4430e98d8113e72f29.png>)

The area $\mathcal{A}$ can be approximated using the formula

$$
\mathcal{A} \approx
\left(\overbrace{{\color{red}{f(0.5)}} + {\color{red}{f(1)}} + {\color{red}{f(1.5)}} + {\color{red}{f(2)}}}^{\color{red}{\large\text{heights}}}\right)
\cdot
\underbrace{{\color{blue}{\Delta x}}}_{\color{blue}{\large\text{width}}}
$$

So, we now set up a table with the values of $f(x)$ at each point:

| $x$ | $0.5$ | $1$ | $1.5$ | $2$ |
| --- | ---: | ---: | ---: | ---: |
| $f(x)$ | $11$ | $6$ | $3$ | $2$ |

Finally, we obtain the following approximation for our area:

$$
\begin{aligned}
\mathcal{A} &\approx (11 + 6 + 3 + 2) \cdot 0.5 \\
&= 22 \cdot 0.5 \\
&= 11
\end{aligned}
$$

---

**Question 1**

```quiz
type: radio
id: ma-74324
content: |-
  > A calculator is required to answer this question.

  Estimate the area under the curve $y = 4 - 2x$ over the interval $[0, 1]$ using a right Riemann sum with step size $\Delta x = 0.25$.
options:
- id: a
  content: |-
    $3.5$
- id: b
  content: |-
    $3.25$
- id: c
  content: |-
    $2.5$
- id: d
  correct: true
  content: |-
    $2.75$
- id: e
  content: |-
    $4$
```

---

**Question 2**

```quiz
type: radio
id: ma-4411
content: |-
  > A calculator is required to answer this question.

  Estimate the area under the curve $y = x^{2}$ over the interval $[- 1, 1]$ using a right Riemann sum with step size $\Delta x = 0.5$.
options:
- id: a
  content: |-
    $0.5$
- id: b
  content: |-
    $0.43$
- id: c
  correct: true
  content: |-
    $0.75$
- id: d
  content: |-
    $0.67$
- id: e
  content: |-
    $0$
```

---

<a id="solving-for-an-unknown-given-the-value-of-a-right-riemann-sum-with-regular-step-size"></a>
## Solving for an Unknown Given the Value of a Right Riemann Sum With Regular Step Size

**Example:** The table below gives some values of a continuous function $f(x)$ on the closed interval $[-4,2]$. The right Riemann sum approximation to the area under the curve $y=f(x)$ with $3$ equal subintervals has a value of $12$. What must be the value of $k$?

| $x$ | $-4$ | $-2$ | $0$ | $2$ |
| --- | ---: | ---: | ---: | ---: |
| $f(x)$ | $5$ | $3$ | $k$ | $2$ |

**Explanation**

The area $\mathcal{A}$ under the graph can be approximated using the formula for the right Riemann sum:

$$
\mathcal{A} \approx
\left(\overbrace{{\color{red}{f(-2)}} + {\color{red}{f(0)}} + {\color{red}{f(2)}}}^{\color{red}{\large\text{heights}}}\right)
\cdot
\underbrace{{\color{blue}{\Delta x}}}_{\color{blue}{\large\text{width}}}
$$

So, we set up a table with the values of $f(x)$ at each point:

| $x$ | $-2$ | $0$ | $2$ |
| --- | ---: | ---: | ---: |
| $f(x)$ | $3$ | $k$ | $2$ |

Now, we obtain the following approximation for the area:

$$
\begin{aligned}
\mathcal{A} &\approx (3 + k + 2) \cdot 2 \\
&= (k + 5) \cdot 2 \\
&= 2k + 10
\end{aligned}
$$

Since we are given that $\mathcal{A}$ must be $12$, we obtain

$$
\begin{aligned}
2k + 10 &= 12 \\
2k &= 2 \\
k &= 1
\end{aligned}
$$

---

**Question 3**

```quiz
type: radio
id: ma-49090
content: |-
  > A calculator is required to answer this question.

  The table below gives some values of a continuous function $f(x)$ on the closed interval $[- 2, 7]$. The right Riemann sum approximation to the area under the curve $y = f(x)$ with $3$ equal subintervals has a value of $30$. What must be the value of $k$?

  | $x$ | $-2$ | $1$ | $4$ | $7$ |
  | --- | ---: | ---: | ---: | ---: |
  | $f(x)$ | $1$ | $k$ | $3$ | $2$ |
options:
- id: a
  content: |-
    $8$
- id: b
  content: |-
    $2$
- id: c
  content: |-
    $15$
- id: d
  correct: true
  content: |-
    $5$
- id: e
  content: |-
    $12$
```

---

**Question 4**

```quiz
type: radio
id: ma-74343
content: |-
  > A calculator is required to answer this question.

  The table below gives some values of a continuous function $f(x)$ on the closed interval $[2, 8]$. The right Riemann sum approximation to the area under the curve $y = f(x)$ with $3$ equal subintervals has a value of $14$. What must be the value of $k$?

  | $x$ | $2$ | $4$ | $6$ | $8$ |
  | --- | ---: | ---: | ---: | ---: |
  | $f(x)$ | $3$ | $1$ | $k$ | $4$ |
options:
- id: a
  content: |-
    $5$
- id: b
  content: |-
    $9$
- id: c
  content: |-
    $0$
- id: d
  correct: true
  content: |-
    $2$
- id: e
  content: |-
    $6$
```

---

<a id="overestimates-and-underestimates"></a>
## Overestimates and Underestimates

Whether the right Riemann sum underestimates or overestimates the actual area under a function depends on whether the function is increasing or decreasing.

- If the function $f(x)$ is increasing, then the rectangles reach *above* the function, which means the right Riemann sum gives an *overestimate* of the actual area under the curve $y=f(x)$.

  ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/9748837bbceeccf80084a79949f81507.png>)
- If the function $f(x)$ is decreasing, then the rectangles fall *below* the function, which means the right Riemann sum gives an *underestimate* of the actual area under the curve $y=f(x)$.

  ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/c31e0ca0a71df0308a782c70fe691900.png>)

---

<a id="determining-whether-a-right-riemann-sum-is-an-overestimate-or-underestimate"></a>
## Determining Whether a Right Riemann Sum is an Overestimate or Underestimate

**Example:** Estimate the area under the curve $y=(2x-4)^2+2$ over the interval $[0,2]$ using a right Riemann sum with step size $\Delta x=0.5$. Is this an overestimate or an underestimate?

**Explanation**

Let's sketch our situation.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/a8e0ae48fa80476387e12db42712712d.png>)

The area $\mathcal{A}$ can be approximated using the formula

$$
\mathcal{A} \approx
\left(\overbrace{{\color{red}{f(0.5)}} + {\color{red}{f(1)}} + {\color{red}{f(1.5)}} + {\color{red}{f(2)}}}^{\color{red}{\large\text{heights}}}\right)
\cdot
\underbrace{{\color{blue}{\Delta x}}}_{\color{blue}{\large\text{width}}}
$$

So, we now set up a table with the values of $f(x)$ at each point:

| $x$ | $0.5$ | $1$ | $1.5$ | $2$ |
| --- | ---: | ---: | ---: | ---: |
| $f(x)$ | $11$ | $6$ | $3$ | $2$ |

Finally, we obtain the following approximation for our area:

$$
\begin{aligned}
\mathcal{A} &\approx (11 + 6 + 3 + 2) \cdot 0.5 \\
&= 22 \cdot 0.5 \\
&= 11
\end{aligned}
$$

Because the function is *strictly decreasing* over the interval $[0,2]$, the rectangles reach *below* the function, which means our approximation is an *underestimate* of the correct area.

---

**Question 5**

```quiz
type: radio
id: ma-49117
content: |-
  > A calculator is required to answer this question.

  A right Riemann sum is used to approximate the area under the curve $y = f(x)$ between $x =-3$ and $x =-1$ for each of the functions below. For which function does the Riemann sum give an *overestimate* of the area?
options:
- id: a
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49117-a-3.png>)
- id: b
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49117-a-5.png>)
- id: c
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49117-a-4.png>)
- id: d
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49117-a-1.png>)
  correct: true
- id: e
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49117-a-2.png>)
```

---

**Question 6**

```quiz
type: radio
id: ma-49120
content: |-
  > A calculator is required to answer this question.

  A right Riemann sum is used to approximate the area under the curve $y = f(x)$ between $x = 2$ and $x = 4$ for each of the functions below. For which function does the Riemann sum give an *underestimate* of the area?
options:
- id: a
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49120-a-2.png>)
- id: b
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49120-a-3.png>)
- id: c
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49120-a-1.png>)
  correct: true
- id: d
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49120-a-4.png>)
- id: e
  content: |-
    ![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/q-49120-a-5.png>)
```

---

<a id="right-riemann-sums-with-irregular-step-size"></a>
## Right Riemann Sums with Irregular Step Size

In the last few examples, the step size $\Delta x$ was the same for each of the rectangles. In these cases, we say that the step size is **regular**.

There are situations where the step size can vary, which we call an **irregular step size**. But we can still use a right Riemann sum to approximate the area.

For example, let's use a right Riemann sum to approximate the area under the curve of the continuous function $y=f(x)$ whose data is given in the table below.

| $x$ | $1$ | $1.5$ | $2.5$ | $4$ |
| --- | ---: | ---: | ---: | ---: |
| $f(x)$ | $1$ | $2$ | $6$ | $8$ |

The first thing we note is that the domain of the function $y=f(x)$ is *partitioned* as

$$
[1,4] = [1,1.5] \cup [1.5,2.5] \cup [2.5,4]
$$

Let's plot what this function might look like, using the values given in the table.

![](<../Source/Approximating Areas With the Right Riemann Sum - 1281/Images/22b27a2d788b7111178adea9862f3120.png>)

We've drawn some rectangles to help us calculate our right Riemann sum, and we have chosen the heights of each rectangle to be calculated using the right endpoint of each interval.

By calculating the area of each rectangle, we obtain the following approximation for our area:

$$
\mathcal{A} \approx f(1.5)(1.5 - 1) + f(2.5)(2.5 - 1.5) + f(4)(4 - 2.5)
$$

Plugging our numbers into the above, we find

$$
\begin{aligned}
\mathcal{A}
&\approx {\color{red}{2}} \cdot ({\color{blue}{1.5 - 1}})
+ {\color{red}{6}} \cdot ({\color{blue}{2.5 - 1.5}})
+ {\color{red}{8}} \cdot ({\color{blue}{4 - 2.5}}) \\
&= {\color{red}{2}} \cdot {\color{blue}{0.5}}
+ {\color{red}{6}} \cdot {\color{blue}{1}}
+ {\color{red}{8}} \cdot {\color{blue}{1.5}} \\
&= 1 + 6 + 12 \\
&= 19
\end{aligned}
$$

---

<a id="using-the-right-riemann-sum-with-irregular-step-size"></a>
## Using the Right Riemann Sum With Irregular Step Size

**Example:** The following table shows the values of a continuous function $f(x)$ over the interval $[1,4]$.

| $x$ | $1$ | $2$ | $3$ | $3.5$ | $4$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $f(x)$ | $0$ | $4$ | $8.5$ | $10$ | $8$ |

Use the right Riemann sum, with the four subintervals indicated by the data, to approximate the area under the curve $y=f(x)$ over the interval $[1,4]$.

**Explanation**

In this case, we have $n=4$ rectangles. Using the right Riemann sum, the area is computed as

$$
\mathcal{A} \approx f(2)\Delta x_1 + f(3)\Delta x_2 + f(3.5)\Delta x_3 + f(4)\Delta x_4
$$

where each $\Delta x_i$ is calculated by considering the step between a particular $x$-value and the previous one, i.e.,

$$
\Delta x_i = x_i - x_{i-1}
$$

We set up a table of values that include the $\Delta x$'s.

| $x$ | $1$ | $2$ | $3$ | $3.5$ | $4$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $\Delta x$ | $-$ | $1$ | $1$ | $0.5$ | $0.5$ |
| $f(x)$ | $-$ | $4$ | $8.5$ | $10$ | $8$ |

Finally, we plug in the numbers to approximate the area under the curve, and get

$$
\begin{aligned}
\mathcal{A} &\approx 4 \cdot 1 + 8.5 \cdot 1 + 10 \cdot 0.5 + 8 \cdot 0.5 \\
&= 4 + 8.5 + 5 + 4 \\
&= 21.5
\end{aligned}
$$

---

**Question 7**

```quiz
type: radio
id: ma-49111
content: |-
  > A calculator is required to answer this question.

  The table below gives the rate of change $w(t)$, in pounds per year, in a child's weight when the child is exactly $t$ years old.

  | $t$ (years) | $1$ | $1.5$ | $2$ | $3$ | $4$ |
  | --- | ---: | ---: | ---: | ---: | ---: |
  | $w(t)$ (pounds/year) | $20$ | $12$ | $10$ | $15$ | $10$ |

  Use the right Riemann sum over $[1, 4]$ with four subintervals to approximate the total increase in the weight of the child.
options:
- id: a
  content: |-
    $51\text{ pounds}$
- id: b
  correct: true
  content: |-
    $36\text{ pounds}$
- id: c
  content: |-
    $31\text{ pounds}$
- id: d
  content: |-
    $61\text{ pounds}$
- id: e
  content: |-
    $41\text{ pounds}$
```

---

**Question 8**

```quiz
type: radio
id: ma-49107
content: |-
  > A calculator is required to answer this question.

  Pauline is selling orange juice on a market stall. The table below gives the rate $l(t)$, in liters per hour, of lemonade sold at certain moments during the day.

  | $t$ (hours) | $1$ | $3$ | $4$ | $7$ |
  | --- | ---: | ---: | ---: | ---: |
  | $l(t)$ (liters/hour) | $3$ | $2$ | $4$ | $5$ |

  Use the right Riemann sum for $l(t)$ over the interval $[1, 7]$ with three subintervals to approximate the total number of liters Pauline sold.
options:
- id: a
  content: |-
    $28\text{ liters}$
- id: b
  content: |-
    $11\text{ liters}$
- id: c
  correct: true
  content: |-
    $23\text{ liters}$
- id: d
  content: |-
    $26\text{ liters}$
- id: e
  content: |-
    $14\text{ liters}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
