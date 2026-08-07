# Reading Path Difference from a Double-Slit Pattern

## Table of Contents

- [Introduction](#introduction)
- [Bright Fringes Use Whole Wavelengths](#bright-fringes-use-whole-wavelengths)
- [Count from the Central Maximum](#count-from-the-central-maximum)
- [Separate Bright and Dark Fringes](#separate-bright-and-dark-fringes)
- [Name the Longer Path](#name-the-longer-path)
- [Summary](#summary)

## Prerequisites

- Interpret $\lambda$ as one wavelength.
- Distinguish constructive interference (bright) from destructive interference (dark).
- Count equally spaced bands outward from a central reference band.

---

<a id="introduction"></a>
## Introduction

When a double-slit problem marks a band and asks for a path difference, first identify whether the band is bright or dark and then count its order from the central maximum. The reusable quantity is the difference between the two slit-to-point path lengths:

$$
\Delta r=|r_L-r_R|.
$$

Bright fringes occur when the two waves arrive an integer number of wavelengths apart:

$$
\Delta r=m\lambda,\qquad m=0,1,2,\ldots
$$

The central maximum is the zeroth-order bright fringe, so counting begins with $m=0$, not $m=1$.

Read a marked pattern in three passes:

| Cue | Decision | What it controls |
| --- | --- | --- |
| Bright or dark band | Choose the interference condition | Whole or half-integer multiples of $\lambda$ |
| Number of bands from the center | Determine the fringe order | Magnitude of $\Delta r$ |
| Left or right of center | Identify the farther slit | Which slit-to-point path is longer |

---

<a id="bright-fringes-use-whole-wavelengths"></a>
## Bright Fringes Use Whole Wavelengths

**Example:** A point lies at the third-order bright fringe. What is the path-length difference?

**Explanation**

A bright fringe uses $\Delta r=m\lambda$. Third order means $m=3$, so

$$
\Delta r=3\lambda.
$$

The word *bright* selects whole-number multiples of $\lambda$; the order supplies the whole number. Moving from one bright band to the next changes $\Delta r$ by exactly one wavelength, so the bright-fringe orders form the sequence $0\lambda,1\lambda,2\lambda,\ldots$.

```quiz
type: radio
id: p3-bright-order-q1
content: |-
  A point is on the fourth-order bright fringe of a double-slit pattern. What is the magnitude of its path difference?
options:
- id: p3-bright-order-q1-a
  content: |-
    $0.5\lambda$
  feedback: |-
    A half-wavelength path difference produces the first dark fringe. A bright fringe requires an integer multiple of $\lambda$, and fourth order uses the integer $4$.
- id: p3-bright-order-q1-b
  content: |-
    $2\lambda$
  feedback: |-
    The coefficient is the bright-fringe order. $2\lambda$ belongs to the second-order bright fringe, while this point is fourth order.
- id: p3-bright-order-q1-c
  content: |-
    $3.5\lambda$
  feedback: |-
    Half-integer multiples correspond to dark fringes. Because the point is bright, use $\Delta r=m\lambda$ with the integer order $m=4$.
- id: p3-bright-order-q1-d
  content: |-
    $4\lambda$
  correct: true
  feedback: |-
    Bright fringes satisfy $\Delta r=m\lambda$. Here $m=4$, so the path difference has magnitude $\Delta r=4\lambda$.
- id: p3-bright-order-q1-e
  content: |-
    $4.5\lambda$
  feedback: |-
    Adding one-half switches from constructive to destructive interference. The fourth bright fringe is at $4\lambda$; $4.5\lambda$ is a dark-fringe condition.
```

---

<a id="count-from-the-central-maximum"></a>
## Count from the Central Maximum

**Example:** Starting at the central maximum, a marked point lies on the first bright band encountered to the right. What is its order and path difference?

**Explanation**

The central maximum itself is $m=0$. The next bright band is therefore $m=1$, so

$$
\Delta r=1\lambda.
$$

Do not count the central maximum as the first-order band. Use it as the zero reference, then count bright bands outward: $0,1,2,3,\ldots$.

A reliable reading chain is **anchor → jumps → index**:

- **Anchor:** label the central maximum $m=0$.
- **Jumps:** count only bright-to-bright steps toward the marked bright band.
- **Index:** the number of jumps is $m$, and therefore $\Delta r=m\lambda$.

```quiz
type: radio
id: p3-count-center-q1
content: |-
  A marked point lies on the third bright band to the left of the central maximum. Which order and path-difference magnitude describe it?
options:
- id: p3-count-center-q1-a
  content: |-
    $m=0$ and $\Delta r=0$
  feedback: |-
    Only the central maximum has $m=0$ and zero path difference. Moving to the third bright band gives three whole-wavelength steps from that reference.
- id: p3-count-center-q1-b
  content: |-
    $m=1$ and $\Delta r=\lambda$
  feedback: |-
    This describes the first bright band adjacent to the central maximum. The prompt identifies the third bright band, so continue counting to $m=3$.
- id: p3-count-center-q1-c
  content: |-
    $m=2$ and $\Delta r=2\lambda$
  feedback: |-
    This result stops one band too early. With the center labeled $m=0$, the first, second, and third outward bright bands have $m=1,2,3$.
- id: p3-count-center-q1-d
  content: |-
    $m=3$ and $\Delta r=3\lambda$
  correct: true
  feedback: |-
    The central maximum is order zero, and the third bright band outward is $m=3$. Bright fringes obey $\Delta r=m\lambda$, giving $\Delta r=3\lambda$.
- id: p3-count-center-q1-e
  content: |-
    $m=3$ and $\Delta r=3.5\lambda$
  feedback: |-
    The order was counted correctly, but a half-integer path difference is dark. A third-order bright fringe uses the integer multiple $3\lambda$.
```

---

<a id="separate-bright-and-dark-fringes"></a>
## Separate Bright and Dark Fringes

**Example:** A point has path difference $1.5\lambda$. Is it on a bright or dark fringe?

**Explanation**

Dark fringes occur at half-integer multiples:

$$
\Delta r=\left(m+\frac12\right)\lambda,\qquad m=0,1,2,\ldots
$$

Because $1.5\lambda=(1+\tfrac12)\lambda$, the point lies on the second dark fringe. The neighboring bright fringes are at $1\lambda$ and $2\lambda$.

| Marked band | Path-difference condition | First values outward from center |
| --- | --- | --- |
| Bright | $\Delta r=m\lambda$ | $0,1\lambda,2\lambda,3\lambda,\ldots$ |
| Dark | $\Delta r=(m+\tfrac12)\lambda$ | $0.5\lambda,1.5\lambda,2.5\lambda,\ldots$ |

The dark-fringe formula labels the first dark fringe with $m=0$, even though it occurs at $0.5\lambda$. This is why it is safer to classify the band before assigning a coefficient.

```quiz
type: radio
id: p3-bright-dark-q1
content: |-
  Which path difference places a point on the third dark fringe from the central maximum?
options:
- id: p3-bright-dark-q1-a
  content: |-
    $1.5\lambda$
  feedback: |-
    Dark fringes occur at $0.5\lambda,1.5\lambda,2.5\lambda,\ldots$. Thus $1.5\lambda$ is the second dark fringe, one dark band too close to the center.
- id: p3-bright-dark-q1-b
  content: |-
    $2\lambda$
  feedback: |-
    Integer multiples of $\lambda$ produce bright fringes. $2\lambda$ is the second-order bright fringe, not a dark fringe.
- id: p3-bright-dark-q1-c
  content: |-
    $2.5\lambda$
  correct: true
  feedback: |-
    Dark fringes begin at $0.5\lambda$ and increase by one wavelength. The third dark fringe is therefore $0.5\lambda+2\lambda=2.5\lambda$.
- id: p3-bright-dark-q1-d
  content: |-
    $3\lambda$
  feedback: |-
    A whole-number multiple gives constructive interference. $3\lambda$ identifies the third-order bright fringe; the third dark fringe lies halfway between $2\lambda$ and $3\lambda$.
- id: p3-bright-dark-q1-e
  content: |-
    $3.5\lambda$
  feedback: |-
    This is a dark-fringe value, but it is the fourth dark fringe: $0.5,1.5,2.5,3.5$. The third occurs at $2.5\lambda$.
```

---

<a id="name-the-longer-path"></a>
## Name the Longer Path

**Example:** A point is on the first-order bright fringe to the left of center. Which slit-to-point path is longer, and by how much?

**Explanation**

A point on the left side is closer to the left slit and farther from the right slit. First-order bright means a magnitude of $\lambda$, so the path from the right slit is longer by $\lambda$.

For a point on the right side, reverse the slit names: the path from the left slit is longer. Keep the two roles separate:

- **Magnitude:** the fringe type and order determine *by how much* the paths differ.
- **Path identity:** the side of the pattern determines *which* slit-to-point path is longer.

```quiz
type: radio
id: p3-source-pattern-q1
shuffle: true
content: |-
  A laboratory experiment produces a double-slit interference pattern on a screen. The marked point is how much farther from the left slit than from the right slit?

  ![](<../Source/Images/double-slit-second-order-bright-fringe-dot.png>)
options:
- id: p3-source-pattern-q1-a
  content: |-
    $0.5\lambda$
  feedback: |-
    A path difference of $0.5\lambda$ produces the first dark fringe. The marked point lies on a bright band, so its path difference must be an integer multiple of $\lambda$.
- id: p3-source-pattern-q1-b
  content: |-
    $1.0\lambda$
  feedback: |-
    The first bright band next to the central maximum has path difference $1.0\lambda$. The dot lies on the next bright band outward, so it is second order.
- id: p3-source-pattern-q1-c
  content: |-
    $1.5\lambda$
  feedback: |-
    A half-integer multiple produces destructive interference. Although $1.5\lambda$ lies between the first- and second-order bright conditions, the dot is centered on a bright band.
- id: p3-source-pattern-q1-d
  content: |-
    $2.0\lambda$
  correct: true
  feedback: |-
    Bright fringes satisfy $\Delta r=m\lambda$. The dot is on the second bright band to the right of the central maximum, so $m=2$; on the right side the left-slit path is longer, here by $2.0\lambda$.
- id: p3-source-pattern-q1-e
  content: |-
    $2.5\lambda$
  feedback: |-
    A half-integer path difference produces a dark band. $2.5\lambda$ is the third dark-fringe condition, whereas the marked point is on the second bright band.
- id: p3-source-pattern-q1-f
  content: |-
    $3.0\lambda$
  feedback: |-
    This is an integer multiple and therefore bright, but it corresponds to the third-order bright fringe. The dot is one bright band closer to the center, at second order.
```

---

<a id="summary"></a>
## Summary

When a double-slit pattern marks a point, use this procedure:

1. **Classify:** decide whether the marked band is bright or dark.
2. **Anchor:** find the central maximum and label it $m=0$.
3. **Count:** move outward band by band to determine the order.
4. **Convert:** use $\Delta r=m\lambda$ for bright fringes or $\Delta r=(m+\tfrac12)\lambda$ for dark fringes.
5. **Name:** use the side of the pattern to identify the longer path—on the right, the left-slit path is longer; on the left, the right-slit path is longer.

The main trap is mixing the two counting systems: bright fringes use whole wavelengths, while dark fringes lie halfway between them.
