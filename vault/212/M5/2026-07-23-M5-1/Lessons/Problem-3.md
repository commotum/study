# Identifying the Restoring Force of a Hanging Spring

<!--
lesson-id: 212-M5-003
topic-code: MTH212.M5.03
-->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Recognize a Restoring Force](#recognize-a-restoring-force)
- [Separate Equilibrium Balance From Restoration](#separate-equilibrium-balance-from-restoration)
- [Check Both Sides of Equilibrium](#check-both-sides-of-equilibrium)
- [Apply the Test to Problem 3](#apply-the-test-to-problem-3)
- [Summary](#summary)

## Prerequisites

- Identify the equilibrium position of an oscillating object.
- Add forces with signs that represent direction.
- Recall that gravity near Earth's surface is approximately constant.
- Recall that an ideal spring's force changes with its stretch or compression.

---

<a id="introduction"></a>
## Introduction

When a mass on a hanging spring is displaced from equilibrium and the question asks what restores it, look for the force that changes with displacement. Determine the restoring force by comparing the constant gravitational force with the changing spring force and identifying which change makes the net force point back toward equilibrium.

---

<a id="recognize-a-restoring-force"></a>
## Recognize a Restoring Force

**Recognition cue:** When a mass is displaced from equilibrium and the question asks what restores it, look for the force whose change makes the net force point back toward equilibrium.

Let $\Delta x$ be displacement from equilibrium. A restoring net force has the form

$$
F_{\mathrm{net}}=-k\Delta x.
$$

Here $k>0$ sets the force magnitude per unit displacement. The negative scalar makes the force vector point opposite the displacement vector:

- If $\Delta x>0$, then $F_{\mathrm{net}}<0$.
- If $\Delta x<0$, then $F_{\mathrm{net}}>0$.
- If $\Delta x=0$, then $F_{\mathrm{net}}=0$.

**Example:** A block on a horizontal spring is pulled to the right of equilibrium. The spring pulls left, so the spring force is restoring.

**Explanation**

The displacement and the spring force point in opposite directions. That direction reversal is the defining test.

```quiz
type: radio
id: p3-recognize-restoring
content: |-
  A block attached to a horizontal spring is displaced to the left of equilibrium. Which direction must the restoring net force point?
options:
- id: p3-recognize-restoring-a
  content: |-
    To the right
  correct: true
  feedback: |-
    A restoring net force points opposite the displacement. A leftward displacement therefore requires a rightward net force. Choosing “to the left” makes the force push the block farther from equilibrium.
- id: p3-recognize-restoring-b
  content: |-
    To the left
- id: p3-recognize-restoring-c
  content: |-
    It must be zero
- id: p3-recognize-restoring-d
  content: |-
    Perpendicular to the displacement
```

---

<a id="separate-equilibrium-balance-from-restoration"></a>
## Separate Equilibrium Balance From Restoration

For a hanging mass, gravity pulls downward with the constant force $mg$. The spring pulls upward, and its force changes as the spring's length changes.

At equilibrium, the forces balance:

$$
\vec F_{\mathrm{spring,eq}}+\vec F_g=\vec 0,
$$

or, in magnitudes, $F_{\mathrm{spring,eq}}=mg$. The individual forces are not zero; their vector sum is zero.

This balance locates equilibrium; it does not make gravity the restoring force. If downward is positive and the mass is displaced by $\Delta x$ from equilibrium, then

$$
\begin{aligned}
F_{\mathrm{net}}
&=mg-k(x_{\mathrm{eq}}+\Delta x)\\
&=mg-kx_{\mathrm{eq}}-k\Delta x\\
&=-k\Delta x,
\end{aligned}
$$

because $mg=kx_{\mathrm{eq}}$. Gravity cancels the equilibrium part of the spring force. The **changing spring force** supplies the displacement-dependent net force.

**Example:** A hanging mass is motionless at equilibrium. Which statement best describes its forces?

**Explanation**

Gravity and the spring force are both present, but they have equal magnitudes and opposite directions. Therefore, the net force is zero at equilibrium.

```quiz
type: radio
id: p3-equilibrium-balance
content: |-
  A mass hangs motionless from a vertical spring at equilibrium. Which statement is correct?
options:
- id: p3-equilibrium-balance-a
  content: |-
    Gravity is absent.
- id: p3-equilibrium-balance-b
  content: |-
    The spring force is absent.
- id: p3-equilibrium-balance-c
  content: |-
    The spring force and gravity balance, so the net force is zero.
  correct: true
  feedback: |-
    At equilibrium, both forces act and are opposite vectors of equal magnitude. Their resultant is zero. Equilibrium does not mean that the individual forces disappear.
- id: p3-equilibrium-balance-d
  content: |-
    Gravity is the only force on the mass.
```

---

<a id="check-both-sides-of-equilibrium"></a>
## Check Both Sides of Equilibrium

The cleanest conceptual check is to move the mass to each side of equilibrium.

| Position of mass | Spring force compared with gravity | Direction of net force |
| --- | --- | --- |
| Below equilibrium | Spring force is larger | Upward, toward equilibrium |
| At equilibrium | Spring force equals gravity | Zero |
| Above equilibrium | Spring force is smaller | Downward, toward equilibrium |

Gravity does not reverse or change size during this motion. The spring force changes, causing the net force to reverse direction at equilibrium.

Choosing equilibrium as the coordinate origin makes the pattern especially clear:

$$
(\Delta x,F_{\mathrm{net}})=(0,0),
$$

and $F_{\mathrm{net}}=-k\Delta x$ is a straight-line proportional relationship with negative slope. The line passes through the origin because the net force is zero at equilibrium.

**Example:** A hanging mass is pulled below equilibrium and released. Its spring is stretched more than at equilibrium, so the upward spring force exceeds the downward gravitational force. The net force is upward, toward equilibrium.

**Explanation**

The individual force that changes with displacement is the spring force. The resulting net force is restoring because it points opposite $\Delta x$.

```quiz
type: radio
id: p3-both-sides
content: |-
  A hanging mass is displaced slightly above equilibrium while the spring remains stretched. What makes the net force point downward toward equilibrium?
options:
- id: p3-both-sides-a
  content: |-
    Gravity becomes stronger.
- id: p3-both-sides-b
  content: |-
    The upward spring force becomes smaller than the constant downward gravitational force.
  correct: true
  feedback: |-
    Gravity remains constant. Above equilibrium, the spring is less stretched, so its upward force is smaller than gravity and the resultant points downward. The spring force itself need not reverse direction.
- id: p3-both-sides-c
  content: |-
    Both gravity and the spring force vanish.
- id: p3-both-sides-d
  content: |-
    The spring force changes direction and points downward.
```

---

<a id="apply-the-test-to-problem-3"></a>
## Apply the Test to Problem 3

**Example:** A mass oscillates on a hanging spring. What provides the restoring force to the mass? Explain.

**Explanation**

The correct choice is **Spring force**. Gravity is constant and sets the equilibrium position, but it does not vary with displacement from equilibrium. The changing spring force produces the net force back toward equilibrium. Relative to equilibrium,

$$
F_{\mathrm{net}}=-k\Delta x.
$$

Use this decision test:

1. At equilibrium, gravity and the spring force cancel.
2. Away from equilibrium, gravity stays approximately constant while the spring force changes.
3. That change makes the resultant point back toward equilibrium.

Therefore, the requested force is the **Spring force**, even though the restoring equation describes the net force relative to equilibrium.

```quiz
type: radio
id: p3-source-check
shuffle: true
content: |-
  **Question 2**

  A mass oscillates on a hanging spring. What provides the restoring force to the mass? Explain.
options:
- id: p3-source-check-a
  content: Gravity
  feedback: Gravity is constant and sets the equilibrium position, but it does not vary with displacement from equilibrium.
- id: p3-source-check-b
  content: Spring force
  correct: true
  feedback: The changing spring force produces the net force back toward equilibrium. Relative to equilibrium, $F_{\mathrm{net}}=-k\Delta x$.
- id: p3-source-check-c
  content: Other
```

---

## Summary

- Cue: the object is displaced from equilibrium and the net force must point back.
- Rule: with $k>0$, the negative sign in $F_{\mathrm{net}}=-k\Delta x$ means that force and displacement point in opposite directions.
- Hanging-spring result: gravity fixes the equilibrium stretch; the changing spring force provides the restoring effect.
- Resultant check: the spring force and gravity add to zero at equilibrium, not because either individual force vanishes.
- Main trap: do not call gravity the restoring force merely because gravity acts on the mass; it stays approximately constant during the oscillation.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
