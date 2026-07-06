# Maximum Speed on a Frictional Banked Curve

## Table of Contents

- [Introduction](#introduction)
- [Friction Points Down the Bank at Maximum Speed](#friction-points-down-the-bank-at-maximum-speed)
- [Write the Radial and Vertical Force Equations](#write-the-radial-and-vertical-force-equations)
- [Divide the Equations to Isolate Speed](#divide-the-equations-to-isolate-speed)
- [Evaluate the Formula Carefully](#evaluate-the-formula-carefully)
- [Summary](#summary)

## Prerequisites

- Resolve a force into components parallel to horizontal radial and vertical axes.
- Use $a_r=\frac{v^2}{r}$ for uniform circular motion.
- Use $f_s=\mu_sN$ at the limiting speed before sliding.

---

<a id="introduction"></a>
## Introduction

When a car moves around a banked curve with friction, the maximum-speed case has a specific cue: the car is just about to slide up the bank. Static friction opposes that impending motion, so it points down the slope of the bank.

The task is to compute the maximum speed by combining the radial force equation with the vertical force equation:

$$
v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}.
$$

The important work is knowing why the signs in that fraction look that way.

---

<a id="friction-points-down-the-bank-at-maximum-speed"></a>
## Friction Points Down the Bank at Maximum Speed

**Example:** A car travels on a banked curve with angle $\theta$ and coefficient of static friction $\mu_s$. Which way does static friction point when the car is moving at the maximum speed before sliding?

**Explanation**

At the no-friction design speed, the normal force supplies exactly the needed inward force. If the car moves faster than that, it needs more inward force than the normal force alone can provide. The car tends to slide up the bank, so static friction points down the bank.

Down the bank means friction has two components:

- inward horizontal component: $f_s\cos\theta$
- downward vertical component: $f_s\sin\theta$

That direction is the sign decision that controls the whole formula. For the maximum-speed case, friction helps provide inward force but makes the vertical support equation smaller.

```quiz
type: radio
id: p6-friction-direction
content: |-
  A car is on a banked curve and is moving faster than the no-friction design speed. Which direction does static friction point?
options:
- id: a
  content: |-
    Up the bank, because the car needs help moving outward.
- id: b
  content: |-
    Down the bank, because the car tends to slide up the bank.
  correct: true
  feedback: |-
    At high speed, the car tends to slide up the bank, so static friction points down the bank.
- id: c
  content: |-
    Forward along the car's motion.
- id: d
  content: |-
    Backward opposite the car's motion.
```

---

<a id="write-the-radial-and-vertical-force-equations"></a>
## Write the Radial and Vertical Force Equations

**Example:** For the maximum-speed case, write the force equations for a car of mass $m$ on a banked curve of radius $r$ and angle $\theta$.

**Explanation**

Use radial inward as the positive horizontal direction. The normal force contributes $N\sin\theta$ inward. Since friction points down the bank at maximum speed, friction contributes $\mu_sN\cos\theta$ inward.

| Force | Radial inward component | Vertical upward component |
| --- | ---: | ---: |
| Normal force | $N\sin\theta$ | $N\cos\theta$ |
| Static friction down the bank | $\mu_sN\cos\theta$ | $-\mu_sN\sin\theta$ |
| Weight | $0$ | $-mg$ |

$$
N\sin\theta+\mu_sN\cos\theta=\frac{mv^2}{r}
$$

Use upward as positive vertical direction. The normal force contributes $N\cos\theta$ upward. Weight and the vertical part of friction point downward.

$$
N\cos\theta-mg-\mu_sN\sin\theta=0
$$

So the vertical equation can be written as

$$
N(\cos\theta-\mu_s\sin\theta)=mg.
$$

```quiz
type: radio
id: p6-force-equations
content: |-
  For the maximum-speed case on a banked curve, which pair of equations uses the correct friction direction?
options:
- id: a
  content: |-
    $N\sin\theta+\mu_sN\cos\theta=\frac{mv^2}{r}$ and $N\cos\theta-\mu_sN\sin\theta=mg$
  correct: true
  feedback: |-
    Down-slope friction adds inward force and subtracts from the upward vertical balance.
- id: b
  content: |-
    $N\sin\theta-\mu_sN\cos\theta=\frac{mv^2}{r}$ and $N\cos\theta+\mu_sN\sin\theta=mg$
- id: c
  content: |-
    $N\cos\theta+\mu_sN\sin\theta=\frac{mv^2}{r}$ and $N\sin\theta-\mu_sN\cos\theta=mg$
- id: d
  content: |-
    $N+\mu_sN=\frac{mv^2}{r}$ and $N-mg=0$
```

---

<a id="divide-the-equations-to-isolate-speed"></a>
## Divide the Equations to Isolate Speed

**Example:** Starting from the maximum-speed equations, solve for $v_{\max}$.

**Explanation**

Start with the two equations:

$$
N(\sin\theta+\mu_s\cos\theta)=\frac{mv^2}{r}
$$

$$
N(\cos\theta-\mu_s\sin\theta)=mg
$$

Divide the radial equation by the vertical equation. This cancels $N$ and $m$:

$$
\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}
=\frac{v^2/r}{g}.
$$

This is why the car's mass does not appear in the final speed formula. The given mass can matter for the size of the normal force, but it does not change the maximum speed.

Then solve for $v$:

$$
v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}.
$$

```quiz
type: radio
id: p6-speed-formula
content: |-
  Which formula gives the maximum speed for a frictional banked curve when friction points down the bank?
options:
- id: a
  content: |-
    $v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}$
  correct: true
  feedback: |-
    The numerator has both inward force components, and the denominator comes from the vertical balance.
- id: b
  content: |-
    $v_{\max}=\sqrt{rg\left(\frac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}\right)}$
- id: c
  content: |-
    $v_{\max}=\sqrt{rg\tan\theta}$
- id: d
  content: |-
    $v_{\max}=\sqrt{\mu_srg}$
```

---

<a id="evaluate-the-formula-carefully"></a>
## Evaluate the Formula Carefully

**Example:** Find the maximum speed for $r=55\ \mathrm{m}$, $\theta=12^\circ$, and $\mu_s=0.65$.

**Explanation**

The given mass $m=1400\ \mathrm{kg}$ is not needed because it canceled when the force equations were divided.

Substitute into the maximum-speed formula:

$$
v_{\max}=\sqrt{(55)(9.8)\left(\frac{\sin 12^\circ+0.65\cos 12^\circ}{\cos 12^\circ-0.65\sin 12^\circ}\right)}.
$$

Evaluate the trig pieces in degree mode:

$$
\sin 12^\circ\approx 0.208
\qquad
\cos 12^\circ\approx 0.978.
$$

Then the ratio is

$$
\frac{\sin 12^\circ+0.65\cos 12^\circ}{\cos 12^\circ-0.65\sin 12^\circ}
\approx
\frac{0.208+0.65(0.978)}{0.978-0.65(0.208)}
\approx 1.001.
$$

So

$$
v_{\max}\approx \sqrt{539.5}\approx 23.2\ \mathrm{m/s}.
$$

To two significant figures, the answer is

$$
23\ \mathrm{m/s}.
$$

```quiz
type: radio
id: p6-numeric-evaluation
content: |-
  A car goes around a banked curve with $r=60\ \mathrm{m}$, $\theta=10^\circ$, and $\mu_s=0.50$. Use
  $$
  v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}
  $$
  with $g=9.8\ \mathrm{m/s^2}$. What is $v_{\max}$ to two significant figures?
options:
- id: a
  content: |-
    $10\ \mathrm{m/s}$
- id: b
  content: |-
    $21\ \mathrm{m/s}$
  correct: true
  feedback: |-
    The ratio is about $0.742$, so $v_{\max}\approx\sqrt{(60)(9.8)(0.742)}\approx 21\ \mathrm{m/s}$.
- id: c
  content: |-
    $17\ \mathrm{m/s}$
- id: d
  content: |-
    $24\ \mathrm{m/s}$
```

---

<a id="summary"></a>
## Summary

For the maximum speed on a frictional banked curve, use the cue "about to slide up the bank." That means static friction points down the bank.

The force equations are

$$
N(\sin\theta+\mu_s\cos\theta)=\frac{mv^2}{r}
$$

and

$$
N(\cos\theta-\mu_s\sin\theta)=mg.
$$

Dividing them gives

$$
v_{\max}=\sqrt{rg\left(\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}\right)}.
$$

The main trap is using the minimum-speed signs. For maximum speed, friction points down the bank, so it adds inward force and points partly downward.

The mass may be given, but it cancels out. Use the mass only if you are later asked for $N$ or $f_s$, not when the target is $v_{\max}$.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Deciding True Statements About Static Friction on a Banked Turn](<../../2026-07-03-HW-2/Lessons/Problem-9.md>)

<!-- study-guide-nav:end -->
