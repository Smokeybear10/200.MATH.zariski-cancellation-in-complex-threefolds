# A nonaffine rational solution in the next split-form coefficient equation

Status: working negative result about a proposed proof extension.
The affine-solution conclusion used for \(q=t^4\) does not extend to
\(q=-t^3-t^{-1}\). An explicit rational function satisfies the correct
new necessary equation and all of its nonzero denominator gates.
This is not an actual polynomial frame or a cancellation counterexample.

The purpose is to keep the nonzero-R quadratic-projection alternatives
open until their remaining equations and actual inverse are analyzed.
The separate zero-R work is unaffected.

## 1. The necessary coefficient equation before specializing q

Let \(q\in\mathbb C(t)\), with \(q'''\ne0\), and put
\[
d=q'''/6,\qquad e=q''''/24=d'/4.
\tag{1}
\]
Work in an exact finite algebraic coefficient field as in
[universal chart184](weight-four-universal-chart-potentials-pass184-working.md).
For this calculation assume \(R=k_\rho\ne0\) and \(R_\rho=0\).
Write \(K=\ker_L\partial_\rho\), so \(R\in K^*\) and
\(k=R\rho+k_0\), with \(k_0\in K\). Primes on \(K\) mean the
\(t\)-derivative, while the displayed coefficient partials on \(L\)
are taken before evaluating the independent variables \(U,V\).

The generic bad-linear potentials give
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=eU^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
 +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
 +(R'U+n_\rho)(\ell-S).
\end{aligned}
\tag{2}
\]
These are the same exact formal potentials as in the
[quartic-graph reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md),
with its particular \(d=4t,e=1\) replaced by (1).
The calculation below is conditional on this coefficient setup;
it does not itself prove that all split charts have \(R_\rho=0\).

Writing \(s=n_\rho\), direct coefficient extraction gives
\[
\begin{gathered}
[V^2]\mathcal H=Rn_{\rho\rho}/2,\qquad
[V]\mathcal H=\Delta U^2+(Rn_{t\rho}-2R's)U-R\ell_\rho-s^2,\\
\Delta=RR''/2-(R')^2,\qquad
C_4=[U^4]\mathcal H=eR-dR',\\
C_3=[U^3V^0]\mathcal H
 =Rk_{ttt}/6-R'k_{tt}/2-ds .
\end{gathered}
\tag{3}
\]

Consider precisely the nondegenerate square-completion alternative
\[
\mathcal H=A(V-P(U))^2+B_1U+B_0,\quad
P=p_2U^2+p_1U+p_0,\quad A,p_2\ne0.
\tag{4}
\]
All coefficients in (4) initially lie in \(L\).
This form includes the two quadratic alternatives discussed in189;
it is not asserted that they actually occur in a split chart.

Put \(N_2=n_{\rho\rho}\).
Comparing the \(V^2,U^2V,UV,U^4,U^3\) coefficients in order gives
\[
\begin{gathered}
A=RN_2/2,\quad p_2=-\Delta/(RN_2),\quad
p_1=-(Rn_{t\rho}-2R's)/(RN_2),\\
C_4=\Delta^2/(2RN_2)\ne0,\qquad
N_2=\Delta^2/(2RC_4)\in K^*,\qquad \Delta\ne0,\\
C_3=\frac{\Delta(Rn_{t\rho}-2R's)}{RN_2}.
\end{gathered}
\tag{5}
\]
These nonzero gates precede every division below.
Because \(N_2\in K\), primitive subtraction in \(\rho\) writes
\(n=N_2\rho^2/2+s_0\rho+n_0\), with \(s_0,n_0\in K\).
Differentiating the last equation in (5) in \(\rho\) yields
\[
\frac{RR'''}6-\frac{R'R''}2-dN_2
 =\Delta\left(\frac{N_2'}{N_2}-\frac{2R'}R\right).
\tag{6}
\]
In deriving the left side, \(k_{ttt,\rho}=R'''\) and
\(n_{\rho\rho}=N_2\); on the right side, \(R,\Delta,N_2\) are
\(\rho\)-constant. No rationality assumption on \(K\) is used.

## 2. Exact reciprocal form and the new ODE

Set \(f=1/R\) and \(D=ef+df'\). Equations (3)--(5) become
\[
\Delta=-\frac{f''}{2f^3},\qquad C_4=\frac{D}{f^2},\qquad
N_2=\frac{(f'')^2}{8f^3D},\qquad f,f'',D\ne0.
\tag{7}
\]
The needed derivative identities are
\[
\frac{N_2'}{N_2}=\frac{2f'''}{f''}-\frac{3f'}f-\frac{D'}D,\qquad
\frac{RR'''}6-\frac{R'R''}2
 =\frac{f'f''}{2f^4}-\frac{f'''}{6f^3}.
