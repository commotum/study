# Converting Decibels to Intensity

<!--
lesson-id: 212-M5-056
topic-code: MTH212.M5.56
-->

## Table of Contents

- [Introduction](#introduction)
- [Isolate the Logarithm](#isolate-the-logarithm)
- [Rewrite in Exponential Form](#rewrite-in-exponential-form)
- [Combine With the Reference Intensity](#combine-with-the-reference-intensity)
- [Match the Source Problem](#match-the-source-problem)
- [Summary](#summary)

## Prerequisites

- Interpret $\log_{10}$ as a base-10 logarithm.
- Convert between $\log_{10}(x)=y$ and $x=10^y$.
- Multiply powers of ten by adding their exponents.

---

<a id="introduction"></a>
## Introduction

Sound intensity level $\beta$ compares an intensity $I$ with a positive reference intensity $I_0$:

$$
\beta=10\log_{10}\!\left(\frac{I}{I_0}\right).
$$

The logarithm is a **common logarithm**, so its base is $10$. Its argument is the dimensionless ratio $I/I_0$.

When $\beta$ and $I_0$ are known and the problem asks for $I$, undo the formula in reverse order:

$$
\frac{\beta}{10}=\log_{10}\!\left(\frac{I}{I_0}\right),
$$

$$
10^{\beta/10}=\frac{I}{I_0},
$$

$$
\boxed{I=I_0\,10^{\beta/10}}.
$$

The ratio $I/I_0$ has no units, as a logarithm requires. The final intensity has the same units as $I_0$.

---

<a id="isolate-the-logarithm"></a>
## Isolate the Logarithm

**Example:** A sound level is $50\ \mathrm{dB}$. What logarithmic equation results after dividing the decibel formula by $10$?

**Explanation**

The factor $10$ multiplies the entire logarithm, so divide both sides by $10$:

$$
\frac{50}{10}=\log_{10}\!\left(\frac{I}{I_0}\right),
$$

or

$$
5=\log_{10}\!\left(\frac{I}{I_0}\right).
$$

```quiz
type: radio
id: decibels-isolate-logarithm
content: |-
  Starting from $\beta=10\log_{10}(I/I_0)$, which equation correctly isolates the logarithm?
options:
- id: decibels-isolate-beta-over-ten
  content: |-
    $\displaystyle \log_{10}\!\left(\frac{I}{I_0}\right)=\frac{\beta}{10}$
  correct: true
  feedback: |-
    The coefficient $10$ multiplies the whole logarithm. Dividing both sides by $10$ gives $\log_{10}(I/I_0)=\beta/10$.
- id: decibels-isolate-ten-beta
  content: |-
    $\displaystyle \log_{10}\!\left(\frac{I}{I_0}\right)=10\beta$
  feedback: |-
    This multiplies by the coefficient instead of undoing it. Because the original right side is $10$ times the logarithm, isolate that logarithm by dividing $\beta$ by $10$.
- id: decibels-isolate-beta
  content: |-
    $\displaystyle \log_{10}\!\left(\frac{I}{I_0}\right)=\beta$
  feedback: |-
    This leaves the outside factor $10$ unaccounted for. The logarithm equals one-tenth of the decibel level, so it is $\beta/10$.
- id: decibels-isolate-ten-over-beta
  content: |-
    $\displaystyle \log_{10}\!\left(\frac{I}{I_0}\right)=\frac{10}{\beta}$
  feedback: |-
    Dividing both sides by $10$ does not take the reciprocal of $\beta$. It produces $\beta/10$ on the left, so the isolated logarithm is $\beta/10$.
```

---

<a id="rewrite-in-exponential-form"></a>
## Rewrite in Exponential Form

The conversion template is reversible:

$$
\log_b(a)=x
\quad\Longleftrightarrow\quad
a=b^x.
$$

For the decibel equation, the roles are

$$
b=10,
\qquad
a=\frac{I}{I_0},
\qquad
x=\frac{\beta}{10}.
$$

Therefore,

$$
\log_{10}\!\left(\frac{I}{I_0}\right)=\frac{\beta}{10}
\quad\Longleftrightarrow\quad
\frac{I}{I_0}=10^{\beta/10}.
$$

This works because the common logarithm reverses a base-$10$ exponential: $\log_{10}(10^x)=x$.

**Example:** For $\beta=30\ \mathrm{dB}$,

$$
\frac{I}{I_0}=10^{30/10}=10^3.
$$

Thus the intensity is $1000$ times the reference intensity.

```quiz
type: radio
id: decibels-to-intensity-ratio
content: |-
  A sound level is $40\ \mathrm{dB}$. What is the intensity ratio $I/I_0$?
options:
- id: decibels-ratio-ten-fourth
  content: |-
    $10^4$
  correct: true
  feedback: |-
    The decibel definition gives $I/I_0=10^{\beta/10}$. With $\beta=40\ \mathrm{dB}$, the exponent is $40/10=4$, so $I/I_0=10^4$.
- id: decibels-ratio-ten-fortieth
  content: |-
    $10^{40}$
  feedback: |-
    This uses the decibel value as the exponent without first removing the outside factor $10$. Divide by $10$ before exponentiating: $40/10=4$, so the ratio is $10^4$.
- id: decibels-ratio-four
  content: |-
    $4$
  feedback: |-
    The value $4$ is the logarithm of the ratio, not the ratio itself. Converting $\log_{10}(I/I_0)=4$ to exponential form gives $I/I_0=10^4$.
- id: decibels-ratio-ten-negative-fourth
  content: |-
    $10^{-4}$
  feedback: |-
    A positive $40\ \mathrm{dB}$ level means $I>I_0$, so the ratio must exceed $1$. The exponent is positive $40/10=4$, giving $10^4$ rather than $10^{-4}$.
```

---

<a id="combine-with-the-reference-intensity"></a>
## Combine With the Reference Intensity

After finding the dimensionless ratio, multiply by the reference intensity:

$$
I=I_0\,10^{\beta/10}.
$$

**Example:** Let $I_0=10^{-12}\ \mathrm{W/m^2}$ and $\beta=70\ \mathrm{dB}$. Then

$$
I=10^{-12}\,10^{70/10}
=10^{-12}\,10^7
=10^{-5}\ \mathrm{W/m^2}.
$$

The exponent check is $-12+7=-5$. Also, every increase of $10\ \mathrm{dB}$ multiplies intensity by $10$.

Two boundary checks help catch sign errors. At $0\ \mathrm{dB}$, the ratio is $10^0=1$, so $I=I_0$. For a positive decibel level, $10^{\beta/10}>1$, so the intensity must exceed $I_0$.

```quiz
type: radio
id: decibels-reference-intensity
content: |-
  Use $I_0=10^{-12}\ \mathrm{W/m^2}$. What intensity corresponds to $80\ \mathrm{dB}$?
options:
- id: decibels-reference-one-e-minus-four
  content: |-
    $1.0\times10^{-4}\ \mathrm{W/m^2}$
  correct: true
  feedback: |-
    Converting from level to intensity gives $I=I_0 10^{\beta/10}$. Here $I=10^{-12}10^8=10^{-4}\ \mathrm{W/m^2}$.
- id: decibels-reference-one-e-eight
  content: |-
    $1.0\times10^8\ \mathrm{W/m^2}$
  feedback: |-
    The factor $10^8$ is the dimensionless ratio $I/I_0$, not the intensity. Multiplying it by $I_0=10^{-12}\ \mathrm{W/m^2}$ gives $10^{-4}\ \mathrm{W/m^2}$.
- id: decibels-reference-one-e-minus-twenty
  content: |-
    $1.0\times10^{-20}\ \mathrm{W/m^2}$
  feedback: |-
    This divides by $10^8$ instead of multiplying by the intensity ratio. A positive $80\ \mathrm{dB}$ level is above the reference, so use $10^{-12}10^8=10^{-4}\ \mathrm{W/m^2}$.
- id: decibels-reference-eight-e-minus-twelve
  content: |-
    $8.0\times10^{-12}\ \mathrm{W/m^2}$
  feedback: |-
    The exponent $8=80/10$ is not itself the intensity ratio. The ratio is $10^8$, so multiply $10^{-12}$ by $10^8$ and add exponents to obtain $10^{-4}\ \mathrm{W/m^2}$.
```

---

<a id="match-the-source-problem"></a>
## Match the Source Problem

Apply the same sequence: divide the level by $10$, use that result as a base-10 exponent, and multiply the resulting ratio by $I_0$.

```quiz
type: radio
id: khadley-intensity-q3
content: |-
  **Question 3**

  What intensity corresponds to a sound level of $60\ \mathrm{dB}$? Use $I_0=10^{-12}\ \mathrm{W/m^2}$ and enter $\mathrm{W/m^2}$:
options:
- id: khadley-intensity-q3-one-e-minus-six
  content: |-
    `1.0e-6`
  correct: true
  feedback: |-
    From $\beta=10\log_{10}(I/I_0)$, $I=I_0 10^{\beta/10}=10^{-12}10^6=1.0\times10^{-6}\ \mathrm{W/m^2}$, so the requested entry is `1.0e-6`.
- id: khadley-intensity-q3-one-e-six
  content: |-
    `1.0e6`
  feedback: |-
    This is the ratio $I/I_0=10^6$, not the intensity. Multiply that dimensionless ratio by $I_0=10^{-12}\ \mathrm{W/m^2}$ to obtain `1.0e-6` $\mathrm{W/m^2}$.
- id: khadley-intensity-q3-one-e-minus-eighteen
  content: |-
    `1.0e-18`
  feedback: |-
    This subtracts the positive exponent $6$ from $-12$. The formula multiplies $I_0$ by $10^6$, so powers of ten add: $-12+6=-6$, giving `1.0e-6`.
- id: khadley-intensity-q3-six-e-minus-twelve
  content: |-
    `6.0e-12`
  feedback: |-
    The value $6=60/10$ is the logarithm of the ratio, not the ratio itself. Exponentiate first to get $I/I_0=10^6$, then multiply by $I_0$.
```

---

<a id="summary"></a>
## Summary

- Cue: sound level $\beta$ and reference intensity $I_0$ are given, and intensity $I$ is requested.
- Divide first: $\log_{10}(I/I_0)=\beta/10$.
- Map the conversion: base $10$, argument $I/I_0$, exponent $\beta/10$.
- Undo the common logarithm: $I/I_0=10^{\beta/10}$, since $\log_{10}(10^x)=x$.
- Multiply by the reference: $I=I_0 10^{\beta/10}$.
- Check: $0\ \mathrm{dB}$ gives $I=I_0$, and a $10\ \mathrm{dB}$ increase multiplies intensity by $10$.
- Main trap: $\beta/10$ is the exponent, not the intensity ratio itself.
