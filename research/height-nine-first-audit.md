# Audit of the first height-nine identities

The identities and closing subcases in
[height-nine-first-pass.md](height-nine-first-pass.md) pass this bounded
audit. The proposed additional bound
\[
\operatorname{rank}\operatorname{Jac}(E^4x)\le1
\tag{A}
\]
also follows from the weighted adjugate argument. This audit does not
attempt to close the remaining height-nine case.

Use the notation of that note: \(P=E(x)\), \(J=\operatorname{Jac}P\),
\(W_i=[E,T_i]\), \(V=[E,W_4]\), \(v=V(x)\), and
\(R=ve_4^{\mathsf T}\). Coefficient vectors are columns.

## 1. Defect and inverse-Jacobian orientation

The coefficient vector of \([E,W_i]\) is
\(-E(J_{\cdot i})+J J_{\cdot i}\). Thus the first three double brackets
vanish and the fourth equals \(v\) precisely when
\[
E(J)=J^2-R.
\]
Likewise \([E,V]=0\) gives \(E(v)=Jv\), not \(E(v)=0\).

Let \(F_t=\exp(tE)x\), and let \(C_i(t)\) be the coefficient column
of \(\exp(tE)T_i\exp(-tE)\). That derivation applied to the \(j\)-th
component of \(F_t\) gives \(\delta_{ij}\). Therefore
\[
\operatorname{Jac}(F_t)C(t)=I,
\qquad C(t)=I-tJ+\frac{t^2}{2}R.
\]
This verifies the orientation in equation (7). No substitution of
\(x\) by \(F_t\) in the displayed \(J\) or \(R\) is needed.

The flow is a polynomial automorphism over \(\mathbb C[t]\), with
inverse the negative-time flow. Its Jacobian determinant is a unit in
\(\mathbb C[t,x]\), hence a complex constant, equal to one at \(t=0\).
Consequently \(\det C(t)=1\) and
\(\operatorname{Jac}(F_t)=\operatorname{adj}C(t)\).

All cofactors have degree at most four. In row four of the adjugate,
the deleted column is column four of \(C\), so the remaining three
columns all have degree at most one. That row has degree at most three.
The resulting bounds are exactly
\[
E^5(x)=c\in\mathbb C^4,\quad E^6(x)=0,
\qquad E^4(x_4)=k\in\mathbb C,\quad c_4=0.
\]
The trace check also has the stated sign: the degree-two determinant
coefficient, after \(\operatorname{tr}J=0\), is
\((v_4-\operatorname{tr}J^2)/2\).

## 2. The factor in \(Jc=2kv\)

The identity \(P(F_t)=\operatorname{Jac}(F_t)P\) follows either from
differentiating the flow in time or from applying \(E\) to its coordinate
components. Hence \(C(t)P(F_t)=P\).

In its coefficient of \(t^5\), the only contributions are
\[
-\frac{Jc}{24}+\frac{R E^4(x)}{12}
=-\frac{Jc}{24}+\frac{kv}{12}.
\]
Thus \(Jc=2kv\), and a constant field \(T_c=c\cdot\partial\) satisfies
\([E,T_c]=-2kV\). The two stated specializations, \(k=0,c\ne0\) and
\(k\ne0,c=0\), are valid closing subcases. A nonzero \(c\) alone does
not make \(T_c\) commute with \(E\).

## 3. Nice subcase

If \(E^2(x)=0\), then \(JP=0\). Its derivative is
\(E(J)+J^2=0\). Comparing the first three columns with the
double-bracket identities gives \(J^2=we_4^{\mathsf T}\) for a
polynomial column \(w\). Therefore \(0=J^2P=wP_4\).

If \(w=0\), all double brackets vanish. If \(w\ne0\), the domain
property forces \(P_4=0\), giving an invariant ambient coordinate.
This argument uses only the three double-bracket hypotheses and
niceness; the fourth triple bracket is unnecessary here.

The constant-commuting-direction closure in Section 4 is also valid.
The three-dimensional space of good constant directions contains one
independent of that translation. It descends to a nonzero constant
direction on its coordinate three-ring and retains its double-bracket
identity, as required by the three-variable single-partial lemma.

## 4. Corrected field and additional coefficient identities

Suppose \(k\ne0\), put \(s_0=E^3(x_4)/k\), and note \(E(s_0)=1\).
Since \([E,T_c]=-2kV\) and \([E,V]=0\), the product rule gives
\[
\operatorname{ad}_E^2(s_0T_c)=-4kV.
\]
Thus \(Q=T_4+s_0T_c/(4k)\) satisfies the stated double-bracket identity.

For a direct verification of equation (12), write
\[
F_t(x_4)=x_4+tA+\frac{t^2}{2}B
+\frac{t^3}{6}ks_0+\frac{t^4}{24}k,
\quad A=E(x_4),\quad B=E^2(x_4).
\]
The coefficient of \(t^5\) in
\((T_4+tW_4+t^2V/2)F_t(x_4)=1\) gives \(V(s_0)=0\).
The coefficient of \(t^4\) gives
\[
\frac{k}{6}W_4(s_0)+\frac14V(B)=0.
\]
Because \(c_4=0\), one also has
\((T_c-2ktV)F_t(x_4)=0\). Its coefficient of \(t^3\) is
\[
\frac{k}{6}T_c(s_0)-kV(B)=0.
\]
These are exactly
\(T_c(s_0)=6V(B)=-4kW_4(s_0)\).

There is a further verified identity: for \(i\le3\), the coefficient
of \(t^4\) in \((T_i+tW_i)F_t(x_4)=0\) gives
\[
W_i(s_0)=0,
\qquad E(T_i(s_0))=0.
\tag{B}
\]
It does not itself give \(T_c(s_0)=0\).

Finally, constant partials commute with \(T_c\), so
\([T_i,Q]=T_i(s_0)T_c/(4k)\), as stated. If one additionally knew
\(T_c(s_0)=0\), coordinates adapted to \(T_c\) can be chosen using the
first three original variables and retaining \(u=x_4\). Then \(T_4\)
remains \(\partial_u\), and the proposed triangular integration is
valid. Its simultaneous effect on the other partials is still required.
Neither polynomiality nor the corrected double bracket alone certifies
a coordinate frame.

## 5. Weighted adjugate proves the proposed rank bound

Give columns one through three of \(C(t)\) weight one and column four
weight two. Their weighted leading coefficient matrix is
\[
L=(-J_{\cdot1},-J_{\cdot2},-J_{\cdot3},v/2).
\]
The degree-five coefficient of \(\det C(t)=1\) is \(\det L\), so
\(L\) is singular. By the column-deletion convention for the adjugate,
\[
[t^4]\operatorname{adj}C(t)
=\operatorname{diag}(1,1,1,0)\operatorname{adj}L.
\tag{C}
\]
Deleting one of the first three columns leaves total weight four;
deleting column four leaves total weight three. Multilinearity proves
(C) even if some weighted leading minors vanish.

Over \(\operatorname{Frac}B\), a singular four-by-four matrix has
adjugate rank at most one: it has rank one when the matrix has rank
three, and is zero when the matrix has rank at most two. Since
\[
[t^4]\operatorname{Jac}(F_t)
=\frac1{24}\operatorname{Jac}(E^4x),
\]
equation (C) proves (A).

The bound concerns \(\operatorname{Jac}(E^4x)\), not its linear image
span, and does not by itself prove that \(E^4x\) defines a
quasi-translation. No such additional inference is included in this
audit. No errors requiring correction were found in equations (5)--(13).
