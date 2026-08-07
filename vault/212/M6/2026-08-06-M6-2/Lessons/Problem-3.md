# Counting Visible Diffraction-Grating Maxima on a Finite Screen

## Table of Contents

- [Introduction](#introduction)
- [Turn the Screen Width into an Edge Angle](#turn-the-screen-width-into-an-edge-angle)
- [Turn the Angle Limit into an Integer Order](#turn-the-angle-limit-into-an-integer-order)
- [Count the Symmetric Orders](#count-the-symmetric-orders)
- [Use the Tighter of the Two Limits](#use-the-tighter-of-the-two-limits)
- [Apply the Complete Visibility Test](#apply-the-complete-visibility-test)
- [Summary](#summary)

## Prerequisites

- Converting micrometers and nanometers to a common unit
- Using tangent in a right triangle and evaluating inverse tangent
- Using the diffraction-grating condition $d\sin\theta_m=m\lambda$
- Identifying the greatest integer that does not exceed a positive bound

---

<a id="introduction"></a>
## Introduction

When a problem asks how many bright diffraction-grating fringes appear on a **finite, centered screen**, two conditions must hold for an order $m$:

1. the grating equation must allow a real angle, and
2. that angle must point to the screen rather than beyond its edge.

For a grating spacing $d$ and wavelength $\lambda$, principal maxima obey

$$
d\sin\theta_m=m\lambda.
$$

Because a real angle has $|\sin\theta_m|\leq1$, the physically possible orders satisfy

$$
|m|\leq\frac{d}{\lambda}.
$$

If the screen has full width $W$ and is a perpendicular distance $L$ from the grating, its one-sided half-width is

$$
Y=\frac{W}{2},
$$

and the ray to an edge makes the angle

$$
\theta_{\text{edge}}=\tan^{-1}\left(\frac{Y}{L}\right).
$$

Only rays with $|\theta_m|\leq\theta_{\text{edge}}$ reach the screen. Since sine increases from $0^\circ$ to $90^\circ$, this becomes the symmetric order bound

$$
|m|\leq\frac{d\sin\theta_{\text{edge}}}{\lambda}.
$$

The largest visible order is therefore

$$
m_{\max}
=
\left\lfloor
\min\left(
\frac{d}{\lambda},
\frac{d\sin\theta_{\text{edge}}}{\lambda}
\right)
\right\rfloor.
$$

Here $\lfloor x\rfloor$ means the greatest integer less than or equal to $x$. Once $m_{\max}$ is known, symmetry gives

$$
N=2m_{\max}+1,
$$

where the extra $1$ is the central maximum, $m=0$.

---

<a id="turn-the-screen-width-into-an-edge-angle"></a>
## Turn the Screen Width into an Edge Angle

**Example:** A centered screen is $1.50\ \mathrm{m}$ wide and $2.00\ \mathrm{m}$ from a grating. Find the largest angle that still lands on the screen.

**Explanation**

The right triangle reaches from the center of the screen to one edge, so its opposite side is the **half-width**:

$$
Y=\frac{1.50\ \mathrm{m}}{2}=0.750\ \mathrm{m}.
$$

The adjacent side is the grating-to-screen distance. Thus

$$
\theta_{\text{edge}}
=\tan^{-1}\left(\frac{0.750}{2.00}\right)
=20.556\ldots^\circ.
$$

The same right triangle has hypotenuse $\sqrt{Y^2+L^2}$, so a useful no-rounding form for the next step is

$$
\sin\theta_{\text{edge}}
=\frac{Y}{\sqrt{Y^2+L^2}}.
$$

Keep guard digits if you calculate the angle; rounding too early can change which integer order fits near an edge.

```quiz
type: radio
id: m6-2-p3-screen-angle
content: |-
  A centered screen is $1.60\ \mathrm{m}$ wide and $1.20\ \mathrm{m}$ from a grating. What is its one-sided edge angle, to the nearest tenth of a degree?
options:
- id: m6-2-p3-screen-angle-a
  content: |-
    $33.7^\circ$
  correct: true
  feedback: |-
    A centered screen extends half its full width to either side, so $Y=1.60/2=0.800\ \mathrm{m}$. Therefore $\theta_{\text{edge}}=\tan^{-1}(0.800/1.20)=33.7^\circ$.
- id: m6-2-p3-screen-angle-b
  content: |-
    $53.1^\circ$
  feedback: |-
    This uses the full $1.60\ \mathrm{m}$ width as the opposite side. The edge is only $0.800\ \mathrm{m}$ from the center, so the correct ratio is $0.800/1.20$ and the edge angle is $33.7^\circ$.
- id: m6-2-p3-screen-angle-c
  content: |-
    $56.3^\circ$
  feedback: |-
    This reverses the tangent ratio. Relative to the grating angle, the screen half-width is opposite and the grating-to-screen distance is adjacent, so use $\tan\theta=0.800/1.20$, not $1.20/0.800$.
- id: m6-2-p3-screen-angle-d
  content: |-
    $16.8^\circ$
  feedback: |-
    Halving the computed angle has no geometric basis. Halve the screen width before forming the tangent ratio; $\tan^{-1}[(1.60/2)/1.20]=33.7^\circ$.
- id: m6-2-p3-screen-angle-e
  content: |-
    $0.667^\circ$
  feedback: |-
    The value $0.800/1.20=0.667$ is the tangent of the angle, not the angle in degrees. Applying inverse tangent gives $\theta_{\text{edge}}=33.7^\circ$.
```

---

<a id="turn-the-angle-limit-into-an-integer-order"></a>
## Turn the Angle Limit into an Integer Order

**Example:** A grating has $d=2.20\ \mu\mathrm{m}$ and is illuminated by $\lambda=550\ \mathrm{nm}$ light. A screen subtends a one-sided angle of $36.9^\circ$. Find the largest visible order.

**Explanation**

First use one unit for $d$ and $\lambda$:

$$
d=2200\ \mathrm{nm}.
$$

The grating equation gives the order that would land exactly at the screen edge:

$$
m_{\text{screen}}
=\frac{d\sin\theta_{\text{edge}}}{\lambda}
=\frac{(2200)\sin(36.9^\circ)}{550}
\approx2.40.
$$

Equivalently, the visible interval is $-2.40\lesssim m\lesssim2.40$. Orders are integers, so the actual interval is $-2\leq m\leq2$ and $m_{\max}=2$. Do not round $2.40$ to the nearest integer; rounding upward would count an order whose angle lies beyond the edge.

```quiz
type: radio
id: m6-2-p3-order-cap
content: |-
  A grating has $d=1.50\ \mu\mathrm{m}$ and $\lambda=500\ \mathrm{nm}$. The screen's one-sided edge angle is $30.0^\circ$. What is the largest visible order?
options:
- id: m6-2-p3-order-cap-a
  content: |-
    $1$
  correct: true
  feedback: |-
    The screen sets $m\le d\sin\theta_{\text{edge}}/\lambda=(1500/500)\sin30.0^\circ=1.50$. Since $m$ must be an integer that does not exceed the bound, the largest visible order is $m_{\max}=1$.
- id: m6-2-p3-order-cap-b
  content: |-
    $2$
  feedback: |-
    Rounding $1.50$ up would include an order beyond the screen. In fact, $m=2$ requires $\sin\theta=2\lambda/d=2/3$, or $\theta\approx41.8^\circ$, which exceeds the $30.0^\circ$ edge angle.
- id: m6-2-p3-order-cap-c
  content: |-
    $3$
  feedback: |-
    The value $d/\lambda=3$ is the physical existence limit, reached only at $\theta=90^\circ$. The finite screen ends at $30.0^\circ$, so its tighter bound is $1.50$ and only orders through $m=1$ are visible.
- id: m6-2-p3-order-cap-d
  content: |-
    $4$
  feedback: |-
    An order cannot exceed even the physical bound $d/\lambda=3$, and the screen is tighter still. Applying the screen angle gives $m\le1.50$, so $m_{\max}=1$.
- id: m6-2-p3-order-cap-e
  content: |-
    $0$
  feedback: |-
    The upper bound itself need not be an integer. A bound of $1.50$ permits the integer orders $m=0$ and $m=1$, so the largest visible nonnegative order is $1$.
```

---

<a id="count-the-symmetric-orders"></a>
## Count the Symmetric Orders

**Example:** Suppose the largest visible order is $m_{\max}=3$. How many bright fringes appear?

**Explanation**

Each nonzero order has one maximum on each side of the center:

$$
m=-3,-2,-1,0,1,2,3.
$$

There are three negative orders, three positive orders, and one central order. Therefore

$$
N
=\underbrace{m_{\max}}_{\text{negative}}
+\underbrace{1}_{m=0}
+\underbrace{m_{\max}}_{\text{positive}}
=2m_{\max}+1
=7.
$$

```quiz
type: radio
id: m6-2-p3-symmetry-count
content: |-
  The largest order that lands on a centered screen is $m_{\max}=4$. How many bright fringes are visible?
options:
- id: m6-2-p3-symmetry-count-a
  content: |-
    $9$
  correct: true
  feedback: |-
    Nonzero grating orders occur in symmetric pairs, $\pm1$ through $\pm4$, and $m=0$ contributes one central maximum. Thus $N=2(4)+1=9$.
- id: m6-2-p3-symmetry-count-b
  content: |-
    $8$
  feedback: |-
    The value $2(4)=8$ counts the four left-right pairs but omits the central maximum. Including $m=0$ gives $8+1=9$ visible fringes.
- id: m6-2-p3-symmetry-count-c
  content: |-
    $5$
  feedback: |-
    The orders $m=0,1,2,3,4$ account for only the center and one side. A centered screen also shows $m=-1,-2,-3,-4$, bringing the total to $9$.
- id: m6-2-p3-symmetry-count-d
  content: |-
    $4$
  feedback: |-
    The number $4$ is the largest positive order, not the number of fringes. Each positive order has a negative partner, and the center adds one, so the total is $2(4)+1=9$.
- id: m6-2-p3-symmetry-count-e
  content: |-
    $10$
  feedback: |-
    Counting five orders on each side treats the central order as a pair. The $m=0$ maximum occurs only once, so the correct count is $4+4+1=9$.
```

---

<a id="use-the-tighter-of-the-two-limits"></a>
## Use the Tighter of the Two Limits

**Example:** A grating with $d=2.40\ \mu\mathrm{m}$ uses $\lambda=600\ \mathrm{nm}$ light. A $1.20\ \mathrm{m}$-wide screen is $1.60\ \mathrm{m}$ away. How many bright fringes are visible?

**Explanation**

The physical existence bound is

$$
m_{\text{physical}}=\frac{d}{\lambda}=4.00.
$$

The half-width is $Y=0.600\ \mathrm{m}$, so

$$
\theta_{\text{edge}}
=\tan^{-1}\left(\frac{0.600}{1.60}\right)
=20.556\ldots^\circ.
$$

The screen bound is

$$
m_{\text{screen}}
=\frac{d\sin\theta_{\text{edge}}}{\lambda}
=(4.00)\sin(20.556\ldots^\circ)
=1.404\ldots.
$$

The tighter limit is the screen, so $m_{\max}=1$ and

$$
N=2(1)+1=3.
$$

The orders $m=2,3,4$ can exist as beams, but they do not land on this screen.

```quiz
type: radio
id: m6-2-p3-competing-limits
content: |-
  A grating has $d=3.00\ \mu\mathrm{m}$ and $\lambda=600\ \mathrm{nm}$. A centered screen is $2.40\ \mathrm{m}$ wide and $0.900\ \mathrm{m}$ away. How many bright fringes land on the screen?
options:
- id: m6-2-p3-competing-limits-a
  content: |-
    $9$
  correct: true
  feedback: |-
    The half-width is $1.20\ \mathrm{m}$, so the edge triangle has $\sin\theta_{\text{edge}}=1.20/1.50=0.800$. Hence $m_{\text{screen}}=(d/\lambda)\sin\theta_{\text{edge}}=5(0.800)=4$, giving $m=-4$ through $4$ and $N=9$.
- id: m6-2-p3-competing-limits-b
  content: |-
    $11$
  feedback: |-
    The physical limit $d/\lambda=5$ allows an $m=5$ beam only at $90^\circ$, parallel to the screen plane. The finite screen reaches only $\sin\theta_{\text{edge}}=0.800$, so $m_{\max}=4$ and only $9$ maxima land on it.
- id: m6-2-p3-competing-limits-c
  content: |-
    $8$
  feedback: |-
    The screen admits the four nonzero order pairs $\pm1$ through $\pm4$, but $8$ omits the central maximum. Adding the single $m=0$ fringe gives $9$.
- id: m6-2-p3-competing-limits-d
  content: |-
    $5$
  feedback: |-
    The five nonnegative orders $m=0,1,2,3,4$ cover only the center and one side. The four negative-order partners also land on the centered screen, so the total is $5+4=9$.
- id: m6-2-p3-competing-limits-e
  content: |-
    $4$
  feedback: |-
    The value $4$ is the largest visible order, not the fringe count. Converting the order limit to a count requires both symmetric sides and the center: $N=2(4)+1=9$.
```

---

<a id="apply-the-complete-visibility-test"></a>
## Apply the Complete Visibility Test

**Example:** A grating has $d=1.8\ \mu\mathrm{m}$ and is illuminated by $\lambda=633\ \mathrm{nm}$ light. A centered screen $2.4\ \mathrm{m}$ wide is $0.85\ \mathrm{m}$ away. Find the number of bright fringes on the screen.

**Explanation**

Use nanometers for both microscopic lengths: $d=1800\ \mathrm{nm}$. The screen half-width and edge angle are

$$
Y=\frac{2.4}{2}=1.2\ \mathrm{m},
\qquad
\theta_{\text{edge}}
=\tan^{-1}\left(\frac{1.2}{0.85}\right)
=54.688\ldots^\circ.
$$

Now compare the two order bounds:

$$
\begin{aligned}
m_{\text{physical}}
&=\frac{1800}{633}=2.843\ldots,\\
m_{\text{screen}}
&=\frac{1800\sin(54.688\ldots^\circ)}{633}
=2.320\ldots.
\end{aligned}
$$

The screen bound is tighter. Taking the greatest integer at or below it gives $m_{\max}=2$, so the visible orders are

$$
m=-2,-1,0,1,2,
$$

and the screen shows

$$
\boxed{N=2(2)+1=5\text{ bright fringes}}.
$$

As a direct check, the second-order maximum is at

$$
y_2
=L\tan\left[\sin^{-1}\left(\frac{2\lambda}{d}\right)\right]
=0.841\ \mathrm{m},
$$

which is inside the $1.2\ \mathrm{m}$ half-width. A third order cannot exist because $3\lambda/d=1.055\ldots>1$.

```quiz
type: radio
id: m6-2-p3-complete-check
content: |-
  A grating has $d=3.00\ \mu\mathrm{m}$ and $\lambda=600\ \mathrm{nm}$. A centered screen $1.50\ \mathrm{m}$ wide is $1.00\ \mathrm{m}$ away. How many bright fringes are visible?
options:
- id: m6-2-p3-complete-check-a
  content: |-
    $7$
  correct: true
  feedback: |-
    The half-width is $0.750\ \mathrm{m}$, so $\sin\theta_{\text{edge}}=0.750/1.25=0.600$. Thus $m_{\text{screen}}=(d/\lambda)(0.600)=5(0.600)=3$, and the orders $-3$ through $3$ give $N=2(3)+1=7$.
- id: m6-2-p3-complete-check-b
  content: |-
    $11$
  feedback: |-
    The physical bound $d/\lambda=5$ ignores the finite screen. Its edge admits only $m\le5\sin\theta_{\text{edge}}=3$, so the visible count is $2(3)+1=7$, not the count of every physically possible order.
- id: m6-2-p3-complete-check-c
  content: |-
    $6$
  feedback: |-
    The six nonzero maxima $m=\pm1,\pm2,\pm3$ are visible, but the central maximum is also present. Including $m=0$ gives $6+1=7$.
- id: m6-2-p3-complete-check-d
  content: |-
    $4$
  feedback: |-
    The four nonnegative orders $m=0,1,2,3$ represent only the center and one side. A centered screen also receives $m=-1,-2,-3$, giving $7$ fringes in all.
- id: m6-2-p3-complete-check-e
  content: |-
    $3$
  feedback: |-
    The number $3$ is the largest visible order. It must be converted to a total by counting both signs and the central order: $N=2(3)+1=7$.
```

---

<a id="summary"></a>
## Summary

For a finite screen centered on the grating axis:

1. Use the half-width, $Y=W/2$.
2. Find the edge angle, $\theta_{\text{edge}}=\tan^{-1}(Y/L)$.
3. Compare the physical and screen bounds:

   $$
   \frac{d}{\lambda}
   \qquad\text{and}\qquad
   \frac{d\sin\theta_{\text{edge}}}{\lambda}.
   $$

4. Take the smaller bound, then round **down** to the greatest allowed integer order.
5. Read $|m|\leq m_{\max}$ as the symmetric integer list $-m_{\max},\ldots,0,\ldots,m_{\max}$.
6. Count negative orders, the center, and positive orders with $N=m_{\max}+1+m_{\max}=2m_{\max}+1$.

The main traps are using the full screen width instead of its half-width, counting every physically possible order without checking the screen, rounding an order bound upward, and forgetting the central maximum.
