# Actual controls for normalized defect projection

The slice projection of an original commuting LND is locally
nilpotent on the invariant localization. The full moving-column
identity supplies the extra polynomial coefficient needed to
clear it globally with the proposed power of the top factor.
The examples below test that mechanism and its rank and
denominator boundaries. None realizes the full canonical moving
\((1,1,2,2)\) frame.

## 1. The exact projection gate being tested

The general deduction and its actual moving-frame hypotheses are stated
separately in [projected-cubic-defects-pass69.md](projected-cubic-defects-pass69.md).
This note supplies independent controls, not a second recognition theorem.

In the moving cubic setting, put \(\delta=E/g\) on \(B_g\),
and \(\sigma=\delta X\), so \(\delta\sigma=1\).
An original bad top \(V=[E,[E,T]]\) is a polynomial LND,
commutes with \(E\), and kills \(g\), by the actual highest
identities retained in
[pass42](two-quadratic-top-line-pass42.md#5-exact-rescaling-boundary).
It is therefore an LND of \(B_g\) commuting with \(\delta\).

The divided coordinate-column identity gives
\(\widetilde V\sigma=0\), and its exact formula is
\[
\widetilde V=g^{-2}V+2g^{-3}(Wg)E,\qquad W=[E,T].
\tag{1}
\]
The vanishing on \(\sigma\) does not require original joint
rank three. Indeed, applying
\(T+z[\delta,T]+z^2\widetilde V/2\) to
\(\exp(z\delta)X=X+z\sigma+z^2/2\), the cubic coefficient
is \(\widetilde V\sigma/2=0\). This uses an actual conjugated
partial but not its local nilpotence on \(B_g\).

Since \(E\sigma=g\), equation (1) yields
\[
V\sigma=-2Wg\in B,\qquad
N:=V-(V\sigma)\delta=g^2\widetilde V.
\tag{2}
\]
Write \(C=\ker(\delta|B_g)\). The actual slice theorem gives
\(B_g=C[\sigma]\). Commutation makes \(V(C)\subset C\) and
\(V\sigma\in C\). Thus \(N\) is \(V|_C\) extended by
\(N\sigma=0\), proving \(N\) is an LND of \(B_g\).
No finite-generation assumption on \(C\) is needed for this
coefficientwise argument.

Moreover \(Ng=0\), so its invariant multiple \(gN\) is also
an LND of \(B_g\). Equation (2) makes it polynomial on the
original ring:
\[
R=gN=gV+2(Wg)E=g^3\widetilde V.
\tag{3}
\]
Restriction and the injection \(B\hookrightarrow B_g\) prove
that \(R\) is a global polynomial LND. It commutes with \(E\)
and fixes \(g\) and \(EX=g\sigma\).
This is stronger than arbitrary denominator clearing, which
need not preserve local nilpotence or give the claimed power.

For a commuting original pair \(V_1,V_2\), the two projections
commute. Over \(K=\operatorname{Frac}B\), the projection
annihilates precisely the \(E\)-line in their joint span:
\[
\operatorname{rank}_K(R_1,R_2)
 =\operatorname{rank}_K(E,V_1,V_2)-1,
\quad
\langle E,R_1,R_2\rangle_K=\langle E,V_1,V_2\rangle_K.
\tag{4}
\]
An individual projection may vanish. The formula does not
preserve rank on every fiber or produce a lower-height
polynomial coordinate frame.

## 2. A true coordinate partial with a nonpolynomial local slice

Start with \(B=\mathbb C[a,y,z,s]\), \(E=\partial_s\), and
\(g=a\). Define the actual polynomial coordinates
\[
A_0=a+\frac{sz}{2},\qquad
Y_0=y-\frac{as^2z}{2}-\frac{s^3z^2}{8},\qquad
X=z+\frac{a^2s^2}{2}+ys,
\]
ordered as \((s,A_0,Y_0,X)\).
Their polynomial inverse is
\[
z=X-\frac{A_0^2s^2}{2}-Y_0s,\qquad
a=A_0-\frac{sz}{2},\qquad
y=Y_0+\frac{A_0s^2z}{2}-\frac{s^3z^2}{8}.
\tag{5}
\]
Substitution in both orders gives the identity, and the
Jacobian determinant relative to \((a,y,z,s)\) is \(-1\).
The true partial belonging to \(X\) is
\[
T=\partial_z-\frac{s}{2}\partial_a+\frac{as^2}{2}\partial_y.
\]
Its two original adjoints are
\[
W=-\frac12\partial_a+as\partial_y,\qquad
V=a\partial_y,\qquad [E,V]=0,\qquad Wg=-\frac12.
\tag{6}
\]
Here \(V\) is visibly an actual polynomial LND and fixes \(g\).

The divided action and chosen coordinate satisfy
\[
\delta=\frac1a\partial_s,\qquad
\sigma=\delta X=as+\frac ya,\qquad
\delta\sigma=1,\quad V\sigma=1.
\tag{7}
\]
The slice \(\sigma\) has a genuine pole along \(a=0\).
Its projection and normalized top are
\[
\widetilde V=\frac1a\partial_y-\frac1{a^3}\partial_s,
\qquad
N=a\partial_y-\frac1a\partial_s,
\qquad
R=a^2\partial_y-\partial_s.
\tag{8}
\]
The last is a global nice LND with the actual coordinate
slice \(-s\). It fixes \(a\) and \(EX=a^2s+y\), and
commutes with \(E\). In contrast \(N=a^2\widetilde V\)
is not polynomial on \(B\). This tests the exact powers
in (2)--(3), including a case where one cannot lower the
power three multiplying \(\widetilde V\).

The original coordinate partial \(T\) itself is not an LND
of \(B_a\): it moves the unit \(a\), since \(Ta=-s/2\).
This does not prevent the normalized defect from being an
LND of that localization.

The full original adjoint heights of the ordered coordinates
are exactly \((5,5,3,2)\), and
\[
E^3(s,A_0,Y_0,X)^t=(0,0,-3z^2/4,0)^t.
\tag{9}
\]
Thus \(g=a\) is not the canonical factor of a full highest
vector \(c a^3\). Both the full-frame bounds and that canonical
top equation fail. The control proves no realization of the
remaining independent moving cubic frame.

## 3. Actual commuting fields and generic rank

Keep (7), \(E=\partial_s\), and \(V_1=a\partial_y\).
All additional fields in this section are actual polynomial
LNDs commuting with \(E\) and fixing \(a\), but are not
asserted to be simultaneous top columns of the preceding
coordinate frame.

Take first \(V_2=V_1+E\). The original joint rank is two,
yet the two global projections coincide:
\[
R_1=R_2=a^2\partial_y-\partial_s.
\tag{10}
\]
They have rank one, as (4) requires.

Instead take \(V_2=\partial_z\). The original joint rank is
three, and the global projections are
\[
R_1=a^2\partial_y-\partial_s,\qquad R_2=a\partial_z.
\tag{11}
\]
They commute and have generic rank two. After adjoining \(E\)
the generic rank is three, but on the whole fiber \(a=0\)
it becomes one. Multiplication by the invariant factor is
therefore not a fiberwise rank-preservation assertion.
Taking \(V=E\) also gives a zero projection, illustrating
the possible individual vanishing.

## 4. The polynomial coefficient gate cannot be omitted

On the same polynomial ring and with the same \(\delta,\sigma\),
choose the actual commuting LND \(V_0=\partial_y\).
It fixes \(a\), but \(V_0\sigma=1/a\) is not polynomial.
Its locally nilpotent slice projection is
\[
N_0=\partial_y-\frac1{a^2}\partial_s,\qquad
aN_0=a\partial_y-\frac1a\partial_s\notin\operatorname{Der}(B).
\tag{12}
\]
Only \(a^2N_0\) is polynomial in this example.
Consequently local nilpotence of a commuting \(V\) and the
existence of a localized slice do not alone prove the proposed
one-power polynomial descent. Here \(V_0\sigma\) cannot equal
\(-2Wg\) for a polynomial \(W\); this is precisely the actual
column gate used in (2), not a counterexample to it.

## 5. Verification scope

The standalone
[normalized_defect_projection_checks_pass69.py](normalized_defect_projection_checks_pass69.py)
has three methods. Its first complete run passed all three in
0.158 seconds, exit zero, with no failed assertion.
It imports only unittest and SymPy.

The methods verify the true coordinate inverse and partial,
the complete out-of-scope adjoint profile and top, exact
projection and denominator powers, actual commuting-field
rank examples, and failure of the one-power polynomial gate
when its required coefficient is absent.
Repeated runs are not additional methods.

These are exact controls and a scoped reconstruction of the
projection mechanism. They do not certify a new full moving
frame, a global coordinate or kernel-recognition theorem,
human review, formal proof verification, historical novelty,
or general cancellation. Frozen pass68 and earlier files are
unchanged.
