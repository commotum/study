# The Second Fundamental Theorem of Calculus

<!--
lesson-id: 613
topic-code: MF3.9.4.2
-->

## Table of Contents

- [Introduction](#introduction)
- [Applying the Second Fundamental Theorem of Calculus](#applying-the-second-fundamental-theorem-of-calculus)
- [Applying the Second Fundamental Theorem of Calculus by Interchanging the Limits of Integration](#applying-the-second-fundamental-theorem-of-calculus-by-interchanging-the-limits-of-integration)
- [Applying the Second Fundamental Theorem of Calculus Using the Chain Rule](#applying-the-second-fundamental-theorem-of-calculus-using-the-chain-rule)
- [Applying the Second Fundamental Theorem of Calculus With Two Variable Limits](#applying-the-second-fundamental-theorem-of-calculus-with-two-variable-limits)

## Prerequisites

- [The Integral as an Accumulation Function](<9.4.1. The Integral as an Accumulation Function.md>)

---

<a id="introduction"></a>
## Introduction

The **second fundamental theorem of calculus** (abbreviated FTC II) states the following:

> *If a function $f(x)$ is continuous on $[a,b]$ with $x\in(a,b)$, and the accumulation function $F(x)$ is defined as*
> $F(x) = \int_a^x f(t)\,\textrm d t$,
> *then the derivative of $F(x)$ is given by*
> $F'(x) = \dfrac {\textrm d} {\textrm dx} \int_a^x f(t) \,\textrm d t = f(x)$.

Loosely speaking, taking the derivative "cancels out" the integral and leaves us with the integrand. This happens because the derivative and the integral are *opposite* operations.

To demonstrate how this works, let's define the accumulation function $F(x)$ as

$$
F(x)=\int^{x}_{2} \sin(t^2)\,\textrm d t
$$

Suppose that we want to differentiate this function to find $F'(x)$. Let's start by differentiating both sides with respect to $x$, which gives

$$
F'(x) = \dfrac{\textrm{d}}{\textrm{d}x}\int^{x}_{2} \sin(t^2)\,\textrm d t
$$

Evaluating the integral on the right-hand side is difficult. However, we can apply FTC II and get

$$
F^{′}(x) = \sin (x^{2})
$$

And that's it! This theorem saves us a ton of work and is especially useful when the integral is hard to calculate.

**Note:** To gain further intuition for FTC II, it helps to work out an example in a simple case. Let's define the accumulation function $F(x)$ as an integral that we can actually compute:

$$
F(x)=\int^{x}_{2} t^2 \,\textrm d t
$$

Computing the integral, we have

$$
\begin{aligned}
F(x) &= \frac{t^{3}}{3} \mid _{2}^{x} = \frac{x^{3}}{3} - \frac{8}{3}
\end{aligned}
$$

and taking the derivative, we get

$$
\begin{aligned}
F^{′}(x) &= \frac{d}{dx}(\frac{x^{3}}{3} - \frac{8}{3}) = x^{2}
\end{aligned}
$$

which matches up with the original integrand. Taking the integral turned $t^2$ into

$$
\dfrac{x^3}{3}
$$

minus a constant, and taking the derivative "reversed" the process to give us just $x^2$.

---

<a id="applying-the-second-fundamental-theorem-of-calculus"></a>
## Applying the Second Fundamental Theorem of Calculus

**Example:** Calculate $\displaystyle\dfrac {\textrm d} {\textrm dx} \int_2^x \dfrac {t^3} {t-1}\,\textrm d t$ for $x>2$.

**Explanation**

The function

$$
\dfrac {t^3} {t-1}
$$

is continuous on $[2,x]$, where $x>2$. So FTC II applies, and we get

$$
\frac{d}{dx}∫_{2}^{x}\frac{t^{3}}{t - 1}dt = \frac{x^{3}}{x - 1}
$$

---

**Question 1:**

```quiz
type: radio
id: q-1
content: |-
  Calculate $\frac{d}{dx}∫_{3}^{x}\frac{\cos t}{t^{2} + 4}dt$ for $x > 3$.
options:
- id: a
  content: |-
    $\frac{\cos x}{x^{2} + 4} - \frac{\cos 3}{13}$
- id: b
  content: |-
    $\frac{\sin x}{x^{2}} - \frac{\sin 3}{13}$
- id: c
  content: |-
    $\frac{\cos x}{x^{2} + 4}$
  correct: true
- id: d
  content: |-
    $-\frac{\cos x}{x^{2}} + \frac{\cos 3}{13}$
- id: e
  content: |-
    $\frac{x\cos x}{x^{2} + 4}$
```

---

**Question 2:**

```quiz
type: radio
id: q-2
content: |-
  Calculate
  
  $\frac{d}{dx}∫_{2}^{x}(4t^{3} + 7t)dt$
  for $x > 2$.
options:
- id: a
  content: |-
    $24$
- id: b
  content: |-
    $x^{2} + x$
- id: c
  content: |-
    $4x^{2} + 7x^{3}$
- id: d
  content: |-
    $4x^{3} + 21$
- id: e
  content: |-
    $4x^{3} + 7x$
  correct: true
```

---

<a id="applying-the-second-fundamental-theorem-of-calculus-by-interchanging-the-limits-of-integration"></a>
## Applying the Second Fundamental Theorem of Calculus by Interchanging the Limits of Integration

**Example:** Calculate $\displaystyle\dfrac {\textrm d} {\textrm dx} \int_x^0 \dfrac{t^3}{t^2 +1}\,\textrm d t$.

**Explanation**

In this example, the variable limit $x$ is located on the lower limit. To apply FTC II, we need the variable to be on the upper limit. Using the properties of definite integrals, we can write

$$
\displaystyle \int_x^0 \dfrac{t^3}{t^2 +1} \,\textrm d t =-\int_0^x \dfrac{t^3}{t^2 +1}\,\textrm d t
$$

Therefore, by FTC II, we have

$$
\begin{aligned} \displaystyle\dfrac {\textrm d} {\textrm dx} \int_x^0 \dfrac{t^3}{t^2 +1} \,\textrm d t & \, \, = \, \, \dfrac {\textrm d} {\textrm dx} \left(-\int_0^x \dfrac{t^3}{t^2 +1} \,\textrm d t \right) \\ & \, \, = \, \, -\dfrac {\textrm d} {\textrm dx} \left(\int_0^x \dfrac{t^3}{t^2 +1} \,\textrm d t \right) \\ &= \, \, -\dfrac{x^3}{x^2 +1}. \end{aligned}
$$

---

**Question 3:**

```quiz
type: radio
id: q-3
content: |-
  Calculate
  
  $\frac{d}{dx}∫_{x}^{0}\sqrt{\cos t + 2}dt$
  for $x < 0$.
options:
- id: a
  content: |-
    $\sqrt{\cos x}$
- id: b
  content: |-
    $\frac{1}{2}\sin x$
- id: c
  content: |-
    $-\sqrt{\cos x + 2}$
  correct: true
- id: d
  content: |-
    $3\sqrt{\cos x - 2}$
- id: e
  content: |-
    $2\sqrt{\sin x + 2}$
```

---

**Question 4:**

```quiz
type: radio
id: q-4
content: |-
  Calculate
  
  $\frac{d}{dx}∫_{x}^{1}e^{t^{2}}dt$
  for $x < 1$.
options:
- id: a
  content: |-
    $6e^{2x}$
- id: b
  content: |-
    $e^{x^{2}}$
- id: c
  content: |-
    $e^{3x}$
- id: d
  content: |-
    $-e^{x^{2}}$
  correct: true
- id: e
  content: |-
    $-6e^{x^{2}}$
```

---

<a id="applying-the-second-fundamental-theorem-of-calculus-using-the-chain-rule"></a>
## Applying the Second Fundamental Theorem of Calculus Using the Chain Rule

**Example:** Find $f'(x)$ for $f(x) = \displaystyle \int_2^{x^2}\arctan t\,\textrm d t$.

**Explanation**

To compute $f'(x)$, we first make the substitution $u=x^2$ and then we apply the chain rule, as follows:

$$
\begin{aligned}
f^{′}(x) &= \frac{d}{dx}∫_{2}^{x^{2}}\arctan tdt \\
&= \frac{du}{dx} \cdot \frac{d}{du}∫_{2}^{u}\arctan tdt
\end{aligned}
$$

The integrand is continuous for all $t$, so by FTC II we get

$$
\begin{aligned}
f^{′}(x) &= \frac{du}{dx} \cdot \arctan (u) \\
&= \frac{d}{dx}(x^{2}) \cdot \arctan (u) \\
&= 2x\arctan (x^{2})
\end{aligned}
$$

---

**Question 5:**

```quiz
type: radio
id: q-5
content: |-
  For $x > e^{6}$, find $f^{′}(x)$ if $f(x) = ∫_{6}^{\ln x}\frac{t}{t - 1}dt$.
options:
- id: a
  content: |-
    $\frac{1 - \ln x}{x\ln x}$
- id: b
  content: |-
    $\frac{\ln x}{\ln x - 1}$
- id: c
  content: |-
    $(1)/(x(\ln x - 1))$
- id: d
  content: |-
    $(\ln x)/(x(\ln x - 1))$
  correct: true
- id: e
  content: |-
    $\frac{x - \ln x}{1 - \ln x}$
```

---

**Question 6:**

```quiz
type: radio
id: q-6
content: |-
  For $x > 2$, find $f^{′}(x)$ if $f(x) = ∫_{2}^{\sqrt{x}}\frac{1}{2 - t^{2}}dt$.
options:
- id: a
  content: |-
    $\frac{\sqrt{x}}{2 - \sqrt{x}}$
- id: b
  content: |-
    $\frac{1}{2 - x}$
- id: c
  content: |-
    $(1)/(2\sqrt{x}(2 - x))$
  correct: true
- id: d
  content: |-
    $\frac{1}{2 - \sqrt{x}}$
- id: e
  content: |-
    $(1)/(2\sqrt{x}(2 - \sqrt{x}))$
```

---

<a id="applying-the-second-fundamental-theorem-of-calculus-with-two-variable-limits"></a>
## Applying the Second Fundamental Theorem of Calculus With Two Variable Limits

**Example:** Find $f'(1)$ if $\displaystyle f(x) = \int_x^{x^2} (t^2 + 2t) \,\, \textrm d t$.

**Explanation**

Here, both the lower and upper limits contain a variable. However, to apply FTC II, we need the variable to be on the upper limit only. So, we can split the integral into two integrals, and rewrite them so that in both cases the variable is on the upper limit. We get

$$
\begin{aligned}
∫_{x}^{x^{2}}(t^{2} + 2t)dt &= ∫_{x}^{a}(t^{2} + 2t)dt + ∫_{a}^{x^{2}}(t^{2} + 2t)dt \\
&= - ∫_{a}^{x}(t^{2} + 2t)dt + ∫_{a}^{x^{2}}(t^{2} + 2t)dt
\end{aligned}
$$

where $a$ is any constant number between $x$ and $x^2$.

The integrand $t^2 + 2t$ is continuous for all $t$, so applying FTC II gives

$$
\begin{aligned}
f^{′}(x) &= \frac{d}{dx}(- ∫_{a}^{x}(t^{2} + 2t)dt + ∫_{a}^{x^{2}}(t^{2} + 2t)dt) \\
&=-\frac{d}{dx}(∫_{a}^{x}(t^{2} + 2t)dt) + \frac{d}{dx}(∫_{a}^{x^{2}}(t^{2} + 2t)dt) \\
&= - (x^{2} + 2x) + \frac{du}{dx}\frac{d}{du}(∫_{a}^{u}(t^{2} + 2t)dt) \\
&=-x^{2} - 2x + 2x(u^{2} + 2u) \\
&=-x^{2} - 2x + 2x((x^{2})^{2} + 2x^{2}) \\
&=-x^{2} - 2x + 2x(x^{4} + 2x^{2}) \\
&=-x^{2} - 2x + 2x^{5} + 4x^{3} \\
&= 2x^{5} + 4x^{3} - x^{2} - 2x
\end{aligned}
$$

Note that we used the substitution $u=x^2$, as before.

Finally, we can compute $f'(1)$. We get

$$
\begin{aligned}
f^{′}(1) &= 2(1)^{5} + 4(1)^{3} - (1)^{2} - 2(1) \\
&= 2 + 4 - 1 - 2 \\
&= 3
\end{aligned}
$$

---

**Question 7:**

```quiz
type: radio
id: q-7
content: |-
  Find $F^{′}(0)$ if $F(x) = ∫_{x}^{\sin (x)}\sqrt[3]{1 + t^{2}}dt$.
options:
- id: a
  content: |-
    $\sqrt[3]{2}$
- id: b
  content: |-
    $\sqrt[3]{2} - 1$
- id: c
  content: |-
    $-\frac{1}{2}$
- id: d
  content: |-
    $1$
- id: e
  content: |-
    $0$
  correct: true
```

---

**Question 8:**

```quiz
type: radio
id: q-8
content: |-
  Find $f^{′}(1)$ if $f(x) = ∫_{x}^{3x}e^{t^{2}}dt$.
options:
- id: a
  content: |-
    $2e^{3}$
- id: b
  content: |-
    $4e^{9}$
- id: c
  content: |-
    $e(3e^{5} + 2)$
- id: d
  content: |-
    $e^{2}(2e^{7} + 1)$
- id: e
  content: |-
    $e(3e^{8} - 1)$
  correct: true
```

```update-progress
```

[[252/Home|Home]]
[[252/0. Table of Contents/TOC|Table of Contents]]