\tag{8}
\]
Subtracting the right side of (6) from its left side and multiplying
by the nonzero field element \(24f^3D\) gives exactly
\[
\boxed{\mathscr E_d(f):=
20Df'''-3d(f'')^2-12f''D'=0.}
\tag{9}
\]
Thus (9) is equivalent to (6) under the gates (7), not merely a
condition obtained by multiplying by a potentially zero factor.
Since
\(D'=d''f/4+5d'f'/4+df''\), it can also be written
\[
5(d'f+4df')f'''-15d(f'')^2-15d'f'f''-3d''ff''=0.
\tag{10}
\]

For the earlier \(q=t^4\), one has \(d=4t,e=1,D=f+4tf'\).
Equation (9) is then exactly twenty times
\[
(f+4tf')f'''-3f'f''-3t(f'')^2=0.
\tag{11}
\]
The algebraic-solution lemma in189 applies to this particular
equation and excludes its square-completion cases. Nothing in that
lemma permits replacing \(d\) while retaining the same conclusion.

## 3. A nonaffine rational solution for the split form

For the next split leading relation
\(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4\), the
coefficient chart has
\[
q=-t^3-t^{-1},\quad d=t^{-4}-1,\quad e=-t^{-5}.
\tag{12}
\]
Take
\[
f=t^5+3t,\quad
f'=5t^4+3,\quad f''=20t^3,\quad f'''=60t^2,\quad
D=ef+df'=1-5t^4,\quad D'=-20t^3.
\tag{13}
\]
This \(f\) is a rational function and is not affine.
The three terms of (9) are respectively
\[
\begin{aligned}
20Df'''&=1200t^2-6000t^6,\\
-3d(f'')^2&=-1200t^2+1200t^6,\\
-12f''D'&=4800t^6 .
\end{aligned}
\tag{14}
\]
They sum to zero identically, not just at finitely many values of
\(t\). All the field elements required nonzero in (7) are indeed
nonzero. More explicitly,
\[
\begin{gathered}
R=\frac1{t(t^4+3)},\qquad
\Delta=-\frac{10}{(t^4+3)^3},\\
C_4=\frac{1-5t^4}{t^2(t^4+3)^2},\qquad
N_2=\frac{50t^3}{(t^4+3)^3(1-5t^4)} .
\end{gathered}
\tag{15}
\]
Consequently this solution also satisfies the undivided rational
identity (6) with \(N_2\) from (15). It was not introduced by
clearing a factor that vanishes identically.

The poles at individual complex values of \(t\) are permitted in
the coefficient field. That observation does not make any of
their denominators units of the original polynomial ring.
A later actual-coordinate argument would have to handle them.

## 4. Exact consequence and the remaining proof obligation

The general statement
“every nonzero algebraic solution of the square-completion
equation is affine” is false when that equation is (9) with
\(d=t^{-4}-1\). The candidate (13) is an exact counterexample
to that attempted extension.

It is not a counterexample to the lemma actually proved in189:
that lemma has \(d=4t\). It is also not a counterexample to
cancellation, an example of an actual quadratic projected graph,
or a solution of all the remaining coefficient equations.
We have not supplied compatible \(k_0,s_0,n_0,\ell,m\), the full
evaluated unit cofactor, or the original polynomial inverse.

The next nonzero-R step must examine those extra constraints, or
find a different obstruction. In particular, the two quadratic
alternatives may not be discarded using the earlier affine
algebraic-function lemma. The zero-R regular-differential and
pole-order lemmas in
[split coefficient lemmas191](weight-four-split-coefficient-ode-lemmas-pass191-working.md)
address different equations and are not contradicted.

This note is separate from the frozen190 recognition packet.
It records a negative result about a proof route, not historical
novelty, expert review, formal certification or a public claim.

