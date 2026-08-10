# Auditing Qualitative Optics Claims

## Table of Contents

- [Introduction](#introduction)
- [Classify an Image by the Actual Rays](#classify-an-image-by-the-actual-rays)
- [Measure Snell's-Law Angles from the Normal](#measure-snells-law-angles-from-the-normal)
- [Test a Diverging Lens with Magnification](#test-a-diverging-lens-with-magnification)
- [Audit a Set of Claims One at a Time](#audit-a-set-of-claims-one-at-a-time)
- [Summary](#summary)

## Prerequisites

- Distinguish a light ray from the backward extension of a ray.
- Identify the normal as the line perpendicular to an optical surface.
- Solve a simple reciprocal equation and interpret the sign and magnitude of a ratio.

---

<a id="introduction"></a>
## Introduction

When a problem asks which optics statements are true, audit each statement independently. Do not decide from a familiar keyword alone.

1. Name the quantity or classification in the claim.
2. State the definition, convention, or equation that controls it.
3. Check the claim's conditions and translate the result back into words.

Use this audit card:

| Claim language | Controlling test | Condition to lock first |
| --- | --- | --- |
| real or virtual image | Do actual rays pass through the image location? | Actual rays versus backward extensions |
| angle in Snell's law | What line is the angle measured from? | The conventional sine form uses the normal |
| magnified or reduced image | Is $|m|$ greater than or less than $1$? | Real-object setup and lens sign convention |

A statement is true only if all parts survive the appropriate test under the stated conditions.

---

<a id="classify-an-image-by-the-actual-rays"></a>
## Classify an Image by the Actual Rays

**Example:** A person looks into a plane mirror. The reflected rays reaching the person's eyes diverge, but their backward extensions meet behind the mirror. Is the image real or virtual?

**Explanation**

The deciding question is whether actual light rays pass through the image location.

- A **real image** occurs where actual rays converge.
- A **virtual image** occurs where rays only appear to originate; their backward extensions meet, but no light passes through that apparent location.

For a plane mirror, the actual reflected rays remain in front of the mirror. Only their backward extensions meet behind it, so the image is virtual.

```quiz
type: radio
id: p1-q1-ray-reality
content: |-
  Reflected rays from a plane mirror diverge toward an observer. Their backward extensions intersect behind the mirror, but no actual ray passes through that intersection. How should the image be classified?
options:
- id: p1-q1-a
  content: |-
    Virtual, because only the backward extensions intersect at the apparent image location
  correct: true
  feedback: |-
    Image reality is determined by the actual rays. Here only their backward extensions intersect behind the mirror, so no light passes through the apparent location and the image is virtual.
- id: p1-q1-b
  content: |-
    Real, because the backward extensions intersect behind the mirror
  feedback: |-
    An intersection of backward extensions locates a virtual image, not a real one. A real image would require the actual reflected rays themselves to converge at the image location.
- id: p1-q1-c
  content: |-
    Real, because light from the object reaches the observer
  feedback: |-
    Light reaching the observer makes the image visible, but it does not make the image real. Reality depends on whether actual rays pass through the image location, and these rays do not pass behind the mirror.
- id: p1-q1-d
  content: |-
    Neither, because diverging rays cannot define an image location
  feedback: |-
    Diverging rays can define a virtual image when their backward extensions share an apparent origin. The shared point behind the mirror is therefore a valid virtual-image location.
```

---

<a id="measure-snells-law-angles-from-the-normal"></a>
## Measure Snell's-Law Angles from the Normal

**Example:** An incident ray makes a $35^\circ$ angle with a flat surface. Which incident angle belongs in the conventional form of Snell's law?

**Explanation**

In

$$
n_1\sin\theta_1=n_2\sin\theta_2,
$$

both $\theta_1$ and $\theta_2$ are measured from the **normal**, not from the surface. The surface and its normal are perpendicular, so an angle $\phi$ measured from the surface must be converted:

$$
\theta=90^\circ-\phi.
$$

Thus an angle of $35^\circ$ from the surface is $55^\circ$ from the normal. Surface-referenced angles can describe the same rays, but then the conventional sine equation must be rewritten using complementary angles. One cannot switch reference lines while leaving the formula unchanged.

If $\phi_1$ and $\phi_2$ are measured from the surface, then $\theta_i=90^\circ-\phi_i$, so

$$
n_1\cos\phi_1=n_2\cos\phi_2.
$$

Lock the reference line first; only then substitute an angle into a trigonometric function.

```quiz
type: radio
id: p1-q2-snell-reference
content: |-
  A ray is measured at $20^\circ$ from an interface. What value should be used for that ray's angle in $n_1\sin\theta_1=n_2\sin\theta_2$?
options:
- id: p1-q2-a
  content: |-
    $70^\circ$
  correct: true
  feedback: |-
    The conventional Snell angle is measured from the normal. Because the normal is $90^\circ$ from the interface, the required angle is $90^\circ-20^\circ=70^\circ$.
- id: p1-q2-b
  content: |-
    $20^\circ$
  feedback: |-
    The given $20^\circ$ is referenced to the interface, while the sine form of Snell's law uses angles from the normal. Convert the complementary angle to obtain $70^\circ$.
- id: p1-q2-c
  content: |-
    Either $20^\circ$ or $70^\circ$, because the reference line does not affect the sine
  feedback: |-
    Complementary angles generally have different sines: $\sin20^\circ\ne\sin70^\circ$. Either reference line can describe the geometry only if the equation is changed consistently; the conventional sine form requires $70^\circ$ here.
- id: p1-q2-d
  content: |-
    $90^\circ$
  feedback: |-
    The $90^\circ$ angle is between the surface and its normal, not between the ray and the normal. Subtract the ray's $20^\circ$ surface angle from $90^\circ$ to get $70^\circ$.
```

---

<a id="test-a-diverging-lens-with-magnification"></a>
## Test a Diverging Lens with Magnification

**Example:** A real object is placed $24\ \mathrm{cm}$ from a diverging lens with focal length $f=-12\ \mathrm{cm}$. Describe the image.

**Explanation**

For a thin lens,

$$
\frac{1}{f}=\frac{1}{d_o}+\frac{1}{d_i}.
$$

Substitute $f=-12\ \mathrm{cm}$ and $d_o=24\ \mathrm{cm}$:

$$
\frac{1}{d_i}
=\frac{1}{f}-\frac{1}{d_o}
=-\frac{1}{12}-\frac{1}{24}
=-\frac{1}{8},
$$

so $d_i=-8\ \mathrm{cm}$. The negative image distance means the image is virtual. Its magnification is

$$
m=-\frac{d_i}{d_o}=-\frac{-8}{24}=\frac{1}{3}.
$$

Therefore the image is upright because $m>0$ and reduced because $0<m<1$.

Keep the three classifications separate:

| Quantity | What it controls here |
| --- | --- |
| sign of $d_i$ | real ($d_i>0$) or virtual ($d_i<0$) |
| sign of $m$ | upright ($m>0$) or inverted ($m<0$) |
| magnitude $|m|$ | magnified ($|m|>1$) or reduced ($|m|<1$) |

More generally, write $f=-F$ with $F>0$. For a real object,

$$
|d_i|=\frac{Fd_o}{F+d_o}<d_o,
$$

so $0<m=|d_i|/d_o<1$. In the ordinary real-object setup, a single diverging lens cannot produce a magnified image. That scope matters: the claim is about a real object placed in front of the lens.

```quiz
type: radio
id: p1-q3-diverging-lens
content: |-
  A real object is placed in front of a diverging thin lens. The lens produces $d_i=-6\ \mathrm{cm}$ for $d_o=18\ \mathrm{cm}$. Which description is correct?
options:
- id: p1-q3-a
  content: |-
    Virtual, upright, and reduced, with $m=+\tfrac{1}{3}$
  correct: true
  feedback: |-
    A negative $d_i$ identifies a virtual image, and $m=-d_i/d_o=+6/18=+1/3$. The positive sign means upright and the magnitude below $1$ means reduced.
- id: p1-q3-b
  content: |-
    Virtual, inverted, and reduced, with $m=-\tfrac{1}{3}$
  feedback: |-
    The image is virtual because $d_i<0$, but magnification includes the minus sign: $m=-(-6)/18=+1/3$. Positive magnification means upright, not inverted.
- id: p1-q3-c
  content: |-
    Real, upright, and reduced, with $m=+\tfrac{1}{3}$
  feedback: |-
    The magnification is $+1/3$, so upright and reduced are correct, but $d_i=-6\ \mathrm{cm}$ places the image on the virtual side. A real image would have $d_i>0$ in this convention.
- id: p1-q3-d
  content: |-
    Virtual, upright, and magnified, with $m=+3$
  feedback: |-
    This reverses the magnification ratio. The thin-lens relation gives $m=-d_i/d_o=6/18=1/3$, not $18/6=3$, so the image is reduced rather than magnified.
```

---

<a id="audit-a-set-of-claims-one-at-a-time"></a>
## Audit a Set of Claims One at a Time

**Example:** Apply the same three-step audit to a collection of statements: identify the controlling rule, check every qualifier, and decide each statement without letting one answer influence another.

**Explanation**

Audit the claims with separate cues before combining the results:

| Claim | Cue and test | Result |
| --- | --- | --- |
| plane-mirror image | Only backward extensions meet behind the mirror | virtual |
| conventional Snell angles | The sine form defines angles from the normal | surface and normal references are not interchangeable |
| real object and diverging lens | $f<0$ gives $d_i<0$ and $0<m<1$ | virtual, upright, reduced |

The phrase **select all that apply** means each option receives its own test. There may be more than one true statement.

```quiz
type: radio
id: p1-q4-original-claim-audit
content: |-
  Consider these statements:

  1. When someone views their image in a plane mirror, they are viewing a virtual image because the light rays forming the image do not pass through the image location.
  2. The angles $\theta_1$ and $\theta_2$ in the conventional form of Snell's law, $n_1\sin\theta_1=n_2\sin\theta_2$, can be measured either with respect to the line tangent to the surface or the line normal to the surface.
  3. A diverging lens cannot magnify objects.

  In the standard real-object lens context, which set contains all and only the true statements?
options:
- id: p1-q4-a
  content: |-
    Statement 1 only
  feedback: |-
    Statement 1 is true because only backward ray extensions meet behind a plane mirror. However, statement 3 is also true in the stated real-object context: a diverging lens gives $0<m<1$, so this set omits a true statement.
- id: p1-q4-b
  content: |-
    Statement 2 only
  feedback: |-
    Statement 2 is false because the conventional sine form of Snell's law defines both angles from the normal. Surface angles are complementary and require conversion; meanwhile statements 1 and 3 satisfy their ray and magnification tests.
- id: p1-q4-c
  content: |-
    Statements 1 and 3 only
  correct: true
  feedback: |-
    Statement 1 passes the actual-ray test for a virtual image, and statement 3 passes the real-object diverging-lens test $0<m<1$. Statement 2 fails because the conventional Snell angles are measured only from the normal, so statements 1 and 3 are exactly the true set.
- id: p1-q4-d
  content: |-
    Statements 2 and 3 only
  feedback: |-
    Statement 3 is true for the stated real-object setup, but statement 2 uses the wrong angle convention: the unchanged sine form requires normal-referenced angles. Statement 1 is also true because no actual rays pass through the plane mirror's apparent image location.
- id: p1-q4-e
  content: |-
    Statements 1, 2, and 3
  feedback: |-
    Statements 1 and 3 pass their defining tests, but statement 2 does not. Angles from the surface can describe the geometry only after complementary-angle conversion; they cannot replace normal-referenced angles in the conventional sine equation unchanged.
```

---

<a id="summary"></a>
## Summary

- **Cue:** A qualitative optics problem asks whether several claims are true.
- **Procedure:** Test each claim independently with its controlling definition, convention, or equation, then check the claim's scope.
- **Image reality:** Actual rays through the image location mean real; only backward extensions meeting there mean virtual.
- **Snell angles:** In $n_1\sin\theta_1=n_2\sin\theta_2$, measure both angles from the normal.
- **Diverging lens:** For a real object, $f<0$ gives a virtual, upright, reduced image with $0<m<1$.
- **Main trap:** Do not treat a familiar phrase as sufficient; a changed angle reference or an omitted physical condition can change whether a statement is true.
