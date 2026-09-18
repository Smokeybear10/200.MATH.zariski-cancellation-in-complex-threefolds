# Multiplier restrictions and the exact pole of the uncorrected inverse

The additive inverse from pass 19 does not extend unchanged to
nonunit local-slice multipliers. For a multiplier \(f^e\), its first
reverse coordinate is polynomial exactly when a specified coefficient
vanishes to order at least \(e\); below that order the pole is exact.
This obstructs the uncorrected formula, not polynomiality of the
slice kernel. Correcting a preceding curve polynomial remains possible.

## 1. The fixed invariant frame restricts allowable multipliers

Use the pass-18 polynomial-curve data
\[
f=xz-F(y),\quad r=xP(x,f)+yf^n,\quad
xh=K_n(f,r),\quad K_n(f,T)=G(T,f^n)+f^{nd+1},
\]
where \(F\) is monic of degree \(d\ge2\), \(n\ge1\),
\(P(x,0)\) is nonconstant, and \(G(T,S)=S^dF(T/S)\).
The established base derivation \(D_1=-\operatorname{Jac}(f,h,\cdot)\)
is primitive, has kernel \(\mathbb C[f,h]\), and \(D_1r=f^nh\).

Keeping this invariant frame and using a polynomial affine local
slice \(r_*=a(f,h)r+b(f,h)\), the construction's derivative condition
\(D_1r_*=h\,q(f)\ne0\) forces
\[
a(f,h)f^n=q(f),\qquad a\in\mathbb C[f]\setminus\{0\}.
\tag{1}
\]
Conversely such an \(a\) satisfies the derivative requirement.
Thus arbitrary \(h\)-dependent polynomial multipliers are not
automatically inputs in this fixed frame. Changing invariant
generators could change the question; it is not included in (1).

Write \(b=b_0(f)+hQ(f,h)\). Subtracting \(b_0(f)\) is an invariant
translation, so take
\[
R_*=a(f)r+hQ(f,h),\qquad
\Phi(f,T)=G(T,a(f)f^n)+a(f)^d f^{nd+1}.
\tag{2}
\]
Then the next polynomial invariant is
\[
k=\Phi(f,R_*)/h
 =a^dx+Q(f,h)\Delta_G(R_*,ar;af^n).
\tag{3}
\]
The divided difference is polynomial, including at equal arguments.
The relation \(\Phi\) is monic and irreducible over \(\mathbb C[f]\):
over \(\mathbb C(f)\) it is obtained from \(K_n\) by the invertible
change \(T\mapsto T/a\), and a monic factorization would persist there.
Modulo \(h\), it is the minimal relation of \(ar\).

Freudenburg's local-slice theorem therefore supplies the LND
\[
D_2=\operatorname{Jac}(f,k,\cdot),\qquad D_2R_*=af^nk.
\tag{4}
\]
The fixed-frame replacement principle and construction are prior
work.[^1] The assertion below concerns a particular attempted inverse.

## 2. A valid slice extension with tunable vanishing order

Take \(a=f^e\), \(e\ge1\), and \(N=n+e\). Then \(\Phi=K_N\)
exactly, and \(hk=K_N(f,R_*)\). Assume
\[
q(H):=Q(0,H)\ne0,\qquad
B=1+f^\ell kJ(f,k),\quad \ell\ge1,\quad J(0,K)\ne0.
\tag{5}
\]
The derivative in (4) is \(p=f^Nk\), not merely its radical.
The derivation \(E=D_2+B\partial_t\) has a slice. Indeed \(B-1\)
belongs to \(\sqrt{p\mathbb C[f,k]}\), so \(B\) is invertible
modulo \(p\). Explicitly, with \(v=B-1\),
\[
L=\sum_{j=0}^{N-1}(-v)^j,\qquad
U=(1-BL)/p\quad\text{satisfy}\quad Up+LB=1.
\tag{6}
\]
The quotient defining \(U\) is polynomial because \(v^N\) is
divisible by \(f^Nk\). Thus \(UR_*+Lt\) is a polynomial slice.
Minimality of \(R_*\) is not needed for this sufficiency.

