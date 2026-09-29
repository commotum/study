# SEQUENCES & SERIES — KEY FORMULAS

## Sequences

$$
a_n=f(n)
\qquad
a_1=f(1),\ a_2=f(2),\ldots
$$

$$
\text{Arithmetic:}
\qquad
a_n=a_1+(n-1)d
\qquad
d=a_{n+1}-a_n
$$

$$
\text{Geometric:}
\qquad
a_n=a_1r^{n-1}
\qquad
r=\frac{a_{n+1}}{a_n}
$$

$$
(-1)^n=-1,1,-1,1,\ldots
\qquad
(-1)^{n+1}=1,-1,1,-1,\ldots
$$

$$
\text{Recursive:}
\qquad
a_{n+1}=f(a_n)
\qquad
a_n\to L\Longrightarrow L=f(L)
$$

## Partial Sums and Series

$$
S_N=\sum_{n=m}^{N}a_n
\qquad
\sum_{n=m}^{\infty}a_n=\lim_{N\to\infty}S_N
$$

$$
\sum_{k=1}^{N}k=\frac{N(N+1)}{2}
$$

$$
S_N^{\text{arith}}
=
\frac{N}{2}(a_1+a_N)
=
\frac{N}{2}\left[2a_1+(N-1)d\right]
$$

$$
S_N^{\text{geom}}
=
a\frac{1-r^N}{1-r},
\qquad
r\ne1
$$

## Infinite Geometric Series

$$
\sum_{n=0}^{\infty}ar^n
=
\frac{a}{1-r},
\qquad
|r|<1
$$

$$
\sum_{n=1}^{\infty}ar^{n-1}
=
\frac{a}{1-r},
\qquad
|r|<1
$$

$$
\sum_{n=m}^{\infty}r^n
=
\frac{r^m}{1-r},
\qquad
|r|<1
$$

$$
|r|<1\Longrightarrow\text{converges}
\qquad
|r|\ge1\Longrightarrow\text{diverges}
$$

## Divergence Test

$$
\sum a_n\text{ converges}
\Longrightarrow
\lim_{n\to\infty}a_n=0
$$

$$
\lim_{n\to\infty}a_n\ne0
\Longrightarrow
\sum a_n\text{ diverges}
$$

$$
\lim_{n\to\infty}a_n=0
\quad\text{does not guarantee convergence}
$$

## Harmonic and \(p\)-Series

$$
\sum_{n=1}^{\infty}\frac{1}{n^p}
=
\begin{cases}
\text{convergent}, & p>1,\\
\text{divergent}, & p\le1
\end{cases}
$$

$$
\sum_{n=1}^{\infty}\frac1n
\text{ diverges}
$$

$$
H_N=\sum_{n=1}^{N}\frac1n
\approx
\ln N+\gamma
\qquad
\gamma\approx0.57721
$$

## Telescoping Series

$$
\sum_{n=m}^{N}(b_n-b_{n+1})
=
b_m-b_{N+1}
$$

$$
\sum_{n=m}^{\infty}(b_n-b_{n+1})
=
b_m-\lim_{N\to\infty}b_{N+1}
$$

$$
\frac{1}{(n+a)(n+b)}
=
\frac{1}{b-a}
\left(
\frac{1}{n+a}-\frac{1}{n+b}
\right)
$$

$$
\frac{1}{(n+1)(n+2)}
=
\frac{1}{n+1}-\frac{1}{n+2}
$$

$$
\sum_{n=2}^{N}
\left(
\frac{1}{n-1}-\frac{1}{n}
\right)
=
1-\frac1N
$$

## Logarithmic Series

$$
\sum_{n=1}^{\infty}\frac{x^n}{n}
=
-\ln(1-x),
\qquad
|x|<1
$$

$$
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}
=
\ln2
$$

$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
=
-\ln2
$$

## Repeating Decimals

$$
0.\overline{B}
=
\frac{B}{10^d-1}
$$

$$
d=\text{number of repeating digits}
$$

