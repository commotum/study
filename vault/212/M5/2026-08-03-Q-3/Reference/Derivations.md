# Reusable Derivations for Quiz 3

This file expands the solved endpoints into reusable symbolic methods. Each derivation begins with the governing model, keeps the variables general, and then recovers the course example as a special case.

The boxed expressions are destinations, not substitutes for checking the geometry and assumptions. In particular:

- measure every pendulum distance from the actual pivot;
- distinguish wave-propagation speed from the transverse speed of the medium;
- use signed velocities during collisions and Doppler shifts;
- distinguish a formula that follows from geometry from one that is universally true.

# Lecture-derived families

## 1. Uniform rod about an arbitrary pivot

### Physical-pendulum backbone

For a rigid assembly of total mass \(M\), let \(\ell\) be the distance from the pivot to the combined center of mass and let \(I_P\) be the total moment of inertia about the pivot. For a small angular displacement,

$$
\tau_P=-Mg\ell\sin\theta\simeq-Mg\ell\theta.
$$

Using \(\tau_P=I_P\ddot\theta\),

$$
I_P\ddot\theta=-Mg\ell\theta
\quad\Longrightarrow\quad
\ddot\theta+\frac{Mg\ell}{I_P}\theta=0.
$$

This has the SHM form \(\ddot\theta+\omega^2\theta=0\), so

$$
\omega=\sqrt{\frac{Mg\ell}{I_P}},
\qquad
\boxed{T=2\pi\sqrt{\frac{I_P}{Mg\ell}}}.
$$

This model assumes a rigid object, a fixed pivot, small oscillations, and a stable equilibrium with the center of mass below the pivot.

### Apply it to a uniform rod

Let a uniform rod have mass \(M\), length \(L\), and a pivot a distance \(a\) from one end. Its center of mass is at \(L/2\), so

$$
\ell=\left|\frac L2-a\right|.
$$

Begin with the center-of-mass inertia and shift it to the pivot:

$$
I_{\mathrm{CM}}=\frac1{12}ML^2,
$$

$$
I_P=I_{\mathrm{CM}}+M\ell^2
=M\left(\frac{L^2}{12}+\ell^2\right).
$$

Substitution into the physical-pendulum formula gives

$$
\boxed{
T_{\mathrm{rod}}
=2\pi\sqrt{\frac{L^2/12+\ell^2}{g\ell}}
},
\qquad
\ell=\left|\frac L2-a\right|.
$$

For an end pivot, \(a=0\) and \(\ell=L/2\):

$$
T_{\mathrm{rod,end}}
=2\pi\sqrt{\frac{L^2/12+L^2/4}{gL/2}}
=\boxed{2\pi\sqrt{\frac{2L}{3g}}}.
$$

For a pivot \(L/6\) from an end, \(\ell=L/3\):

$$
I_P=M\left(\frac{L^2}{12}+\frac{L^2}{9}\right)
=\frac7{36}ML^2,
$$

$$
T_{\mathrm{rod},\,a=L/6}
=2\pi\sqrt{\frac{(7/36)ML^2}{Mg(L/3)}}
=\boxed{2\pi\sqrt{\frac{7L}{12g}}}.
$$

The mass cancels, but the mass distribution does not. If \(a=L/2\), then \(\ell=0\); gravity supplies no first-order restoring torque, so this pendulum formula is not applicable.

## 2. Rod with an attached point mass

For multiple rigidly connected components, it is often shorter to avoid explicitly calculating the combined center of mass. When every component center lies on the same ray below the pivot,

$$
I_P=\sum_i I_{i,P},
\qquad
M\ell=\sum_i m_id_i,
$$

so

$$
\boxed{
T=2\pi\sqrt{\frac{\sum_i I_{i,P}}{g\sum_i m_id_i}}
}.
$$

Let a uniform rod of mass \(M_r\) and length \(L\) pivot about one end. Attach a point mass \(M_p\) at distance \(d\) from the pivot.

The inertia contributions are

$$
I_r=\frac13M_rL^2,
\qquad
I_p=M_pd^2.
$$

The gravitational first moment is

