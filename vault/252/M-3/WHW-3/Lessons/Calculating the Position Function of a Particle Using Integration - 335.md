# Calculating the Position Function of a Particle Using Integration

<!--
lesson-id: 335
topic-code: MF3.11.1.6
-->

## Table of Contents

- [Introduction](#introduction)
- [Determining the Position of a Particle Given Its Velocity and Initial Position](#determining-the-position-of-a-particle-given-its-velocity-and-initial-position)
- [Determining the Position of a Particle Given Its Acceleration, Initial Velocity and Initial Position](#determining-the-position-of-a-particle-given-its-acceleration-initial-velocity-and-initial-position)

## Prerequisites

- [Calculating Velocity Using Integration](<11.1.4. Calculating Velocity Using Integration.md>)
- [Calculating Distance From a Speed-Time Graph](<../../../../AG1/2. Two-Variable Equations & Inequalities/2.2. Modeling With Two-Variable Linear Equations/Lessons/2.2.7. Calculating Distance From a Speed-Time Graph.md>)

---

<a id="introduction"></a>
## Introduction

For a particle moving along a straight line with position $x(t)$, we calculate the velocity $v(t)$ by differentiating $x$ with respect to $t$. This means that $x(t)$ is the antiderivative of the velocity $v(t)$.

Therefore, to find the position $x(t)$ of a particle given its velocity $v(t)$, we integrate $v(t)$ with respect to $t$:

$$
v(t) = \frac{\textrm{d}x}{\textrm{d}t} \quad\Rightarrow\quad x(t) = \int v(t) \, \textrm{d}t
$$

We determine the arbitrary constant of integration using some information that's known about the system.

---

<a id="determining-the-position-of-a-particle-given-its-velocity-and-initial-position"></a>
## Determining the Position of a Particle Given Its Velocity and Initial Position

**Example:** A particle moves along a straight line relative to a fixed origin $O$ with velocity $v(t) = 2t+3t^2$, where $t>0$ is the time. If the particle is at the position $x=1$ when $t=0$, calculate the position $x$ of the particle at time $t$.

**Explanation**

We start by integrating the velocity to get $x(t)$:

$$
\begin{aligned}
x(t) &= ∫v(t)dt \\
&= ∫(2t + 3t^{2})dt \\
&= t^{2} + t^{3} + C
\end{aligned}
$$

To determine $C$, we use the fact that $x(0) = 1$. Substituting this into the above gives

$$
\begin{aligned}
1 &= (0)^{2} + (0)^{3} + C \\
C &= 1
\end{aligned}
$$

Therefore, the position $x$ of the particle at time $t$ is

$$
x(t) = t^3+t^2+1
$$

---

**Question 1**

> A scientific calculator is required to answer this question.

A particle moves along a straight line relative to a fixed origin $O$ with velocity $v(t) = 6t + 6t^{2}$, where $t > 0$ is the time. If the particle is at the position $x = 2$ when $t = 0$, calculate the position $x$ of the particle at time $t$.

- [ ] A. $x(t) = 3t^{2} + 2t^{3}$
- [ ] B. $x(t) = 3t^{2} + 2t^{3} - 2$
- [ ] C. $x(t) = 3t^{2} + 2t^{3} + 1$
- [ ] D. $x(t) = 3t^{2} + 2t^{3} - 1$
- [ ] E. $x(t) = 3t^{2} + 2t^{3} + 2$

---

**Question 2**

> A scientific calculator is required to answer this question.

A particle moves along a straight line relative to a fixed origin $O$ with velocity $v(t) = 9$, where $t$ is the time. If the particle is at the position $x = 0$ when $t = 1$, calculate the position $x$ of the particle at time $t > 0$.

- [ ] A. $x(t) = 9$
- [ ] B. $x(t) = 0$
- [ ] C. $x(t) = 9t + 1$
- [ ] D. $x(t) = 9t - 9$
- [ ] E. $x(t) = 9t$

---

<a id="determining-the-position-of-a-particle-given-its-acceleration-initial-velocity-and-initial-position"></a>
## Determining the Position of a Particle Given Its Acceleration, Initial Velocity and Initial Position

**Example:** A particle moves along a straight line relative to a fixed origin $O$ with acceleration $a(t) = 1-2t$, where $t\geq 0$ is the time. If the particle has position $x=1$ and velocity $v=2$ when $t=1$, calculate the position $x$ of the particle at time $t >0$.

**Explanation**

We start by integrating the acceleration to get the velocity $v(t)$:

$$
\begin{aligned}
v(t) &= ∫a(t)dt \\
&= ∫(1 - 2t)dt \\
&= t - t^{2} + C
\end{aligned}
$$

To determine $C$, we use the fact that $v(1) = 2$. Substituting this into the above gives

$$
\begin{aligned}
2 &= (1) - (1)^{2} + C \\
C &= 2
\end{aligned}
$$

So the velocity is given by

$$
v(t) = t-t^2 + 2
$$

Now, we integrate the velocity to get $x(t)$:

$$
\begin{aligned}
x(t) &= ∫v(t)dt \\
&= ∫(t - t^{2} + 2)dt \\
&= \frac{1}{2}t^{2} - \frac{1}{3}t^{3} + 2t + K
\end{aligned}
$$

To determine $K$, we use the fact that $x(1) = 1$. Substituting this into the above gives

$$
\begin{aligned}
1 &= \frac{1}{2}(1)^{2} - \frac{1}{3}(1)^{3} + 2(1) + K \\
K &= -\frac{7}{6}
\end{aligned}
$$

Therefore, the position $x$ of the particle at time $t$ is

$$
x(t) = \dfrac{1}{2}t^2-\dfrac{1}{3}t^3 +2t -\dfrac{7}{6}
$$

---

**Question 3**

> A scientific calculator is required to answer this question.

A particle moves along a straight line relative to a fixed origin $O$ with acceleration $a(t) = 2e^{2t}$, where $t \ge 0$ is the time. If the particle has position $x = e^{2}$ and velocity $v = e^{2}$ when $t = 1$, calculate the position $x$ of the particle at time $t > 0$.

- [ ] A. $x(t) = 2e^{2t} + e^{2}$
- [ ] B. $x(t) = \frac{1}{2}e^{2t} + te^{2} + e^{2}$
- [ ] C. $x(t) = e^{2t} + te^{2}$
- [ ] D. $x(t) = \frac{1}{2}e^{2t} + \frac{1}{2}e^{2}$
- [ ] E. $x(t) = 2e^{2t} + te^{2} + \frac{1}{2}e^{2}$

---

**Question 4**

> A scientific calculator is required to answer this question.

A particle moves along a straight line relative to a fixed origin $O$ with acceleration $a(t) = t - 2t^{4}$, where $t \ge 0$ is the time. If the particle has position $x = \frac{1}{10}$ and velocity $v = \frac{1}{10}$ when $t = 1$, calculate the position $x$ of the particle at time $t > 0$.

- [ ] A. $x(t) = \frac{1}{3}t^{3} - \frac{1}{12}t^{6}$
- [ ] B. $x(t) = \frac{1}{6}t^{3} - \frac{1}{15}t^{6} + \frac{1}{20}t^{2}$
- [ ] C. $x(t) = \frac{1}{6}t^{3}$
- [ ] D. $x(t) = \frac{1}{6}t^{3} - \frac{1}{15}t^{6}$
- [ ] E. $x(t) = \frac{1}{6}t^{3} - \frac{1}{15}t^{6} + \frac{1}{20}t^{2}$

```update-progress
```

[[MA/Mathematical-Foundations/MF3/Home|Home]]
[[MA/Mathematical-Foundations/MF3/0. Table of Contents/TOC|Table of Contents]]
