# Initial relations for two linear and two quadratic time coordinates

**Status: working proof with explicitly retained recognition inputs.**

For an actual sliced four-ring with E-time degrees \((1,1,2,2)\),
each quadratic-slot partial has exact all-ring degree shift at most
three. Its leading intrinsic LND fixes all four coordinate leading
coefficients. Consequently their weighted initial algebra has
transcendence degree at most three.

When that initial algebra has transcendence degree three, its unique
prime relation has weight at most four. More precisely, a bad-coordinate
partial of actual shift \(k_T\) that differentiates the relation gives
weight at most \(k_T+1\). A weight-two relation produces a third
E-affine coordinate by an explicit polynomial inverse and is recognized
by156. The surviving weight-three, weight-four, and lower-initial-rank
cases are not recognized here.

The tuple is an E-time degree tuple in an actual polynomial frame.
No earlier theorem about a numerically identical adjoint-height tuple
is used. This is not an entry theorem or unrestricted cancellation.

## 1. Actual coordinates and ordinary leading coefficients

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}_{\mathbb C}(B),
\qquad Eu=1,\qquad A=\ker E,\qquad B=A[u],\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
X=x_0+a u,\qquad Y=y_0+b u,\qquad
Z=z_0+z_1u+e u^2,\qquad W=w_0+w_1u+h u^2 .
\end{gathered}
\tag{1}
\]
All coefficients in the last line belong to \(A\), and
\(a,b,e,h\ne0\). In particular \(e=E^2Z/2\) and \(h=E^2W/2\)
are ordinary coefficients of \(u^2\), not undivided second
derivatives.
The four original generators are actual coordinates; the slice
\(u\) is not assumed to be an ambient coordinate.

The algebra \(A\simeq B/(u)\) is finitely generated and has
transcendence degree three. Write \(K=\operatorname{Frac}A\).
Choose a separating transcendence basis
\(\xi_1,\xi_2,\xi_3\) of \(K/\mathbb C\). The resulting finite
extension of \(\mathbb C(\xi_1,\xi_2,\xi_3)\) is separable.
Its coordinate derivatives extend uniquely to \(K\), and its
three differentials, together with \(du\), form a basis over \(K(u)\).
No polynomial coordinate presentation for \(A\) is assumed.

## 2. Invariant volume bounds both bad-coordinate partials

The original volume has the form
\[
dX\wedge dY\wedge dZ\wedge dW
 =J(u)\,d\xi_1\wedge d\xi_2\wedge d\xi_3\wedge du,
\qquad J(u)\in K[u]\setminus\{0\},\qquad J(u)=J_0\in K^* .
\tag{2}
\]
To justify the last equality, the polynomial automorphism
\(\exp(tE)\) over \(\mathbb C[t]\) has Jacobian determinant one
in the original coordinates. Its inverse is \(\exp(-tE)\);
the determinant is a unit of \(B[t]\), and evaluation at \(t=0\)
fixes that constant.
The flow fixes \(K\) and sends \(u\) to \(u+t\).
Taking differentials over \(\mathbb C(t)\) in (2) gives
\(J(u+t)=J(u)\), hence \(J\) is independent of \(u\).
The coefficient \(J_0\) is not asserted to be a complex constant.
This is the actual-volume argument retained in125/135.[^1]

Take either actual polynomial partial \(T=\partial_Z\) or
\(T=\partial_W\), holding the other original coordinates fixed.
It is an LND of \(B\).
Solve its four defining coordinate equations using the inverse
of the Jacobian matrix in (2).

For each \(T(\xi_j)\), the relevant cofactor uses the three rows
of the other coordinates, whose time degrees are \(1,1,2\).
One of its columns is the \(u\)-derivative column, lowering the
row degree of that entry by one. Every nonzero determinant term
therefore has degree at most \(1+1+2-1=3\).
The cofactor for \(T(u)\) uses only horizontal derivative columns
and has degree at most \(1+1+2=4\).
Division by \(J_0\) does not change these degrees.

For every \(f\in K\), the separating-basis chain rule writes
\(T(f)=\sum_j f_{\xi_j}T(\xi_j)\), with coefficients in \(K\).
If \(f\in A\), its actual image also lies in \(B=A[u]\).
Uniqueness of coefficients in \(K[u]\) returns the bounds to
the actual ring:
\[
T(A)\subset A[u]_{\le3},\qquad T(u)\in A[u]_{\le4}.
\tag{3}
\]
There is no assumption that the degree-three horizontal
coefficient is nonzero.