$$
0.\overline{a}=\frac{a}{9}
\qquad
0.\overline{ab}=\frac{ab}{99}
\qquad
0.\overline{abc}=\frac{abc}{999}
$$

## Standard Sequence Limits

$$
\lim_{n\to\infty}\frac{1}{n^p}=0,
\qquad
p>0
$$

$$
\lim_{n\to\infty}r^n
=
\begin{cases}
0, & |r|<1,\\
1, & r=1,\\
\infty, & r>1,\\
DNE, & r\le-1\text{ with oscillation}
\end{cases}
$$

$$
\lim_{n\to\infty}
\frac{a_mn^m+\cdots}{b_kn^k+\cdots}
=
\begin{cases}
0, & m<k,\\[2mm]
\frac{a_m}{b_k}, & m=k,\\[2mm]
\pm\infty\text{ or }DNE, & m>k
\end{cases}
$$

$$
c^n\gg n^p\gg\ln n,
\qquad
c>1,\ p>0
$$

## Standard Trigonometric and Logarithmic Limits

$$
\lim_{x\to0}\frac{\sin x}{x}=1
\qquad
\sin x\sim x
$$

$$
\lim_{x\to0}\frac{\ln(1+x)}{x}=1
\qquad
\ln(1+x)\sim x
$$

$$
\lim_{n\to\infty}\sin\left(\frac{c}{n}\right)=0
$$

## The Number \(e\)

$$
\lim_{n\to\infty}
\left(1+\frac1n\right)^n
=
e
$$

$$
\lim_{n\to\infty}
\left(1+\frac{c}{n}\right)^n
=
e^c
$$

$$
\lim_{n\to\infty}
\left(1+\frac{c}{n}\right)^{kn}
=
e^{ck}
$$

## Logarithm Rules

$$
\ln(ab)=\ln a+\ln b
$$

$$
\ln\left(\frac{a}{b}\right)=\ln a-\ln b
$$

$$
\ln(a^p)=p\ln a
$$

$$
\ln1=0
\qquad
\ln e=1
$$

## Monotonicity Tests

$$
a_{n+1}-a_n
\begin{cases}
>0 & \Longrightarrow\text{increasing},\\
\ge0 & \Longrightarrow\text{nondecreasing},\\
<0 & \Longrightarrow\text{decreasing},\\
\le0 & \Longrightarrow\text{nonincreasing}
\end{cases}
$$

$$
a_n>0:
\qquad
\frac{a_{n+1}}{a_n}
\begin{cases}
>1 & \Longrightarrow\text{increasing},\\
<1 & \Longrightarrow\text{decreasing}
\end{cases}
$$

$$
a_n=f(n):
\qquad
f'(x)
\begin{cases}
>0 & \Longrightarrow\text{increasing},\\
<0 & \Longrightarrow\text{decreasing}
\end{cases}
$$

## Boundedness and Monotone Convergence

$$
m\le a_n\le M
\Longrightarrow
\{a_n\}\text{ is bounded}
$$

$$
\text{Increasing and bounded above}
\Longrightarrow
\text{convergent}
$$

$$
\text{Decreasing and bounded below}
\Longrightarrow
\text{convergent}
$$

$$
\text{Monotonic and unbounded}
\Longrightarrow
\text{divergent}
$$

## Exponential Decay Models

$$
P_n=Pr^{n-1}
$$

$$
P_{\text{total}}
=
\frac{P}{1-r},
\qquad
0<r<1
$$

$$
Pr^{n-1}<T
$$

$$
n-1>
\frac{\ln(T/P)}{\ln r},
\qquad
0<r<1
$$

## Useful Algebra

$$
(n+1)!=(n+1)n!
$$

$$
\frac{a^n}{b^n}
=
\left(\frac{a}{b}\right)^n
$$

$$
\sqrt{n^2}=|n|
\qquad
n>0\Longrightarrow\sqrt{n^2}=n
$$

$$
x+x^2+x^3+\cdots
=
\frac{x}{1-x},
\qquad
|x|<1
$$