$$
M\ell=M_r\frac L2+M_pd.
$$

Therefore,

$$
\boxed{
T_{\mathrm{rod+point}}
=2\pi\sqrt{
\frac{\frac13M_rL^2+M_pd^2}
{g(M_rL/2+M_pd)}
}
}.
$$

For a point mass at the rod tip, \(d=L\):

$$
T
=2\pi\sqrt{
\frac{\frac13M_rL^2+M_pL^2}
{g(M_rL/2+M_pL)}
}
=\boxed{
2\pi\sqrt{\frac{2L(M_r+3M_p)}{3g(M_r+2M_p)}}
}.
$$

Useful limit checks are

$$
M_p\to0
\Rightarrow
T\to2\pi\sqrt{\frac{2L}{3g}},
$$

$$
M_r\to0
\Rightarrow
T\to2\pi\sqrt{\frac dg}.
$$

The second limit is a point-mass pendulum of length \(d\), not automatically \(L\).

## 3. Rod with an attached extended body

An extended attachment contributes two inertia terms:

$$
I_{b,P}=I_{b,\mathrm{CM}}+M_bd_b^2.
$$

The first term describes rotation about the body’s own center. The second describes motion of that center around the assembly pivot.

For an end-pivoted uniform rod plus a rigidly attached body,

$$
I_P=\frac13M_rL^2+I_{b,\mathrm{CM}}+M_bd_b^2,
$$

$$
M\ell=M_r\frac L2+M_bd_b.
$$

Thus,

$$
\boxed{
T_{\mathrm{rod+body}}
=2\pi\sqrt{
\frac{\frac13M_rL^2+I_{b,\mathrm{CM}}+M_bd_b^2}
{g(M_rL/2+M_bd_b)}
}
}.
$$

If a solid disk of radius \(R\) is attached end-to-end, with its center on the rod’s axis one radius below the rod tip,

$$
d_b=L+R,
\qquad
I_{b,\mathrm{CM}}=\frac12M_bR^2.
$$

Therefore,

$$
\boxed{
T_{\mathrm{rod+disk}}
=2\pi\sqrt{
\frac{
\frac13M_rL^2+\frac12M_bR^2+M_b(L+R)^2
}{
g[M_rL/2+M_b(L+R)]
}
}
}.
$$

To adapt this result, replace only \(d_b\) and \(I_{b,\mathrm{CM}}\):

$$
I_{b,\mathrm{CM}}=
\begin{cases}
\frac12M_bR^2,&\text{solid disk about its symmetry axis},\\[2pt]
\frac25M_bR^2,&\text{solid sphere}.
\end{cases}
$$

Do not use \(d_b=L+R\) unless the body center lies on the rod axis one radius beyond its lower end. Do not omit \(I_{b,\mathrm{CM}}\) for a rigidly attached extended body. A freely spinning attachment requires a different kinetic-energy model.

## 4. Hanging load, wave speed, and particle speed

Let a hanging mass \(m_h\) supply tension to a uniform wire of vibrating length \(L_w\) and mass \(m_w\).

Taking downward as positive for the hanging mass,

$$
m_hg-F_T=m_ha_h
\quad\Longrightarrow\quad
F_T=m_h(g-a_h).
$$

For a stationary mass or one moving at constant velocity,

$$
a_h=0
\quad\Longrightarrow\quad
F_T=m_hg.
$$

The wire’s linear density and propagation speed are

$$
\mu=\frac{m_w}{L_w},
\qquad
v_w=\sqrt{\frac{F_T}{\mu}}.
$$

Hence,

$$
\boxed{
v_w=\sqrt{\frac{m_h(g-a_h)L_w}{m_w}}
}.
$$

The static-load special case is

$$
\boxed{
v_w=\sqrt{\frac{m_hgL_w}{m_w}}
}.
$$

This is the speed of the wave pattern. The transverse velocity of one wire element comes from differentiating the wave:

$$
y(x,t)=A\sin(kx-\omega t+\phi_0),
$$

$$
v_y=\frac{\partial y}{\partial t}
=-\omega A\cos(kx-\omega t+\phi_0).
$$

