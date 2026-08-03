**SHM / SPRINGS**

$$
\text{graph:}\qquad x_{\mathrm{eq}}=\frac{x_{\max}+x_{\min}}2\qquad A=\frac{x_{\max}-x_{\min}}2\qquad x\equiv x_{\mathrm{abs}}-x_{\mathrm{eq}}\qquad T=\frac{\Delta t}{N}\qquad f=\frac1T\qquad \omega=2\pi f=\frac{2\pi}{T}
$$
$$
\text{state:}\qquad x=A\cos(\omega t+\phi_0)\qquad v=-A\omega\sin(\omega t+\phi_0)\qquad a=-A\omega^2\cos(\omega t+\phi_0)=-\omega^2x
$$
$$
\text{initial-condition rescue:}\qquad A=\sqrt{x_0^2+\left(\frac{v_0}{\omega}\right)^2}\qquad \phi_0=\operatorname{atan2}\!\left(-\frac{v_0}{\omega},x_0\right)\qquad v_{\max}=A\omega\qquad a_{\max}=A\omega^2
$$
$$
\text{spring:}\qquad F_x=-k_sx\qquad U_s=\frac12k_sx^2\qquad \omega_s=\sqrt{\frac{k_s}{m}}\qquad T_s=2\pi\sqrt{\frac{m}{k_s}}\qquad f_s=\frac1{2\pi}\sqrt{\frac{k_s}{m}}
$$
$$
\begin{aligned}
\text{spring energy:}\quad&E=\frac12k_sA^2=\frac12k_sx^2+\frac12mv^2,& v(x)&=\pm\omega_s\sqrt{A^2-x^2},\\
&K_{\max}=\frac12m(A\omega_s)^2=\frac12k_sA^2,& \frac UE&=\frac{x^2}{A^2},\quad \frac KE=1-\frac{x^2}{A^2}
\end{aligned}
$$
$$
\begin{aligned}
\text{horizontal stick at }x_c\ [M=\text{block},m=\text{clay at rest}]:\quad
&\omega_i=\sqrt{\frac{k_s}{M}},& v_0\equiv|v|&=\omega_i\sqrt{A^2-x_c^2},\\
&v_f=\frac{M}{M+m}v_0,& \Delta E&\equiv E_{\mathrm{after}}-E_{\mathrm{before}}=-\frac12\frac{Mm}{M+m}v_0^2
\end{aligned}
$$
$$
\text{new oscillation }[x_{\mathrm{eq}}\text{ unchanged}]:\qquad A_f=\sqrt{x_c^2+\frac{M+m}{k_s}v_f^2}=\sqrt{A^2+\frac{2\Delta E}{k_s}}\qquad T_f=2\pi\sqrt{\frac{M+m}{k_s}}
$$

**PENDULA**

$$
\text{simple }[|\theta|\ll1\text{ rad},\ L=\text{pivot--bob CM}]:\qquad \sin\theta\simeq\theta\qquad \omega=\sqrt{\frac gL}\qquad T=2\pi\sqrt{\frac Lg}\qquad f=\frac1{2\pi}\sqrt{\frac gL}\qquad m,\theta_0\ \text{absent}
$$
$$
\text{physical }[\ell=\text{pivot--total CM}]:\qquad \tau=-Mg\ell\sin\theta\simeq-Mg\ell\theta\qquad \omega=\sqrt{\frac{Mg\ell}{I_P}}\qquad T=2\pi\sqrt{\frac{I_P}{Mg\ell}}\qquad f=\frac1{2\pi}\sqrt{\frac{Mg\ell}{I_P}}
$$
$$
\text{composite }[d_i=\text{pivot--component CM}]:\qquad I_P=\sum_i\left(I_{i,\mathrm{cm}}+m_id_i^2\right)\qquad \ell=\frac{\sum_i m_id_i}{\sum_i m_i}\qquad T=2\pi\sqrt{\frac{\sum_i(I_{i,\mathrm{cm}}+m_id_i^2)}{g\sum_i m_id_i}}
$$
$$
\begin{aligned}
\text{inertia:}\quad&I_{\mathrm{point}}=md^2,&I_{\mathrm{rod,cm}}&=\frac1{12}mL^2,&I_{\mathrm{rod,end}}&=\frac13mL^2,\\
&I_{\mathrm{solid\ disk,cm}}=\frac12mR^2,&I_{\mathrm{solid\ sphere,cm}}&=\frac25mR^2
\end{aligned}
$$
$$
\text{rod endpoints:}\qquad T_{\mathrm{end}}=2\pi\sqrt{\frac{2L}{3g}}\qquad T_{\mathrm{pivot}\ L/6}=2\pi\sqrt{\frac{7L}{12g}}
$$
$$
\text{rod + point:}\qquad T=2\pi\sqrt{\frac{\frac13M_rL^2+M_pL^2}{g(M_rL/2+M_pL)}}=2\pi\sqrt{\frac{2L(M_r+3M_p)}{3g(M_r+2M_p)}}
$$
$$
\begin{aligned}
\text{rod + solid body tangent at end:}\quad
T&=2\pi\sqrt{\frac{\frac13M_rL^2+I_{b,\mathrm{cm}}+M_bd^2}{g(M_rL/2+M_bd)}},&d&=L+R,\\
I_{b,\mathrm{cm}}&=\frac12M_bR^2\ (\text{disk}),&I_{b,\mathrm{cm}}&=\frac25M_bR^2\ (\text{sphere})
\end{aligned}
$$

