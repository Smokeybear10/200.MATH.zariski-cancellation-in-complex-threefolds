# Recognition from an actual normalized suspension in every degree

An actual invariant of the form \(XW-F(Y)-\delta Z\), with
\(\deg F\ge3\) and \(\delta\ne0\), forces the distinguished good
speed to be constant under the derivative bounds below and
fixed-point freeness. The invariant kernel and its polynomial
straightening are explicit. In the dense case the selected primitive
intrinsic action also has a global slice.

This extends the normalized cubic calculation132 to arbitrary degree.
The corrected invariant is an explicit hypothesis. A relation among
the leading speeds does not supply it, and this note does not prove
the correction step or arbitrary three-good coordinate entry.

## 1. Exact statement and the actual coordinate reduction

Let \(m\ge2\), and assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}_{\mathbb C}(B),
\qquad E(B)B=B,\\
E^2X=E^2Y=E^2Z=0,\qquad E^{m+1}W=0,\qquad s=EX\ne0,\\
I=XW-F(Y)-\delta Z\in\ker E,\qquad
F(T)=\gamma T^{m+1}+\text{lower terms},\qquad
\gamma,\delta\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The four displayed generators are actual polynomial coordinates.
Fixed-point freeness in (1) means the displayed coefficient-ideal
condition; a global slice is sufficient. No speed-rank or density
assumption is needed until Section 6.

The conclusion is \(s\in\mathbb C^*\), \(t:=EY\in\mathbb C[I]\),
and \(B=\mathbb C[I,V,J,X]\) with \(E=s\partial_X\) in the
explicit coordinates of Section 5. In particular \(\ker E\) is
a polynomial three-ring.

The inverse
\(Z=(XW-F(Y)-I)/\delta\) gives
\(B=\mathbb C[I,X,Y,W]\) before any localization.
Thus \(I\) is a genuine coordinate and \(K=\mathbb C(I)\) is
a coefficient field on \(B_K=K[X,Y,W]\).
The derivation fixes \(K\), remains nonzero and locally nilpotent,
and remains fixed-point free. Indeed its coefficient ideal in this
presentation is \((s,t,EW)\), which is the unit ideal by (1).
Its extension to \(B_K\) is therefore irreducible.

## 2. Backward differentiation gives the entire bad speed

