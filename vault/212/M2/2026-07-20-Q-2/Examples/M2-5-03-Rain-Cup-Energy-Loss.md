# Mechanical Energy Lost in the Rain-Cup Collision

Source: [[212/M2/2026-07-14-M2-5/Source/Lecture-Notes#Mechanical Energy Lost in the Rain-Cup Collision|Lecture example]]

## 1. The Problem

Two cups initially have combined moment of inertia

$$
I_0=\frac12md^2
$$

and rotate at angular speed $\omega_0$. Rain sticks in the cups, increasing the combined moment of inertia to

$$
I_f=md^2.
$$

External torque about the axle is negligible, and the incoming rain has zero angular momentum about the axle.

**A.** Use angular-momentum conservation to obtain $\omega_f$.

**B.** Calculate the initial rotational kinetic energy $K_0$.

**C.** Calculate the final rotational kinetic energy $K_f$.

**D.** Determine the increase in thermal/internal energy, $\Delta E_{\mathrm{th}}=K_0-K_f$.

**E.** Express $K_f$ and $\Delta E_{\mathrm{th}}$ as fractions of $K_0$.

**F.** Explain why angular momentum is conserved while mechanical energy is not.

## 2. The Equations

- Angular-momentum conservation:

  $$
  I_0\omega_0=I_f\omega_f.
  $$

  Negligible external torque preserves angular momentum about the axle.

- Rotational kinetic energy:

  $$
  K=\frac12I\omega^2.
  $$

- Energy converted internally:

  $$
  \Delta E_{\mathrm{th}}=K_0-K_f.
  $$

  Sticking is a completely inelastic process, so mechanical energy need not be conserved.

## 3. The Walkthrough

1. First find the final angular speed:

   $$
   \left(\frac12md^2\right)\omega_0
   =
   (md^2)\omega_f,
   \qquad
   \omega_f=\frac{\omega_0}{2}.
   $$

2. The initial rotational kinetic energy is

   $$
   K_0
   =
   \frac12I_0\omega_0^2
   =
   \frac12\left(\frac12md^2\right)\omega_0^2
   =
   \frac14md^2\omega_0^2.
   $$

3. The final kinetic energy is

   $$
   K_f
   =
   \frac12I_f\omega_f^2
   =
   \frac12(md^2)\left(\frac{\omega_0}{2}\right)^2
   =
   \frac18md^2\omega_0^2.
   $$

4. Subtract:

   $$
   \Delta E_{\mathrm{th}}
   =
   \frac14md^2\omega_0^2
   -
   \frac18md^2\omega_0^2
   =
   \frac18md^2\omega_0^2.
   $$

5. Compare with $K_0$:

   $$
   K_f=\frac12K_0,
   \qquad
   \Delta E_{\mathrm{th}}=\frac12K_0.
   $$

6. Angular momentum remains constant because the net external torque is negligible. Mechanical energy decreases because the rain sticks, and the relative motion is converted into thermal energy, deformation, and sound.
