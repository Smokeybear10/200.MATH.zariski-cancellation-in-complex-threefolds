# A residual coordinate can descend while its normalized parameter has a pole

An actual dense sliced family has a primitive curve equation that is a
coordinate over the entire polynomial coefficient ring. Nevertheless,
the canonical second-tail parameter has a pole at a height-one prime,
even after the selected speed is inverted. No polynomial replacement
can be a slice for that normalized leading derivation.

This separates descent of the curve equation from descent of the
specified normalized parameter. It does not disprove curve-coordinate
descent or cancellation. The actual family is retained143; the present
calculation concerns its coefficient-ring fibers and normalization.[^1]

## 1. Actual coordinates and the leading derivation

Let \(a,b,v,u\) be independent, put \(E=\partial_u\), and choose
nonconstant \(P\in\mathbb C[a]\) and \(F\in\mathbb C[t]\) of degree
\(d\ge2\). Define the polynomial divided difference and coordinates
\[
\begin{gathered}
\Delta_F(P,v,u)=
 \sum_{j=1}^{d}c_j\sum_{i=1}^{j}\binom ji
       v^{j-i}P^i u^{i-1},\qquad F(t)=\sum_{j=0}^{d}c_jt^j,\\
u\Delta_F=F(v+Pu)-F(v),\\
X=u,\qquad Y=v+Pu,\qquad Z=a-F(v)+bu,\qquad
W=b+\Delta_F(P,v,u).
\end{gathered}
\tag{1}
\]
There is no division at \(u=0\). The polynomial inverse is
\[
u=X,\qquad a=Z-XW+F(Y),\qquad
v=Y-P(a)X,\qquad b=W-\Delta_F(P(a),v,X).
\tag{2}
\]
Forward substitution in (2) recovers all four source variables by
the divided-difference identity. Conversely (2) recovers \(X,Y,W\),
and the remaining forward coordinate is
\(a-F(v)+uW-u\Delta_F=a+uW-F(Y)=Z\).
Thus both inverse orders hold polynomially.

The good speeds are \((1,P(a),b)\). They have rank two and dense
homogeneous speed cone: dehomogenizing a homogeneous relation at the
first coordinate gives a polynomial relation between the independent
elements \(P(a),b\). The good speed ideal is the unit ideal, and
\(X=u\) is an actual slice. The bad time degree is exactly \(d-1\).

