# Direction of a Velocity Change in Circular Motion

<!--
lesson-id: 212-M1-072
topic-code: MTH212.M1.72
-->

## Table of Contents

- [Introduction](#introduction)
- [Reverse the Initial Velocity](#reverse-the-initial-velocity)
- [Read the Resultant by Components](#read-the-resultant-by-components)
- [Do Not Confuse Placement with Operation](#do-not-confuse-placement-with-operation)
- [Match the Source Diagram](#match-the-source-diagram)
- [Summary](#summary)

## Prerequisites

- Read a vector's direction from its arrowhead.
- Recognize the cardinal and diagonal compass directions.
- Add horizontal and vertical vector components independently.

---

<a id="introduction"></a>
## Introduction

An object in circular motion can keep the same speed while its velocity changes direction. If its initial and final velocities are $\vec v_1$ and $\vec v_2$, then the velocity change is

$$
\Delta \vec v=\vec v_2-\vec v_1.
$$

The order is final minus initial. The recognition cue is the subtraction $\vec v_2-\vec v_1$. Determine its direction by rewriting it as

$$
\vec v_2-\vec v_1=\vec v_2+(-\vec v_1).
$$

Use this visual sequence:

1. Read the direction of each arrow from its arrowhead.
2. Reverse the initial arrow to make $-\vec v_1$.
3. Add $\vec v_2$ and $-\vec v_1$ and name the resulting quadrant.

The arrows' locations on the page do not change the vectors they represent; a vector may be shifted without changing its magnitude or direction.

---

<a id="reverse-the-initial-velocity"></a>
## Reverse the Initial Velocity

Only the vector after the minus sign reverses.

$$
\underbrace{\vec v_2}_{\text{unchanged}}-\underbrace{\vec v_1}_{\text{reverse}}
=
\underbrace{\vec v_2}_{\text{unchanged}}+\underbrace{(-\vec v_1)}_{\text{opposite direction}}.
$$

**Example:** Suppose $\vec u_1$ points south and $\vec u_2$ points west. Which direction does $\vec u_2-\vec u_1$ point?

**Explanation**

Rewrite the difference:

$$
\vec u_2-\vec u_1=\vec u_2+(-\vec u_1).
$$

The final vector $\vec u_2$ still points west. Since $\vec u_1$ points south, $-\vec u_1$ points north. West plus north points northwest.

```quiz
type: radio
id: velocity-change-reverse-initial
shuffle: true
content: |-
  The initial velocity $\vec v_1$ points north, and the final velocity $\vec v_2$ points east. Which direction does $\vec v_2-\vec v_1$ point?
options:
- id: velocity-change-reverse-initial-ne
  content: Northeast
  feedback: |-
    Northeast would add east to the original northward $\vec v_1$. Subtraction reverses the initial velocity, so the vertical contribution is south, not north.
- id: velocity-change-reverse-initial-se
  content: Southeast
  correct: true
  feedback: |-
    A velocity change is final minus initial. Here $\vec v_2-\vec v_1$ is east plus the opposite of north, which is east plus south, so it points southeast.
- id: velocity-change-reverse-initial-sw
  content: Southwest
  feedback: |-
    Reversing $\vec v_1$ does create a southward component, but $\vec v_2$ remains eastward. There is no westward component, so the result is southeast rather than southwest.
- id: velocity-change-reverse-initial-nw
  content: Northwest
  feedback: |-
    Northwest has both components reversed. Only the subtracted initial velocity reverses; the final velocity $\vec v_2$ still supplies an eastward component.
- id: velocity-change-reverse-initial-none
  content: None of the above
  feedback: |-
    The difference has an eastward component from $\vec v_2$ and a southward component from $-\vec v_1$. Those components match the listed southeast direction.
```

---

<a id="read-the-resultant-by-components"></a>
## Read the Resultant by Components

Components provide a quick check on the compass direction. Take east as positive $x$ and north as positive $y$.

- $\Delta v_x>0$ means east, while $\Delta v_x<0$ means west.
- $\Delta v_y>0$ means north, while $\Delta v_y<0$ means south.

This check is equivalent to reversing and adding the arrows: compute

$$
(\Delta v_x,\Delta v_y)=(v_{2x}-v_{1x},v_{2y}-v_{1y})
$$

and read the signs.

**Example:** Let $\vec u_1=(4,0)$ point east and $\vec u_2=(0,-3)$ point south. Find the direction of $\vec u_2-\vec u_1$.

**Explanation**

Subtract corresponding components:

$$
\vec u_2-\vec u_1=(0,-3)-(4,0)=(-4,-3).
$$

The negative $x$-component points west, and the negative $y$-component points south. Therefore, the difference points southwest.

```quiz
type: radio
id: velocity-change-component-signs
shuffle: true
content: |-
  The initial velocity is $\vec v_1=(-5,0)$ and the final velocity is $\vec v_2=(0,2)$, where positive $x$ is east and positive $y$ is north. Which direction does $\vec v_2-\vec v_1$ point?
options:
- id: velocity-change-component-signs-ne
  content: Northeast
  correct: true
  feedback: |-
    Subtract components: $(0,2)-(-5,0)=(5,2)$. Both components are positive, so the velocity change points east and north: northeast.
- id: velocity-change-component-signs-se
  content: Southeast
  feedback: |-
    A southeast result would require a negative $y$-component. The final velocity supplies $+2$ in $y$, and the initial velocity has zero $y$-component, so the difference points north, not south.
- id: velocity-change-component-signs-sw
  content: Southwest
  feedback: |-
    Subtracting the initial $x$-component gives $0-(-5)=+5$, not $-5$. The double negative makes the horizontal component eastward, so the result cannot point southwest.
- id: velocity-change-component-signs-nw
  content: Northwest
  feedback: |-
    Northwest keeps the initial vector's westward direction instead of reversing it. Because $\vec v_1$ is subtracted, its westward component becomes an eastward contribution.
- id: velocity-change-component-signs-none
  content: None of the above
  feedback: |-
    The difference $(5,2)$ has nonzero eastward and northward components, which is exactly the listed northeast direction.
```

---

<a id="do-not-confuse-placement-with-operation"></a>
## Do Not Confuse Placement with Operation

Two arrows may be drawn head-to-tail, but that placement does not decide which algebraic operation the question asks for. The visible arrow from the first tail to the final head represents the sum in the order drawn. A minus sign still requires reversing the vector after it.

**Example:** Suppose $\vec u_1$ points north. From its head, $\vec u_2$ is drawn pointing west. The visible start-to-finish path points northwest, which represents $\vec u_1+\vec u_2$. What direction does $\vec u_2-\vec u_1$ point?

**Explanation**

Follow the written expression instead of tracing the visible path:

$$
\vec u_2-\vec u_1=\text{west}+\text{south}.
$$

The difference points southwest. The northwest direction belongs to the sum $\vec u_1+\vec u_2$.

```quiz
type: radio
id: velocity-change-head-to-tail-trap
shuffle: true
content: |-
  A diagram draws $\vec v_1$ westward and then draws $\vec v_2$ northward from the head of $\vec v_1$. Which direction does $\vec v_2-\vec v_1$ point?
options:
- id: velocity-change-head-to-tail-trap-ne
  content: Northeast
  correct: true
  feedback: |-
    The requested difference is $\vec v_2+(-\vec v_1)$. North stays north, while the opposite of west is east, so the result points northeast.
- id: velocity-change-head-to-tail-trap-se
  content: Southeast
  feedback: |-
    Reversing the westward initial vector does produce an eastward component, but the final velocity remains northward. The vertical component is north, so the result is northeast rather than southeast.
- id: velocity-change-head-to-tail-trap-sw
  content: Southwest
  feedback: |-
    Southwest reverses the final velocity instead of the initial velocity. In $\vec v_2-\vec v_1$, $\vec v_2$ remains northward and only $\vec v_1$ reverses.
- id: velocity-change-head-to-tail-trap-nw
  content: Northwest
  feedback: |-
    Northwest is the visible start-to-finish direction of the head-to-tail sum $\vec v_1+\vec v_2$. The question asks for a difference, so the westward $\vec v_1$ must first reverse to east.
- id: velocity-change-head-to-tail-trap-none
  content: None of the above
  feedback: |-
    North from $\vec v_2$ plus east from $-\vec v_1$ gives the listed northeast direction.
```

---

<a id="match-the-source-diagram"></a>
## Match the Source Diagram

The same reverse-then-add move applies directly to the circular-motion vector diagram.

**Example:** If an initial velocity points west and the final velocity points south, then

$$
\vec v_2-\vec v_1=\text{south}+\text{east},
$$

so the velocity change points southeast.

**Explanation**

Read each original arrow from its arrowhead, reverse only $\vec v_1$, and then combine the horizontal and vertical directions. As a check, the component signs must name the same quadrant. Use the compass rose to report the answer in the source problem's requested form.

```quiz
type: radio
id: khadley-circular-motion-q1
shuffle: true
content: |-
  **Question 1**

  Which direction does $\vec v_2-\vec v_1$ point?

  ![](<../Source/Images/vectors-1.jpg>)

  ![](<../Source/Images/nsew.jpg>)
options:
- id: ne
  content: Northeast
  feedback: |-
    Subtraction means adding $-\vec v_1$. Combining a southward $\vec v_2$ with a westward $-\vec v_1$ cannot produce a northeast result.
- id: se
  content: Southeast
  feedback: |-
    Southeast is the visible start-to-finish direction of the sum $\vec v_1+\vec v_2$. In the requested difference, subtraction reverses the eastward $\vec v_1$, so the horizontal component points west rather than east.
- id: sw
  content: Southwest
  correct: true
  feedback: |-
    Write $\vec v_2-\vec v_1=\vec v_2+(-\vec v_1)$. The final velocity points south and the opposite of the initial eastward velocity points west, so the difference points southwest.
- id: nw
  content: Northwest
  feedback: |-
    The westward component is correct because $\vec v_1$ reverses, but the vertical contribution comes from the unchanged southward $\vec v_2$. The result points south, not north.
- id: none
  content: None of the above
  feedback: |-
    The difference has both a westward component and a southward component, which is exactly the listed southwest direction.
```

---

<a id="summary"></a>
## Summary

When the question asks for the direction of $\vec v_2-\vec v_1$:

1. Keep the final velocity $\vec v_2$ unchanged.
2. Reverse the initial velocity to form $-\vec v_1$.
3. Add $\vec v_2+(-\vec v_1)$.
4. Check the horizontal and vertical component signs.
5. Name the compass direction requested by the problem.

The arrow method and the component-sign check should agree. The main trap is tracing a head-to-tail diagram as though the question asked for $\vec v_1+\vec v_2$. The written minus sign controls the operation.
