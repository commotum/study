# Quiz 2 General Form

Each section stands alone. See [[212/M2/2026-07-20-Q-2/Variables|Variables]] for symbol definitions.

## 1. Center of Mass and Density

Use when finding where discrete pieces or a continuous object balance.
$$
\begin{aligned}
M&=\sum_i m_i,\\
\vec r_{\mathrm{cm}}&=\frac{\sum_i m_i\vec r_i}{M},\\
x_{\mathrm{cm}}&=\frac{\sum_i m_ix_i}{M}
\end{aligned}
$$
$$
M=\int dm
\qquad
dm=\lambda\,dx=\sigma\,dA=\rho\,dV
$$
$$
\vec r_{\mathrm{cm}}=\frac1M\int\vec r\,dm
$$
1. Choose one origin and measure every position from it.
2. Replace each uniform piece or group by its mass at its own center.
3. For a distribution, build $dm$, use $M=\int dm$ to normalize any unknown density constant, then evaluate the center-of-mass integral.
4. Check that the answer lies toward the greater concentration of mass and balances the torques.

**Trap:** Do not average positions without weighting them by mass.

## 2. Moment of Inertia

Use when finding rotational resistance, changing axes, combining pieces, removing a hole, or calculating rotational energy.
$$
I=\sum_i m_ir_i^2=\int r^2\,dm
\qquad
I_{\mathrm{total}}=\sum_i I_i
$$
$$
I=I_{\mathrm{cm}}+Md^2
\qquad
I_{\mathrm{rem}}=I_{\mathrm{full}}-I_{\mathrm{hole}}
$$
$$
\begin{aligned}
I_{\mathrm{point}}=I_{\mathrm{hoop}}&=MR^2,\\
I_{\mathrm{disk}}=I_{\mathrm{solid\ cyl}}&=\frac12MR^2,\\
I_{\mathrm{solid\ sphere}}&=\frac25MR^2,\\
I_{\mathrm{shell}}&=\frac23MR^2,\\
I_{\mathrm{rod,cm}}&=\frac1{12}ML^2,\\
I_{\mathrm{rod,end}}&=\frac13ML^2
\end{aligned}
$$
$$
K_{\mathrm{rot}}=\frac12I\omega^2
$$
1. Name the rotation axis and measure every perpendicular distance from it.
2. Use a sum or integral, or shift a center-of-mass result with the parallel-axis theorem.
3. Put every component about the same axis before adding or subtracting.
4. Check for units of $\mathrm{kg\,m^2}$ and confirm that moving mass outward increases $I$.

**Trap:** A memorized shape formula is correct only for its stated axis.

## 3. Torque and Rotational Dynamics

Use when a force turns an object or when angular acceleration is requested.
$$
\vec\tau=\vec r\times\vec F
\qquad
|\tau|=rF\sin\phi=Fd_\perp
$$
$$
\sum\tau=I\alpha
$$
1. Choose the axis and draw where every force acts.
2. Find each perpendicular moment arm and assign a clockwise/counterclockwise sign.
3. Drop forces whose lines of action pass through the axis.
4. Add torques, build $I$ about the same axis, and solve $\sum\tau=I\alpha$.
5. Check that increasing torque increases $|\alpha|$ while increasing $I$ decreases it.

**Trap:** Use the angle between $\vec r$ and $\vec F$, not merely the angle labeled in the diagram.

## 4. Static Equilibrium and Massive Pulleys

Use the first form for objects at rest, impending tipping, or impending slipping.
$$
\sum\vec F=0
\qquad
\sum\tau=0
$$
$$
f_{s,\max}=\mu_sN
\qquad
N_{\mathrm{unused}}=0\ \text{at tipping}
$$
$$
mgx_{\max}=Mg\,d_{\mathrm{cm}}
\qquad
\mu_{s,\mathrm{ladder}}=\frac1{2\tan\theta}
$$
1. Draw an extended free-body diagram.
2. Choose a pivot that removes the most unknown forces.
3. At impending tip, set the lost support force to zero.
4. At impending slip, use $f_s=\mu_sN$.

Use the second form when translating masses drive a pulley with rotational inertia.
$$
T_1-m_1g=m_1a
\qquad
m_2g-T_2=m_2a
$$
$$
(T_2-T_1)r=I\alpha
\qquad
a=\alpha r
$$
$$
a=
\frac{(m_2-m_1)g}
{m_1+m_2+I/r^2}
$$
1. Draw a separate free-body diagram for each mass and keep $T_1$ and $T_2$ distinct.
2. Write both force equations, the pulley torque equation, and the no-slip relation.
3. Eliminate the tensions and $\alpha$, then solve for $a$.
4. Check that $I\to0$ gives the massless-pulley result and that increasing $I$ reduces $a$.

**Trap:** Static systems need both force and torque balance; massive-pulley systems need both translation and rotation equations.

## 5. Rolling Motion and Angular Momentum

Use the rolling form when an object rolls without slipping.
$$
v_{\mathrm{cm}}=\omega R
\qquad
a_{\mathrm{cm}}=\alpha R
$$
$$
K_{\mathrm{rolling}}
=
\frac12Mv_{\mathrm{cm}}^2+\frac12I_{\mathrm{cm}}\omega^2
$$
$$
v=\sqrt{\frac{2gh}{1+I/(MR^2)}}
\qquad
a_{\mathrm{ramp}}=\frac{g\sin\theta}{1+I/(MR^2)}
$$
1. Verify no slipping, then connect translation and rotation.
2. Include both translational and rotational kinetic energy.
3. Insert the correct $I$ and use $I/(MR^2)$ to compare shapes.

Use the angular-momentum form when external torque about the chosen axis is zero or negligible.
$$
\vec L=\vec r\times m\vec v
\qquad
L_{\mathrm{rigid}}=I\omega
$$
$$
\sum\vec\tau_{\mathrm{ext}}=\frac{d\vec L}{dt}
\qquad
\sum\vec\tau_{\mathrm{ext}}=0
\Rightarrow
\vec L_i=\vec L_f
$$
$$
I_i\omega_i+(\vec r\times m\vec v)_i=I_f\omega_f
$$
1. Define the system and axis, then test the external torque about that axis.
2. Write every initial and final angular-momentum contribution about the same axis.
3. If something sticks, add it to $I_f$ and conserve angular momentum—not kinetic energy.

**Trap:** No-slip relations fail during sliding, and $K_i\ne K_f$ for a sticking collision.
