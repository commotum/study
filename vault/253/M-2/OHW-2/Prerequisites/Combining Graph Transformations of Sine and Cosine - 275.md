# Combining Graph Transformations of Sine and Cosine

<!--
lesson-id: 275
topic-code: MF2.9.7.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Identifying Shifts of a Transformed Sine or Cosine Curve](#identifying-shifts-of-a-transformed-sine-or-cosine-curve)
- [Identifying the Vertical Stretch of a Transformed Sine or Cosine Curve](#identifying-the-vertical-stretch-of-a-transformed-sine-or-cosine-curve)
- [Identifying the Horizontal Stretch of a Transformed Sine or Cosine Curve](#identifying-the-horizontal-stretch-of-a-transformed-sine-or-cosine-curve)
- [Identifying the Equation of a Transformed Sine Curve](#identifying-the-equation-of-a-transformed-sine-curve)

## Prerequisites

- [Vertical Translations of Trigonometric Functions](<9.7.1. Vertical Translations of Trigonometric Functions.md>)
- [Horizontal Stretches of Trigonometric Functions](<9.7.4. Horizontal Stretches of Trigonometric Functions.md>)
- [Combining Graph Transformations: Two Operations](<../../../4. Functions/4.2. Graph Transformations of Functions/Lessons/4.2.7. Combining Graph Transformations- Two Operations.md>)
- [Horizontal Translations of Trigonometric Functions](<9.7.3. Horizontal Translations of Trigonometric Functions.md>)
- [Vertical Stretches of Trigonometric Functions](<9.7.2. Vertical Stretches of Trigonometric Functions.md>)

---

<a id="introduction"></a>
## Introduction

We can combine vertical and horizontal shifts and stretches to get new transformed sine and cosine curves. For example, let's draw the graph of the curve

$$
y = 2 \cos\left(x+ 2\right) - 1
$$

To plot the given curve, we follow these steps:

- Start with the graph of $y=\cos{x}$.

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/ada7f7603853d35bcf0e03ac54d53157.png>)

- Then, stretch it parallel to the $y$-axis by a stretch factor of $2$ to give $y=2\cos{x}$.

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/1b0c78d79016771cccd6aa50fb60bf02.png>)

- Next, shift to the **left** by $2$ units to give $y=2\cos(x + 2)$.

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/504ee16c673208beb2774641c5e66863.png>)

- Finally, shift it **down** by $1$ unit to give $y=2\cos\left(x + 2\right) - 1$.

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/02789c684c86be83fdb2c38704233384.png>)

---

<a id="identifying-shifts-of-a-transformed-sine-or-cosine-curve"></a>
## Identifying Shifts of a Transformed Sine or Cosine Curve

**Example:** The graph above shows the function $y=2\sin{(x+C)}$, where $C$ is a constant. Given that $-\pi < C < \pi$, what is the value of $C$?

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/18432f4bbf6c1b1d25ed7b28e8a18a15.png>)

**Explanation**

The constant $C$ is the phase shift of the function.

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/83b66425886a41270f3088d72b5cc1e8.png>)

To plot the given function, we follow these steps:

- Take the graph of $y=\sin x$.
- Vertically stretch it by a scale factor of $2$ to give $y = 2 \sin x$.
- Then, shift it by $2$ units **right** to give $y=2\sin \left(x-2\right)$.

Therefore, $C=-2$.

---

**Question 1**

```quiz
type: radio
id: ma-65530
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65530.png>)
  
  The graph above shows the function $y = 5\cos (x + C)$, where $C$ is a constant. Given that $- π < C < π$, what is the value of $C$?
options:
- id: a
  content: |-
    $-3$
  correct: true
- id: b
  content: |-
    $6$
- id: c
  content: |-
    $-5$
- id: d
  content: |-
    $5$
- id: e
  content: |-
    $3$
```

---

**Question 2**

```quiz
type: radio
id: ma-65635
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65635.png>)
  
  The graph above shows the function $y = \frac{1}{2}\sin x + D$. What is the value of $D$?
options:
- id: a
  content: |-
    $3$
  correct: true
- id: b
  content: |-
    $\frac{1}{3}$
- id: c
  content: |-
    $\frac{1}{2}$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $-3$
```

---

<a id="identifying-the-vertical-stretch-of-a-transformed-sine-or-cosine-curve"></a>
## Identifying the Vertical Stretch of a Transformed Sine or Cosine Curve

**Example:** The graph above shows the function $y=A\cos\left(x+2\right)$, where $A$ is a constant. What is $A$?

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/5e0c2c562d9337497b4b8c194e38cd14.png>)

**Explanation**

The constant $A$ is the amplitude of the function.

From the graph, we see that the maximum value is

$$
y_\max=\sqrt{2}
$$

and the minimum value is

$$
y_\min=-\sqrt{2}
$$

Therefore, the amplitude is

$$
A = \dfrac{y_\max-y_\min}{2} = \dfrac{\sqrt{2}-(-\sqrt{2})}{2}=\sqrt{2}
$$

