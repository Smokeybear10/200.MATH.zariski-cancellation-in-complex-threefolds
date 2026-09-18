# The two square-completion gates for the square-root leading ratio

Status: bounded working differential classification. For the leading ratio
\(q^2=t\), the two necessary square-completion equations have solutions,
unlike the equations for the rational split ratio treated in194.
Their complete nondegenerate solution list over any exact finite
coefficient field is
\[
f=a t+bq\quad(a\in\mathbb C,\ b\in\mathbb C^*),
\qquad\text{or}\qquad
f=b/q\quad(b\in\mathbb C^*).
\tag{1}
\]
Here \(f=1/R\). This classifies two necessary differential equations,
not the actual polynomial frames. In particular (1) does not supply
lower potentials, all scalar-Jacobian coefficients, or an original-ring
coordinate inverse.

## 1. Actual context and the conditional square-form input

The positive-rank normal form under consideration is the full initial
kernel
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\ker\bigl(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W
 \longmapsto(a_E\eta,b_E\eta,e_E\eta^2,h_E\eta^2)\bigr)
 =(\mathsf Z^2-\mathsf X^3\mathsf Y).
\end{gathered}
\tag{2}
\]
Here \(a_E=EX,\ b_E=EY,\ e_E=E^2Z/2,\ h_E=E^2W/2\);
\(\eta\) is the independent initial-algebra variable.
The four generators are actual polynomial coordinates and the displayed
ideal is the full initial kernel, not merely one vanishing relation.
The actual degree-preserving normalizations in
[positive-rank184](weight-four-positive-bad-rank-normal-forms-pass184-working.md)
include this absent-\(W\) repeated-root case.

