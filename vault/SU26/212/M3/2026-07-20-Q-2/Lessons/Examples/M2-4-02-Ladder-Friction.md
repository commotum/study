# Ladder Against a Frictionless Wall

Source: [[212/M2/2026-07-13-M2-4/Source/Lecture-Notes#Example 2: Ladder Against a Frictionless Wall|Lecture example]]

## 1. The Problem

A uniform ladder of length $L$ and mass $m$ rests at an angle $\theta$ above a horizontal floor. The wall is frictionless. The floor has coefficient of static friction $\mu_s$, and the ladder is just at the threshold of slipping.

**A.** Draw the extended free-body diagram and label where all four forces act.

**B.** Use vertical equilibrium to solve for the floor’s normal force.

**C.** Use horizontal equilibrium and the impending-slip condition to relate the wall normal force to $\mu_s$.

**D.** Choose the bottom of the ladder as the pivot and write the torque-balance equation.

**E.** Solve symbolically for the minimum coefficient of static friction $\mu_s$.

**F.** Check that $\mu_s$ is dimensionless and predict how it changes as the ladder becomes steeper.

## 2. The Equations

- Static force balance:

  $$
  \sum F_x=0,\qquad \sum F_y=0.
  $$

- Maximum static friction:

  $$
  f_{s,\max}=\mu_sN_F.
  $$

  Equality applies because the ladder is at the threshold of slipping.

- Static torque balance:

  $$
  \sum\tau=0.
  $$

- Torque magnitude:

  $$
  \tau=rF\sin\phi.
  $$

  Choosing the bottom pivot removes both unknown floor-force torques.

## 3. The Walkthrough

1. The forces are the ladder’s weight $mg$ at its midpoint, floor normal $N_F$ upward at the bottom, floor friction $f_s$ horizontally at the bottom, and wall normal $N_W$ horizontally at the top. There is no wall-friction force.

2. Vertical equilibrium gives

   $$
   N_F-mg=0,
   \qquad
   N_F=mg.
   $$

3. Horizontal equilibrium gives $N_W=f_s$. At impending slip,

   $$
   f_s=\mu_sN_F=\mu_smg,
   $$

   so

   $$
   N_W=\mu_smg.
   $$

4. Choose the bottom of the ladder as the pivot. The floor forces have zero lever arm. The wall force produces torque

   $$
   \tau_W=N_WL\sin\theta.
   $$

5. The weight acts at $L/2$, and its perpendicular factor is $\cos\theta$:

   $$
   \tau_g=mg\frac{L}{2}\cos\theta.
   $$

6. Balance the opposing torques:

   $$
   N_WL\sin\theta
   =
   mg\frac{L}{2}\cos\theta.
   $$

7. Substitute $N_W=\mu_smg$ and cancel $mgL$:

   $$
   \mu_s\sin\theta=\frac12\cos\theta.
   $$

8. Solve:

   $$
   \mu_s
   =\frac12\frac{\cos\theta}{\sin\theta}
   =\frac12\cot\theta
   =\frac{1}{2\tan\theta}.
   $$

9. The coefficient is dimensionless. As $\theta$ increases, $\tan\theta$ increases, so the required friction decreases; a steeper ladder needs less horizontal friction to remain in equilibrium.
