---
cssclasses: mth212-cheat-sheet
---

<style>
@page { size: letter; margin: 0.35in; }
.markdown-preview-view.mth212-cheat-sheet .markdown-preview-sizer { max-width: none; }
.markdown-preview-view.mth212-cheat-sheet { font-size: 8.2pt; line-height: 1.12; }
.markdown-preview-view.mth212-cheat-sheet h1 { font-size: 13pt; margin: 0 0 4px; }
.markdown-preview-view.mth212-cheat-sheet h2 { font-size: 9.5pt; margin: 5px 0 2px; padding: 0; border-bottom: 1px solid var(--background-modifier-border); }
.markdown-preview-view.mth212-cheat-sheet p,
.markdown-preview-view.mth212-cheat-sheet ul { margin-block: 1px; }
.markdown-preview-view.mth212-cheat-sheet li { margin-block: 0; }
.markdown-preview-view.mth212-cheat-sheet table { font-size: 7.4pt; line-height: 1.08; margin: 2px 0 4px; }
.markdown-preview-view.mth212-cheat-sheet th,
.markdown-preview-view.mth212-cheat-sheet td { padding: 1px 4px; vertical-align: top; }
@media print {
  .markdown-preview-view.mth212-cheat-sheet .markdown-preview-sizer { column-count: 2; column-gap: 0.18in; }
  .markdown-preview-view.mth212-cheat-sheet h1 { column-span: all; }
}
</style>

# MTH 212 Cheat Sheet

Use radians unless told otherwise. $g\approx9.8\ \mathrm{m/s^2}$. Choose inward radial as positive unless a problem says otherwise.

## Core Kinematics

| Idea | Equations / Cues |
| --- | --- |
| Angle units | $1\ \mathrm{rev}=2\pi\ \mathrm{rad}$, $\omega=(\mathrm{rpm})(2\pi/60)$ |
| Period/frequency | $f=1/T$, $\omega=2\pi f=2\pi/T$, $v=2\pi r/T$ |
| Definitions | $\omega=d\theta/dt$, $\alpha=d\omega/dt=d^2\theta/dt^2$ |
| Constant $\alpha$ | $\omega_f=\omega_0+\alpha t$; $\theta_f=\theta_0+\omega_0t+\frac12\alpha t^2$; $\omega_f^2=\omega_0^2+2\alpha\Delta\theta$ |
| Reversal/stopping | Set $\omega(t)=0$. Then use $\Delta\theta=\omega_0t+\frac12\alpha t^2$ or $\omega_f^2=\omega_0^2+2\alpha\Delta\theta$. |
| Graphs | slope of $\theta(t)$ is $\omega$; slope of $\omega(t)$ is $\alpha$; area under $\omega(t)$ is $\Delta\theta$. |
| Units check | Every term in a sum has same units. If $\theta=At^n$, then $[A]=\mathrm{rad/s^n}$. If $\alpha=Bt^n$, then $[B]=\mathrm{rad/s^{n+2}}$. |

## Circular Motion

| Quantity | Formula / Direction |
| --- | --- |
| Arc length | $s=r\theta$ |
| Tangential speed | $v_t=r\omega$ |
| Tangential acceleration | $a_t=r\alpha$; along motion if speeding up, opposite if slowing down |
| Radial/centripetal acceleration | $a_r=\dfrac{v^2}{r}=r\omega^2=\dfrac{4\pi^2r}{T^2}$, always inward |
| Total acceleration | $\vec a=\vec a_r+\vec a_t$, $|\vec a|=\sqrt{a_r^2+a_t^2}$ when perpendicular |
| Net force | $\sum F_r=m\dfrac{v^2}{r}=mr\omega^2$; $\sum F_t=ma_t=mr\alpha$ |
| Arrow questions | $\vec F_{\mathrm{net}}$ points with $\vec a$: inward plus tangent. Uniform circle: inward only. |

## Force Setup Rules

- Draw only real forces: weight, normal, tension, friction. Do **not** draw a separate "centripetal force."
- Static friction: $|f_s|\le \mu_sN$; at threshold $f_s=\mu_sN$.
- Vertical balance usually means $\sum F_y=0$. Circular motion needs inward $\sum F_r=mv^2/r$.
- Normal force can push, not pull. Contact loss means $N=0$.

## Common Systems

