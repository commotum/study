# Calculating the Displacement of a Particle Using Integration

<!--
lesson-id: 3576
topic-code: MF3.11.1.7
-->

## Table of Contents

- [Introduction](#introduction)
- [Finding the Total Displacement of a Particle Given Its Velocity](#finding-the-total-displacement-of-a-particle-given-its-velocity)
- [Finding the Final Position of a Particle](#finding-the-final-position-of-a-particle)
- [Finding the Final Position of a Particle Given a Velocity-Time Graph](#finding-the-final-position-of-a-particle-given-a-velocity-time-graph)

## Prerequisites

- [The Integral as an Accumulation Function](<../../../9. Definite Integrals/9.4. Accumulation Functions/Lessons/9.4.1. The Integral as an Accumulation Function.md>)
- [Calculating the Position Function of a Particle Using Integration](<11.1.6. Calculating the Position Function of a Particle Using Integration.md>)

---

<a id="introduction"></a>
## Introduction

The **total displacement** $d$ of a particle over the time interval $t \in [a,b]$ is the difference in the position of the particle between $t=a$ and $t=b$.

$$
d = x(b) - x(a)
$$

Now, the fundamental theorem of calculus states that

$$
d = x(b) - x(a) = \int_a^b x'(t) \, \textrm dt
$$

and since

$$
x'(t) = v(t)
$$

we can find the total displacement of a particle by integrating the velocity:

$$
d = x(b) - x(a) = \int_a^b v(t) \, \textrm dt
$$

To summarize, the total displacement of a particle over the time interval $t \in [a,b]$ can be found by integrating the velocity $v(t)$ over the time interval $t\in[a,b]$.

$$
\begin{aligned}
d &= ∫_{a}^{b}v(t)dt
\end{aligned}
$$

---

<a id="finding-the-total-displacement-of-a-particle-given-its-velocity"></a>
## Finding the Total Displacement of a Particle Given Its Velocity

**Example:** A particle $P$ moves along the $x$-axis and its velocity at time $t$ is given by $v(t) = 2t + 3t^2$. What is the total displacement of the particle between $t=1$ and $t=3$?

**Explanation**

We find the total displacement by calculating the definite integral of the velocity.

Let $d$ be the total displacement. Then, we have

$$
\begin{aligned}
d &= ∫_{1}^{3}(2t + 3t^{2})dt \\
&= (t^{2} + t^{3}) \mid _{1}^{3} \\
&= [3^{2} + 3^{3}] - [1^{2} + 1^{3}] \\
&= [9 + 27] - [1 + 1] \\
&= 36 - 2 \\
&= 34
\end{aligned}
$$

So the total displacement between $t=1$ and $t=3$ is $34$.

---

**Question 1**

> A scientific calculator is required to answer this question.

A particle $P$ moves along the $x$-axis and its velocity at time $t$ is given by $v(t) = 6t^{2} - 2t$. What is the total displacement of the particle between $t = 1$ and $t = 4$?

- [ ] A. $88$
- [ ] B. $92$
- [ ] C. $148$
- [ ] D. $111$
- [ ] E. $4$

---

**Question 2**

> A scientific calculator is required to answer this question.

A particle $P$ moves along the $x$-axis and its velocity at time $t$ is given by $v(t) = 12t^{2} - 4t$. What is the total displacement of the particle between $t = 0$ and $t = 3$?

- [ ] A. $96$
- [ ] B. $68$
- [ ] C. $0$
- [ ] D. $72$
- [ ] E. $90$

---

<a id="finding-the-final-position-of-a-particle"></a>
## Finding the Final Position of a Particle

**Example:** A particle $P$ moves along the $x$-axis and its velocity at time $t>0$ is given by $v(t) = 6t^2 +4t$. At time $t=2$ the particle is located at the position $x=-20$. What is the position of the particle at time $t=4$?

**Explanation**

The position of the particle at $t=4$ is equal to its position at $t=2$ plus the total displacement over $t\in[2,4]$. Therefore, we can calculate it as follows:

$$
x(4) = x(2) + \int_2^4 v(t)\,\textrm{d}t
$$

Carrying out the computations, we get

$$
\begin{aligned}
x(4) &= -20 + ∫_{2}^{4}(6t^{2} + 4t)dt \\
&=-20 + [2t^{3} + 2t^{2}]_{2}^{4} \\
&=-20 + ([2(4)^{3} + 2(4)^{2}] - [2(2)^{3} + 2(2)^{2}]) \\
&=-20 + ([128 + 32] - [16 + 8]) \\
&=-20 + (160 - 24) \\
&=-20 + 136 \\
&= 116
\end{aligned}
$$

So the position of the particle at $t=4$ is $x=116$.

---

**Question 3**

> A scientific calculator is required to answer this question.

A particle $P$ moves along the $x$-axis and its velocity at time $t \ge 0$ is given by $v(t) = e^{t/3} - 1$. At time $t = 0$ the particle is located at the position $x = e + 1$. What is the position of the particle at time $t = 3$?

- [ ] A. $x = 3e - 1$
- [ ] B. $x = e - 1$
- [ ] C. $x = 4e - 5$
- [ ] D. $x = 3e^{3} - e$
- [ ] E. $x = 4e^{3}$

---

**Question 4**

> A scientific calculator is required to answer this question.

A particle $P$ moves along the $x$-axis and its velocity at time $t > 0$ is given by $v(t) = 4t + 3t^{2}$. At time $t = 1$ the particle is located at the position $x = 12$. What is the position of the particle at time $t = 4$?

- [ ] A. $92$
- [ ] B. $100$
- [ ] C. $97$
- [ ] D. $93$
- [ ] E. $105$

---

<a id="finding-the-final-position-of-a-particle-given-a-velocity-time-graph"></a>
## Finding the Final Position of a Particle Given a Velocity-Time Graph

**Example:** The graph above shows the velocity of an object moving in a straight line along the $x$-axis. At time $t=2$ the particle is located at the position $x=-1$. What is the position of the particle at time $t=8$?

![](<../Source/Calculating the Displacement of a Particle Using Integration - 3576/Images/1e5634171531dd04f9da7173af00e15c.png>)

**Explanation**

The position of the particle at $t = 8$ is equal to its position at $t=2$ plus the total displacement over $t\in [2,8]$. Therefore, we can calculate it as follows:

$$
x(8) = x(2)+ \int_2^8 v(t) \, \textrm d t
$$

We are told that $x(2)=-1$, and we can compute the integral $\displaystyle\int_2^8 v(t) \, \textrm dt$ by finding the signed area under the graph from $t=2$ to $t=8$. Computing the signed area, we get

$$
\int_2^8 v(t) \, \textrm dt = 6
$$

Therefore,

$$
x(8) = -1+ 6 = 5
$$

So the position of the particle at $t=8$ is $x=5$.

---

**Question 5**

![](<../Source/Calculating the Displacement of a Particle Using Integration - 3576/Images/q-81515.png>)

The graph above shows the velocity of an object moving in a straight line along the $x$-axis. At time $t = 1$ the particle is located at the position $x = 2$. What is the position of the particle at time $t = 7$?

- [ ] A. $2$
- [ ] B. $7$
- [ ] C. $4$
- [ ] D. $6$
- [ ] E. $8$

---

**Question 6**

![](<../Source/Calculating the Displacement of a Particle Using Integration - 3576/Images/q-49319.png>)

The graph above shows the velocity of an object moving in a straight line along the $x$-axis. At time $t = 0$ the particle is located at the position $x = 6$. What is the position of the particle at time $t = 3$?

- [ ] A. $12$
- [ ] B. $8$
- [ ] C. $14$
- [ ] D. $11$
- [ ] E. $20$

```update-progress
```

[[MA/MF3/Home|Home]]
[[MA/MF3/0. Table of Contents/TOC|Table of Contents]]
