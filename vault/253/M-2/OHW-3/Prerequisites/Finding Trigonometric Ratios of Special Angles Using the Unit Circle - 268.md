# Finding Trigonometric Ratios of Special Angles Using the Unit Circle

<!--
lesson-id: 268
topic-code: MF2.9.4.3
-->

## Table of Contents

- [Introduction](#introduction)
- [A Method For Constructing the Other Quadrants](#a-method-for-constructing-the-other-quadrants)
- [Finding the Sine or Cosine of a Special Angle Given in Degrees](#finding-the-sine-or-cosine-of-a-special-angle-given-in-degrees)
- [Finding the Sine or Cosine of a Special Angle Given in Radians](#finding-the-sine-or-cosine-of-a-special-angle-given-in-radians)
- [Finding the Secant or Cosecant of a Special Angle](#finding-the-secant-or-cosecant-of-a-special-angle)
- [Finding the Tangent or Cotangent of a Special Angle](#finding-the-tangent-or-cotangent-of-a-special-angle)

## Prerequisites

- [Finding Trigonometric Ratios of Quadrantal Angles](<../../../../MA/Mathematical-Foundations/MF2/9. Trigonometry/9.4. Special Trigonometric Ratios/Lessons/9.4.1. Finding Trigonometric Ratios of Quadrantal Angles.md>)
- [Introduction to Sequences](<../../../../MA/Mathematical-Foundations/MF2/7. Sequences/7.1. Introduction to Sequences/Lessons/7.1.1. Introduction to Sequences.md>)

---

<a id="introduction"></a>
## Introduction

The unit circle provides a convenient way to represent the sine and cosine of special angles in each quadrant.

We first recall the following:

- The $x$-coordinate of any point on the unit circle equals the *cosine* of the corresponding central angle, and
- the $y$-coordinate equals the *sine* of the corresponding central angle.

Let's use the unit circle to list the special values of sine and cosine, starting with the first quadrant. First, we mark off the special angles in this quadrant.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/ed8cf89ecc6ef7248f6e1e1029756cb3.png>)

Now, let's write down each point's $x$- and $y$-coordinates, corresponding to the cosine and sine of each point's central angle. In addition, we'll highlight the $y$-coordinate at each point.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/b2a47ec4428587635cc4bebfd85b5c14.png>)

Before we move on, observe that if we rotate counterclockwise from the positive $x$-axis, we see that the $y$-coordinates at the special angles are given by the following sequence:

$$
f(n) = \dfrac{\sqrt n}{2}, \qquad n=0,1,2,3,4
$$

as shown below.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/283f91d6a58eac8e6d515f55f6c8f4d7.png>)

There is a similar pattern for the $x$-coordinates (corresponding to the cosine of the central angle). The only difference is that now we go in reverse, from $90^\circ$ to $0^\circ$, as shown below

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/aa8f1b7bb4657357505f5c304fe968a6.png>)

Take a moment to ensure you can reproduce this diagram on your own without looking. We'll add to it shortly.

---

<a id="a-method-for-constructing-the-other-quadrants"></a>
## A Method For Constructing the Other Quadrants

So, we know how the unit circle can be used to list the cosine and sine of the special angles in the *first* quadrant. But what about the other quadrants?

The values in the remaining quadrants can be obtained from the coordinates in the first quadrant. Let's see how:

- To obtain the points in the *second* quadrant, let's first mark off the special angles in this quadrant. These angles have the same reference angles as the angles in the first quadrant:$180^\circ - 30^\circ = 150^\circ$ $180^\circ - 45^\circ = 135^\circ$ $180^\circ - 60^\circ = 120^\circ$ We mark these angles below and include the quadrantal angle $180^\circ$.![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/695244e52d48f5aecee1945a6ff9431c.png>)
Now, we reflect the coordinates in the first quadrant in the $y$-axis. This changes the sign of the $x$-coordinate at each point and leaves the $y$-coordinate unchanged.![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/9b127a2591c147e1eafa071bb07ac258.png>)
- To obtain the points in the third quadrant, we first find the special angles in this quadrant. Again, these angles have the same reference angles as the special angles in the first quadrant:$180^\circ + 30^\circ = 210^\circ$ $180^\circ + 45^\circ = 225^\circ$ $180^\circ + 60^\circ = 240^\circ$ Then, we take the points in the second quadrant and reflect them in the $x$-axis. This changes the sign of the $y$-coordinate at each point and leaves the $x$-coordinate unchanged.![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/569e59e0c4b6a35d0ad48c17def1e2f0.png>)
- Finally, to obtain the points in the fourth quadrant, we first compute the special angles in this quadrant:$360^\circ - 30^\circ = 330^\circ$ $360^\circ - 45^\circ = 315^\circ$ $360^\circ - 60^\circ = 300^\circ$ Then, we take the points in the first quadrant and reflect them in the $x$-axis. This changes the sign of the $y$-coordinate at each point and leaves the $x$-coordinate unchanged.![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/30edde29a62e06b92db6641e803f3103.png>)

Therefore, our complete unit circle is as follows.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/7bbc48142296cc0620cfd299962427b0.png>)

Take a moment to ensure you can create this diagram yourself without looking. We'll be referring to it often!

---

<a id="finding-the-sine-or-cosine-of-a-special-angle-given-in-degrees"></a>
## Finding the Sine or Cosine of a Special Angle Given in Degrees

**Example:** What is the value of $\cos 225^\circ$?

**Explanation**

Let's remind ourselves of the special trigonometric ratios, as given by the unit circle.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/94ef4796a49139d82a9ada453d523c3b.png>)

From the unit circle, we see that the angle $225^\circ$ corresponds to the point

$$
\left(-\dfrac{\sqrt{2}}{2}, -\dfrac{\sqrt{2}}{2} \right)
$$

Since the cosine of the angle corresponds to the $x$-coordinate, we have

$$
\cos 225^\circ = -\dfrac{\sqrt{2}}{2}
$$

---

**Question 1:**

```quiz
type: radio
id: ma-23387
content: |-
  What is $\cos 120^{∘}$?
options:
- id: a
  content: |-
    $-1$
- id: b
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: c
  content: |-
    $-\frac{1}{2}$
  correct: true
- id: d
  content: |-
    $-\frac{\sqrt{2}}{2}$
- id: e
  content: |-
    $\frac{1}{2}$
```

---

**Question 2:**

```quiz
type: radio
id: ma-23388
content: |-
  What is $\sin 330^{∘}$?
options:
- id: a
  content: |-
    $-\frac{\sqrt{3}}{2}$
- id: b
  content: |-
    $-\frac{1}{\sqrt{2}}$
- id: c
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: d
  content: |-
    $-\frac{1}{2}$
  correct: true
- id: e
  content: |-
    $\frac{\sqrt{2}}{2}$
```

---

<a id="finding-the-sine-or-cosine-of-a-special-angle-given-in-radians"></a>
## Finding the Sine or Cosine of a Special Angle Given in Radians

**Example:** What is the value of $\sin \left(\dfrac {7\pi} 4\right)$?

**Explanation**

Let's remind ourselves of the special trigonometric ratios, as given by the unit circle.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/dd30285d4f7fd51565aefe260650a5b2.png>)

From the unit circle, we see that the angle

$$
\dfrac{7\pi}{4}
$$

corresponds to the point

$$
\left(\dfrac{\sqrt{2}}{2}, -\dfrac{\sqrt{2}}{2} \right)
$$

Since the sine of the angle corresponds to the $y$-coordinate, we have

$$
\sin \left(\dfrac {7\pi} 4\right) = -\dfrac {\sqrt 2} 2
$$

---

**Question 3:**

```quiz
type: radio
id: ma-1695
content: |-
  What is $\sin (\frac{4π}{3})$?
options:
- id: a
  content: |-
    $\frac{2\sqrt{3}}{3}$
- id: b
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: c
  content: |-
    $-\frac{\sqrt{3}}{2}$
  correct: true
- id: d
  content: |-
    $-\frac{2\sqrt{3}}{3}$
- id: e
  content: |-
    $\frac{3\sqrt{2}}{4}$
```

---

**Question 4:**

```quiz
type: radio
id: ma-1684
content: |-
  What is $\cos (\frac{3π}{4})$?
options:
- id: a
  content: |-
    $\frac{\sqrt{2}}{2}$
- id: b
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: c
  content: |-
    $-\frac{\sqrt{2}}{2}$
  correct: true
- id: d
  content: |-
    $\frac{-1}{2}$
- id: e
  content: |-
    $-\frac{\sqrt{3}}{2}$
```

---

<a id="finding-the-secant-or-cosecant-of-a-special-angle"></a>
## Finding the Secant or Cosecant of a Special Angle

**Example:** Find the value of $\csc 120^\circ$.

**Explanation**

Let's remind ourselves of the special trigonometric ratios, as given by the unit circle.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/fc6ed311842488b636362d1c36d3acdd.png>)

From the unit circle, we see that the angle $120^\circ$ corresponds to the point

$$
\left(-\dfrac{1}{2}, \dfrac{\sqrt{3}}{2} \right)
$$

Since the sine of the angle corresponds to the $y$-coordinate, we have

$$
\sin 120^\circ= \dfrac{\sqrt 3}{2}
$$

Therefore, using the fact that

$$
\csc{\theta} = \dfrac{1}{\sin\theta}
$$

we have

$$
\csc 120^\circ = \dfrac{1}{\sin 120^\circ} = \dfrac{2}{\sqrt 3} = \dfrac{2\sqrt 3}{3}
$$

---

**Question 5:**

```quiz
type: radio
id: ma-86323
content: |-
  What is $\csc 225^{∘}$?
options:
- id: a
  content: |-
    $-\sqrt{2}$
  correct: true
- id: b
  content: |-
    $\frac{\sqrt{3}}{2}$
- id: c
  content: |-
    $\frac{\sqrt{2}}{3}$
- id: d
  content: |-
    $\frac{\sqrt{2}}{2}$
- id: e
  content: |-
    $\sqrt{3}$
```

---

**Question 6:**

```quiz
type: radio
id: ma-64948
content: |-
  What is $\sec (\frac{2π}{3})$?
options:
- id: a
  content: |-
    $\frac{2}{\sqrt{3}}$
- id: b
  content: |-
    $-1$
- id: c
  content: |-
    $-2$
  correct: true
- id: d
  content: |-
    $-\frac{1}{2}$
- id: e
  content: |-
    $\frac{2\sqrt{3}}{3}$
```

---

<a id="finding-the-tangent-or-cotangent-of-a-special-angle"></a>
## Finding the Tangent or Cotangent of a Special Angle

**Example:** Find the value of $\tan \left(\dfrac {4 \pi} 3\right)$.

**Explanation**

Let's remind ourselves of the special trigonometric ratios, as given by the unit circle.

![](<../Source/Finding Trigonometric Ratios of Special Angles Using the Unit Circle - 268/Images/d040fbae600c923d0af40dd7e9cec2e0.png>)

From the unit circle, we see that the angle

$$
\dfrac{4\pi}{3}
$$

corresponds to the point

$$
\left(-\dfrac{1}{2}, -\dfrac{\sqrt{3}}{2} \right)
$$

- Since the cosine of the angle corresponds to the $x$-coordinate, we have $\cos\left(\dfrac {4\pi} {3}\right) = -\dfrac 1 2$.
- Since the sine of the angle corresponds to the $y$-coordinate, we have $\sin\left(\dfrac {4\pi} {3}\right) = -\dfrac {\sqrt 3} 2$.

Therefore, using the fact that

$$
\tan{\theta} = \dfrac{\sin\theta}{\cos\theta}
$$

we have

$$
\tan\left(\dfrac{4\pi}{3}\right) = \dfrac{\sin{\left(\dfrac{4\pi}{3}\right)}}{\cos{\left(\dfrac{4\pi}{3}\right)}} = \dfrac{\left(-\dfrac {\sqrt 3} 2\right)}{\left(-\dfrac 1 2\right)} = \sqrt{3}
$$

---

**Question 7:**

```quiz
type: radio
id: ma-64945
content: |-
  What is $\cot (\frac{π}{3})$?
options:
- id: a
  content: |-
    $\sqrt{3}$
- id: b
  content: |-
    $-\sqrt{3}$
- id: c
  content: |-
    $1$
- id: d
  content: |-
    $-\frac{1}{\sqrt{3}}$
- id: e
  content: |-
    $\frac{1}{\sqrt{3}}$
  correct: true
```

---

**Question 8:**

```quiz
type: radio
id: ma-1692
content: |-
  What is $\tan (\frac{5π}{6})$?
options:
- id: a
  content: |-
    $-\frac{\sqrt{3}}{3}$
  correct: true
- id: b
  content: |-
    $\frac{\sqrt{3}}{3}$
- id: c
  content: |-
    $-1$
- id: d
  content: |-
    $-\frac{\sqrt{2}}{2}$
- id: e
  content: |-
    $-\frac{\sqrt{3}}{2}$
```

```update-progress
```

[[253/Home|Home]]
[[253/0. Table of Contents/TOC|Table of Contents]]
