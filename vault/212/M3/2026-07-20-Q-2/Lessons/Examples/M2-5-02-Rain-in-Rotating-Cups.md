# Rain Falling into Rotating Cups

Source: [[212/M2/2026-07-14-M2-5/Source/Lecture-Notes#Rain Falling into Rotating Cups|Lecture example]]

## 1. The Problem

Two identical cups rotate about a vertical central axis. Initially, each cup has mass $m$, the centers of the cups are separated by distance $d$, and the system rotates at angular speed $\omega_0$. Rain falls vertically into both cups and doubles the mass of each cup. Treat each cup and its collected rain as a point mass at radius $d/2$. The incoming rain has no initial angular momentum about the vertical axis, and external torque about that axis is negligible.

**A.** Explain why angular momentum about the central axis is conserved.

**B.** Calculate the initial moment of inertia.

**C.** Calculate the final moment of inertia.

**D.** Solve symbolically for the final angular speed $\omega_f$.

**E.** Evaluate the result for $\omega_0=4.2\text{ rad/s}$.

**F.** Check the units and explain the result covariationally.

## 2. The Equations

- Point-mass moment of inertia:

  $$
  I=\sum_i m_ir_i^2.
  $$

- Angular momentum of a rigid rotating system:

  $$
  L=I\omega.
  $$

- Conservation condition:

  $$
  \sum\tau_{\mathrm{ext}}=0
  \quad\Longrightarrow\quad
  L_0=L_f.
  $$

  Conservation is tested about the chosen axis.

## 3. The Walkthrough

1. About the vertical axle, external torque is negligible. The vertically falling rain arrives with no tangential momentum and hence no initial angular momentum about that axis. Therefore,

   $$
   I_0\omega_0=I_f\omega_f.
   $$

2. Initially, each cup has mass $m$ at radius $d/2$:

   $$
   I_0
   =
   m\left(\frac d2\right)^2
   +
   m\left(\frac d2\right)^2
   =
   \frac12md^2.
   $$

3. Finally, each cup-plus-rain mass is $2m$:

   $$
   I_f
   =
   2m\left(\frac d2\right)^2
   +
   2m\left(\frac d2\right)^2
   =
   md^2.
   $$

4. Apply conservation:

   $$
   \left(\frac12md^2\right)\omega_0
   =
   (md^2)\omega_f.
   $$

5. Cancel $m$ and $d^2$:

   $$
   \omega_f=\frac{\omega_0}{2}.
   $$

6. For $\omega_0=4.2\text{ rad/s}$:

   $$
   \omega_f=2.1\text{ rad/s}.
   $$

7. The units remain angular speed. Doubling the rotating mass at the same radius doubles $I$, so conservation of $I\omega$ requires $\omega$ to be halved.