Put \(R_W=EW\). Since \(Es=Et=0\), differentiating \(EI=0\)
gives, for every \(2\le k\le m+1\),
\[
\begin{gathered}
k s E^{k-1}W+X E^kW=F^{(k)}(Y)t^k,\\
sE^mW=m!\gamma t^{m+1}.
\end{gathered}
\tag{2}
\]
The term from \(Z\) vanishes for these indices. Starting with
\(k=m+1\), where \(E^{m+1}W=0\), and substituting backward
down to \(k=2\) yields
\[
R_W=
\sum_{j=0}^{m-1}
\frac{(-X)^j F^{(j+2)}(Y)t^{j+2}}
     {(j+2)!\,s^{j+1}} .
\tag{3}
\]
For example the first two terms are
\(F''(Y)t^2/(2s)-XF'''(Y)t^3/(6s^2)\).
The product of the successive integers \(2,\ldots,j+2\)
explains the factorial. Equation (3) initially takes place in
\(\operatorname{Frac}B\); its left side is the original polynomial
coefficient. No denominator has been declared a unit in \(B\).

## 3. Wang's two alternatives apply over the exact field

Dasgupta--Gupta, Theorem 4.1, states Wang's classification for a
nonzero irreducible LND on a three-variable polynomial ring over
any characteristic-zero field when two displayed variables have
zero second derivative. Its cases retain the third original
variable in the first alternative and the first two in the
second.[^1] Apply it to \(B_K=K[X,Y,W]\), where the required
coordinate presentation and irreducibility were proved above.

In the first alternative there is a nonzero invariant \(K\)-linear
form in \(X,Y\). Its \(Y\) coefficient is nonzero because \(s\ne0\).
Hence \(t=\kappa s\) for \(\kappa\in K\), and (3) becomes
\[
R_W=s\sum_{j=0}^{m-1}
\frac{(-X)^jF^{(j+2)}(Y)\kappa^{j+2}}{(j+2)!}.
\tag{4}
\]
Thus \(s\) divides all three coefficients \(s,t,R_W\) in
\(B_K\). Irreducibility gives \(s\in K^*\), and then \(t\in K\).
This includes \(t=0\).

In the second alternative there is an invariant coordinate \(V_0\)
with \(B_K=K[V_0,X,Y]\) and \(s,t\in K[V_0]\).
Because the coordinate change retains \(X,Y\), comparison of
degrees in the remaining variable and its polynomial inverse gives
\[
\begin{gathered}
V_0=\lambda W+P(X,Y),\qquad
\lambda\in K^*,\quad P\in K[X,Y],\qquad
\gcd_{K[V_0]}(s,t)=1,\\
\lambda E^mW
=-\sum_{j=0}^{m}\binom mj
s^{m-j}t^j
\frac{\partial^mP}{\partial X^{m-j}\partial Y^j}.
\end{gathered}
\tag{5}
\]
The gcd assertion follows from irreducibility in these coordinates:
the remaining coefficient \(EV_0\) is zero. Equation (2) gives
\(s\mid t^{m+1}\), so \(s\in K^*\).
If \(d=\deg_{V_0}t>0\), the right side of (5) has
\(V_0\)-degree at most \(md\), whereas its left side, by (2),
has degree \((m+1)d\). This is impossible. Hence \(t\in K\).
If \(t=0\), the same conclusion is immediate.

Both alternatives give \(s,t\in B\cap K=\mathbb C[I]\).
This intersection uses the actual presentation
\(\mathbb C[I,X,Y,W]\), not an unspecified invariant-field model.

## 4. Every zero of the distinguished speed would give fixed points

If \(t=0\), equation (3) gives \(R_W=0\), and the only nonzero
coefficient in coordinates \(I,X,Y,W\) is \(s\).
Fixed-point freeness therefore makes \(s\) a complex unit.

Assume \(t\ne0\). Distinct summands in (3) have distinct \(X\)
powers. For each \(j\), the leading \(Y^{m-1-j}\) coefficient
of \(F^{(j+2)}(Y)\) is a nonzero complex number. Comparing these
individual coordinate monomials gives
\[
s,t\in\mathbb C[I],\qquad
B_j:=\frac{t^{j+2}}{s^{j+1}}\in\mathbb C[I]
\quad(0\le j\le m-1).
\tag{6}
\]
Let \(p=I-\lambda_0\) divide \(s\), and write
\(e=\operatorname{ord}_p s>0\),
\(f=\operatorname{ord}_p t\).
The last coefficient in (6) gives
\[
\begin{gathered}
(m+1)f-me\ge0,\qquad f>0,\\
\operatorname{ord}_p B_j
=(j+2)f-(j+1)e
\ \ge\ \frac{m-j-1}{m+1}e>0
\quad(0\le j\le m-2),\\
(s,t,R_W)\subset (p,X)\mathbb C[I,X,Y,W].
\end{gathered}
\tag{7}
\]
For the last inclusion, all earlier summands of (3) vanish
modulo \(p\), and the remaining summand is divisible by
\(X^{m-1}\). This power lies in \((X)\) because \(m\ge2\).
The ideal \((p,X)\) is proper, contradicting fixed-point freeness.
Thus \(s\) has no root and \(s=c\in\mathbb C^*\).

This is the all-degree version of the cubic divisor argument132.[^2]
Its crucial polynomial coefficient comparison became valid only
after the actual invariant presentation put \(s,t\) in
\(\mathbb C[I]\). The leading relation in (2) by itself does not
justify that step. The restriction \(m\ge2\) is also used exactly
in the last line of (7).

## 5. Explicit polynomial straightening

Set \(\eta=t/c\in\mathbb C[I]\), and define
\[
\begin{gathered}
V=Y-\eta(I)X,\\
\mathcal S(I,V,X)=
\sum_{k=2}^{m+1}
\frac{\eta(I)^k F^{(k)}(V)}{k!}\,X^{k-1},\qquad
J=W-\mathcal S(I,V,X).
\end{gathered}
\tag{8}
\]
All three expressions are polynomials. The inverse is
\[
\begin{gathered}
Y=V+\eta(I)X,\qquad
W=J+\mathcal S(I,V,X),\qquad
Z=(XW-F(Y)-I)/\delta,\\
B=\mathbb C[I,V,J,X],\qquad
EI=EV=EJ=0,\qquad EX=c,\qquad
\ker E=\mathbb C[I,V,J].
\end{gathered}
\tag{9}
\]
The displayed successive recovery formulas prove both inverse
orders. They involve no localization. To check \(EJ=0\)
without a summation identity, Taylor's formula gives
\(X\mathcal S=F(V+\eta X)-F(V)-\eta XF'(V)\), and hence
\(\delta Z=X(J-\eta F'(V))-F(V)-I\).
Now \(EI=EV=E\eta=0\) and \(E^2Z=0\) imply
\(2c\,EJ+X E^2J=0\).
In the polynomial coordinates just constructed, \(EJ\) is still
locally nilpotent under \(E\); differentiating this identity
enough times gives \(EJ=0\) by downward induction.
Equivalently, substituting (3) directly into the derivative of
(8) gives the same equality.

One may replace \(J\) in the invariant generators by \(R=EZ\):
the preceding identity and (9) give
\(\delta R=cJ-tF'(V)\), an invertible triangular replacement.

## 6. Selected primitive slice in the dense case

Suppose additionally that the three good speeds have rank two
and dense homogeneous cone, and let \(T=\partial_W\) hold
\(X,Y,Z\) fixed. In the invariant coordinates \(I,V,R\) and
slice \(u_0=X/c\), differentiation gives
\[
\begin{gathered}
TI=cu_0,\qquad Tu_0=0,\qquad
TV=-c\,t'(I)u_0^2,\\
TR=\frac c\delta-\frac c\delta t'(I)F'(V)u_0,\qquad
N=[u_0^2]T|_{\ker E}
=-c\,t'(I)\partial_V,\qquad
\ker N=\mathbb C[I,R].
\end{gathered}
\tag{10}
\]
For the middle derivative, write
\(\mathcal S=(F(Y)-F(V)-\eta XF'(V))/X\) in the fraction
field while holding \(X,Y\) fixed. Since
\(TV=-\eta'(I)X^2\), one obtains
\(T\mathcal S=\eta\eta'X^2F''(V)\).
Substitution in \(R=(cJ-tF'(V))/\delta\) cancels those terms
and gives (10). The result is polynomial, so it also holds at
\(X=0\).

Density excludes constant \(t\), which would give a homogeneous
linear relation among the speeds \(c,t,R\). Thus \(t'\ne0\),
and the primitive part of \(N\) is a complex-unit multiple
of \(\partial_V\); it has a global polynomial slice.
If another global \(E\)-slice was initially used, it differs
from \(u_0\) by an invariant. The coefficient of degree two
on \(\ker E\) is unchanged by this translation.

The same statement transfers through constant affine good changes
and bad shears by good polynomials, which preserve the selected
partial up to a nonzero complex factor. It does not transfer
through an arbitrary nonlinear change of the good coordinates.

## 7. Remaining correction input and source scope

The result begins with the actual invariant \(I\) in (1).
Neither a weighted leading relation
\(s\,c_m=\gamma t^{m+1}\), a pure-power generic leading form,
nor generic polynomial-line geometry alone has been used as a
substitute for it. Producing such a corrected invariant or a
different sufficient global recognition mechanism remains a
separate problem. No general cancellation conclusion follows.

## Sources

1. N. Dasgupta and N. Gupta,
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   Theorem 4.1, printed p. 9, stating Wang's two-quasi-nice
   classification over a characteristic-zero field.
   The full displayed statement, both alternatives and field
   convention were freshly read. The invocation above verifies
   its exact polynomial-coordinate and irreducibility premises.
   This is a use of the classification, not a fresh recursive
   proof audit of Wang's original argument.
2. [Classification of irreducible actions preserving a normalized cubic suspension](normalized-cubic-action-classification-pass132.md),
   Sections 1--5 and 8. The cubic backward identity, exact
   field passage, divisorial fixed-point contradiction, and
   selected-coordinate calculation extended here.
3. [A weight-three invariant in every supplied primitive quadratic frame](primitive-cubic-correction-existence-pass134-working.md),
   Sections 6--7. Its actual corrected-invariant construction
   illustrates the extra input needed before this recognition
   mechanism can be applied. No all-degree correction theorem
   is inferred from that quadratic result.

[^1]: Source 1. The coefficient field here is \(K=\mathbb C(I)\).
[^2]: Source 2. Source 3 concerns the distinct correction step.
