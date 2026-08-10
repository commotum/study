# Changing a Source Position for Constructive Interference

<!--
lesson-id: 212-M5-058
topic-code: MTH212.M5.58
-->

## Table of Contents

- [Introduction](#introduction)
- [Convert Source Separation to Path Difference](#convert-source-separation-to-path-difference)
- [Update the Difference After Moving a Source](#update-the-difference-after-moving-a-source)
- [Solve for Every Constructive Move](#solve-for-every-constructive-move)
- [Use Phase Periodicity as a Check](#use-phase-periodicity-as-a-check)
- [Original Problem Check](#original-problem-check)
- [Summary](#summary)

## Prerequisites

- Interpret wavelength $\lambda$ as one complete spatial cycle.
- Distinguish a source's position from the distance its wave travels to an observer.
- Use signed forward and backward displacements on a line.
- Recognize integer multiples, including zero and negative multiples.

---

<a id="introduction"></a>
## Introduction

Two in-phase sources interfere completely constructively at a forward observation point when their path-length difference is an integer number of wavelengths:

$$
\boxed{\Delta r=n\lambda,\qquad n\in\mathbb Z}.
$$

The integer may be zero. Equal path lengths give $\Delta r=0=0\lambda$, so waves emitted in phase also arrive in phase.

For sources on the same forward line, let Speaker 2 initially be a distance $d$ in front of Speaker 1. A distant point in front is then $d$ farther from Speaker 1 than from Speaker 2, so

$$
\Delta r=r_1-r_2=d.
$$

If Speaker 1 moves by signed displacement $s$, where $s>0$ means forward and $s<0$ means backward, the new path difference is

$$
\boxed{\Delta r_{\text{new}}=d-s}.
$$

The recognition cue is an in-phase source pair, a wavelength, an initial forward offset, and proposed source movements. Update $d-s$ for each move and keep the choices that make it an integer multiple of $\lambda$.

---

<a id="convert-source-separation-to-path-difference"></a>
## Convert Source Separation to Path Difference

**Example:** Two in-phase speakers emit forward waves of wavelength $3.0\ \mathrm m$. Speaker 2 is $1.5\ \mathrm m$ in front of Speaker 1. Classify their current forward interference.

**Explanation**

For a forward observer, the rear speaker's wave travels the extra source separation:

$$
\Delta r=1.5\ \mathrm m
=\frac12(3.0\ \mathrm m)
=\frac{\lambda}{2}.
$$

An integer wavelength gives complete constructive interference, while a half-integer wavelength gives complete destructive interference for in-phase sources:

$$
\Delta r=\left(n+\frac12\right)\lambda.
$$

Here $\Delta r=\lambda/2$, so the waves arrive completely out of phase and interfere completely destructively.

```quiz
type: radio
id: source-separation-path-difference
shuffle: true
content: |-
  Two in-phase sources emit forward waves with $\lambda=1.6\ \mathrm m$. Source 2 is $0.8\ \mathrm m$ in front of Source 1. What is their current forward interference?
options:
- id: completely-destructive
  content: |-
    Completely destructive
  correct: true
  feedback: |-
    The rear source's wave travels an extra $0.8\ \mathrm m=\lambda/2$. For in-phase sources, a half-integer-wavelength path difference produces a phase difference of $\pi$ and complete destructive interference.
- id: completely-constructive
  content: |-
    Completely constructive
  feedback: |-
    Complete constructive interference requires $\Delta r=n\lambda$. Here the source offset is $\lambda/2$, not an integer wavelength, so the waves arrive out of phase.
- id: quarter-cycle
  content: |-
    Neither complete type because the path difference is $\lambda/4$
  feedback: |-
    The numerical offset is $0.8\ \mathrm m$, while $\lambda/4=0.4\ \mathrm m$. The actual path difference is $\lambda/2$, which gives complete destructive interference.
- id: need-amplitudes
  content: |-
    It cannot be classified without the amplitudes.
  feedback: |-
    Amplitudes determine the size of the resulting maximum or minimum, but the stated equal-frequency phase condition and path difference determine whether arrival is in phase or out of phase. Here $\Delta r=\lambda/2$ is completely destructive.
- id: need-observer-distance
  content: |-
    It cannot be classified without the exact forward observer distance.
  feedback: |-
    Along the common forward line, the difference in travel distances equals the fixed source separation. Moving the observer farther forward adds the same distance to both paths, so $\Delta r=0.8\ \mathrm m=\lambda/2$ remains unchanged.
```

---

<a id="update-the-difference-after-moving-a-source"></a>
## Update the Difference After Moving a Source

**Example:** Speaker 2 begins $0.75\ \mathrm m$ in front of Speaker 1, and $\lambda=1.0\ \mathrm m$. Speaker 1 moves backward $0.25\ \mathrm m$. Determine the new interference condition.

**Explanation**

Use $s=-0.25\ \mathrm m$ because backward is negative. Then

$$
\begin{aligned}
\Delta r_{\text{new}}
&=d-s\\
&=0.75\ \mathrm m-(-0.25\ \mathrm m)\\
&=1.00\ \mathrm m\\
&=\lambda.
\end{aligned}
$$

The backward move increases the separation. Because the new path difference is one full wavelength, the forward waves arrive in phase and interfere completely constructively.

```quiz
type: radio
id: moving-source-update-path-difference
shuffle: true
content: |-
  Source 2 is $0.60\ \mathrm m$ in front of Source 1, and the in-phase sources emit waves with $\lambda=1.2\ \mathrm m$. Source 1 moves forward $0.60\ \mathrm m$. What happens in the forward direction?
options:
- id: zero-difference-constructive
  content: |-
    The new path difference is $0$, so the interference is completely constructive.
  correct: true
  feedback: |-
    A forward move of Source 1 reduces the initial separation: $\Delta r_{\text{new}}=0.60-0.60=0$. Since $0=0\lambda$ is an integer multiple, the in-phase waves arrive completely constructively.
- id: one-wavelength-constructive
  content: |-
    The new path difference is $1.2\ \mathrm m$, so the interference is completely constructive.
  feedback: |-
    The conclusion would be constructive if the new difference were $\lambda$, but a forward move closes the $0.60\ \mathrm m$ gap instead of adding to it. The actual new difference is $0$.
- id: half-wavelength-destructive
  content: |-
    The new path difference remains $0.60\ \mathrm m$, so the interference is completely destructive.
  feedback: |-
    This ignores the source displacement. Moving Source 1 forward by the entire initial offset aligns the sources, reducing the path difference from $\lambda/2$ to $0$.
- id: negative-half-destructive
  content: |-
    The new path difference is $-0.60\ \mathrm m$, so the interference is completely destructive.
  feedback: |-
    Subtracting the forward move twice gives the wrong geometry. Speaker 1 moves from behind Source 2 to the same position, so the new separation and path difference are exactly zero.
- id: move-breaks-in-phase
  content: |-
    Moving a source makes complete interference impossible.
  feedback: |-
    A position change alters propagation phase through path length, but it does not prevent the waves from arriving in phase. Here the move equalizes the paths, which produces complete constructive interference.
```

---

<a id="solve-for-every-constructive-move"></a>
## Solve for Every Constructive Move

**Example:** Speaker 2 begins $0.30\ \mathrm m$ ahead of Speaker 1, and $\lambda=1.2\ \mathrm m$. Find two nearest moves of Speaker 1 that produce complete constructive interference.

**Explanation**

Set the updated difference equal to an integer wavelength:

$$
d-s=n\lambda.
$$

Solve for the signed move:

$$
\boxed{s=d-n\lambda}.
$$

Two nearby integer choices give

$$
\begin{aligned}
n=0:\qquad s&=0.30\ \mathrm m,
&\text{move forward }0.30\ \mathrm m,\\
n=1:\qquad s&=0.30\ \mathrm m-1.20\ \mathrm m=-0.90\ \mathrm m,
&\text{move backward }0.90\ \mathrm m.
\end{aligned}
$$

The first move makes the path difference zero. The second makes it one wavelength. Both are completely constructive because constructive solutions repeat every wavelength.

```quiz
type: radio
id: all-constructive-source-moves
shuffle: true
content: |-
  Speaker 2 starts $0.40\ \mathrm m$ in front of Speaker 1, and $\lambda=1.0\ \mathrm m$. Which pair gives the two nearest moves of Speaker 1 that make the forward interference completely constructive?
options:
- id: forward-040-backward-060
  content: |-
    Forward $0.40\ \mathrm m$ and backward $0.60\ \mathrm m$
  correct: true
  feedback: |-
    Constructive moves satisfy $s=d-n\lambda$. With $d=0.40\ \mathrm m$, $n=0$ gives $s=+0.40\ \mathrm m$, while $n=1$ gives $s=-0.60\ \mathrm m$. These create path differences $0$ and $\lambda$.
- id: forward-040-only
  content: |-
    Forward $0.40\ \mathrm m$ only
  feedback: |-
    Moving forward $0.40\ \mathrm m$ is constructive because it makes $\Delta r=0$, but it is not the only nearby solution. Moving backward $0.60\ \mathrm m$ makes $\Delta r=1.0\ \mathrm m=\lambda$ and is also constructive.
- id: forward-060-backward-040
  content: |-
    Forward $0.60\ \mathrm m$ and backward $0.40\ \mathrm m$
  feedback: |-
    These moves produce path differences $-0.20\ \mathrm m$ and $0.80\ \mathrm m$, neither an integer multiple of the $1.0\ \mathrm m$ wavelength. The displacements must solve $0.40-s=n(1.0)$.
- id: forward-020-backward-020
  content: |-
    Forward $0.20\ \mathrm m$ and backward $0.20\ \mathrm m$
  feedback: |-
    These moves leave differences $0.20\ \mathrm m$ and $0.60\ \mathrm m$. Constructive interference requires $0$, $1.0\ \mathrm m$, or another integer wavelength instead.
- id: backward-060-only
  content: |-
    Backward $0.60\ \mathrm m$ only
  feedback: |-
    Moving backward $0.60\ \mathrm m$ is constructive because it makes the difference one wavelength, but moving forward $0.40\ \mathrm m$ also works by making the difference zero.
```

---

<a id="use-phase-periodicity-as-a-check"></a>
## Use Phase Periodicity as a Check

**Example:** Explain why path differences of $0$, $\lambda$, and $-\lambda$ all give complete constructive interference for in-phase sources.

**Explanation**

Path difference and propagation phase difference are related by

$$
\Delta\phi=\frac{2\pi}{\lambda}\Delta r.
$$

For the three path differences,

$$
\Delta r=0,\lambda,-\lambda
\qquad\Longrightarrow\qquad
\Delta\phi=0,2\pi,-2\pi.
$$

These angles differ by complete turns and represent the same relative phase. More generally, $\Delta r=n\lambda$ gives $\Delta\phi=2\pi n$, so every integer-wavelength path difference is completely constructive.

By contrast, $\Delta r=\lambda/2$ gives $\Delta\phi=\pi$, which puts the arriving waves completely out of phase.

```quiz
type: radio
id: path-difference-phase-periodicity
shuffle: true
content: |-
  Two in-phase sources have a signed path difference $\Delta r=-2\lambda$ at an observation point. What is their interference there?
options:
- id: constructive-minus-two-lambda
  content: |-
    Completely constructive
  correct: true
  feedback: |-
    The phase difference is $(2\pi/\lambda)(-2\lambda)=-4\pi$, which is two complete turns from zero phase. Any integer-wavelength signed path difference gives complete constructive interference.
- id: destructive-because-negative
  content: |-
    Completely destructive because the path difference is negative
  feedback: |-
    The sign indicates which path is longer; it does not by itself determine constructive or destructive interference. Since $-2\lambda$ is an integer multiple of $\lambda$, the waves arrive in phase.
- id: destructive-two-lambda
  content: |-
    Completely destructive because the paths differ by two wavelengths
  feedback: |-
    Two wavelengths correspond to a phase change of $4\pi$, which is two complete cycles. Half-integer wavelengths, not integer wavelengths, produce complete destructive interference for in-phase sources.
- id: neither-four-pi
  content: |-
    Neither, because the phase difference is $-4\pi$
  feedback: |-
    A phase difference of $-4\pi$ is coterminal with $0$ and represents the same phase alignment. Therefore the interference is completely constructive.
- id: need-absolute-distance
  content: |-
    It cannot be determined without both absolute path lengths.
  feedback: |-
    Interference depends on the path-length difference, not the separate absolute lengths. The given difference $-2\lambda$ already determines a $-4\pi$ phase difference and complete constructive interference.
```

---

<a id="original-problem-check"></a>
## Original Problem Check

**Example:** Solve the original select-all problem before checking the answer set.

**Explanation**

> **Question 1**
>
> Two in-phase speakers emit waves with $\lambda=2.0\ \mathrm m$. Speaker 2 is $1.0\ \mathrm m$ in front of Speaker 1. Which changes make their forward waves completely constructive? Select all that apply.
>
> ![[../Source/Images/speakers.jpg]]
>
> - Move Speaker 1 forward $1.0\ \mathrm m$.
> - Move Speaker 1 forward $0.5\ \mathrm m$.
> - Move Speaker 1 backward $0.5\ \mathrm m$.
> - Move Speaker 1 backward $1.0\ \mathrm m$.
> - Do not move either speaker.

The original answer form requires selecting every valid change. Take forward as positive, so $d=1.0\ \mathrm m$ and

$$
\Delta r_{\text{new}}=1.0\ \mathrm m-s.
$$

Check each proposed $s$ against $\Delta r_{\text{new}}=n(2.0\ \mathrm m)$.

```quiz
type: radio
id: khadley-phase-q1
shuffle: true
content: |-
  Which complete set of choices should be selected in the original problem?
options:
- id: original-forward-one-and-backward-one
  content: |-
    Move Speaker 1 forward $1.0\ \mathrm m$ and move Speaker 1 backward $1.0\ \mathrm m$.
  correct: true
  feedback: |-
    Forward $1.0\ \mathrm m$ makes the path difference $0$, while backward $1.0\ \mathrm m$ makes it $2.0\ \mathrm m=\lambda$. Both are integer-wavelength differences, so these and only these listed changes are completely constructive.
- id: original-forward-one-only
  content: |-
    Move Speaker 1 forward $1.0\ \mathrm m$ only.
  feedback: |-
    Moving forward $1.0\ \mathrm m$ is valid because it aligns the speakers, but the original response requires every valid choice. Moving backward $1.0\ \mathrm m$ also works because it creates a one-wavelength path difference.
- id: original-half-meter-pair
  content: |-
    Move Speaker 1 forward $0.5\ \mathrm m$ and move Speaker 1 backward $0.5\ \mathrm m$.
  feedback: |-
    These moves leave path differences $0.5\ \mathrm m=\lambda/4$ and $1.5\ \mathrm m=3\lambda/4$. Neither is an integer wavelength, so neither produces complete constructive interference.
- id: original-backward-one-only
  content: |-
    Move Speaker 1 backward $1.0\ \mathrm m$ only.
  feedback: |-
    Moving backward $1.0\ \mathrm m$ is valid because it makes the difference one wavelength, but moving forward $1.0\ \mathrm m$ is also valid because zero is an integer multiple of the wavelength.
- id: original-unchanged-and-half-meter
  content: |-
    Do not move either speaker, and select both $0.5\ \mathrm m$ moves.
  feedback: |-
    Unchanged, the difference is $1.0\ \mathrm m=\lambda/2$, which is completely destructive. The two half-meter moves give $\lambda/4$ and $3\lambda/4$, so none of these three choices is completely constructive.
```

---

<a id="summary"></a>
## Summary

For in-phase sources on a common forward line:

1. Let $d$ be how far Source 2 begins in front of Source 1.
2. Give Source 1's move a sign: forward $s>0$, backward $s<0$.
3. Update the path difference:
   $$
   \Delta r_{\text{new}}=d-s.
   $$
4. Require complete constructive interference:
   $$
   d-s=n\lambda,\qquad n\in\mathbb Z.
   $$
5. Equivalently, find all allowed source moves from
   $$
   s=d-n\lambda.
   $$

Zero and every positive or negative integer multiple of $\lambda$ are constructive because their phase differences differ by whole turns. The main traps are treating $\lambda/2$ as constructive, forgetting that zero is an integer multiple, or reversing whether a forward move increases or decreases the source separation.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
