# Exact integrability of degree-one pencils

The full degree-one normal form admits an exact polynomial-coordinate
recognition criterion. It asks for one invariant polynomial correction
satisfying two finite-divisor congruences, rather than an unknown
two-variable automorphism. When the common-local-slice factor is nonzero
at the marked divisor, the criterion becomes a constructive
necessary-and-sufficient test: radical divisibility and one explicit
first-jet parity condition suffice.

This recognizes which prescribed pencils come from the unchanged
canonical model. It does not supply a repair path for every given
horizontal, or prove that an unknown polynomial cylinder admits such
coordinates. An explicit nonsliced top with common-local-slice
derivative exactly \(x^2\) separates those questions.

## 1. Polynomial data and conventions

Let
\[
R=\mathbb C[x,\lambda,b,c],\quad h=x^2c-b^2,\quad
F=p(x)b+Q(x,h),
\tag{1}
\]
where \(p\ne0\), \(Q\in\mathbb C[x,T]\). Assume the polynomial
derivation \(L=J_F\) is primitive, and choose a nonzero
\(g\in\mathbb C[x,T]\). The convention is
\(J_H=H_c\partial_b-H_b\partial_c\). Write
\[
G(x,T)=\int_0^T g(x,s)\,ds,\qquad
K=h+\lambda G(x,F),
\]
\[
\mathcal D=D_0+\lambda g(x,F)L=J_K,\qquad
D_0=x^2\partial_b+2b\partial_c,\qquad v=1+\lambda x.
\tag{2}
\]
All these expressions are polynomial. In particular
\[
\mathcal DF=x^2p,\qquad \mathcal DK=0.
\tag{3}
\]
Over \(\mathbb C(x)\), the variables \(F,h\) are actual coordinates,
with \(b=(F-Q(x,h))/p\), \(c=(h+b^2)/x^2\).
In these coordinates \(\mathcal DF=x^2p\) and
\(\mathcal Dh=-\lambda x^2p\,g(x,F)\); hence \(\mathcal D\) is
triangular and locally nilpotent. This descends to \(R\).
The same argument proves local nilpotence of \(L\).

An *actual canonical realization* means a polynomial isomorphism
fixing \(x,\lambda\),
\[
\theta:\mathbb C[x,\lambda,w,z]\longrightarrow R,\qquad
\theta(w)=W,\quad\theta(z)=Z,\quad
\theta\equiv\operatorname{id}\pmod\lambda,
\tag{4}
\]
which intertwines
\[
\Delta=x^2\partial_w+2v^2w\partial_z
\quad\hbox{and}\quad \mathcal D.
\]
It must have a polynomial inverse. The potential \(K\) may differ
from \(\theta(x^2z-v^2w^2)\) by an element of
\(\mathbb C[x,\lambda]\). No equality of those potentials is
silently imposed.

Every normalized degree-one horizontal in the fixed model supplies
data (1)–(2), by [pass 35](general-q1-repair-pass35.md).
The converse is the integrability problem studied here.

## 2. An exact single-correction criterion

**Theorem 1.** The data admit an actual canonical realization if and
only if there is \(U\in\mathbb C[x,\lambda,T]\) such that
\[
N=F-Q(x,K)+\lambda U(x,\lambda,K)
\quad\hbox{is divisible by }p\hbox{ in }R,
\tag{5}
\]
and, putting \(W=N/p\),
\[
K+v^2W^2\in\mathbb C[x,\lambda]+x^2R.
\tag{6}
\]
Only the class of \(U\) modulo \(p(x)x^2\) matters. Thus its
\(x\)-degree can be taken below \(\deg p+2\), after scaling the
modulus to be monic. This is not a bound on its degrees in
\(\lambda,T\).

### 2.1 Every normalized local slice has this form

Over \(\mathbb C(x)[\lambda]\), the variables \(F,K\) are actual
coordinates: first pass from \(b,c\) to \(F,h\), then replace
\(h\) by \(K=h+\lambda G(x,F)\). Consequently
\[
\ker\mathcal D=\mathbb C(x)[\lambda,K]
\]
in that localized ring. If \(W\) is any polynomial with
\(\mathcal DW=x^2\), then
\(W=F/p+A(x,\lambda,K)\), with
\(A\in\mathbb C(x)[\lambda,T]\).
Normalization \(W|_{\lambda=0}=b\) gives
\(A(x,0,T)=-Q(x,T)/p\). Hence (5) holds initially with
\(U\in\mathbb C(x)[\lambda,T]\).