## 3. The exact shift and its nonzero intrinsic LND

First \(T(A)\ne0\). Otherwise, since \(T(X)=0\) and
\(X=x_0+a u\) with \(a\ne0\), one has \(aT(u)=0\);
then \(T\) vanishes on the generating ring \(A[u]\), a contradiction.

Choose finite algebra generators of \(A\), and let \(k_0\ge0\)
be the largest \(u\)-degree of their nonzero images under \(T\).
The derivation rule gives this same bound on all of \(T(A)\).
Give the zero polynomial degree \(-\infty\), and put
\(k=\max\{k_0,\deg_uT(u)-1\}\). By (3), \(0\le k\le3\).
Write
\[
\begin{gathered}
T(f)=\sum_{j=0}^{k}D_j(f)u^j\quad(f\in A),\qquad
T(u)=\sum_{j=0}^{k+1}h_j u^j,\qquad D_j\in\operatorname{Der}_{\mathbb C}(A),\\
T_\varepsilon=\varepsilon^k\varphi T\varphi^{-1},\qquad
\varphi(u)=u/\varepsilon,\quad \varphi|_{A[\varepsilon]}=\mathrm{id},\\
T_\varepsilon(f)=\sum_{j=0}^{k}D_j(f)u^j\varepsilon^{k-j},\qquad
T_\varepsilon(u)=\sum_{j=0}^{k+1}h_j u^j\varepsilon^{k+1-j}.
\end{gathered}
\tag{4}
\]
Here \(T\) is extended to kill the new indeterminate
\(\varepsilon\). On the Laurent extension, \(T_\varepsilon\)
is an actual conjugate LND multiplied by an invariant unit.
The nonnegative powers in (4) show that it preserves
\(B[\varepsilon]\), where it is still locally nilpotent.
Specializing the stable ideal \((\varepsilon)\) gives an LND
\(\mathcal D\) of \(B\) with
\(\mathcal D|_A=u^kD_k\) and
\(\mathcal D(u)=h_{k+1}u^{k+1}\).
It is nonzero by the definition of \(k\).

For an LND on a characteristic-zero domain,
\(f\mid\mathcal D(f)\) implies \(\mathcal D(f)=0\).
Indeed LND degree is additive on nonzero products, whereas a
nonzero derivative has degree one less than its argument.
Apply this to \(u\): it forces \(h_{k+1}=0\).
Therefore \(D_k\ne0\), \(k=k_0\), and \(\deg_uT(u)\le k\).
As \(\mathcal D(u)=0\),
\(\mathcal D^j(f)=u^{kj}D_k^j(f)\) for \(f\in A\);
local nilpotence implies that \(N_T:=D_k\) is an LND of \(A\).
Thus, for each of the two choices of \(T\),
\[
\begin{gathered}
k_T:=k\in\{0,1,2,3\},\qquad
0\ne N_T=[u^{k_T}]T|_A\in\operatorname{LND}(A),\qquad
\deg_uT(u)\le k_T,\\
\deg_E T(f)\le\deg_E f+k_T\quad(0\ne f\in B,\ T(f)\ne0),\\
N_T(a)=N_T(b)=N_T(e)=N_T(h)=0 .
\end{gathered}
\tag{5}
\]
The middle bound follows by applying the derivation to each
coefficient times a power of \(u\). It is the exact maximal shift:
some element of \(A\) has a nonzero \(u^{k_T}\) coefficient in
its image.

For the last line, in \(T(X),T(Y),T(Z),T(W)\), the coefficient of
\(u^{k_T+\deg_E Q}\) for a coordinate \(Q\) is \(N_T\) applied
to its leading coefficient. Terms from differentiating \(u\)
have strictly smaller degree. The actual image \(T(Q)\) is zero
or one, and \(k_T+\deg_EQ>0\); hence this coefficient vanishes.
This includes \(k_T=0\).
The proof has used only actual LNDs and an invariant Laurent
indeterminate. No localization at a polynomial moved by \(T\)
has been declared locally nilpotent.

## 4. The generated weighted initial algebra

