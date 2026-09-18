# An induced action forced by an actual nonunit-speed coordinate

## Scope and statement

Let
\[
 B\simeq\mathbb C^{[4]},\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\qquad
 Eu=1,\qquad A=\ker E.
 \tag{1}
\]
The slice identity gives the actual ring equality \(B=A[u]\).
The supplied slice \(u\) is not assumed to be an ambient coordinate,
and \(A\) is not assumed to be polynomial.

Suppose an actual ambient coordinate \(v\) satisfies
\[
                 E^2v=0,\qquad Ev=a\ne0,\qquad a\notin A^*.
 \tag{2}
\]
Then, uniquely,
\[
                        v=au+b,\qquad a,b\in A.
 \tag{3}
\]
“Actual coordinate” means that \(v\) is part of a whole polynomial
coordinate system of \(B\), not only of its fraction field or a
localization.

**Necessary induced-action statement.** Under (1)--(2), there exists
\[
                     0\ne N\in\operatorname{LND}_{\mathbb C}(A)
                     \quad\text{with}\quad N(a)=0.
 \tag{4}
\]
Its extension to \(A[u]\) that kills \(u\) is locally nilpotent and
commutes with \(E\).

More precisely, choose any actual completion of \(v\), and let \(D\)
be the resulting coordinate partial with \(Dv=1\). Its exact shift
\(\delta\) for the \(u\)-degree filtration is nonnegative. The full
leading derivation of \(D\) is \(\eta^\delta N\) on
\(\operatorname{gr}B=A[\eta]\).
If \(\delta=0\), one additionally has
\[
 D|_A=N,\qquad Du=\beta\in A,\qquad N(b)+a\beta=1.
 \tag{5}
\]
In particular \(N\) descends to \(A/(a)\), where the class of \(b\)
is a slice.
The zero-shift case also gives an actual invariant-coefficient
presentation over a polynomial three-ring: with \(C=\ker D\),
one has \(B=C[v]\), \(C\simeq\mathbb C^{[3]}\), and
\(E=H+a\partial_v\), where \(0\ne H\in\operatorname{LND}(C)\)
and \(a\in\ker H\). This is a statement about \(C\), not a prior
identification of \(A\) with \(C\).

This note does not prove that (2) exists for arbitrary sliced input,
or that its existence recognizes \(A\) as \(\mathbb C^{[3]}\).
A whole polynomial control below shows that even the primitive induced
\(N\) in the zero-shift case can have no slice. That control has a
known polynomial kernel and is not a cancellation counterexample.
No novelty claim is made.

## 1. The actual coordinate partial and its finite shift

Complete \(v\) to actual coordinates \((v,v_2,v_3,v_4)\) of \(B\),
and set
\[
                       D=\partial/\partial v.
 \tag{6}
\]
This is a nonzero whole locally nilpotent derivation, with \(Dv=1\).
It need not preserve \(A\) or commute with \(E\).

The ring \(A\) is finitely generated: the slice identity identifies
it with \(B/(u)\). Choose any finite algebra generators \(a_1,\ldots,a_m\)
of \(A\). Use \(\deg_u 0=-\infty\), and define
\[
 \delta=
 \max\bigl\{\deg_u D(a_i):1\le i\le m,\ 
                       \deg_u D(u)-1\bigr\}.
 \tag{7}
\]
The Leibniz rule shows that this is the exact filtration shift:
\[
                  \deg_u D(F)\le\deg_u F+\delta
                  \qquad(F\in B,\ D(F)\ne0).
 \tag{8}
\]
It is attained on a generator realizing (7), and thus does not depend
on the chosen finite generating set of \(A\).

If \(\delta<0\), then \(D(A)=0\) and \(Du\in A\).
Equation (3) would give
\[
                             1=Dv=a\,Du.
 \tag{9}
\]
This contradicts the nonunit hypothesis on \(a\).
Therefore
\[
                                  \delta\ge0.
 \tag{10}
\]
No statement about a globally minimizing ambient frame is used here.

## 2. The full leading derivation

The filtration is the actual polynomial-degree filtration of \(A[u]\),
so its associated graded ring is exactly \(A[\eta]\), with \(A\) in
degree zero and \(\eta=\operatorname{in}(u)\) in degree one.
Equation (8) induces a nonzero homogeneous derivation
\[
                      \overline D:A[\eta]\longrightarrow A[\eta]
                      \quad\text{of degree }\delta.
 \tag{11}
\]
It is locally nilpotent. Indeed, if a successive iterate of
\(\overline D\) on a homogeneous initial form stays nonzero, it is
the corresponding leading form of the same iterate of \(D\) on a
lift, of degree increased by \(\delta\) at each step.
Local nilpotence of \(D\) forces eventual vanishing. A finite sum of
homogeneous elements is then killed by one sufficiently large power.

