# Enforcing the Zero-Normal-Force Contact Threshold

<!--
lesson-id: 212-M1-082
topic-code: MTH212.M1.82
-->

## Table of Contents

- [Introduction](#introduction)
- [Draw Inward Before Writing Forces](#draw-inward-before-writing-forces)
- [Source-Video Problem 1: Outside Hill](#source-video-problem-1-outside-hill)
- [Source-Video Problem 2: Inside Loop](#source-video-problem-2-inside-loop)
- [Choose the Physical Side of the Threshold](#choose-the-physical-side-of-the-threshold)
- [Summary](#summary)

## Prerequisites

- Draw a free-body diagram containing only real forces on the object.
- Point the positive radial direction inward, toward the circle's center.
- Use $a_r=v^2/r$ and write Newton's second law as $\sum F_r=mv^2/r$.
- Treat an ordinary surface contact as one-sided: it may push with $N\geq0$, but it cannot pull an unrestrained object back toward the surface.

---

<a id="introduction"></a>
## Introduction

If a prompt says **just maintains contact**, **just begins to leave the track**, **maximum speed over a crest**, or **minimum speed at the top of a loop**, the normal force has reached its lower physical limit. The same issue appears when a contact calculation gives $N<0$.

Follow this sequence:

1. Mark the circle's center and choose inward as positive.
2. Give each real radial force a sign from the diagram, then write $\sum F_r=mv^2/r$.
3. At the instant contact is just being lost, set $N=0$ and solve for the boundary speed.
4. Enforce $N\geq0$ in the original force equation to decide which side of the boundary preserves contact.

A negative value from a contact equation is not a negative normal force. It says the assumed circular contact would require the surface to pull. Once the object separates, the actual normal force is $N=0$, and the object no longer follows that surface's circular path.

At the top of both geometries, setting $N=0$ gives the same boundary value, $v=\sqrt{rg}$. The force directions decide the inequality:

| Geometry at the top | Inward-positive radial equation | Contact condition |
|---|---|---|
| Outside a convex hill | $mg-N=mv^2/r$ | $v\leq\sqrt{rg}$ |
| Inside a vertical loop | $mg+N=mv^2/r$ | $v\geq\sqrt{rg}$ |

Do not choose the inequality from the formula $\sqrt{rg}$ alone.

---

<a id="draw-inward-before-writing-forces"></a>
## Draw Inward Before Writing Forces

**Example:** Compare an unrestrained object at the top of an outside hill with one at the top of an inside loop.

**Explanation**

The center is below the object in both cases, so inward points downward. What changes is the normal-force direction.

```text
Outside crest                         Inside loop

        ↑ N (outward)                  /¯¯¯¯¯¯¯¯¯\  track
        ● object                            ● object
     __/ \__                               ↓ N (inward)
        ↓ mg (inward)                      ↓ mg (inward)
        ↓ +r                               ↓ +r
        ⊙ center                           ⊙ center
```

For the outside crest, gravity is inward and the normal force is outward:

$$
mg-N=\frac{mv^2}{r}.
$$

For the inside loop, both forces are inward:

$$
mg+N=\frac{mv^2}{r}.
$$

The expression $mv^2/r$ is the required inward **net force**, not an extra force to add to the diagram.

```quiz
type: radio
id: mct-p8-force-directions
content: |-
  An unrestrained cart is at the top of an inside vertical loop. Which inward-positive radial equation matches the free-body diagram?
options:
- id: mct-p8-force-directions-a
  content: |-
    $mg+N=\dfrac{mv^2}{r}$
  correct: true
  feedback: |-
    Inward is downward at the top of the loop. Both gravity and the track's normal force point downward toward the center, so their sum supplies the inward net force: $mg+N=mv^2/r$.
- id: mct-p8-force-directions-b
  content: |-
    $mg-N=\dfrac{mv^2}{r}$
  feedback: |-
    This is the outside-crest equation, where the surface pushes outward while gravity points inward. Inside the loop, the track pushes the cart inward, so $N$ has the same sign as $mg$.
- id: mct-p8-force-directions-c
  content: |-
    $N-mg=\dfrac{mv^2}{r}$
  feedback: |-
    This sign pattern fits the bottom of a dip when inward is upward. At the top of an inside loop, inward is downward and both $N$ and $mg$ point that way.
- id: mct-p8-force-directions-d
  content: |-
    $N=mg$
  feedback: |-
    Equal normal force and weight would give zero radial net force. Circular motion at nonzero speed needs an inward net force $mv^2/r$, so the two forces cannot simply be balanced here.
- id: mct-p8-force-directions-e
  content: |-
    $mg+N+\dfrac{mv^2}{r}=0$
  feedback: |-
    The quantity $mv^2/r$ is the value of the inward net force from Newton's second law, not a third force. The real radial forces are gravity and the normal force.
```

---

<a id="source-video-problem-1-outside-hill"></a>
## Source-Video Problem 1: Outside Hill

**Example:** In the source video's first problem (0:05–8:14), a $5\,\mathrm{kg}$ box moves at $15\,\mathrm{m/s}$ through a dip at A and over an outside crest at B. The radius of curvature is $2\,\mathrm m$ at both points. Find the normal force at A, interpret the contact calculation at B, and find the greatest speed that still permits contact at B.

**Explanation**

The two locations reverse the inward direction relative to the upward normal force:

```text
A: bottom of the dip                  B: outside crest

        ⊙ center                            ↑ N_B (outward)
        ↑ +r                                ● box
        ↑ N_A                            __/ \__
        ● box                               ↓ mg and +r
        ↓ mg                                ⊙ center
     \__A__/
```

At A, inward is upward. The normal force must overcome gravity and still leave an upward radial net force:

$$
\begin{aligned}
N_A-mg&=\frac{mv^2}{r},\\
N_A&=mg+\frac{mv^2}{r}\\
&=(5)(9.8)+\frac{(5)(15^2)}{2}\\
&=49+562.5\\
&=611.5\,\mathrm N.
\end{aligned}
$$

At B, inward is downward. Gravity points inward, but the surface normal points outward:

$$
\begin{aligned}
mg-N_B&=\frac{mv^2}{r},\\
N_B&=mg-\frac{mv^2}{r}\\
&=49-562.5\\
&=-513.5\,\mathrm N \qquad \text{(formal contact result).}
\end{aligned}
$$

The road cannot provide that downward pull. The box has already left the crest, so its actual normal force is $N_B=0$.

At the boundary between contact and separation, set $N_B=0$:

$$
\begin{aligned}
mg&=\frac{mv_{\mathrm{threshold}}^2}{r},\\
v_{\mathrm{threshold}}&=\sqrt{rg}\\
&=\sqrt{(2\,\mathrm m)(9.8\,\mathrm{m/s^2})}\\
&=4.43\,\mathrm{m/s}.
\end{aligned}
$$

For contact, $N_B=mg-mv^2/r$ must be nonnegative. Therefore,

$$
\boxed{v\leq4.43\,\mathrm{m/s}}.
$$

The stated $15\,\mathrm{m/s}$ is above this maximum, which agrees with the negative formal result.

```quiz
type: radio
id: mct-p8-outside-mirror
content: |-
  An unrestrained $3.0\,\mathrm{kg}$ package passes over an outside crest of radius $8.0\,\mathrm m$ at $10.0\,\mathrm{m/s}$. What is the physical conclusion? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p8-outside-mirror-a
  content: |-
    The contact equation gives $N=-8.1\,\mathrm N$; physically $N=0$, and the package loses contact.
  correct: true
  feedback: |-
    At an outside crest, $N=mg-mv^2/r=(3)(9.8)-(3)(10^2)/8=-8.1\,\mathrm N$ formally. A surface cannot pull the package downward, so the negative result means separation; the actual contact force is $N=0$.
- id: mct-p8-outside-mirror-b
  content: |-
    The package stays in contact with a normal force of $-8.1\,\mathrm N$.
  feedback: |-
    The arithmetic is the formal contact result, but its interpretation is not physical for an unrestrained package. A negative $N$ would require the surface to pull, so contact has failed and the actual normal force is zero.
- id: mct-p8-outside-mirror-c
  content: |-
    The package stays in contact with $N=66.9\,\mathrm N$.
  feedback: |-
    Adding $mg$ and $mv^2/r$ uses the bottom-of-a-dip force pattern. At an outside crest, gravity is inward and $N$ is outward, so $N=mg-mv^2/r$, not their sum.
- id: mct-p8-outside-mirror-d
  content: |-
    The threshold is $8.85\,\mathrm{m/s}$, and contact requires $v\geq8.85\,\mathrm{m/s}$.
  feedback: |-
    The boundary value $\sqrt{(8)(9.8)}=8.85\,\mathrm{m/s}$ is correct, but the inequality is reversed. Faster motion demands more inward force while the outward normal force can only decrease, so outside-crest contact requires $v\leq8.85\,\mathrm{m/s}$.
- id: mct-p8-outside-mirror-e
  content: |-
    The package stays in contact with $N=mg=29.4\,\mathrm N$.
  feedback: |-
    Setting $N=mg$ would make the radial net force zero. At nonzero speed the package needs $mv^2/r$ inward, so the normal force must differ from its level-surface value; here the required value becomes unphysical and contact is lost.
```

---

<a id="source-video-problem-2-inside-loop"></a>
## Source-Video Problem 2: Inside Loop

**Example:** In the source video's second problem (8:39–15:31), an unrestrained roller-coaster car is upside down at the top of an inside loop of radius $15\,\mathrm m$. Find the minimum speed that preserves contact.

**Explanation**

The track is outside the car and pushes it toward the center:

```text
              inside track
          /¯¯¯¯¯¯¯¯¯¯¯¯¯\
               ● car
               ↓ N
               ↓ mg
               ↓ +r
               ⊙ center
```

Both real forces are inward, so

$$
mg+N=\frac{mv^2}{r}
$$

and

$$
N=\frac{mv^2}{r}-mg.
$$

At the contact threshold, $N=0$:

$$
\begin{aligned}
mg&=\frac{mv_{\mathrm{threshold}}^2}{r},\\
v_{\mathrm{threshold}}&=\sqrt{rg}\\
&=\sqrt{(15\,\mathrm m)(9.8\,\mathrm{m/s^2})}\\
&=12.12\,\mathrm{m/s}.
\end{aligned}
$$

Now impose $N\geq0$:

$$
\frac{mv^2}{r}-mg\geq0
\quad\Longrightarrow\quad
\boxed{v\geq12.12\,\mathrm{m/s}}.
$$

This corrects the source video's final spoken inequality. The speed must be **greater than or equal to** $12.12\,\mathrm{m/s}$, not less than or equal to it. Below that speed, the circular-contact equation asks for $N<0$; the car instead loses contact and falls inward.

```quiz
type: radio
id: mct-p8-inside-mirror
content: |-
  An unrestrained cart reaches the top of an inside loop of radius $20\,\mathrm m$ at $15\,\mathrm{m/s}$. What does the contact model predict? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p8-inside-mirror-a
  content: |-
    The minimum speed is $14\,\mathrm{m/s}$; since $15\,\mathrm{m/s}$ is larger, $N>0$ and the cart remains in contact.
  correct: true
  feedback: |-
    For an inside loop, $v_{\min}=\sqrt{rg}=\sqrt{(20)(9.8)}=14\,\mathrm{m/s}$. The actual speed is above this boundary, so $N=m(v^2/r-g)>0$ and the track can maintain contact.
- id: mct-p8-inside-mirror-b
  content: |-
    The maximum speed is $14\,\mathrm{m/s}$; since $15\,\mathrm{m/s}$ is larger, the cart loses contact.
  feedback: |-
    An inside loop has a minimum, not a maximum, contact speed. Increasing $v$ increases the required inward net force, and the track can supply the extra inward force through a positive $N$.
- id: mct-p8-inside-mirror-c
  content: |-
    The cart loses contact because gravity alone is smaller than $mv^2/r$.
  feedback: |-
    When gravity alone is insufficient, the inside track can add an inward normal force. From $mg+N=mv^2/r$, a larger required inward force gives $N>0$, which is physically allowed.
- id: mct-p8-inside-mirror-d
  content: |-
    The cart is exactly at the threshold, so $N=0$.
  feedback: |-
    The threshold is $14\,\mathrm{m/s}$, not $15\,\mathrm{m/s}$. Because the cart is above the threshold, the normal force is positive rather than zero.
- id: mct-p8-inside-mirror-e
  content: |-
    The cart remains in contact because $N=mg$ at every point on a vertical loop.
  feedback: |-
    The conclusion happens to be contact, but the reason is false. At the top, $N=m(v^2/r-g)$ and depends on speed and radius; it equals $mg$ only for the special speed satisfying $v^2/r=2g$.
```

---

<a id="choose-the-physical-side-of-the-threshold"></a>
## Choose the Physical Side of the Threshold

**Example:** Two unrestrained objects move at $9.0\,\mathrm{m/s}$ on curves of radius $10\,\mathrm m$. One is at an outside crest and the other is at the top of an inside loop. Decide whether each remains in contact.

**Explanation**

Their shared boundary speed is

$$
v_{\mathrm{threshold}}=\sqrt{(10)(9.8)}=9.90\,\mathrm{m/s}.
$$

The given speed lies below the boundary. Check that choice against $N\geq0$ rather than guessing from the common formula:

$$
\begin{aligned}
N_{\mathrm{outside}}
&=m\left(g-\frac{v^2}{r}\right)
=m(9.8-8.1)>0,\\
N_{\mathrm{inside}}
&=m\left(\frac{v^2}{r}-g\right)
=m(8.1-9.8)<0 \qquad \text{(formal result).}
\end{aligned}
$$

The outside object remains in contact. The inside-loop object cannot have a negative contact force, so its actual $N$ is zero and it loses contact.

The full sign check is:

| Speed | Outside crest | Inside loop |
|---|---|---|
| $v<\sqrt{rg}$ | $N>0$: contact | formal $N<0$: no contact |
| $v=\sqrt{rg}$ | $N=0$: just at threshold | $N=0$: just at threshold |
| $v>\sqrt{rg}$ | formal $N<0$: no contact | $N>0$: contact |

Equality belongs to both contact conditions because $N=0$ is physically allowed. Crossing to the other side of either boundary would require $N<0$, so that is where the circular-contact model fails.

```quiz
type: radio
id: mct-p8-boundary-equality
content: |-
  An unrestrained object at an outside crest and an unrestrained object at the top of an inside loop each move at exactly $v=\sqrt{rg}$ for their respective curves. What is true at that instant?
options:
- id: mct-p8-boundary-equality-a
  content: |-
    Both objects have $N=0$ and are exactly at their contact thresholds.
  correct: true
  feedback: |-
    Substituting $v^2/r=g$ gives $N=m(g-v^2/r)=0$ outside and $N=m(v^2/r-g)=0$ inside. Equality is included in both conditions, even though the allowed sides of the boundary are opposite.
- id: mct-p8-boundary-equality-b
  content: |-
    Only the outside object is at threshold; the inside-loop object has already lost contact.
  feedback: |-
    Inside-loop contact requires $v\geq\sqrt{rg}$, so equality is allowed. At equality, gravity alone supplies the required inward force and the track's normal force is zero.
- id: mct-p8-boundary-equality-c
  content: |-
    Only the inside-loop object is at threshold; the outside object has already lost contact.
  feedback: |-
    Outside-crest contact requires $v\leq\sqrt{rg}$, which also includes equality. At the boundary, gravity supplies exactly $mv^2/r$ and $N=0$.
- id: mct-p8-boundary-equality-d
  content: |-
    Both objects have $N=mg$ because their speeds match.
  feedback: |-
    Matching the boundary speed makes gravity equal to the required inward net force, $mg=mv^2/r$. No additional normal force is needed, so $N=0$, not $mg$.
- id: mct-p8-boundary-equality-e
  content: |-
    The normal forces cannot be determined without knowing each mass.
  feedback: |-
    Mass cancels in the threshold equation. More directly, inserting $v^2/r=g$ into either geometry-specific expression makes the factor multiplying $m$ equal to zero, so both normal forces are zero for any positive mass.
```

```quiz
type: radio
id: mct-p8-compare-geometries
content: |-
  Two unrestrained objects are at the tops of curves with the same radius, $18\,\mathrm m$, and each moves at $12\,\mathrm{m/s}$. One is on an outside crest; the other is inside a vertical loop. Which statement is correct? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p8-compare-geometries-a
  content: |-
    The outside object remains in contact, while the inside-loop object loses contact.
  correct: true
  feedback: |-
    The shared boundary is $\sqrt{(18)(9.8)}\approx13.28\,\mathrm{m/s}$. The speed $12\,\mathrm{m/s}$ is below it, which satisfies the outside maximum $v\leq\sqrt{rg}$ but not the inside minimum $v\geq\sqrt{rg}$.
- id: mct-p8-compare-geometries-b
  content: |-
    Both objects remain in contact because both have the same value of $\sqrt{rg}$.
  feedback: |-
    The common boundary value does not give a common allowed side. At an outside crest $N=m(g-v^2/r)$, while inside a loop $N=m(v^2/r-g)$; below the boundary only the outside normal force is nonnegative.
- id: mct-p8-compare-geometries-c
  content: |-
    The outside object loses contact, while the inside-loop object remains in contact.
  feedback: |-
    This reverses the two inequalities. A speed below $\sqrt{rg}$ is allowed at an outside crest, where gravity can supply enough inward force, but is too slow at the top of an inside loop.
- id: mct-p8-compare-geometries-d
  content: |-
    Both objects are exactly at the threshold, so both have $N=0$.
  feedback: |-
    Exact threshold contact would require $v=13.28\,\mathrm{m/s}$. At $12\,\mathrm{m/s}$, the outside normal force is positive and the inside-loop contact equation gives a negative formal value.
- id: mct-p8-compare-geometries-e
  content: |-
    Both objects lose contact because $12\,\mathrm{m/s}<\sqrt{rg}$.
  feedback: |-
    Being below the boundary causes loss of contact only inside the loop. At an outside crest, lower speed reduces the required inward force and allows a nonnegative outward normal force, so contact remains possible.
```

---

<a id="summary"></a>
## Summary

When a problem says **just maintains contact**, **just leaves the track**, **maximum crest speed**, or **minimum loop speed**:

1. Point positive radial inward and draw the real forces.
2. Write $\sum F_r=mv^2/r$ before setting anything to zero.
3. Set $N=0$ only at the contact boundary and solve $v_{\mathrm{threshold}}=\sqrt{rg}$.
4. Return to the geometry-specific expression for $N$ and require $N\geq0$.

At an outside crest, $N=mg-mv^2/r$, so contact requires $v\leq\sqrt{rg}$. At the top of an inside loop, $N=mv^2/r-mg$, so contact requires $v\geq\sqrt{rg}$. A negative formal $N$ means the contact model has failed; the actual normal force is zero after separation.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
