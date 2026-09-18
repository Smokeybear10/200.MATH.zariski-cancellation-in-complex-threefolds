# A sliced first-shift coefficient outside the image plus kernel

## 1. Exact conclusion

For every integer \(n\ge2\), there is a homogeneous Jacobian LND
\(H\) on the actual ring \(R=\mathbb C[x,y,z]\) and an ordinary
homogeneous polynomial \(\psi\) such that
\[
\begin{gathered}
E=H+(1+\psi)\partial_t\quad\hbox{on }B=R[t]
\quad\hbox{has an explicit polynomial slice},\\
\psi\notin H(R)+\ker H,\\
\deg_H\psi+1=N(\deg\psi-4n),\qquad N=8n+2,
\end{gathered}
\tag{1}
\]
and the actual positive frame \((x+z,y+z,z,t)\) has exact
weighted Euler shift one.

Consequently sliceness, homogeneity, the sharp degree equality, and
actual first shift do not force an image-plus-kernel decomposition.
Unlike the unsliced control in597, this counterexample retains the
polynomial-slice hypothesis. It refutes only that proposed reduction:
the kernels here are already polynomial by the recognized family
in [pass 595](rank-three-family-pole-repair-recognition-pass595-working.md).
It is not a cancellation counterexample, a failure of recognition,
or a novelty claim.

The obstruction specifically prevents a base shear \(t\mapsto t-Q\),
\(Q\in R\), from making \(E(t-Q)\) invariant: that would require
\(\psi-HQ\in\ker H\). It does not prevent other nonlinear coordinate
changes, including the known polynomial slice completion in595.

## 2. Whole base and exact degrees

Set
\[
\begin{gathered}
a=2n+1,\qquad M=4n+1=2a-1,\qquad
d_H=4n,\qquad N=8n+2,\\
f=xz-y^2,\qquad r=x^a+yf^n,\\
g=\frac{f^a+r^2}{x}
  =zf^{2n}+2x^{a-1}yf^n+x^{2a-1},\\
H(P)=\det J(f,g,P).
\end{gathered}
\tag{2}
\]
The quotient defining \(g\) is the displayed whole polynomial.
The Jacobian convention is the ordered row convention \(f,g,P\).
Its complete coordinate identities are
\[
\begin{aligned}
Hx&=-2f^n r,\\
Hy&=2a x^{a-1}r-g,\\
Hz&=2x^{a-2}\bigl(f^{n+1}+(2a-1)yr\bigr),\\
Hf&=Hg=0,\qquad Hr=-f^ng.
\end{aligned}
\tag{3}
\]
In particular \(H\) is ordinary homogeneous of derivation degree
\(d_H\), and \(\deg f=2,\deg r=a,\deg g=M\).

All required localization assertions have explicit inverses. In \(R_{fg}\),
\[
x=\frac{f^a+r^2}{g},\qquad
y=\frac{r-x^a}{f^n},\qquad
z=\frac{g-2x^{a-1}r+x^{2a-1}}{f^{2n}}.
\tag{4}
\]
Hence
\[
R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r].
\tag{5}
\]
This equality also proves that \(f,g,r\) are algebraically independent,
by transcendence degree. The notation on the right is thus an actual
Laurent polynomial ring with polynomial variable \(r\), not just a
generating list with unexamined relations.
There \(H=-f^ng\,\partial_r\), which is locally nilpotent.
It preserves \(R\) by (3), so \(H\) is an LND of \(R\).

For an independent parameter \(w\), the entire finite flow has
\[
r(w)=r-f^ngw,\qquad
x(w)=x-2f^nrw+f^{2n}gw^2.
\tag{6}
\]
Substitution in (4) gives its \(y,z\) images, with highest
coefficients \(-f^{2na-n}g^a\) and \(f^{4n(a-1)}g^{2a-1}\).
Thus the exact LND-degrees are
\[
\deg_H(x,y,z)=(2,4n+2,N).
\tag{7}
\]
The flow is globally the finite sum of iterates of \(H\) on each
original coordinate. Localization only computes those identities.
As usual in a characteristic-zero domain,
\(\deg_H(PQ)=\deg_HP+\deg_HQ\) for nonzero \(P,Q\), and
\(\deg_H(HP)=\deg_HP-1\) when \(HP\ne0\).

