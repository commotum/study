# Calculating the Total Distance Traveled by a Particle

<!--
lesson-id: 636
topic-code: CA2.2.5.5
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Total Distance Traveled by a Particle](#calculating-the-total-distance-traveled-by-a-particle)
- [Calculating the Total Distance Traveled by a Particle When It Changes Direction](#calculating-the-total-distance-traveled-by-a-particle-when-it-changes-direction)
- [Finding an Expression For the Total Distance Traveled By a Particle](#finding-an-expression-for-the-total-distance-traveled-by-a-particle)
- [Calculating the Time It Takes a Particle to Travel a Given Distance](#calculating-the-time-it-takes-a-particle-to-travel-a-given-distance)

## Prerequisites

- [Finding the Area Between a Curve and the X-Axis When They Intersect](<../../../../MA/Mathematical-Foundations/MF3/9. Definite Integrals/9.3. The Area Under a Curve/Lessons/9.3.4. Finding the Area Between a Curve and the X-Axis When They Intersect.md>)
- [Calculating the Displacement of a Particle Using Integration](<../../../../MA/Mathematical-Foundations/MF3/11. Contextual Applications of Calculus/11.1. Displacement, Velocity, and Acceleration/Lessons/11.1.7. Calculating the Displacement of a Particle Using Integration.md>)

---

<a id="introduction"></a>
## Introduction

The **total distance** $d$ traveled by a particle over the time interval $[t_1,t_2]$ is given by

$$
d = \int_{t_1}^{t_2} \mid v(t) \mid \,\textrm d t
$$

In other words, we integrate the speed of the particle over the relevant time interval.

**Watch out!** We need to integrate the speed $\mid v(t) \mid$, not just the velocity $v(t)$. Integrating the velocity gives us displacement, which is not the same as distance.

For example, if you take a step forward and then a step backward, your total distance traveled is $2$ steps, while your displacement is $0$ steps.

---

<a id="calculating-the-total-distance-traveled-by-a-particle"></a>
## Calculating the Total Distance Traveled by a Particle

**Example:** A particle $P$ moves along a straight line relative to a fixed origin $O$. Its velocity $v\,\textrm{m/s}$ is given by $v(t) =3t^2-2t$, where $t$ is the time in seconds. Calculate the total distance traveled by $P$ in the interval $\dfrac{2}{3}\leq t\leq 1$.

**Explanation**

To find the total distance traveled, we first need to find the points where the particle changes its direction, which can only occur when the velocity is zero. Solving $v(t) = 0$, we get

$$
\begin{aligned} v(t) &= 0 \\ 3t^2 - 2t&= 0 \\ t(3t -2) & = 0 \\ t & =0, \dfrac{2}{3}. \end{aligned}
$$

The graph of the velocity $v(t)$ is given below:

![](<../Source/Calculating the Total Distance Traveled by a Particle - 636/Images/e20372269fde052019afad9992ab801e.png>)

Notice that in the interval

$$
\dfrac{2}{3} \leq t\leq 1
$$

the graph of $v(t)$ doesn't cross the $t$-axis. Therefore, we don't need to split up the distance integral.

In the interval

$$
\dfrac{2}{3} \leq t\leq 1
$$

we have

$$
v(t)\geq 0
$$

Therefore,

$$
\mid v(t) \mid = v(t) = 3t^2-2t
$$

We can now calculate the total distance traveled, as follows:

$$
\begin{aligned} d&=\int_{2/3}^1 \begin{vmatrix}v(t) & \, dt \\[5pt] &=\int_{2/3}^{1} \left(3t^2-2t \right)\,\textrm{d}t \\[5pt] &=\Big.\left(t^3-t^2 \right)\Big\end{vmatrix}_{2/3}^{1} \\[5pt] &=\left(1^3-1^2 \right)-\left(\left(\dfrac{2}{3}\right)^3-\left(\dfrac{2}{3}\right)^2\right) \\[5pt] &=\dfrac{4}{9}-\dfrac{8}{27} \\[5pt] &=\dfrac{4}{27} \end{aligned}
$$

Therefore, the particle travels a total distance of

$$
\dfrac{4}{27}\,\textrm m
$$

in the time interval

$$
\dfrac{2}{3}\leq t\leq 1
$$

---

**Question 1**

```quiz
type: radio
id: ma-19928
content: |-
  > A scientific calculator is required to answer this question.

  A particle $P$ moves along a straight line relative to a fixed origin $O$. Its displacement $scm$ is given by
  $s(t) =-\frac{1}{3}t^{3} + \frac{5}{2}t^{2} + 6t - 2$,
  where $t$ is the time, in seconds. Calculate the total distance traveled by $P$ in the interval $0 \le t \le 6$.
options:
- id: a
  content: |-
    $52cm$
- id: b
  content: |-
    $2cm$
- id: c
  content: |-
    $54cm$
  correct: true
- id: d
  content: |-
    $27cm$
- id: e
  content: |-
    $50cm$
```

---

**Question 2**

```quiz
type: radio
id: ma-19934
content: |-
  > A scientific calculator is required to answer this question.

  A particle $P$ moves along a straight line relative to a fixed origin $O$. Its velocity $vm/s$ is given by $v(t) =-t^{2} + 8t - 7$, where $t$ is the time in seconds. Calculate the total distance traveled by $P$ in the interval $2 \le t \le 6$.
options:
- id: a
  content: |-
    $30m$
- id: b
  content: |-
    $\frac{2}{3}m$
- id: c
  content: |-
    $\frac{92}{3}m$
  correct: true
- id: d
  content: |-
    $\frac{88}{3}m$
- id: e
  content: |-
    $15m$
```

---

<a id="calculating-the-total-distance-traveled-by-a-particle-when-it-changes-direction"></a>
## Calculating the Total Distance Traveled by a Particle When It Changes Direction

**Example:** A particle $P$ moves along a straight line relative to a fixed origin $O$. Its displacement $s\,\textrm{cm}$ is given by

$s(t) =2t^3-6t^2+4$,
where $t$ is the time, in seconds. Calculate the total distance traveled by $P$ in the interval $0\leq t\leq 4$.

**Explanation**

The displacement $s(t)$ is given by

$$
s(t) =2t^3-6t^2+4
$$

The velocity $v(t)$ is obtained by differentiating $s(t)$. This gives

$$
\begin{aligned} v(t)&=\dfrac{\textrm{d}s}{\textrm{d}t}=6t^2-12t. \end{aligned}
$$

To find the total distance traveled, we need to find the points where the velocity changes direction. This occurs when the velocity is zero. Solving $v(t) = 0$, we get

$$
\begin{aligned} 6t^2-12t &= 0 \\ 6t(t -2) & = 0 \\ t & =0,2. \end{aligned}
$$

A sketch of $v(t)$ is shown below:

![](<../Source/Calculating the Total Distance Traveled by a Particle - 636/Images/12afae1ccf84d653c53e73981d061bd4.png>)

Notice that in the interval

$$
0\leq t\leq 4
$$

the curve $v(t)$ crosses the $t$-axis at $t=2$. Therefore, total distance traveled $d$ is given by

$$
d = \left\begin{vmatrix}s(2) - s(0) & + & s(4) - s(2)\right\end{vmatrix}
$$

We calculate the total distance traveled as follows:

$$
\begin{aligned}
d &= \begin{vmatrix}(2(2)^{3} - 6(2)^{2} + 4) - (4) & + & (2(4)^{3} - 6(4)^{2} + 4) - (2(2)^{3} - 6(2)^{2} + 4)\end{vmatrix} \\
&= 8 + 40 \\
&= 48m
\end{aligned}
$$

Therefore, the total distance traveled by $P$ in the interval

$$
0 \leq t\leq 4
$$

is $48\,\textrm{m}$.

---

**Question 3**

```quiz
type: radio
id: ma-19495
content: |-
  > A scientific calculator is required to answer this question.

  A particle $P$ moves along a straight line relative to a fixed origin $O$. Its velocity $vm/s$ is given by $v(t) = 2t - t^{2}$, where $t$ is the time in seconds. Find the total distance traveled by $P$ in the interval $1 \le t \le 3$.
options:
- id: a
  content: |-
    $1m$
- id: b
  content: |-
    $2m$
  correct: true
- id: c
  content: |-
    $\frac{2}{3}m$
- id: d
  content: |-
    $4m$
- id: e
  content: |-
    $\frac{4}{3}m$
```

---

**Question 4**

```quiz
type: radio
id: ma-19929
content: |-
  > A scientific calculator is required to answer this question.

  A particle $P$ moves along a straight line relative to a fixed origin $O$. Its displacement $sm$ is given by

  $s(t) =-t^{2} + 6t - 3$,
  where $t$ is the time, in seconds. Calculate the total distance traveled by $P$ in the interval $0 \le t \le 4$.
options:
- id: a
  content: |-
    $3m$
- id: b
  content: |-
    $9m$
- id: c
  content: |-
    $10m$
  correct: true
- id: d
  content: |-
    $6m$
- id: e
  content: |-
    $8m$
```

---

<a id="finding-an-expression-for-the-total-distance-traveled-by-a-particle"></a>
## Finding an Expression For the Total Distance Traveled By a Particle

**Example:** The velocity of a particle, in meters per second, is given by $v(t) = \dfrac{1}{2}t - 1$, where $t>0$ is the time in seconds. Find an expression for the total distance traveled by the particle between $t = 0$ and $t=T$ where $T > 2$.

**Explanation**

To find the total distance traveled, we first need to find the points where the particle changes its direction, which can only occur when the velocity is zero. Solving $v(t) = 0$, we get

$$
\begin{aligned}
v(t) &= 0 \\
\frac{1}{2}t - 1 &= 0 \\
\frac{1}{2}t &= 1 \\
t &= 2
\end{aligned}
$$

A sketch of $v(t)$ is shown below:

![](<../Source/Calculating the Total Distance Traveled by a Particle - 636/Images/0489c64bccb52ed9728b8d0ac517da4e.png>)

Notice that in the interval

$$
0\leq t\leq T
$$

for $T > 2$, the curve $v(t)$ crosses the $t$-axis at $t=2$. Therefore, we need to split up the distance integral between the intervals

$$
0\leq t\leq 2
$$

and

$$
2\leq t\leq T
$$

In the interval

$$
0 \leq t\leq 2
$$

we have $v(t) \lt 0$. Therefore,

$$
\mid v(t) \mid = -v(t) = 1 - \dfrac{1}{2}t
$$

Similarly, in the interval

$$
2 \leq t \leq T
$$

we have $v(t) \gt 0$. Therefore,

$$
\mid v(t) \mid = v(t) = \dfrac{1}{2}t - 1
$$

Finally, splitting the integral over the two intervals, we can find an expression for the total distance traveled, as follows:

$$
\begin{aligned}
d &= ∫_{0}^{T}\begin{vmatrix}v(t) & dt \\ = ∫_{0}^{2} & v(t)\end{vmatrix}dt + ∫_{2}^{T} \mid v(t)\begin{vmatrix}dt \\ = ∫_{0}^{2}(1 - \frac{1}{2}t)dt + ∫_{2}^{T}(\frac{1}{2}t - 1)dt \\ = (t - \frac{1}{4}t^{2})\end{vmatrix}_{0}^{2} + (\frac{1}{4}t^{2} - t) \mid _{2}^{T} \\
&= [(2 - \frac{1}{4}(2)^{2}) - 0] + [(\frac{1}{4}T^{2} - T) - (\frac{1}{4}(2)^{2} - 2)] \\
&= 1 + \frac{1}{4}T^{2} - T - (-1) \\
&= \frac{1}{4}T^{2} - T + 2
\end{aligned}
$$

---

**Question 5**

```quiz
type: radio
id: ma-50112
content: |-
  > A scientific calculator is required to answer this question.

  The velocity of a particle, in meters per second, is given by $v(t) = 6t^{2} - 6t$, where $t > 0$ is the time in seconds. Find an expression for the total distance traveled by the particle between $t = 0$ and $t = T$ where $T > 1$.
options:
- id: a
  content: |-
    $2T^{3} - 3T^{2} + 2$
  correct: true
- id: b
  content: |-
    $2T^{3} - 3T^{2} + 1$
- id: c
  content: |-
    $2T^{3} - 3T^{2}$
- id: d
  content: |-
    $2T^{3} - 3T^{2} + 10$
- id: e
  content: |-
    $2T^{3} - 3T^{2} - 2$
```

---

**Question 6**

```quiz
type: radio
id: ma-50096
content: |-
  > A scientific calculator is required to answer this question.

  The velocity of a particle, in meters per second, is given by $v(t) = 2 - \frac{1}{2}t$, where $t > 0$ is the time in seconds. Find an expression for the total distance traveled by the particle between $t = 0$ and $t = T$ where $T > 4$.
options:
- id: a
  content: |-
    $\frac{1}{8}T^{2} - 2T + 8$
- id: b
  content: |-
    $\frac{1}{4}T^{2} - 2T + 8$
  correct: true
- id: c
  content: |-
    $\frac{1}{8}T^{2} - 2T$
- id: d
  content: |-
    $\frac{1}{2}T^{2} - 2T$
- id: e
  content: |-
    $\frac{1}{4}T^{2} - 2T$
```

---

<a id="calculating-the-time-it-takes-a-particle-to-travel-a-given-distance"></a>
## Calculating the Time It Takes a Particle to Travel a Given Distance

**Example:** The velocity of a particle, in meters per second, is given by $v(t) = 12-3t^2$, where $t>0$ is the time in seconds. Calculate the time taken for the particle to travel $32\,\textrm m$.

**Explanation**

To find the total distance traveled, we first need to find the points where the particle changes its direction, which can only occur when the velocity is zero. Solving $v(t) = 0$, we get

$$
\begin{aligned}
12 - 3t^{2} &= 0 \\
- 3(t^{2} - 4) &= 0 \\
t &= ± 2
\end{aligned}
$$

A sketch of $v(t)$ is shown below:

![](<../Source/Calculating the Total Distance Traveled by a Particle - 636/Images/e460276e1a3e82fa9ffe1ab1ef39bf83.png>)

Notice that in the interval

$$
0\leq t\leq T
$$

for $T > 2$, the curve $v(t)$ crosses the $t$-axis at $t=2$. Therefore, we need to split up the distance integral between the intervals

$$
0\leq t\leq 2
$$

and

$$
2\leq t\leq T
$$

In the interval

$$
0\leq t\leq 2
$$

we have $v(t) > 0$. Therefore,

$$
\mid v(t) \mid = v(t) =12-3t^2
$$

We can work out the total distance traveled in the interval $0 < t < 2$ as follows:

$$
\begin{aligned}
d &= ∫_{0}^{2} \mid v(t)\begin{vmatrix}dt \\ = ∫_{0}^{2}(12 - 3t^{2})dt \\ = (12t - t^{3})\end{vmatrix}_{0}^{2} \\
&= 12(2) - 2^{3} \\
&= 16
\end{aligned}
$$

Since $16 < 32$, the time taken for the particle to travel $32\,\textrm{m}$ is greater than $2$ seconds.

Now, in the interval

$$
2\leq t\leq T
$$

for $T>2$, we have $v(t)<0$. Therefore,

$$
\mid v(t) \mid =-v(t) = 3t^2-12
$$

Therefore, an expression for the total distance $d$ traveled between $t=0$ and $t=T$ for $T >2$ is given by

$$
\begin{aligned}
d(T) &= ∫_{0}^{T}\begin{vmatrix}v(t) & dt \\ = ∫_{0}^{2} & v(t)\end{vmatrix}dt_(⏟)_(16) + ∫_{2}^{T} \mid v(t)\begin{vmatrix}dt \\ = 16 + ∫_{2}^{T}(3t^{2} - 12)dt \\ = 16 + (t^{3} - 12t)\end{vmatrix}_{2}^{T} \\
&= 16 + [(T^{3} - 12T) - ((2)^{3} - 12(2)] \\
&= 16 + T^{3} - 12T - (-16) \\
&= T^{3} - 12T + 32
\end{aligned}
$$

Finally, the particle travels $32\,\textrm{m}$ when $d = 32$. So, we can solve for $T$ as follows:

$$
\begin{aligned}
T^{3} - 12T + 32 &= 32 \\
T^{3} - 12T &= 0 \\
T(T^{2} - 12) &= 0
\end{aligned}
$$

The solutions are $T=0$ and

$$
T=\pm 2\sqrt 3
$$

Since we require $T> 2$, the only valid solution is

$$
T=2\sqrt 3
$$

Therefore, we conclude that it takes $2\sqrt 3$ seconds for the particle to travel a total of $32\,\textrm{m}$.

---

**Question 7**

```quiz
type: radio
id: ma-83139
content: |-
  > A scientific calculator is required to answer this question.

  The velocity of a particle, in centimeters per second, is given by $v(t) = 2t - 6$, where $t > 0$ is the time in seconds. Calculate the time taken for the particle to travel $13cm$.
options:
- id: a
  content: |-
    $3$ seconds
- id: b
  content: |-
    $4$ seconds
- id: c
  content: |-
    $7$ seconds
- id: d
  content: |-
    $5$ seconds
  correct: true
- id: e
  content: |-
    $6$ seconds
```

---

**Question 8**

```quiz
type: radio
id: ma-49924
content: |-
  > A scientific calculator is required to answer this question.

  The velocity of a particle, in meters per second, is given by $v(t) = 3t^{2} - 6t$, where $t > 0$ is the time in seconds. Calculate the time taken for the particle to travel $8m$.
options:
- id: a
  content: |-
    $6$ seconds
- id: b
  content: |-
    $3$ seconds
  correct: true
- id: c
  content: |-
    $5$ seconds
- id: d
  content: |-
    $2$ seconds
- id: e
  content: |-
    $4$ seconds
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
