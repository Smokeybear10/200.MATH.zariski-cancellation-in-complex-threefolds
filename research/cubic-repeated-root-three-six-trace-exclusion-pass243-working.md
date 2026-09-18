# The cubic first projection cannot have a degree-six second projection

In the supplied actual chart \(q=\rho^2-t^3\), the projected degree
pair \((\deg_vy,\deg_v\theta)=(3,6)\) is impossible. The complete
centered eliminant has no term linear in its second formal variable.
The irreducible relation of a birational polynomial pair of degrees
\((3,6)\), however, necessarily has such a term.

The proof uses a trace calculation over the exact coefficient field.
It does not assume that field is rational, make an ambient coordinate
change, or infer plane normality from birationality.

## 1. Actual assumptions and the centered relation

Assume the actual globally sliced exact1122 hypotheses of
[rebuilt237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md),
with the entire supplied initial kernel
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=\mathscr A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0\tau,b_0\tau,e_0\tau^2,h_0\tau^2)\bigr)
 =(\mathsf X^2\mathsf Z-\mathsf W^2+\mathsf X\mathsf Y^3),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2 .
\end{gathered}                                                     \tag{1}
\]
Here \(\tau\) is independent. The literal new \(Z\) pivot has already
been rebuilt after the actual coordinate interchange in237.
Its chart supplies
\[
\begin{gathered}
0\ne N=[u^3]\partial_Z|_{\mathscr A},\qquad
L=\operatorname{Frac}(\ker_{\mathscr A}N),\qquad
\mathscr A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
t,\rho\text{ algebraically independent},\quad q=\rho^2-t^3,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\\
y,z,w,\theta,\sigma\in L[v],\quad
L[y,z,w]=L[v],\quad J(X)=-a_0^3\in L^* .
\end{gathered}                                                     \tag{2}
\]
All coefficient partials extend uniquely to \(L\) and fix \(v\).
The proof below uses them only through the already derived complete
potential identities.

Suppose, for contradiction, that
\[
\deg_vy=3,\qquad \deg_v\theta=6,\qquad
R=2\theta+k_\rho\ne0 .
\tag{3}
\]
The last condition is automatic from the degree, but is written to
specify the return branch. The actual third and fourth potentials give
\[
\mathcal C=L[y,\theta]\subset\mathcal O=L[v],\qquad
\mathcal O=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C,\qquad
\operatorname{Frac}\mathcal C=L(v).
\tag{4}
\]
Indeed \(Rw\in\mathcal C\), the fourth potential is monic quadratic
in \(w\), and \(z=2\rho w+f(y,\theta)\). These are the exact
whole-line and return arguments of
[centered239](radical-minus-polynomial-centered-eliminant-pass239-working.md).
Only the fraction-field equality in (4) is needed after this point.

Put \(\kappa=k_\rho\), introduce an independent formal variable
\(\zeta=V+\kappa/2\), and set
\(\psi=\theta+\kappa/2\in L[v]\). This is a formal centering over
\(L\), not an original coordinate change. The complete eliminant
from239 satisfies
\[
\begin{gathered}
\mathcal H_c(U,\zeta)=\mathcal H(U,\zeta-\kappa/2),\qquad
\mathcal H_c(y,\psi)=0,\qquad
\deg\mathcal H_c=6,\quad (\mathcal H_c)_6=U^6,\\
\mathcal H_c=p(U)^2+\zeta^2A_2(U)+\zeta^3A_3(U)
                         +\zeta^4A_4(U)+\zeta^5A_5,\qquad
[\zeta]\mathcal H_c=0 .
\end{gathered}                                                     \tag{5}
\]
The notation \([\zeta]\) means the entire coefficient polynomial
in \(U\). The absence of this coefficient is an exact lower-potential
identity, not just a claim about the highest homogeneous part.

The birational pure-leading-form argument used in
[frontier240](cubic-repeated-root-projection-frontier-pass240-working.md)
gives degree six for the irreducible plane relation of \((y,\psi)\).
Equivalently, this follows by intersecting its birational polynomial
parametrization with a generic line: the resulting polynomial has
degree \(\max(3,6)=6\). Thus if \(G\) generates the evaluation kernel,
\[
\deg G=6,\qquad \mathcal H_c=\lambda G,\quad \lambda\in L^* .
\tag{6}
\]
The second assertion uses (5) and irreducibility in \(L[U,\zeta]\).
It is a scalar cofactor conclusion specific to this degree-six branch.

## 2. A trace degree bound over an arbitrary characteristic-zero field

For this section let \(L\) be any characteristic-zero field and write
\[
y(v)=a v^3+bv^2+cv+d,\qquad a\in L^* .
\tag{7}
\]
The letters in (7) are polynomial coefficients, not the actual leading
coefficients in (1). View \(L[U]\) inside \(L[v]\) by \(U\mapsto y(v)\).
The relation
\[
v^3=\frac{U-d-bv^2-cv}{a}
\tag{8}
\]
shows that \(1,v,v^2\) span \(L[v]\) over \(L[U]\).
They are independent: in a nonzero sum
\(\sum_{j=0}^2 P_j(y(v))v^j\), the nonzero summands have distinct
leading degrees modulo three. Consequently \(L[v]\) is free of
rank three with this basis and
\([L(v):L(y)]=3\).

