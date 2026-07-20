# Testing Statements About Gravity and Orbits

## Table of Contents

- [Introduction](#introduction)
- [Check a Formula Against Its Conditions](#check-a-formula-against-its-conditions)
- [Read the Sign of Gravitational Potential Energy](#read-the-sign-of-gravitational-potential-energy)
- [Test Definitions Word by Word](#test-definitions-word-by-word)
- [Translate Proportionality Into an Equation](#translate-proportionality-into-an-equation)
- [Final Statement Check](#final-statement-check)
- [Summary](#summary)

## Prerequisites

- Substitute a surface distance into a formula.
- Interpret a negative quantity becoming more negative.
- Distinguish a diameter from half of that diameter.
- Read direct and inverse proportionality notation.

---

<a id="introduction"></a>
## Introduction

When a question asks which physics statements are true, do not judge them by familiarity alone. Translate each statement into its defining equation or precise definition, and then check its conditions, sign, direction of change, and proportionality.

The key reference facts for this problem are

$$
g(r)=\frac{GM_E}{r^2},
\qquad
U(r)=-\frac{Gm_1m_2}{r},
\qquad
v_{\mathrm{esc}}=\sqrt{\frac{2GM}{R}},
\qquad
T^2\propto a^3.
$$

For an ellipse, the major axis is the longest diameter through the center, and the semi-major axis is half its length.

Use the same three-line check every time:

1. **Claim:** isolate the exact phrase being tested.
2. **Reference:** write the matching equation or definition.
3. **Verdict:** compare them, paying special attention to conditions, signs, powers, and words such as *directly* or *inversely*.

---

<a id="check-a-formula-against-its-conditions"></a>
## Check a Formula Against Its Conditions

**Example:** Is the statement “Near Earth's surface, $g\approx GM_E/R_E^2$” correct?

**Explanation**

The gravitational acceleration at distance $r$ from Earth's center is

$$
g(r)=\frac{GM_E}{r^2}.
$$

Near the surface, $r\approx R_E$. Substituting this condition gives

$$
g\approx\frac{GM_E}{R_E^2}.
$$

The approximation is therefore correct. The common trap is to use altitude above the surface in place of the distance from Earth's center.

```quiz
type: radio
id: p1-surface-gravity
content: |-
  A satellite is at distance $r$ from Earth's center. Which expression gives the magnitude of its gravitational acceleration due to Earth?
options:
- id: a
  content: |-
    $\dfrac{GM_E}{r^2}$
  correct: true
- id: b
  content: |-
    $\dfrac{GM_E}{r}$
- id: c
  content: |-
    $\dfrac{GM_Er^2}{1}$
- id: d
  content: |-
    $\dfrac{GmM_E}{r^2}$
- id: e
  content: |-
    $\dfrac{GM_E}{R_E}$
```

---

<a id="read-the-sign-of-gravitational-potential-energy"></a>
## Read the Sign of Gravitational Potential Energy

**Example:** Does gravitational potential energy decrease when two masses move closer together?

**Explanation**

With zero potential energy chosen at infinite separation,

$$
U(r)=-\frac{Gm_1m_2}{r}.
$$

If $r$ decreases, the positive magnitude $Gm_1m_2/r$ increases. The leading negative sign then makes $U$ more negative. For example,

$$
-\frac{C}{4}>-\frac{C}{2}
\qquad (C>0).
$$

Thus, moving from $r=4$ to $r=2$ decreases $U$. The negative sign is consistent with an attractive interaction and the chosen zero at infinity.

```quiz
type: radio
id: p1-potential-sign
content: |-
  Two masses move from separation $3r$ to separation $r$. What happens to $U=-Gm_1m_2/r$?
options:
- id: a
  content: |-
    It becomes three times as negative, so it decreases.
  correct: true
- id: b
  content: |-
    It becomes one-third as negative, so it increases.
- id: c
  content: |-
    It becomes positive because the masses approach.
- id: d
  content: |-
    It stays constant because both masses stay the same.
- id: e
  content: |-
    It becomes zero at the smaller separation.
```

---

<a id="test-definitions-word-by-word"></a>
## Test Definitions Word by Word

**Example:** Check these two statements:

1. Escape speed is the minimum launch speed from a body's surface needed for an object never to fall back.
2. The semi-major axis of an ellipse is its longest diameter.

**Explanation**

The first statement matches the ideal definition of escape speed: the minimum initial speed that lets an unpowered object reach arbitrarily far away without returning. Its launch direction does not change the ideal energy threshold, though real atmospheres and rotation can matter.

The second statement mixes up a whole length and a half-length. The **major axis** is the longest diameter through the center. If its length is $2a$, then the **semi-major axis** has length $a$.

```quiz
type: radio
id: p1-escape-definition
content: |-
  In the ideal model with no atmosphere, which statement best defines the escape speed from a body's surface?
options:
- id: a
  content: |-
    It is the minimum launch speed that allows an unpowered object never to return to the body.
  correct: true
- id: b
  content: |-
    It is the speed of every object moving in a circular orbit at the surface.
- id: c
  content: |-
    It is the minimum speed needed to leave the ground temporarily.
- id: d
  content: |-
    It is the speed needed to make gravitational potential energy positive at the surface.
- id: e
  content: |-
    It is independent of the body's mass and radius.
```

```quiz
type: radio
id: p1-definition-check
content: |-
  An ellipse has a longest diameter of length $18\,\mathrm{m}$. Which statement is correct?
options:
- id: a
  content: |-
    Its major axis has length $18\,\mathrm{m}$ and its semi-major axis has length $9\,\mathrm{m}$.
  correct: true
- id: b
  content: |-
    Its major axis has length $9\,\mathrm{m}$ and its semi-major axis has length $18\,\mathrm{m}$.
- id: c
  content: |-
    Both axes have length $18\,\mathrm{m}$.
- id: d
  content: |-
    Its semi-major axis has length $36\,\mathrm{m}$.
- id: e
  content: |-
    The major axis need not pass through the center.
```

---

<a id="translate-proportionality-into-an-equation"></a>
## Translate Proportionality Into an Equation

**Example:** Is the statement “Kepler's third law says $T^2$ is inversely proportional to $a$” correct?

**Explanation**

For bodies orbiting the same central mass, Kepler's third law is

$$
T^2=\frac{4\pi^2}{GM}a^3.
$$

Therefore,

$$
T^2\propto a^3,
$$

which is a direct cubic proportionality. An inverse claim would instead have the form $T^2\propto 1/a^n$ for some positive power $n$. Increasing $a$ actually increases $T^2$; it does not decrease it. The word “inversely” makes the proposed statement false, and omitting the cube is a second error.

```quiz
type: radio
id: p1-kepler-proportionality
content: |-
  Which statement correctly expresses Kepler's third law for objects orbiting the same central mass?
options:
- id: a
  content: |-
    $T^2$ is directly proportional to $a^3$.
  correct: true
- id: b
  content: |-
    $T^2$ is inversely proportional to $a$.
- id: c
  content: |-
    $T$ is inversely proportional to $a^3$.
- id: d
  content: |-
    $T^2$ is directly proportional to $a$.
- id: e
  content: |-
    $T$ is independent of $a$.
```

---

<a id="final-statement-check"></a>
## Final Statement Check

**Example:** Apply the same test to every statement in the original problem.

**Explanation**

- The surface-gravity formula follows by using $r\approx R_E$ in $g=GM_E/r^2$.
- The negative potential becomes more negative as separation decreases.
- The escape-speed statement matches the ideal definition.
- The major-axis and semi-major-axis definitions are correct.
- Kepler's third law is direct in $a^3$, not inverse in $a$.

```quiz
type: radio
id: p1-original-check
content: |-
  Consider the following statements.

  **A.** Near Earth's surface, the approximate magnitude of the free-fall acceleration is $g=\dfrac{GM_E}{R_E^2}$, where $M_E$ and $R_E$ are Earth's mass and radius.

  **B.** The negative sign in $U=-\dfrac{Gm_1m_2}{r}$ reflects that gravity is attractive and ensures that the potential energy decreases as the objects approach each other.

  **C.** The escape speed of a body is the minimum launch speed from its surface required for an object never to fall back.

  **D.** The major axis of an ellipse is its longest diameter, passing through the center and connecting the two farthest points on the ellipse. The semi-major axis is half this distance.

  **E.** Kepler's third law states that the square of a planet's orbital period is inversely proportional to the semi-major axis of its orbit.

  Which set contains all and only the true statements?
options:
- id: a
  content: |-
    A, B, C, and D
  correct: true
- id: b
  content: |-
    A, B, C, and E
- id: c
  content: |-
    A, C, D, and E
- id: d
  content: |-
    B, C, D, and E
- id: e
  content: |-
    A, B, C, D, and E
```

---

<a id="summary"></a>
## Summary

To test a conceptual statement:

1. Write the defining equation or definition.
2. Check the condition: for example, near Earth's surface means $r\approx R_E$.
3. Track signs and direction of change: smaller $r$ makes $U=-C/r$ more negative.
4. Keep whole and half-length definitions distinct: major axis $=2a$, semi-major axis $=a$.
5. Translate proportionality exactly: Kepler's third law is $T^2\propto a^3$, not an inverse law.

The main trap is accepting familiar vocabulary while overlooking one decisive word such as “inverse,” or confusing a complete quantity with half of it.