Therefore,

$$
|v_y|_{\max}=A\omega.
$$

Using \(f=v_w/\lambda\) and \(\omega=2\pi f\),

$$
\boxed{
|v_y|_{\max}
=\frac{2\pi A}{\lambda}v_w
=\frac{2\pi A}{\lambda}
\sqrt{\frac{m_h(g-a_h)L_w}{m_w}}
}.
$$

If the pulley is nonideal or tension varies along the wire, calculate the tension in the vibrating span before using \(v_w=\sqrt{F_T/\mu}\).

The value \(\sqrt{F_T/\mu}\) is the propagation speed relative to the wire material. It is also the laboratory speed when the vibrating span is stationary. If the wire itself translates through a pulley, combine the relative wave speed with the material velocity using the appropriate propagation direction.

## 5. Circular wavefront geometry

A point source produces spherical wavefronts; a two-dimensional cross-section is a circle centered on the source.

For a general source \(S=(x_s,y_s)\), two points \(P_1=(x_1,y_1)\) and \(P_2=(x_2,y_2)\) on the same wavefront satisfy

$$
(x_s-x_1)^2+(y_s-y_1)^2
=(x_s-x_2)^2+(y_s-y_2)^2.
$$

Expanding and canceling the common quadratic terms gives the perpendicular-bisector equation

$$
\boxed{
2x_s(x_2-x_1)+2y_s(y_2-y_1)
=x_2^2+y_2^2-x_1^2-y_1^2
}.
$$

Two equal-distance observations determine a line of possible sources. A further constraint determines the actual source.

For the common special case

$$
S=(x_s,0),
\qquad
P_1=(x_1,0),
\qquad
P_2=(x_2,0),
$$

the source is the midpoint:

$$
\boxed{x_s=\frac{x_1+x_2}{2}},
\qquad
\boxed{R=\frac{|x_2-x_1|}{2}}.
$$

Every other point \((x,y)\) on that wavefront obeys

$$
(x-x_s)^2+(y-y_s)^2=R^2.
$$

If a third point’s horizontal coordinate \(x_3\) is known,

$$
\boxed{
y_3=y_s\pm\sqrt{R^2-(x_3-x_s)^2}
}.
$$

Choose the sign from the diagram, and require

$$
|x_3-x_s|\le R
$$

for a real point on the wavefront. The midpoint shortcut fails if the source is not constrained to the receivers’ line or if the detections correspond to different wavefronts.

## 6. Interference extrema along an axis

Place coherent sources at

$$
A=(0,0),
\qquad
B=(0,-d),
$$

and observe along

$$
P=(x,0),
\qquad x>0.
$$

The path lengths and their positive difference are

$$
r_A=x,
\qquad
r_B=\sqrt{x^2+d^2},
\qquad
\Delta r=\sqrt{x^2+d^2}-x.
$$

Let \(D>0\) be whichever path difference the phase condition requires. Solve

$$
\sqrt{x^2+d^2}-x=D.
$$

Move \(x\) and square:

$$
\sqrt{x^2+d^2}=x+D,
$$

$$
x^2+d^2=x^2+2Dx+D^2.
$$

Therefore,

$$
\boxed{
x(D)=\frac{d^2-D^2}{2D}
}.
$$

A finite point with \(x>0\) requires

$$
0<D<d.
$$

For arbitrary initial source-phase difference \(\delta\phi_0\),

$$
\delta\phi=\frac{2\pi\Delta r}{\lambda}+\delta\phi_0.
$$

Constructive interference requires \(\delta\phi=2\pi N\), so

$$
D_N^{(\mathrm C)}
=\left(N-\frac{\delta\phi_0}{2\pi}\right)\lambda.
$$

Destructive interference requires \(\delta\phi=(2N+1)\pi\), so

$$
D_N^{(\mathrm D)}
=\left(N+\frac12-\frac{\delta\phi_0}{2\pi}\right)\lambda.
$$

Choose a positive allowed \(D_N<d\), then substitute it into \(x(D)\).

For in-phase constructive interference, \(D=m\lambda\):