**TRAVELING WAVES / STRINGS**

$$
\text{traveling wave:}\qquad y=A\sin(kx\mp\omega t+\phi_0)\qquad k=\frac{2\pi}{\lambda}\qquad \omega=2\pi f\qquad v_w=\lambda f=\frac\omega k\qquad kx-\omega t\to+x,\quad kx+\omega t\to-x
$$
$$
\text{medium particle:}\qquad v_y=\frac{\partial y}{\partial t}=\mp v_w\frac{\partial y}{\partial x}\qquad a_y=\frac{\partial^2y}{\partial t^2}=-\omega^2y\qquad |v_y|_{\max}=A\omega=\frac{2\pi A}{\lambda}v_w
$$
$$
\text{string:}\qquad \mu=\frac{m_w}{L_w}\qquad v_w=\sqrt{\frac{F_T}{\mu}}=\sqrt{\frac{F_TL_w}{m_w}}\qquad F_T=\mu v_w^2\qquad \frac{v_2}{v_1}=\sqrt{\frac{F_{T2}}{F_{T1}}\frac{\mu_1}{\mu_2}}
$$
$$
\text{hanging load:}\qquad F_T=M_hg\qquad v_w=\sqrt{\frac{M_hgL_w}{m_w}}\qquad |v_y|_{\max}=\frac{2\pi A}{\lambda}\sqrt{\frac{M_hgL_w}{m_w}}
$$
$$
\begin{aligned}
\text{shelf statics }[m_1=\text{shelf},m_2=\text{load}]:\quad
&F_{\mathrm{hang}}=m_2g,&0&=F_TL\sin\theta-m_1g\frac L2-m_2gL,\\
&&F_T&=\frac{(m_1+2m_2)g}{2\sin\theta}
\end{aligned}
$$
$$
\text{shelf wire }[\theta=\angle(\text{wire,shelf})]:\qquad L_w=\frac L{\cos\theta}\qquad \mu=\frac{m_w\cos\theta}{L}\qquad v_w=\sqrt{\frac{(m_1+2m_2)gL}{2m_w\sin\theta\cos\theta}}\qquad A,\lambda\ \text{unused}
$$
$$
\text{refraction/counting:}\qquad n=\frac{c_0}{v}=\frac{\lambda_0}{\lambda}\qquad f_{\mathrm{vac}}=f_{\mathrm{med}}\qquad n_1\lambda_1=n_2\lambda_2\qquad N_\lambda=\frac d\lambda=\frac{ndf}{c_0}
$$
$$
\text{two-frequency count }[n\text{ constant}]:\qquad \Delta N_\lambda=\frac{nd}{c_0}(f_g-f_r)
$$
$$
\begin{aligned}
\text{circular wavefront }[S,(x_1,0),(x_2,0)\text{ on }x\text{-axis}]:\quad
&x_s=\frac{x_1+x_2}{2},&y_s&=0,&R&=\frac{|x_2-x_1|}{2},\\
&(x-x_s)^2+(y-y_s)^2=R^2,&P=(0,y>0)&\Rightarrow y=\sqrt{R^2-x_s^2}
\end{aligned}
$$
$$
\text{power }[\text{fixed medium; same area for }I]:\qquad P_{\mathrm{avg}},I\propto f^2A^2\qquad \frac{P_2}{P_1}=\frac{I_2}{I_1}=\left(\frac{f_2}{f_1}\right)^2\left(\frac{A_2}{A_1}\right)^2
$$