Use distinct formal source variables and the indicated positive weights:
\[
\begin{gathered}
\mathscr P=\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W],
\qquad \operatorname{wt}(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)=(1,1,2,2),\\
\theta:\mathscr P\longrightarrow A[\eta],\qquad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,h\eta^2),\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a,b,e,h)\le2,\qquad
\operatorname{trdeg}_{\mathbb C}\operatorname{im}\theta\le3 .
\end{gathered}
\tag{6}
\]
The new \(\eta\) is independent over \(A\).
For either nonzero \(N_T\), the local-slice theorem gives
\(\operatorname{trdeg}_{\mathbb C}\ker_A N_T=2\).
Equation (5) puts all four leading coefficients in that kernel,
which proves both bounds in (6).
No polynomial-plane presentation or finite generation of that
kernel is required.

If \(a,b\) are proportional over \(\mathbb C\), a nonzero
constant linear combination of \(X,Y\) is an invariant actual
coordinate. The slice makes \(A\) regular, so the retained BGL
invariant-coordinate gate recognizes \(A\simeq\mathbb C^{[3]}\).[^2]
Henceforth assume they are not proportional.
Then \(a\eta,b\eta\) are algebraically independent.
Any relation would separate into homogeneous binary relations
in \(a,b\), and over \(\mathbb C\) every nonzero homogeneous
binary polynomial factors into linear forms.
A vanishing factor would contradict nonproportionality.
Thus the initial algebra has transcendence degree either two
or three.

Assume now that it has transcendence degree three.
Its kernel is a height-one prime in the UFD \(\mathscr P\),
so it is generated by an irreducible weighted homogeneous
polynomial \(F\). Homogeneity follows because \(\theta\) respects
the grading and factors of a weighted homogeneous polynomial
for positive weights are weighted homogeneous.
The independence of the first two images implies that \(F\)
involves at least one of \(\mathsf Z,\mathsf W\).
Consequently \(d:=\operatorname{wt}F\ge2\).
For every quadratic slot \(Q\in\{Z,W\}\) occurring in \(F\),
we will prove
\[
\ker\theta=(F),\qquad
2\le d\le k_{\partial_Q}+1\le4 .
\tag{7}
\]
The bound is asserted only for pivots with
\(\partial_{\mathsf Q}F\ne0\).
The generated algebra in (6) is not assumed to be the full
associated graded algebra \(\operatorname{gr}_E B=A[\eta]\).

## 5. Exact multiplicity and actual partial differentiation

Fix such a pivot \(Q\), write \(T=\partial_Q\), and put \(k=k_T\).
Let \(P\in\mathscr P\) be nonzero, with original weighted degree
\(M\) and top weighted part \(P_M\).
Suppose \(P_M=F^\ell G\) with exact multiplicity
\(\ell\ge1\), so \(F\nmid G\).
Characteristic zero and dependence on the pivot give
\(F_{\mathsf Q}\notin(F)\). Differentiating exactly \(\ell\)
times gives
\[
\begin{gathered}
\partial_{\mathsf Q}^{\ell}P_M
 \equiv \ell!\,G(F_{\mathsf Q})^\ell\pmod{F},\\
\deg_E\bigl(T^\ell P(X,Y,Z,W)\bigr)=M-2\ell,\qquad
\deg_E P(X,Y,Z,W)\ge M-(k+2)\ell .
\end{gathered}
\tag{8}
\]
The residue in the first line is nonzero in the domain
\(\mathscr P/(F)\). Its weight is \(M-2\ell\).
Every lower weighted part of \(P\), after the same differentiation,
has smaller weight or is zero.
Therefore the coefficient of \(u^{M-2\ell}\) in the actual
evaluation is nonzero and cannot cancel. This proves the exact
degree in the second line.
Iterating the actual shift estimate (5) proves the final inequality.
This reproduces the multiplicity mechanism133 with the present
pivot weight two and its actual shift \(k\).[^3]

## 6. Invariant growth gives the strict bound

For every \(f\in A\setminus\mathbb C\), take its unique representing
polynomial \(P\) in the original coordinates.
It has \(M>0\), but \(E\)-degree zero. Hence \(\theta(P_M)=0\),
so its exact multiplicity \(\ell\) along \(F\) is positive.
Equation (8) yields
\[
\ell d\le M\le(k+2)\ell .
\tag{9}
\]
Nonconstant invariants exist because \(\operatorname{trdeg}A=3\);
thus \(d\le k+2\).