$$
\boxed{
x_m=\frac{d^2-m^2\lambda^2}{2m\lambda}
},
\qquad
0<m\lambda<d.
$$

The first maximum encountered while moving right from the origin uses the largest allowed path difference, not necessarily \(m=1\). Since \(\Delta r\) decreases as \(x\) increases,

$$
\boxed{
m_*=\left\lceil\frac d\lambda\right\rceil-1
},
\qquad
x_{\mathrm{first}}=x_{m_*},
$$

provided \(m_*\ge1\). If \(d/\lambda\) is an integer, the order \(m=d/\lambda\) lies at \(x=0\) and is excluded by \(x>0\). Complete destructive interference additionally requires equal received amplitudes.

# Homework and practice-quiz families

## 7. Perfectly inelastic capture by a spring oscillator

Consider a mass \(M\) oscillating horizontally on an ideal spring of constant \(k\). At displacement \(x_c\), an incoming mass \(m\) sticks to it.

Assume the collision is short compared with the oscillation period. The spring then supplies negligible impulse during the collision, and the position does not change appreciably. Let \(v^-\) be the oscillator’s signed velocity immediately before capture and \(u^-\) the incoming mass’s horizontal velocity.

All momentum and energy terms below refer to motion along the oscillator’s \(x\)-axis. If the incoming object also has perpendicular kinetic energy, the reduced-mass expression below is only the horizontal mechanical-energy change \(\Delta E_x\), not the total collision-energy loss.

### Recover the pre-collision velocity

Before impact,

$$
\frac12kA_i^2
=\frac12kx_c^2+\frac12M(v^-)^2.
$$

Thus,

$$
\boxed{
v^-=\pm\sqrt{\frac{k}{M}\left(A_i^2-x_c^2\right)}
}.
$$

Choose the sign from the actual direction of motion.

### Apply momentum during capture

Mechanical energy is not conserved in a sticking collision, but horizontal momentum is:

$$
Mv^-+mu^-=(M+m)v^+.
$$

Therefore,

$$
\boxed{
v^+=\frac{Mv^-+mu^-}{M+m}
}.
$$

Because the spring position is unchanged during the short collision, its potential-energy term cancels from the energy change:

$$
\begin{aligned}
\Delta E_x
&=\left[\frac12(M+m)(v^+)^2+\frac12kx_c^2\right]\\
&\quad-\left[\frac12M(v^-)^2+\frac12m(u^-)^2+\frac12kx_c^2\right]\\
&=\boxed{
-\frac12\frac{Mm}{M+m}(v^--u^-)^2
}.
\end{aligned}
$$

The missing mechanical energy becomes deformation, heat, and sound.

### Start the new oscillation

For a horizontal spring, adding mass does not shift equilibrium. Immediately after capture,

$$
\frac12kA_f^2
=\frac12kx_c^2+\frac12(M+m)(v^+)^2.
$$

Hence,

$$
\boxed{
A_f
=\sqrt{
x_c^2+\frac{(Mv^-+mu^-)^2}{k(M+m)}
}
},
$$

$$
\boxed{
T_f=2\pi\sqrt{\frac{M+m}{k}}
}.
$$

If the incoming object has no horizontal velocity, \(u^-=0\):

$$
v^+=\frac{M}{M+m}v^-,
$$

$$
\boxed{
A_f=\sqrt{\frac{MA_i^2+mx_c^2}{M+m}}
}
=\sqrt{A_i^2+\frac{2\Delta E_x}{k}}.
$$

In the strictly one-dimensional model, \(\Delta E_x\) is the complete mechanical-energy change and may be written simply as \(\Delta E\).

For a vertical spring, adding mass shifts equilibrium; measure the impact position relative to the new equilibrium before applying the post-collision amplitude formula. If the objects rebound, replace the sticking condition with the appropriate collision relation.

## 8. Support tension for a hinged shelf

Consider a horizontal rigid shelf hinged at one end. A support cable attaches a distance \(a\) from the hinge and makes angle \(\theta\) with the shelf. Distances \(a\), \(x_s\), and \(x_j\) are measured along the shelf.