**INTENSITY / DOPPLER**

$$
\begin{aligned}
\text{isotropic spreading }[P\text{ fixed; no loss}]:\quad
&I=\frac PS,&I_{\mathrm{sph}}&=\frac{P}{4\pi r^2},&I_1r_1^2&=I_2r_2^2,\\
&I_2=I_1\left(\frac{r_1}{r_2}\right)^2,&&r_2=r_1\sqrt{\frac{I_1}{I_2}}
\end{aligned}
$$
$$
\text{decibels:}\qquad \beta=(10\,\mathrm{dB})\log_{10}\!\frac I{I_0}\qquad I_0=10^{-12}\,\mathrm{W/m^2}\qquad I=I_0\,10^{\beta/(10\,\mathrm{dB})}\qquad \Delta\beta=(10\,\mathrm{dB})\log_{10}\!\frac{I_2}{I_1}
$$
$$
\begin{aligned}
\text{independent/incoherent:}\quad&I_{\mathrm{tot}}=\sum_iI_i,&\beta_{\mathrm{tot}}&=(10\,\mathrm{dB})\log_{10}\!\left[\sum_i10^{\beta_i/(10\,\mathrm{dB})}\right],\\
\text{equal sources:}\quad&\beta_N=\beta_1+(10\,\mathrm{dB})\log_{10}N,&2I&\Rightarrow+3.01\,\mathrm{dB},\quad10I\Rightarrow+10\,\mathrm{dB}
\end{aligned}
$$
$$
\begin{aligned}
\text{lossless tube }[\text{same full }P]:\quad
&I_{\mathrm{sph}}=\frac{P}{4\pi d^2},&I_{\mathrm{tube}}&=\frac{P}{\pi r^2},\\
&\frac{I_{\mathrm{tube}}}{I_{\mathrm{sph}}}=\left(\frac{2d}{r}\right)^2,&\beta_{\mathrm{tube}}&=\beta_{\mathrm{sph}}+(20\,\mathrm{dB})\log_{10}\!\frac{2d}{r}
\end{aligned}
$$
$$
\text{Doppler }[\text{LOS; medium speeds; }v_s<c_s]:\qquad \begin{array}{c|cc} & \text{toward }(f'>f_0) & \text{away }(f'<f_0) \\ \text{observer moves} & f'=f_0(1+v_o/c_s) & f'=f_0(1-v_o/c_s) \\ \text{source moves} & f'=f_0/(1-v_s/c_s) & f'=f_0/(1+v_s/c_s) \end{array}
$$
$$
\text{Doppler inverse:}\qquad \begin{array}{c|cc} & \text{toward} & \text{away} \\ \text{observer} & v_o=c_s(f'/f_0-1) & v_o=c_s(1-f'/f_0) \\ \text{source} & v_s=c_s(1-f_0/f') & v_s=c_s(f_0/f'-1) \end{array}
$$
$$
\text{echo }[\text{source approaches stationary wall head-on}]:\qquad f_1=f_0\frac{c_s}{c_s-v_s}\qquad f_{\mathrm{echo}}=f_1\frac{c_s+v_s}{c_s}=f_0\frac{c_s+v_s}{c_s-v_s}
$$
$$
\text{rotating source:}\qquad f_{\mathrm{rot}}=\frac{\mathrm{rpm}}{60}\qquad v_s=2\pi Rf_{\mathrm{rot}}\qquad f_{\mathrm{high}}=f_0\frac{c_s}{c_s-v_s}\qquad f_{\mathrm{low}}=f_0\frac{c_s}{c_s+v_s}
$$