---

**Question 3**

```quiz
type: radio
id: ma-65673
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65673.png>)
  
  The graph above shows the function $y = A\sin x + D$, where $A$ and $D$ are constants. What is $A - D$?
options:
- id: a
  content: |-
    $-3$
- id: b
  content: |-
    $-2$
- id: c
  content: |-
    $-1$
- id: d
  content: |-
    $5$
  correct: true
- id: e
  content: |-
    $1$
```

---

**Question 4**

```quiz
type: radio
id: ma-65651
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65651.png>)
  
  The graph above shows the function $y = A\cos (x + \frac{π}{3})$, where $A$ is a constant. What is $A$?
options:
- id: a
  content: |-
    $1$
- id: b
  content: |-
    $\frac{5}{2}$
  correct: true
- id: c
  content: |-
    $\frac{2}{3}$
- id: d
  content: |-
    $\frac{2}{5}$
- id: e
  content: |-
    $\frac{1}{5}$
```

---

<a id="identifying-the-horizontal-stretch-of-a-transformed-sine-or-cosine-curve"></a>
## Identifying the Horizontal Stretch of a Transformed Sine or Cosine Curve

**Example:** The graph above shows the function $y=4\sin{(Bx)}$, where $B$ is a positive constant. What is $B$?

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/8f5530a7155089ee92031b433f06893f.png>)

**Explanation**

The constant $B$ is the horizontal stretch of the function.

We can see that the function repeats itself $3$ times in the interval $x\in[0,2\pi]$. Therefore, the period $T$ of the function is

$$
T = \dfrac{2\pi}{3}
$$

The formula for the period $T$ of the function

$$
y=A\sin(Bx + C) + D
$$

is given by

$$
T = \dfrac{2\pi}{B}
$$

Applying the formula for the period, we get

$$
\dfrac{2\pi}{3} = \dfrac{2\pi}{B}\quad\Longrightarrow\quad B = \dfrac{2\pi}{\left(\dfrac{2\pi}{3}\right)} = 3
$$

Therefore, $B=3$.

---

**Question 5**

```quiz
type: radio
id: ma-65414
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65414.png>)
  
  The graph above shows the function $y = \cos (Bx) + D$, where $B$ and $D$ are constants. Given that $B > 0$, what is $B + D$?
options:
- id: a
  content: |-
    $1$
  correct: true
- id: b
  content: |-
    $\frac{1}{2}$
- id: c
  content: |-
    $\frac{3}{2}$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $3$
```

---

**Question 6**

```quiz
type: radio
id: ma-65653
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-65653.png>)
  
  The graph above shows the function $y = \cos Bx - 2$, where $B$ is a positive constant. What is the value of $B$?
options:
- id: a
  content: |-
    $5$
- id: b
  content: |-
    $\frac{5}{2}$
  correct: true
- id: c
  content: |-
    $\frac{2}{5}$
- id: d
  content: |-
    $2$
- id: e
  content: |-
    $\frac{1}{5}$
```

---

<a id="identifying-the-equation-of-a-transformed-sine-curve"></a>
## Identifying the Equation of a Transformed Sine Curve

**Example:** The graph above represents a transformed sine curve. What is the equation of the graph?

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/17361430717e9011126b9fcc1df3819b.png>)

**Explanation**

![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/03649ffb7c21d1e5fb877f7f68681b68.png>)

To plot the given curve, we follow these steps:

- Start with the graph of $y=\sin x$.
- Then, stretch it parallel to the $y$-axis by a stretch factor of $3$ to give $y=3\sin x$.
- Finally, shift it **up** by $3$ units to give $y=3\sin x + 3$.

Therefore, the given curve is the graph of

$$
y=3\sin x + 3
$$

---

**Question 7**

```quiz
type: radio
id: ma-12540
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-12540.png>)
  
  What is the equation of the graph shown above?
options:
- id: a
  content: |-
    $y = 2\sin (x)$
- id: b
  content: |-
    $y = 4\sin (x)$
- id: c
  content: |-
    $y = 2\sin (\frac{x}{2})$
  correct: true
- id: d
  content: |-
    $y = 4\sin (2x)$
- id: e
  content: |-
    $y = \sin (\frac{x}{2})$
```

---

**Question 8**

```quiz
type: radio
id: ma-6620
content: |-
  ![](<../Source/Combining Graph Transformations of Sine and Cosine - 275/Images/q-6620.png>)
  
  What is the equation of the graph shown above?
options:
- id: a
  content: |-
    $y = 2\sin x + 4$
  correct: true
- id: b
  content: |-
    $y = 2\sin x$
- id: c
  content: |-
    $y = 4\sin x + 2$
- id: d
  content: |-
    $y = \sin x + 4$
- id: e
  content: |-
    $y = \sin 2x + 4$
```

```update-progress
```

[[MA/Mathematical-Foundations/MF2/Home|Home]]
[[MA/Mathematical-Foundations/MF2/0. Table of Contents/TOC|Table of Contents]]