Let the shelf’s weight \(W_s=M_sg\) act at distance \(x_s\), and let additional downward forces \(F_j\) act at positions \(x_j\).

Take torques about the hinge so the unknown hinge forces disappear. Only the component of cable tension perpendicular to the shelf contributes:

$$
F_{T,\perp}=F_T\sin\theta.
$$

Static rotational equilibrium gives

$$
aF_T\sin\theta-W_sx_s-\sum_jF_jx_j=0.
$$

Thus,

$$
\boxed{
F_T=\frac{W_sx_s+\sum_jF_jx_j}{a\sin\theta}
}.
$$

If every load is a stationary suspended mass, \(F_j=m_jg\):

$$
\boxed{
F_T=\frac{g(M_sx_s+\sum_jm_jx_j)}{a\sin\theta}
}.
$$

For a uniform shelf of length \(L\), a cable attached at its end, and one stationary end load \(m_\ell\),

$$
a=L,
\qquad
x_s=\frac L2,
\qquad
x_\ell=L,
$$

so

$$
\boxed{
F_T=\frac{(M_s+2m_\ell)g}{2\sin\theta}
}.
$$

The angle must be measured between the cable and shelf. A hanging object contributes its string tension, which equals \(mg\) only when that object has zero acceleration.

If the shelf instead makes angle \(\varphi\) above horizontal while the listed distances remain measured along it, each downward force gains the perpendicular factor \(\cos\varphi\):

$$
\boxed{
F_T=
\frac{\cos\varphi\left(W_sx_s+\sum_jF_jx_j\right)}
{a\sin\theta}
}.
$$

## 9. Wave speed in a shelf-support wire

Treat the taut support wire as a uniform string of vibrating length \(L_w\), mass \(m_w\), and approximately uniform tension \(F_T\):

$$
\mu=\frac{m_w}{L_w},
\qquad
v_w=\sqrt{\frac{F_T}{\mu}}
=\sqrt{\frac{F_TL_w}{m_w}}.
$$

Insert the general shelf-tension result:

$$
\boxed{
v_w=
\sqrt{
\frac{L_w}{m_w}
\frac{W_sx_s+\sum_jF_jx_j}{a\sin\theta}
}
}.
$$

For a horizontal shelf, if the cable’s upper endpoint is directly above the hinge, its horizontal projection is \(a\):

$$
L_w\cos\theta=a
\quad\Longrightarrow\quad
L_w=\frac a{\cos\theta}.
$$

Then

$$
\boxed{
v_w=
\sqrt{
\frac{W_sx_s+\sum_jF_jx_j}
{m_w\sin\theta\cos\theta}
}
}.
$$

For a uniform shelf of length \(L\), supported at its end, with a stationary end load \(m_\ell\),

$$
W_sx_s+F_\ell x_\ell
=M_sg\frac L2+m_\ell gL,
$$

$$
\boxed{
v_w=
\sqrt{
\frac{(M_s+2m_\ell)gL}
{2m_w\sin\theta\cos\theta}
}
}.
$$

Wave amplitude and wavelength do not determine propagation speed in this ideal-string model; once \(v_w\) is known, \(f=v_w/\lambda\). Significant wire weight, sag, or varying density makes \(F_T\) or \(\mu\) position-dependent.

## 10. Difference between wavelength counts

Suppose electromagnetic wave \(i\), of frequency \(f_i\), travels an actual path length \(d_i\) through a stationary homogeneous medium with refractive index \(n_i\).

The number of phase cycles across the path is

$$
N_i=\frac{d_i}{\lambda_i}.
$$

For any wave type, the safe starting point is

$$
N_i=\frac{d_i}{\lambda_i}=\frac{d_if_i}{v_i}.
$$

The refractive-index substitution below specializes that generator to light.

Frequency does not change at a stationary boundary. Since

$$
v_i=f_i\lambda_i,
\qquad
v_i=\frac{c_0}{n_i},
$$

the medium wavelength is

$$
\lambda_i=\frac{c_0}{n_if_i}.
$$

Therefore,

$$
\boxed{
N_i=\frac{n_id_if_i}{c_0}
}.
$$