In fact \(U\) has no poles in \(x\). For every complex \(\alpha\),
the substitution
\[
\mathbb C[\lambda,T]\longrightarrow\mathbb C[\lambda,b,c],
\qquad T\longmapsto K(\alpha,\lambda,b,c)
\tag{7}
\]
is injective. To see this, take the lowest nonzero power of
\(\lambda\) in a putative relation. At \(\lambda=0\), its
coefficient becomes a nonzero polynomial in
\(\alpha^2c-b^2\), which cannot vanish.
Since
\(\lambda U(x,\lambda,K)=pW-F+Q(x,K)\) is polynomial,
a highest pole at \(x=\alpha\) would contradict (7).
This applies to every pole order. Therefore \(U\) is polynomial.

For an actual realization, the relative Jacobian is one by
normalization and the actual inverse. Thus the two potentials
\(\theta(x^2z-v^2w^2)\) and \(K\), having the same Jacobian
derivation, differ by a polynomial in \(x,\lambda\).
This is exactly (6), proving necessity.

### 2.2 The congruences give a genuine two-sided inverse

Conversely suppose (5)–(6). Choose \(C\in\mathbb C[x,\lambda]\)
so that
\[
Z=\frac{K+C+v^2W^2}{x^2}
\tag{8}
\]
is polynomial. It can be chosen with \(C|_{\lambda=0}=0\):
at \(\lambda=0\), \(W=b\), \(K=h\), so the numerator without
\(C\) is \(x^2c\).
Equation (3) gives
\[
\mathcal DW=x^2,\quad \mathcal DZ=2v^2W,\quad
\det\frac{\partial(W,Z)}{\partial(b,c)}=1.
\tag{9}
\]
The last identity alone will not be used to infer coordinates.

First invert \(x\), and put \(S=\mathbb C[x,x^{-1},\lambda]\).
The generic kernel over \(\operatorname{Frac}S\) is
\(\operatorname{Frac}S[K]\). Since
\(\mathcal DW=x^2\in S^*\), the two derivatives of \(K\)
generate the unit ideal. For every irreducible \(\pi\in S\),
the residue of \(K\) is therefore nonconstant in \(b,c\) over
\(\operatorname{Frac}(S/\pi)\). A highest-\(\pi\)-pole argument
contracts the generic kernel to
\[
\ker(\mathcal D:R_x\to R_x)=S[K].
\tag{10}
\]
The ordinary slice theorem, applied to \(W/x^2\), now gives
\(R_x=S[K,W]=S[W,Z]\), the last equality following from (8).
This proves an actual localized isomorphism.

Next reduce modulo \(x\). Equation (8) implies
\[
-\overline W^{\,2}
 =\overline K+\overline C
 =-b^2+\lambda G(0,F(0,b,c))+\overline C.
\]
The partial derivatives in \(b,c\) of the right side have
\(\lambda\)-degree at most one. Since
\(\overline W|_{\lambda=0}=b\), the integral-domain degree
argument from pass 35 gives
\[
\overline W=b+\alpha\lambda,\qquad \alpha\in\mathbb C.
\tag{11}
\]
There is no leading-product cancellation in \(W W_b\), because
\(W_b|_{\lambda=0}=1\). Its two degree-two derivative
coefficients then force the \(\lambda\)-coefficient of \(W\)
to be constant. Reducing the Jacobian identity (9) gives
\(\overline Z_c=1\), so
\(\overline Z=c+J(\lambda,b)\).
The reduced map is therefore an actual triangular isomorphism.

Finally, localized surjectivity and reduced injectivity clear
every inverse denominator. If \(x^na=\theta(P)\) for a target
generator and a polynomial \(P\), reduction modulo \(x\) forces
\(P\) to be divisible by \(x\) whenever \(n>0\). Cancel \(x\)
and repeat. Thus every target generator has a polynomial
preimage. Injectivity follows from the localized isomorphism.
This proves the full isomorphism (4).

If \(U\) changes by \(px^2V\), then \(W\) changes by
\(\lambda x^2V(x,\lambda,K)\). Both (5) and (6) remain true.
This proves the final assertion of Theorem 1.

## 3. The exact off-boundary coefficient ideal

