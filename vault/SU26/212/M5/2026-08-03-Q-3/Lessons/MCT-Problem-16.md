# Resolve Beat-Frequency Ambiguity

<!--
lesson-id: 212-M5-074
topic-code: MTH212.M5.74
-->

## Table of Contents

- [Introduction](#introduction)
- [Paired-Lecture Mechanism: Why Beats Occur](#lecture-beat-mechanism)
- [Source-Video Worked Problem: Direct Beat Rate](#source-direct-beat-rate)
- [Source-Video Worked Problem: Count Beats and Keep Both Candidates](#source-count-and-candidates)
- [Source-Video Worked Problem: Intersect Candidate Sets](#source-candidate-intersection)
- [Controlled Variation: Use an Ordering Clue](#ordering-clue)
- [Summary](#summary)

## Prerequisites

- Subtract frequencies measured in hertz.
- Interpret frequency as a count per unit time.
- Use absolute value as the nonnegative distance between two numbers.
- Find the common element of two small sets.

---

<a id="introduction"></a>
## Introduction

When two nearby tones produce beats, the beat frequency is the absolute difference between their frequencies:

$$
\boxed{f_b=\left|f_1-f_2\right|}.
$$

Look for phrases such as “beats per second,” “two nearby tones,” or “a tuning fork compared with a reference.” Treat the beat frequency as a distance on the frequency scale.

| Given information | Action |
|---|---|
| two tone frequencies | subtract and take the absolute value |
| a beat count over a time interval | calculate $f_b=N_b/t$ first |
| one reference frequency and $f_b$ | keep both candidates, $f_u=f_r\pm f_b$ |
| a second comparison or an ordering clue | retain only the candidate that satisfies it |

The two-candidate step follows directly from

$$
\left|f_u-f_r\right|=f_b.
$$

Split the absolute-value equation into its two branches:

$$
\begin{aligned}
f_u-f_r&=f_b
\quad\text{or}\quad
f_u-f_r=-f_b,\\
f_u&=f_r+f_b
\quad\text{or}\quad
f_u=f_r-f_b.
\end{aligned}
$$

If the unknown lies below the reference, then $f_u=f_r-f_b$. If it lies above, then $f_u=f_r+f_b$. A beat measurement alone does not say which side is correct:

$$
\boxed{f_u\in\{f_r-f_b,\ f_r+f_b\}}.
$$

Beat frequency is not the average $(f_1+f_2)/2$. It is also never negative. When $f_b=0$, the two candidates coincide because the tones have the same frequency.

---

<a id="lecture-beat-mechanism"></a>
## Paired-Lecture Mechanism: Why Beats Occur

The M5-4 lecture notes explain the mechanism without a trigonometric derivation. Two waves with similar but unequal frequencies repeatedly move into and out of phase. Their superposition alternates between constructive interference, when the sound amplitude is larger, and destructive interference, when it is smaller. The rate of this swell-and-fade pattern is $|f_1-f_2|$.

---

<a id="source-direct-beat-rate"></a>
## Source-Video Worked Problem: Direct Beat Rate

The frame-verified opening problem in M-OMq4QsPfY at 0:00:01-0:00:44 gives two tones:

$$
f_1=425\,\mathrm{Hz},
\qquad
f_2=436\,\mathrm{Hz}.
$$

Subtract in either order and take the absolute value:

$$
\begin{aligned}
f_b
&=\left|f_1-f_2\right|\\
&=\left|425-436\right|\,\mathrm{Hz}\\
&=\left|-11\right|\,\mathrm{Hz}\\
&=\boxed{11\,\mathrm{Hz}}.
\end{aligned}
$$

The result means $11$ amplitude swells per second. The average frequency,

$$
\frac{425+436}{2}=430.5\,\mathrm{Hz},
$$

is not the beat rate.

**Source-caption corrections.** The automatic captions repeatedly render “beat frequency” as “beak frequency” or “b frequency.” Later they render “tuning fork” as “24” or “two and four.” The video context and visible prompts identify beat frequency and tuning fork; none of the numerical values change.

```quiz
type: radio
id: mct-p16-direct-beat-rate
shuffle: true
content: |-
  Two nearby tones have frequencies $512\,\mathrm{Hz}$ and $519\,\mathrm{Hz}$. What beat frequency do they produce?
options:
- id: mct-p16-direct-beat-rate-a
  content: |-
    $515.5\,\mathrm{Hz}$
  feedback: |-
    This is the average of the two tone frequencies. Beat frequency measures their separation, so use the absolute difference instead.
- id: mct-p16-direct-beat-rate-b
  content: |-
    $-7\,\mathrm{Hz}$
  feedback: |-
    The subtraction $512-519$ is negative, but beat frequency is an absolute difference. Taking the magnitude gives a nonnegative rate.
- id: mct-p16-direct-beat-rate-c
  content: |-
    $7\,\mathrm{Hz}$
  correct: true
  feedback: |-
    Beat frequency is the absolute separation of the tones: $f_b=|512-519|=7\,\mathrm{Hz}$.
- id: mct-p16-direct-beat-rate-d
  content: |-
    $1031\,\mathrm{Hz}$
  feedback: |-
    This adds the tone frequencies. The slow beat pattern comes from their difference, not their sum.
- id: mct-p16-direct-beat-rate-e
  content: |-
    $0.143\,\mathrm{Hz}$
  feedback: |-
    This takes the reciprocal of the $7\,\mathrm{Hz}$ difference. That reciprocal is the beat period, about $0.143\,\mathrm{s}$, not the beat frequency.
```

---

<a id="source-count-and-candidates"></a>
## Source-Video Worked Problem: Count Beats and Keep Both Candidates

The second problem in M-OMq4QsPfY at 0:00:46-0:02:11 states that a $360\,\mathrm{Hz}$ tone and an unknown tuning fork produce $32$ beats in $4\,\mathrm{s}$.

First convert the count to a rate:

$$
\begin{aligned}
f_b
&=\frac{N_b}{t}\\
&=\frac{32\ \text{beats}}{4\,\mathrm{s}}\\
&=\boxed{8\,\mathrm{Hz}}.
\end{aligned}
$$

The count $32$ is not itself a frequency. It becomes a frequency only after division by the elapsed time.

Now solve the absolute-value equation:

$$
\left|f_u-360\right|=8.
$$

The unknown fork can be $8\,\mathrm{Hz}$ below or above the reference:

$$
\begin{aligned}
f_u&=360-8=\boxed{352\,\mathrm{Hz}},\\
f_u&=360+8=\boxed{368\,\mathrm{Hz}}.
\end{aligned}
$$

Both candidates pass the original measurement:

$$
|352-360|=8,
\qquad
|368-360|=8.
$$

Nothing in this one comparison selects one of them, so both must be retained.

```quiz
type: radio
id: mct-p16-count-and-candidates
shuffle: true
content: |-
  An unknown tuning fork and a $440\,\mathrm{Hz}$ reference produce $54$ beats in $6.0\,\mathrm{s}$. What are the two possible frequencies of the unknown fork?
options:
- id: mct-p16-count-and-candidates-a
  content: |-
    $386\,\mathrm{Hz}$ or $494\,\mathrm{Hz}$
  feedback: |-
    These values use the total count $54$ as though it were the beat frequency. Divide by $6.0\,\mathrm{s}$ first to obtain $f_b=9\,\mathrm{Hz}$.
- id: mct-p16-count-and-candidates-b
  content: |-
    $431\,\mathrm{Hz}$ or $449\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The beat rate is $54/6.0=9\,\mathrm{Hz}$. An absolute difference of $9\,\mathrm{Hz}$ from the $440\,\mathrm{Hz}$ reference gives $440-9=431\,\mathrm{Hz}$ and $440+9=449\,\mathrm{Hz}$.
- id: mct-p16-count-and-candidates-c
  content: |-
    $434\,\mathrm{Hz}$ or $446\,\mathrm{Hz}$
  feedback: |-
    These values use the elapsed time $6.0$ as the frequency separation. The separation is the beat count divided by time, $54/6.0=9\,\mathrm{Hz}$.
- id: mct-p16-count-and-candidates-d
  content: |-
    $449\,\mathrm{Hz}$ only
  feedback: |-
    The upper candidate is valid, but an absolute difference does not identify a side of the reference. The lower candidate $440-9=431\,\mathrm{Hz}$ is equally consistent.
- id: mct-p16-count-and-candidates-e
  content: |-
    $9\,\mathrm{Hz}$
  feedback: |-
    This is the beat frequency, not the tuning fork's frequency. Use that $9\,\mathrm{Hz}$ separation on both sides of the $440\,\mathrm{Hz}$ reference.
```

---

<a id="source-candidate-intersection"></a>
## Source-Video Worked Problem: Intersect Candidate Sets

The third problem in M-OMq4QsPfY at 0:02:14-0:03:36 gives two measurements for the same unknown fork:

- it makes $5\,\mathrm{Hz}$ beats with a $415\,\mathrm{Hz}$ reference;
- it makes $6\,\mathrm{Hz}$ beats with a $426\,\mathrm{Hz}$ reference.

Generate both candidates from each measurement. The first comparison gives

$$
C_1=\{415-5,\ 415+5\}
=\{410,\ 420\}\,\mathrm{Hz}.
$$

The second gives

$$
C_2=\{426-6,\ 426+6\}
=\{420,\ 432\}\,\mathrm{Hz}.
$$

The unknown must satisfy both measurements, so keep the intersection:

$$
C_1\cap C_2
=\{410,420\}\cap\{420,432\}
=\boxed{\{420\}\,\mathrm{Hz}}.
$$

Check the selected frequency against both references:

$$
|420-415|=5,
\qquad
|420-426|=6.
$$

Thus the tuning fork frequency is

$$
\boxed{f_u=420\,\mathrm{Hz}}.
$$

Taking the union of the candidate sets would keep values that satisfy only one measurement. The word “and” requires the common candidate.

```quiz
type: radio
id: mct-p16-candidate-intersection
shuffle: true
content: |-
  An unknown fork produces $4\,\mathrm{Hz}$ beats with a $508\,\mathrm{Hz}$ reference and $7\,\mathrm{Hz}$ beats with a $519\,\mathrm{Hz}$ reference. What is the unknown frequency?
options:
- id: mct-p16-candidate-intersection-a
  content: |-
    $504\,\mathrm{Hz}$
  feedback: |-
    This is a candidate from the first comparison, but it is $15\,\mathrm{Hz}$ from $519\,\mathrm{Hz}$ rather than $7\,\mathrm{Hz}$. A valid frequency must pass both measurements.
- id: mct-p16-candidate-intersection-b
  content: |-
    $526\,\mathrm{Hz}$
  feedback: |-
    This is a candidate from the second comparison, but it is $18\,\mathrm{Hz}$ from $508\,\mathrm{Hz}$ rather than $4\,\mathrm{Hz}$. Intersect the two candidate sets.
- id: mct-p16-candidate-intersection-c
  content: |-
    $513.5\,\mathrm{Hz}$
  feedback: |-
    This averages the two reference frequencies. The references are separate absolute-difference conditions, so generate candidates from each beat rate instead.
- id: mct-p16-candidate-intersection-d
  content: |-
    $512\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The candidate sets are $\{504,512\}\,\mathrm{Hz}$ and $\{512,526\}\,\mathrm{Hz}$. Their only common value is $512\,\mathrm{Hz}$, which is $4\,\mathrm{Hz}$ from $508$ and $7\,\mathrm{Hz}$ from $519$.
- id: mct-p16-candidate-intersection-e
  content: |-
    Any of $504\,\mathrm{Hz}$, $512\,\mathrm{Hz}$, or $526\,\mathrm{Hz}$
  feedback: |-
    This combines the candidate sets as a union. The same fork produced both beat measurements, so its frequency must lie in their intersection; only $512\,\mathrm{Hz}$ does.
```

---

<a id="ordering-clue"></a>
## Controlled Variation: Use an Ordering Clue

A second reference is not the only way to resolve the two candidates. A statement that the unknown tone is higher or lower than the reference also selects a side.

Suppose an unknown fork makes $12\,\mathrm{Hz}$ beats with a $460\,\mathrm{Hz}$ reference. The beat measurement alone gives

$$
f_u\in\{460-12,\ 460+12\}
=\{448,\ 472\}\,\mathrm{Hz}.
$$

If an independent calibration says the unknown is below $460\,\mathrm{Hz}$, keep the lower candidate:

$$
\boxed{f_u=448\,\mathrm{Hz}}.
$$

The ordering clue filters candidates after the absolute-difference equation has produced them; it does not change the beat-frequency formula.

```quiz
type: radio
id: mct-p16-ordering-clue
shuffle: true
content: |-
  An unknown tone makes $9\,\mathrm{Hz}$ beats with a $625\,\mathrm{Hz}$ reference. A separate calibration shows that the unknown frequency is lower than $625\,\mathrm{Hz}$. What is the unknown frequency?
options:
- id: mct-p16-ordering-clue-a
  content: |-
    $616\,\mathrm{Hz}$
  correct: true
  feedback: |-
    The beat measurement gives $625\pm9$, or $616\,\mathrm{Hz}$ and $634\,\mathrm{Hz}$. The independent “lower” clue selects $616\,\mathrm{Hz}$.
- id: mct-p16-ordering-clue-b
  content: |-
    $634\,\mathrm{Hz}$
  feedback: |-
    This is the upper candidate from $625+9$. It fits the beat rate but conflicts with the independent statement that the unknown lies below the reference.
- id: mct-p16-ordering-clue-c
  content: |-
    $9\,\mathrm{Hz}$
  feedback: |-
    This is the separation between the tones, not the unknown tone's frequency. Apply that separation to the $625\,\mathrm{Hz}$ reference, then use the ordering clue.
- id: mct-p16-ordering-clue-d
  content: |-
    $69.4\,\mathrm{Hz}$
  feedback: |-
    Dividing the reference frequency by the beat frequency does not solve an absolute-difference equation. The unknown must be $9\,\mathrm{Hz}$ away from $625\,\mathrm{Hz}$.
- id: mct-p16-ordering-clue-e
  content: |-
    $625\,\mathrm{Hz}$
  feedback: |-
    Equal frequencies would produce $|625-625|=0\,\mathrm{Hz}$ beats. The observed $9\,\mathrm{Hz}$ beat rate requires a $9\,\mathrm{Hz}$ separation.
```

---

<a id="summary"></a>
## Summary

- Beats from two nearby tones occur as their interference alternates between constructive and destructive.
- Calculate the beat rate with
  $$
  f_b=|f_1-f_2|.
  $$
- If beats are counted over time, calculate $f_b=N_b/t$ before solving for a tone frequency.
- One reference and one beat rate usually give two candidates:
  $$
  f_u=f_r-f_b
  \qquad\text{or}\qquad
  f_u=f_r+f_b.
  $$
- Retain both candidates until a second comparison or an ordering clue removes one.
- For two comparisons, form both candidate sets and keep their intersection.
- Check the selected frequency in every original absolute-difference condition.
- Do not replace the absolute difference with an average, a signed difference, or the raw beat count.

<!-- lesson-nav:start -->
---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---
<!-- lesson-nav:end -->
