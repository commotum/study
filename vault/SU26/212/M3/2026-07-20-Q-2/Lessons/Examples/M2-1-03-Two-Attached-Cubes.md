# Two Attached Cubes: Composite Center of Mass

Source: [[212/M2/2026-07-07-M2-1/Source/Lecture-Notes#Example 3: Two Attached Cubes|Lecture example]]

## 1. The Problem

A solid cube of side length $2L$ is attached face-to-face to a solid cube of side length $L$. Both cubes have the same uniform volume mass density $\rho$. Place the origin at the left face of the larger cube, with the smaller cube attached to its right face.

**A.** Find the mass of each cube symbolically in terms of $\rho$ and $L$.

**B.** Determine the $x$-coordinate of each cube’s individual center of mass.

**C.** Treat the two cubes as point masses at their centers and solve symbolically for the composite $x_{\mathrm{cm}}$.

**D.** Show which factors cancel and state whether the answer depends on $\rho$.

**E.** Check that the result lies between $L$ and $2L$ and explain why it must be to the right of $L$.

## 2. The Equations

- Mass from volume density:

  $$
  m=\rho V.
  $$

  Equal density does not imply equal mass when the volumes differ.

- Cube volume:

  $$
  V=s^3.
  $$

  Doubling the side length multiplies the volume and mass by $2^3=8$.

- Composite center of mass:

  $$
  x_{\mathrm{cm}}
  =\frac{m_1x_1+m_2x_2}{m_1+m_2}.
  $$

  Each uniform cube can be represented by its full mass at its geometric center.

## 3. The Walkthrough

1. Compute the large cube’s volume and mass:

   $$
   V_1=(2L)^3=8L^3,
   \qquad
   m_1=8\rho L^3.
   $$

2. Compute the small cube’s volume and mass:

   $$
   V_2=L^3,
   \qquad
   m_2=\rho L^3.
   $$

3. Locate the individual centers. The large cube spans $0\le x\le2L$, so

   $$
   x_1=L.
   $$

   The small cube spans $2L\le x\le3L$, so

   $$
   x_2=2L+\frac{L}{2}=\frac{5L}{2}.
   $$

4. Substitute into the composite center-of-mass expression:

   $$
   x_{\mathrm{cm}}
   =
   \frac{(8\rho L^3)(L)+(\rho L^3)(5L/2)}
        {8\rho L^3+\rho L^3}.
   $$

5. Cancel $\rho L^3$ and combine terms:

   $$
   x_{\mathrm{cm}}
   =\frac{8L+5L/2}{9}
   =\frac{21L/2}{9}
   =\frac{7L}{6}.
   $$

6. Density cancels because both cubes have the same $\rho$. The result satisfies

   $$
   L<\frac{7L}{6}<2L.
   $$

   It lies just to the right of the large cube’s center because the smaller cube adds mass on that side, while the large cube still contains eight times as much mass.
