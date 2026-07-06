# Choosing Friction Direction on a Banked Curve

## Table of Contents

- [Introduction](#introduction)
- [Match the No-Friction Speed](#match-the-no-friction-speed)
- [Handle a Speed That Is Too High](#handle-a-speed-that-is-too-high)
- [Handle a Speed That Is Too Low](#handle-a-speed-that-is-too-low)
- [Apply the Answer Choices](#apply-the-answer-choices)
- [Summary](#summary)

## Prerequisites

- Centripetal acceleration points horizontally toward the center of the curve.
- The normal force is perpendicular to the road surface.
- Static friction points along the road surface and opposes the direction the tires would slip.
- At the no-friction banked-curve speed, the horizontal component of the normal force supplies exactly the required centripetal force.

---

<a id="introduction"></a>
## Introduction

When a banked curve question gives a speed that is safe on ice, that speed is the no-friction speed. At that speed, friction is not needed.

To decide the direction of static friction at a different speed, compare the required inward force with the inward force supplied by the normal force at the no-friction speed. Then ask which way the car would tend to slip along the bank. Static friction points opposite that slipping tendency.

On a usual banked curve, up the bank is toward the outside of the curve, and down the bank is toward the inside of the curve.

---

<a id="match-the-no-friction-speed"></a>
## Match the No-Friction Speed

**Example:** A car travels around an icy banked curve at the special speed $v$. What direction does friction point?

**Explanation**

If the road is icy, there is no useful static friction. The phrase "safely navigates at speed $v$" means the bank angle and speed are matched so that the normal force alone supplies the required inward force:

$$
F_{\text{inward}}=\frac{mv^2}{r}
$$

So at exactly speed $v$, static friction would not be needed. If friction is available but there is no tendency to slide along the bank, the static friction force is zero.

```quiz
type: radio
id: p5-no-friction-speed
content: |-
  A car takes a banked curve at the no-friction speed $v$. The road now has static friction, but the car still travels at speed $v$. What is the direction of the static friction force?
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

**Example:** The same car goes faster than the no-friction speed $v$. What direction does static friction point?

**Explanation**

If the new speed is $u$, the required inward force is

$$
\frac{mu^2}{r}
$$

When $u>v$, the car needs more inward force than it needed at the no-friction speed. Without friction, the car would tend to slide up the bank, toward the outside of the curve.

Static friction opposes that possible slipping. Therefore, friction points down the slope of the bank, toward the inside of the curve. A down-bank friction force also has an inward horizontal component, which is the extra inward force the faster car needs.

```quiz
type: radio
id: p5-too-fast
content: |-
  A car safely takes an icy banked curve at speed $v$. On the same curve, the road is dry and the car travels faster than $v$. Which statement correctly gives the static friction direction?
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

**Example:** The same car goes slower than the no-friction speed $v$. What direction does static friction point?

**Explanation**

If the new speed is $u<v$, then

$$
\frac{mu^2}{r}<\frac{mv^2}{r}
$$

so the car needs less inward force than it needed at the no-friction speed. Without friction, the car would tend to slide down the bank, toward the inside of the curve.

Static friction opposes that possible slipping. Therefore, friction points up the slope of the bank. An up-bank friction force has an outward horizontal component, which reduces the net inward force.

```quiz
type: radio
id: p5-too-slow
content: |-
  A car safely takes an icy banked curve at speed $v$. On the same curve, the road is dry and the car travels slower than $v$. What is the direction of static friction?
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

<a id="apply-the-answer-choices"></a>
## Apply the Answer Choices

**Example:** A car safely navigates an icy banked curve at speed $v$. Now the ice has melted, and there is static friction between the tires and road. What is the direction of the friction force if the car is going faster than $v$?

![](<../Source/Images/banked-curve-car-diagram.png>)

**Explanation**

The cue is "faster than $v$." Since $v$ was the no-friction speed, a faster car would tend to slide up the bank. Static friction opposes that possible motion, so it points down the slope of the bank.

The direction is not forward or backward along the path. In this question, static friction is preventing slipping along the banked surface.

```quiz
type: radio
id: p5-original-check
content: |-
  A car safely navigates an icy banked curve at speed $v$. Now consider that the ice has melted and there is static friction between the tires and road. What is the direction of the friction force if the car is going faster than $v$?
  
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

Use the no-friction speed as the comparison point:

- At exactly the no-friction speed, friction is not needed.
- Faster than the no-friction speed means the car tends to slide up the bank, so friction points down the bank.
- Slower than the no-friction speed means the car tends to slide down the bank, so friction points up the bank.

The main trap is choosing a forward or backward direction. For this kind of banked-curve question, static friction is opposing slipping along the slope, not pushing along the direction of travel.