If \(d=k+2\), (9) forces \(M=d\ell\) and
\(\operatorname{wt}G=0\). Positivity of the source weights makes
\(G\) a nonzero complex constant.
The highest weighted part of every nonconstant invariant is
therefore a scalar power of \(F\).

Let \(\mathcal F_MA\) be the vector space of invariants whose
original coordinate polynomial has weighted degree at most \(M\).
The top-part map embeds
\(\mathcal F_MA/\mathcal F_{M-1}A\) into the weight-\(M\) source
polynomials. The previous paragraph bounds its dimension by one
if \(d\mid M\), and by zero otherwise.
Choose three algebraically independent invariants and let
\(D>0\) be the maximum of their original weighted degrees.
Their monomials of total exponent at most \(j\) are independent,
so
\[
\binom{j+3}{3}
\le\dim_{\mathbb C}\mathcal F_{Dj}A
\le \left\lfloor\frac{Dj}{d}\right\rfloor+1
\qquad(j\ge0).
\tag{10}
\]
This is impossible for large \(j\).
No finite initial generating set or equality with the full
associated graded ring is needed.
It follows that \(d\le k+1\), proving (7).

In particular, a surviving weight-three relation needs
\(k_{\partial_Q}\ge2\) for every quadratic pivot occurring in it.
A weight-four relation needs \(k_{\partial_Q}=3\) for every
such pivot. A pivot of shift zero cannot occur in this
height-one, nonproportional case. A pivot of shift one forces
the weight-two case addressed next.
These implications of the growth bound do not assert that the
smaller shifts occur. Section 8 determines the exact shifts
in the height-one case.

## 7. Weight two is an actual three-good reduction

