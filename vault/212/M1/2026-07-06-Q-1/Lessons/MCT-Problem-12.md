# Switching from Circular Motion to Projectile Motion at Release

<!--
lesson-id: 212-M1-086
topic-code: MTH212.M1.86
-->

## Table of Contents

- [Introduction](#introduction)
- [Carry the Tangent Velocity Across Release](#carry-the-tangent-velocity-across-release)
- [Evolve the Horizontal and Vertical Components](#evolve-the-horizontal-and-vertical-components)
- [Match the Equation to the Release Geometry](#match-the-equation-to-the-release-geometry)
- [Keep Only the Physical Time](#keep-only-the-physical-time)
- [Pass Circular-Motion Data Into the Projectile](#pass-circular-motion-data-into-the-projectile)
- [Summary](#summary)

## Prerequisites

- Resolve a vector into horizontal and vertical components using a stated angle.
- Use constant-acceleration kinematics with a consistent vertical sign convention.
- Use $a_r=v^2/r$ and write a signed radial force equation when release speed is not given.

---

<a id="introduction"></a>
## Introduction

A string is cut, a track ends, or an object otherwise leaves a circular path. That event is the cue to switch models.

Immediately before release, the circular constraint bends the path. If the release gives no impulse, position and velocity cannot jump at that instant. The object's projectile velocity is therefore the same instantaneous velocity it had on the circle: **tangent to the path**, not radially outward. The acceleration can change at once because the constraint force disappears.

Use one handoff procedure:

1. Finish the pre-release calculation if the tangent speed is not already known.
2. Freeze the tangent speed and direction at the release instant.
3. Resolve that tangent into $v_{0x}$ and $v_{0y}$ using the angle actually drawn.
4. After release, use $a_x=0$ and $a_y=-g$ when air resistance is neglected.
5. Solve the requested horizontal or vertical motion, then keep only results that occur at $t\geq0$.

Do not carry radial acceleration, tension, or a normal force into the projectile stage. Those quantities describe the constrained motion before release.

---

<a id="carry-the-tangent-velocity-across-release"></a>
## Carry the Tangent Velocity Across Release

**Example:** A bead moves counterclockwise on a circular track. It leaves the track at the rightmost point with speed $12\,\mathrm{m/s}$. State its initial projectile velocity direction.

**Explanation**

At the rightmost point, the radius points right. The counterclockwise tangent points up, so the release velocity is

$$
\vec v_0=(0\,\hat{\mathbf i}+12\,\hat{\mathbf j})\,\mathrm{m/s}.
$$

The release changes the force model, not the velocity vector already present:

| State | Velocity | Forces and acceleration |
| --- | --- | --- |
| Just before release | tangent to the circle | gravity plus the circular constraint; $a_r=v^2/r$ points inward |
| Just after release | the same tangent vector | gravity only; $\vec a=-g\hat{\mathbf j}$ |

The bead does not launch radially outward. Once it leaves the track, gravity curves this tangent motion into a projectile path.

```quiz
type: radio
id: mct-p12-tangent-release
shuffle: true
content: |-
  A ball moves clockwise around a vertical circle. Its string is cut at the leftmost point. Which direction is the ball's velocity immediately after the cut?
options:
- id: mct-p12-tangent-release-a
  content: |-
    Upward, tangent to the circle
  correct: true
  feedback: |-
    Velocity is continuous through a release that supplies no impulse. Clockwise motion at the leftmost point has an upward tangent, so the ball begins its projectile motion upward.
- id: mct-p12-tangent-release-b
  content: |-
    Leftward, radially away from the center
  feedback: |-
    The radius locates the center and sets the pre-release acceleration direction; it is not the velocity direction. Circular-motion velocity is tangent to the path, which is upward here.
- id: mct-p12-tangent-release-c
  content: |-
    Rightward, toward the center
  feedback: |-
    Rightward is the inward radial direction at the leftmost point. The pre-release acceleration can point inward, but the instantaneous velocity is perpendicular to that radius and points upward.
- id: mct-p12-tangent-release-d
  content: |-
    Downward because gravity acts after the cut
  feedback: |-
    Gravity changes velocity over time; it does not replace the existing velocity instantaneously. The initial projectile velocity is the upward tangent, although gravity immediately begins reducing its vertical component.
- id: mct-p12-tangent-release-e
  content: |-
    Along the original circle because inertia preserves circular motion
  feedback: |-
    Inertia preserves the instantaneous tangent velocity, not the curved path. Continued circular motion would require an inward constraint force, and cutting the string removes that force.
```

---

<a id="evolve-the-horizontal-and-vertical-components"></a>
## Evolve the Horizontal and Vertical Components

**Source-video component timeline:** A projectile begins with

$$
v_{0x}=7\,\mathrm{m/s},
\qquad
v_{0y}=30\,\mathrm{m/s},
$$

and the video rounds gravity to $g=10\,\mathrm{m/s^2}$. With upward positive,

$$
v_x(t)=7,
\qquad
v_y(t)=30-10t.
$$

In component form,

$$
\vec v(t)=7\,\hat{\mathbf i}+(30-10t)\,\hat{\mathbf j}\ \mathrm{m/s}.
$$

Keep this vector form while the question concerns direction or a component. Recombine the components with $|\vec v|=\sqrt{v_x^2+v_y^2}$ only when the question asks for speed.

The components and total speed are therefore

| $t$ (s) | $v_x$ (m/s) | $v_y$ (m/s) | $|\vec v|=\sqrt{v_x^2+v_y^2}$ (m/s) |
| ---: | ---: | ---: | ---: |
| $0$ | $7$ | $30$ | $30.8$ |
| $1$ | $7$ | $20$ | $21.2$ |
| $2$ | $7$ | $10$ | $12.2$ |
| $3$ | $7$ | $0$ | $7.0$ |
| $4$ | $7$ | $-10$ | $12.2$ |
| $5$ | $7$ | $-20$ | $21.2$ |
| $6$ | $7$ | $-30$ | $30.8$ |

At the apex, only the **vertical component** is zero. The projectile still moves horizontally at $7\,\mathrm{m/s}$, so its total velocity and speed are not zero. Likewise, at $t=5\,\mathrm s$, $20\,\mathrm{m/s}$ is the magnitude of the vertical component; the total speed is

$$
|\vec v|=\sqrt{7^2+(-20)^2}=\sqrt{449}\approx21.2\,\mathrm{m/s}.
$$

This corrects the video's one-dimensional use of “speed.” In two dimensions, speed is the magnitude of the whole velocity vector.

```quiz
type: radio
id: mct-p12-component-timeline
shuffle: true
content: |-
  In the source-video timeline, what are the velocity vector and total speed at $t=5\,\mathrm s$?
options:
- id: mct-p12-component-timeline-a
  content: |-
    $\vec v=(7\,\hat{\mathbf i}-20\,\hat{\mathbf j})\,\mathrm{m/s}$ and $|\vec v|\approx21.2\,\mathrm{m/s}$
  correct: true
  feedback: |-
    Gravity changes only the vertical component, so $v_x=7$ and $v_y=30-10(5)=-20\,\mathrm{m/s}$. Speed is the vector magnitude $\sqrt{7^2+(-20)^2}\approx21.2\,\mathrm{m/s}$.
- id: mct-p12-component-timeline-b
  content: |-
    $\vec v=(7\,\hat{\mathbf i}-20\,\hat{\mathbf j})\,\mathrm{m/s}$ and $|\vec v|=20\,\mathrm{m/s}$
  feedback: |-
    The components are correct, but $20\,\mathrm{m/s}$ is only $|v_y|$. Because $v_x$ is still $7\,\mathrm{m/s}$, the whole-vector magnitude is $\sqrt{7^2+20^2}$.
- id: mct-p12-component-timeline-c
  content: |-
    $\vec v=(0\,\hat{\mathbf i}-20\,\hat{\mathbf j})\,\mathrm{m/s}$ and $|\vec v|=20\,\mathrm{m/s}$
  feedback: |-
    Neglecting air resistance makes horizontal acceleration zero, not horizontal velocity zero. The projectile retains $v_x=7\,\mathrm{m/s}$ throughout the flight.
- id: mct-p12-component-timeline-d
  content: |-
    $\vec v=(7\,\hat{\mathbf i}+20\,\hat{\mathbf j})\,\mathrm{m/s}$ and $|\vec v|\approx21.2\,\mathrm{m/s}$
  feedback: |-
    The speed magnitude is right, but the vertical sign is not. At $t=5\,\mathrm s$, the projectile is descending, so $v_y=30-50=-20\,\mathrm{m/s}$.
- id: mct-p12-component-timeline-e
  content: |-
    $\vec v=(7\,\hat{\mathbf i}-20\,\hat{\mathbf j})\,\mathrm{m/s}$ and $|\vec v|=-21.2\,\mathrm{m/s}$
  feedback: |-
    A velocity component may be negative because it carries direction, but speed is a magnitude and cannot be negative. Here the magnitude is positive $21.2\,\mathrm{m/s}$.
```

---

<a id="match-the-equation-to-the-release-geometry"></a>
## Match the Equation to the Release Geometry

**Source-video trajectory cases:** Once the tangent velocity becomes the projectile's initial velocity, use the release and landing heights to decide which condition applies. In this table, $\theta$ is measured from the horizontal, so

$$
v_{0x}=v_0\cos\theta,
\qquad
v_{0y}=v_0\sin\theta.
$$

| Release geometry | Initial components | Useful condition |
| --- | --- | --- |
| Horizontal launch from a cliff | $v_{0x}=v_0$, $v_{0y}=0$ | Horizontal and vertical motion share the same flight time. |
| Angled launch returning to its release height | $v_{0x}=v_0\cos\theta$, $v_{0y}=v_0\sin\theta$ | Rise/fall symmetry applies only because the endpoint heights match. |
| Angled launch from an elevation | $v_{0x}=v_0\cos\theta$, $v_{0y}=v_0\sin\theta$ | Set the chosen final height in $y_f=y_0+v_{0y}t-\tfrac12gt^2$ and solve for time. |

If an angle is measured from the vertical instead, the sine and cosine roles swap. The component triangle, not a memorized label, decides which function to use.

**Source-video Problem 1:** A ball launches horizontally from a cliff at $v_x=20\,\mathrm{m/s}$ and lands after $10\,\mathrm s$. Find the cliff height and range.

**Explanation**

Choose upward as positive. Then $v_{0y}=0$, $a_y=-g$, and $\Delta y=-h$:

$$
\begin{aligned}
-h&=0-\frac12g t^2,\\
h&=\frac12(9.8)(10)^2=490\,\mathrm m.
\end{aligned}
$$

Horizontal speed is constant, so

$$
R=v_xt=(20)(10)=200\,\mathrm m.
$$

**Source-video Problem 2:** A ball rolls horizontally from a $200\,\mathrm m$ cliff. Find the flight time.

**Explanation**

The horizontal speed is not needed for a vertical fall-time question. With $v_{0y}=0$,

$$
h=\frac12gt^2
\quad\Longrightarrow\quad
t=\sqrt{\frac{2h}{g}}
=\sqrt{\frac{2(200)}{9.8}}
=6.389\,\mathrm s.
$$

```quiz
type: radio
id: mct-p12-horizontal-launch
shuffle: true
content: |-
  A ball launches horizontally at $15\,\mathrm{m/s}$ and lands $4.0\,\mathrm s$ later. What are its vertical drop and horizontal range? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p12-horizontal-launch-a
  content: |-
    $78.4\,\mathrm m$ down and $60\,\mathrm m$ horizontally
  correct: true
  feedback: |-
    A horizontal launch has $v_{0y}=0$, so the drop magnitude is $\tfrac12gt^2=\tfrac12(9.8)(4.0)^2=78.4\,\mathrm m$. Independently, the range is $v_xt=(15)(4.0)=60\,\mathrm m$.
- id: mct-p12-horizontal-launch-b
  content: |-
    $39.2\,\mathrm m$ down and $60\,\mathrm m$ horizontally
  feedback: |-
    The range is correct, but the drop uses $t$ instead of $t^2$. Constant vertical acceleration gives $\tfrac12gt^2$, so $4.0^2$, not $4.0$, belongs in the vertical calculation.
- id: mct-p12-horizontal-launch-c
  content: |-
    $78.4\,\mathrm m$ down and $240\,\mathrm m$ horizontally
  feedback: |-
    The drop is correct, but $240$ comes from an extra factor of time. With constant $v_x$, horizontal displacement is $v_xt=(15)(4.0)=60\,\mathrm m$.
- id: mct-p12-horizontal-launch-d
  content: |-
    $138.4\,\mathrm m$ down and $60\,\mathrm m$ horizontally
  feedback: |-
    This adds the independent vertical drop and horizontal range. Perpendicular displacements answer different questions; the vertical drop remains $78.4\,\mathrm m$ and the horizontal range remains $60\,\mathrm m$.
- id: mct-p12-horizontal-launch-e
  content: |-
    $60\,\mathrm m$ down and $78.4\,\mathrm m$ horizontally
  feedback: |-
    This swaps the component results. The given $15\,\mathrm{m/s}$ is horizontal, while gravity controls the vertical drop through $\tfrac12gt^2$.
```

---

<a id="keep-only-the-physical-time"></a>
## Keep Only the Physical Time

**Source-video Problem 3(a), vertical boundary case:** A ball is released from rest $800\,\mathrm m$ above the ground. Find the fall time.

**Explanation**

With $v_{0y}=0$, the horizontal component is absent and

$$
t=\sqrt{\frac{2h}{g}}
=\sqrt{\frac{2(800)}{9.8}}
\approx12.78\,\mathrm s.
$$

**Source-video Problem 3(b), controlled change:** The same ball is instead thrown straight down at $30\,\mathrm{m/s}$. Find the fall time.

**Explanation**

Keep upward positive. Then $\Delta y=-800\,\mathrm m$, $v_{0y}=-30\,\mathrm{m/s}$, and $a_y=-9.8\,\mathrm{m/s^2}$:

$$
-800=-30t-4.9t^2.
$$

Put the equation in standard form before using the quadratic formula:

$$
4.9t^2+30t-800=0.
$$

Thus

$$
t=\frac{-30\pm\sqrt{30^2-4(4.9)(-800)}}{2(4.9)}
=\frac{-30\pm\sqrt{16580}}{9.8}.
$$

The roots are approximately $10.08\,\mathrm s$ and $-16.20\,\mathrm s$. The negative root lies before the release instant, so the physical flight time is

$$
t=10.08\,\mathrm s.
$$

Both numbers solve the extended quadratic trajectory, but only $t\geq0$ belongs to the model that starts its clock at release. The physical time is shorter than $12.78\,\mathrm s$, as expected for a ball given an initial downward velocity.

```quiz
type: radio
id: mct-p12-physical-time
shuffle: true
content: |-
  A ball is thrown straight down at $10\,\mathrm{m/s}$ from a height of $125\,\mathrm m$. How long after release does it hit the ground? Use upward as positive and $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p12-physical-time-a
  content: |-
    $4.13\,\mathrm s$
  correct: true
  feedback: |-
    The signed equation is $-125=-10t-4.9t^2$, or $4.9t^2+10t-125=0$. Its nonnegative root is $[-10+\sqrt{2550}]/9.8=4.13\,\mathrm s$.
- id: mct-p12-physical-time-b
  content: |-
    $5.05\,\mathrm s$
  feedback: |-
    This is the release-from-rest time $\sqrt{2h/g}$. The ball already has a downward velocity of $10\,\mathrm{m/s}$, so the linear term $-10t$ must be included and the flight time is shorter.
- id: mct-p12-physical-time-c
  content: |-
    $-6.17\,\mathrm s$
  feedback: |-
    This is the other algebraic root of the position equation. It describes an extrapolated time before the chosen release instant, so it is not the requested post-release flight time.
- id: mct-p12-physical-time-d
  content: |-
    $6.17\,\mathrm s$
  feedback: |-
    Changing the negative root's sign does not turn it into another physical solution. Substitute candidate times into $-125=-10t-4.9t^2$; only $t=4.13\,\mathrm s$ is nonnegative and satisfies the release model.
- id: mct-p12-physical-time-e
  content: |-
    $12.5\,\mathrm s$
  feedback: |-
    Dividing height by the initial speed assumes the ball keeps moving at $10\,\mathrm{m/s}$. Gravity increases its downward speed, so constant-speed division overestimates the time.
```

---

<a id="pass-circular-motion-data-into-the-projectile"></a>
## Pass Circular-Motion Data Into the Projectile

**M1-5 lecture release application:** A ball of mass $m=0.56\,\mathrm{kg}$ moves clockwise on a string of length $L=0.88\,\mathrm m$. At the shown instant, the tension is $T_{\mathrm{tens}}=1.2\,\mathrm N$ and $\theta=14^\circ$.

![](<../../2026-07-02-M1-5/Source/Images/vertical-circle-ball-string-diagram.png>)

In this diagram, $\theta$ is measured between the outward radius and upward vertical. Equivalently, the inward radial direction makes angle $\theta$ with downward vertical, and the clockwise tangent points $\theta$ above horizontal. That geometry gives

$$
v_{0y}=v_0\sin\theta.
$$

**Explanation**

Finish the circular-motion stage first. Tension and the inward component of gravity supply the radial force:

$$
T_{\mathrm{tens}}+mg\cos\theta=ma_r.
$$

Therefore,

$$
a_r=\frac{T_{\mathrm{tens}}}{m}+g\cos\theta
=\frac{1.2}{0.56}+9.8\cos14^\circ
=11.65\,\mathrm{m/s^2}.
$$

Since $a_r=v_0^2/L$ immediately before the cut,

$$
v_0^2=a_rL
=L\left(\frac{T_{\mathrm{tens}}}{m}+g\cos\theta\right).
$$

Now make the model switch. The string is cut, tension disappears, and the tangent velocity becomes the projectile's initial velocity. At the maximum height, $v_y=0$ but $v_x$ generally remains nonzero. Use the vertical no-time equation:

$$
\begin{aligned}
0&=v_{0y}^2-2g\Delta y_{\max},\\
\Delta y_{\max}&=\frac{v_0^2\sin^2\theta}{2g}\\
&=\frac{L\left(\dfrac{T_{\mathrm{tens}}}{m}+g\cos\theta\right)\sin^2\theta}{2g}.
\end{aligned}
$$

Substitution gives

$$
\Delta y_{\max}
=\frac{(0.88)(11.65)\sin^2(14^\circ)}{2(9.8)}
=0.0306\,\mathrm m
\approx0.031\,\mathrm m.
$$

The ball rises about $3.1\,\mathrm{cm}$ above its release point. If another diagram defines its angle from the vertical or uses the opposite tangent direction, resolve that tangent again rather than reusing $v_0\sin\theta$ automatically.

```quiz
type: radio
id: mct-p12-circular-handoff
shuffle: true
content: |-
  Just before release, a ball has radial acceleration $a_r=8.0\,\mathrm{m/s^2}$ on a circular path of radius $L=0.50\,\mathrm m$. Its tangent points $30^\circ$ above horizontal. How far does it rise above the release point? Use $g=9.8\,\mathrm{m/s^2}$.
options:
- id: mct-p12-circular-handoff-a
  content: |-
    $0.0510\,\mathrm m$
  correct: true
  feedback: |-
    The circular stage gives $v_0^2=a_rL=(8.0)(0.50)=4.0\,\mathrm{m^2/s^2}$. The vertical part is $v_0^2\sin^230^\circ=1.0\,\mathrm{m^2/s^2}$, so the rise is $1.0/[2(9.8)]=0.0510\,\mathrm m$.
- id: mct-p12-circular-handoff-b
  content: |-
    $0.204\,\mathrm m$
  feedback: |-
    This uses the full tangent speed as though it were vertical. Only $v_{0y}=v_0\sin30^\circ$ raises the ball; the horizontal component remains horizontal.
- id: mct-p12-circular-handoff-c
  content: |-
    $0.102\,\mathrm m$
  feedback: |-
    This uses one factor of $\sin30^\circ$. The height equation contains $v_{0y}^2$, so substituting $v_{0y}=v_0\sin\theta$ produces $v_0^2\sin^2\theta$.
- id: mct-p12-circular-handoff-d
  content: |-
    $0.0128\,\mathrm m$
  feedback: |-
    This squares the trigonometric factor twice. Because $v_0^2$ is already available from $a_rL$, multiply it by one $\sin^2\theta$ factor before dividing by $2g$.
- id: mct-p12-circular-handoff-e
  content: |-
    $0.408\,\mathrm m$
  feedback: |-
    This omits both the vertical-component factor and the $2$ in the no-time kinematic equation. The rise is $v_{0y}^2/(2g)$, with $v_{0y}=v_0\sin30^\circ$.
```

---

<a id="summary"></a>
## Summary

When a circular constraint disappears:

1. Find the speed immediately before release if needed, using $a_r=v^2/r$ or a radial force equation.
2. Carry the instantaneous **tangent** velocity across the release. Do not point it radially outward.
3. Define the angle from the diagram, then resolve the tangent into $v_{0x}$ and $v_{0y}$.
4. After release, use independent components: $a_x=0$ and $a_y=-g$ when drag is neglected.
5. At maximum height, set only $v_y=0$; total speed can remain nonzero.
6. If a height equation produces two times, keep only a root in the post-release interval $t\geq0$.

Finish the circular model, pass its tangent velocity into projectile kinematics, and leave pre-release radial acceleration and constraint forces out of the post-release equations.

<!-- lesson-nav:start -->

---

```update-progress
```

[[212/Home|Home]]
[[212/0. Table of Contents/TOC|Table of Contents]]

---

<!-- lesson-nav:end -->
