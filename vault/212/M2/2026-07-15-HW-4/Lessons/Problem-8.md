# Conservation Tests for an Off-Center Sticking Collision

<!--
lesson-id: 212-M2-044
topic-code: MTH212.M2.44
-->

## Table of Contents

- [Introduction](#introduction)
- [Choose the Complete System](#choose-the-complete-system)
- [Test Each Conservation Law Separately](#test-each-conservation-law-separately)
- [Choose a Valid Origin for Angular Momentum](#choose-a-valid-origin-for-angular-momentum)
- [Apply the Tests to the Rod and Ball](#apply-the-tests-to-the-rod-and-ball)
- [Summary](#summary)

## Prerequisites

- Linear momentum: $\vec P=\sum_i m_i\vec v_i$
- Angular momentum of a particle about an origin $O$: $\vec L_O=\vec r_{i/O}\times\vec p_i$
- The meaning of a perfectly inelastic collision: the objects stick together

---

<a id="introduction"></a>
## Introduction

In an off-center collision, several quantities change at once. The cue is a short collision in an isolated setting such as outer space. The reliable move is to **name the system and the angular-momentum origin before deciding what is conserved**.

Sort every proposed conservation statement with three labels:

| Label | Question to ask |
|---|---|
| **System** | Is this one object, or the complete interacting system? |
| **Origin** | For angular momentum, is the origin fixed and inertial, or the complete system's center of mass? |
| **Law** | Does this quantity require zero external impulse, zero external angular impulse, or an elastic collision? |

For the rod-and-ball problem, the useful system is the combined rod plus ball. During the brief collision, forces between the ball and rod are internal to this system. With no significant external impulse or external angular impulse,

$$
\vec P_{\text{system},i}=\vec P_{\text{system},f}
$$

and angular momentum is conserved about a valid origin, especially the combined system's center of mass. Sticking tells us that kinetic energy is **not** conserved.

The values $m$, $L$, $r$, and $v$ would matter if we were calculating the final speed or angular speed. They do not determine **which** conservation laws apply; the system boundary, external interactions, origin, and the word “sticks” do.

![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)

---

<a id="choose-the-complete-system"></a>
## Choose the Complete System

**Example:** A moving puck strikes a stationary block and sticks to it on a frictionless surface. Is the puck's momentum conserved? Is the puck-block system's momentum conserved?

**Explanation**

During impact, the block exerts an impulse on the puck, so the puck's momentum changes. The force from the block is external if the system contains only the puck.

For the combined puck-block system, the contact impulses are internal and cancel in the total. With negligible external impulse, the combined momentum is conserved:

$$
\vec p_{\text{puck},i}
=
\vec P_{\text{puck+block},f},
$$

because the block initially has zero momentum. The equation does not say that the puck keeps its own momentum.

```quiz
type: radio
id: p8-system-q1
content: |-
  A clay ball hits a cart and sticks while the cart rolls on a nearly frictionless track. Which momentum is guaranteed to be conserved during the collision?
options:
- id: p8-system-q1-a
  content: |-
    The clay ball's momentum alone
- id: p8-system-q1-b
  content: |-
    The cart's momentum alone
- id: p8-system-q1-c
  content: |-
    The total momentum of the clay-ball-and-cart system
  correct: true
- id: p8-system-q1-d
  content: |-
    The momentum of each object separately
- id: p8-system-q1-e
  content: |-
    No momentum, because the objects stick
```

---

<a id="test-each-conservation-law-separately"></a>
## Test Each Conservation Law Separately

**Example:** Two isolated objects collide and stick. Decide whether the system's linear momentum, angular momentum, and kinetic energy are conserved.

**Explanation**

Use a separate condition for each quantity:

| Quantity | Conservation test during the collision |
|---|---|
| Total linear momentum $\vec P$ | Net external impulse is negligible |
| Total angular momentum $\vec L_O$ | Net external angular impulse about $O$ is negligible, with $O$ a valid inertial origin or the isolated system's center of mass |
| Total kinetic energy $K$ | The collision is elastic |

An isolated sticking collision passes the first two tests, but fails the kinetic-energy test. Some initial kinetic energy becomes thermal energy, deformation, or vibration. Total energy is still conserved; kinetic energy is not.

Notice that “inelastic” answers only the kinetic-energy question. It does not cancel linear- or angular-momentum conservation for an isolated system.

```quiz
type: radio
id: p8-laws-q1
content: |-
  Two satellites collide in deep space and latch together. External impulse and external angular impulse are negligible. Which statement is correct?
options:
- id: p8-laws-q1-a
  content: |-
    Total linear momentum, total angular momentum, and kinetic energy are all conserved
- id: p8-laws-q1-b
  content: |-
    Only kinetic energy is conserved
- id: p8-laws-q1-c
  content: |-
    Total linear momentum and total angular momentum are conserved, but kinetic energy is not
  correct: true
- id: p8-laws-q1-d
  content: |-
    Total linear momentum is not conserved because the collision is inelastic
- id: p8-laws-q1-e
  content: |-
    Angular momentum is not conserved because the joined satellites rotate
```

---

<a id="choose-a-valid-origin-for-angular-momentum"></a>
## Choose a Valid Origin for Angular Momentum

**Example:** A small mass strikes the end of an isolated bar and sticks. Why is the center of mass of the complete mass-bar system a safe origin for checking angular momentum, while the bar's own center of mass is not the standard conservation origin?

**Explanation**

The center of mass of the complete isolated system moves with constant velocity because the net external force is zero. It therefore supplies a valid origin for the system's internal rotation. With no external torque,

$$
\vec L_{\mathrm{CM},i}=\vec L_{\mathrm{CM},f}.
$$

The bar's center of mass is the center of only one part of the system. It receives an impulse during the collision and changes velocity. Angular momentum measured relative to that accelerating point is not generally conserved. Likewise, the bar alone receives an external torque from the incoming mass, so the bar's angular momentum about its own center changes.

The phrase “angular momentum is conserved” is incomplete until both the **system** and the **origin** are named.

```quiz
type: radio
id: p8-origin-q1
content: |-
  A particle sticks to the end of an isolated rod. Which choice gives the safest direct conservation statement for the collision?
options:
- id: p8-origin-q1-a
  content: |-
    The rod's angular momentum about the rod's center of mass is conserved
- id: p8-origin-q1-b
  content: |-
    The particle's angular momentum about its own center of mass is conserved
- id: p8-origin-q1-c
  content: |-
    The combined system's angular momentum about the combined system's center of mass is conserved
  correct: true
- id: p8-origin-q1-d
  content: |-
    Angular momentum cannot be conserved when the final object rotates
- id: p8-origin-q1-e
  content: |-
    Angular momentum is conserved only if kinetic energy is conserved
```

---

<a id="apply-the-tests-to-the-rod-and-ball"></a>
## Apply the Tests to the Rod and Ball

**Example:** A nonspinning ball of mass $m/2$ strikes the end of a stationary uniform rod of mass $m$ and sticks. Which conservation statements survive the system-origin-law test?

**Explanation**

The numerical values are not needed for this classification. Test each candidate against the system-origin-law labels:

| Candidate | System-origin-law test | Result |
|---|---|---|
| Ball's center-of-mass momentum | The rod gives the ball an external impulse when the ball alone is the system. | Not conserved |
| Combined system's center-of-mass momentum | The complete system has negligible external impulse. | **Conserved** |
| Rod's angular momentum about the rod's center | The ball gives the rod an external angular impulse when the rod alone is the system. | Not conserved |
| Combined system's angular momentum about the combined center | The complete system has negligible external angular impulse about its own center of mass. | **Conserved** |
| Combined system's angular momentum about the rod's center | The rod's center is attached to only part of the system and changes velocity during impact. | Not the valid conservation statement here |
| Combined system's kinetic energy | “Sticks” means perfectly inelastic. | Not conserved |

Therefore the conserved quantities are the combined system's center-of-mass momentum and its angular momentum about the combined system's center of mass.

```quiz
type: radio
id: p8-source-check
content: |-
  A thin uniform rod of mass $m$ and length $L$ is initially at rest in outer space. A nonspinning ball of mass $m/2$ and radius $r$ strikes one end of the rod with speed $v$ and sticks to it.

  Which quantities are the same immediately before and after the collision—that is, which are conserved?

  A. The center-of-mass momentum of the ball

  B. The center-of-mass momentum of the combined rod–ball system

  C. The angular momentum of the rod about the rod's center of mass

  D. The angular momentum of the combined rod–ball system about the combined system's center of mass

  E. The angular momentum of the combined rod–ball system about the rod's center of mass

  F. The total kinetic energy of the combined rod–ball system

  ![](<../Source/2026-07-15-HW-4/Images/rod-ball-inelastic-collision.png>)
options:
- id: p8-source-check-a
  content: |-
    B and D only
  correct: true
- id: p8-source-check-b
  content: |-
    A, B, and D only
- id: p8-source-check-c
  content: |-
    B, D, and F only
- id: p8-source-check-d
  content: |-
    B and E only
- id: p8-source-check-e
  content: |-
    C and D only
```

---

## Summary

For a collision-conservation question:

1. **Name the complete system.** Internal collision impulses do not conserve each object's momentum, but they cancel in the system total.
2. **Test linear momentum:** negligible external impulse $\Rightarrow$ total $\vec P$ is conserved.
3. **Name the angular-momentum origin.** Use a fixed inertial origin or the complete isolated system's center of mass; then negligible external angular impulse $\Rightarrow$ total $\vec L$ is conserved.
4. **Read the collision type.** If the objects stick, kinetic energy is not conserved.

Main trap: do not transfer a conservation law for the complete isolated system to one object or to an origin attached to only one part of the system.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