For two waves,

$$
\boxed{
N_1-N_2
=\frac{n_1d_1f_1-n_2d_2f_2}{c_0}
}.
$$

If both traverse the same distance \(d\),

$$
N_1-N_2=\frac d{c_0}(n_1f_1-n_2f_2).
$$

If the medium is also nondispersive over the two frequencies, \(n_1=n_2=n\):

$$
\boxed{
N_1-N_2=\frac{nd}{c_0}(f_1-f_2)
}.
$$

Use \(|N_1-N_2|\) if only the magnitude is requested. In a dispersive medium, retain \(n(f_1)\) and \(n(f_2)\). The associated propagation-phase difference is

$$
\Delta\phi=2\pi\Delta N.
$$

Across several layers,

$$
N_i=\frac{f_i}{c_0}\sum_j n_{ij}d_j.
$$

## 11. Confined sound versus spherical spreading

Let a source emit acoustic power \(P\). At distance \(d\), ideal isotropic spherical spreading gives

$$
I_{\mathrm{sph}}=\frac{P}{4\pi d^2}.
$$

Now guide a fraction \(\eta\) of that power through a uniform tube of cross-sectional area \(\mathcal A_t\). If the power is uniformly distributed and wall losses are neglected,

$$
P_{\mathrm{tube}}=\eta P,
\qquad
I_{\mathrm{tube}}=\frac{\eta P}{\mathcal A_t}.
$$

The intensity ratio is

$$
\boxed{
\frac{I_{\mathrm{tube}}}{I_{\mathrm{sph}}}
=\frac{4\pi\eta d^2}{\mathcal A_t}
}.
$$

For a circular tube of radius \(r\), \(\mathcal A_t=\pi r^2\):

$$
\boxed{
\frac{I_{\mathrm{tube}}}{I_{\mathrm{sph}}}
=\eta\left(\frac{2d}{r}\right)^2
}.
$$

Sound intensity level is

$$
\beta=(10\,\mathrm{dB})\log_{10}\frac I{I_0}.
$$

Subtracting the spherical and tube levels eliminates \(I_0\):

$$
\beta_{\mathrm{tube}}-\beta_{\mathrm{sph}}
=(10\,\mathrm{dB})
\log_{10}\frac{I_{\mathrm{tube}}}{I_{\mathrm{sph}}}.
$$

Therefore,

$$
\boxed{
\beta_{\mathrm{tube}}
=\beta_{\mathrm{sph}}
+(10\,\mathrm{dB})\log_{10}\eta
+(20\,\mathrm{dB})\log_{10}\frac{2d}{r}
}.
$$

For perfect coupling and no losses, \(\eta=1\), leaving the familiar \(20\log_{10}(2d/r)\) increase. If power is not uniformly distributed across the tube or leaks through the walls, replace this ideal area model with the actual transmitted power and effective area.

## 12. Double Doppler shift from a stationary reflector

Treat reflection as two consecutive Doppler transformations.

Let a source emit frequency \(f_0\) while moving directly toward a stationary wall at speed \(u_s\). The wall is a stationary observer, so it receives

$$
f_1=f_0\frac{c_s}{c_s-u_s}.
$$

A stationary reflector does not change frequency in the medium’s frame. It therefore reradiates the reflected wave with frequency \(f_1\).

Let the returning observer move toward the reflected wave at speed \(u_o\). For a moving observer and stationary reflected source,

$$
f_{\mathrm{echo}}=f_1\frac{c_s+u_o}{c_s}.
$$

Combining the two legs,

$$
\boxed{
f_{\mathrm{echo}}
=f_0\frac{c_s+u_o}{c_s-u_s}
}.
$$

If the emitter and receiver are the same object continuing toward the wall at constant speed \(u\),

$$
\boxed{
f_{\mathrm{echo}}
=f_0\frac{c_s+u}{c_s-u}
}.
$$

The two factors are different because the object is a moving source on the outbound leg and a moving observer on the return leg. For other directions, determine separately whether each leg raises or lowers the frequency; do not reuse one global sign blindly. A moving reflector requires additional Doppler transformations.