**STANDING WAVES**

$$
\text{transverse-string reflection:}\qquad \text{fixed: }y_r=-y_i,\ \Delta\phi_{\mathrm{ref}}=\pi\qquad \text{free: }y_r=+y_i,\ \Delta\phi_{\mathrm{ref}}=0
$$
$$
\text{string displacement ends:}\qquad \text{fixed}=N_y\qquad \text{free}=A_y
$$
$$
\text{pipe boundaries:}\qquad \begin{array}{c|cc} & \text{displacement} & \text{pressure} \\ \text{closed} & N_y & A_p \\ \text{open} & A_y & N_p \end{array}\qquad \Delta x_{NN}=\Delta x_{AA}=\frac\lambda2\qquad \Delta x_{NA}=\frac\lambda4
$$
$$
\text{same-type ends }[\text{string FF; pipe OO/CC}]:\qquad \lambda_n=\frac{2L}{n}\qquad f_n=\frac{nv}{2L}=nf_1\qquad n=1,2,3,\ldots
$$
$$
\text{open--closed pipe:}\qquad \lambda_n=\frac{4L}{n}\qquad f_n=\frac{nv}{4L}=nf_1\qquad n=1,3,5,\ldots\qquad \frac{f_b}{f_a}=\frac ba
$$
$$
\text{fixed string modes:}\qquad f_n=\frac{n}{2L}\sqrt{\frac{F_T}{\mu}}=\frac n2\sqrt{\frac{F_T}{m_wL}}\qquad F_T=M_hg\Rightarrow f_n=\frac n2\sqrt{\frac{M_hg}{m_wL}}\qquad F_T=\frac{4m_wLf_n^2}{n^2}
$$
$$
\text{same-family shortcuts:}\qquad f=\frac{v}{2\Delta x_{NN}}=\frac{v}{2\Delta x_{AA}}\qquad f_{n,2}=\frac{n_2}{n_1}f_{n,1}\qquad f_{1,OO}=f_{1,OC}\Rightarrow L_{OC}=\frac{L_{OO}}2
$$

**SUPERPOSITION / INTERFERENCE**

$$
\text{coherent }[\text{same }f\text{, polarization}]:\qquad y_{\mathrm{tot}}=\sum_i y_i\qquad A_R=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\delta\phi}\qquad A_1=A_2=A\Rightarrow A_R=2A\left|\cos\frac{\delta\phi}{2}\right|
$$
$$
\text{geometry:}\qquad r_i=\sqrt{(x-x_i)^2+(y-y_i)^2}\qquad \delta r=r_2-r_1
$$
$$
\text{phase:}\qquad \delta\phi_0=\phi_{2,0}-\phi_{1,0}\qquad \delta\phi=\frac{2\pi\delta r}{\lambda}+\delta\phi_0\qquad \delta\phi_{\mathrm{eq}}=\delta\phi\bmod2\pi
$$
$$
\begin{aligned}
\delta\phi_0=0:\quad&C:\ |\delta r|=m\lambda,&D:\ |\delta r|&=\left(m+\frac12\right)\lambda,\\
\delta\phi_0=\pi:\quad&C:\ |\delta r|=\left(m+\frac12\right)\lambda,&D:\ |\delta r|&=m\lambda,\qquad m=0,1,2,\ldots
\end{aligned}
\qquad [D\text{ complete only if }A_1=A_2]
$$
$$
\text{in-phase }[A(0,0),B(0,-d),P(x>0,0)]:\qquad r_A=x\qquad r_B=\sqrt{x^2+d^2}\qquad r_B-r_A=m\lambda\qquad x_m=\frac{d^2-m^2\lambda^2}{2m\lambda}\quad(m=1,2,\ldots)
$$
$$
\text{first maximum }(x>0):\qquad m_*=\left\lceil\frac d\lambda\right\rceil-1\qquad m_*\ge1\qquad x_{\mathrm{first}}=x_{m_*}
$$

$$
g=9.81\,\mathrm{m/s^2}\qquad c_s=343\,\mathrm{m/s}\qquad c_0=3.0\times10^8\,\mathrm{m/s}
$$
