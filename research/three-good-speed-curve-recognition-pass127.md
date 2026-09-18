# Recognition of a supplied three-good frame with a speed curve

## 1. The theorem and its exact scope

Suppose the displayed generators are actual polynomial coordinates,
and the locally nilpotent derivation has a global slice:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad
Eu=1,\quad A=\ker E,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad
r=\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3]\le1.
\end{gathered}
\tag{1}
\]
Then \(A\simeq\mathbb C^{[3]}\). There is **no bound** on the
\(E\)-degree of the last coordinate \(z\). In particular, neither
\(E^3z=0\) nor a joint curve containing \(E^2z\) is assumed.

The new argument produces an invariant actual ambient coordinate
in the remaining unit-speed case. The last kernel-recognition step
uses the retained Bhatwadekar--Gupta--Lokhande theorem, with its
hypotheses checked below. This is recognition within a supplied
three-good-coordinate frame. It does not produce such a frame for
an arbitrary sliced action, or settle speed rank two or unrestricted
cancellation.

## 2. Rank zero, polynomial parametrization, and the proper ideal

If \(r=0\), all \(a_i\) are complex constants. If one is nonzero,
the corresponding \(x_i/a_i\) is an actual coordinate slice, and
\(A\simeq B/(x_i)\simeq\mathbb C^{[3]}\). If all vanish, then
\(E=(Ez)\partial_z\); the slice equation
\((Ez)\partial_z u=1\) makes \(Ez\in\mathbb C^*\), and the kernel
is the good-coordinate polynomial ring. Thus assume \(r=1\).

The retained [polynomial-curve factorization source](polynomial-curve-factorization-source.md)
gives a genuinely polynomial \(p\in B\setminus\mathbb C\) with
\(a_i=f_i(p)\), \(f_i\in\mathbb C[T]\). This is the application of
de Bondt's Corollary 3.2 to the speed algebra itself. It does not
place any unspecified acceleration in that curve algebra.
Choosing a nonconstant \(f_i\) and differentiating \(E(f_i(p))=0\)
shows \(E(p)=0\). Polynomiality of \(p\) is essential below;
it is not yet an ambient coordinate.

Here is the complete reduction already established in
[the speed-curve part of126](three-good-joint-curve-bound-pass126.md),
Sections 4--5. Put \(c=Ez\), let \(b=\gcd(f_1,f_2,f_3)\), and use
univariate Bézout. The actual slice gives
\[
\begin{gathered}
a_i=f_i(p),\qquad Ep=0,\qquad
I=(a_1,a_2,a_3)B=b(p)B,\qquad (b(p),c)B=B,\\
0=b(p)\sum_i(f_i/b)(p)p_{x_i}+c\,p_z,
\qquad b(p)\mid p_z.
\end{gathered}
\tag{2}
\]
The last divisibility is modulo the full ideal \(b(p)B\), not its
radical. If \(I\ne B\), then \(b\) is nonconstant. Were \(p_z\ne0\),
the original degree \(m=\deg_zp\ge1\) would give
\(\deg_z b(p)=(\deg b)m\ge m>m-1=\deg_zp_z\), contradicting (2).
Hence \(p_z=0\) in that case.

Whenever \(p_z=0\), including in the unit case, all good speeds
belong to the actual ring \(\mathbb C[x_1,x_2,x_3]\). An elementary
degree argument gives an invariant linear coordinate in this
particular curve situation. Write \(f(T)=\sum_k v_kT^k\) with
constant vectors \(v_k\in\mathbb C^3\), put
\(L_k=v_k\cdot\partial_{\rm good}\), and let
\(d=\deg p\ge1\) be total degree in the good coordinates.
Every nonzero \(L_kp\) has total degree between zero and \(d-1\).
Thus the total degree of a nonzero summand \(p^kL_kp\) belongs
to \([kd,(k+1)d-1]\). These intervals are disjoint for distinct
\(k\); the highest-degree nonzero summand could not cancel in
\(0=Ep=\sum_k p^kL_kp\). Hence \(L_kp=0\) for every \(k\).
This compares the summands' total degrees, not their full
homogeneous supports.

If the vectors \(v_k\) spanned \(\mathbb C^3\), every good partial
of \(p\) would vanish, contradicting its nonconstancy. Their
span is therefore proper. A nonzero constant row annihilating
it gives a constant linear form in the \(x_i\) fixed by \(E\),
and that form is an actual ambient coordinate. Section 7 gives
the regular-kernel recognition endpoint. No classification of
nice three-variable derivations is needed for this reduction.