Let \(p_{\mathrm{red}}\) be the product of the distinct
nonzero-root factors of \(p\). Then
\[
(\mathcal Db,\mathcal Dc)R_x=R_x
\quad\Longleftrightarrow\quad
p_{\mathrm{red}}\mid g(x,T)
\text{ coefficientwise}.
\tag{12}
\]
Indeed, after inverting \(x\), the ideal is
\[
(1+\lambda g(x,F)Q_T(x,h),\ \lambda p(x)g(x,F)).
\tag{13}
\]
If \(p(\alpha)=0\), \(\alpha\ne0\), then
\(F_\alpha=Q(\alpha,h_\alpha)\).
Primitivity of \(L\) makes this nonconstant: otherwise both
coefficients of \(L\) would have factor \(x-\alpha\).
Thus \(Q_T(\alpha,h_\alpha)\ne0\).
If \(g(\alpha,T)\ne0\), specializing (13) gives the proper
principal ideal generated by
\[
1+\lambda g(\alpha,Q(\alpha,h_\alpha))
                    Q_T(\alpha,h_\alpha),
\]
a nonconstant polynomial in \(\lambda\). This proves necessity.

Conversely, (12) makes \(p\) divide a sufficiently high power
of \(g\) in \(\mathbb C[x,x^{-1},T]\). A sufficiently high power
of \(\lambda gQ_T\) then lies in \((\lambda pg)\).
The finite geometric series makes \(1+\lambda gQ_T\) a unit
modulo \(\lambda pg\), proving sufficiency.

This is a full coefficient-ideal statement, not a claim that
off-boundary freeness alone solves the marked-divisor lifting
problem.

## 4. A constructive full criterion when \(p(0)\ne0\)

