# Problem 3 Lesson: Units of a Coefficient in Angular Acceleration

## Core Move

Determine the units of an unknown coefficient by requiring every term in an equation to have the same units as the quantity on the left, then divide out the units contributed by variables like time.

## When to Use This

Use this move when a formula contains a constant with unknown units, especially when the constant multiplies a variable with known units.

The key cue is a sum like

$$
\alpha_z(t)=Bt^2+C.
$$

Since terms are being added, $Bt^2$, $C$, and $\alpha_z(t)$ must all have the same units.

## Target Problem

The $z$-component of angular acceleration is

$$
\alpha_z(t)=Bt^2+C.
$$

What SI units is $B$ measured in?

## Step 1: Match Terms To The Left Side

Angular acceleration has units of radians per second squared:

$$
[\alpha_z]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Because $Bt^2$ and $C$ are added to make $\alpha_z(t)$, each term must also have units of angular acceleration:

$$
[Bt^2]=\frac{\mathrm{rad}}{\mathrm{s}^2}
$$

and

$$
[C]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

### Worked Example

Suppose

$$
a(t)=Kt+a_0,
$$

where $a(t)$ is linear acceleration. Find the units of $K$.

Since $a(t)$ has units $\mathrm{m}/\mathrm{s}^2$, the term $Kt$ must also have units $\mathrm{m}/\mathrm{s}^2$:

$$
[Kt]=\frac{\mathrm{m}}{\mathrm{s}^2}.
$$

Since $[t]=\mathrm{s}$,

$$
[K]\mathrm{s}=\frac{\mathrm{m}}{\mathrm{s}^2}.
$$

Divide by $\mathrm{s}$:

$$
[K]=\frac{\mathrm{m}}{\mathrm{s}^3}.
$$

### Try It

If

$$
v(t)=At+v_0,
$$

and $v(t)$ has units $\mathrm{m}/\mathrm{s}$, what are the units of $A$?

**Answer check:** $[At]=\mathrm{m}/\mathrm{s}$, so $[A]\mathrm{s}=\mathrm{m}/\mathrm{s}$ and $[A]=\mathrm{m}/\mathrm{s}^2$.

## Step 2: Divide Out The Time Power

In the target problem,

$$
[Bt^2]=[\alpha_z].
$$

Now substitute the units:

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

Divide by $\mathrm{s}^2$:

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

So $B$ is measured in

$$
\boxed{\mathrm{rad}/\mathrm{s}^4}.
$$

### Worked Example

Suppose

$$
\omega(t)=Dt^3+\omega_0,
$$

where $\omega(t)$ is angular velocity. Find the units of $D$.

Angular velocity has units $\mathrm{rad}/\mathrm{s}$, so

$$
[Dt^3]=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Since $[t^3]=\mathrm{s}^3$,

$$
[D]\mathrm{s}^3=\frac{\mathrm{rad}}{\mathrm{s}}.
$$

Divide by $\mathrm{s}^3$:

$$
[D]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

### Try It

If

$$
\theta(t)=Et^2+\theta_0,
$$

and $\theta(t)$ has units $\mathrm{rad}$, what are the units of $E$?

**Answer check:** $[Et^2]=\mathrm{rad}$, so $[E]\mathrm{s}^2=\mathrm{rad}$ and $[E]=\mathrm{rad}/\mathrm{s}^2$.

## Step 3: Avoid The Common Traps

### Trap 1: Using meters for angular quantities

Angular acceleration is not linear acceleration. Linear acceleration uses $\mathrm{m}/\mathrm{s}^2$, but angular acceleration uses $\mathrm{rad}/\mathrm{s}^2$.

In this problem, the symbol $\alpha_z$ tells you it is angular acceleration, so the numerator should be $\mathrm{rad}$, not $\mathrm{m}$.

### Trap 2: Forgetting the $t^2$

The coefficient $B$ is not itself angular acceleration. The whole product $Bt^2$ has units of angular acceleration.

That means $B$ must carry two extra powers of $1/\mathrm{s}$:

$$
[B]=\frac{[\alpha_z]}{[t^2]}
=\frac{\mathrm{rad}/\mathrm{s}^2}{\mathrm{s}^2}
=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

### Trap 3: Finding the units of $C$ instead

The constant $C$ is added directly to $Bt^2$, so $C$ has the same units as $\alpha_z$:

$$
[C]=\frac{\mathrm{rad}}{\mathrm{s}^2}.
$$

But the question asks for $B$, and $B$ multiplies $t^2$, so $B$ has units $\mathrm{rad}/\mathrm{s}^4$.

## Mastery Check

1. If $x(t)=At^2+x_0$ and $x(t)$ is measured in $\mathrm{m}$, what are the units of $A$?

2. If $v(t)=Bt^3+v_0$ and $v(t)$ is measured in $\mathrm{m}/\mathrm{s}$, what are the units of $B$?

3. If $\omega(t)=Ct^2+\omega_0$ and $\omega(t)$ is measured in $\mathrm{rad}/\mathrm{s}$, what are the units of $C$?

4. If $\alpha(t)=Dt+\alpha_0$ and $\alpha(t)$ is measured in $\mathrm{rad}/\mathrm{s}^2$, what are the units of $D$?

5. If $\alpha_z(t)=Et^4+F$ and $\alpha_z(t)$ is measured in $\mathrm{rad}/\mathrm{s}^2$, what are the units of $E$?

### Mastery Check Answers

1. $\mathrm{m}/\mathrm{s}^2$
2. $\mathrm{m}/\mathrm{s}^4$
3. $\mathrm{rad}/\mathrm{s}^3$
4. $\mathrm{rad}/\mathrm{s}^3$
5. $\mathrm{rad}/\mathrm{s}^6$

## Summary

When a formula adds terms, every term must have the same units.

For

$$
\alpha_z(t)=Bt^2+C,
$$

the left side has units $\mathrm{rad}/\mathrm{s}^2$. Therefore

$$
[B]\mathrm{s}^2=\frac{\mathrm{rad}}{\mathrm{s}^2},
$$

so

$$
[B]=\frac{\mathrm{rad}}{\mathrm{s}^4}.
$$

The answer is $\boxed{\mathrm{rad}/\mathrm{s}^4}$.
