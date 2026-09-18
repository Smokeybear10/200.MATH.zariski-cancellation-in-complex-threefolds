# Original volume gives a global denominator for slice-difference descent

In the actual three-good-coordinate setting, the original coordinate
volume supplies an additional constraint not contained in the
universal generator pencil. It puts the slice difference into the
smaller generator ring after inverting one explicit velocity
determinant. The argument uses neither a generic curve coordinate
nor a denominator from a local slice of the intrinsic derivation.

## 1. Centered coordinates and the velocity determinant

Retain the entire actual setup of the
[invariant-plane lemma](constant-acceleration-invariant-plane-pass88.md).
Thus B=C[x_1,x_2,x_3,z]=A[u], E(u)=1, q is a nonzero complex
constant, and W is the actual nonzero intrinsic LND fixing u,
with S=ker(W|A)=C[s_1,s_2]. Put
\[
x_i=b_i u+a_i,\qquad b_i\in S,\quad a_i\in A,
\qquad z=r+\frac q2u^2,\qquad r\in A.
\tag{1}
\]
The elements a_i here are the centered invariants x_i-b_i u;
they are not the invariants from a different slice projection.
Use the two actual polynomial coordinates s_1,s_2 on S to define
\[
L=b_{s_1}\times b_{s_2}\in S^3,\qquad
\Omega=L\cdot b=\det[b_{s_1},b_{s_2},b]\in S.
\tag{2}
\]
The derivatives in (2) are ordinary derivatives of the three
polynomials b_i in S. They are not extensions of ambient partials
through an algebraic field. The conclusion below is a global
polynomial identity whether or not L or Omega vanishes.

## 2. The cubic coefficient of the actual volume

Let F=Frac(A), so Frac(B)=F(u) and trdeg_C F=3. Work with
Kahler differential forms over C in this field and write
\[
\omega=dx_1\wedge dx_2\wedge dx_3\wedge dz,
\qquad \mathcal L_E\omega=0.
\tag{3}
\]
The last identity uses the actual original polynomial coordinates.
Their E-flow is x_i to x_i+tau b_i and
z to z+q tau u+q tau squared/2, a polynomial automorphism over
C[tau] with polynomial inverse. Its Jacobian is a unit of
C[tau,x_1,x_2,x_3,z], hence a nonzero constant; specialization
tau=0 makes that constant 1. Differentiating preservation of the
coordinate volume gives (3). This is not a volume-preservation
assumption for abstract coefficient data or proposed generators.

Substituting (1) makes omega a polynomial in u with coefficients
in Omega cubed of F, followed by du. Indeed Omega to the fourth
of F is zero, and the differentials of elements of F contain no
du term. On these coefficients the Lie derivative of E vanishes,
while its action on u is ordinary differentiation and on du is
zero. Characteristic zero and (3) therefore force every positive
coefficient of this polynomial in u to vanish.

Since each db_i belongs to the F-span of ds_1,ds_2, the wedge of
all three db_i is zero. Expanding the coefficient of u cubed gives
the exact sign and expression
\[
[u^3]\omega
 =q\,ds_1\wedge ds_2\wedge
      \left(\sum_{i=1}^3 L_i\,da_i\right)\wedge du
 =0.
\tag{4}
\]
For clarity, the contributing terms are q times
(da_1 wedge db_2 wedge db_3 + db_1 wedge da_2 wedge db_3
+ db_1 wedge db_2 wedge da_3), followed by du. Reordering gives
respectively the three positive cross-product components in (4).
The term using dr and all three db_i vanishes. Terms using a good
du and dr have u-degree at most two; the possible degree-four
term also contains the vanishing triple wedge of db_i.

Because L has entries in S, wedging with ds_1 and ds_2 removes
the terms a_i dL_i. After removing the independent final du,
(4) says ds_1 wedge ds_2 wedge d(L dot a)=0 in Omega cubed of F.
Contract this three-form with W. Its contractions with ds_1 and
ds_2 are zero, so
W(L dot a) ds_1 wedge ds_2=0. The two-form is nonzero because
s_1,s_2 are algebraically independent in characteristic zero.
Consequently W(L dot a)=0. The element L dot a is in A, and
the exact kernel there is S. This proves the global conclusion
\[
L\cdot a\in S.
\tag{5}
\]
Working in the fraction field to compare differential forms did
not invert an element in this conclusion: membership in S follows
from the original intrinsic kernel inside A. In particular no
plinth factor or local intrinsic slice occurs in (5).

## 3. Descent away from one explicit velocity determinant

Let N=[b,v_2,v_3] be the inverse of the completed S-matrix in
the invariant-plane lemma. It is an actual matrix in GL_3(S),
and x=N(sigma,A_1,A_2) transposed. Put h=u-sigma and
R=S[A_1,A_2], as in the
[universal-pencil proof](universal-generator-pencil-pass88.md).
Then (1) gives a=-b h+v_2 A_1+v_3 A_2. Hence (5) becomes
\[
\Omega h=(L\cdot v_2)A_1+(L\cdot v_3)A_2-\kappa\in R,
\qquad \kappa=L\cdot a\in S.
\tag{6}
\]
If Omega is nonzero, this yields h in R localized at Omega.
If Omega is a nonzero complex constant, it yields h in R itself.
No conclusion is drawn by dividing by an identically zero Omega.
More generally the same formula retains its exact linear relation
among A_1,A_2 and the S-constant kappa even when Omega is zero.

This is a genuine additional actual-frame identity. It does not
by itself prove that Omega is nonzero, that its zero locus can be
discarded, or that the remaining extension R to A is finite or
faithfully flat. Local membership h in R localized at Omega is
not an assertion of coordinate recognition on that open set or
globally. No ambient automorphism is inferred from N.

Jet first identified the leading generation-determinant constraint.
Root supplied the centered form and its global Omega h consequence.
Jet reconstructed the differential-form proof above, avoiding a
generic curve-coordinate or local-volume trivialization gate.
These six equations are a written proof, not a numerical certificate;
this note adds no checker or method. The earlier control files and
all frozen artifacts are unchanged.
