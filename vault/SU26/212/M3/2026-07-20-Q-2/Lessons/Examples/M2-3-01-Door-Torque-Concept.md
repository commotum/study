# Door Concept Question: Comparing Torques

Source: [[212/M2/2026-07-09-M2-3/Source/Lecture-Notes#Door Concept Question|Lecture example]]

## 1. The Problem

A door of width $R$ rotates about a vertical hinge. Four forces have the same magnitude $F$ and act in the horizontal plane:

- Force A acts at the outer edge, perpendicular to the door.
- Force B acts halfway from the hinge to the outer edge, perpendicular to the door.
- Force C acts at the outer edge at an angle of $30^\circ$ to the line from the hinge.
- Force D acts at the hinge.

**A.** Write the torque magnitude produced by each force about the hinge.

**B.** Rank the four torque magnitudes from greatest to least.

**C.** Identify which force produces the maximum possible torque for the given $F$ and door width.

**D.** Identify every geometric way an applied force could produce zero torque about the hinge.

**E.** Explain why equal force magnitudes do not imply equal rotational effects.

## 2. The Equations

- Torque vector:

  $$
  \vec{\tau}=\vec{r}\times\vec{F}.
  $$

  Its direction is perpendicular to the plane containing $\vec{r}$ and $\vec{F}$.

- Torque magnitude:

  $$
  \tau=rF\sin\theta.
  $$

  Both the distance from the pivot and the perpendicular component of force matter.

- Moment-arm form:

  $$
  \tau=Fd_\perp.
  $$

  Here $d_\perp$ is the shortest distance from the hinge to the force’s line of action.

- Limiting cases:

  $$
  \tau_{\max}=rF\quad(\theta=90^\circ),
  \qquad
  \tau=0\quad(r=0\text{ or }\sin\theta=0).
  $$

## 3. The Walkthrough

1. Force A has $r=R$ and $\theta=90^\circ$:

   $$
   \tau_A=RF.
   $$

2. Force B has $r=R/2$ and $\theta=90^\circ$:

   $$
   \tau_B=\frac{RF}{2}.
   $$

3. Force C has $r=R$ and $\theta=30^\circ$:

   $$
   \tau_C=RF\sin30^\circ=\frac{RF}{2}.
   $$

4. Force D acts at the pivot, so $r=0$:

   $$
   \tau_D=0.
   $$

5. The ranking is

   $$
   \tau_A>\tau_B=\tau_C>\tau_D.
   $$

6. Force A produces the maximum because it combines the largest available radius with a perpendicular force. Zero torque occurs when the force is applied at the hinge or when its line of action passes through the hinge, corresponding to $\theta=0^\circ$ or $180^\circ$.

7. Equal forces produce unequal torques because torque measures turning effect, not merely force magnitude.