Because \(\delta\ge0\), homogeneity gives
\[
                       \overline D(\eta)=\beta_*\eta^{\delta+1}
                       \quad\text{for some }\beta_*\in A.
 \tag{12}
\]
A locally nilpotent derivation of a characteristic-zero domain cannot
send a nonzero element to a nonzero multiple of itself. For if
\(\partial h=hq\ne0\), additivity of locally nilpotent degree gives
\(\deg_\partial h-1=\deg_\partial h+\deg_\partial q\), an impossibility.
Applying this observation to (12) proves
\[
                         \overline D(\eta)=0,\qquad
                         \deg_u Du\le\delta.
 \tag{13}
\]

For \(c\in A\), the degree-\(\delta\) homogeneous image has the form
\[
                              \overline D(c)=\eta^\delta N(c).
 \tag{14}
\]
The derivation rule makes \(N\) a derivation of \(A\).
It is nonzero: otherwise (13)--(14) would make the entire
\(\overline D\) zero, contradicting the exact shift.
Since \(\overline D\eta=0\),
\[
                        \overline D^{\,k}(c)
                        =\eta^{k\delta}N^k(c).
 \tag{15}
\]
The ring \(A[\eta]\) is a domain, so local nilpotence of \(\overline D\)
implies local nilpotence of \(N\).
This proves the existence of a nonzero \(N\) without promoting any
element or coordinate of a coefficient field.

## 3. The speed relation and the zero-shift refinement

Use the whole equality \(D(au+b)=1\). For elements of \(A\), the
coefficient of \(u^\delta\) in their \(D\)-image is \(N\).
By (13), \(aDu\) and \(Db\) both have degree at most \(\delta\).
The only possible degree-\(\delta+1\) term in
\[
                         (Da)u+aDu+Db=1
 \tag{16}
\]
has coefficient \(N(a)\). The right side has degree zero, whereas
\(\delta+1\ge1\). Hence
\[
                                      N(a)=0.
 \tag{17}
\]
This is the additional constraint supplied by the actual flow-affine
coordinate. It is stronger than merely producing some auxiliary
derivation from a coordinate partial.

When \(\delta=0\), (7) and (13) imply \(D(A)\subseteq A\) and
\(Du=\beta\in A\). In this case \(D|_A=N\), and (16) becomes
exactly (5). Because \(N(a)=0\), the ideal \((a)\) is stable, and
the quotient derivation satisfies
\[
                      \overline N(\overline b)=1
                      \quad\text{on }A/(a).
 \tag{18}
\]
The quotient is nonzero because \(a\) is a nonunit. This statement
does not assume it is reduced or a domain.
The usual finite slice identities apply to a \(\mathbb Q\)-algebra
even in this case, and give
\[
                  A/(a)=(\ker\overline N)[\,\overline b\,].
 \tag{19}
\]
Equation (19) concerns the whole speed-zero scheme, not a polynomial
recognition of \(A\).

There is also a whole-ring consequence specific to this zero-shift
case. Equation (5) shows directly on \(A\) and \(u\) that
\([E,D]=0\). Since \(D\) is the actual coordinate partial chosen in
(6),
\[
 C:=\ker D=\mathbb C[v_2,v_3,v_4],\qquad B=C[v].
\]
Commutation implies that \(E\) preserves \(C\). Its restriction
\(H:=E|_C\) is locally nilpotent. Moreover \(Da=N(a)=0\) and
\(Ea=0\), so \(a\in C\) and \(H(a)=0\). Consequently, on this
actual polynomial presentation,
\[
                         E=H+a\partial_v.
\]
Here \(H\ne0\): otherwise \(Eu=a\partial_vu=1\) would make \(a\)
a unit of \(B\), hence a nonzero complex constant and a unit of
\(A\), contrary to (2). This proves conditional entry into an
invariant-coefficient extension over a polynomial three-ring.
It neither places \(H\) in a specified homogeneous family nor proves
that an arbitrary completion can be replaced by one of zero shift.

The extension \(\widetilde N\) defined by
\(\widetilde N|_A=N\) and \(\widetilde N(u)=0\) is locally nilpotent
on \(A[u]\), and \([E,\widetilde N]=0\).
Thus the coordinate premise also supplies an independent commuting
additive direction, but it does not prove that direction is a
coordinate partial or has a slice.

## 4. Exact recovery from commutators

The construction has a finite description using the supplied \(E,u,D\).
Let
\[
                      C_\delta=\operatorname{ad}_E^\delta D,
                      \qquad
                      \beta_\delta=[u^\delta]Du\in A.
 \tag{20}
\]
Since \(E=\partial_u\) on \(A[u]\), repeated commutation differentiates
the polynomial \(u\)-coefficients of \(D\). Equations (13)--(14) give
\[
 C_\delta=\delta!\,(\widetilde N+\beta_\delta E),\qquad
 \operatorname{ad}_E^{\delta+1}D=0,\qquad C_\delta\ne0.
 \tag{21}
\]
These statements include \(\delta=0\).
In particular
\[
                \widetilde N
                =\frac{C_\delta-C_\delta(u)E}{\delta!}.
 \tag{22}
\]
The nonzero horizontal term makes \(\delta\) the terminal nonvanishing
commutator order here. The correction in (22) is essential: the raw
terminal commutator need not kill the supplied slice.