| System | Equations / Results |
| --- | --- |
| Level flat curve | $N=mg$, $f_s=mv^2/r$. Threshold: $\mu_smg=mv^2/r$, so $\mu_{s,\min}=v^2/(rg)$ and $v_{\max}=\sqrt{\mu_sgr}$. |
| Coin on turntable | Static friction supplies radial force: $\mu_smg\ge mr\omega^2$. Thus $\omega_{\max}=\sqrt{\mu_sg/r}$ and $T_{\min}=2\pi\sqrt{r/(\mu_sg)}$. |
| Top of Ferris wheel / hill | Inward is down: $mg-N=mv^2/r$, so $N=mg-mv^2/r<mg$. Contact loss when $v^2=gr$. |
| Bottom of Ferris wheel | Inward is up: $N-mg=mv^2/r$, so $N=mg+mv^2/r>mg$. |
| Top inside a loop | Inward is down: $mg+N=mv^2/r$. Minimum contact at top: $N=0$, $v_{\text{top,min}}=\sqrt{gr}$. |
| Loop entry from bottom | Energy from bottom to top: $\frac12mv_0^2=\frac12mv_\text{top}^2+mg(2r)$. With $v_\text{top}^2=gr$: $v_{0,\min}=\sqrt{5gr}$. |
| Outside sphere / igloo | Radial: $mg\cos\theta-N=mv^2/r$. Lift-off: $N=0$, so $v^2=gr\cos\theta$. From rest at top: $v^2=2gr(1-\cos\theta)$. Therefore $\cos\theta_c=2/3$, $\theta_c\approx48.2^\circ$. |
| Vertical-circle release | First get $v^2$ from radial forces. Then use tangent component $v_y$ and projectile rise $\Delta y=v_y^2/(2g)$. |

## Banked Curves

Let $\theta$ be the bank angle from horizontal. Normal components: $N_y=N\cos\theta$, $N_r=N\sin\theta$.

| Case | Equations / Result |
| --- | --- |
| Frictionless bank | $N\cos\theta=mg$, $N\sin\theta=mv^2/r$, so $\tan\theta=v^2/(rg)$ and $v=\sqrt{rg\tan\theta}$. |
| High-speed limit | Car tends up bank; friction points **down** bank: $f=\mu_sN$. $N(\sin\theta+\mu_s\cos\theta)=mv^2/r$, $N(\cos\theta-\mu_s\sin\theta)=mg$. $v_{\max}=\sqrt{rg\dfrac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}}$. |
| Low-speed limit | Car tends down bank; friction points **up** bank. $v_{\min}=\sqrt{rg\dfrac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}}$ when numerator is positive. |
| Given uphill friction | $N\sin\theta-f_s\cos\theta=mv^2/r$, $N\cos\theta+f_s\sin\theta=mg$. Solving gives $f_s=mg\sin\theta-\dfrac{mv^2}{r}\cos\theta$. A negative result means friction actually points down bank. |

## Conical / Cone Motion

| System | Equations / Result |
| --- | --- |
| Conical pendulum, string angle $\theta$ from vertical | $r=L\sin\theta$, $T\cos\theta=mg$, $T\sin\theta=mv^2/r$. Hence $\tan\theta=v^2/(rg)=\omega^2r/g$. |
| Conical pendulum period | $\omega=\sqrt{g\tan\theta/r}$, so $P=2\pi\sqrt{r/(g\tan\theta)}$. |
| Bead on frictionless inverted cone | If $\theta$ is measured between $N$ and radial inward: $N\sin\theta=mg$, $N\cos\theta=mv^2/r$, so $\tan\theta=gr/v^2$. With cone geometry $\tan\theta=r/h$, $v=\sqrt{gh}$ and $P=2\pi r/\sqrt{gh}$. |

## Fast Problem Patterns

| Cue | First Move |
| --- | --- |
| "speeding up/slowing down" in circular path | Add tangential acceleration to inward radial acceleration. |
| "constant speed" | $a_t=0$; acceleration/net force is purely inward. |
| "minimum/maximum before slipping" | Use $f_s=\mu_sN$ and pick friction direction from impending slip. |
| "loses contact" | Set $N=0$ in the radial equation, not $a_r=0$. |
| "frictionless" with height change | Use energy: $\frac12mv_i^2+mgy_i=\frac12mv_f^2+mgy_f$. |
| "which FBD?" | Include only real forces; velocity/acceleration are not forces. |
