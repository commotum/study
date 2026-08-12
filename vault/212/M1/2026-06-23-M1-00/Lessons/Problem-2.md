# Angular Displacement Before Reversal

<!--
lesson-id: 212-M1-032
topic-code: MTH212.M1.32
-->

## Table of Contents

- [Introduction](#introduction)
- [Find the Reversal Time](#find-the-reversal-time)
- [Set Up the Angle Integral](#set-up-the-angle-integral)
- [Evaluate the Polynomial Integral](#evaluate-the-polynomial-integral)
- [Combine the Steps](#combine-the-steps)

## Prerequisites

- Solve an equation of the form $A-Bt^2=0$ for the positive time.
- Interpret angular displacement as the integral of angular velocity.
- Use the power rule antiderivative $\int t^2\,dt=\frac{t^3}{3}$.

---

<a id="introduction"></a>
## Introduction

When angular velocity is given as a function of time, the angle turned over a time interval is the signed area under the angular velocity graph:

$$
\Delta\theta=\int_{t_0}^{t_1}\omega(t)\,dt.
$$

The cue in this problem is the phrase "between $t_0=0.0\ \mathrm{s}$ and the time at which it reverses its direction." The upper endpoint is not given directly. First find the time when $\omega(t)=0$, then integrate $\omega(t)$ from $0$ to that positive time.

For

$$
\omega(t)=A-Bt^2,
$$

with $A>0$ and $B>0$, the reversal time satisfies

$$
A-Bt^2=0.
$$

Once the reversal time $t_{\mathrm{rev}}$ is known, use

$$
\Delta\theta=\int_0^{t_{\mathrm{rev}}}(A-Bt^2)\,dt
=\left[At-\frac{Bt^3}{3}\right]_0^{t_{\mathrm{rev}}}.
$$

---

<a id="find-the-reversal-time"></a>
## Find the Reversal Time

**Example:** A disk has angular velocity $\omega(t)=20-5t^2$. Find the positive time when it reverses direction.

**Explanation**

The disk reverses direction when its angular velocity is zero:

$$
\begin{aligned}
20-5t^2 &= 0 \\
5t^2 &= 20 \\
t^2 &= 4 \\
t &= 2.
\end{aligned}
$$

The equation also has the solution $t=-2$, but the interval starts at $t=0$, so the relevant reversal time is $t=2$.

```quiz
type: radio
id: p2-q1
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=27-3t^2$. What is the positive time when it reverses direction?
options:
- id: p2q1-a
  content: |-
    $t=3$
  correct: true
- id: p2q1-b
  content: |-
    $t=9$
- id: p2q1-c
  content: |-
    $t=\sqrt{27}$
- id: p2q1-d
  content: |-
    $t=24$
- id: p2q1-e
  content: |-
    $t=-3$
```

---

<a id="set-up-the-angle-integral"></a>
## Set Up the Angle Integral

**Example:** A disk has angular velocity $\omega(t)=16-4t^2$ and starts at $t=0$. Set up the integral for the angle it turns before reversing direction.

**Explanation**

First find the reversal time:

$$
\begin{aligned}
16-4t^2 &= 0 \\
4t^2 &= 16 \\
t^2 &= 4 \\
t &= 2.
\end{aligned}
$$

Angular displacement comes from integrating angular velocity. Since the interval is from $0$ to $2$, the angle turned is

$$
\Delta\theta=\int_0^2 (16-4t^2)\,dt.
$$

This setup uses the whole velocity function. Do not use the initial angular velocity times the time, and do not use the final angular velocity times the time.

```quiz
type: radio
id: p2-q2
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=12-3t^2$ and starts at $t=0$. Which integral gives the angle it turns before reversing direction?
options:
- id: p2q2-a
  content: |-
    $\displaystyle \int_0^2 (12-3t^2)\,dt$
  correct: true
- id: p2q2-b
  content: |-
    $\displaystyle \int_0^2 12\,dt$
- id: p2q2-c
  content: |-
    $\displaystyle \int_0^4 (12-3t^2)\,dt$
- id: p2q2-d
  content: |-
    $\displaystyle \int_0^2 (3t^2-12)\,dt$
- id: p2q2-e
  content: |-
    $2(12-3(2)^2)$
```

---

<a id="evaluate-the-polynomial-integral"></a>
## Evaluate the Polynomial Integral

**Example:** Evaluate the angular displacement

$$
\int_0^3 (15-t^2)\,dt.
$$

**Explanation**

Use the power rule on each term:

$$
\begin{aligned}
\int_0^3 (15-t^2)\,dt
&=\left[15t-\frac{t^3}{3}\right]_0^3 \\
&=\left(15(3)-\frac{3^3}{3}\right)-0 \\
&=45-9 \\
&=36.
\end{aligned}
$$

So the disk turns through $36$ radians over that interval.

```quiz
type: radio
id: p2-q3
shuffle: true
content: |-
  Evaluate $\displaystyle \int_0^2 (12-3t^2)\,dt$.
options:
- id: p2q3-a
  content: |-
    $8$
- id: p2q3-b
  content: |-
    $16$
  correct: true
- id: p2q3-c
  content: |-
    $20$
- id: p2q3-d
  content: |-
    $24$
- id: p2q3-e
  content: |-
    $48$
```

---

<a id="combine-the-steps"></a>
## Combine the Steps

**Example:** The angular velocity of a spinning disk is

$$
\omega(t)=A-Bt^2,
$$

where $A=18\ \mathrm{rad}/\mathrm{s}$ and $B=0.50\ \mathrm{rad}/\mathrm{s}^3$. Through what angle does the disk turn between $t_0=0.0\ \mathrm{s}$ and the time when it reverses direction?

**Explanation**

First find the reversal time:

$$
\begin{aligned}
18-0.50t^2 &= 0 \\
0.50t^2 &= 18 \\
t^2 &= 36 \\
t &= 6.
\end{aligned}
$$

Then integrate angular velocity from $0$ to $6$:

$$
\begin{aligned}
\Delta\theta
&=\int_0^6 (18-0.50t^2)\,dt \\
&=\left[18t-\frac{0.50t^3}{3}\right]_0^6 \\
&=18(6)-\frac{0.50(6^3)}{3} \\
&=108-36 \\
&=72.
\end{aligned}
$$

The disk turns through $72$ radians.

The units also match the requested answer: angular velocity has units $\mathrm{rad}/\mathrm{s}$, and $dt$ has units $\mathrm{s}$, so the integral has units $\mathrm{rad}$.

```quiz
type: radio
id: p2-q4
shuffle: true
content: |-
  A disk has angular velocity $\omega(t)=8-2t^2$ and starts at $t=0$. Through what angle does it turn before reversing direction?
options:
- id: p2q4-a
  content: |-
    $2$ radians
- id: p2q4-b
  content: |-
    $8$ radians
- id: p2q4-c
  content: |-
    $\frac{16}{3}$ radians
- id: p2q4-d
  content: |-
    $\frac{32}{3}$ radians
  correct: true
- id: p2q4-e
  content: |-
    $16$ radians
```

---

## Summary

When a problem asks for the angle turned before reversal, do not stop after finding the reversal time. Use this procedure:

1. Set $\omega(t)=0$.
2. Solve for the positive reversal time.
3. Integrate $\omega(t)$ from the starting time to that reversal time, using $\left[At-\frac{Bt^3}{3}\right]$ for $\omega(t)=A-Bt^2$.
4. Report the result in radians.

The main trap is answering with the time of reversal instead of the angular displacement.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