## 3. The recognized sliced coefficient and its homogeneous gauge

Define
\[
b=-gf^{n-2},\qquad
\psi_0=fbr=-gf^{n-1}r,\qquad
E_0=H+(1+\psi_0)\partial_T
\quad\hbox{on }R[T].
\tag{8}
\]
All expressions are polynomial because \(n\ge2\).
One has \(Hb=0\), \(Hr=f^2b\), and \(\deg_H\psi_0=1\).
The triangular extension \(E_0\) is locally nilpotent, as its
restriction to \(R\) is \(H\) and the derivative sequence of \(T\)
terminates.

There is a whole polynomial slice, with no inverse of \(f\) or \(g\):
\[
v=fT-r^2/2,\qquad q=fbv-r,\qquad
u_0=T-brv+\frac{fb^2}{2}v^2.
\tag{9}
\]
Indeed direct differentiation and expansion give
\[
E_0v=f,\qquad E_0q=0,\qquad fu_0=v+q^2/2.
\tag{10}
\]
Applying \(E_0\) to the last identity proves \(E_0u_0=1\), by
cancellation of the nonzero element \(f\) in the domain. This
cancellation is a polynomial identity argument, not localization of
the claimed slice.

Now set
\[
k=4n,\qquad \ell=8n,\qquad
\psi=\psi_0+H(z^k),\qquad E=H+(1+\psi)\partial_t
\quad\hbox{on }R[t].
\tag{11}
\]
Both terms of \(\psi\) are ordinary homogeneous of degree \(\ell\):
\[
\deg\psi_0=M+2(n-1)+a=8n,\qquad
\deg H(z^k)=k+d_H=8n.
\]
The actual coordinate shear and its inverse are
\[
T=t-z^k,\qquad t=T+z^k,
\tag{12}
\]
with \(x,y,z\) unchanged. It gives \(ET=1+\psi_0\).
Thus the isomorphism \(R[T]\to R[t]\) fixing \(R\) and sending
\(T\) to \(t-z^k\) intertwines \(E_0\) and \(E\).
Substitution of (12) in (9) provides the explicit whole polynomial
slice \(u\) for \(E\). This proves sliceness independently of any
recognition theorem.

By (7),
\[
\deg_H H(z^k)=kN-1>1=\deg_H\psi_0,\qquad
s:=\deg_H\psi+1=kN=N(\ell-d_H).
\tag{13}
\]
The strict inequality ensures that no cancellation between these
two summands changes the stated degree. Thus the sharp condition
holds for the actual full coefficient, not just its formal top.

## 4. Uniform image-plus-kernel obstruction in a Laurent polynomial ring

We prove \(\psi_0\notin H(R)+\ker H\), which also proves the result
for \(\psi\) by subtracting \(H(z^k)\). Suppose instead that
\[
\psi_0=H(Q)+K,\qquad Q,K\in R,\quad HK=0.
\tag{14}
\]
Apply \(H\) and use (3):
\[
H^2Q=H\psi_0=f^{2n-1}g^2.
\tag{15}
\]
In the actual localization (5), this says
\(\partial_r^2Q=1/f\). Since \(Q\) is polynomial in \(r\) there,
coefficient comparison over the characteristic-zero Laurent ring gives
\[
Q=\frac{r^2}{2f}+A(f,g)r+B(f,g),\qquad
A,B\in\mathbb C[f^{\pm1},g^{\pm1}].
\tag{16}
\]
This conclusion requires no identification of the whole kernel of \(H\).
It uses (15), the explicit localized ring, and ordinary polynomial
differentiation in its independent variable \(r\).

