# Explicit nonlinear coordinates for invariant-coefficient extensions

A local-slice matrix construction gives explicit polynomial coordinates
for a class of four-variable additive actions whose coefficients may
depend on several invariants. It includes examples that cannot be
reduced by elementary coefficient-row operations. The construction
has a polynomial inverse and an exact necessary-and-sufficient slice
criterion under its stated congruence hypothesis.

This is a restricted theorem, not a solution of complex threefold
cancellation. The working target remains
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]
The intended field and dimension have not been confirmed by Xiangrui
Luo. The original email's conclusion has a dimension mismatch. The
November 2025 revision of *Relative Cancellation* records the
characteristic-zero problem in dimension at least three as open;
this is a dated source statement, not an exhaustive September 2026
literature-status claim.[^1]

The results below have complete working proofs and separate algebraic
reconstructions. Neither novelty nor human expert review is established.
Finite exact tests support the constructions but do not formally prove
the general arguments.

## 1. Definitions and the remaining recognition problem

A derivation \(D\) of an algebra over a characteristic-zero field is locally
nilpotent if each element is killed by some power of \(D\). A slice
is an element \(s\) with \(Ds=1\). The slice theorem then gives
\(R=(\ker D)[s]\). A local slice instead satisfies
\(Dr=g\ne0\) and \(Dg=0\); after inverting \(g\),
\(R_g=(\ker D)_g[r/g]\).[^2]

The cancellation question is equivalent to asking whether every
slice locally nilpotent derivation of \(\mathbb C^{[4]}\) has kernel
\(\mathbb C^{[3]}\). The slice theorem alone only gives a polynomial
extension of an unknown three-ring. It does not identify that ring.

This report studies extensions which already have a polynomial base
\(R\), a nonzero locally nilpotent derivation \(D\) of \(R\), and
an extra variable \(t\). The general theorem in Section 2 allows any
domain \(R\) over a characteristic-zero field. Polynomial-kernel conclusions
specialize to \(R=\mathbb C^{[3]}\).

## 2. An invariant-ring matrix-lift theorem

Let \(k\) be a field of characteristic zero, let \(R\) be a \(k\)-domain,
and let \(0\ne D\in\operatorname{LND}(R)\). Put \(C=\ker D\),
choose \(r\in R\) with \(Dr=g\in C\setminus\{0\}\), and take
\[
A,B,Q\in C,\qquad B=1+gQ,\qquad
E=AD+B\partial_t\quad\text{on }R[t].
\tag{1}
\]
The derivation \(D\) kills \(t\). The two summands defining \(E\)
commute and are locally nilpotent, so \(E\) is locally nilpotent.

**Theorem.** Under precisely these hypotheses, the following conditions
are equivalent: \(E\) has a slice; \((A,B)C=C\);
\((gA,B)C=C\); and \(E\) is conjugate to \(\partial_t\) by a
polynomial algebra automorphism of \(R[t]\). In the positive case
the automorphism and its inverse are explicit. No finite generation
of \(C\), coordinate assumption on \(r\) or \(g\), or elementary
matrix factorization is required.

The field hypothesis matters. Over \(\mathbb Z[x,y,t]\),
\(D=\partial_x+x\partial_y\) has slice \(x\), but is not conjugate
to \(\partial_t\): after reduction modulo two, \(D^2(y)=1\),
whereas \(\partial_t^2\) is zero. Merely assuming that a domain has
characteristic zero would incorrectly include this example. The
finite flow uses the inverses of factorials.

### 2.1. Completion of the row

Suppose \(AU+BV=1\), with \(U,V\in C\). Define
\[
L=-QU,\qquad M=AU+V.
\]
Then
\[
BM+gAL=1,\qquad M-1=-gQV.
\tag{2}
\]
Conversely, the first identity gives \((A,B)C=C\). Since
\(B-gQ=1\), the unit-ideal conditions on \((A,B)\) and \((gA,B)\)
are equivalent. In particular both \((B-1)/g\) and \((M-1)/g\)
belong to \(C\).

