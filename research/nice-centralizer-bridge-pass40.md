# A polynomial auxiliary kernel in the degree-five residual

The polynomial nice symmetry constructed in the degree-five reduction
has a polynomial three-dimensional kernel. This is a consequence of an
established classification theorem, once its primitive and coordinate
hypotheses are verified. It recognizes the auxiliary quotient, not the
original quotient whose polynomiality is sought.

## 1. Primitive division preserves the required structure

Work in \(B=\mathbb C[x_1,x_2,x_3,x_4]\) with the hypotheses and
notation of [the degree-five proof](cubic-degree-five-pass40.md). Its
explicit polynomial derivation is
\[
W=g^4T_e+\frac{g^2q}{3\lambda}T_d+
\left(\frac{g^3p}{3\lambda}-\frac{q^2}{12\lambda^2}\right)T_c,
\quad p=Ex_4,\quad q=E^2x_4.
\tag{1}
\]
It satisfies \(W^2x_i=0\), \([E,W]=0\), \(Wg=0\), and
\(Wx_4=\lambda g^4\ne0\). Also the rational function
\(\sigma=q/(\lambda g^2)\) satisfies \(W\sigma=0\) and
\(E\sigma=g\ne0\).

Let \(h\) be a polynomial gcd of the four coefficients \(Wx_i\),
and put \(D=W/h\). Every coefficient of W lies in its kernel.
The kernel of an LND is factorially closed, so every irreducible
factor of h is W-invariant. In particular \(Wh=0\). Thus D is
a polynomial derivation with
\[
Dh=0,\qquad W^nf=h^nD^nf,\qquad D^2x_i=0.
\tag{2}
\]
These identities show that D is an irreducible nice LND and
\(\ker D=\ker W\).

The primitive division also preserves commutation with E. From
\([E,hD]=0\), every \((Eh)D(x_i)\) is divisible by h.
Since the coefficients of D have gcd one, comparison at each
irreducible factor of h gives \(h\mid Eh\). For an LND on a
domain of characteristic zero, \(h\mid Eh\) implies \(Eh=0\):
otherwise the additive derivation degree of \(Eh\) would be
\(\deg_Eh-1\), while the degree of its nonzero expression
\(h(Eh/h)\) is at least \(\deg_Eh\). Consequently
\[
Eh=0,\qquad [E,D]=0.
\tag{3}
\]
No multivariate Bezout identity is inferred from the coefficient gcd.

## 2. Exact application of the nice-derivation theorem

All coefficient vectors in (1) lie in the constant span of c,d,e,
which has dimension at most three. Choose a nonzero constant linear
form w annihilating that span, and complete w to linear coordinates
\((w,X,Y,Z)\) of B. Then
\[
D(w)=0,\qquad D^2X=D^2Y=D^2Z=0.
\tag{4}
\]
The base ring \(\mathbb C[w]\) is a PID. Theorem 3.6 of
Dasgupta and Gupta applies to this irreducible nice derivation over
that PID. It gives a change in \(\operatorname{GL}_3(\mathbb C[w])\)
to coordinates U,V,T for which
\[
D=a(w,U)\partial_V+b(w,U)\partial_T,
\quad \gcd(a,b)=1,
\quad R:=\ker D=\mathbb C[w,U,bV-aT].
\tag{5}
\]
In particular \(R\simeq\mathbb C^{[3]}\). This is an application
of their known result, not a new classification.[^1]

The coordinate change in (5) is polynomial with polynomial inverse:
its determinant is a unit of \(\mathbb C[w]\). The statement
does not make \((a,b)\) a unit ideal. The cited theorem explicitly
allows a non-flat quotient in the noncomaximal case.

Commutation in (3) makes \(F=E|_R\) an LND. It is nonzero:
\(g\in R\), \(\sigma\in R_g\), and \(F\sigma=g\ne0\)
after localization. Miyanishi's three-variable kernel theorem then
gives
\[
S:=\ker F=\ker E\cap\ker D\simeq\mathbb C^{[2]}.
\tag{6}
\]
The source used for this established input is its explicit statement
as Theorem 2.8 in Dasgupta and Gaifullin.[^2]

Writing \(A=\ker E\), the restriction \(D|_A\) is a nonzero
intrinsic LND with kernel S. Nonvanishing follows because otherwise,
in the actual cylinder \(B=A[s_*]\), D would be a multiple of E,
contradicting \(D\sigma=0\) and \(E\sigma=g\ne0\).
Thus the auxiliary polynomial three-ring provides a concrete
factorization of the common invariant plane. Existence of a plane
kernel for a nonzero intrinsic action was already established in
[the earlier surface note](intrinsic-quotient-surface-pass.md).