For the actual bad partial \(T=\partial_W\), with \(X,Y,Z\) fixed,
differentiating (2) gives
\[
\begin{gathered}
Tu=0,\qquad Ta=-u,\qquad Tv=P'(a)u^2,\qquad
Tb=1+P'(a)F'(v)u,\\
N=[u^2]T|_A=P'(a)\partial_v,\qquad
A=\mathbb C[a,b,v],\qquad S=\ker_A N=\mathbb C[a,b],\\
s=EX=1,\qquad N'=N,\qquad L=\operatorname{Frac}S.
\end{gathered}
\tag{3}
\]
For \(Tb\), applying \(T\) to \(u\Delta_F=F(Y)-F(v)\)
and canceling \(u\) in the polynomial domain gives the displayed
formula. Since \(P'\ne0\), multiplication by this coefficient does
not change the kernel of \(\partial_v\).

## 2. The relation descends on every coefficient-ring fiber

The projected goods are \(y=v\) and \(z=a-F(v)\). With formal
variables \(U,V\), the exact curve relation and normalized parameter
are
\[
\begin{gathered}
g=a-V-F(U),\qquad S[U,V]/(g)\simeq S[v],\\
(G,H)=(g,U),\qquad U=H,\quad V=a-G-F(H),\\
\Phi=g,\qquad \Psi=\frac{U}{P'(a)},\qquad
r=\Psi(y,z)=\frac{v}{P'(a)},\qquad N'r=1.
\end{gathered}
\tag{4}
\]
The displayed inverse proves that \(g\) is an \(S\)-coordinate,
not just an \(L\)-coordinate. The same inverse remains valid after
every base change from \(S\), including every height-one residue
field. No denominator is needed for the relation or its completion.

For completeness the retained canonical peeling coefficients are
\(f_0=b+c_1P\), \(f_j=c_{j+1}P^{j+1}\) for \(1\le j\le d-1\),
and \(f_{-1}=c_0-a\). The coefficient partial
\(\partial_\tau a=1/P'(a)\), with \(\tau=P(a)\) and \(\rho=b\),
gives exactly \(\Phi\) and \(\Psi\) in (4). The normalization is
therefore the canonical one, not a freely rescaled parameter.

## 3. A genuine unremoved height-one pole

Take \(P(a)=a^2+1\) and \(F(t)=t^3/2\). The bad coordinate is
quadratic in \(u\), with \(E^2W=P(a)^3\), while
\[
\begin{gathered}
N=2a\partial_v,\qquad g=a-V-U^3/2,\qquad
\Psi=U/(2a),\qquad r=v/(2a),\\
N(A)=aA,\qquad N\bmod(a)=0,\qquad s=1.
\end{gathered}
\tag{5}
\]
The equality \(N(A)=aA\) is equality of additive images: in
characteristic zero \(\partial_v\) is surjective on \(S[v]\).
In particular \(1\notin N(A)\), so there is no polynomial normalized
slice, not merely a failure of the particular choice \(r\).

At the height-one prime \((a)\subset S\), the numerator \(v\)
is not divisible by \(a\) in \(S[v]\). Thus \(r\) has valuation
\(-1\) along this divisor and is not in \(S_{(a)}[v]\).
Adding a rational coefficient constant from \(L\) cannot remove
the coefficient \(1/(2a)\) of \(v\). The curve relation still
specializes to \(-V-U^3/2\), a coordinate. The degeneration is
in the chosen leading derivation and parameter, not in that curve.

This also survives a nonconstant selected speed. Reorder the goods
as \((Y,Z,X)\), so the selected speed is \(s=P(a)\). Set
\(R=S[1/P]\). Projection at \(Y=0\) gives
\[
\begin{gathered}
\widetilde y=a-F(v)-bv/P,\qquad \widetilde z=-v/P,\\
\widetilde g(U,V)=U-a+F(-PV)-bV,\\
(G,H)=(\widetilde g,V),\qquad
U=G+a-F(-PH)+bH,\quad V=H,\\
N'=\frac{P'}{P^2}\partial_v,\qquad
\widetilde r=\frac{P^2v}{P'},\qquad N'\widetilde r=1.
\end{gathered}
\tag{6}
\]
Again the relation is an \(S\)-coordinate before localization.
For \(P=a^2+1\), the prime \((a)\) survives in \(R\), because
\(P\equiv1\pmod a\). The coefficient of \(v\) in
\(\widetilde r\) still has a simple pole there. Every field slice
of \(N'\) differs from \(\widetilde r\) by an element of \(L\),
so no such slice is polynomial over \(R\).

## 4. Exact unit criterion and scope

More generally, for any nonzero selected \(s\in S\), put
\(R=S[1/s]\). The coefficient-ring derivations in question obey
\[
\begin{gathered}
\text{there is }f\in R[v]\text{ with }Nf=1
\quad\Longleftrightarrow\quad P'\in R^*,\\
\text{there is }f\in R[v]\text{ with }(N/s^2)f=1
\quad\Longleftrightarrow\quad P'\in R^*.
\end{gathered}
\tag{7}
\]
Necessity follows by comparing the constant coefficient in \(v\)
in \(P'f_v=1\), or from \(P'R[v]\) being a proper ideal when
\(P'\) is a nonunit. If \(P'\) is a unit, \(v/P'\) and
\(s^2v/P'\) respectively are explicit slices. Here \(s\) is
already a unit in \(R\), so the two criteria are identical.

For the actual charts above, \(s=1\) or \(s=P\). The abstract
unit criterion does not claim that every element of \(S\) occurs
as a selected coordinate speed. Nor does the pole prove that the
primitive leading derivation has no slice: removing the common
factor \(P'\) gives \(\partial_v\), which has the slice \(v\).

Both frames are explicitly translations and their invariant ring
is already \(S[v]\). The computation refutes automatic polynomial
descent of a normalized leading-derivation slice after inverting
only the selected speed. It supplies a positive fiberwise control
for descent of the primitive curve relation. It gives no
cancellation counterexample and no obstruction to choosing a
different, non-normalized polynomial fiber parameter.

## Sources

1. [The recovered-invariant template143](recovered-invariant-template-rigidity-pass143-working.md),
   Sections 2--3 and equations (5)--(9). The actual inverse,
   selected partial, coefficient field and normalized tail formulas.
   They are reconstructed directly above in the stated coordinate order.
2. [Common Taylor integrality145](common-gauss-integrality-tail-primitivity-pass145-working.md).
   Context for distinguishing first-tail primitivity from the
   polynomial descent of a chosen normalized parameter. The elementary
   examples and unit criterion here do not depend on that theorem.

No new runtime checker is used in this note. The statements concern
this explicit all-degree family, not a classification of actual dense
frames or a historical novelty determination.

[^1]: Source 1. This is a new coefficient-ring analysis of a retained
    actual family, not a newly discovered polynomial automorphism.