The shift and induced derivation depend on the chosen completion of
\(v\); no canonicity or minimality across completions is asserted.

## 5. A primitive induced derivation without a slice

Here is a full actual-coordinate boundary with \(\delta=0\).
Start with the known polynomial ring
\[
 B=\mathbb C[x,y,z,u],\qquad E=\partial_u,\qquad
 A=\mathbb C[x,y,z],
 \qquad
 N=x\partial_y+y\partial_z.
 \tag{23}
\]
Take
\[
 a=1+x,\qquad b=-y,\qquad
 v=(1+x)u-y,\qquad D=N+\partial_u.
 \tag{24}
\]
The speed \(Ev=1+x\) is nonzero and a nonunit, and \(E^2v=0\).
Define
\[
                   Y=y-xu,\qquad
                   Z=z-yu+\frac{x u^2}{2}.
 \tag{25}
\]
Then \((v,x,Y,Z)\) is an actual coordinate frame.
Its full inverse is
\[
                    u=v+Y,\qquad
                    y=Y+xu,\qquad
                    z=Z+yu-\frac{x u^2}{2}.
 \tag{26}
\]
The right sides are polynomials in the independent new coordinates
after the displayed substitutions. In both substitution orders,
(24)--(26) recover every coordinate. The Jacobian is \(-1\).

Direct differentiation gives
\[
                         Dv=1,\qquad Dx=DY=DZ=0.
 \tag{27}
\]
Therefore \(D\) is exactly the actual coordinate partial \(\partial_v\)
for this completion, not just a derivation chosen to have \(Dv=1\).
Its \(u\)-degree shift is zero, and its induced action is the displayed
\(N\). The exact zero-shift relation is
\[
                       N(-y)+(1+x)\cdot1=-x+1+x=1.
 \tag{28}
\]

The derivation \(N\) is irreducible on \(A\), since its nonzero
coefficients \(x,y\) have greatest common divisor one. It is locally
nilpotent by its triangular form. Nevertheless it has no slice:
\[
                              N(A)\subseteq(x,y)A,
 \tag{29}
\]
so it cannot send a polynomial to one. Equivalently it vanishes on
the entire line \(x=y=0\).
Modulo \(a=1+x\), it does have the prescribed slice
\(\overline b=-\overline y\), as (18) requires. Thus a slice on the
speed-zero scheme does not force a slice for the primitive \(N\)
on all of \(A\).

The kernel \(A\) in this control is already polynomial and \(E\)
already a translation. It is not a counterexample to recognition
under (2). Nor does it rule out a better choice of completion:
\((v,x,z,u)\) gives the coordinate partial \(-\partial_y\) instead.
The counterstatement is only that an induced primitive \(N\) need
not automatically be sliced.

## 6. A positive-shift completion and completion-dependence

For completeness, completion-dependence also occurs at positive shift.
In \(B=\mathbb C[x,y,z,u]\) with \(E=\partial_u\), take
\[
                   v=xu+y,\qquad W=z+xvu^2.
 \tag{30}
\]
The actual frame is \((v,x,W,u)\), with inverse
\[
                         y=v-xu,\qquad z=W-xvu^2.
 \tag{31}
\]
Its coordinate partial is
\[
                D=\partial_y-xu^2\partial_z,\qquad
                \delta=2,\qquad N=-x\partial_z.
 \tag{32}
\]
All four coordinate-partial equations follow from (30)--(31).
This \(N\) kills the speed \(a=x\) but has no slice, since
\(N(A)\subseteq xA\). Dividing by its invariant factor produces
the sliced derivation \(-\partial_z\), so this example alone would
not refute a claim about primitive induced actions. Section 5
supplies that separate primitive boundary.
The alternative completion \((v,x,z,u)\) has shift zero and induced
action \(\partial_y\). There is no claim that every completion has
positive shift or fails a slice test.

## 7. What this does and does not settle

The new necessary information from (2) is the speed-annihilating
action (4), the exact commutator recovery, and, for a zero-shift
completion, the quotient slice (18)--(19) and the actual presentation
\(E=H+a\partial_v\) over \(C=\ker D\simeq\mathbb C^{[3]}\).
These conclusions do not produce an
invariant ambient coordinate of \(B\), identify \(A\) with an actual
polynomial three-ring, or show that a completion with a more useful
induced action always exists.

In particular, a three-variable theorem whose input already requires
an actual presentation \(A=\mathbb C^{[3]}\) cannot be applied to
this \(N\) to prove that same presentation. The existence of a slice
for the original \(E\) is not a slice for \(N\), as the complete
primitive control demonstrates.

Fresh unsaved algebra checked both whole inverse directions and all
coordinate-partial, speed, and zero-shift identities in Section 5,
and independently the entire inverse and derivative identities in
Section 6. The general associated-graded and commutator arguments
are proved above, not inferred from these examples.

No saved checker was executed, imported, or compiled. No canonical
file or prior source was changed. This bounded working proof makes
no novelty or cancellation claim and requires a separate independent
saved-source review after full author review and a final HELD hash.
