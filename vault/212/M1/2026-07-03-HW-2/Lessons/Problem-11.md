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
- [Match the Answer Choices](#match-the-answer-choices)
- [Summary](#summary)

## Prerequisites

- Use $a_c=\dfrac{v^2}{r}$ for circular motion of radius $r$.
- Write a radial force equation with inward as the positive direction.
- Use conservation of mechanical energy when rolling friction is ignored.
- Recognize that the top of a loop is $2r$ higher than the bottom.

---

<a id="introduction"></a>
## Introduction

When a loop-the-loop problem asks for the minimum entry speed needed to never lose contact, the key cue is "minimum" together with "never leaves contact." Compute the minimum entry speed by setting the normal force to zero at the top of the loop, then using energy conservation from the bottom to the top.

Use the same three checks each time:

1. At the top, set $N=0$ for the just-barely-contact case.
2. From bottom to top, use a height change of $2r$.
3. Substitute the top-speed condition into the energy equation and take the positive square root.

For Hony Tawk's loop of radius $r$, the minimum entry speed is the answer choice that makes the top speed just large enough for circular motion.

---

<a id="set-the-top-contact-condition"></a>
## Set the Top Contact Condition

**Example:** A rider is at the top of a vertical loop of radius $R$ with speed $v_{\text{top}}$. What is the smallest possible $v_{\text{top}}$ that still keeps contact with the track?

**Explanation**

At the top of the loop, inward points downward. Both gravity and the normal force point inward if the rider is still in contact with the track:

$$
mg+N=m\dfrac{v_{\text{top}}^2}{R}.
$$

The track can push on the rider, but it cannot pull. At the exact minimum speed for contact,

$$
N=0.
$$

So the force equation becomes

$$
mg=m\dfrac{v_{\text{top}}^2}{R}.
$$

Cancel $m$ and solve:

$$
v_{\text{top}}^2=gR,
$$

so

$$
v_{\text{top}}=\sqrt{gR}.
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
    $N=0$ and $mg=m\dfrac{v_{\text{top}}^2}{r}$
  correct: true
- id: p11q1-b
  content: |-
    $N=mg$ and $mg=m\dfrac{v_{\text{top}}^2}{r}$
- id: p11q1-c
  content: |-
    $N=0$ and $0=m\dfrac{v_{\text{top}}^2}{r}$
- id: p11q1-d
  content: |-
    $N$ must point outward and equal $mg$.
```

---

<a id="use-energy-from-bottom-to-top"></a>
## Use Energy from Bottom to Top

**Example:** A rider enters the bottom of a frictionless vertical loop of radius $R$ with speed $v_0$ and reaches the top with speed $v_{\text{top}}$. Write the energy equation connecting these speeds.

**Explanation**

Choose gravitational potential energy $0$ at the bottom of the loop. The top of the loop is $2R$ higher than the bottom, so the top has gravitational potential energy

$$
mg(2R).
$$

With rolling friction ignored, mechanical energy is conserved:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2+mg(2R).
$$

This equation says the entry kinetic energy must supply both the kinetic energy still needed at the top and the gravitational potential energy gained while rising.

```quiz
type: radio
id: p11-q2-energy-equation
shuffle: true
content: |-
  A cart enters a frictionless vertical loop of radius $r$ at the bottom with speed $v_0$ and reaches the top with speed $v_{\text{top}}$. Which energy equation correctly connects the two speeds?
options:
- id: p11q2-a
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2+mg(2r)$
  correct: true
- id: p11q2-b
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2+mgr$
- id: p11q2-c
  content: |-
    $\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2-mg(2r)$
- id: p11q2-d
  content: |-
    $v_0=v_{\text{top}}$ because the path is circular.
```

---

<a id="combine-the-two-conditions"></a>
## Combine the Two Conditions

**Example:** A rider enters a frictionless vertical loop of radius $R$ from the bottom. What entry speed gives the minimum speed for completing the loop?

**Explanation**

Start with the energy equation:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2+mg(2R).
$$

The unknown is the entry speed $v_0$. Treat $g$ and $R$ as given quantities, and replace $v_{\text{top}}^2$ using the contact condition.

At the minimum speed, the top contact condition gives

$$
v_{\text{top}}^2=gR.
$$

Substitute that into the energy equation:

$$
\dfrac12 mv_0^2=\dfrac12 m(gR)+2mgR.
$$

The right side has

$$
\dfrac12 mgR+2mgR=\dfrac52 mgR.
$$

So

$$
\dfrac12 mv_0^2=\dfrac52 mgR.
$$

Cancel $\dfrac12 m$ from both sides:

$$
v_0^2=5gR.
$$

Since speed is nonnegative,

$$
v_0=\sqrt{5gR}.
$$

```quiz
type: radio
id: p11-q3-combine
shuffle: true
content: |-
  A rider enters the bottom of a frictionless loop of radius $r$. At the minimum entry speed, $v_{\text{top}}^2=gr$. What is $v_0^2$ at the bottom?
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

<a id="match-the-answer-choices"></a>
## Match the Answer Choices

**Example:** Hony Tawk completes a circular loop-the-loop of radius $r$ and never leaves contact. What is the minimum speed required to enter the loop if rolling friction is ignored?

**Explanation**

The top contact condition gives the minimum top speed:

$$
v_{\text{top}}^2=gr.
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

The common trap is choosing only the top-speed condition, $\sqrt{gr}$, or forgetting that the rider rises by $2r$. In the given choices, $2\sqrt{gr}=\sqrt{4gr}$ is close, but it is still missing the extra $gr$ needed for the minimum top speed.

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

For a minimum-speed loop-the-loop question, test contact at the top first. At the minimum, $N=0$, so

$$
v_{\text{top}}^2=gr.
$$

Then use energy from the bottom to the top:

$$
\dfrac12 mv_0^2=\dfrac12 mv_{\text{top}}^2+mg(2r).
$$

Substituting $v_{\text{top}}^2=gr$ gives

$$
v_0=\sqrt{5gr}.
$$

The main trap is stopping at the top-speed condition or using a height change of only $r$ instead of $2r$.

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<Study-Guide.md>)

Next: [Finding the Critical Angle Where a Slider Leaves a Sphere](<Problem-13.md>)

Study guide index: 29/30

<!-- study-guide-nav:end -->
