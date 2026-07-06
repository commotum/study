# Finding the Radius from an Angled String

<!--
lesson-id: 212-M1-027
topic-code: MTH212.M1.27
-->

## Table of Contents

- [Introduction](#introduction)
- [Turn the Side View Into a Right Triangle](#turn-the-side-view-into-a-right-triangle)
- [Choose Cosine When the Angle Starts at the Horizontal](#choose-cosine-when-the-angle-starts-at-the-horizontal)
- [Do Not Swap the Reference Line](#do-not-swap-the-reference-line)
- [Apply the Rule to the Conical Pendulum](#apply-the-rule-to-the-conical-pendulum)
- [Summary](#summary)

## Prerequisites

- Identify the hypotenuse and the adjacent side in a right triangle.
- Use $\cos\theta=\dfrac{\text{adjacent}}{\text{hypotenuse}}$.
- Recognize that the radius of circular motion is the horizontal distance from the rotation axis to the object.

---

<a id="introduction"></a>
## Introduction

When a bob moves in a horizontal circle on a string, the radius of the circular path is not the whole string length. In the side view, the string is the hypotenuse of a right triangle, and the radius is the horizontal leg.

For this problem, the cue is that the string makes an angle $\theta$ with the horizontal. That makes the circular radius adjacent to $\theta$, so the radius comes from cosine.

---

<a id="turn-the-side-view-into-a-right-triangle"></a>
## Turn the Side View Into a Right Triangle

**Example:** A string of length $L$ holds a bob below a ceiling. The string makes an angle $\theta$ with the horizontal ceiling. Let $r$ be the horizontal distance from the point directly below the pivot to the bob. Which part of the right triangle is $r$?

**Explanation**

In the side view, imagine drawing a vertical line down from the pivot and a horizontal line from that vertical line to the bob. Those two legs meet at a right angle.

- The string has length $L$, so it is the hypotenuse.
- The horizontal leg is the distance from the center line to the bob, so it is the radius $r$.
- Because $\theta$ is measured from the horizontal, $r$ touches the angle $\theta$.

So $r$ is the side adjacent to $\theta$.

```quiz
type: radio
id: p2-q1
content: |-
  A string of length $8$ makes an angle $\theta$ with a horizontal support. The bob is at the lower end of the string. Which side of the side-view right triangle is the horizontal radius?
options:
- id: a
  content: |-
    The hypotenuse, because the string itself is circular
- id: b
  content: |-
    The adjacent leg to $\theta$
  correct: true
- id: c
  content: |-
    The opposite leg to $\theta$
- id: d
  content: |-
    The full string length $8$
```

---

<a id="choose-cosine-when-the-angle-starts-at-the-horizontal"></a>
## Choose Cosine When the Angle Starts at the Horizontal

**Example:** A string of length $12$ cm makes an angle of $35^\circ$ with the horizontal. Find the horizontal radius $r$ in terms of trig functions.

**Explanation**

The given string length is the hypotenuse, and the horizontal radius is adjacent to the given angle. Cosine relates adjacent side to hypotenuse:

$$
\cos 35^\circ=\frac{r}{12}.
$$

Solve for $r$:

$$
r=12\cos 35^\circ.
$$

The key is the phrase "with the horizontal." If the angle is measured from the horizontal, the horizontal leg is adjacent, not opposite.

```quiz
type: radio
id: p2-q2
content: |-
  A string of length $L$ makes an angle $\alpha$ with the horizontal. The bob moves in a horizontal circle. Which expression gives the radius of the circular path?
options:
- id: a
  content: |-
    $L$
- id: b
  content: |-
    $L\sin\alpha$
- id: c
  content: |-
    $L\cos\alpha$
  correct: true
- id: d
  content: |-
    $L\tan\alpha$
```

---

<a id="do-not-swap-the-reference-line"></a>
## Do Not Swap the Reference Line

**Example:** A string of length $L$ makes an angle $\phi$ with the vertical. The bob moves in a horizontal circle. Which expression gives the radius $r$?

**Explanation**

The string is still the hypotenuse, and the radius is still the horizontal leg. The difference is the reference angle.

If $\phi$ is measured from the vertical, then the horizontal radius is opposite $\phi$, not adjacent to it. That gives

$$
\sin\phi=\frac{r}{L}
$$

so

$$
r=L\sin\phi.
$$

This does not contradict the previous rule. It shows why the wording "with the horizontal" matters.

```quiz
type: radio
id: p2-q3
content: |-
  A string of length $L$ makes an angle $\beta$ with the vertical. The bob moves in a horizontal circle. Which expression gives the radius of the circular path?
options:
- id: a
  content: |-
    $L\cos\beta$
- id: b
  content: |-
    $L\sin\beta$
  correct: true
- id: c
  content: |-
    $L\tan\beta$
- id: d
  content: |-
    $L$
```

---

<a id="apply-the-rule-to-the-conical-pendulum"></a>
## Apply the Rule to the Conical Pendulum

**Example:** A conical pendulum has string length $L$. The string makes an angle $\theta$ with the horizontal, and the bob travels in a horizontal circle. What is the radius of the circular trajectory?

![](<../Source/Images/conical-pendulum-diagram.png>)

**Explanation**

The top view shows the circular path, but the side view tells us its radius. The radius is the horizontal distance from the rotation axis to the bob.

In the side-view triangle:

- hypotenuse: $L$
- adjacent side to $\theta$: $r$
- opposite side to $\theta$: the vertical drop

Therefore,

$$
\cos\theta=\frac{r}{L}
$$

and

$$
r=L\cos\theta.
$$

This also passes a quick check: if $\theta$ were very small, the string would be nearly horizontal and the radius would be close to $L$, just like $L\cos\theta$.

```quiz
type: radio
id: p2-q4
content: |-
  The figures below show a bob of mass $m$ attached to a light string of length $L$ which traverses a circular trajectory when viewed from above/below.

  The string makes an angle $\theta$ with the horizontal and the period of the circular motion is $T$ (constant).

  What is the radius of the circular trajectory?

  ![](<../Source/Images/conical-pendulum-diagram.png>)
options:
- id: a
  content: |-
    $L$
- id: b
  content: |-
    $L\cos\theta$
  correct: true
- id: c
  content: |-
    $L\sin\theta$
- id: d
  content: |-
    $L\tan\theta$
```

---

<a id="summary"></a>
## Summary

When the string length is $L$ and the angle $\theta$ is measured from the horizontal, the radius is the horizontal projection of the string:

$$
r=L\cos\theta.
$$

Use cosine because the radius is adjacent to the angle. The main trap is choosing $L\sin\theta$, which would be the vertical projection when the angle is measured from the horizontal.

<!-- study-guide-nav:start -->

---

## Study Guide Navigation

Study guide: [212 Study Guide](<../../../study-guide.md>)

Next: [Deriving the Angle in a Conical Pendulum](<Problem-5.md>)

<!-- study-guide-nav:end -->

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]
