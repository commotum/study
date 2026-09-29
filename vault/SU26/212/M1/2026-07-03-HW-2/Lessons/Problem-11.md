# Finding the Minimum Entry Speed for a Loop-the-Loop

<!--
lesson-id: 212-M1-029
topic-code: MTH212.M1.29
-->

## Table of Contents

- [Introduction](#introduction)
- [Set the Top Contact Condition](#set-the-top-contact-condition)
- [Use Energy from Bottom to Top](#use-energy-from-bottom-to-top)
- [Combine the Two Conditions](#combine-the-two-conditions)
- [Find Hony's Entry Speed](#find-honys-entry-speed)
- [Summary](#summary)

## Prerequisites

- Use $a_r=\dfrac{v^2}{r}$ for circular motion of radius $r$.
- Write a radial force equation with inward as the positive direction.
- Use conservation of mechanical energy when rolling friction is ignored.
- Recognize that the top of a loop is $2r$ higher than the bottom.

---

<a id="introduction"></a>
## Introduction

Hony Tawk enters the bottom of a circular loop of radius $r$. Rolling friction is ignored, and he must complete the loop without losing contact with the track. What is the minimum speed he can have when he enters?

![](<../Source/Images/loop-the-loop-diagram.png>)

The slowest successful trip still requires motion at the top. There, at the threshold, gravity alone supplies the inward force and the track has just stopped needing to push, so the normal force is zero. The entry speed must provide both the gravitational potential energy gained over the $2r$ climb and the kinetic energy that remains at the top.

---

<a id="set-the-top-contact-condition"></a>
## Set the Top Contact Condition

**Example:** A rider is at the top of a vertical loop of radius $r$ with speed $v_{\mathrm{top}}$. What is the smallest possible $v_{\mathrm{top}}$ that still keeps contact with the track?

**Explanation**

At the top of the loop, inward points downward. Both gravity and the normal force point inward if the rider is still in contact with the track:

$$
\sum F_r=m a_r=m\dfrac{v_{\mathrm{top}}^2}{r}=mg+N_{\mathrm{top}}.
$$

The track can push on the rider, but it cannot pull. At the exact minimum speed for contact,

$$
N_{\mathrm{top}}=0.
$$

So the force equation becomes

$$
mg=m\dfrac{v_{\mathrm{top}}^2}{r}.
$$

Cancel $m$ and solve:

$$
v_{\mathrm{top}}^2=gr,
$$

so

$$
v_{\mathrm{top}}=\sqrt{gr}.
$$

```quiz
type: radio
id: p11-q1-top-contact
shuffle: true
content: |-
  A cart is just barely maintaining contact at the top of a vertical loop of radius $r$. Which condition should be used at that instant?
options:
- id: p11q1-a
  content: |-
    $N_{\mathrm{top}}=0$ and $mg=m\dfrac{v_{\mathrm{top}}^2}{r}$
  correct: true
- id: p11q1-b
  content: |-
    $N_{\mathrm{top}}=mg$ and $mg=m\dfrac{v_{\mathrm{top}}^2}{r}$
- id: p11q1-c
  content: |-
    $N_{\mathrm{top}}=0$ and $0=m\dfrac{v_{\mathrm{top}}^2}{r}$
- id: p11q1-d
  content: |-
    $N_{\mathrm{top}}$ must point outward and equal $mg$.
```

---

<a id="use-energy-from-bottom-to-top"></a>
## Use Energy from Bottom to Top

**Example:** A rider enters the bottom of a frictionless vertical loop of radius $r$ with speed $v_0$ and reaches the top with speed $v_{\mathrm{top}}$. Write the energy equation connecting these speeds.

**Explanation**

Choose gravitational potential energy $0$ at the bottom of the loop. The top of the loop is $2r$ higher than the bottom, so the top has gravitational potential energy

$$
mg(2r).
$$

With rolling friction ignored, mechanical energy is conserved:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2+mg(2r).
$$

This equation says the entry kinetic energy must supply both the kinetic energy still needed at the top and the gravitational potential energy gained while rising.

```quiz
type: radio
id: p11-q2-energy-equation
shuffle: true
content: |-
  A cart enters a frictionless vertical loop of radius $r$ at the bottom with speed $v_0$ and reaches the top with speed $v_{\mathrm{top}}$. Which energy equation correctly connects the two speeds?
options:
- id: p11q2-a
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2+mg(2r)$
  correct: true
- id: p11q2-b
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2+mgr$
- id: p11q2-c
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2-mg(2r)$
- id: p11q2-d
  content: |-
    $v_0=v_{\mathrm{top}}$ because the path is circular.
```

---

<a id="combine-the-two-conditions"></a>
## Combine the Two Conditions

**Example:** A rider enters a frictionless vertical loop of radius $r$ from the bottom. What entry speed gives the minimum speed for completing the loop?

**Explanation**

Start with the energy equation:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2+mg(2r).
$$

The unknown is the entry speed $v_0$. Treat $g$ and $r$ as given quantities, and replace $v_{\mathrm{top}}^2$ using the contact condition.

Keep the position labels attached to every speed. The radial equation gives a condition on $v_{\mathrm{top}}$ at one instant; it does not directly give the bottom entry speed $v_0$. Conservation of energy connects those differently located quantities.

At the minimum speed, the top contact condition gives

$$
v_{\mathrm{top}}^2=gr.
$$

Substitute that into the energy equation:

$$
\dfrac12 mv_0^2=\dfrac12 m(gr)+2mgr.
$$

The right side has

$$
\dfrac12 mgr+2mgr=\dfrac52 mgr.
$$

So

$$
\dfrac12 mv_0^2=\dfrac52 mgr.
$$

Cancel $\dfrac12 m$ from both sides:

$$
v_0^2=5gr.
$$

Since speed is nonnegative,

$$
v_0=\sqrt{5gr}.
$$

```quiz
type: radio
id: p11-q3-combine
shuffle: true
content: |-
  A rider enters the bottom of a frictionless loop of radius $r$. At the minimum entry speed, $v_{\mathrm{top}}^2=gr$. What is $v_0^2$ at the bottom?
options:
- id: p11q3-a
  content: |-
    $v_0^2=gr$
- id: p11q3-b
  content: |-
    $v_0^2=3gr$
- id: p11q3-c
  content: |-
    $v_0^2=4gr$
- id: p11q3-d
  content: |-
    $v_0^2=5gr$
  correct: true
```

---

<a id="find-honys-entry-speed"></a>
## Find Hony's Entry Speed

**Example:** Hony Tawk completes a circular loop-the-loop of radius $r$ and never leaves contact. What is the minimum speed required to enter the loop if rolling friction is ignored?

**Explanation**

The top contact condition gives the minimum top speed:

$$
v_{\mathrm{top}}^2=gr.
$$

The energy equation from bottom to top is

$$
\dfrac12 mv_0^2=\dfrac12 m(gr)+mg(2r).
$$

This gives

$$
v_0^2=5gr,
$$

so the entry speed is

$$
v_0=\sqrt{5gr}.
$$

The value $\sqrt{gr}$ is only the required speed at the top, not the entry speed. Using $2\sqrt{gr}=\sqrt{4gr}$ accounts for the climb but leaves no kinetic energy at the top; the extra $gr$ in $v_0^2=5gr$ supplies the motion needed to maintain contact there.

```quiz
type: radio
id: p11-q4-original-choice
shuffle: true
content: |-
  Hony Tawk completes a circular loop-the-loop and never leaves contact with the loop of radius $r$. What is the minimum speed required for Hony Tawk to enter the loop-the-loop? Ignore rolling friction.
options:
- id: p11q4-a
  content: |-
    $\sqrt{2gr}$
- id: p11q4-b
  content: |-
    $\sqrt{3gr}$
- id: p11q4-c
  content: |-
    $2\sqrt{gr}$
- id: p11q4-d
  content: |-
    $\sqrt{5gr}$
  correct: true
```

---

<a id="summary"></a>
## Summary

For a minimum-speed loop-the-loop question, test contact at the top first. At the minimum, $N_{\mathrm{top}}=0$, so

$$
v_{\mathrm{top}}^2=gr.
$$

Then use energy from the bottom to the top:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\mathrm{top}}^2+mg(2r).
$$

Substituting $v_{\mathrm{top}}^2=gr$ gives

$$
v_0=\sqrt{5gr}.
$$

Check the symbolic result before accepting it. Its units are speed, mass has canceled, and it predicts that a larger loop or stronger gravity requires a larger entry speed. These checks also expose the common mistake of reporting $\sqrt{gr}$, which is the speed at the top rather than at the entrance.

Stopping at the top-speed condition gives the speed at the wrong location. The energy step must also use the full bottom-to-top height change of $2r$.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Finding the Critical Angle Where a Slider Leaves a Sphere](Problem-13.md)

Study guide index: 34/35

---
<!-- lesson-nav:end -->
