# An additive local-slice step preserves the explicit kernel lift

This is a bounded induction bridge, not a reduction of all rank-three
derivations to local-slice chains. Starting from the pass-18 polynomial-curve
base, one additional additive local-slice construction retains polynomial
kernels for every invariant slice extension. The genuine rank-three branch
uses a finite reparametrization of a curve in a nilpotent surface. No
correction to the new local-slice polynomial \(Q\) is needed.

The argument below is a working algebraic proof, not a novelty claim or
external review. A [separate full reconstruction](proof-audits-pass19.md)
found no actionable algebraic gap. The
[independent four-method checker](iterated_local_slice_checks_pass19.py)
passed in the original 0.647-second run and the
[complete main regression](../verification-pass-19.json).
Its finite cases supplement, rather than prove, the general assertions.

## 1. The exact next step and the reversal trap

Use the notation of [pass 18](polynomial-curve-lift-pass18.md):
\[
f=xz-F(y),\quad r=xP(x,f)+yf^n,\quad
K(f,T)=G(T,f^n)+f^{nd+1},\quad xh=K(f,r),
\]
where \(F\) is monic of degree \(d\ge2\), \(n\ge1\),
\(\deg_xP(x,0)\ge1\), and \(G(T,S)=S^dF(T/S)\).
Let \(D_1=-\operatorname{Jac}(f,h,\cdot)\). The earlier proof gives
\(\ker D_1=\mathbb C[f,h]\), primitivity, and \(D_1r=f^nh\).

Choose any \(Q(f,h)\in\mathbb C[f,h]\), and set
\[
r_2=r+hQ(f,h),\qquad
k=K(f,r_2)/h
  =x+Q(f,h)\,\Delta_G(r_2,r;f^n),
\tag{1}
\]
where \(\Delta_G(a,b;S)\) is the polynomial divided difference
\((G(a,S)-G(b,S))/(a-b)\), including at equal arguments.
These are polynomials and \(hk=K(f,r_2)\).

Modulo \(h\), \(r_2=r\), so its minimal irreducible relation over
\(\mathbb C[f]\) is still \(K\). This follows from the exact
\(f\)-localized presentation and contraction of the prime ideal
\((K)\); \(K\) is monic and irreducible, and is not divisible by
\(f\). Thus (1) is an actual application of Freudenburg's local-slice
construction, not just a formal Jacobian ansatz.[^1]