The element \(f\) is prime in \(R\): it is primitive and linear in
\(z\) over \(\mathbb C[x,y]\), with coprime coefficients \(x,-y^2\).
Its quotient is a domain. Since
\[
g\equiv x^M,\qquad r\equiv x^a\pmod f,
\tag{17}
\]
one has \(f\nmid g\), and
\[
R_g/(f)\cong\mathbb C[x^{\pm1},y].
\tag{18}
\]
Indeed, inverting \(g\) in the quotient inverts \(x\), and then
\(z=y^2/x\). In this quotient the coefficient ring
\(\mathbb C[g^{\pm1}]\) maps injectively to
\(\mathbb C[x^{\pm M}]\).

Expand \(A,B\) as finite Laurent sums in \(f\), with coefficients in
\(\mathbb C[g^{\pm1}]\). If either has a pole of maximum order
\(j>1\), multiply (16) by \(f^j\) and reduce in (18). The left
side is zero, since \(Q\in R\). The quadratic term also vanishes,
and the result is
\[
A_{-j}(x^M)x^a+B_{-j}(x^M)=0,
\tag{19}
\]
where at least one of the two Laurent coefficients is nonzero.
This is impossible: the exponents in its two summands lie in
different congruence classes \(a\) and \(0\) modulo \(M\).
Here \(0<a<M\), and the Laurent monomials in \(x\) are linearly
independent. Thus both \(A\) and \(B\) have at most a simple
\(f\)-pole.

Multiplying (16) by \(f\) and again reducing therefore gives
\[
\frac{x^{2a}}2+A_{-1}(x^M)x^a+B_{-1}(x^M)=0.
\tag{20}
\]
The three exponent classes modulo \(M\) are now \(1,a,0\), since
\(2a=M+1\). They are distinct for every \(n\ge2\).
The first summand is nonzero, so the same Laurent-monomial
independence contradicts (20). This proves
\[
\psi_0\notin H(R)+\ker H,\qquad
\psi\notin H(R)+\ker H.
\tag{21}
\]
All pole arguments took place in an injective localization and its
genuine prime quotient. No rational function was promoted to a
polynomial coordinate, and no square root or coefficient-field
rationality assumption was needed.

The argument also gives the following exact bounded coefficient test:
for every \(c\in\mathbb C[f,g]\),
\[
cr\in H(R)+\ker H
\quad\Longleftrightarrow\quad f^n\mid c
\quad\Longleftrightarrow\quad cr\in H(R).
\tag{22}
\]
The zero coefficient satisfies every condition. If \(f^n\mid c\),
then \(H(-cx/(2f^n))=cr\), with a polynomial preimage.
Conversely, applying \(H\) to a putative decomposition of \(cr\)
gives \(H^2Q=-cf^ng\) and hence
\[
Q=-\frac{c\,r^2}{2gf^n}+Ar+B
\quad\hbox{in }R_{fg}.
\tag{23}
\]
If \(j=\operatorname{ord}_f c<n\), the quadratic term has pole
order \(n-j\), with a nonzero leading coefficient in
\(\mathbb C[g^{\pm1}]\). Higher poles in \(A,B\) are impossible
by the two-class argument (19). At pole order \(n-j\), the
three-class argument (20) is again impossible, now with that
nonzero Laurent coefficient multiplying \(x^{2a}\).
This proves necessity. Formula (22) is an image test for this
specified base, not a classification of arbitrary extension slices.

## 5. Actual Euler frame and exact first shift

