# Calculating Distance From a Speed-Time Graph

<!--
lesson-id: 1590
topic-code: MF1.6.2.6
-->

## Table of Contents

- [Introduction](#introduction)
- [Calculating the Area Under a Triangular Speed-Time Graph](#calculating-the-area-under-a-triangular-speed-time-graph)
- [Calculating the Area Under a Trapezoidal Speed-Time Graph](#calculating-the-area-under-a-trapezoidal-speed-time-graph)
- [Solving for Some Missing Information in a Speed-Time Graph](#solving-for-some-missing-information-in-a-speed-time-graph)
- [Constructing a Speed-Time Graph and Calculating the Distance Traveled](#constructing-a-speed-time-graph-and-calculating-the-distance-traveled)

## Prerequisites

- [Areas of Trapezoids](<../../../13. Polygons/13.3. Area and Perimeter/Lessons/13.3.3. Areas of Trapezoids.md>)
- [Speed-Time Graphs](<6.2.5. Speed-Time Graphs.md>)

---

<a id="introduction"></a>
## Introduction

The speed-time graph below represents the motion of a subatomic particle over a period of $50$ seconds. We will use this graph to find the total distance covered by the particle during this period.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/ce7344958cf92b460fd80fb8b4de9417.png>)

In a speed-time graph, the distance covered by an object is equal to the area below the graph and above the $t$-axis. In this case, the required area is a triangle:

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/b83d297bb9cff585f5e5e200ec4894f9.png>)

The area of a triangle with base $b$ and height $h$ is given by

$$
\mathcal{A} = \dfrac{b\cdot h}{2}
$$

In our case,

$$
b=50\,\textrm{s}
$$

and

$$
h=4\,\textrm{cm/s}
$$

Therefore, the area under the graph is

$$
\begin{aligned}
A &= \frac{b \cdot h}{2} \\
&= \frac{50 \cdot 4}{2} \\
&= \frac{200}{2} \\
&= 100
\end{aligned}
$$

This means the subatomic particle covered a total distance of $100 \,\textrm{cm}$.

To understand why the area represents the distance traveled, we can consider the units of each of the variables in the area equation:

- the base $(b)$ of the triangle has units of seconds, and
- the height $(h)$ of the triangle has units of centimeters per second.

If we include these units in our area calculation, they cancel out to give centimeters, which is a unit of distance.

$$
\begin{aligned}
A &= \frac{b \cdot h}{2} \\
&= \frac{1}{2}(50s)(4cm/s) \\
&= \frac{1}{2} \cdot 50 \cdot 4 \cdot s \cdot \frac{cm}{s} \\
&= 25 \cdot 4 \cdot s \cdot \frac{cm}{s} \\
&= 100cm
\end{aligned}
$$

---

<a id="calculating-the-area-under-a-triangular-speed-time-graph"></a>
## Calculating the Area Under a Triangular Speed-Time Graph

**Example:** The speed-time graph shows the motion of an object during the time interval from $t=0$ to $t=9$ hours. What is the total distance covered by the moving object?

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/0570d47b0e9459fca054f043c3545938.png>)

**Explanation**

In a speed-time graph, the distance traveled is equal to the area under the graph.

In this case, the area that we need to calculate is the area of a right triangle.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/e050e32249b0441b72e44a49d9e79376.png>)

The area of a triangle is given by the formula

$$
A = \dfrac{bh}{2}
$$

where $b$ is a base and $h$ is a corresponding height.

In this case, we have the following:

- The base of the triangle is $b=9$.
- The height of the triangle is $h=80$.

We substitute these values into the area formula and compute:

$$
\begin{aligned}
A &= \frac{80 \cdot 9}{2} \\
&= \frac{720}{2} \\
&= 360
\end{aligned}
$$

So, the distance covered by the object is $360\,\textrm{km}$.

---

**Question 1**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-59768.png>)

