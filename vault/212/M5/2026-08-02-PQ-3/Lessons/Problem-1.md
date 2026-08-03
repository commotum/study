# Deciding What Changes a Pendulum's Frequency — Version 1: Derivation First

<!--
lesson-id: 212-M5-045
topic-code: MTH212.M5.45
-->

## Table of Contents

- [Introduction](#introduction)
- [Derive the Small-Angle Frequency](#derive-the-frequency)
- [Read What the Formula Says](#read-the-dependencies)
- [Turn the Formula Into a Comparison Rule](#compare-with-a-ratio)
- [Apply the Rule](#apply-the-rule)
- [Summary](#summary)

## Prerequisites

- Apply Newton's second law, $F=ma$.
- Recognize the SHM relation $a=-\omega^2x$.
- Use $f=\omega/(2\pi)$.
- Use the small-angle approximation $\sin\theta\approx\theta$.
- Compare quantities using a ratio.
- Simplify square roots.

---

<a id="introduction"></a>
## Introduction

A heavier pendulum bob experiences a larger gravitational force. Does that make it oscillate at a different frequency? To answer that question, derive the bob's restoring acceleration instead of reasoning from force or mass alone.

Consider an ideal simple pendulum: a bob of mass $m$ hangs from a massless string of length $L$ and undergoes small oscillations in a uniform gravitational field $g$.

The causal chain is

$$
\text{tangential restoring force}
\longrightarrow
\text{tangential acceleration}
\longrightarrow
\text{SHM equation}
\longrightarrow
\omega
\longrightarrow
f.
$$

---

<a id="derive-the-frequency"></a>
## Derive the Small-Angle Frequency

Let $s$ be the bob's signed displacement along its circular path from equilibrium, and let $\theta$ be its angular displacement in radians. Arc length gives

$$
s=L\theta,
$$

so

$$
\theta=\frac{s}{L}.
$$

The string tension points perpendicular to the bob's path, so it does not accelerate the bob along that path. The component of gravity tangent to the path is

$$
F_{\mathrm{tan}}=-mg\sin\theta.
$$

The minus sign means the force is restoring: it points back toward equilibrium.

For small angles,

$$
\sin\theta\approx\theta.
$$

Therefore,

$$
F_{\mathrm{tan}}
\approx-mg\theta
=-\frac{mg}{L}s.
$$

Apply Newton's second law along the path:

$$
ma_{\mathrm{tan}}=-\frac{mg}{L}s.
$$

The mass appears on both sides and cancels:

$$
a_{\mathrm{tan}}=-\frac{g}{L}s.
$$

Compare this with the standard SHM relation

$$
a=-\omega^2x.
$$

Here $s$ plays the role of the displacement $x$, so

$$
\omega^2=\frac{g}{L}
$$

and

$$
\omega=\sqrt{\frac{g}{L}}.
$$

Since $f=\omega/(2\pi)$,

$$
\boxed{f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}}.
$$

The mass cancellation is the key physical result. A heavier bob has a proportionally larger gravitational restoring force, but it also has proportionally greater inertia. Those effects cancel, so changing the bob's mass alone does not change the frequency predicted by this model.

This is an ideal, small-angle result. At larger amplitudes, $\sin\theta\approx\theta$ is no longer accurate, so the motion is not exactly simple harmonic and the frequency also depends slightly on amplitude.

```quiz
type: radio
id: pq3-p1-mass-cancellation
content: |-
  Why does the bob's mass not appear in the small-angle frequency of a simple pendulum?
options:
- id: pq3-p1-mass-cancellation-a
  content: |-
    Gravity exerts the same tangential force on every bob, regardless of mass.
  feedback: |-
    The tangential gravitational force is not mass-independent: at fixed $\theta$, $|F_{\mathrm{tan}}|\approx mg|\theta|$, so a heavier bob feels a larger force. Its inertia grows by the same factor, so $m$ cancels from $F=ma$.
- id: pq3-p1-mass-cancellation-b
  content: |-
    Restoring force and inertia both scale with $m$, so the factor of $m$ cancels from the equation of motion.
  correct: true
  feedback: |-
    The restoring force contains $m$, and Newton's second law contributes the same $m$ through inertia. Canceling it gives $a_{\mathrm{tan}}=-(g/L)s$, so $\omega$ and $f$ are independent of bob mass.
- id: pq3-p1-mass-cancellation-c
  content: |-
    String tension cancels the tangential component of gravity.
  feedback: |-
    Tension points radially along the string, while the restoring component of gravity points along the bob's path. Tension therefore cannot cancel the tangential force; the cancellation is between the factor $m$ in that force and the factor $m$ in $ma$.
- id: pq3-p1-mass-cancellation-d
  content: |-
    The small-angle approximation sets the mass equal to one.
  feedback: |-
    The approximation replaces $\sin\theta$ with $\theta$; it does not change or normalize the mass. Mass disappears only after $ma_{\mathrm{tan}}=-(mg/L)s$ is divided by $m$.
- id: pq3-p1-mass-cancellation-e
  content: |-
    A heavier bob moves more slowly but travels through a proportionally shorter arc.
  feedback: |-
    Bobs released through the same angle travel the same arc length when their strings have the same $L$. Their frequencies match because restoring force and inertia scale together, not because the heavier bob follows a shorter path.
```

---

<a id="read-the-dependencies"></a>
## Read What the Formula Says

The derivation gives

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Holding the other quantities fixed,

$$
f\propto\sqrt{g},
\qquad
f\propto\frac{1}{\sqrt L},
\qquad
f\text{ is independent of }m.
$$

In physical terms:

- Stronger gravity produces a greater restoring acceleration, so the frequency increases.
- A longer pendulum has a smaller restoring acceleration for the same displacement along its path, so the frequency decreases.
- Increasing the bob's mass increases restoring force and inertia by the same factor, so the frequency does not change.

**Example:** Two bobs have masses $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. Each hangs from a string of the same length in the same location. Compare their frequencies.

**Explanation**

Both pendulums have the same $g$ and $L$. Since mass canceled before the frequency formula was obtained,

$$
f_{0.20}=f_{0.80}.
$$

---

<a id="compare-with-a-ratio"></a>
## Turn the Formula Into a Comparison Rule

For two pendulum conditions,

$$
f_1=\frac{1}{2\pi}\sqrt{\frac{g_1}{L_1}}
\qquad\text{and}\qquad
f_2=\frac{1}{2\pi}\sqrt{\frac{g_2}{L_2}}.
$$

Divide the new frequency by the original frequency:

$$
\begin{aligned}
\frac{f_2}{f_1}
&=
\frac{\dfrac{1}{2\pi}\sqrt{g_2/L_2}}
     {\dfrac{1}{2\pi}\sqrt{g_1/L_1}}\\
&=
\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
\end{aligned}
$$

Thus,

$$
\boxed{\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}}.
$$

If the location does not change, then $g_2/g_1=1$. If the length does not change, then $L_1/L_2=1$. No mass ratio appears because mass already canceled from the equation of motion.

**Example:** A pendulum's length changes from $L$ to $4L$ while $g$ stays fixed. Find the new frequency in terms of the original frequency $f$.

**Explanation**

Set $g_2/g_1=1$ and $L_2/L_1=4$:

$$
\frac{f_{\mathrm{new}}}{f}
=\sqrt{1\cdot\frac{L}{4L}}
=\frac12.
$$

Therefore,

$$
f_{\mathrm{new}}=\frac{f}{2}.
$$

```quiz
type: radio
id: pq3-p1-length-reduced
content: |-
  A simple pendulum has frequency $f$. Its length is changed from $L$ to $L/9$ while its location stays fixed. What is the new frequency?
options:
- id: pq3-p1-length-reduced-a
  content: |-
    $f/9$
  feedback: |-
    This gives frequency the same change factor as length. Pendulum frequency varies inversely with the square root of length, so shortening $L$ to $L/9$ makes the oscillation faster rather than nine times slower.
- id: pq3-p1-length-reduced-b
  content: |-
    $f/3$
  feedback: |-
    This uses the correct square-root factor but applies it in the wrong direction. Because $L$ is in the denominator, reducing the length to $L/9$ increases the frequency by $\sqrt9=3$.
- id: pq3-p1-length-reduced-c
  content: |-
    $f$
  feedback: |-
    Unlike bob mass, length remains in the equation of motion. Changing $L$ to $L/9$ multiplies $f$ by $\sqrt{L/(L/9)}=3$, so the frequency does not remain unchanged.
- id: pq3-p1-length-reduced-d
  content: |-
    $3f$
  correct: true
  feedback: |-
    A shorter pendulum has a greater restoring acceleration for the same path displacement. Since $f\propto1/\sqrt L$, reducing $L$ to $L/9$ increases the frequency by $\sqrt9=3$, giving $f_{\mathrm{new}}=3f$.
- id: pq3-p1-length-reduced-e
  content: |-
    $9f$
  feedback: |-
    This treats frequency as inversely proportional to length rather than to its square root. A factor-of-$9$ decrease in $L$ produces a factor-of-$3$ increase, so $f_{\mathrm{new}}=3f$.
```

---

<a id="apply-the-rule"></a>
## Apply the Rule

For every comparison:

1. Write $f_2/f_1$ as the new frequency divided by the original frequency.
2. Insert the gravity and length change factors.
3. Omit mass because it already canceled.
4. Simplify the square root.

**Mass change:** The original practice-quiz question is a direct test of the cancellation derived above.

```quiz
type: radio
id: pq3-p1-original-check
shuffle: true
content: |-
  A bob of mass $m$ swings as a pendulum on a massless string with frequency $f$. If the bob's mass is doubled, what happens to the oscillation frequency?
options:
- id: pq3-p1-original-check-a
  content: |-
    The new frequency is one-fourth the original frequency.
  feedback: |-
    This invents an inverse-square dependence on bob mass. Doubling $m$ doubles both the tangential restoring force and the inertia in $ma$, so the mass cancels and the frequency remains $f$.
- id: pq3-p1-original-check-b
  content: |-
    The new frequency is one-half the original frequency.
  feedback: |-
    This assumes doubling mass doubles the period. In the pendulum equation of motion, the same factor of $m$ multiplies restoring force and inertia, so changing $m$ alone leaves the frequency unchanged.
- id: pq3-p1-original-check-c
  content: |-
    The new frequency is the same as the original frequency.
  correct: true
  feedback: |-
    A heavier bob has proportionally greater restoring force and inertia, so mass cancels. With $g$ and $L$ unchanged, the frequency remains $f$.
- id: pq3-p1-original-check-d
  content: |-
    The new frequency is twice the original frequency.
  feedback: |-
    This treats mass as a direct frequency multiplier. Bob mass is absent from $f=(2\pi)^{-1}\sqrt{g/L}$ because it canceled from the acceleration equation, so doubling $m$ does not produce $2f$.
- id: pq3-p1-original-check-e
  content: |-
    The new frequency is four times the original frequency.
  feedback: |-
    This introduces a mass dependence and then squares its change factor. Mass contributes no multiplier after cancellation, so neither $2$ nor $4$ belongs in the frequency ratio; the result remains $f$.
```

**Example — gravity change:** Suppose the same pendulum is moved to a location where $g_2=4g_1$, with $L$ unchanged.

**Explanation**

The ratio rule gives

$$
\frac{f_2}{f_1}
=\sqrt{\frac{4g_1}{g_1}\frac{L}{L}}
=\sqrt4
=2.
$$

Stronger gravity increases the restoring acceleration, so the frequency doubles.

```quiz
type: radio
id: pq3-p1-gravity-reduced
content: |-
  A simple pendulum has frequency $f$. It is moved to a location where the gravitational-field strength is $g/9$, while its length and bob mass stay unchanged. What is its new frequency?
options:
- id: pq3-p1-gravity-reduced-a
  content: |-
    $f/9$
  feedback: |-
    This applies the gravity factor directly. Frequency depends on the square root of $g$, so reducing $g$ by a factor of $9$ reduces $f$ by only $\sqrt9=3$.
- id: pq3-p1-gravity-reduced-b
  content: |-
    $f/3$
  correct: true
  feedback: |-
    Weaker gravity gives a smaller restoring acceleration. Since $f\propto\sqrt g$, changing $g$ to $g/9$ multiplies the frequency by $\sqrt{1/9}=1/3$, giving $f_{\mathrm{new}}=f/3$.
- id: pq3-p1-gravity-reduced-c
  content: |-
    $f$
  feedback: |-
    Bob mass is irrelevant, but gravity is not. Moving to $g/9$ changes the restoring acceleration and multiplies the frequency by $\sqrt{1/9}=1/3$.
- id: pq3-p1-gravity-reduced-d
  content: |-
    $3f$
  feedback: |-
    This uses the right square-root factor but reverses the physical direction. Weaker gravity makes the restoring acceleration smaller, so the pendulum oscillates more slowly and the new frequency is $f/3$.
- id: pq3-p1-gravity-reduced-e
  content: |-
    $9f$
  feedback: |-
    This makes frequency inversely and linearly dependent on gravity. The actual dependence is $f\propto\sqrt g$, so reducing $g$ to $g/9$ gives $f/3$, not $9f$.
```

**Example — mixed change:** Suppose $m_2=2m_1$, $g_2=9g_1$, and $L_2=4L_1$.

**Explanation**

Ignore the mass change and use the two relevant ratios:

$$
\frac{f_2}{f_1}
=\sqrt{9\cdot\frac14}
=\frac32.
$$

The stronger gravity wins over the longer length, so the new frequency is $3f_1/2$.

```quiz
type: radio
id: pq3-p1-mixed-change
content: |-
  A pendulum changes from $m$, $g$, and $L$ to $5m$, $4g$, and $9L$. If its original frequency is $f$, what is its new frequency?
options:
- id: pq3-p1-mixed-change-a
  content: |-
    $f/3$
  feedback: |-
    This includes the length effect $1/\sqrt9=1/3$ but omits the gravity effect $\sqrt4=2$. Combining both relevant changes gives $(2)(1/3)f=2f/3$.
- id: pq3-p1-mixed-change-b
  content: |-
    $2f/3$
  correct: true
  feedback: |-
    Mass cancels, so only gravity and length enter the ratio. Therefore $f_2/f=\sqrt{4\cdot(1/9)}=2/3$, giving $f_2=2f/3$.
- id: pq3-p1-mixed-change-c
  content: |-
    $3f/2$
  feedback: |-
    This inverts the new-to-original comparison. The required ratio is $\sqrt{(g_2/g_1)(L_1/L_2)}=\sqrt{4/9}=2/3$, not $\sqrt{9/4}=3/2$.
- id: pq3-p1-mixed-change-d
  content: |-
    $2f$
  feedback: |-
    This includes the gravity multiplier $\sqrt4=2$ but ignores the longer pendulum. The length change $L\to9L$ contributes another factor of $1/3$, so the combined multiplier is $2/3$.
- id: pq3-p1-mixed-change-e
  content: |-
    $10f/3$
  feedback: |-
    This multiplies the correct gravity-and-length factor $2/3$ by the mass factor $5$. Bob mass already canceled from the equation of motion, so the factor $5$ must be omitted.
```

---

<a id="summary"></a>
## Summary

The derivation follows

$$
F_{\mathrm{tan}}
\longrightarrow
a_{\mathrm{tan}}=-\frac{g}{L}s
\longrightarrow
\omega=\sqrt{\frac{g}{L}}
\longrightarrow
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

For comparisons,

$$
\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
$$

| Change | Frequency multiplier |
| --- | ---: |
| $m\to km$ | $1$ |
| $g\to kg$ | $\sqrt{k}$ |
| $L\to kL$ | $1/\sqrt{k}$ |

The main trap is inserting bob mass after it has already canceled. The model also assumes an ideal pendulum and small angles; at larger amplitudes, the frequency depends slightly on amplitude.

---

# Deciding What Changes a Pendulum's Frequency — Version 2: Original

<!-- lesson-version: 2-original -->

## Table of Contents

- [Introduction](#v2-introduction)
- [Read the Dependency Formula](#v2-read-the-dependency-formula)
- [Compare a Variable That Does Matter](#v2-compare-a-variable-that-does-matter)
- [Reject a False Mass Dependence](#v2-reject-a-false-mass-dependence)
- [Summary](#v2-summary)

## Prerequisites

- Read which variables appear in a formula.
- Compare quantities using a ratio.
- Simplify square roots such as $\sqrt{1/4}=1/2$.

---

<a id="v2-introduction"></a>
## Introduction

For a simple pendulum undergoing small oscillations, the frequency is

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}},
$$

where $g$ is the gravitational-field strength and $L$ is the pendulum length. When a question changes one feature of the pendulum, first check whether that feature appears in this formula. If it does not appear, changing it alone cannot change the frequency predicted by this model.

Holding the other quantities fixed, the formula gives this dependency map:

$$
f\propto \sqrt{g},
\qquad
f\propto \frac{1}{\sqrt{L}},
\qquad
f\text{ is independent of }m.
$$

---

<a id="v2-read-the-dependency-formula"></a>
## Read the Dependency Formula

**Example:** Two bobs have masses $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. Each hangs from a string of the same length in the same location. Compare their oscillation frequencies.

**Explanation**

The formula contains $g$ and $L$, but not the bob mass $m$. Both pendulums have the same $g$ and $L$, so they have the same frequency:

$$
f_{0.20}=f_{0.80}.
$$

The larger mass changes forces such as the bob's weight, but mass cancels from the equation of motion and does not remain in the frequency formula.

```quiz
type: radio
id: pq3-p1-v2-mass-tripled
content: |-
  A simple pendulum has frequency $f$. Its bob is replaced by another bob with three times the mass while the string length and location remain unchanged. What is the new frequency?
options:
- id: pq3-p1-v2-mass-tripled-a
  content: |-
    $f/3$
  feedback: |-
    This assumes that tripling the bob's mass makes the pendulum three times slower. For a simple pendulum, the greater gravitational force and greater inertia scale together, so mass cancels; with $g$ and $L$ unchanged, the frequency remains $f$.
- id: pq3-p1-v2-mass-tripled-b
  content: |-
    $f/\sqrt{3}$
  feedback: |-
    This imports the spring-oscillator dependence $f\propto 1/\sqrt m$ into a pendulum. Bob mass affects a mass-spring frequency, but a simple pendulum is controlled by $g$ and $L$, so tripling $m$ does not introduce a factor of $1/\sqrt3$.
- id: pq3-p1-v2-mass-tripled-c
  content: |-
    $f$
  correct: true
  feedback: |-
    A heavier pendulum bob has proportionally more weight and inertia, so mass cancels from its small-angle motion. Since $f=(2\pi)^{-1}\sqrt{g/L}$ and neither $g$ nor $L$ changes, the new frequency is $f$.
- id: pq3-p1-v2-mass-tripled-d
  content: |-
    $\sqrt{3}f$
  feedback: |-
    The factor $\sqrt3$ would follow if the gravitational field $g$ tripled, because $f\propto\sqrt g$. Here only the bob mass triples, and mass is absent from the pendulum frequency, so the multiplier is $1$.
- id: pq3-p1-v2-mass-tripled-e
  content: |-
    $3f$
  feedback: |-
    This treats frequency as directly proportional to bob mass. Increasing mass increases both the restoring torque and rotational inertia by the same factor, leaving $f=(2\pi)^{-1}\sqrt{g/L}$ and therefore the frequency unchanged.
```

---

<a id="v2-compare-a-variable-that-does-matter"></a>
## Compare a Variable That Does Matter

**Example:** A pendulum's length changes from $L$ to $4L$ while $g$ stays fixed. Find the new frequency in terms of the original frequency $f$.

**Explanation**

For any two simple pendulums described by this model,

$$
\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
$$

This ratio contains changes in $g$ and $L$, but no mass factor. Here $g_2=g_1$ and $L_2=4L_1$, so

$$
\frac{f_{\mathrm{new}}}{f}
=\sqrt{\frac{L}{4L}}
=\frac{1}{2}.
$$

Therefore,

$$
f_{\mathrm{new}}=\frac{f}{2}.
$$

This contrast is useful: changing $L$ matters because $L$ appears under the square root, while changing $m$ does not matter because $m$ is absent.

```quiz
type: radio
id: pq3-p1-v2-length-reduced
content: |-
  A simple pendulum has frequency $f$. Its length is changed from $L$ to $L/9$ while its location stays fixed. What is the new frequency?
options:
- id: pq3-p1-v2-length-reduced-a
  content: |-
    $f/9$
  feedback: |-
    This gives frequency the same change factor as length. Pendulum frequency varies inversely with the square root of length, so shortening $L$ to $L/9$ makes the oscillation faster rather than nine times slower.
- id: pq3-p1-v2-length-reduced-b
  content: |-
    $f/3$
  feedback: |-
    This uses the correct square-root factor but applies it in the wrong direction. Because $L$ is in the denominator of $f=(2\pi)^{-1}\sqrt{g/L}$, reducing the length to $L/9$ increases the frequency by $\sqrt9=3$.
- id: pq3-p1-v2-length-reduced-c
  content: |-
    $f$
  feedback: |-
    Unlike bob mass, length controls a simple pendulum's frequency. A shorter pendulum has a shorter time scale; changing $L$ to $L/9$ multiplies $f$ by $\sqrt{L/(L/9)}=3$, so it does not remain $f$.
- id: pq3-p1-v2-length-reduced-d
  content: |-
    $3f$
  correct: true
  feedback: |-
    A shorter simple pendulum oscillates more rapidly, with $f\propto 1/\sqrt L$. Reducing the length from $L$ to $L/9$ therefore increases the frequency by $\sqrt9=3$, giving $f_{\mathrm{new}}=3f$.
- id: pq3-p1-v2-length-reduced-e
  content: |-
    $9f$
  feedback: |-
    This correctly predicts an increase but treats frequency as inversely proportional to length. The dependence is inverse square root, so a factor-of-$9$ decrease in $L$ produces only a factor-of-$3$ increase: $f_{\mathrm{new}}=3f$.
```

---

<a id="v2-reject-a-false-mass-dependence"></a>
## Reject a False Mass Dependence

**Example:** A student argues that doubling the bob's mass must reduce the frequency because a heavier object is harder to accelerate. Identify the error.

**Explanation**

The student is reasoning from mass alone instead of reading the pendulum model. After the mass changes from $m$ to $2m$, the right-hand side of the frequency formula is still

$$
\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Therefore,

$$
f_{\mathrm{new}}
=\frac{1}{2\pi}\sqrt{\frac{g}{L}}
=f.
$$

Doubling $m$ changes no symbol on the right-hand side. There is no valid place to insert a factor of $2$, $1/2$, or $1/\sqrt{2}$.

```quiz
type: radio
id: pq3-p1-v2-original-check
shuffle: true
content: |-
  A bob of mass $m$ swings as a pendulum on a massless string with frequency $f$. If the bob's mass is doubled, what happens to the oscillation frequency?
options:
- id: pq3-p1-v2-original-check-a
  content: |-
    The new frequency is one-fourth the original frequency.
  feedback: |-
    This invents an inverse-square dependence on bob mass. Mass increases the pendulum's gravitational restoring torque and its rotational inertia by the same factor, so it cancels; doubling $m$ leaves the frequency at $f$, not $f/4$.
- id: pq3-p1-v2-original-check-b
  content: |-
    The new frequency is one-half the original frequency.
  feedback: |-
    This assumes that doubling the bob mass doubles the period and halves the frequency. In the simple-pendulum model, bob mass cancels and only $g$ and $L$ control the frequency, so changing $m$ alone leaves it unchanged.
- id: pq3-p1-v2-original-check-c
  content: |-
    The new frequency is the same as the original frequency.
  correct: true
  feedback: |-
    A simple pendulum's small-angle frequency is $f=(2\pi)^{-1}\sqrt{g/L}$ because mass cancels between restoring force and inertia. Doubling only the bob mass leaves $g$ and $L$ unchanged, so the new frequency is still $f$.
- id: pq3-p1-v2-original-check-d
  content: |-
    The new frequency is twice the original frequency.
  feedback: |-
    This treats bob mass as a direct frequency multiplier. Mass is not a control variable in $f=(2\pi)^{-1}\sqrt{g/L}$; with the same length and location, doubling $m$ leaves the frequency at $f$ rather than $2f$.
- id: pq3-p1-v2-original-check-e
  content: |-
    The new frequency is four times the original frequency.
  feedback: |-
    This both introduces a mass dependence and squares the change factor. Bob mass cancels entirely from the simple-pendulum motion, so neither a factor of $2$ nor $4$ belongs in the frequency; it remains $f$.
```

---

<a id="v2-summary"></a>
## Summary

When a pendulum parameter changes:

1. Start with $f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}$.
2. Hold the other quantities fixed and check whether the changed parameter appears.
3. Translate its change factor through the formula.

| Change | Frequency multiplier |
| --- | ---: |
| $m\to km$ | $1$ |
| $g\to kg$ | $\sqrt{k}$ |
| $L\to kL$ | $1/\sqrt{k}$ |

The main trap is inventing a mass dependence that the simple-pendulum formula does not contain.

---

# Deciding What Changes a Pendulum's Frequency — Version 3: Formula First, Then Why Mass Cancels

<!-- lesson-version: 3-balanced -->

## Table of Contents

- [Introduction](#v3-introduction)
- [Why Mass Does Not Appear](#v3-why-mass-cancels)
- [Apply the Dependency Formula](#v3-apply-the-dependency-formula)
- [Compare a Variable That Does Matter](#v3-compare-a-variable-that-does-matter)
- [Check the Mass Conclusion](#v3-check-the-mass-conclusion)
- [Summary](#v3-summary)

## Prerequisites

- Apply Newton's second law, $F=ma$.
- Recognize the SHM relation $a=-\omega^2x$.
- Use $f=\omega/(2\pi)$.
- Use the small-angle approximation $\sin\theta\approx\theta$.
- Compare quantities using a ratio.
- Simplify square roots.

---

<a id="v3-introduction"></a>
## Introduction

For a simple pendulum undergoing small oscillations, the frequency is

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}},
$$

where $g$ is the gravitational-field strength and $L$ is the pendulum length. When a question changes one feature of the pendulum, first check whether that feature appears in this formula. If it does not appear, changing it alone cannot change the frequency predicted by this model.

Holding the other quantities fixed, the formula gives this dependency map:

$$
f\propto\sqrt{g},
\qquad
f\propto\frac{1}{\sqrt L},
\qquad
f\text{ is independent of }m.
$$

This formula is the practical decision rule. The next section explains why bob mass does not appear in it.

---

<a id="v3-why-mass-cancels"></a>
## Why Mass Does Not Appear

A heavier bob experiences a larger gravitational restoring force, but it also has greater inertia. The frequency depends on the restoring force relative to that inertia, not on the restoring force alone.

When the bob is displaced by an angle $\theta$, the string tension points perpendicular to the bob's circular path. It therefore has no tangential component. Gravity supplies the entire net force along the path:

$$
\sum F_{\mathrm{tan}}=-mg\sin\theta.
$$

The minus sign means that the force points back toward the equilibrium position $\theta=0$.

Newton's second law is

$$
\sum F_{\mathrm{tan}}=ma_{\mathrm{tan}}.
$$

To make the role of inertia visible, solve for the acceleration:

$$
a_{\mathrm{tan}}
=\frac{\sum F_{\mathrm{tan}}}{m}.
$$

Substitute the gravitational restoring force:

$$
a_{\mathrm{tan}}
=\frac{-mg\sin\theta}{m}
=-g\sin\theta.
$$

This is where the two roles of mass become visible:

- The $m$ in the numerator makes the gravitational restoring force larger for a heavier bob.
- The $m$ in the denominator is inertial mass: a heavier bob requires more force to produce the same acceleration.

If the mass is multiplied by any factor $k$, then

$$
a'_{\mathrm{tan}}
=\frac{-(km)g\sin\theta}{km}
=-g\sin\theta
=a_{\mathrm{tan}}.
$$

The restoring force becomes $k$ times as large, but the inertia also becomes $k$ times as large. Therefore, changing the bob's mass does not change its tangential acceleration at a given angle.

To connect this acceleration to frequency, use the small-angle approximation

$$
\sin\theta\approx\theta.
$$

Let $s$ be the bob's signed displacement along its circular path. Since

$$
s=L\theta,
$$

we have $\theta=s/L$. Therefore,

$$
a_{\mathrm{tan}}
\approx-g\theta
=-\frac{g}{L}s.
$$

This has the standard SHM form

$$
a=-\omega^2x.
$$

Here $s$ plays the role of the displacement $x$, so

$$
\omega^2=\frac{g}{L}.
$$

For small angles, the restoring-force magnitude per unit path displacement is $mg/L$. Therefore, the restoring-strength-to-inertia ratio is

$$
\omega^2
=\frac{mg/L}{m}
=\frac{g}{L}.
$$

Thus,

$$
\omega=\sqrt{\frac{g}{L}},
$$

and because $f=\omega/(2\pi)$,

$$
\boxed{f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}}.
$$

Mass is absent from the frequency formula because it already canceled when the gravitational restoring force was divided by the bob's inertia.

This is an ideal, small-angle result. At larger amplitudes, $\sin\theta\approx\theta$ is no longer accurate, so the motion is not exactly simple harmonic and the frequency also depends slightly on amplitude.

```quiz
type: radio
id: pq3-p1-v3-mass-cancellation
content: |-
  Why does the bob's mass not appear in the small-angle frequency of a simple pendulum?
options:
- id: pq3-p1-v3-mass-cancellation-a
  content: |-
    Gravity exerts the same tangential force on every bob, regardless of mass.
  feedback: |-
    The tangential gravitational force grows with mass: at a fixed angle, $|F_{\mathrm{tan}}|=mg|\sin\theta|$. A heavier bob also has proportionally greater inertia, so dividing the force by $m$ gives the same tangential acceleration.
- id: pq3-p1-v3-mass-cancellation-b
  content: |-
    Restoring force and inertia both scale with $m$, so the factor of $m$ cancels from the equation of motion.
  correct: true
  feedback: |-
    A heavier bob has a proportionally larger gravitational restoring force and proportionally greater inertia. Dividing $-mg\sin\theta$ by $m$ gives $a_{\mathrm{tan}}=-g\sin\theta$, so the frequency is independent of bob mass.
- id: pq3-p1-v3-mass-cancellation-c
  content: |-
    String tension cancels the tangential component of gravity.
  feedback: |-
    Tension points along the string, perpendicular to the tangent to the bob's path, so it has no tangential component. The cancellation is between the factor $m$ in the gravitational restoring force and the inertial mass in $F=ma$.
- id: pq3-p1-v3-mass-cancellation-d
  content: |-
    The small-angle approximation removes the mass from the equation.
  feedback: |-
    The small-angle approximation replaces $\sin\theta$ with $\theta$; it does not affect mass. The mass has already canceled in $a_{\mathrm{tan}}=(-mg\sin\theta)/m$ before that approximation is used.
- id: pq3-p1-v3-mass-cancellation-e
  content: |-
    A heavier bob moves more slowly but travels through a proportionally shorter arc.
  feedback: |-
    With the same string length and release angle, both bobs travel through the same arc. Their frequencies match because restoring force and inertia increase by the same factor, leaving the tangential acceleration unchanged.
```

---

<a id="v3-apply-the-dependency-formula"></a>
## Apply the Dependency Formula

**Example:** Two bobs have masses $0.20\ \mathrm{kg}$ and $0.80\ \mathrm{kg}$. Each hangs from a string of the same length in the same location. Compare their oscillation frequencies.

**Explanation**

The changed feature is bob mass. Mass does not appear in

$$
f=\frac{1}{2\pi}\sqrt{\frac{g}{L}}.
$$

Both pendulums have the same $g$ and $L$, so

$$
f_{0.20}=f_{0.80}.
$$

The formula gives the quick decision, and the preceding derivation explains why that decision is physically valid.

---

<a id="v3-compare-a-variable-that-does-matter"></a>
## Compare a Variable That Does Matter

For two pendulum conditions,

$$
f_1=\frac{1}{2\pi}\sqrt{\frac{g_1}{L_1}}
\qquad\text{and}\qquad
f_2=\frac{1}{2\pi}\sqrt{\frac{g_2}{L_2}}.
$$

Divide the new frequency by the original frequency:

$$
\begin{aligned}
\frac{f_2}{f_1}
&=
\frac{\dfrac{1}{2\pi}\sqrt{g_2/L_2}}
     {\dfrac{1}{2\pi}\sqrt{g_1/L_1}}\\
&=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
\end{aligned}
$$

Thus,

$$
\boxed{\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}}.
$$

No mass ratio appears because mass already canceled from the equation of motion.

**Example:** A pendulum's length changes from $L$ to $4L$ while $g$ stays fixed. Find the new frequency in terms of the original frequency $f$.

**Explanation**

Here $g_2/g_1=1$ and $L_2/L_1=4$, so

$$
\frac{f_{\mathrm{new}}}{f}
=\sqrt{1\cdot\frac{L}{4L}}
=\frac12.
$$

Therefore,

$$
f_{\mathrm{new}}=\frac{f}{2}.
$$

Changing $L$ matters because $L$ appears in the frequency formula. Making the pendulum longer reduces its frequency.

```quiz
type: radio
id: pq3-p1-v3-length-reduced
content: |-
  A simple pendulum has frequency $f$. Its length is changed from $L$ to $L/9$ while its location stays fixed. What is the new frequency?
options:
- id: pq3-p1-v3-length-reduced-a
  content: |-
    $f/9$
  feedback: |-
    This gives frequency the same change factor as length. Pendulum frequency varies inversely with the square root of length, so shortening $L$ to $L/9$ makes the oscillation faster rather than nine times slower.
- id: pq3-p1-v3-length-reduced-b
  content: |-
    $f/3$
  feedback: |-
    This uses the correct square-root factor but applies it in the wrong direction. Because $L$ is in the denominator, reducing the length to $L/9$ increases the frequency by $\sqrt9=3$.
- id: pq3-p1-v3-length-reduced-c
  content: |-
    $f$
  feedback: |-
    Unlike bob mass, length appears in the frequency formula. Changing $L$ to $L/9$ multiplies the frequency by $\sqrt{L/(L/9)}=3$, so it does not remain unchanged.
- id: pq3-p1-v3-length-reduced-d
  content: |-
    $3f$
  correct: true
  feedback: |-
    A shorter pendulum oscillates more rapidly. Since $f\propto1/\sqrt L$, reducing $L$ to $L/9$ increases the frequency by $\sqrt9=3$, giving $f_{\mathrm{new}}=3f$.
- id: pq3-p1-v3-length-reduced-e
  content: |-
    $9f$
  feedback: |-
    This treats frequency as inversely proportional to length rather than to its square root. A factor-of-$9$ decrease in $L$ produces a factor-of-$3$ increase, so $f_{\mathrm{new}}=3f$.
```

---

<a id="v3-check-the-mass-conclusion"></a>
## Check the Mass Conclusion

Now return to the original comparison. The quick rule says that changing a variable absent from the frequency formula has no effect. The derivation explains why: changing $m$ multiplies both restoring force and inertia by the same factor.

```quiz
type: radio
id: pq3-p1-v3-original-check
shuffle: true
content: |-
  A bob of mass $m$ swings as a pendulum on a massless string with frequency $f$. If the bob's mass is doubled, what happens to the oscillation frequency?
options:
- id: pq3-p1-v3-original-check-a
  content: |-
    The new frequency is one-fourth the original frequency.
  feedback: |-
    This invents an inverse-square dependence on bob mass. Doubling $m$ doubles both the gravitational restoring force and the inertia, so mass cancels and the frequency remains $f$.
- id: pq3-p1-v3-original-check-b
  content: |-
    The new frequency is one-half the original frequency.
  feedback: |-
    This assumes that doubling mass doubles the period. Bob mass does not appear in $f=(2\pi)^{-1}\sqrt{g/L}$ because its effects on restoring force and inertia cancel, so changing $m$ alone leaves the frequency unchanged.
- id: pq3-p1-v3-original-check-c
  content: |-
    The new frequency is the same as the original frequency.
  correct: true
  feedback: |-
    Bob mass is absent from the frequency formula because restoring force and inertia scale together. With $g$ and $L$ unchanged, doubling $m$ leaves the frequency at $f$.
- id: pq3-p1-v3-original-check-d
  content: |-
    The new frequency is twice the original frequency.
  feedback: |-
    This treats mass as a direct frequency multiplier. Doubling $m$ doubles the restoring force but also doubles the inertia, so the tangential acceleration and frequency remain unchanged.
- id: pq3-p1-v3-original-check-e
  content: |-
    The new frequency is four times the original frequency.
  feedback: |-
    This introduces a mass dependence and then squares its change factor. Bob mass cancels entirely from the simple-pendulum frequency, so neither a factor of $2$ nor $4$ belongs in the result; the frequency remains $f$.
```

---

<a id="v3-summary"></a>
## Summary

When a pendulum parameter changes:

1. Start with $f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}$.
2. Check whether the changed parameter appears in the formula.
3. If it is absent, changing it alone does not change the frequency predicted by the model.
4. If it appears, translate its change factor through the square root or use the frequency ratio.

$$
\frac{f_2}{f_1}
=\sqrt{\frac{g_2}{g_1}\frac{L_1}{L_2}}.
$$

| Change | Frequency multiplier |
| --- | ---: |
| $m\to km$ | $1$ |
| $g\to kg$ | $\sqrt{k}$ |
| $L\to kL$ | $1/\sqrt{k}$ |

Mass is absent because the gravitational restoring force and the bob's inertia both scale with $m$ and cancel. The result assumes an ideal pendulum oscillating through small angles.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

[Quiz 3 Study Guide](../../2026-08-03-Q-3/Study-Guide.md)
Next: [Period of a Uniform Rod as a Physical Pendulum](../../../M4/2026-07-22-M4-2/Lessons/Problem-3.md)

Study guide index: 06/28

---
<!-- lesson-nav:end -->
