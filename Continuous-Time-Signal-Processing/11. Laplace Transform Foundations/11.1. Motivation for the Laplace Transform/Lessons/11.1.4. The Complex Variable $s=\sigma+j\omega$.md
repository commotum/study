# The Complex Variable $s=\sigma+j\omega$

<!--
lesson-id: EE01-M11-01-L04
-->

## Table of Contents

- [Introduction to The Complex Variable $s=\sigma+j\omega$](#introduction-to-the-complex-variable-ssigmajomega)
- [Identifying $\sigma$ and $\omega$ in $s=\sigma+j\omega$](#identifying-sigma-and-omega-in-ssigmajomega)
- [Combining $e^{-\sigma t}$ and $e^{-j\omega t}$ into $e^{-st}$](#combining-e-sigma-t-and-e-jomega-t-into-e-st)
- [Rewriting an Exponentially Weighted Fourier Integral in Terms of $s$](#rewriting-an-exponentially-weighted-fourier-integral-in-terms-of-s)
- [Interpreting the Weighting and Frequency Roles of a Given $s$](#interpreting-the-weighting-and-frequency-roles-of-a-given-s)

---

<a id="introduction-to-the-complex-variable-ssigmajomega"></a>
## Introduction to The Complex Variable $s=\sigma+j\omega$

When you try to use a Fourier kernel and the integral $\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt$ fails to converge, the previous lesson shows that adding an exponential weight is the remedy. You now package that idea so students can reuse it later in Laplace notation.

The direct action is to replace separate factors with a single combined representation. Start from $e^{-\sigma t}$ and $e^{-j\omega t}$ and write them using one compact symbol $s$.

Define the complex variable as $s=\sigma+j\omega$. In this definition, $\sigma$ is the real part that controls exponential weighting, and $\omega$ is the angular-frequency part that controls oscillation.

$$
s=\sigma+j\omega
$$

Apply the rule to combine the product of factors into one exponential: $e^{-\sigma t}e^{-j\omega t}=e^{-st}$. This keeps later derivations short and consistent.

$$
e^{-\sigma t}e^{-j\omega t}=e^{-(\sigma+j\omega)t}=e^{-st}
$$

$$
s\big|_{\sigma=0}=j\omega
$$

---

<a id="identifying-sigma-and-omega-in-ssigmajomega"></a>
## Identifying $\sigma$ and $\omega$ in $s=\sigma+j\omega$

**Example:** Write $s=-2+j\,7$ as "$\sigma$ is ... and $\omega$ is ..."

**Explanation**

Use the target representation from this lesson, $s=\sigma+j\omega$, as the cue. You should match each part of the given number to that template without rearranging terms.

The rule is: the part not multiplied by $j$ is the real part, so it is $\sigma$; the coefficient of $j$ is the imaginary part, so it is $\omega$. This is the same extraction you will reuse in every later section.

$$
s=-2+j\,7=(-2)+j(7) \Rightarrow \sigma=-2,\;\omega=7
$$

Therefore, the answer is "$\sigma$ is $-2$ and $\omega$ is $7$". A negative $\sigma$ means the real part is negative in $s=\sigma+j\omega$, so the associated exponential factor in $e^{-st}$ is growing in time if used directly.

$$
s=\sigma+j\,\omega \text{ with } \omega=0 \Rightarrow s=\sigma
$$

So for the edge case $\omega=0$, the same rule gives zero oscillation and $s$ is purely real; that is the special $j\omega$-axis condition you will use in the next practice model.

**Question 1:**

```quiz
type: radio
id: EE01-M11-01-L04-q001
content: |-
  Given $s=-3+j5$, identify $\sigma$ and $\omega$ in $s=\sigma+j\omega$.

options:
- id: a
  content: |-
    $\sigma=-3,\;\omega=5$
  correct: true
  feedback: |-
    Match the given value to $s=\sigma+j\omega$. The part not multiplied by $j$ is $\sigma$, and the coefficient of $j$ is $\omega$.

    $$
    s=-3+j5=(-3)+j(5) \Rightarrow \sigma=-3,\;\omega=5
    $$

- id: b
  content: |-
    $\sigma=5,\;\omega=-3$

- id: c
  content: |-
    $\sigma=3,\;\omega=5$

- id: d
  content: |-
    $\sigma=-3,\;\omega=0$

- id: e
  content: |-
    $\sigma=5,\;\omega=3$
```

---

**Question 2:**

```quiz
type: radio
id: EE01-M11-01-L04-q002
content: |-
  Given $s=4-j6$, identify $\sigma$ and $\omega$ in $s=\sigma+j\omega$.

options:
- id: a
  content: |-
    $\sigma=4,\;\omega=-6$
  correct: true
  feedback: |-
    Rewrite the imaginary part so the value has the form $\sigma+j\omega$. Since $-j6=j(-6)$, the coefficient of $j$ is negative.

    $$
    s=4-j6=4+j(-6) \Rightarrow \sigma=4,\;\omega=-6
    $$

- id: b
  content: |-
    $\sigma=-6,\;\omega=4$

- id: c
  content: |-
    $\sigma=4,\;\omega=6$

- id: d
  content: |-
    $\sigma=-4,\;\omega=-6$

- id: e
  content: |-
    $\sigma=4,\;\omega=0$
```

---

<a id="combining-e-sigma-t-and-e-jomega-t-into-e-st"></a>
## Combining $e^{-\sigma t}$ and $e^{-j\omega t}$ into $e^{-st}$

**Example:** Show that $e^{-2t}\,e^{-j4t}=e^{-st}$ and find $s$.

**Explanation**

Keep the same recognition target from the previous steps: the final form is $e^{-st}$. Here, the cue is already set by one factor with real exponent and one with imaginary exponent, both in the same variable $t$ and both with a leading minus sign.

Apply the composition rule $e^A e^B=e^{A+B}$ with $A=-2t$ and $B=-j4t$, then merge them into one exponent.

$$
e^{-2t}e^{-j4t}=e^{-2t-j4t}
$$

Now factor $t$ and write the combined exponent in canonical form $-(\sigma+j\omega)t$. Since $-2t-j4t=-(2+j4)t$, we identify $\sigma=2$ and $\omega=4$.

$$
e^{-2t-j4t}=e^{-(2+j4)t}=e^{-st},\; s=2+j4
$$

The result is the same rule in reverse of the previous step: this time you reconstruct the single $s$ from two factors, so the answer is that the expression is in $e^{-st}$ form with $s=2+j4$.

**Question 3:**

```quiz
type: radio
id: EE01-M11-01-L04-q003
content: |-
  Rewrite $e^{-5t}e^{-j2t}$ in $e^{-st}$ form and state $s$.

options:
- id: a
  content: |-
    $e^{-(5+j2)t}=e^{-st}$ with $s=5+j2$
  correct: true
  feedback: |-
    Combine the exponents because the factors have the same variable $t$: $e^A e^B=e^{A+B}$.

    $$
    e^{-5t}e^{-j2t}=e^{-5t-j2t}=e^{-(5+j2)t}
    $$

    Matching $e^{-(5+j2)t}$ to $e^{-st}$ gives $s=5+j2$.

- id: b
  content: |-
    $e^{-5t}e^{-j2t}$, so it is not a single $e^{-st}$ term

- id: c
  content: |-
    $e^{-(5-j2)t}=e^{-st}$ with $s=5-j2$

- id: d
  content: |-
    $e^{-(2+j5)t}=e^{-st}$ with $s=2+j5$

- id: e
  content: |-
    $e^{-(5+j2)}=e^{-s}$ with $s=5+j2$
```

---

**Question 4:**

```quiz
type: radio
id: EE01-M11-01-L04-q004
content: |-
  Rewrite $e^{3t}e^{-j6t}$ in $e^{-st}$ form and state $s$.

options:
- id: a
  content: |-
    $e^{-(-3+j6)t}=e^{-st}$ with $s=-3+j6$
  correct: true
  feedback: |-
    First merge the exponents, then rewrite the result with a leading minus sign so it matches $e^{-st}$.

    $$
    e^{3t}e^{-j6t}=e^{(3-j6)t}=e^{-(-3+j6)t}
    $$

    Therefore the combined expression has $s=-3+j6$.

- id: b
  content: |-
    $e^{3t}e^{-j6t}$, so no single $s$ can be stated

- id: c
  content: |-
    $e^{-(3+j6)t}=e^{-st}$ with $s=3+j6$

- id: d
  content: |-
    $e^{-(-3-j6)t}=e^{-st}$ with $s=-3-j6$

- id: e
  content: |-
    $e^{-(6-j3)t}=e^{-st}$ with $s=6-j3$
```

---

<a id="rewriting-an-exponentially-weighted-fourier-integral-in-terms-of-s"></a>
## Rewriting an Exponentially Weighted Fourier Integral in Terms of $s$

**Example:** Let $X(\sigma,\omega)=\int_{-\infty}^{\infty}x(t)e^{-3t}e^{-j\omega t}\,dt$. Rewrite this as $X(s)$.

**Explanation**

This example is the weighted-integral form of the same rule: the cue is a product of two exponentials inside the transform integral, so the target is a single $e^{-st}$ factor.

Copy the integrand and label $e^{-3t}$ as the real damping factor and $e^{-j\omega t}$ as the oscillation factor. The exponent form is now ready for one substitution.

$$
X(\sigma,\omega)=\int_{-\infty}^{\infty}x(t)e^{-3t}e^{-j\omega t}\,dt=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt
$$

Use $e^{-\sigma t}e^{-j\omega t}=e^{-st}$ from the previous steps with $\sigma=3$, so the integral can be rewritten directly in Laplace form.

$$
s=\sigma+j\omega=3+j\omega
$$

Final result: the rewritten expression is $X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt$, with $\sigma=3$ as the real part of $s$ and unchanged angular part from $\omega$.

**Question 5:**

```quiz
type: radio
id: EE01-M11-01-L04-q005
content: |-
  Rewrite $\int_{-\infty}^{\infty}x(t)e^{-2t}e^{-j\omega t}\,dt$ in $s$-notation. Which choice correctly gives both the integral and the corresponding $s$?

options:
- id: a
  content: |-
    $$
    X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt,\quad s=2+j\omega
    $$
  correct: true
  feedback: |-
    Combine the two exponential factors into one exponent. The real weighting factor $e^{-2t}$ gives $\sigma=2$, and the oscillating factor $e^{-j\omega t}$ keeps the imaginary part $j\omega$.

    $$
    e^{-2t}e^{-j\omega t}=e^{-(2+j\omega)t}=e^{-st},\quad s=2+j\omega
    $$

- id: b
  content: |-
    $$
    X(s)=\int_{-\infty}^{\infty}x(t)e^{-2t}e^{-st}\,dt,\quad s=j\omega
    $$

- id: c
  content: |-
    $$
    X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt,\quad s=-2+j\omega
    $$

- id: d
  content: |-
    $$
    X(s)=\int_{0}^{\infty}x(t)e^{-st}\,dt,\quad s=2+j\omega
    $$

- id: e
  content: |-
    $$
    X(s)=\int_{-\infty}^{\infty}x(s)e^{-st}\,ds,\quad s=2+j\omega
    $$
```

---

**Question 6:**

```quiz
type: radio
id: EE01-M11-01-L04-q006
content: |-
  Rewrite $\int_{0}^{\infty}y(t)e^{4t}e^{-j7t}\,dt$ in $s$-notation. Which choice correctly preserves the limits and identifies $s$?

options:
- id: a
  content: |-
    $$
    Y(s)=\int_{0}^{\infty}y(t)e^{-st}\,dt,\quad s=-4+j7
    $$
  correct: true
  feedback: |-
    Match the product to $e^{-\sigma t}e^{-j\omega t}=e^{-st}$. Because $e^{4t}$ has a positive exponent, it corresponds to $\sigma=-4$, not $\sigma=4$.

    $$
    e^{4t}e^{-j7t}=e^{-(-4)t}e^{-j7t}=e^{-(-4+j7)t}=e^{-st}
    $$

- id: b
  content: |-
    $$
    Y(s)=\int_{0}^{\infty}y(t)e^{-st}\,dt,\quad s=4+j7
    $$

- id: c
  content: |-
    $$
    Y(s)=\int_{0}^{\infty}y(t)e^{4t}e^{-st}\,dt,\quad s=j7
    $$

- id: d
  content: |-
    $$
    Y(s)=\int_{0}^{\infty}y(t)e^{-st}\,dt,\quad s=-4-j7
    $$

- id: e
  content: |-
    $$
    Y(s)=\int_{-\infty}^{\infty}y(t)e^{-st}\,dt,\quad s=-4+j7
    $$
```

---

<a id="interpreting-the-weighting-and-frequency-roles-of-a-given-s"></a>
## Interpreting the Weighting and Frequency Roles of a Given $s$

**Example:** Given $s=-1+j4$, explain what the real and imaginary parts imply about the weighting and frequency of $e^{-st}$.

**Explanation**

Use the cue $e^{-st}=e^{-\sigma t}e^{-j\omega t}$, and read the given value as a concrete decomposition target.

Separate $s$ into parts: in $s=-1+j4$, the real part is $\sigma=-1$ and the imaginary coefficient is $\omega=4$.

$$
s=-1+j4 \Rightarrow \sigma=-1,\;\omega=4
$$

Apply the sign rule to $e^{-\sigma t}$. Because $\sigma=-1$, the real part gives $e^{-(-1)t}=e^{t}$, which is growing in time; if $\sigma>0$, that same term would decay.

$$
e^{-st}=e^{-(-1)t}e^{-j4t}=e^{t}e^{-j4t}
$$

Use the imaginary part for oscillation: $\omega=4$ gives sinusoidal frequency $4$ in the factor $e^{-j4t}$, so the full interpretation is growth modulation with angular frequency $4$.

**Question 7:**

```quiz
type: radio
id: EE01-M11-01-L04-q007
content: |-
  For $s=2-j5$, choose the correct interpretation of the real exponential factor and oscillatory frequency component in $e^{-st}$.

options:
- id: a
  content: |-
    The real part gives decay as $e^{-2t}$, and $\omega=-5$ gives the oscillatory factor $e^{j5t}$.
  correct: true
  feedback: |-
    Match the value to $s=\sigma+j\omega$. Here $\sigma=2$ and $\omega=-5$.

    $$
    e^{-st}=e^{-2t}e^{-j(-5)t}=e^{-2t}e^{j5t}
    $$

    A positive $\sigma$ makes the real exponential factor decay, while the imaginary part sets the oscillatory factor.

- id: b
  content: |-
    The real part gives growth as $e^{2t}$, and $\omega=-5$ gives the oscillatory factor $e^{j5t}$.

- id: c
  content: |-
    $\omega=-5$ gives decay as $e^{-5t}$, and $2$ is the oscillatory frequency.

- id: d
  content: |-
    Both $2$ and $-5$ are independent oscillatory frequencies, so there is no exponential decay or growth.

- id: e
  content: |-
    Because $\sigma\ne 0$, there is no oscillation; the expression only decays as $e^{-2t}$.
```

---

**Question 8:**

```quiz
type: radio
id: EE01-M11-01-L04-q008
content: |-
  For $s=-3+j2$, which choice correctly describes the weighting and frequency roles in $e^{-st}$?

options:
- id: a
  content: |-
    $\sigma=-3$ gives growth as $e^{3t}$, and $\omega=2$ gives the oscillatory factor $e^{-j2t}$.
  correct: true
  feedback: |-
    Separate the real and imaginary parts: $\sigma=-3$ and $\omega=2$.

    $$
    e^{-st}=e^{-(-3)t}e^{-j2t}=e^{3t}e^{-j2t}
    $$

    A negative $\sigma$ produces growth in $e^{-\sigma t}$, and $\omega$ sets the sinusoidal frequency factor.

- id: b
  content: |-
    $\sigma=-3$ gives decay as $e^{-3t}$, and $\omega=2$ gives the oscillatory factor $e^{-j2t}$.

- id: c
  content: |-
    $\omega=2$ gives growth as $e^{2t}$, and $\sigma=-3$ is the oscillatory frequency.

- id: d
  content: |-
    Both $-3$ and $2$ are frequencies, so $e^{-st}$ has no real exponential weighting.

- id: e
  content: |-
    Because $\sigma\ne 0$, the imaginary part does not cause oscillation.
```