### 2.2. Polynomial maps and their inverse

For an independent variable \(T\), let
\[
\theta_T(f)=\sum_{j\ge0}\frac{T^j}{j!}D^j(f),\qquad f\in R.
\]
Each sum is finite. Evaluation at a polynomial parameter is an algebra
homomorphism. Set
\[
W=Qr-At,\qquad W'=\frac{M-1}{g}r+At,
\tag{3}
\]
and define homomorphisms \(\Phi,\Psi:R[t]\to R[t]\) by
\[
\begin{aligned}
\Phi(f)&=\theta_W(f),&\Phi(t)&=Lr+Mt,\\
\Psi(f)&=\theta_{W'}(f),&\Psi(t)&=-Lr+Bt
\end{aligned}
\qquad(f\in R).
\tag{4}
\]
They fix \(C\). On the pair \((r,t)\), their matrices are
\[
\begin{pmatrix}B&-gA\\L&M\end{pmatrix},\qquad
\begin{pmatrix}M&gA\\-L&B\end{pmatrix}.
\tag{5}
\]
Equation (2) makes them inverse matrices of determinant one.

Localizing at \(g\) gives \(R_g[t]=C_g[r/g,t]\). Thus (5) proves
that the extended maps are inverse on the entire localized ring, not
just on two selected elements. Localization is injective because
\(R[t]\) is a domain and \(g\ne0\). Therefore already over
\(R[t]\),
\[
\Phi\Psi=\Psi\Phi=\mathrm{id}.
\tag{6}
\]
Equivalently, direct substitution gives \(\Phi(W')=-W\) and
\(\Psi(W)=-W'\); the finite flow group law gives the same inverse.

An important distinction is that \(\theta_W\) is flow evaluation,
not the operator exponential \(\exp(WD)\). Indeed
\(DW=gQ=B-1\) can be nonzero. No local nilpotence of \(WD\)
is asserted or needed.

### 2.3. The invariant coordinates and slice

Since \(E\) kills \(C\),
\[
EW=QgA-AB=-A.
\]
Applying \(E\) to the finite sum in (4), the derivative of \(W^j\)
cancels the term from \(AD^{j+1}f\). Hence
\[
E\Phi(f)=0\quad(f\in R),\qquad E\Phi(t)=gAL+BM=1.
\tag{7}
\]
Together with (6), this proves
\(\Phi^{-1}E\Phi=\partial_t\), so \(\ker E=\Phi(R)\).
For \(R=k[x_1,x_2,x_3]\), the four elements
\(\Phi(x_1),\Phi(x_2),\Phi(x_3),Lr+Mt\) are polynomial
coordinates. The first three generate the kernel.

### 2.4. Necessity, without a degree bound on the slice

Suppose \(ES=1\) for some \(S\in R[t]\). If \(B\) is a unit
in \(C\), the unit-ideal conclusion is immediate. Otherwise reduce
modulo \(B\). In \(C/(B)\), the element \(g\) is a unit with
inverse \(-Q\). The local-slice presentation therefore gives
\[
R[t]/BR[t]\simeq (C/(B))[\rho,t],\qquad \rho=r/g.
\tag{8}
\]
Here the induced derivation is \(\overline A\partial_\rho\).
The equation \(\overline A\partial_\rho\overline S=1\), evaluated
at \(\rho=t=0\), exhibits an inverse for \(\overline A\) in
\(C/(B)\). Consequently \(AU+BV=1\) for some \(U,V\in C\).

This argument remains valid when \(C/(B)\) is nonreduced. It does
not infer that units of a polynomial ring over a nonreduced ring are
constant: it evaluates an explicit polynomial inverse. It also covers
\(B=0\), when (1) itself forces \(g\) to be a unit. This completes
the theorem.

The same statement with \(B\equiv\beta\pmod{gC}\),
\(\beta\in k^*\), follows by applying the theorem to \(E/\beta\).
For a coefficient \(f\in R\) not in \(C\), an exhibited identity
\(f=B+A D(H)\) allows the shear \(t\mapsto t+H\) to conjugate
\(AD+f\partial_t\) to (1). Existence of this identity for every
slice extension is not proved.

## 3. A two-invariant example beyond elementary row reduction

Let \(\eta\in C\) be arbitrary. Take
\[
A=g^2,\quad B=1+g\eta,\quad
L=-\eta^3,\quad M=1-g\eta+g^2\eta^2.
\tag{9}
\]
Then \(BM+gAL=1\). The theorem gives a coordinate slice
\[
s=(1-g\eta+g^2\eta^2)t-\eta^3r
\]
and invariant coordinates \(\theta_W(x_i)\), where
\(W=\eta r-g^2t\). Formulas (3)-(6) give the full polynomial inverse,
including when \(D\) has rank three. This is not merely a certificate
that \(Es=1\).

If \(g,\eta\) are algebraically independent, the coefficient row
\((g^2,1+g\eta)\) is not elementarily reducible over
\(k[g,\eta]\). This follows from Cohn's original example
\[
\begin{pmatrix}1+xy&x^2\\-y^2&1-xy\end{pmatrix}
\in\mathrm{SL}_2(k[x,y])\setminus E_2(k[x,y]).
\]
If its first row could be reduced to \((1,0)\) by elementary
matrices, the resulting determinant-one lower triangular matrix would
itself be elementary, contradicting Cohn's theorem.[^3]

The obstruction concerns elementary operations over that particular
subring. It is not an obstruction to all polynomial coordinate changes
or necessarily to elementary operations over a larger invariant ring.
Equations (3)-(9) explicitly demonstrate the distinction.

## 4. Complete one-parameter normal forms

There is a complementary classification without the congruence in (1)
when both coefficients depend on one nonconstant local-slice derivative.
Assume \(R=\mathbb C^{[3]}\), \(Dr=g\ne0\), \(Dg=0\), and
\(g\notin\mathbb C\). For nonzero coefficient pair
\(A(u),B(u)\in\mathbb C[u]^2\), let \(h\) be their monic gcd
and put \(a=A/h,b=B/h\). There is a polynomial automorphism \(F\),
fixing \(g\), with
\[
F\bigl(A(g)D+B(g)\partial_t\bigr)F^{-1}=
\begin{cases}
h(g)b(0)\partial_t,&b(0)\ne0,\\
h(g)a(0)D,&b(0)=0.
\end{cases}
\tag{10}
\]
Notice the conjugation orientation differs from the choice of \(\Phi\)
in Section 2.

The available automorphisms are
\(\exp(tH(g)D)\) and \(\exp(rK(g)\partial_t)\). Their exact
coefficient-row operations are
\[
(A,B)\mapsto(A-HB,B),\qquad
(A,B)\mapsto(A,B-uKA).
\tag{11}
\]
For a coprime pair with \(B(0)\ne0\), divide \(A\) by \(B\).
The first move leaves \(A_1\) with \(\deg A_1<\deg B\). Unless
\(B\) is already constant, coprimality makes \(A_1\ne0\). Divide
\(B\) by \(uA_1\) and use the second move. Its remainder \(B_1\)
satisfies \(\deg B_1\le\deg A_1<\deg B\) and
\(B_1(0)=B(0)\). Each cycle decreases \(\deg B\), and a final
upper move yields \((0,B(0))\).

If \(B(0)=0\), write \(B=uC_1\). The auxiliary pair \((C_1,A)\)
is coprime and has \(A(0)\ne0\). The preceding algorithm applies
with upper and lower moves interchanged, giving \((A(0),0)\) in
the original pair. Applying these moves to \((a,b)\) preserves the
common factor \(h(g)\) and proves (10).

Every nonzero derivation in (10) has abstract kernel
\(\mathbb C^{[3]}\). The translation branch has kernel \(R\);
the base branch has kernel \((\ker D)[t]\), and Miyanishi's theorem
gives \(\ker D\simeq\mathbb C^{[2]}\).[^2] A slice exists exactly
when \(h=1\) and either \(b(0)\ne0\) or \(D\) itself has a slice.
Indeed a nonconstant \(h(g)\) is a nonunit dividing every derivative;
for the base branch, evaluate any proposed slice at \(t=0\).

The zero pair is excluded and has no slice. If \(g\) is a nonzero
constant, evaluate \(A,B\) at that constant first; the formal gcd
criterion no longer applies, and \(r/g\) is already a base slice.
No claim about nonunits is transferred to arbitrary localized rings.
The [full normal-form proof](research/extension-mixing-pass15.md)
includes each zero-coefficient boundary and explicit shear variants.

## 5. Fixed schemes of the induced quotient action

Now allow an arbitrary coefficient \(f\in R=\mathbb C^{[3]}\),
and suppose \(E=D+f\partial_t\) has a slice \(s\). Put
\(U=\partial_t\), \(K=\ker E\), \(d=U|_K\), and \(q=Us\).
Then \(R[t]=K[s]\), \(q\in K\), and
\(U=d+q\partial_s\). The common invariant ring is
\(C=\ker D=\ker d\).

For a derivation \(L\) on an algebra \(T\), let \(I_L\) be the
ideal generated by \(L(T)\). Define the intrinsic ideal
\[
J=(E(a)U(b)-U(a)E(b):a,b\in R[t]).
\]
In the presentation \(R[t]\), the wedge is \(D\wedge\partial_t\).
In \(K[s]\), it is \(\partial_s\wedge d\). Testing one argument
equal to \(t\), respectively \(s\), proves the full ideal equality
\[
J=I_D R[t]=I_d K[s].
\tag{12}
\]
This is an equality of ideals, not just their radicals.

Modulo \(J\), the first presentation has
\(\overline E=\overline f\partial_t\). The slice equation forces
\(\overline f\) to be a unit of \(R/I_D\), and
\(\overline s=\overline f^{-1}t+\overline h\). Thus the kernel of
\(\overline E\) is \(R/I_D\). In the other presentation that kernel
is \(K/I_d\). Hence there is a canonical \(C\)-algebra isomorphism
\[
R/I_D\simeq K/I_d.
\tag{13}
\]
It preserves the nonreduced fixed schemes. In particular
\(I_D\cap C=I_d\cap C\), and \(d\) is fixed-point-free exactly
when \(D\) is fixed-point-free.

Kaliman proves that every fixed-point-free additive action on
\(\mathbb C^3\) is a translation.[^4] Consequently a rank-three
base derivation \(D\) makes this induced \(d\) necessarily nonfree,
regardless of \(f\) and the degree of the slice. The strategy of
proving that this particular induced action is free cannot close the
rank-three extension problem. A different intrinsic action is not
excluded.

## 6. The plinth radicals agree

Write \(P_D=D(R)\cap C\) and \(P_d=d(K)\cap C\). Then
\[
\sqrt{P_D}=\sqrt{P_d}\quad\text{as ideals of }C.
\tag{14}
\]
To prove the first inclusion, take \(0\ne g=Dr\in P_D\) and
\(\rho=r/g\). On \(R_g=C_g[\rho]\), integrate the polynomial
\(f\) with respect to \(\rho\), obtaining \(D(F)=f\).
The element \(v=t-F\) satisfies \(Ev=0\), \(Uv=1\), and
\(K_g=C_g[v]\). Clearing a power of \(g\) from \(v\) gives
\(g^N\in P_d\).

Conversely, for \(0\ne h=dv\in P_d\), write
\(K_h=C_h[\sigma]\), \(\sigma=v/h\). On \(K_h[s]\),
\(U=\partial_\sigma+q\partial_s\). Integrating \(q\) in
\(\sigma\) gives \(F\in K_h\), and \(w=s-F\) has \(Uw=0\),
\(Ew=1\). Therefore \(R_h=C_h[w]\), and clearing denominators
gives \(h^N\in P_D\). Both ideals have nonzero elements since
both derivations are nonzero locally nilpotent derivations. This
proves (14), without claiming equality of plinth multiplicities.

The [quotient comparison note](research/commuting-quotient-pass15.md)
contains the full reconstruction and explicit reduced and nonreduced
controls. Fixed-scheme equality alone does not identify either
three-dimensional ambient algebra.

## 7. Reproducible certificates and verification limits

The [row solver](research/invariant_mixing_solver.py) uses exact
standard-library rational arithmetic and emits immutable internal
certificates as JSON. The separate
[verifier](research/invariant_mixing_verifier.py) recomputes the gcd,
checks the primitive coefficients and branch, replays every operation,
and checks the final row using SymPy. It does not import solver
internals. Its tests invoke the solver as an untrusted external
certificate producer and bind the answers to the requested inputs.

From the project directory, reproduce a nonconstant example with:

```sh
python3 research/invariant_mixing_solver.py --a '["-1","1"]' --b '["1","1"]' | /opt/anaconda3/bin/python research/invariant_mixing_verifier.py --certificate -
/opt/anaconda3/bin/python research/invariant_mixing_verifier.py --self-test
```

Coefficient lists are in ascending powers of the formal parameter.
The verifier explicitly reports that the supplied derivation's local
nilpotence, polynomial-base hypothesis and chosen local-slice identity
remain external hypotheses. A row certificate alone cannot establish
them. Its scope is conditional row reduction, not arbitrary
cancellation or proof-assistant verification.

The new suite checks 728 nonzero pairs of quadratic polynomials with
coefficients in \(\{-1,0,1\}\), rational and higher-degree cases,
malformed and forged certificates, matrix inverse identities,
invariant coordinates, slices and fixed-scheme controls. The finite
grid is one test method, not 728 independent theorem proofs.
The complete regression results and actual commands are recorded in
[verification-pass-15.json](verification-pass-15.json).
There are 330 passing test methods in 23 suites, including 23 in the
new suite. The additional integer-base control checks the necessity
of the characteristic-zero field hypothesis. Two quotient controls
check the boundary in the following section.

## 8. Quotient-slice conditions and a failed congruence reduction

For arbitrary \(A,B\in C=\ker D\), suppose
\(E=AD+B\partial_t\) has a slice \(S=\sum_j s_jt^j\).
Its constant coefficient gives
\[
A D(s_0)+Bs_1=1.
\tag{15}
\]
Thus on \(\overline R=R/BR\), \(\overline A\) is a unit and
\(\overline D(\overline A\,\overline{s_0})=1\). The reduced base
action must itself have a slice. These necessary conditions do not
assume the congruence in Section 2.

The affine-in-\(t\) question has an exact algebraic formulation.
Writing \(P_D=D(R)\cap C\), a slice of the form \(r+ht\)
exists exactly when \(A P_D+BC=C\). For \(A\ne0\), the
coefficient of \(t\) forces \(Dh=0\), and applying \(D\) to
the constant equation forces \(D^2r=0\). Conversely a relation
\(A Dr+Bh=1\) with \(Dr,h\in C\) supplies that slice.
For \(A=0\), both conditions reduce to \(B\) being a unit.
An arbitrary polynomial slice has not been proved to imply this
affine-slice criterion.

One cannot automatically identify its kernel with \(C/(B)\).
For \(D=x\partial_y+2y\partial_z\) and \(B=x\), the original
kernel is \(\mathbb C[x,xz-y^2]\). After reduction modulo \(x\),
\(\overline D=2y\partial_z\) has kernel \(\mathbb C[y]\), while
the image of \(C/(x)\) is only \(\mathbb C[-y^2]\). This example
illustrates failure of invariant base change; it is not a positive
slice example for (15).

Even comaximality of \(B\) with the whole plinth ideal would not,
by itself, supply a local-slice value \(g\) with
\(B\equiv c\pmod g\) for a nonzero scalar \(c\). Take
\[
R=\mathbb C[u,v,w],\quad D=(uv-1)\partial_w,\quad B=u.
\]
Here \(C=\mathbb C[u,v]\), \(P_D=(uv-1)C\), and
\((B,P_D)=C\), because \(uv-(uv-1)=1\). The extension
\(E=(uv-1)\partial_w+u\partial_t\) is explicitly a translation:
\[
h=uw-(uv-1)t,\qquad s=-w+vt,
\]
\[
w=vh+(uv-1)s,\qquad t=h+us,
\tag{16}
\]
with \(Eh=0\), \(Es=1\). Nevertheless every nonzero local-slice
value of \(D\) is divisible by \(uv-1\), and \(u\) is a
nonconstant unit in
\(C/(uv-1)\simeq\mathbb C[u,u^{-1}]\). Therefore no such value
can divide \(u-c\) for any scalar \(c\).

This closes a specific proposed inference, not cancellation and not
every possible change of base derivation. The base in this example
has rank one, so it does not rule out a separately proved rank-three
refinement. The important unresolved issue is more precise: a unit
modulo a plinth ideal need not be a scalar modulo it.

The [quotient-slice boundary note](research/quotient-slice-boundary-pass15.md)
also records the exact obstruction module for invariant base change,
and a localized-base counterexample to abstract quotient-slice lifting.
That localized example is explicitly not a polynomial-threefold
counterexample. It cannot settle the unlocalized case by analogy.

## 9. Exact scope and the next unresolved implication

Sections 2-4 finish the stated coefficient families in all degrees.
They do not show that an arbitrary slice derivation admits a commuting
coordinate partial, nor that an arbitrary extension coefficient has
an invariant remainder satisfying the required congruence after a
polynomial change of coordinates. Those are substantial missing
implications, not implementation details.

The nearest audited extension results have stronger premises.
Freudenburg's Proposition 7.1 requires intersection identities for all
image ideals and describes a kernel algebra rather than proving it
polynomial. Theorem 7.6 assumes a fundamental pair and a specified
invariant grading.[^2] These hypotheses are not consequences of merely
commuting with \(\partial_t\). The
[statement-level literature audit](research/extension-mixing-literature-pass15.md)
records the comparisons and their limits. A bounded search failing
to locate this exact matrix lift does not establish originality.

The next useful algebraic question is whether the quotient-slice
condition in Section 8 can be lifted to a polynomial coordinate
construction without the scalar congruence of Section 2. Neither
invariant base change nor comaximality alone supplies that implication.
The fixed-scheme theorem rules
out trying to replace that argument with freeness of the particular
induced quotient action when the base has rank three. The full
cancellation goal remains unresolved.

## Sources

[^1]: Hongdi Huang, Zahra Nazemian, Yanhua Wang and James J. Zhang,
    [*Relative Cancellation*](https://arxiv.org/html/2503.10083v3),
    arXiv:2503.10083v3, November 9, 2025, introduction. Used only for
    the dated status of characteristic-zero cancellation.

[^2]: Gene Freudenburg,
    [*Actions of SL2(k) on Affine k-Domains and Fundamental Pairs*](https://arxiv.org/pdf/2108.12021),
    arXiv:2108.12021v2, June 7, 2022; published in
    *Transformation Groups* 29 (2024), 959-1003. Section 2.2 gives
    local slices; Theorem 2.4(a) records Miyanishi's kernel theorem;
    Proposition 7.1 and Theorem 7.6 supply the precise extension
    comparisons, not the matrix-lift theorem proved here.

[^3]: P. M. Cohn,
    [*On the structure of the GL2 of a ring*](https://www.numdam.org/item/PMIHES_1966__30__5_0.pdf),
    *Publications Mathématiques de l'IHÉS* 30 (1966), 5-53,
    Proposition 7.3 and the example on printed page 26.
    DOI: [10.1007/BF02684355](https://doi.org/10.1007/BF02684355).

[^4]: Shulim Kaliman,
    [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
    *Inventiones Mathematicae* 156 (2004), 163-173, Theorem 1.
