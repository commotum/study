# Two Point Masses: Center of Mass and Torque Balance

Source: [[212/M2/2026-07-07-M2-1/Source/Lecture-Notes#Example 1: Two Point Masses|Lecture example]]

## 1. The Problem

Two point masses lie on the $x$-axis and are separated by a distance $L$. Place the origin at the first mass, so that

$$
x_1=0,\qquad x_2=L.
$$

The masses satisfy $m_1=3m_2$.

**A.** Draw and label the one-dimensional coordinate system, including both masses and their positions.

**B.** Starting from the discrete center-of-mass definition, solve symbolically for $x_{\mathrm{cm}}$ in terms of $L$.

**C.** Evaluate the result for $L=0.88\text{ m}$ and include units.

**D.** Treat $x_{\mathrm{cm}}$ as the location of a support. Write the torque-balance equation about that support and independently recover the symbolic result.

**E.** Check that the answer has the correct units and lies closer to the larger mass.

## 2. The Equations

- Discrete center of mass:

  $$
  x_{\mathrm{cm}}=\frac{\sum_i m_ix_i}{\sum_i m_i}.
  $$

  Each position is weighted by its mass.

- Static torque balance about a support:

  $$
  \sum\tau=0.
  $$

  At the balancing point, the clockwise and counterclockwise torques from the two weights have equal magnitudes.

- Torque magnitude from a perpendicular force:

  $$
  \tau=rF.
  $$

  Each weight is perpendicular to its horizontal lever arm.

- Weight:

  $$
  F_g=mg.
  $$

  The factor $g$ cancels when both torques are gravitational.

## 3. The Walkthrough

1. Use $x_1=0$, $x_2=L$, and $m_1=3m_2$:

   $$
   x_{\mathrm{cm}}
   =\frac{m_1(0)+m_2L}{m_1+m_2}
   =\frac{m_2L}{3m_2+m_2}.
   $$

2. Cancel the common mass:

   $$
   x_{\mathrm{cm}}=\frac{L}{4}.
   $$

3. Substitute $L=0.88\text{ m}$:

   $$
   x_{\mathrm{cm}}=\frac{0.88\text{ m}}{4}=0.22\text{ m}.
   $$

4. Verify by torque balance. If the support is at $x_{\mathrm{cm}}$, the lever arms are $x_{\mathrm{cm}}$ and $L-x_{\mathrm{cm}}$:

   $$
   m_1g\,x_{\mathrm{cm}}
   =m_2g(L-x_{\mathrm{cm}}).
   $$

5. Cancel $g$, collect the center-of-mass terms, and solve:

   $$
   (m_1+m_2)x_{\mathrm{cm}}=m_2L,
   \qquad
   x_{\mathrm{cm}}=\frac{m_2L}{m_1+m_2}=\frac{L}{4}.
   $$

6. The result has units of length. Since $L/4<L/2$, it lies closer to the larger mass at the origin, as expected.