It therefore suffices to treat \(I=B\) and
\(\alpha=p_z\ne0\). In this case \(\gcd(f_1,f_2,f_3)=1\) up to a
complex unit, since a nonconstant polynomial in the nonconstant
\(p\) cannot be a unit of \(B\). If \(Ez=0\), \(z\) itself is
already an invariant ambient coordinate. Otherwise put
\(\ell=\deg_Ez\ge1\), which is finite by local nilpotence.

## 3. The actual selected commutator and its local nilpotence

Write \(T_z=\partial_z\), \(\delta=c_z\), and
\(A_0=f'(p)\cdot\nabla_{\rm good}p\). The selected-column proof in
[cofactor126](three-good-flow-cofactor-bounds-pass126.md),
Sections 2--3, does not impose a last-coordinate degree bound.
Its rank-one application can also be seen directly here.

Let \(F_t=\exp(tE)(x_1,x_2,x_3,z)\). It is an actual polynomial
automorphism over \(\mathbb C[t]\), so its original-coordinate
Jacobian determinant is the constant one. The column of
\(\exp(tE)T_z\exp(-tE)\) is the last column of
\(\operatorname{Jac}(F_t)^{-1}\). Its cofactors use only the three
good rows \(dx_i+t f_i'(p)\,dp\). Terms using two copies of \(dp\)
vanish. Consequently this column has degree at most one:
\[
\begin{gathered}
\exp(tE)T_z\exp(-tE)=T_z+tQ,\qquad [E,Q]=0,\\
Q=[E,T_z]=-\alpha f'(p)\cdot\partial_{\rm good}
                 -\delta\partial_z,\qquad
A_0+\delta=0,\\
Qp=-\alpha(A_0+\delta)=0,\qquad
E\alpha=[E,T_z]p+T_z(Ep)=0.
\end{gathered}
\tag{3}
\]
The middle scalar identity is the coefficient of \(t\) in the
actual flow determinant, or equivalently the vanishing divergence
of \(E=(f(p),c)\). No quadratic expression for the fourth flow
coordinate is being substituted.

The derivation \(Q\) is a nonzero LND of the original ring.
Indeed
\(\varepsilon\exp(\varepsilon^{-1}E)T_z
\exp(-\varepsilon^{-1}E)=\varepsilon T_z+Q\)
is an LND on \(B[\varepsilon,\varepsilon^{-1}]\), fixes
\(\varepsilon\), and preserves \(B[\varepsilon]\).
Restriction is locally nilpotent because that subring injects
into the Laurent ring; specialization at \(\varepsilon=0\)
then gives an LND on \(B\). Nonvanishing follows from
\(\alpha\ne0\) and \(f'\ne0\). This construction never localizes
\(T_z\) at an element it may move.

## 4. Finite flow degree preserves the full content multiplicities

Put \(Z_t=\exp(tE)z\in B[t]\), of degree \(\ell\). The full
Jacobian is the identity plus the two column/row updates
\((f'(p),0)^t\,t\,dp\) and \(e_4(dZ_t-dz)\).
The two-by-two determinant identity therefore gives exactly
\[
\begin{gathered}
1=\det\operatorname{Jac}(F_t)
 =(1+tA_0)\partial_z Z_t
       -t\alpha f'(p)\cdot\nabla_{\rm good}Z_t,\\
(1-t\overline\delta)\,\overline{\partial_z Z_t}=1
       \quad\hbox{in }(B/(\alpha))[t],\\
\alpha\mid\delta^{\,\ell+1}.
\end{gathered}
\tag{4}
\]
Bars denote reduction modulo the entire principal ideal
\((\alpha)\). If \(\alpha\) is a unit, the last assertion is
immediate and \(Q\alpha=0\) below is automatic. Otherwise the
displayed quotient may be nonreduced, which causes no problem.
Write \(\overline{\partial_zZ_t}=\sum_{j=0}^{\ell}w_jt^j\),
padding its coefficients with zeros if its degree is smaller.
The constant coefficient is \(w_0=1\). Comparing successive
coefficients in (4) gives \(w_j=\overline\delta^{\,j}\), and the
coefficient of \(t^{\ell+1}\) is
\(-\overline\delta^{\,\ell+1}=0\). This proves the stated
divisibility, with all prime multiplicities.

Let \(d=\gcd(\alpha,\delta)\) in the original polynomial UFD,
including \(\delta=0\). Every coefficient of \(Q\) is divisible
by \(d\), so \(d\mid Q(d)\) and LND divisibility gives \(Q(d)=0\).
At each prime, if the orders of \(\alpha,\delta\) are \(v,w\),
then \(v\le(\ell+1)w\) implies
\(v\le(\ell+1)\min(v,w)\). Thus
\[
\alpha\mid d^{\,\ell+1},\qquad Q(d)=0,\qquad
Q\alpha=0,\qquad Ep=E\alpha=Qp=Q\alpha=0.
\tag{5}
\]
For \(\delta=0\), take \(d=\alpha\) up to a unit. The implication
from \(Q(d)=0\) to \(Q\alpha=0\) is factorial closure of the
kernel of an LND. Both elementary LND facts follow from additivity
of the LND degree in a characteristic-zero domain: a nonzero
multiple of an element cannot be its nonzero derivative, and
the factors of an invariant product have degree zero.

For an independent reconstruction of the exponent, put
\(c_k=E^kz\), \(c_0=z\). Equation (3) gives
\(T_zc_k=-kQc_{k-1}\) for \(k\ge1\).
The equality \(c_{\ell+1}=0\) gives \(Qc_\ell=0\).
Using the actual coefficient row for \(Q\), one obtains
\(Qc_k=-\alpha f'(p)\cdot\nabla_{\rm good}c_k+
k\delta Qc_{k-1}\).
Starting with \(Qz=-\delta\), these scalar identities give
\(Qc_k\equiv-k!\delta^{k+1}\pmod\alpha\), and again (4) follows.
No derivation is applied to a quotient ideal not yet known to
be stable. This covers \(\ell=1\) and permits the highest
\(c_\ell\) to be constant or nonconstant.

## 5. The primitive polynomial normal forces vanishing Wronskians

View \(p\) as the polynomial \(P(x_1,x_2,x_3,z)\), and put
\(m=\deg_zP\ge1\). Define the three polynomials
\[
\mathbf B=(B_1,B_2,B_3),\qquad
B_i=P_zP_{x_i z}-P_{zz}P_{x_i},\qquad
\deg_zB_i\le2m-2,\qquad
f(P)\cdot\mathbf B=f'(P)\cdot\mathbf B=0.
\tag{6}
\]
The first orthogonality is obtained by eliminating the \(cP_{zz}\)
terms between \(Ep=0\) and \(E\alpha=0\). The second follows by
the same elimination from \(Qp=Q\alpha=0\), using the row in (3).

The vectors \(f,f'\) are independent over \(\mathbb C(T)\).
Otherwise their nonzero component ratios have zero derivative,
so \(f\) is a polynomial scalar times a fixed complex vector.
The unit gcd of the components makes that scalar constant,
contradicting speed rank one.

Let \(n(T)\in\mathbb C[T]^3\) be the primitive normal obtained
from \(f\times f'\) by dividing the gcd of its components.
It is a nonzero unimodular polynomial row, orthogonal to both
\(f\) and \(f'\). Over \(\operatorname{Frac}B\), (6) gives
\(\mathbf B=\lambda n(P)\). Choose univariate Bézout coefficients
\(v_i(T)\) with \(\sum_i v_i n_i=1\). Then
\(\lambda=\sum_i v_i(P)B_i\) actually belongs to \(B\).
In particular,
\[
\mathbf B=\lambda n(P),\quad \lambda\in B,\qquad
\deg n\ge2\ \Longrightarrow\ \mathbf B=0.
\tag{7}
\]
Indeed, if \(\lambda\ne0\), a component \(n_j\) of maximum
degree has
\(\deg_z(\lambda n_j(P))=\deg_z\lambda+m\deg n\ge2m\),
contradicting (6).

It remains to examine the low-degree normal rather than assume
it away. If \(n=n_0+Tn_1\) has degree at most one,
differentiation of \(nf=0\), together with \(nf'=0\),
gives \(n_1f=0\) and then \(n_0f=0\). If the two constant
rows \(n_0,n_1\) are independent, \(f\) is again a polynomial
scalar times their fixed one-dimensional common kernel.
The unit gcd makes \(f\) constant, a contradiction.
If the rows are dependent, primitivity of \(n\) forces
\(n\) to be a nonzero constant row. Then
\(n\cdot x_{\rm good}\) is already an invariant ambient linear
coordinate. Therefore the only case still needing recognition
has \(B_1=B_2=B_3=0\).

## 6. The Wronskian equation gives a global triangular coordinate

This last step is an elementary polynomial lemma, not a formal
or localized coordinate assertion. Write
\(P=\sum_{j=0}^m A_j(x_{\rm good})z^j\), \(A_m\ne0\).
The coefficient of \(z^{2m-2}\) in \(B_i=0\) is
\(mA_m\partial_{x_i}A_m\). Thus \(A_m\in\mathbb C^*\).

Over \(\mathbb C(x_1,x_2,x_3)(z)\), the same equation says
\(\partial_z(P_{x_i}/P_z)=0\). The constants of this ordinary
one-variable rational derivative are
\(\mathbb C(x_1,x_2,x_3)\).
Since \(A_m\) is constant, comparison of leading terms gives
\[
\begin{gathered}
\frac{P_{x_i}}{P_z}
  =\frac{\partial_{x_i}A_{m-1}}{mA_m}
  =\partial_{x_i}H,\qquad
H=\frac{A_{m-1}}{mA_m}\in\mathbb C[x_1,x_2,x_3],\\
v=z+H(x_{\rm good}),\qquad
z=v-H(x_{\rm good}),\qquad
P=F(v)\quad\hbox{for some }F\in\mathbb C[v]\setminus\mathbb C .
\end{gathered}
\tag{8}
\]
If \(\partial_{x_i}A_{m-1}=0\), the ratio has zero limit at
infinity, so its constant value is zero; this covers that
coefficient edge. Formula (8) also includes \(m=1\).
Holding \(v\) fixed gives
\(\partial_{x_i}P(x,v-H)=P_{x_i}-H_{x_i}P_z=0\).
Hence all coefficients of this polynomial in \(v\) are
complex constants, proving \(P=F(v)\).

The two transformations in (8) are explicit polynomial inverses
on the original four-ring. Since \(Ep=0\), the domain property
and characteristic zero give
\(0=E(F(v))=F'(v)Ev\), hence \(Ev=0\).
The parameter \(p\) itself need not be asserted to be a coordinate;
the actual coordinate supplied by the proof is \(v\).

## 7. Recognition, dependencies, and the remaining problem

Every unresolved branch above has produced an invariant actual
ambient coordinate, either a constant linear form or the
triangular coordinate in (8). The kernel \(A\) is regular:
regularity descends from its polynomial extension \(A[u]=B\);
equivalently the actual slice gives a smooth hypersurface
\(u=0\), since \(Eu=1\) makes its partial derivatives generate
the unit ideal. Thus the retained regular-kernel theorem applies:
\[
B=\mathbb C[v]^{[3]},\quad Ev=0,\quad E\ne0,\quad A\text{ regular}
\quad\Longrightarrow\quad
A=\mathbb C[v]^{[2]}\simeq\mathbb C^{[3]}.
\tag{9}
\]
This is precisely Bhatwadekar--Gupta--Lokhande Theorem 3.5, as
recorded with its complete displayed source proof in
[the recognition gate126](three-good-common-leading-kernel-boundary-pass126.md),
Section 3. Its deeper dependencies are retained, not reproved here.
The \(p_z=0\) reduction now uses the elementary degree separation
in Section 2, not the previously available nice-three source gate.

The complete saved polynomial-curve factorization note, the
cofactor126 proof, the joint-curve126 proof, the common-leading-kernel126
proof, and the linear-invariant71 source gate were reread.
The last of these is comparison material, not a dependency of
the present recognition argument.
The argument independently reconstructs the determinant,
full-multiplicity content, normal-degree, and polynomial-inverse
steps above. No new primary-source proof read or numerical run is
claimed by this author.

Root proposed the normal-degree and original-coordinate
Wronskian mechanism, the elementary \(p_z=0\) endpoint, and
independently reconstructed the all-degree commutator recursion.
General supplied the
all-degree determinant-quotient proof; Jet supplied the shorter
rational-derivative proof of (8). The separate
[canonical-volume factorization127](three-good-canonical-volume-factorization-pass127.md)
remains a valid additional result in its narrower unit joint-curve
presentation, but it is not a dependency of this recognition proof.
Neither an invariant-plane theorem, faithful-flat quotient
contraction, nor equality of invariant rings or fraction fields
is used to construct \(v\).

In particular this closes the speed-rank-one branch left by126,
including the quadratic joint-curve partial-profile case recorded
there. It does not close every abstract partial profile with the
same numerical entries. Speed rank two in a supplied three-good
frame, and entry into such a frame for an arbitrary sliced
four-variable action, remain separate unresolved obligations.
No file through pass126 is changed.