Use the actual polynomial coordinates
\[
(X_1,X_2,X_3,X_4)=(x+z,y+z,z,t),
\quad
(x,y,z,t)=(X_1-X_3,X_2-X_3,X_3,X_4).
\tag{24}
\]
The base orders in (7) are strictly smaller than \(N\) for \(x,y\).
On \(R\), \(E\) acts exactly as \(H\); on \(t\) its first derivative
is \(1+\psi\). Hence the complete positive \(E\)-degree tuple of
(24) is
\[
(N,N,N,s),\qquad s=kN,
\]
and its weighted Euler derivation is exactly
\[
D=N(x\partial_x+y\partial_y+z\partial_z)+s\,t\partial_t.
\tag{25}
\]
This uses the original actual coordinates and degrees after defining
\(E\), not weights transferred unchanged across a degree-changing
coordinate substitution.

With \([E,D]=ED-DE\), whole homogeneity and \(s=N(\ell-d_H)\)
give
\[
C:=[E,D]=N\ell\,\partial_t-Nd_HE,\qquad [E,C]=0.
\tag{26}
\]
In particular \([E,[E,D]]=0\). To check the exact filtration shift,
not merely an upper bound from this commutator, first note that
\[
[E^j,D]=jCE^{j-1}\quad(j\ge1).
\tag{27}
\]
For any nonzero polynomial \(P\) of \(E\)-degree \(h\), this
implies \(E^{h+2}(DP)=0\), and thus \(\deg_E DP\le h+1\)
whenever \(DP\ne0\). The all-ring shift is at most one.

The polynomial \(q\) in (9), with the actual substitution (12),
is an \(E\)-invariant and satisfies
\[
\partial_tq=f^2b=-f^ng\ne0,\qquad
E(Dq)=Cq=-N\ell f^ng\ne0,\qquad E^2(Dq)=0.
\tag{28}
\]
It follows that \(\deg_Eq=0\) and \(\deg_EDq=1\).
Therefore the exact all-ring weighted Euler shift is one.
This explicitly witnesses the horizontal, degree-raising part of
the terminal commutator; no inference from nonvanishing of the
commutator alone is necessary.

There are again two commuting homogeneous LND components:
\(\partial_t\), of \(D\)-weight \(-s\), and
\(H+\psi\partial_t\), of weight \(Nd_H\).
The second is locally nilpotent by the triangular extension argument,
and both commute because their coefficients are independent of \(t\).
These extra properties do not restore the failed image-plus-kernel
conclusion.

## 6. Existing recognition and verification scope

The recognition input in595 matches exactly, before the shear (12).
Its parameters are
\[
m=2,\qquad n\ge2,\qquad F(X,Z)=X^{2n}.
\tag{29}
\]
They satisfy \(m,n\ge2\) and \(F(X,0)\notin\mathbb C\), and give
\(xF(x,f)=x^{2n+1}\), exactly the \(r,g,H\) of (2).
Its extension coefficient is exactly
\(1-gf^{n-1}r=1+\psi_0\), and its displayed slice is (9).
Thus the retained theorem gives
\(\ker E_0\cong\mathbb C^{[3]}\) and a polynomial completion of
\(u_0\). The whole shear intertwining \(E_0,E\) transports these
conclusions to \(E\) and \(u\).

The entire final595 source was read through EOF for this parameter
and conclusion check, at SHA256
8e4e68eae92f3d57b360f16d1179240525d6022e3bcd02a72899f7ede1f90bf7.
This use retains its recognition proof; it does not claim a new
recursive verification of all of its external historical inputs.
The slice and nonmembership statements above do not depend on that
recognition conclusion.

Fresh unsaved calculations for \(n=2,3,4\) reconstructed the whole
Jacobian, \(H\psi_0\), the actual shear identity, the full Euler
commutator on all four coordinates, and all polynomial identities
in (9)--(10), including \(E_0u_0=1\). All residuals were zero.
The full arbitrary-\(n\) proof uses (16)--(20), not finite sampling
or the failure of a bounded search.
No saved checker was executed, imported, or compiled.

The conclusion is a negative answer to the specific proposed
image-plus-kernel reduction even in the sliced homogeneous first-shift
branch. General recognition is not refuted: these very examples
already have polynomial kernels. No conclusion about arbitrary
threefold cancellation or novelty follows from the counterexample.