The speed-time graph shows the motion of an object during the time interval from $t = 0$ to $t = 8$ hours. What is the total distance covered by the moving object?

- [ ] A. $270km$
- [ ] B. $540km$
- [ ] C. $560km$
- [ ] D. $290km$
- [ ] E. $280km$

---

**Question 2**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-237038.png>)

The speed-time graph represents the motion of an object during a time interval of $9$ seconds.The total distance covered by the object is
$\underline{\hspace{1.5cm}}$
$ft$.

---

<a id="calculating-the-area-under-a-trapezoidal-speed-time-graph"></a>
## Calculating the Area Under a Trapezoidal Speed-Time Graph

**Example:** The speed-time graph below represents the motion of an object during the time interval from $t=0$ to $t=80$ seconds. What is the total distance covered by the moving object?

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/e1c947c5b2d235ba6ec9fe20a07126a0.png>)

**Explanation**

In a speed-time graph, the distance traveled is equal to the area under the graph.

In this case, the area that we need to calculate is the area of a trapezoid.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/c78a43e737ae66608c98cd7ed1168c21.png>)

The area of a trapezoid is given by the formula

$$
A = \dfrac{(a+b)h}{2}
$$

where $a$ and $b$ are the bases, and $h$ is the height.

In this case, we have the following:

- The bottom base of the trapezoid is $a=80$.
- The top base of the trapezoid is $b=60-20=40$.
- The height of the trapezoid is $h=8$.

We substitute these values into the area formula and compute:

$$
\begin{aligned}
A &= ((80 + 40) \cdot 8)/(2) \\
&= \frac{120 \cdot 8}{2} \\
&= 480
\end{aligned}
$$

So, the distance covered by the object is $480$ meters.

---

**Question 3**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-208838.png>)

The speed-time graph represents the motion of a car over a time interval of $5$ hours.The total distance covered by the car is
$\underline{\hspace{1.5cm}}$
$km$.

---

**Question 4**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-26501.png>)

The speed-time graph shows the motion of an object during the time interval from $t = 0$ to $t = 80$ seconds. What is the total distance covered by the moving object?

- [ ] A. $300m$
- [ ] B. $60m$
- [ ] C. $180m$
- [ ] D. $240m$
- [ ] E. $210m$

---

**Question 5**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-237063.png>)

The speed-time graph represents the motion of an arrow over a time interval of $3$ seconds.The total distance covered by the arrow is
$\underline{\hspace{1.5cm}}$
$m$.

---

<a id="solving-for-some-missing-information-in-a-speed-time-graph"></a>
## Solving for Some Missing Information in a Speed-Time Graph

**Example:** A car starts to decelerate from an initial speed of $10\,\textrm{m/s}$ until it comes to rest. The speed-time graph illustrates the motion of the car. If the total distance covered by the car was $80$ meters, how long did it take for the car to stop?

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/c72cd346c2e22f8c5f0398185ddd877c.png>)

**Explanation**

In a speed-time graph, the distance traveled is equal to the area under the graph.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/f1cec8c52b1cd479a2e72daf4f76ae24.png>)

The base of the triangle corresponds to the time it took for the car to stop. We do not know this quantity, so let's call it $x$.

The area of a triangle is given by the formula

$$
A = \dfrac{bh}{2}
$$

where $b$ is a base and $h$ is a corresponding height.

In this case, we have the following:

- The base of the triangle is $b=x$.
- The height of the triangle is $h=10$.

We substitute these values into the area formula and compute:

$$
\begin{aligned}
A &= \frac{1}{2}bh \\
&= \frac{1}{2} \cdot x \cdot 10 \\
&= 5x
\end{aligned}
$$

The distance traveled is $80$ meters and must be equal to the area of the shaded triangle. Therefore, we can solve for $x$, as follows:

$$
\begin{aligned}
80 &= 5x \\
\frac{80}{5} &= x \\
16 &= x
\end{aligned}
$$