With the sign convention
\[
D_2=\operatorname{Jac}(f,k,\cdot),
\]
one has
\[
D_2r_2=f^nk,\qquad D_2h=f^nG_R(r_2,f^n).
\tag{2}
\]
For \(Q=0\), (1) gives \(k=x\), so this step simply returns
\(x\partial_y+F'(y)\partial_z\). Reusing the original local
slice is a reversal, not an increase in construction depth.

More generally, if \(Q=f^nT(f,h)\), the flow
\(\exp(TD_1)\) sends \(r\) to \(r_2\) and \(x\) to
\(k\). Consequently \(D_2\) is conjugate to that same triangular
reversal. The weaker condition \(f\mid Q\) also gives rank two,
but needs the finite argument in Section 3.

## 2. All denominator ideals and the exact surface mutation

The first and second surface charts are related by polynomial maps:
\[
(x,h,r)\longmapsto(h,k,r_2),\qquad
r_2=r+hQ,\quad k=x+Q\Delta_G(r_2,r;f^n),
\tag{3}
\]
and
\[
r=r_2-hQ(f,h),\qquad
x=k-Q(f,h)\Delta_G(r_2,r;f^n).
\tag{4}
\]
They identify the abstract surfaces
\[
\mathcal S_K=
\mathbb C[f,x,h,r]/(xh-K(f,r)),
\quad
\mathbb C[f,h,k,r_2]/(hk-K(f,r_2)).
\tag{5}
\]
No localization is needed for (3)-(5). The physical ring is not
silently identified with this surface ring: it also contains
\[
y=\frac{r-xP(x,f)}{f^n},\qquad
z=\frac{h-T_F(x,y,P(x,f),f)}{f^{nd}},
\tag{6}
\]
where \(T_F\) is the Taylor sum from pass 18. Thus
\(R_f=(\mathcal S_K)_f\), and the only remaining denominator
ideals in (6) are \((f^n)\) and \((f^{nd})\). The maps (3)-(4)
do not prove that they preserve this particular overring \(R\).
That is the divisibility issue addressed below.

The exact second chart is
\[
R_f=\mathbb C[f^{\pm1},h,k,r_2]/(hk-K(f,r_2)).
\tag{7}
\]
It proves local nilpotence in (2), and its monic normal basis
\(h^b r_2^i\), \(0\le i<d\), has distinct derivative degrees
\(db+i\). Hence its invariant ring is \(\mathbb C[f^{\pm1},k]\),
and its degree-at-most-one module has basis \(1,r_2\).

## 3. Kernel, primitivity, and the rank-two/rank-three dichotomy

Put \(P_0=P(x,0)\), \(a=\deg P_0\ge1\), and
\[
H_0=x^{d-1}P_0^d,\quad R_0=xP_0,\quad q_0(H)=Q(0,H),
\]
\[
L_0=1+x^{d-2}P_0^{d-1}q_0(H_0).
\]
Then
\[
k\bmod f=k_0=xL_0^d,\qquad
r_2\bmod f=T_0=R_0L_0.
\tag{8}
\]
The polynomial \(k_0\) is nonconstant. Contracting the invariant
ring in (7), using (8), therefore gives
\(\ker D_2=\mathbb C[f,k]\).

Both \(f,k\) are prime in \(R\), by factorial closure of this
exact kernel. Every coefficient gcd divides \(D_2r_2=f^nk\).
The degree-\(d-1\) polynomial \(G_R\) is nonzero modulo the
monic degree-\(d\) relation in (7), so \(k\nmid D_2h\).
Also
\[
D_2y\equiv xk_0'(x)\pmod f,
\]
which is nonzero. This last formula follows directly by substituting
\(k=k_0(x)+f\cdot(\text{polynomial})\) in its Jacobian. Thus
\(D_2\) is primitive for every \(Q\).

If \(q_0\ne0\), write \(b=\deg q_0\ge0\) and
\(e=d(a+1)-1\). Formula (8) gives
\[
\deg T_0=e(b+1),\qquad \deg k_0=e(db+d-1).
\]
Except when \(d=2,b=0\), the latter degree is larger, so
\(T_0\notin\mathbb C(k_0)\). In the exception, write \(q_0=c\ne0\).
The two degrees coincide, but
\[
T_0-k_0/c=-x(P_0+1/c)
\]
is nonconstant of smaller degree. A polynomial in \(x\) lying in
\(\mathbb C(k_0)\) must be polynomial in \(k_0\): a denominator
coprime to its numerator cannot cancel after substituting \(k_0\).
Equal degrees would therefore force an affine dependence, which the
last display excludes.

As in pass 18, a negative \(f\)-pole in
\(b(f,k)+c(f,k)r_2\) would give a nontrivial relation
\(b_0(k_0)+c_0(k_0)T_0=0\). Hence
\[
\ker D_2^2=\mathbb C[f,k]\oplus\mathbb C[f,k]r_2,
\qquad P_{D_2}=f^nk\mathbb C[f,k].
\tag{9}
\]
Primitivity and the published rank-at-most-two local-slice criterion
then give rank three, exactly as in pass 18.[^1]

If \(q_0=0\), use the same formulas before reduction modulo \(f\),
in the ring \(S_n=\mathbb C[f]/(f^n)\):
\[
H=x^{d-1}P(x,f)^d,\quad
L=1+x^{d-2}P(x,f)^{d-1}Q(f,H).
\]
Modulo \(f^n\), one has \(k=xL^d\), \(r_2=xPL\), and
\(L\equiv1\pmod f\). The polynomial \(x\mapsto xL^d\)
has a finite inverse in \(S_n[x]\). Substituting that inverse in
\(xPL\) produces \(\psi(f,k)\) with
\(r_2-\psi(f,k)\in f^nR\). Thus
\[
u=(r_2-\psi(f,k))/f^n\in R,\qquad D_2u=k.
\tag{10}
\]
Since \(k\) is a coordinate of the invariant ring, the published
local-slice criterion makes it an ambient coordinate.[^1] Therefore
\(D_2\) has rank at most two. By the principal-plinth theorem, its
plinth containing \((k)\) is generated by a divisor of \(k\).
Its plinth is exactly \((k)\):
the only alternative is a unit, which would give
\(R=\mathbb C[f,k][s]\), making \(f\) an ambient coordinate.
But \(f=xz-F(y)\) has a critical point \((0,c,0)\) at any root
\(c\) of \(F'\), and so cannot be a coordinate. This also excludes
primitive rank one. In this branch \(D_2\) has rank two, and every
invariant slice extension has polynomial kernel by the known
ambient-invariant-coordinate result.[^2]

## 4. Finite curve reparametrization lemma

Let \(S_n=\mathbb C[f]/(f^n)\), and consider the surface ring
\[
\mathcal C_n=S_n[x,h,r]/(xh-r^d).
\]
Its vertex ideal is \((x,h,r)\). Let \(\alpha\) be a polynomial
automorphism of this ring preserving that ideal and reducing to the
identity modulo \(f\). Evaluate its coordinate formulas on the curve
\[
(x,h,r)=(u,u^{d-1}P(u,f)^d,uP(u,f)).
\]
Vertex preservation gives polynomials \(U,V\in S_n[u]\) such that
\[
\alpha(x)=uU(u,f),\qquad \alpha(r)=uV(u,f),\qquad
U\equiv1\pmod f.
\tag{11}
\]
Here these equalities mean evaluation on the displayed curve.
Thus \(U\) is a unit. The map
\(\beta(u)=uU(u,f)=u+fW(u,f)\) has a polynomial inverse
\(j(X,f)\) over \(S_n\): iterate \(j_{i+1}=X-fW(j_i,f)\),
starting with \(j_0=X\), for \(n-1\) steps. Each update improves
the error by one power of \(f\).

Define the finite polynomial jet
\[
\widetilde P(X,f)=\bigl(V/U\bigr)(j(X,f),f).
\tag{12}
\]
The surface relation gives
\[
\alpha(h)=u^{d-1}V^d/U
          =\beta(u)^{d-1}\widetilde P(\beta(u),f)^d.
\]
The cancellation of \(u\) here is legitimate: the indeterminate
\(u\) is a nonzerodivisor in \(S_n[u]\), despite the nilpotents in
\(S_n\). Consequently \(\alpha\) carries the entire \(P\)-curve
isomorphically to the \(\widetilde P\)-curve, with parameter
\(X=\beta(u)\). Its inverse carries the latter curve back, with
parameter \(u=j(X,f)\). This inverse statement holds after any
specialization to an \(S_n\)-algebra; it is not merely a calculation
at reduced points. Also \(\widetilde P(X,0)=P(X,0)\).

## 5. Constructing the extension's invariant coordinates

Consider \(E=AD_2+B\partial_t\), with \(A,B\in\mathbb C[f,k]\).
In the genuine rank-three branch, the pass-17 affine-replacement theorem
and (9) give exactly the slice criterion
\[
(A,B)=1,\qquad B=c+fkJ(f,k),\qquad c\ne0.
\tag{13}
\]
This necessity retains the source-dependent geometric premise of pass 17.
The sufficiency and coordinate construction below use only (13).
Scale both coefficients and \(E\) by \(c^{-1}\), so \(c=1\).
Choose \(U_1,V_1\in\mathbb C[f,k]\) with
\(Af^nkU_1+BV_1=1\), and set
\[
\rho=Br_2-Af^nk t,\qquad
\sigma=U_1r_2+V_1t.
\tag{14}
\]
Then \(E\rho=0\), \(E\sigma=1\), and
\(r_2=V_1\rho+Af^nk\sigma\), \(t=-U_1\rho+B\sigma\).

The invariant polynomial
\[
\widehat h=K(f,\rho)/k
=h+\frac{\rho-r_2}{k}\Delta_G(\rho,r_2;f^n)
\tag{15}
\]
is well defined: \(\rho-r_2\) is divisible by \(k\), since
\(B\equiv1\pmod k\). Reverse the mutation polynomially:
\[
\widehat r=\rho-\widehat hQ(f,\widehat h),\qquad
\widehat x=k-Q(f,\widehat h)\Delta_G(\rho,\widehat r;f^n).
\tag{16}
\]
They satisfy \(\widehat x\widehat h=K(f,\widehat r)\).
All three quantities are \(E\)-invariant.

Modulo \(f^n\), the mutation (3) becomes a vertex-preserving
automorphism \(\mu\) between two copies of the cone \(xh=r^d\).
On its target copy the last-slice transformation is exactly
\[
(h,k,r_2)\longmapsto(B^dh,k,Br_2).
\]
It is an automorphism because \(B\equiv1\pmod f\), and its
inverse replaces \(B\) by \(B^{-1}\), evaluated at the fixed \(k\).
Thus the transformation in (15)-(16) reduces to
\(\alpha=\mu^{-1}\circ\sigma_B\circ\mu\), which preserves
the vertex and is the identity modulo \(f\).

Apply Section 4 to this \(\alpha\), and choose the representative
\(\widetilde P\in\mathbb C[X,f]\) of degree less than \(n\)
in \(f\). Then
\[
Y=\frac{\widehat r-\widehat x\widetilde P(\widehat x,f)}{f^n}
\tag{17}
\]
is polynomial. Since \(\widehat x\equiv x\pmod f\), it is
coprime to the prime \(f\). Taylor's identity now gives the polynomial
\[
Z=\frac{\widehat h-
 T_F(\widehat x,Y,\widetilde P(\widehat x,f),f)}{f^{nd}},
\qquad f=\widehat xZ-F(Y).
\tag{18}
\]
The numerator's divisibility follows by multiplying it by
\(\widehat x\), obtaining \(f^{nd}(F(Y)+f)\), and using
coprimality in the polynomial UFD. In particular, the second-stage
polynomial \(Q\) has not been changed; only \(P\) was corrected.

## 6. Polynomial inverse, including the other direction of the jet

In independent coordinates \((X,Y,Z,\sigma)\), set
\[
f=XZ-F(Y),\quad
\widehat r=X\widetilde P(X,f)+Yf^n,\quad
\widehat h=T_F(X,Y,\widetilde P(X,f),f)+Zf^{nd}.
\]
Apply the forward mutation (3) to obtain \(\rho,k\). Evaluate
\(A,B,U_1,V_1\) at \(f,k\), and recover \(r_2,t\) by the
inverse of (14). Since \(V_1\equiv1\pmod k\),
\[
h=\widehat h+
 \left(\frac{V_1-1}{k}\rho+Af^n\sigma\right)
 \Delta_G(r_2,\rho;f^n)
\tag{19}
\]
is polynomial and satisfies \(hk=K(f,r_2)\). Apply (4) to recover
polynomial \(r,x\).

Modulo \(f^n\), this is exactly \(\alpha^{-1}\) on the
\(\widetilde P\)-curve, since \(BV_1=1\) there. Section 4 gives
\(r-xP(x,f)=0\) in that quotient and \(x\equiv X\pmod f\).
Thus \(y=(r-xP(x,f))/f^n\) is polynomial. The same Taylor identity
and \(\gcd(x,f)=1\) then make
\(z=(h-T_F(x,y,P(x,f),f))/f^{nd}\) polynomial.

Substitution in the original ring recovers \(r_2,t\) by the inverse
matrix, then \(h,r,x\) by the surface identities and inverse mutation,
and finally \(y,z\) by (6). This gives a surjection between two
polynomial four-rings; equality of dimensions makes it injective.
Therefore \(E\) is a coordinate translation and its kernel is
\(\mathbb C^{[3]}\). Nothing is inferred from an unspecified
formal completion: (11)-(12) use a finite jet, while (15)-(19) give
the actual global polynomial maps and their inverse.

## 7. A genuine negative control and its repair

Take \(F(y)=y^2\), \(P=x^2\), \(n=2\), and \(Q(f,h)=h\).
Then
\[
r_2=r+h^2,\qquad k=x+2hr+h^3.
\]
The new base has rank three and plinth \(f^2k\), by Section 3.
For \(A=1,B=1+fk\), (15)-(16) give invariant
\(\widehat h,\widehat r,\widehat x\). Put
\(k_0(x)=x(1+x^7)^2\). Direct reduction modulo \(f^2\) gives
\[
\widehat r-\widehat x^3
 =fk_0(x)x^3(1+15x^7)\pmod{f^2}.
\tag{20}
\]
The coefficient is nonzero, so the uncorrected formula
\((\widehat r-\widehat x^3)/f^2\) has an actual \(f\)-pole.
This is a counterexample to naive preservation of the old coordinate
formula, not to polynomiality of the kernel.

The finite curve correction is explicit at this order:
\[
\widetilde P(X,f)=X^2+
 fX^3(1+X^7)^2(1+15X^7)\pmod{f^2}.
\tag{21}
\]
The checker verifies both forward and independently reconstructed inverse
curve congruences at orders \(n=2\) and \(n=3\). It also checks
the lower-coefficient surface mutation and the finite primitive correction
in the \(f\mid Q\) branch. Its full command is

```sh
/opt/anaconda3/bin/python research/iterated_local_slice_checks_pass19.py
```

## 8. The precise finite-chain corollary and its limit

The argument in Sections 4–6 only uses that \(\mu\) is a polynomial
isomorphism of \(\mathcal S_K\), that its reduction preserves the
cone vertex, and that the physical denominators remain those in (6).
It therefore applies to a finite composition of the additive mutations
(3), not just one such map. Each inverse remains polynomial, and
conjugating the final scaling still gives a vertex-preserving
automorphism congruent to the identity modulo \(f\).

For such a finite chain, retain as explicit hypotheses that the final
derivation has invariant ring \(\mathbb C[f,k]\), a local slice
\(r_*\) with derivative \(f^nk\), and that the coefficients satisfy
\((A,B)=1\), \(B=c+fkJ\). Then the finite-chain extension has the
same polynomial-coordinate conclusion. To assert that this covers
**every** slice extension of a given final derivation, also verify its
minimal plinth \((f^nk)\), or supply an alternative necessity argument.
The one-step analysis in Section 3 supplies these obligations completely;
they are not automatically asserted for every longer chain.

This is an actual preservation lemma for an explicitly controlled
construction class. It does not include arbitrary changes of invariant
generators, local slices with nonunit multiplicative coefficients,
unrelated minimal relations, or arbitrary affine modifications. No
theorem placing every rank-three LND in such a finite chain is assumed.
It also does not reduce arbitrary slice LNDs on four-space to invariant
extensions. Those remain separate requirements for cancellation.

## Sources

[^1]: N. Dasgupta and S. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), Theorem 2.17 and its exact local-slice data; Theorem 2.10(ii); Lemma 2.15(ii); Lemma 4.3. The displayed monomial construction and general local-slice machinery are prior work. The curve-reparametrization preservation argument above is a deduction here, not a statement quoted from that paper.

[^2]: H. Derksen, A. van den Essen, P. van Rossum, *The Cancellation Problem in Dimension Four*, Theorem 4.4 and Corollary 4.5, with the inspected source and exact ambient-coordinate scope recorded in [the pass-18 modification note](arbitrary-invariant-kernel-pass18.md).