The occurring \(Z\) pivot of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
gives the exact coefficient field \(L\), its commuting partials in
\(t=b_E/a_E,\rho=h_E/a_E^2\), and
\[
q=e_E/a_E^2,\qquad q^2=t,\qquad
[L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\qquad [K:\mathbb C(t)]<\infty.
\tag{3}
\]
In particular \(q\in K\). Primes denote the unique extension of
\(d/dt\) to \(K\); its constants are \(\mathbb C\). The field is not
assumed rational. The original global slice \(u\) in (2) is unrelated
to \(q\), which will be the rational parameter for the calculation.

To explain the application precisely, assume additionally that the
nonzero-\(R\) square-completion branch has been reached:
\[
\begin{gathered}
R=k_\rho\in K^*,\qquad k=R\rho+k_0,\qquad
n=\nu\rho^2/2+s_0\rho+n_0,\quad \nu\in K^*,\\
\mathcal H=\mathcal A(V-P(U))^2+B_1U+B_0,\qquad
P=p_2U^2+p_{1,\mathrm{full}}U+p_0,\qquad
\mathcal A p_2\ne0.
\end{gathered}
\tag{4}
\]
The other coefficients initially belong to the exact fields indicated
by the universal chart. The present note does not prove that every
frame (2) reaches (4), nor that every solution of its necessary equations
is realized by a frame.

For clarity, the coefficient comparisons giving the first differential
gate use only \(q\in K\), not rationality of \(q\). Set
\[
d=q'''/6,\quad e=d'/4,\quad
\Delta=RR''/2-(R')^2,\quad C_4=eR-dR'.
\]
The universal potentials, exactly as in Section 1 of
[coefficient192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md),
give
\[
\begin{gathered}
\mathcal A=R\nu/2,\qquad p_2=-\Delta/(R\nu),\qquad
C_4=\Delta^2/(2R\nu)\ne0,\\
\frac{RR'''}6-\frac{R'R''}2-d\nu
 =\Delta\left(\frac{\nu'}{\nu}-\frac{2R'}R\right).
\end{gathered}
\tag{5}
\]
These follow by comparing \(V^2,U^2V,U^4,U^3\) and differentiating
the last comparison in \(\rho\). All operations are coefficient
derivatives before evaluating \(U,V\). Thus the same derivation applies
to the algebraic \(q\) in (3).

## 2. The exact pair of differential equations

Write \(f=1/R\), and impose the nonzero gates \(f f''D\ne0\), where
\[
\begin{gathered}
d=\frac1{16q^5},\qquad
D=d'f/4+df',\qquad
\Delta=-\frac{f''}{2f^3},\qquad
\nu=\frac{(f'')^2}{8f^3D},\\
p_2=-\frac{\Delta}{R\nu},\qquad
p=\frac{2R'}R-\frac{\nu'}{\nu}.
\end{gathered}
\tag{6}
\]
The symbol \(p\) is the coefficient of \(\rho\) in
\(p_{1,\mathrm{full}}\), not that entire coefficient.
The last equation in (5), after multiplication by the nonzero element
\(24f^3D\), is equivalent to
\[
\mathscr E(f)=20Df'''-3d(f'')^2-12f''D'=0.
\tag{7}
\]
The same coefficient and scalar-Jacobian argument in
[square-Jacobian193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
is written for general \(q\in K\). It supplies the second gate
\[
\begin{aligned}
L_3&=\frac{R\nu''/4-R'\nu'/2-\nu R''/2
                     -R\nu p^2/2-\nu^2p_2}{3Rp_2},\\
J_3&=-RL_3'+R'L_3-\nu\nu'/2-p(3RL_3+\nu^2)=0.
\end{aligned}
\tag{8}
\]
Here \(L_3=[\rho^3]\ell\). In an actual square branch the remaining
linear term \(B_1\) is \(\rho\)-constant, and (8) is its cubic
\(\rho\)-coefficient. The scalar determinant and whole-line hypotheses
used for that assertion remain separate geometric inputs.

The theorem proved below is purely differential: for any finite
\(K/\mathbb C(t)\) containing \(q\) with \(q^2=t\), equations (7)--(8)
and \(f f''D\ne0\) hold exactly for the list (1).

## 3. Eliminate the third derivative using the first equation

Let
\[
\delta=t\partial_t,\qquad
x=\frac{tf'}f,\qquad y=\frac{t^2f''}f,\qquad H=8x-5.
\tag{9}
\]
The nonzero gates give \(yH\ne0\). Indeed
\[
D=\frac{dfH}{8t},\qquad
\nu=\frac{16y^2}{f^2qH},\qquad
p_2=\frac{fH}{32yq^3}.
\]
Since \(d'/d=-5/(2t)\), equation (7) is equivalent to
\[
f'''=\frac{3f''(7f-10tf'+4t^2f'')}
                 {2t(-5f+8tf')}.
\tag{10}
\]
In logarithmic coordinates this gives the two rational derivative rules
\[
\delta x=y-x^2+x,\qquad
\delta y=\frac{y(12y-16x^2+12x+1)}{2H}.
\tag{11}
\]
No new independent variables or rationality assertion about \(K\) is
implicit here: (11) is a pair of identities for the two elements (9).

Put \(P=tp\). Differentiating \(\nu\) from (6), using (10), gives
\[
P=\frac{16x^2-8y-7}{2H},\qquad
\delta\log\nu=-2x-P.
\tag{12}
\]
Logarithmic derivative notation only means a quotient of derivatives;
no logarithm is adjoined to the field.

## 4. An explicit factorization of the second gate

Define the rational expression
\[
\begin{aligned}
S&=-2y-2x^2-\delta P+2xP-P^2+P\\
 &=-\frac{3(256x^2y-24x^2-320xy+28x+
                   32y^2+112y-7)}{4H^2}.
\end{aligned}
\tag{13}
\]
In evaluating \(\delta P\), use the two rules (11). Substitution in
(8), or direct grouping of its five numerator terms, gives
\[
L_3=\frac{\nu S}{12p_2t^2}.
\]
For an explicit check of this grouping, write
\(n=\delta\log\nu=-2x-P\). Four times the coefficient of
\(R\nu/t^2\) in the numerator defining \(L_3\) is
\[
\delta n+n^2-n+2xn-4x^2-2P^2.
\]
The two contributions involving \(y\) from
\(-\nu R''/2\) and \(-\nu^2p_2\) cancel here.
Replacing \(\delta x\) by (11) yields exactly \(S\).

The identities
\(\nu p_2=y/(2ft^2)\) and (12) now reduce the second gate to
\[
J_3=\frac{R\nu}{12p_2t^3}
 \left\{-\delta S+
 S\left(2x-P+\frac{\delta y}{y}\right)+6xy-3yP\right\}.
\]
All entries in braces are rational in \(x,y\), using (11).
Multiplying by \(H^3\) and collecting gives the exact identity
\[
-\delta S+
 S\left(2x-P+\frac{\delta y}{y}\right)+6xy-3yP
 =-\frac{21(x-2y-1)^2(4x+4y-1)}{H^3}.
\tag{14}
\]
For example, (13) and (11) verify (14) by the ordinary quotient rule;
there is no use of an additional differential equation at this step.
Equivalently, back in the original jets, the result is
\[
\boxed{
-\frac{896(f'')^3t^4
 (-f+4tf'+4t^2f'')
 (f-tf'+2t^2f'')^2}
 {f^5(-5f+8tf')^5}
=J_3.}
\tag{15}
\]
Formula (15) is an identity under the first gate (7).
Every divided factor is nonzero by (6) and (9).
Consequently the two gates force at least one of the Euler equations
\[
4t^2f''+4tf'-f=0
\qquad\text{or}\qquad
2t^2f''-tf'+f=0.
\tag{16}
\]

## 5. Solve the Euler equations inside the exact field

No analytic expansion or assumption \(K=\mathbb C(t)\) is needed.
Because \(q'=1/(2q)\), in the first case of (16) the two elements
\[
a=\frac{f+2tf'}{2q},\qquad
b=\frac q2(f-2tf')
\]
have derivative zero. They are therefore complex constants, and
\(f=aq+b/q\). Substitution into (7), with
\(\partial_t=(2q)^{-1}\partial_q\), gives
\[
\mathscr E(aq+b/q)=\frac{15ab}{32q^{13}}.
\tag{17}
\]
Thus \(ab=0\). The nonzero gates leave the two nonzero monomials
\(f=aq\) and \(f=b/q\).

In the second case of (16), the derivative-zero elements are
\[
a=\frac{2tf'-f}{t},\qquad
b=\frac{2(f-tf')}{q}.
\]
Hence \(f=at+bq\), with \(a,b\in\mathbb C\).
Its second derivative is \(-b/(4q^3)\), so the gate \(f''\ne0\)
is exactly \(b\ne0\). Direct differentiation gives
\[
D=\frac{3aq-b}{128q^6},\qquad
f''=-\frac b{4q^3},\qquad f'''=\frac{3b}{8q^5},
\qquad \mathscr E(at+bq)=0.
\tag{18}
\]
The numerator \(3aq-b\) cannot vanish identically for \(b\ne0\),
because \(q\) is transcendental over \(\mathbb C\).
Thus every member of this family has all the required nonzero gates.
It satisfies the second Euler equation, so (15) gives \(J_3=0\).
The other family \(f=b/q\) likewise satisfies (7), the first Euler
equation and all the gates. This proves both directions of (1).

The assertion about derivative constants used here is elementary in
the stated finite field. If an element with zero derivative were
transcendental over \(\mathbb C\), its nonzero separable differential
would contradict that \(\Omega_{K/\mathbb C}\) is one-dimensional
and detected by \(\partial_t\). Equivalently one can differentiate
its monic minimal polynomial over \(\mathbb C(t)\), whose normalized
coefficients must be constant. Algebraicity over the algebraically
closed field \(\mathbb C\) then makes the element complex.

## 6. Exact monomial controls and the remaining actual problem

At \(f=q\), the quantities in (6)--(8) are
\[
\begin{gathered}
R=q^{-1},\quad D=-1/(128q^6),\quad
\nu=-q^{-3},\quad \Delta=1/(8q^6),\\
p_2=1/(8q^2),\quad p=1/(2q^2),\quad
L_3=-1/(2q^5).
\end{gathered}
\tag{19}
\]
The four summands of \(J_3\) are respectively
\((-5,1,3,1)/(4q^8)\), and hence sum to zero.
At \(f=q^{-1}\) they are
\[
\begin{gathered}
R=q,\quad D=-9/(128q^8),\quad
\nu=-q,\quad \Delta=-3/(8q^2),\\
p_2=-3/(8q^4),\quad p=1/(2q^2),\quad L_3=-q/2.
\end{gathered}
\tag{20}
\]
The four summands are \((1,-1,-1,1)/4\).
Thus neither monomial is rejected by the second gate, and (18)
shows why checking only those two monomials would miss a whole family.

For possible subsequent coefficient analysis, the full first family
has the exact nondegenerate values
\[
\begin{gathered}
f=q(aq+b),\qquad
\nu=\frac{b^2}{q^3(aq+b)^3(3aq-b)},\qquad
\Delta=\frac{b}{8q^6(aq+b)^3},\\
p_2=-\frac{(aq+b)(3aq-b)}{8bq^2},\qquad
p=\frac{9a^2q^2+4abq-b^2}
         {2q^2(aq+b)(3aq-b)}.
\end{gathered}
\tag{21}
\]
These are elements of \(\mathbb C(q)\), although the ambient exact
coefficient field may still be larger. The theorem proves rationality
of these displayed coefficients, not rationality of that entire field.

In an actual frame, (1) is a restriction on a square branch satisfying
(4). It does not construct \(k_0,s_0,n_0,\ell,m\), prove the whole-line
and actual-field-return conditions for any proposed data, control every
coefficient of the scalar Jacobian, or turn a generic parameter into
an original polynomial coordinate. No actual realization or exclusion
of the surviving families is claimed. The pure-quartic alternative,
constant projected coordinates, and any prior reduction to (4) are
separate obligations.

This note preserves every earlier source. A read-only, unsaved rational
calculation checked the elementary factorization (14); no saved checker
was executed, imported or compiled. The formulas above retain a complete
written derivation and their exact nonzero hypotheses. They are not
formal verification, human expert certification, or a historical novelty
claim, and do not settle unrestricted cancellation or arbitrary entry.