## 13. Doppler extrema from a rotating source

Convert the rotation rate to cycles per second:

$$
f_{\mathrm{rot}}=\frac{\mathrm{rpm}}{60}.
$$

For circular radius \(R\), the source speed is

$$
u=2\pi Rf_{\mathrm{rot}}.
$$

Only the line-of-sight component changes the observed frequency. Let \(\hat n\) point from the source toward the observer and define

$$
u_{\mathrm{LOS}}=\vec u\cdot\hat n,
$$

positive when the source moves toward the observer. For a stationary observer,

$$
\boxed{
f_{\mathrm{obs}}
=f_0\frac{c_s}{c_s-u_{\mathrm{LOS}}}
}.
$$

If the observer lies outside the circular path, tangent sightlines allow

$$
u_{\mathrm{LOS,max}}=+u,
\qquad
u_{\mathrm{LOS,min}}=-u.
$$

Then

$$
\boxed{
f_{\max}=f_0\frac{c_s}{c_s-u}
},
\qquad
\boxed{
f_{\min}=f_0\frac{c_s}{c_s+u}
}.
$$

Do not automatically substitute \(\pm u\) when the observer geometry cannot produce those projections. For example, an observer at the center of the circle has \(u_{\mathrm{LOS}}=0\) at every instant and hears no first-order Doppler modulation.

## 14. Standing-wave shortcuts from boundary conditions

### Feature spacing

Adjacent nodes and adjacent antinodes are each separated by half a wavelength:

$$
\Delta x_{NN}=\Delta x_{AA}=\frac\lambda2.
$$

Therefore,

$$
\lambda=2\Delta x_{NN}=2\Delta x_{AA},
$$

$$
\boxed{
f=\frac{v}{2\Delta x_{NN}}
=\frac{v}{2\Delta x_{AA}}
}.
$$

An adjacent node and antinode are separated by \(\lambda/4\), so \(f=v/(4\Delta x_{NA})\).

### Allowed harmonics

For equal-end boundary conditions—fixed–fixed strings, open–open pipes, or closed–closed pipes—

$$
L=\frac{n\lambda_n}{2},
\qquad
n=1,2,3,\ldots
$$

and

$$
\boxed{
f_n=\frac{nv}{2L}=nf_1
}.
$$

For an open–closed pipe,

$$
L=\frac{n\lambda_n}{4},
\qquad
n=1,3,5,\ldots
$$

so

$$
\boxed{
f_n=\frac{nv}{4L}=nf_1
}.
$$

At fixed \(v\), \(L\), and boundary conditions,

$$
\boxed{
\frac{f_b}{f_a}=\frac{n_b}{n_a}
}.
$$

For an open–closed pipe, use odd harmonic labels; the next mode after \(n=1\) is \(n=3\), not \(n=2\).

### Equal fundamentals

For the same wave speed,

$$
f_{1,\mathrm{OO}}=\frac{v}{2L_{\mathrm{OO}}},
\qquad
f_{1,\mathrm{OC}}=\frac{v}{4L_{\mathrm{OC}}}.
$$

Equating them gives

$$
\frac{v}{2L_{\mathrm{OO}}}
=\frac{v}{4L_{\mathrm{OC}}}
\quad\Longrightarrow\quad
\boxed{
L_{\mathrm{OC}}=\frac{L_{\mathrm{OO}}}{2}
}.
$$

### Solve a string mode backward for tension

For a uniform string fixed at both ends,

$$
f_n=\frac{n}{2L}\sqrt{\frac{F_T}{\mu}}.
$$

Isolate the square root and square:

$$
\frac{2Lf_n}{n}=\sqrt{\frac{F_T}{\mu}},
$$

$$
\boxed{
F_T=\mu\left(\frac{2Lf_n}{n}\right)^2
}.
$$

If the entire vibrating span has mass \(m_w\), then \(\mu=m_w/L\):

$$
\boxed{
F_T=\frac{4m_wLf_n^2}{n^2}
}.
$$

All of these shortcuts come from the same two moves: translate the boundary pattern into \(\lambda_n\), then use \(f_n=v/\lambda_n\).