Assume now \(p_0=p(0)\ne0\). Write coefficient expansions
\[
p=p_0+xp_1+O(x^2),\quad
Q=Q_0+xQ_1+O(x^2),\quad
g=g_0+xg_1+O(x^2),\quad
G=G_0+xG_1+O(x^2).
\tag{14}
\]
All \(Q_i,g_i,G_i\) are polynomials in one variable, and
\(G_i'=g_i,\ G_i(0)=0\).

Here is an entirely polynomial test. First require
\[
g_0(T)=\gamma\in\mathbb C,\qquad \gamma Q_0'(T)=0.
\tag{15}
\]
Set
\[
\alpha=-\gamma p_0/2,\quad
F_0=p_0b+Q_0(-b^2),\quad F_1=p_1b+Q_1(-b^2),
\]
\[
s=b+\alpha\lambda,\quad
k_0=\alpha^2\lambda^2+\lambda\gamma Q_0(0),\quad
K_0=k_0-s^2,\quad
J=G_1(F_0)+\gamma F_1,
\]
\[
D_Q=\frac{Q_1(-b^2)-Q_1(K_0)}{\lambda}.
\tag{16}
\]
The quotient defining \(D_Q\) is polynomial, since
\(K_0|_{\lambda=0}=-b^2\). Define
\[
E(\lambda,b)=
 \bigl(p_0-2sQ_0'(K_0)\bigr)J
 +2s(D_Q-p_1\alpha)+2p_0s^2.
\tag{17}
\]
The *parity test* is
\[
\frac{E(\lambda,s-\alpha\lambda)
      +E(\lambda,-s-\alpha\lambda)}2
 \in\mathbb C[\lambda].
\tag{18}
\]

**Theorem 2.** Under \(p_0\ne0\), an actual canonical realization
exists if and only if all three conditions hold:

- \(\operatorname{rad}(p)\mid g(x,T)\) coefficientwise;
- the boundary condition (15);
- the parity test (18).

For constant nonzero \(p\), the first condition is vacuous.
The proof constructs a polynomial \(U\) in Theorem 1 by finite
nilpotent inversion and the Chinese remainder theorem.

### 4.1 Necessity and the first jet

An actual realization gives (12); here all roots of \(p\)
are nonzero. Its square relation modulo \(x\) implies
\(G_0(F_0)\) is affine in \(b\). Since \(p_0\ne0\),
\(F_0\) is nonconstant. If \(g_0\ne0\), composition degrees
force \(G_0\) and \(F_0\) to be linear, giving (15).
If \(g_0=0\), (15) is automatic.
Thus \(G_0=\gamma T\), \(K\bmod x=K_0\), and (11) has
precisely the \(\alpha\) in (16).

Write \(U=U_0+xU_1+O(x^2)\). The zeroth-order numerator in
(5) forces \(U_0=p_0\alpha\). The substitution map in \(T\)
is injective, so this is an equality of polynomials, not
merely a choice along one curve.
Direct expansion, using \([x]K=\lambda J\), gives
\[
[x]W=\frac{\lambda}{p_0}
 \bigl(D_Q-p_1\alpha-Q_0'(K_0)J
                      +U_1(\lambda,K_0)\bigr).
\tag{19}
\]
Consequently
\[
K+v^2W^2
 \equiv k_0+\frac{x\lambda}{p_0}
       \bigl(E(\lambda,b)+2sU_1(\lambda,K_0)\bigr)
       \pmod{x^2}.
\tag{20}
\]
Since \(K_0=k_0-s^2\), the correction term is odd in \(s\).
Its even part cannot change (18), proving necessity.

### 4.2 Explicit correction at the marked divisor

Suppose (18) holds, and write
\(\widetilde E(\lambda,s)=E(\lambda,s-\alpha\lambda)\).
Let \(e_0(\lambda)\) be its even part. Define the polynomial
\(R_1(\lambda,z)\) by
\[
R_1(\lambda,s^2)
  =-\frac{\widetilde E(\lambda,s)-e_0(\lambda)}{2s}.
\tag{21}
\]
The numerator is odd, so division by \(s\) is exact and
the quotient is even. Choose
\[
U_1(\lambda,T)=R_1(\lambda,k_0-T),\qquad
U\equiv p_0\alpha+xU_1\pmod{x^2}.
\tag{22}
\]
Then (20) becomes
\(k_0+x\lambda e_0(\lambda)/p_0\), independent of \(b,c\).
It satisfies the second congruence of Theorem 1.

### 4.3 Explicit correction at the other divisor

If \(p\) is nonconstant, work in
\(A=\mathbb C[x]/(p)\).
Its nilradical is the ideal generated by
\(\operatorname{rad}(p)\) modulo \(p\).
The first condition of Theorem 2 makes \(G\) coefficientwise
nilpotent in this ring. Thus
\[
\phi(T)=T+\lambda G(x,Q(x,T))
\quad\text{in }A[\lambda,T]
\tag{23}
\]
has a finite polynomial inverse \(\psi\).
For clarity, if \(e(T)=\phi(T)-T\) has coefficients in a
nilpotent ideal \(I\), iterate
\(T_0=T,\ T_{j+1}=T-e(T_j)\).
Consecutive differences lie in successively higher powers of
\(I\), so the sequence stabilizes to a solution
\(\psi+e(\psi)=T\). Uniqueness by the same power argument
gives the inverse composition in the other order as well.

Modulo \(p\), \(F=Q(x,h)\) and \(K=\phi(h)\).
Choose
\[
U_p(\lambda,T)=
 \frac{Q(x,T)-Q(x,\psi(T))}{\lambda}
 \quad\text{in }A[\lambda,T].
\tag{24}
\]
The quotient is polynomial because \(\psi(T)|_{\lambda=0}=T\).
Substitution \(T=K\) makes the numerator \(N\) in (5)
vanish modulo \(p\).
For constant \(p\), this part is simply omitted.

Since \(p(0)\ne0\), the ideals \((p)\) and \((x^2)\) are
comaximal in \(\mathbb C[x]\). The Chinese remainder theorem
combines (24) and (22) into an actual
\(U\in\mathbb C[x,\lambda,T]\).
Theorem 1 now supplies polynomial \(W,Z\), normalization, and
a genuine global inverse. This proves sufficiency.

The construction uses no unbounded formal series and no
hypothesis that a Jacobian-one pair is automatically a coordinate
pair. It is a finite algorithm on prescribed polynomial data
satisfying the tests. It is not an algorithm finding such data
or a path between arbitrary realizations.

## 5. A sharp all-degree simplification at zero boundary speed

If \(g_0=0\), then \(\alpha=0\), \(K_0=-b^2\).
The parity test simplifies to
\[
\operatorname{Even}_b
 \bigl(G_1(F_0)F_0'(b)+2p_0b^2\bigr)
 \text{ is constant}.
\tag{25}
\]
This forces \(\deg Q_0\le1\). To see the nonconstant case,
take a polynomial \(H_1\) with \(H_1'=G_1\). Integrating
(25) yields
\[
\operatorname{Odd}_b H_1(F_0)
 =c\,b-\frac23p_0b^3.
\tag{26}
\]
Translate the constant \(Q_0(0)\) out of \(F_0\).
If \(N=\deg Q_0\ge1\) and \(d=\deg H_1\ge2\), the highest
odd term on the left has degree \(2N(d-1)+1\), with nonzero
coefficient
\(d\,\operatorname{lc}(H_1)\,p_0
  \operatorname{lc}(Q_0(-b^2))^{d-1}\).
Lower powers of \(H_1\) and terms with three or more copies
of \(p_0b\) have smaller degree. A linear \(H_1\) cannot
supply the cubic term. Thus \(N(d-1)=1\).

It follows that if
\(Q_0(T)=q_0+q_1T\) with \(q_1\ne0\), (25) is equivalent to
\[
g_1(T)=\frac{2}{3q_1}.
\tag{27}
\]
If \(Q_0=q_0\) is constant, the correct condition allows
arbitrarily high even degrees:
\[
\operatorname{Odd}_z g_1(q_0+z)
 =-\frac{4z}{p_0^2}.
\tag{28}
\]
The even part is unrestricted. There is no claim that \(g_1\)
must have degree one in this branch.
When \(g_0\ne0\), condition (15) already makes \(Q_0\) constant.
Therefore every actual realization with \(p(0)\ne0\) has
\(\deg Q_0\le1\).

## 6. Exact common derivative does not force a sliced top

Take
\[
p=1,\quad Q(T)=T,\quad g=\frac23x,\quad
F=b+h,\quad
L=x^2\partial_b+(2b-1)\partial_c.
\tag{29}
\]
The criteria hold: \(g_0=0\), \(q_1=1\), and
\(g_1=2/3\). The marked-divisor construction gives
\[
U=\frac{x(2T-1)}3.
\]
Put \(t=2\lambda x/3\), so \(K=h+tF\). Then
\[
W=(1-t+t^2)b+t^2h-t/2,\qquad
Z=\frac{K+(1+\lambda x)^2W^2}{x^2}.
\tag{30}
\]
The quotient is polynomial. The independent \((b,h)\)-matrix
has determinant one:
\[
\begin{pmatrix}W+t/2\\K\end{pmatrix}
 =
\begin{pmatrix}1-t+t^2&t^2\\t&1+t\end{pmatrix}
\begin{pmatrix}b\\h\end{pmatrix}.
\]
Thus a completely explicit inverse, with
\(I=x^2z-(1+\lambda x)^2w^2\), is
\[
b=(1+t)(w+t/2)-t^2I,\quad
h=-t(w+t/2)+(1-t+t^2)I,\quad
c=(h+b^2)/x^2.
\tag{31}
\]
The last quotient is polynomial by its residue modulo \(x^2\).
These formulas independently verify both global compositions.

The resulting actual horizontal has degree one. Its common
local slice has
\[
\mathcal DF=x^2
\]
with no extra nonunit factor \(p\). Yet the primitive top \(L\)
has the fixed line \(x=0,b=1/2\), hence no slice. The potential
\(F=x^2c-b^2+b\) has a critical locus on that line and is not
a global coordinate. Thus knowing the exact common derivative
\(x^2\), without a polynomial companion, is insufficient for
the proposed sliced-top inference.

## 7. Scope and verification boundary

Theorem 1 covers all the polynomial normal-form data in Section 1,
including \(p(0)=0\). Theorem 2 decides integrability constructively
on the full \(p(0)\ne0\) branch. On \(p(0)=0\), the two-congruence
criterion remains exact, but its correction is not asserted to
exist automatically or to have a bounded degree in \(\lambda,T\).

These statements recognize and construct canonical coordinate
realizations from supplied data. They do not construct a
degree-one path repairing every supplied horizontal, nor force
unit primitive-top plinth. The example in Section 6 explicitly
prevents replacing the missing companion by a common local slice.

The argument uses actual relative polynomial planes and the
specified marked coordinate. Those hypotheses cannot be inferred
from \(A[s]\simeq\mathbb C^{[4]}\) when polynomiality of \(A\)
is precisely the unknown issue. No general cancellation claim,
universal recognition claim, or priority claim is made.

The separate q1_integrability_checks_pass36.py tests bounded
instances of the congruences, finite inverse, parity computation,
and exact inverse in Section 6. Universal quantifiers rely on
the proof, not on finite examples.

The initial standalone run passed all eight methods in 0.701 seconds,
with no mathematical or assertion corrections needed. A separate
full-proof reconstruction checked both speed branches, the full
nonreduced divisor correction, and the global inverse argument.

## Source and dependency scope

The input normal form and primitive-kernel contraction are proved
in [pass 35](general-q1-repair-pass35.md). That note explicitly
attributes its planar input to Kuroda's
[*The automorphism theorem and additive group actions on the affine
plane*](https://arxiv.org/pdf/1604.04070), Theorem 1.1, and the
classical characteristic-zero result to Rentschler.
The new congruence recognition proof here uses explicit
coordinates, the slice identity, UFD pole contraction, finite
nilpotent inversion, and the Chinese remainder theorem.
It does not use a determinant-one sufficiency principle or an
unproved global relative-plane cancellation theorem.
