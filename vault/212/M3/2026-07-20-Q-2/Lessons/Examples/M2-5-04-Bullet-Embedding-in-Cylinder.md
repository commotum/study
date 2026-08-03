# Bullet Embedding in a Solid Cylinder

Source: [[212/M2/2026-07-14-M2-5/Source/Lecture-Notes#Bullet Embedding in a Solid Cylinder|Lecture example]]

## 1. The Problem

A uniform solid cylinder of mass $M$ and radius $R$ is initially at rest and rotates freely about a fixed central spindle. A bullet of mass $m$ travels tangentially at speed $v$, strikes the rim, and embeds in the cylinder.

**A.** Choose an axis and explain why angular momentum about that axis is conserved during the short collision.

**B.** Calculate the bullet’s initial angular momentum about the spindle.

**C.** Calculate the final moment of inertia of the cylinder-bullet system.

**D.** Solve symbolically for the final angular speed $\omega_f$.

**E.** Check the units and limiting behavior as $m\to0$.

**F.** State whether mechanical energy is conserved and justify the answer.

## 2. The Equations

- Particle angular momentum:

  $$
  \vec L=\vec r\times m\vec v,
  \qquad
  L=mrv\sin\phi.
  $$

  Tangential impact gives $\phi=90^\circ$.

- Solid-cylinder moment of inertia:

  $$
  I_{\mathrm{cyl}}=\frac12MR^2.
  $$

- Embedded point-mass inertia:

  $$
  I_{\mathrm{bullet}}=mR^2.
  $$

- Angular-momentum conservation:

  $$
  L_0=L_f=I_f\omega_f.
  $$

  The spindle force has zero torque about the spindle itself during the collision.

## 3. The Walkthrough

1. Choose the spindle as the axis. The spindle’s impulsive force acts at that axis, so its torque there is zero. Over the short collision, other external torques are negligible.

2. The cylinder begins at rest. Because the bullet velocity is perpendicular to the impact radius,

   $$
   L_0=mRv.
   $$

3. After embedding, the cylinder and bullet rotate together. Their moments of inertia add:

   $$
   I_f
   =
   \frac12MR^2+mR^2.
   $$

4. Conserve angular momentum:

   $$
   mRv
   =
   \left(
   \frac12MR^2+mR^2
   \right)\omega_f.
   $$

5. Solve for the final angular speed:

   $$
   \omega_f
   =
   \frac{mRv}{\frac12MR^2+mR^2}
   =
   \frac{mv}{R(M/2+m)}.
   $$

6. The units are

   $$
   \frac{(\text{kg})(\text{m/s})}
        {(\text{m})(\text{kg})}
   =\text{s}^{-1},
   $$

   equivalent to $\text{rad/s}$. As $m\to0$, $\omega_f\to0$, as expected.

7. Mechanical energy is not conserved because embedding is perfectly inelastic. Some initial kinetic energy becomes internal energy even though angular momentum about the spindle is conserved.