## 3. A global slice cannot be transferred to the auxiliary kernel

Here is a small control against an invalid remaining step. In actual
coordinates \((w,u,v,t)\), put
\[
D=w\partial_v+u\partial_t,\qquad E=\partial_v,
\quad r=uv-wt.
\tag{7}
\]
Both are polynomial LNDs, D is irreducible and nice, they commute,
and \(v\) is an E-slice. The standard elementary kernel calculation
gives \(R=\mathbb C[w,u,r]\), but
\[
E|_R=u\partial_r.
\tag{8}
\]
Every value of this restricted derivation belongs to the proper
ideal \((u)\), so it has no slice. Meanwhile
\(\ker E=\mathbb C[w,u,t]\) is plainly polynomial. This control
disproves only automatic slice descent, not cancellation. It is
not asserted to realize the degree-five residual.

In the actual residual, neither an invariant ambient coordinate
for E nor a slice of \(D|_A\) has yet been obtained from (5).
The displayed denominator, the possible non-flat elementary
quotient, and the embedding of R in B remain part of the problem.
One cannot replace \(A\) by the isomorphic-type conclusion about R.

## 4. The supplied normal-form plane need not be preserved

Even a sliced commuting action need not preserve the particular
coordinate plane supplied by (5). This statement has an explicit
primitive rank-two nice control, not just a rank-one translation.
Continue with the actual coordinates and derivation
\[
D=w\partial_v+u\partial_t,\qquad r=uv-wt,
\qquad L=u\partial_w+t\partial_v.
\tag{9}
\]
Then \(Lr=Dr=0\) and \([L,D]=0\). The replica \(r^2L\)
is an LND centralizing D. Its polynomial automorphism
\(\Phi=\exp(r^2L)\) and inverse are
\[
\begin{aligned}
\Phi(w,u,v,t)&=(w+ur^2,\ u,\ v+tr^2,\ t),\\
\Phi^{-1}(w,u,v,t)&=(w-ur^2,\ u,\ v-tr^2,\ t).
\end{aligned}
\tag{10}
\]
Both maps fix r, which directly verifies both inverse compositions.
Conjugate the original sliced action \(\partial_v\), while leaving
D fixed:
\[
E'=\Phi\partial_v\Phi^{-1}
   =-2ru^2\partial_w+(1-2rut)\partial_v.
\tag{11}
\]
Thus E' is an actual LND, \([E',D]=0\), and
\[
E'(v+tr^2)=1,\qquad
\ker E'=\mathbb C[u,t,w+ur^2]\simeq\mathbb C^{[3]}.
\tag{12}
\]
The full coordinate presentation in (10), not just its Jacobian,
proves the displayed kernel.

Nevertheless
\[
E'(w)=-2u^2(uv-wt)\notin\mathbb C[w,u],
\tag{13}
\]
as is also witnessed by its nonzero v-derivative \(-2u^3\).
Hence the supplied plane \(\mathbb C[w,u]\subset\ker D\)
is not E'-stable. The different actual coordinate plane
\(\Phi(\mathbb C[w,u])=\mathbb C[w+ur^2,u]\) is E'-stable,
indeed pointwise fixed. This example therefore refutes automatic
preservation of one selected plane, not existence of some suitable
plane. It is not asserted to satisfy the degree-five residual data.

The standalone [nice_centralizer_checks_pass40.py](nice_centralizer_checks_pass40.py)
has three finite methods for primitive division/commutation, failure
of slice transfer, and this conjugated action with both inverse
compositions. It imports only `unittest` and `sympy`. These concrete
controls do not machine-prove the source classification theorem or
the global recognition gap. The initial run passed all three methods
in 0.068 seconds, with no assertion failure or formula correction.
The checker is frozen after that run.

## Sources

[^1]: Nikhilesh Dasgupta and Neena Gupta,
[*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
version 1, 2017, Theorem 3.6 and its proof on PDF pp. 6-7,
Corollary 3.8 on PDF p. 8. The paper was already cited in earlier
project notes; this pass rechecks the hypotheses for (1).

[^2]: Nikhilesh Dasgupta and Sergey Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2),
version 2, Theorem 2.8 on PDF p. 6, explicitly attributed to Miyanishi.
It is applied to the global polynomial ring R in (5), not to R localized
at g.