Therefore, it took $16 \,\textrm{s}$ for the car to stop.

---

**Question 6**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-59772.png>)

A car starts to decelerate from an initial speed of $8m/s$ until it comes to rest. The speed-time graph illustrates the motion of the car. If the car covered a total distance of $20m$ during this period, how long did it take for the car to stop?

- [ ] A. $10s$
- [ ] B. $2s$
- [ ] C. $4s$
- [ ] D. $5s$
- [ ] E. $2.5s$

---

**Question 7**

> A calculator is required to answer this question.

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/q-237117.png>)

A train began to decelerate and came to rest after $3$ minutes. The speed-time graph above illustrates the motion of the train. If the total distance covered while decelerating was $6km$, what was the initial speed of the train?The initial speed of the train was
$\underline{\hspace{1.5cm}}$ $km/\min$.

---

<a id="constructing-a-speed-time-graph-and-calculating-the-distance-traveled"></a>
## Constructing a Speed-Time Graph and Calculating the Distance Traveled

**Example:** An F1 racing car moves with constant acceleration during its first $5$ seconds of travel, changing its speed from $0\,\textrm{m/s}$ to $60\,\textrm{m/s}$. Then, the car applies the brakes, decelerating at a constant rate before it comes to a stop $35$ seconds later. Calculate the total distance covered by the car.

**Explanation**

The distance covered by the car is the area below its speed-time graph. So, we first need to make a speed-time graph that illustrates the described situation.

- The graph starts at $(0,0)$, since the car starts at a speed of $0\,\textrm{m/s}$.
- After $5$ seconds, the speed of the car is $60 \textrm{m/s}$. This corresponds to the point $(5,60)$.
- After another $35$ seconds, the car stops. So, at $t=5+35=40$ seconds, the speed is $0 \textrm{m/s}$. This corresponds to the point $(40,0)$.

Connecting the points with line segments and shading the relevant area, we obtain the following graph:

![](<../Source/Calculating Distance From a Speed-Time Graph - 1590/Images/b20b48ccb8272e3f533be82cc1796c87.png>)

In this case, the area that we need to calculate is the area of a triangle.

The area of a triangle is given by the formula

$$
A = \dfrac{bh}{2}
$$

where $b$ is a base and $h$ is a corresponding height.

In this case, we have the following:

- The base of the triangle is $b=40$.
- The height of the triangle is $h=60$.

We substitute these values into the area formula and compute:

$$
\begin{aligned}
A &= \frac{bh}{2} \\
&= \frac{40 \cdot 60}{2} \\
&= \frac{2400}{2} \\
&= 1200
\end{aligned}
$$

So, the distance covered by the car is $1\,200$ meters.

---

**Question 8**

> A calculator is required to answer this question.

A motorcycle starts from rest and accelerates with a constant acceleration of $3m/s^{2}$. The total distance covered by the motorcycle in the first $6$ seconds is $\underline{\hspace{1.5cm}}$ $m$.

---

**Question 9**

> A calculator is required to answer this question.

A car moves with constant acceleration for $10$ seconds, changing its speed from $0m/s$ to $40m/s$. Then, the car moves with constant deceleration, stopping after a further $5$ seconds. Calculate the entire distance covered by the car.

- [ ] A. $550m$
- [ ] B. $300m$
- [ ] C. $400m$
- [ ] D. $600m$
- [ ] E. $800m$

---

**Question 10**

> A calculator is required to answer this question.

A racing car decelerates steadily from $180mph$ to $60mph$, covering a distance of $880ft$. For how long was the car decelerating?

*Hint: You may use the fact that $1mi = 5280ft$ and $1h = 3600s$.*

The car was decelerating for
$\underline{\hspace{1.5cm}}$ $s$.

```update-progress
```

[[MA/MF1/Home|Home]]
[[MA/MF1/0. Table of Contents/TOC|Table of Contents]]