If \(d=2\), the relation has the form
\(F=\alpha\mathsf Z+\beta\mathsf W+J_2(\mathsf X,\mathsf Y)\),
where \(J_2\) is homogeneous quadratic and
\((\alpha,\beta)\ne(0,0)\).
Choose constants \(\gamma,\delta\) with
\(\Delta=\alpha\delta-\beta\gamma\ne0\).
The change and its inverse are
\[
\begin{gathered}
Z'=\alpha Z+\beta W+J_2(X,Y),\qquad
W'=\gamma Z+\delta W,\qquad X'=X,\quad Y'=Y,\\
Z=\frac{\delta(Z'-J_2(X',Y'))-\beta W'}{\Delta},\qquad
W=\frac{-\gamma(Z'-J_2(X',Y'))+\alpha W'}{\Delta}.
\end{gathered}
\tag{11}
\]
These formulas verify both inverse orders on the original
polynomial ring.
The initial relation makes the \(u^2\) coefficient of \(Z'\)
zero. Therefore \(E^2Z'=0\), and \(X',Y',Z'\) are three
actual E-affine coordinate slots.
The all-degree three-good recognition156 then gives
\(A\simeq\mathbb C^{[3]}\), retaining precisely its working
mathematical and source dependencies.[^4]

## 8. Exact cubic shifts and the initial projection

The actual cubic horizontal cofactor is nonzero precisely when
the other three weighted coordinate initials are algebraically
independent. This gives a sharper description of where the
maximum shift in (5) is attained.

For \(T=\partial_W\), the other coordinates are \(X,Y,Z\).
The highest weighted part of their differential wedge is the
wedge of \(au,bu,eu^2\), namely
\[
\begin{gathered}
d(au)\wedge d(bu)\wedge d(eu^2)
=u^4\,da\wedge db\wedge de
 +u^3\{2e\,da\wedge db-b\,da\wedge de+a\,db\wedge de\}\wedge du,\\
da\wedge db\wedge de=0,\qquad
2e\,da\wedge db-b\,da\wedge de+a\,db\wedge de
=a^4\,d(b/a)\wedge d(e/a^2),\\
k_{\partial_W}=3
\ \Longleftrightarrow\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a\eta,b\eta,e\eta^2)=3 .
\end{gathered}
\tag{12}
\]
The first vanishing follows from the leading-coefficient field
bound in (6). The next equality follows by differentiating
\(b=a(b/a)\) and \(e=a^2(e/a^2)\), and expanding.
All differentials here are over \(\mathbb C\), in the function
field \(K\), with the formal \(u\) subsequently adjoined.

The coefficients of the displayed two-form in the separating
basis are, up to their cofactor signs and the nonzero divisor
\(J_0\), exactly the cubic coefficients of \(T(\xi_j)\).
Lower time terms in the original coordinates cannot contribute
to these cubic horizontal cofactors.
Thus at least one such coefficient is nonzero if and only if
\(d(b/a)\wedge d(e/a^2)\ne0\).
If this occurs only in a rational basis element, the quotient
rule still forces a cubic coefficient on an element of \(A\):
a degree bound on \(T(A)\) extends to \(T(K)\).
Consequently nonvanishing is equivalent to \(k_T=3\).

In characteristic zero the two-form is nonzero exactly when
\(b/a\) and \(e/a^2\) are algebraically independent.
The fraction field of the initial image of the other triple is
\(\mathbb C(a\eta,b/a,e/a^2)\).
Here \(a\eta\) is transcendental over \(K\), so its transcendence
degree is one more than that of the two ratios. This proves
the final equivalence in (12).
The argument for \(T=\partial_Z\) is identical, replacing \(e\)
by \(h\); a change of cofactor orientation does not affect
nonvanishing.

When the full initial kernel is \((F)\), its contraction to the
polynomial subring omitting \(\mathsf Q\) is zero precisely when
\(F\) involves \(\mathsf Q\). If \(F\) involves that variable,
the degree in \(\mathsf Q\) of a nonzero multiple of \(F\) is
positive. If it does not, \(F\) itself lies in that subring.
This contraction is exactly the kernel of the other triple's
initial map. Therefore every quadratic pivot occurring in \(F\)
has exact shift three; a quadratic slot absent from \(F\) has
shift at most two.

In particular \(F=XZ+YW\) forces both selected shifts to be
three, whereas \(F=XZ-Y^3\) forces \(k_{\partial_Z}=3\) and
\(k_{\partial_W}\le2\).
If the full initial image has transcendence degree two, every
other triple is dependent, so both selected shifts are at most
two. This does not make its height-two kernel principal.
It also shows why seeking a smaller shift for an occurring
height-one pivot cannot improve the remaining weight bound:
those pivots necessarily attain the maximum.

## 9. Remaining scope

The height-one argument leaves weights three and four, whose
general weighted forms are respectively
\[
\begin{aligned}
F_3&=L_1(\mathsf X,\mathsf Y)\mathsf Z
      +L_2(\mathsf X,\mathsf Y)\mathsf W+J_3(\mathsf X,\mathsf Y),\\
F_4&=Q_2(\mathsf Z,\mathsf W)
      +J_2(\mathsf X,\mathsf Y)\mathsf Z
      +K_2(\mathsf X,\mathsf Y)\mathsf W+J_4(\mathsf X,\mathsf Y).
\end{aligned}
\tag{13}
\]
Subscripts denote ordinary homogeneous degrees in the indicated
variables; terms may be zero. The relation must still be
irreducible and must involve a quadratic slot.
Neither form alone gives an invariant correction or an actual
new coordinate.

If the initial algebra instead has transcendence degree two,
its prime kernel has height two. The principal-factor
multiplicity argument above does not apply to that ideal.
No exclusion or recognition of this lower-initial-rank case
is inferred from (6).

Thus the present reduction does not recognize every actual
E-time \((1,1,2,2)\) frame. Nor does it show that an arbitrary
sliced action can be put in this profile or in a three-good
profile. It uses no previous adjoint-height classification
with the same numerical tuple.
No finite computations certify these universal conclusions,
and no historical novelty, human expert review, or
proof-assistant certification is claimed.
All156 and earlier artifacts are unchanged.

## Sources and retained inputs

1. [Actual speed-rank proof125](three-good-speed-rank-bound-pass125.md),
   Sections 2--5, and
   [selected-partial proof135](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--3. Their actual volume and Laurent leading-LND
   mechanisms are reconstructed here for different row weights.
   Their three-good hypotheses are not silently reused as a
   theorem for the present two-good frame.
2. [Invariant-coordinate gate in synthesis156](three-good-all-degree-recognition-pass156-working.md),
   Section 3, with the retained Bhatwadekar--Gupta--Lokhande
   regular-kernel theorem and the actual slice regularity check.
3. [Multiplicity and growth argument133](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 2--3. Its derivative calculation and filtered
   dimension argument are reproduced with cost \(k_T+2\),
   not imported with its old cost four.
4. [All-degree three-good recognition156](three-good-all-degree-recognition-pass156-working.md).
   Only the explicit weight-two coordinate change (11) supplies
   its required third good slot.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4.
