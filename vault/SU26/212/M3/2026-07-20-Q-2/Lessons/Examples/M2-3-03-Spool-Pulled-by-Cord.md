# Spool Pulled by a Cord

Source: [[212/M2/2026-07-09-M2-3/Source/Lecture-Notes#Spool Pulled by a Cord|Lecture example]]

## 1. The Problem

A solid cylindrical spool of mass $m$ and radius $r$ rotates freely about a fixed horizontal spindle through its center. A cord wrapped around the rim is pulled with constant tangential tension $T$. The center of the spool does not translate.

**A.** Draw the translational free-body diagram, including the weight, support forces, and cord tension.

**B.** Write the horizontal and vertical force-balance equations.

**C.** Identify which forces produce torque about the spindle axis and explain why the spindle force produces none.

**D.** Solve symbolically for the spool’s angular acceleration $\alpha$.

**E.** Check the units of the symbolic result and state the rotation direction from the applied tension.

## 2. The Equations

- Translational equilibrium of the fixed center:

  $$
  \sum F_x=0,\qquad \sum F_y=0.
  $$

  The spool may rotate even though its center has zero translational acceleration.

- Tangential torque:

  $$
  \tau=Tr.
  $$

  The tension is perpendicular to the radius at the contact point.

- Rotational Newton’s second law:

  $$
  \sum\tau=I\alpha.
  $$

- Solid-cylinder moment of inertia:

  $$
  I=\frac12mr^2.
  $$

## 3. The Walkthrough

1. Let $N_1$ be the upward support force and $N_2$ the horizontal spindle force opposing the tension. Translational balance gives

   $$
   T-N_2=0,
   \qquad
   N_1-mg=0.
   $$

   Therefore $N_2=T$ and $N_1=mg$.

2. Choose the spindle axis as the torque origin. The weight and vertical support act through the center line in the lecture model, and the spindle force acts directly at the pivot. Their moment arms about that axis are zero.

3. The tangential cord tension supplies the net torque:

   $$
   \sum\tau=Tr.
   $$

4. Apply the rotational equation:

   $$
   Tr=\left(\frac12mr^2\right)\alpha.
   $$

5. Isolate the angular acceleration:

   $$
   \alpha
   =\frac{Tr}{(1/2)mr^2}
   =\frac{2T}{mr}.
   $$

6. Check the units:

   $$
   \frac{\mathrm{N}}{\mathrm{kg}\cdot\mathrm{m}}
   =
   \frac{\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}^2}
        {\mathrm{kg}\cdot\mathrm{m}}
   =\mathrm{s}^{-2},
   $$

   which is equivalent to $\text{rad/s}^2$. The right-hand rule applied to the tension determines the sign of $\alpha$.