Write \(\operatorname{Tr}\) for the field trace from \(L(v)\) to
\(L(y)\), identified with the trace of multiplication on this free
module. Let \(s_j(U)=\operatorname{Tr}(v^j)\). In the displayed
basis the multiplication matrix of \(v\) is
\[
M_v=
\begin{pmatrix}
0&0&(U-d)/a\\
1&0&-c/a\\
0&1&-b/a
\end{pmatrix}.
\tag{9}
\]
Therefore
\[
\begin{gathered}
s_0=3,\qquad s_1=-b/a,\qquad
s_2=b^2/a^2-2c/a,\\
s_j=\frac{U-d}{a}s_{j-3}-\frac ba s_{j-1}
                                  -\frac ca s_{j-2}\qquad(j\ge3).
\end{gathered}                                                     \tag{10}
\]
The recurrence follows by multiplying (8) by \(v^{j-3}\)
and applying the trace.

Induction on \(j\) proves
\[
\deg_U s_j\le\lfloor j/3\rfloor,\qquad
[U^k]s_{3k}=3a^{-k}\quad(k\ge0).
\tag{11}
\]
For the degree bound, each term on the right of (10) has at most
the asserted degree. When \(j=3k\), the last two terms have degree
at most \(k-1\); only \(U s_{3k-3}/a\) contributes degree \(k\).
This proves the second assertion too.
By \(L\)-linearity, every polynomial \(h(v)\in L[v]\) satisfies
\[
\deg_U\operatorname{Tr}(h(v))
                      \le\lfloor\deg_vh/3\rfloor .
\tag{12}
\]
The zero polynomial causes no exception to this inequality.
This proof uses neither formal branches at infinity nor rationality
or algebraic closedness of \(L\).

## 3. The linear coefficient of the degree-six generator cannot vanish

Return to (3). Centering does not change the degree of \(\theta\),
so \(\deg_v\psi=6\). Let \(\beta\in L^*\) be its leading coefficient,
let \(a\) be as in (7), and put
\[
\gamma=\beta/a^2,\qquad
\psi=\gamma y^2+r(v),\qquad \deg_vr\le5 .
\tag{13}
\]
No root extraction or parameter rescaling is involved.
Set \(T_1(U)=\operatorname{Tr}(r)\) and
\(T_2(U)=\operatorname{Tr}(r^2)\). Equation (12) gives
\[
\deg T_1\le1,\qquad \deg T_2\le3 .
\tag{14}
\]

By (4), \(L(y,\psi)=L(v)\). The characteristic polynomial of
multiplication by \(\psi\) on the free rank-three module is thus
also its minimal polynomial over \(L(y)\), of degree three.
It has coefficients in \(L[U]\), and is monic in \(\zeta\).
Gauss's lemma makes it the irreducible generator of the plane
evaluation kernel, up to multiplication by a unit of \(L\).
Write this particular generator as
\[
G_{\rm mon}(U,\zeta)
=\zeta^3-e_1(U)\zeta^2+e_2(U)\zeta-e_3(U).
\tag{15}
\]
The elementary trace identity in characteristic zero gives
\[
\begin{aligned}
e_2
&=\frac{(\operatorname{Tr}\psi)^2
                   -\operatorname{Tr}(\psi^2)}2\\
&=3\gamma^2U^4+2\gamma U^2T_1+
                                      \frac{T_1^2-T_2}{2}.
\end{aligned}                                                     \tag{16}
\]
Here \(\operatorname{Tr}\psi=3\gamma U^2+T_1\) and
\(\operatorname{Tr}(\psi^2)=3\gamma^2U^4+
2\gamma U^2T_1+T_2\), so every term is explicit.

By (14), all terms in the last line of (16) other than
\(3\gamma^2U^4\) have degree at most three. Hence
\[
[U^4]e_2=3\gamma^2\ne0 .
\tag{17}
\]
Since \(G_{\rm mon}\) differs from \(G\) in (6) only by a scalar,
(6) and (17) imply \([\zeta]\mathcal H_c\ne0\).
This contradicts the complete centered identity (5).
It excludes the pair \((3,6)\) under the actual hypotheses (1)--(3).

## 4. Why this does not invalidate the earlier formal countercontrol

The formal \((3,6)\) example in Section6 of240 has
\[
y=x^3,\qquad \theta=(x^6+x^4+x^2)/2,\qquad
G_0(U,V)=-(2V-U^2)^3+3U^2(2V-U^2)+U^2+U^4 .
\tag{18}
\]
It satisfies the conductor, module return, squared cubic center,
pure sextic top and the stated cofactor divisibilities there.
It does not satisfy the additional complete centered identity:
\[
[V]G_0=-6U^4+6U^2\ne0 .
\tag{19}
\]
Indeed its monic normalization is \(-G_0/8\), whose linear
coefficient has leading term \(3U^4/4\), exactly (17) with
\(\gamma=1/2\). Thus the formal example remains a valid boundary
for the weaker hypotheses listed in240. The new argument identifies
a specific additional actual identity that it fails.

## 5. Scope

This proof removes only the degree pair \((3,6)\) from the cubic
frontier240. It does not exclude all other projected pairs or supply
an original invariant coordinate. The separate quadratic-graph
argument in242 has its own differential and determinant hypotheses.
No coefficient-field transformation here is promoted to an ambient
polynomial automorphism.

The complete centered239 source, the relevant actual return input,
and the formal240 countercontrol were read before this argument.
The trace recurrence and the coefficient contradiction above are
the proof; no saved checker was executed, imported or compiled.
No earlier proof, index or packet was edited. The unrestricted
cancellation problem, arbitrary-frame entry, historical novelty,
proof-assistant certification and human expert review are outside
the claims of this working note.