The last-slice invariants used by the old formula are
\[
\rho=BR_*-pt,\qquad \widehat h=K_N(f,\rho)/k.
\tag{7}
\]
The second is polynomial because
\(\rho-R_*=k(f^\ell JR_*-f^Nt)\).
The uncorrected reverse coordinate would be
\[
\widehat r_{\rm old}
 =\frac{\rho-\widehat hQ(f,\widehat h)}{f^e}.
\tag{8}
\]
It is invariant as a rational function. Its regularity is separate.

## 3. Exact obstruction theorem

Under (2)-(8),
\[
\widehat r_{\rm old}\in R[t]\quad\Longleftrightarrow\quad \ell\ge e.
\tag{9}
\]
If \(1\le\ell<e\), its valuation at the prime \(f\) is exactly
\[
v_f(\widehat r_{\rm old})=\ell-e.
\tag{10}
\]
The residue ring of \(f=xz-F(y)\) is a domain and contains an
injective copy of \(\mathbb C[x]\).

### Necessity, including the leading coefficient

For \(\ell<e\), \(N>\ell\), and all lower \(T\)-degree terms of
\(K_N\) vanish modulo \(f^{\ell+1}\). Using
\(R_*^d=kh\bmod f^{\ell+1}\), expansion of (7) gives
\[
\rho=R_*+f^\ell kJR_*\pmod{f^{\ell+1}},\qquad
\widehat h=h+d f^\ell kJh\pmod{f^{\ell+1}}.
\tag{11}
\]
The second equality follows from the polynomial divided difference,
so no division modulo \(k\) is being assumed.
Taylor expansion in the second argument of \(Q\) yields
\[
\rho-\widehat hQ(f,\widehat h)
=f^\ell kJh\bigl((1-d)Q-dhQ_h\bigr)
\pmod{f^{\ell+1}}.
\tag{12}
\]
The term \(f^er\) disappears because \(e\ge\ell+1\).

Put \(H_0=x^{d-1}P(x,0)^d\) and
\(k_0=H_0^{d-1}q(H_0)^d\), nonzero nonconstant polynomials.
The residue coefficient on the right of (12) is
\[
k_0J(0,k_0)H_0
\bigl((1-d)q(H_0)-dH_0q'(H_0)\bigr).
\tag{13}
\]
It is nonzero. Substitution of a nonconstant polynomial is injective,
and \((1-d)-dH\,d/dH\) multiplies \(H^j\) by \(1-d-dj\),
nonzero for every \(j\ge0\). Also \(J(0,k_0)\ne0\).
Thus the numerator has valuation exactly \(\ell\), proving (10)
and the negative direction of (9).

### Sufficiency for the first reverse coordinate

If \(\ell\ge e\), both \(\rho-R_*\) and \(\widehat h-h\)
are divisible by \(f^e\). For the latter, use the divided-difference
formula and \(N\ge e\). Since \(R_*-hQ(f,h)=f^er\), the
numerator of (8) is divisible by \(f^e\). This proves polynomiality.

This direction only asserts regularity of (8). It does not
automatically make subsequent coordinates polynomial or give an inverse.

## 4. Exact control and implications

For \(F=y^2\), \(P=x\), \(Q=h\), one has \(H_0=x^3\),
\(k_0=x^9\), and the coefficient in (13), for \(J=1\), is
\(-3x^{15}\). For \(e=2,\ell=1\), the numerator has first order
\(f\), and (8) has a simple pole. More generally the same coefficient
gives pole order \(e-\ell\) whenever \(e>\ell\).

The failure occurs for a derivation with an explicit polynomial
slice, by (6). It is not evidence that a slice does not exist, or
that no other polynomial coordinates exist. In particular this
obstruction fixes \(Q\) during reversal; replacing it by a suitable
finite jet changes (8). Such a correction needs its own forward
and inverse divisibility proof.

Physical direct expansions for \(F=y^2\), \(P=x\), \(Q=h\),
\(n=1,2\), and \(a=f,f-1\) verify \(D_2R_*=af^nk\) and
coefficient gcd one in all four cases. These are finite checks,
not a proof of primitivity or kernel classification for all multipliers.

## Sources

[^1]: G. Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), *Osaka Journal of Mathematics* 34 (1997), 757-767, Section 2, Proposition 2, Theorem 2 and the following iteration paragraph. The sign and derivative convention are also stated in N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), Theorem 2.17.
