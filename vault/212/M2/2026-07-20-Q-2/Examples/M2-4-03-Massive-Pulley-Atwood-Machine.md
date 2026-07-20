# Atwood Machine with a Massive Pulley

Source: [[212/M2/2026-07-13-M2-4/Source/Lecture-Notes#Example 3: Atwood Machine with a Massive Pulley|Lecture example]]

## 1. The Problem

Two masses $m_1<m_2$ are connected by a light string passing over a solid-disk pulley of mass $M_p$ and radius $r$. The string does not slip. Mass $m_2$ accelerates downward while $m_1$ accelerates upward with common magnitude $a$.

**A.** Draw a free-body diagram for each hanging mass and an extended free-body diagram for the pulley.

**B.** Write one translational equation for each mass using positive directions along their motions.

**C.** Explain why the two string tensions must be labeled $T_1$ and $T_2$ rather than treated as equal.

**D.** Write the pulley torque equation and the no-slip relation.

**E.** Eliminate $T_1$, $T_2$, and $\alpha$ to solve symbolically for $a$.

**F.** Check the units, the direction of acceleration, and the massless-pulley limit.

**G.** Predict how increasing $M_p$ changes the acceleration.

## 2. The Equations

- Translational Newton’s second law:

  $$
  \sum F=ma.
  $$

- Rotational Newton’s second law:

  $$
  \sum\tau=I\alpha.
  $$

- Solid-disk pulley:

  $$
  I=\frac12M_pr^2.
  $$

- No-slip constraint:

  $$
  a=\alpha r.
  $$

  The string’s tangential acceleration matches the pulley rim’s tangential acceleration.

## 3. The Walkthrough

1. For $m_1$, choose upward as positive:

   $$
   T_1-m_1g=m_1a,
   \qquad
   T_1=m_1g+m_1a.
   $$

2. For $m_2$, choose downward as positive:

   $$
   m_2g-T_2=m_2a,
   \qquad
   T_2=m_2g-m_2a.
   $$

3. The tension difference must accelerate the pulley rotationally:

   $$
   (T_2-T_1)r=I\alpha.
   $$

   Equal tensions would give zero net pulley torque.

4. Substitute $I=\frac12M_pr^2$ and $\alpha=a/r$:

   $$
   (T_2-T_1)r
   =
   \left(\frac12M_pr^2\right)\frac{a}{r}.
   $$

   Cancel $r$:

   $$
   T_2-T_1=\frac12M_pa.
   $$

5. Substitute the two tension expressions:

   $$
   (m_2g-m_2a)-(m_1g+m_1a)=\frac12M_pa.
   $$

6. Collect terms:

   $$
   (m_2-m_1)g
   =
   \left(m_1+m_2+\frac{M_p}{2}\right)a.
   $$

7. Solve:

   $$
   a=
   \frac{(m_2-m_1)g}
        {m_1+m_2+M_p/2}.
   $$

8. The mass factors cancel to leave units of acceleration. Because $m_2>m_1$, the numerator is positive in the assumed direction.

9. If $M_p\to0$,

   $$
   a\to\frac{(m_2-m_1)g}{m_1+m_2},
   $$

   the massless-pulley result. Increasing $M_p$ enlarges the denominator and reduces $a$.
