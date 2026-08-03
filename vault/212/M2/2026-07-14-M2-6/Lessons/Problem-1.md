# Predicting Angular Speed When Mass Is Added

<!--
lesson-id: 212-M2-036
topic-code: MTH212.M2.36
-->

## Table of Contents

- [Introduction](#introduction)
- [Check Whether Angular Momentum Is Conserved](#check-whether-angular-momentum-is-conserved)
- [Account for the Incoming Mass](#account-for-the-incoming-mass)
- [Connect Added Mass to Moment of Inertia](#connect-added-mass-to-moment-of-inertia)
- [Compare the Initial and Final Angular Speeds](#compare-the-initial-and-final-angular-speeds)
- [Apply the Method](#apply-the-method)
- [Summary](#summary)

## Prerequisites

- Use the relation $L=I\omega$ for rotation about a fixed axis.
- Recognize that mass farther from a rotation axis contributes to moment of inertia.
- Compare positive quantities using a ratio.

---

<a id="introduction"></a>
## Introduction

When mass joins a rotating system, do not assume that the angular speed stays fixed. First identify whether an external torque changes the system's angular momentum. If the angular momentum about the axis remains constant, then

$$
L=I\omega=\text{constant}.
$$

The recognition cues in the rotating-cups problem are **frictionless bearings** and rain that falls **vertically**. These conditions make the external torque and the rain's incoming angular momentum about the vertical axis negligible. Once the rain collects at a nonzero radius, the moment of inertia increases, so the angular speed must decrease.

| Problem cue | Mathematical consequence |
|---|---|
| frictionless bearings | $\tau_{\text{ext},z}\approx0$ |
| rain falls vertically | incoming rain has negligible $L_z$ |
| rain remains in cups away from the axis | $I_f>I_i$ |
| $L_z$ fixed while $I$ increases | $\omega_f<\omega_i$ |

---

<a id="check-whether-angular-momentum-is-conserved"></a>
## Check Whether Angular Momentum Is Conserved

**Example:** A platform rotates about a vertical axle. The axle is frictionless, and no motor acts on the platform. Which rotational quantity is conserved while an object lands on it?

**Explanation**

About the vertical axis, the axle supplies essentially no friction torque. Gravity and the support forces are vertical, so they do not supply a torque about that same axis. Therefore the angular momentum of the platform-plus-object system is conserved:

$$
L_i=L_f.
$$

Rotational kinetic energy need not be conserved because landing and sticking is an inelastic process.

```quiz
type: radio
id: m2-6-p1-conserved-quantity
content: |-
  A disk rotates on a frictionless vertical axle, and a lump of clay lands on it and sticks. Which quantity is conserved about the axle during the landing?
options:
- id: a
  content: |-
    Angular momentum
  correct: true
  feedback: |-
    With negligible external torque about the axle, angular momentum is conserved. Sticking is inelastic, so rotational kinetic energy generally decreases.
- id: b
  content: |-
    Angular speed
- id: c
  content: |-
    Moment of inertia
- id: d
  content: |-
    Rotational kinetic energy
- id: e
  content: |-
    Tangential speed at every point
```

---

<a id="account-for-the-incoming-mass"></a>
## Account for the Incoming Mass

**Example:** Rain falls straight downward into cups rotating about a vertical axis. Does the rain bring angular momentum about that axis before it lands?

**Explanation**

Before landing, the rain's velocity is vertical. It has essentially no tangential velocity around the vertical axis, so its angular momentum component about that axis is negligible.

The rain does add mass to the final rotating system, but it does not add the angular momentum needed to keep the old angular speed. The original angular momentum must be shared by a system with a larger moment of inertia.

```quiz
type: radio
id: m2-6-p1-incoming-rain
content: |-
  Water falls vertically into a container that moves in a horizontal circle about a vertical axis. Just before the water lands, what is its angular momentum about the vertical axis?
options:
- id: a
  content: |-
    Essentially zero, because it has no tangential velocity about the axis
  correct: true
  feedback: |-
    Angular momentum about the vertical axis depends on motion around that axis. Vertically falling water has essentially no tangential velocity, so its incoming angular momentum about that axis is negligible.
- id: b
  content: |-
    Large and in the direction of the container's rotation
- id: c
  content: |-
    Large and opposite the container's rotation
- id: d
  content: |-
    Equal to the container's angular momentum
- id: e
  content: |-
    Undefined because the water is moving vertically
```

---

<a id="connect-added-mass-to-moment-of-inertia"></a>
## Connect Added Mass to Moment of Inertia

**Example:** Two identical cups, each of mass $M$, rotate at radius $\ell$. Each cup collects rainwater of mass $\Delta m$. Compare the initial and final moments of inertia, treating the cups and water as point masses.

**Explanation**

For point masses, each contribution is $mr^2$. Therefore,

$$
I_i=2M\ell^2
$$

and

$$
I_f=2(M+\Delta m)\ell^2.
$$

Because $\Delta m>0$,

$$
I_f>I_i.
$$

The exact point-mass model is not needed for the qualitative conclusion: adding mass at a nonzero distance from the axis increases $I$.

```quiz
type: radio
id: m2-6-p1-inertia-change
content: |-
  A rotating container collects mass while its distance from the rotation axis stays fixed. What happens to the system's moment of inertia?
options:
- id: a
  content: |-
    It increases.
  correct: true
  feedback: |-
    Moment of inertia includes contributions of the form $mr^2$. Adding mass at a fixed nonzero radius increases the moment of inertia.
- id: b
  content: |-
    It decreases.
- id: c
  content: |-
    It remains constant.
- id: d
  content: |-
    It becomes zero.
- id: e
  content: |-
    Its change cannot be determined from the mass change.
```

---

<a id="compare-the-initial-and-final-angular-speeds"></a>
## Compare the Initial and Final Angular Speeds

**Example:** A rotating system has negligible external torque. Its moment of inertia increases from $I_i$ to $I_f$. Express its final angular speed in terms of its initial angular speed $\omega_i$.

**Explanation**

Conservation of angular momentum gives

$$
I_i\omega_i=I_f\omega_f.
$$

Solve for the final angular speed:

$$
\boxed{\omega_f=\frac{I_i}{I_f}\omega_i}.
$$

If $I_f>I_i$, then $I_i/I_f<1$, so $\omega_f<\omega_i$. The system slows down.

The ratio form makes a useful numerical check. For example, if the collected mass makes $I_f=1.25I_i$, then

$$
\frac{\omega_f}{\omega_i}
=\frac{I_i}{1.25I_i}
=0.80.
$$

Because the ratio is less than $1$, the final angular speed is smaller. Any proposed answer that predicts a speedup would reverse this inverse relationship.

```quiz
type: radio
id: m2-6-p1-speed-ratio
content: |-
  With no external torque, a rotating system's moment of inertia doubles. What happens to its angular speed?
options:
- id: a
  content: |-
    It becomes one-half as large.
  correct: true
  feedback: |-
    Since $I_i\omega_i=I_f\omega_f$, doubling $I$ makes $\omega_f=(I_i/2I_i)\omega_i=\omega_i/2$.
- id: b
  content: |-
    It doubles.
- id: c
  content: |-
    It remains unchanged.
- id: d
  content: |-
    It becomes four times as large.
- id: e
  content: |-
    It becomes zero.
```

---

<a id="apply-the-method"></a>
## Apply the Method

**Example:** Predict what happens to the angular speed of two rotating cups when vertically falling rain collects in them.

**Explanation**

In the diagram, each cup lies a nonzero distance $\ell$ from the vertical axis. Water retained in either cup therefore adds a positive $mr^2$ contribution to the system's moment of inertia.

Use the chain of implications:

$$
\tau_{\text{ext},z}\approx0
\quad\Longrightarrow\quad
L_z=I\omega=\text{constant},
$$

$$
\text{rain collects at nonzero radius}
\quad\Longrightarrow\quad
I_f>I_i,
$$

and therefore

$$
\omega_f=\frac{I_i}{I_f}\omega_0<\omega_0.
$$

The system slows down. Angular speed is not conserved, and rotational kinetic energy is not the correct conserved quantity for the inelastic capture of rain.

```quiz
type: radio
id: m2-6pre-q1
shuffle: true
content: |-
  **Question 1**

  Two cups connected by a rod rotate in a horizontal circle on frictionless bearings. It begins to rain, and rainwater collects in the cups.

  What happens to the system's angular speed?

  ![](<../Source/Images/rotating-cups-collecting-rain.png>)
options:
- id: a
  content: |-
    It speeds up.
- id: b
  content: |-
    It slows down.
  correct: true
  feedback: |-
    The rain falls vertically and adds essentially no angular momentum about the rotation axis. With frictionless bearings, angular momentum is conserved:

    $$
    L=I\omega=\text{constant}.
    $$

    As rain collects, the system's mass and moment of inertia increase. Therefore,

    $$
    \omega_f=\frac{I_i}{I_f}\omega_0.
    $$

    Since $I_f>I_i$, it follows that $\omega_f<\omega_0$.
- id: c
  content: |-
    It continues rotating at the same angular speed.
```

---

<a id="summary"></a>
## Summary

- **Cue:** negligible external torque, plus incoming mass with negligible angular momentum about the axis.
- **Conserved quantity:** $L=I\omega$, not $\omega$ and not rotational kinetic energy.
- **Mass effect:** collected rain at nonzero radius increases $I$.
- **Speed comparison:** $\omega_f=(I_i/I_f)\omega_i$.
- **Ratio check:** if $I_f>I_i$, then $I_i/I_f<1$.
- **Conclusion:** multiplying $\omega_i$ by a factor below $1$ makes the system slow down.
- **Main trap:** conservation of angular momentum does not mean constant angular speed.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
