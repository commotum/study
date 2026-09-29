# Arrangement of Identical Blocks

Source: [[212/M2/2026-07-07-M2-1/Source/Lecture-Notes#Example 2: Arrangement of Identical Blocks|Lecture example]]

## 1. The Problem

Ten identical blocks, each of mass $m$, are arranged in three groups along the $x$-axis. The groups may be represented by their total masses at their own center positions:

- six blocks centered at $x=1.5\ \mathrm{cm}$,
- two blocks centered at $x=4.0\ \mathrm{cm}$,
- two blocks centered at $x=5.5\ \mathrm{cm}$.

**A.** Replace each group by an equivalent point mass and list the three mass-position pairs.

**B.** Write the center-of-mass expression for all ten blocks without expanding the arithmetic.

**C.** Calculate $x_{\mathrm{cm}}$ and report the result in centimeters.

**D.** Explain why averaging the three listed positions would be incorrect.

**E.** Check that the result lies within the occupied interval and is pulled toward the largest group.

## 2. The Equations

- Center of mass of grouped discrete objects:

  $$
  x_{\mathrm{cm}}
  =\frac{\sum_j M_jx_j}{\sum_j M_j}.
  $$

  A group can be replaced by its total mass $M_j$ located at that group’s own center of mass.

- Group mass for identical blocks:

  $$
  M_j=N_jm.
  $$

  The number of blocks supplies the weight assigned to each group position.

- Bounds check:

  $$
  x_{\min}\le x_{\mathrm{cm}}\le x_{\max}.
  $$

  A positive collection of masses cannot have its center of mass outside the span of its positions.

## 3. The Walkthrough

1. Replace the groups by the point masses

   $$
   6m\text{ at }1.5\ \mathrm{cm},\qquad
   2m\text{ at }4.0\ \mathrm{cm},\qquad
   2m\text{ at }5.5\ \mathrm{cm}.
   $$

2. Form the weighted average:

   $$
   x_{\mathrm{cm}}
   =
   \frac{6m(1.5)+2m(4.0)+2m(5.5)}{6m+2m+2m}.
   $$

3. Cancel the common block mass $m$:

   $$
   x_{\mathrm{cm}}=\frac{9+8+11}{10}\ \mathrm{cm}.
   $$

4. Evaluate:

   $$
   x_{\mathrm{cm}}=2.8\ \mathrm{cm}.
   $$

5. A plain average of $1.5$, $4.0$, and $5.5$ would give equal influence to unequal groups. The group at $1.5\ \mathrm{cm}$ contains three times as many blocks as either other group.

6. The result lies between $1.5\ \mathrm{cm}$ and $5.5\ \mathrm{cm}$ and is closer to the six-block group, so it passes the physical check.
