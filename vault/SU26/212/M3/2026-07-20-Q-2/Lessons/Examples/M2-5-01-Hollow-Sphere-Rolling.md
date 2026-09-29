# Hollow Sphere Rolling Down a Ramp

Source: [[212/M2/2026-07-14-M2-5/Source/Lecture-Notes#Hollow Sphere Rolling Down a Ramp|Lecture example]]

## 1. The Problem

A thin hollow sphere of mass $m$ and radius $R$ starts from rest and rolls without slipping a distance $d$ down a ramp inclined at angle $\theta$ above the horizontal. Neglect air resistance and rolling losses.

**A.** Determine the vertical height change in terms of $d$ and $\theta$.

**B.** Write the complete mechanical-energy equation, including every form of final kinetic energy.

**C.** State the moment of inertia of a thin spherical shell and apply the no-slip constraint.

**D.** Solve symbolically for the center-of-mass speed $v_f$ at the bottom.

**E.** Check the units and identify which given quantities cancel.

**F.** Explain why using only $\frac12mv_f^2$ would overestimate the speed.

## 2. The Equations

- Ramp geometry:

  $$
  h=d\sin\theta.
  $$

- Conservation of mechanical energy:

  $$
  mgh
  =
  \frac12mv_f^2+\frac12I\omega_f^2.
  $$

  A rolling body has both translational and rotational kinetic energy.

- Hollow-sphere moment of inertia:

  $$
  I=\frac23mR^2.
  $$

- Rolling-without-slipping constraint:

  $$
  v_f=\omega_fR.
  $$

  Translation and rotation are kinematically linked.

## 3. The Walkthrough

1. The sphere descends through vertical height

   $$
   h=d\sin\theta.
   $$

2. With the bottom as the zero of gravitational potential energy, conservation gives

   $$
   mgd\sin\theta
   =
   \frac12mv_f^2+\frac12I\omega_f^2.
   $$

3. Substitute the hollow-sphere inertia and $\omega_f=v_f/R$:

   $$
   \frac12I\omega_f^2
   =
   \frac12\left(\frac23mR^2\right)
   \left(\frac{v_f}{R}\right)^2
   =
   \frac13mv_f^2.
   $$

4. Combine the kinetic-energy terms:

   $$
   mgd\sin\theta
   =
   \left(\frac12+\frac13\right)mv_f^2
   =
   \frac56mv_f^2.
   $$

5. Cancel $m$ and solve:

   $$
   v_f^2=\frac65gd\sin\theta,
   \qquad
   v_f=\sqrt{\frac65gd\sin\theta}.
   $$

6. Inside the square root, $gd$ has units $\mathrm{m}^2/\mathrm{s}^2$, so the result has units $\mathrm{m}/\mathrm{s}$. Both $m$ and $R$ cancel.

7. Omitting rotational energy would give $\sqrt{2gd\sin\theta}$, which is too large because it assigns all available energy to translation.
