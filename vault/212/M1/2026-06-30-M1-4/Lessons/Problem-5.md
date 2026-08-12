# Choosing Friction Direction on a Banked Curve

<!--
lesson-id: 212-M1-023
topic-code: MTH212.M1.23
-->

## Table of Contents

- [Introduction](#introduction)
- [Match the No-Friction Speed](#match-the-no-friction-speed)
- [Handle a Speed That Is Too High](#handle-a-speed-that-is-too-high)
- [Handle a Speed That Is Too Low](#handle-a-speed-that-is-too-low)
- [Return to the Faster Car](#return-to-the-faster-car)
- [Summary](#summary)

## Prerequisites

- Radial acceleration points horizontally toward the center of the curve.
- The normal force is perpendicular to the road surface.
- Static friction points along the road surface and opposes the direction the tires would slip.
- At the no-friction banked-curve speed, the horizontal component of the normal force supplies exactly the required inward net force.

---

<a id="introduction"></a>
## Introduction

A car safely rounds an icy banked curve at its no-friction design speed $v_0$. After the ice melts, the tires can exert static friction on the road. If the car now travels at speed $v>v_0$, which way does the friction force point?

![](<../Source/Images/banked-curve-car-diagram.png>)

Friction does not automatically point backward along the car's motion. Static friction opposes the tires' tendency to slip across the road surface. At speed $v_0$, the bank angle is matched to the circular motion: the normal force supplies exactly the required inward force, and no friction is needed. A faster car requires more inward force and would otherwise slide up the bank toward the outside of the curve. Static friction therefore points down the slope, adding an inward component.

---

<a id="match-the-no-friction-speed"></a>
## Match the No-Friction Speed

**Example:** A car travels around an icy banked curve at the design speed $v_0$. What direction does friction point?

**Explanation**

If the road is icy, there is no static friction. The phrase "safely navigates at speed $v_0$" means the bank angle and speed are matched so that the normal force alone supplies the required inward force:

$$
\sum F_r=m a_r=m\frac{v_0^2}{r}
$$

So at exactly speed $v_0$, static friction would not be needed. If friction is available but there is no tendency to slide along the bank, the static friction force is zero.

```quiz
type: radio
id: p5-no-friction-speed
shuffle: true
content: |-
  A car takes a banked curve at the no-friction speed $v_0$. The road now has static friction, but the car still travels at speed $v_0$. What is the direction of the static friction force?
options:
- id: a
  content: |-
    up the slope of the bank
- id: b
  content: |-
    down the slope of the bank
- id: c
  content: |-
    in the direction the car moves around the curve
- id: d
  content: |-
    opposite the direction the car moves around the curve
- id: e
  content: |-
    there is no static friction force
  correct: true
```

---

<a id="handle-a-speed-that-is-too-high"></a>
## Handle a Speed That Is Too High

**Example:** The same car travels at speed $v>v_0$. What direction does static friction point?

**Explanation**

At its new speed $v$, the required inward force is

$$
\frac{mv^2}{r}
$$

When $v>v_0$, the car needs more inward force than it needed at the no-friction speed. Without friction, the car would tend to slide up the bank, toward the outside of the curve.

That uphill tendency can sound as though the car is driving itself against gravity. Look at the motion from above: inertia carries the car toward a straight tangent and therefore toward the outside of the turn. Because the road rises outward, that outward drift is motion up the bank relative to the road. Static friction then points down the bank to oppose that relative slip.

Static friction opposes that possible slipping. Therefore, friction points down the slope of the bank, toward the inside of the curve. A down-bank friction force also has an inward horizontal component, which is the extra inward force the faster car needs.

```quiz
type: radio
id: p5-too-fast
shuffle: true
content: |-
  A car safely takes an icy banked curve at speed $v_0$. On the same curve, the road is dry and the car travels at $v>v_0$. Which statement correctly gives the static friction direction?
options:
- id: a
  content: |-
    Friction points up the bank because the car needs more outward force.
- id: b
  content: |-
    Friction points down the bank because the car would tend to slide up the bank.
  correct: true
- id: c
  content: |-
    Friction points forward because the car is moving faster.
- id: d
  content: |-
    Friction points backward because the car is moving faster.
- id: e
  content: |-
    There is no friction because the curve was safe on ice.
```

---

<a id="handle-a-speed-that-is-too-low"></a>
## Handle a Speed That Is Too Low

**Example:** The same car travels at speed $v<v_0$. What direction does static friction point?

**Explanation**

If the new speed satisfies $v<v_0$, then

$$
\frac{mv^2}{r}<\frac{mv_0^2}{r}
$$

so the car needs less inward force than it needed at the no-friction speed. Without friction, the car would tend to slide down the bank, toward the inside of the curve.

Static friction opposes that possible slipping. Therefore, friction points up the slope of the bank. An up-bank friction force has an outward horizontal component, which reduces the net inward force.

```quiz
type: radio
id: p5-too-slow
shuffle: true
content: |-
  A car safely takes an icy banked curve at speed $v_0$. On the same curve, the road is dry and the car travels at $v<v_0$. What is the direction of static friction?
options:
- id: a
  content: |-
    up the slope of the bank
  correct: true
- id: b
  content: |-
    down the slope of the bank
- id: c
  content: |-
    in the direction the car moves around the curve
- id: d
  content: |-
    opposite the direction the car moves around the curve
- id: e
  content: |-
    there is no static friction force
```

---

<a id="return-to-the-faster-car"></a>
## Return to the Faster Car

**Example:** A car safely navigates an icy banked curve at its design speed $v_0$. Now the ice has melted, and there is static friction between the tires and road. What is the direction of the friction force if the car travels at $v>v_0$?

**Explanation**

Since $v_0$ was the no-friction speed, a car traveling at $v>v_0$ would tend to slide up the bank. Static friction opposes that possible motion, so it points down the slope of the bank.

The direction is not forward or backward along the path. In this question, static friction is preventing slipping along the banked surface.

```quiz
type: radio
id: p5-original-check
shuffle: true
content: |-
  A car safely navigates an icy banked curve at speed $v_0$. Now consider that the ice has melted and there is static friction between the tires and road. What is the direction of the friction force if the car travels at $v>v_0$?

  ![](<../Source/Images/banked-curve-car-diagram.png>)
options:
- id: a
  content: |-
    in the direction the car is moving around the curve
- id: b
  content: |-
    in the opposite direction that the car is moving around the curve
- id: c
  content: |-
    up the slope of the banked turn
- id: d
  content: |-
    down the slope of the banked turn
  correct: true
  feedback: |-
    Faster than the no-friction speed means the car tends to slide up the bank, so static friction points down the bank.
- id: e
  content: |-
    none of the above
```

---

## Summary

The no-friction speed is the point at which the bank's normal force supplies exactly the needed inward force:

- At exactly the no-friction speed, friction is not needed.
- Faster than the no-friction speed means the car tends to slide up the bank, so friction points down the bank.
- Slower than the no-friction speed means the car tends to slide down the bank, so friction points up the bank.

Static friction is set by the tendency to slip along the bank, not by the car's forward motion around the curve.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 1 Study Guide](../../2026-07-06-Q-1/Study-Guide.md)
Next: [Writing the Vertical Force Equation on a Banked Track](../../2026-07-03-HW-2/Lessons/Problem-6.md)

Study guide index: 24/35

---
<!-- lesson-nav:end -->
