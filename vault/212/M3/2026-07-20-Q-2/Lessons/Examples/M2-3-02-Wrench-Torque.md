# Wrench Example: Torque Magnitude and Direction

Source: [[212/M2/2026-07-09-M2-3/Source/Lecture-Notes#Wrench Example|Lecture example]]

## 1. The Problem

A force of magnitude $120\text{ N}$ is applied to a wrench at a point $52\text{ cm}$ from the pivot. The diagram labels an angle $\phi=33^\circ$ between the force and a line perpendicular to the wrench. The position vector $\vec r$ lies along the wrench.

**A.** Convert the lever length to meters.

**B.** Determine the angle $\theta$ between $\vec r$ and $\vec F$.

**C.** Calculate the torque magnitude about the pivot.

**D.** Use the right-hand rule to determine whether the torque points into or out of the page for the orientation shown in the lecture.

**E.** Check the units explicitly and explain why the labeled $33^\circ$ is not inserted directly into $\sin\theta$.

## 2. The Equations

- Torque magnitude:

  $$
  \tau=rF\sin\theta.
  $$

  The angle must be the angle between the position vector and force vector.

- Complementary-angle geometry:

  $$
  \theta=90^\circ-\phi.
  $$

  This converts the diagram’s labeled angle into the angle required by the cross product.

- Torque direction:

  $$
  \vec\tau=\vec r\times\vec F.
  $$

  The right-hand rule chooses the direction perpendicular to the page.

- Torque units:

  $$
  [\tau]=(\text{m})(\text{N})=\text{N}\cdot\text{m}.
  $$

## 3. The Walkthrough

1. Convert the distance:

   $$
   r=52\text{ cm}=0.52\text{ m}.
   $$

2. Find the angle between $\vec r$ and $\vec F$:

   $$
   \theta=90^\circ-33^\circ=57^\circ.
   $$

3. Substitute into the torque formula:

   $$
   \tau=(0.52\text{ m})(120\text{ N})\sin57^\circ.
   $$

4. Evaluate:

   $$
   \tau\approx52\text{ N}\cdot\text{m}.
   $$

5. Apply the right-hand rule to $\vec r\times\vec F$ in the lecture orientation. Curling from $\vec r$ toward $\vec F$ points the thumb into the page, denoted by $\otimes$.

6. The units are $\text{N}\cdot\text{m}$. Using $33^\circ$ directly would select the wrong force component; the cross product requires the angle between the two vectors themselves.
