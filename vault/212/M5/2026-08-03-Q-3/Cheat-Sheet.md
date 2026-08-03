$$
\text{SHM graph:}\qquad x_{\mathrm{eq}}=\frac{x_{\max}+x_{\min}}{2}\qquad A=\frac{x_{\max}-x_{\min}}{2}\qquad x\equiv x_{\mathrm{abs}}-x_{\mathrm{eq}}\qquad T=\frac{\Delta t}{N}\qquad f=\frac1T\qquad \omega=2\pi f=\frac{2\pi}{T}
$$
$$
\text{SHM state:}\qquad x(t)=A\cos(\omega t+\phi_0)\qquad v(t)=-A\omega\sin(\omega t+\phi_0)\qquad a(t)=-A\omega^2\cos(\omega t+\phi_0)=-\omega^2x(t)
$$
$$
\text{SHM rescue:}\qquad A=\sqrt{x_0^2+\left(\frac{v_0}{\omega}\right)^2}\qquad \phi_0=\operatorname{atan2}\!\left(-\frac{v_0}{\omega},x_0\right)\qquad v_{\max}=A\omega\qquad a_{\max}=A\omega^2
$$
$$
\text{spring:}\qquad F_x=-k_sx\qquad U_s=\frac12k_sx^2\qquad \omega_s=\sqrt{\frac{k_s}{m}}\qquad T_s=2\pi\sqrt{\frac{m}{k_s}}\qquad f_s=\frac1{2\pi}\sqrt{\frac{k_s}{m}}
$$
$$
\text{spring energy:}\qquad E=\frac12k_sA^2=\frac12k_sx^2+\frac12mv^2\qquad v(x)=\pm\omega_s\sqrt{A^2-x^2}\qquad \frac{U}{E}=\frac{x^2}{A^2}\qquad \frac{K}{E}=1-\frac{x^2}{A^2}
$$
$$
\text{spring maxima:}\qquad K_{\max}=\frac12m(A\omega_s)^2=\frac12k_sA^2\qquad v_{\max}=A\omega_s=A\sqrt{\frac{k_s}{m}}
$$
$$
\text{horizontal stick at }x_c\ [M=\text{block},m=\text{clay at rest}]:\qquad \omega_i=\sqrt{\frac{k_s}{M}}\qquad v_0\equiv|v|=\omega_i\sqrt{A^2-x_c^2}\qquad v_f=\frac{M}{M+m}v_0
$$
$$
\text{inelastic loss:}\qquad \Delta E\equiv E_{\mathrm{after}}-E_{\mathrm{before}}=-\frac12\frac{Mm}{M+m}v_0^2
$$
$$
\text{new oscillation }[x_{\mathrm{eq}}\text{ unchanged}]:\qquad A_f=\sqrt{x_c^2+\frac{M+m}{k_s}v_f^2}=\sqrt{A^2+\frac{2\Delta E}{k_s}}\qquad T_f=2\pi\sqrt{\frac{M+m}{k_s}}
$$
$$
\text{simple pendulum }[|\theta|\ll1\text{ rad},\ L=\text{pivot--bob CM}]:\qquad \sin\theta\simeq\theta\qquad \omega=\sqrt{\frac{g}{L}}\qquad T=2\pi\sqrt{\frac{L}{g}}\qquad f=\frac1{2\pi}\sqrt{\frac{g}{L}}\qquad \frac{\partial T}{\partial m}=0
$$
$$
\text{physical pendulum }(|\theta|\ll1\text{ rad}):\qquad \tau=-Mg\ell\sin\theta\simeq-Mg\ell\theta\qquad \omega=\sqrt{\frac{Mg\ell}{I_P}}\qquad T=2\pi\sqrt{\frac{I_P}{Mg\ell}}\qquad f=\frac1{2\pi}\sqrt{\frac{Mg\ell}{I_P}}
$$
$$
\text{composite pendulum }[d_i=\text{pivot--component CM}]:\qquad I_P=\sum_i\left(I_{i,\mathrm{cm}}+m_id_i^2\right)\qquad \ell=\frac{\sum_i m_id_i}{\sum_i m_i}\qquad T=2\pi\sqrt{\frac{\sum_i(I_{i,\mathrm{cm}}+m_id_i^2)}{g\sum_i m_id_i}}
$$
$$
\text{inertia ledger:}\qquad I_{\mathrm{point}}=md^2\qquad I_{\mathrm{rod,cm}}=\frac1{12}mL^2\qquad I_{\mathrm{rod,end}}=\frac13mL^2\qquad I_{\mathrm{solid\ disk,cm}}=\frac12mR^2\qquad I_{\mathrm{solid\ sphere,cm}}=\frac25mR^2
$$
$$
\text{rod endpoints:}\qquad T_{\mathrm{end}}=2\pi\sqrt{\frac{2L}{3g}}\qquad T_{\mathrm{pivot} L/6}=2\pi\sqrt{\frac{7L}{12g}}
$$
$$
\text{rod + point mass:}\qquad T=2\pi\sqrt{\frac{\frac13M_rL^2+M_pL^2}{g(M_rL/2+M_pL)}}=2\pi\sqrt{\frac{2L(M_r+3M_p)}{3g(M_r+2M_p)}}
$$
$$
\text{rod + solid body tangent at end:}\qquad T=2\pi\sqrt{\frac{\frac13M_rL^2+I_{b,\mathrm{cm}}+M_bd^2}{g(M_rL/2+M_bd)}}\qquad d=L+R\qquad I_{b,\mathrm{cm}}=\frac12M_bR^2\ (\text{disk}),\ \frac25M_bR^2\ (\text{sphere})
$$
$$
\text{traveling wave:}\qquad y(x,t)=A\sin(kx\mp\omega t+\phi_0)\qquad k=\frac{2\pi}{\lambda}\qquad \omega=2\pi f\qquad v_w=\lambda f=\frac{\omega}{k}\qquad (-\omega t\!:\,+x,\ +\omega t\!:\,-x)
$$
$$
\text{medium particle:}\qquad v_y=\frac{\partial y}{\partial t}=\mp v_w\frac{\partial y}{\partial x}\qquad a_y=\frac{\partial^2y}{\partial t^2}=-\omega^2y\qquad |v_y|_{\max}=A\omega=\frac{2\pi A}{\lambda}v_w
$$
$$
\text{string wave:}\qquad \mu=\frac{m_w}{L_w}\qquad v_w=\sqrt{\frac{F_T}{\mu}}=\sqrt{\frac{F_TL_w}{m_w}}\qquad F_T=\mu v_w^2\qquad \frac{v_2}{v_1}=\sqrt{\frac{F_{T2}}{F_{T1}}\frac{\mu_1}{\mu_2}}
$$
$$
\text{static hanging load:}\qquad F_T=M_hg\qquad v_w=\sqrt{\frac{M_hgL_w}{m_w}}\qquad |v_y|_{\max}=\frac{2\pi A}{\lambda}\sqrt{\frac{M_hgL_w}{m_w}}
$$
$$
\text{refraction/counting:}\qquad n=\frac{c_0}{v}=\frac{\lambda_0}{\lambda}\qquad f_{\mathrm{vac}}=f_{\mathrm{med}}\qquad n_1\lambda_1=n_2\lambda_2\qquad N_\lambda=\frac{d}{\lambda}=\frac{ndf}{c_0}
$$
$$
\text{two-frequency count }[n\text{ constant}]:\qquad \Delta N_\lambda=\frac{nd}{c_0}(f_g-f_r)
$$
$$
\text{wavefront midpoint }[S,(x_1,0),(x_2,0)\text{ on }x\text{-axis}]:\qquad x_s=\frac{x_1+x_2}{2}\qquad y_s=0\qquad R=\frac{|x_2-x_1|}{2}
$$
$$
\text{wavefront circle:}\qquad (x-x_s)^2+(y-y_s)^2=R^2\qquad P=(0,y>0)\Rightarrow y=\sqrt{R^2-x_s^2}
$$
$$
\text{wave power }[\text{fixed medium; same area for }I]:\qquad P_{\mathrm{avg}},I\propto f^2A^2\qquad \frac{P_2}{P_1}=\frac{I_2}{I_1}=\left(\frac{f_2}{f_1}\right)^2\left(\frac{A_2}{A_1}\right)^2
$$
$$
\text{intensity spreading }[\text{isotropic, fixed }P,\text{ no loss}]:\qquad I=\frac{P}{S}\qquad I_{\mathrm{sph}}=\frac{P}{4\pi r^2}\qquad I_1r_1^2=I_2r_2^2\qquad I_2=I_1\left(\frac{r_1}{r_2}\right)^2\qquad r_2=r_1\sqrt{\frac{I_1}{I_2}}
$$
$$
\text{decibels:}\qquad \beta=(10\,\mathrm{dB})\log_{10}\!\frac{I}{I_0}\qquad I_0=10^{-12}\,\mathrm{W/m^2}\qquad I=I_0\,10^{\beta/(10\,\mathrm{dB})}\qquad \Delta\beta=(10\,\mathrm{dB})\log_{10}\!\frac{I_2}{I_1}
$$
$$
\text{independent/incoherent sources:}\qquad I_{\mathrm{tot}}=\sum_iI_i\qquad \beta_{\mathrm{tot}}=(10\,\mathrm{dB})\log_{10}\!\left[\sum_i10^{\beta_i/(10\,\mathrm{dB})}\right]
$$
$$
\text{equal independent sources:}\qquad \beta_N=\beta_1+(10\,\mathrm{dB})\log_{10}N\qquad 2I\Rightarrow+3.01\,\mathrm{dB}\qquad 10I\Rightarrow+10\,\mathrm{dB}
$$
$$
\text{lossless tube }[\text{same full }P\text{ enters tube}]:\qquad I_{\mathrm{sph}}=\frac{P}{4\pi d^2}\qquad I_{\mathrm{tube}}=\frac{P}{\pi r^2}\qquad \frac{I_{\mathrm{tube}}}{I_{\mathrm{sph}}}=\left(\frac{2d}{r}\right)^2\qquad \beta_{\mathrm{tube}}=\beta_{\mathrm{sph}}+(20\,\mathrm{dB})\log_{10}\!\frac{2d}{r}
$$
$$
\text{Doppler selector }[\text{direct LOS; speeds through medium; }v_s<c_s]:\qquad \begin{array}{c|cc} & \text{toward }(f'>f_0) & \text{away }(f'<f_0) \\ \text{observer moves} & f'=f_0(1+v_o/c_s) & f'=f_0(1-v_o/c_s) \\ \text{source moves} & f'=f_0/(1-v_s/c_s) & f'=f_0/(1+v_s/c_s) \end{array}
$$
$$
\text{Doppler general:}\qquad f'=f_0\frac{c_s+u_o}{c_s-u_s}\qquad u_o>0:\ O\text{ toward }S\qquad u_s>0:\ S\text{ toward }O\qquad (u<0:\ \text{away})
$$
$$
\text{Doppler inverse }[\text{observer}]:\qquad v_{o,\mathrm{toward}}=c_s\left(\frac{f'}{f_0}-1\right)\qquad v_{o,\mathrm{away}}=c_s\left(1-\frac{f'}{f_0}\right)
$$
$$
\text{Doppler inverse }[\text{source}]:\qquad v_{s,\mathrm{toward}}=c_s\left(1-\frac{f_0}{f'}\right)\qquad v_{s,\mathrm{away}}=c_s\left(\frac{f_0}{f'}-1\right)
$$
$$
\text{echo }[\text{source approaches stationary wall head-on}]:\qquad f_1=f_0\frac{c_s}{c_s-v_s}\qquad f_{\mathrm{echo}}=f_1\frac{c_s+v_s}{c_s}=f_0\frac{c_s+v_s}{c_s-v_s}
$$
$$
\text{rotating source:}\qquad f_{\mathrm{rot}}=\frac{\mathrm{rpm}}{60}\qquad v_s=2\pi Rf_{\mathrm{rot}}\qquad f_{\mathrm{high}}=f_0\frac{c_s}{c_s-v_s}\qquad f_{\mathrm{low}}=f_0\frac{c_s}{c_s+v_s}
$$
$$
\text{transverse-string reflection:}\qquad \text{fixed end: }y_r=-y_i,\ \Delta\phi_{\mathrm{ref}}=\pi\qquad \text{free end: }y_r=+y_i,\ \Delta\phi_{\mathrm{ref}}=0
$$
$$
\text{standing-wave boundaries:}\qquad \begin{array}{c|cc} & \text{displacement} & \text{pressure} \\ \text{fixed/closed} & N_y & A_p \\ \text{free/open} & A_y & N_p \end{array}\qquad \Delta x_{NN}=\Delta x_{AA}=\frac{\lambda}{2}\qquad \Delta x_{NA}=\frac{\lambda}{4}
$$
$$
\text{same-type ends:}\qquad \lambda_n=\frac{2L}{n}\qquad f_n=\frac{nv}{2L}=nf_1\qquad n=1,2,3,\ldots\qquad (N\!N\ \text{string/pipe or }A\!A\ \text{pipe})
$$
$$
\text{open--closed pipe:}\qquad \lambda_n=\frac{4L}{n}\qquad f_n=\frac{nv}{4L}=nf_1\qquad n=1,3,5,\ldots\qquad \frac{f_b}{f_a}=\frac{b}{a}
$$
$$
\text{fixed string modes:}\qquad f_n=\frac{n}{2L}\sqrt{\frac{F_T}{\mu}}=\frac{n}{2}\sqrt{\frac{F_T}{m_wL}}\qquad F_T=M_hg\Rightarrow f_n=\frac{n}{2}\sqrt{\frac{M_hg}{m_wL}}\qquad F_T=\frac{4m_wLf_n^2}{n^2}
$$
$$
\text{standing-wave shortcuts }[\text{same resonator/boundary family}]:\qquad f=\frac{v}{2\Delta x_{NN}}=\frac{v}{2\Delta x_{AA}}\qquad f_{n,2}=\frac{n_2}{n_1}f_{n,1}\qquad f_{1,OO}=f_{1,OC}\Rightarrow L_{OC}=\frac{L_{OO}}{2}
$$
$$
\text{coherent superposition }[\text{same }f\text{ and polarization}]:\qquad y_{\mathrm{tot}}=\sum_i y_i\qquad A_R=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\delta\phi}\qquad A_1=A_2=A\Rightarrow A_R=2A\left|\cos\frac{\delta\phi}{2}\right|
$$
$$
\text{coherent intensity at a point:}\qquad I=I_1+I_2+2\sqrt{I_1I_2}\cos\delta\phi\qquad I_1=I_2=I_s\Rightarrow I=4I_s\cos^2\!\frac{\delta\phi}{2}
$$
$$
\text{two-source geometry:}\qquad r_i=\sqrt{(x-x_i)^2+(y-y_i)^2}\qquad \delta r=r_2-r_1
$$
$$
\text{two-source phase:}\qquad \delta\phi_0=\phi_{2,0}-\phi_{1,0}\qquad \delta\phi=\frac{2\pi\delta r}{\lambda}+\delta\phi_0\qquad \delta\phi_{\mathrm{eq}}=\delta\phi\bmod2\pi
$$
$$
\text{sources in phase }(\delta\phi_0=0;\ m=0,1,2,\ldots):\qquad C:\ |\delta r|=m\lambda\qquad D:\ |\delta r|=\left(m+\frac12\right)\lambda\quad(A_1=A_2)
$$
$$
\text{sources opposite }(\delta\phi_0=\pi;\ m=0,1,2,\ldots):\qquad C:\ |\delta r|=\left(m+\frac12\right)\lambda\qquad D:\ |\delta r|=m\lambda\quad(A_1=A_2)
$$
$$
\text{in-phase geometry }[A(0,0),B(0,-d),P(x>0,0)]:\qquad r_A=x\qquad r_B=\sqrt{x^2+d^2}\qquad r_B-r_A=m\lambda\qquad x_m=\frac{d^2-m^2\lambda^2}{2m\lambda}\quad(m=1,2,\ldots)
$$
$$
\text{first maximum for }x>0:\qquad m_*=\left\lceil\frac{d}{\lambda}\right\rceil-1\qquad m_*\ge1\qquad x_{\mathrm{first}}=x_{m_*}
$$
$$
\text{shelf statics }[m_1=\text{shelf},m_2=\text{load},\theta=\angle(\text{wire,shelf})]:\qquad F_{\mathrm{hang}}=m_2g\qquad F_TL\sin\theta-m_1g\frac{L}{2}-m_2gL=0
$$
$$
\text{shelf tension endpoint:}\qquad F_T=\frac{(m_1+2m_2)g}{2\sin\theta}
$$
$$
\text{shelf wire }[m_w\!:\text{wire}]:\qquad L_w=\frac{L}{\cos\theta}\qquad \mu=\frac{m_w}{L_w}=\frac{m_w\cos\theta}{L}
$$
$$
\text{shelf-wave endpoint:}\qquad v_w=\sqrt{\frac{F_T}{\mu}}=\sqrt{\frac{(m_1+2m_2)gL}{2m_w\sin\theta\cos\theta}}\qquad \frac{\partial v_w}{\partial A}=\frac{\partial v_w}{\partial\lambda}=0
$$
$$
g=9.81\,\mathrm{m/s^2}\qquad c_s=343\,\mathrm{m/s}\qquad c_0=3.0\times10^8\,\mathrm{m/s}
$$
