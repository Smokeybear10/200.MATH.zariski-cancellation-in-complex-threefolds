# The rank-two normalizer bounds, but need not erase, compatibility torsion

The actual global Heisenberg normalizer bounds the annihilator of a
compatible-slice obstruction by one explicit divisor. A separate actual
polynomial example shows that the same Heisenberg structure can retain
nonzero torsion at that divisor, even though corrections exist modulo
every power. The extra original-coordinate commutator condition remains
essential and unresolved by this example.

## 1. Precise hypotheses and primitive intrinsic division

Let \(B=A[s]\simeq\mathbb C^{[4]}\), \(E=\partial_s\), and
let \(U,Y\) be polynomial LNDs with
\[
[E,U]=[Y,U]=0,\qquad [E,Y]=-gU,
\quad Eg=Ug=Yg=0,\quad g\ne0.
\tag{1}
\]
Assume \(E,U\) are independent and \(E,U,Y\) have rank two
over \(\operatorname{Frac}B\). Put
\[
D=U|_A\ne0,\quad R=\ker_A D,\quad b=U(s)\in A,
\qquad U=D+bE.
\tag{2}
\]
The [intrinsic quotient theorem](intrinsic-quotient-surface-pass.md)
gives \(R\simeq\mathbb C^{[2]}\) and faithful flatness of
\(A\) over \(R\). The cylinder also gives factoriality of \(A\).
Choose finitely many \(\mathbb C\)-algebra generators \(a_j\) of
\(A\), take \(\delta=\gcd_j D(a_j)\) in this UFD, and write
\[
D=\delta D_0.
\tag{3}
\]
The rational derivation \(D_0\) preserves \(A\): its values on
all the generators lie in \(A\), and the Leibniz rule gives the
same conclusion for every polynomial in them. Since
\(D\delta=\delta D_0\delta\), the LND divisibility lemma gives
\(D\delta=0\). Thus \(\delta\in R\), \(D_0\delta=0\),
and \(D^n(a)=\delta^nD_0^n(a)\) proves that \(D_0\) is an LND.
The values \(D_0(a_j)\) have gcd one. In particular, any rational
multiple \(rD_0\) which preserves \(A\) has \(r\in A\): a prime
in the reduced denominator of \(r\) would otherwise divide every
\(D_0(a_j)\). Thus the primitive-saturation property is intrinsic
and needs no choice or freeness of a tangent-module basis.
This argument does not turn a gcd-one ideal into the unit ideal.

## 2. The exact annihilator bound

For \(a\in A\), (1) gives \(E(Y(a))=-gD(a)\). Therefore
\[
Y|_A=P-gsD
\tag{4}
\]
for a polynomial derivation \(P:A\to A\), obtained by evaluating
at \(s=0\). The rank-two premise makes \(P\) a fraction-field
multiple of \(D_0\). Primitive saturation in (3) gives
\(P=rD_0\) with \(r\in A\). Thus
\[
Y(a)=(r-g\delta s)D_0(a),\qquad a\in A.
\tag{5}
\]
The same rank premise makes \(Y\) kill \(R\), since both \(E\)
and \(U\) kill \(R\). In particular \(Y\delta=0\).
Evaluate \([Y,U]=0\) on \(A\), using (2),(5):
\[
0=[Y,U](a)=\delta\bigl(gb-D_0r\bigr)D_0(a).
\]
The domain and nonzero-field hypotheses imply
\[
D_0r=gb,\qquad Dr=\delta g b.
\tag{6}
\]

The compatibility class \(\xi=[b]\in A/D(A)\) consequently
satisfies the explicit bound
\[
\delta g\,\xi=0.
\tag{7}
\]
The [faithfully flat cokernel lemma](compatible-slice-support-pass44.md)
makes its annihilator a principal ideal, say \(dR\). Equation (7)
gives \(d\mid\delta g\). If the intrinsic \(D\) is primitive,
one may take \(\delta=1\), so \(d\mid g\). More locally, at a
prime divisor \(\pi\) where \(\delta\) is a unit,
\(\operatorname{ord}_\pi d\le\operatorname{ord}_\pi g\).
Any nonzero plinth element \(p\) also confines the support of \(d\)
to \(p=0\), by the earlier lemma.

The formula gives the compatible localized slice explicitly:
\(s-r/(\delta g)\). It does not force \(d=1\) when \(g\)
shares a divisor with the primitive plinth.

For the actual pass-43 construction take \(U=[E,T_c]\).
Then \(V=-gU/a\) and \([E,Y]=aV=-gU\), so (1) has exactly
the displayed sign. Its rank-two branch satisfies all the assumptions
above. This argument does not assume that an \(E/g\)-slice is an
\(E\)-slice or that a local compatible slice is polynomial globally.

## 3. An actual rank-two Heisenberg control with nonzero obstruction

On the polynomial three-ring \(A=\mathbb C[x,y,z]\), put
\[
D=x\partial_y+2y\partial_z,\qquad v=xz-y^2.
\tag{8}
\]
Its kernel is \(R=\mathbb C[x,v]\): after inverting \(x\),
\(A_x=\mathbb C[x,x^{-1},v,y]\); a minimal negative denominator
would reduce to a nonzero polynomial in \(-y^2\) modulo \(x\),
which is impossible. This is the same exact triangular control used
in the earlier intrinsic quotient note.

The full plinth is \(xR\). Indeed \(Dy=x\). Conversely, if
\(Dh=c\in R\), then \(xh-cy\in R\). Reducing this identity
modulo \(x\) separates its even and odd parts in \(y\), and
forces \(c(0,v)=0\), hence \(x\mid c\) in \(R\).
The coefficients \(x,2y\) have gcd one, so \(D\) is primitive.

On \(B=A[s]\), define
\[
E=\partial_s,\qquad U=D+E,\qquad
Y=(y-xs)U,
\qquad g=x.
\tag{9}
\]
All are actual LNDs. For \(Y\), use \(U(y-xs)=0\), so it is
an invariant replica of \(U\). Directly,
\[
[E,U]=[Y,U]=0,\qquad [E,Y]=-xU,
\qquad Ex=Ux=Yx=0.
\tag{10}
\]
The ranks are two as required. The actual constant partial
\(\partial_z\) kills \(g\).

Here \(b=U(s)=1\), and
\[
\operatorname{Ann}_R([1])=D(A)\cap R=xR.
\tag{11}
\]
Thus the bound (7) is attained with \(\delta=1\). The class is
nonzero not only globally but also at the height-one localization
\(R_{(x)}\): its annihilator there is the proper ideal
\(xR_{(x)}\). Localization commutes with the image and invariant
conditions because its denominators lie in \(R\).

There is a compatible slice after inverting \(x\), namely
\(s-y/x\), but none over \(R_{(x)}\). In (6) the explicit
coefficient is \(r=y\).

The field \(U\) even has an actual coordinate slice. The invariant
coordinates \(x, y-xs,z-2ys+xs^2\), together with \(s\), have
the polynomial inverse
\[
y=\eta+xs,\qquad z=\zeta+2\eta s+xs^2,
\]
and \(U=\partial_s\) in that frame. This does not make \(E,U\)
simultaneous coordinate partials, or produce an \(E\)-slice killed
by \(U\).

Crucially, no actual constant partial \(T_c\) with
\(U=[E,T_c]\) is supplied by (9), nor is an unresolved full
adjoint frame supplied. The example therefore refutes automatic
compatibility from the selected Heisenberg/rank/slice properties,
not the stronger original-coordinate condition.

## 4. Corrections modulo every divisor power still exist

The same primitive example admits compatible corrections to every
finite order along \(x=0\), despite (11). Work in \(A_v\),
which is allowed at the generic point \((x)\) of \(R\).
For \(N\ge1\), set
\[
c_k=\frac{\binom{2k}{k}}{4^k},\qquad
f_N=-\sum_{k=1}^N c_k\frac{x^{k-1}y z^k}{v^k}.
\tag{12}
\]
These are actual elements of \(A_v\); they do not invert \(x\).
Writing \(w=xz/v\), the defining relation \(y^2=xz-v\) gives
\[
D\left(\frac{x^{k-1}y z^k}{v^k}\right)
=(2k+1)w^k-2k w^{k-1}.
\tag{13}
\]
The exact recurrence
\(2(k+1)c_{k+1}=(2k+1)c_k\), together with \(2c_1=1\),
telescopes (13) to
\[
Df_N=1-(2N+1)c_N w^N.
\tag{14}
\]
Consequently \(E(s-f_N)=1\) and
\(U(s-f_N)\in x^N B_v\) for every \(N\).
The successive differences \(f_{N+1}-f_N\) belong to
\(x^N A_v\), so the corrections even define a compatible formal
limit in the \(x\)-adic completion. They do not yield an element
of \(A\otimes_R R_{(x)}\) solving \(Df=1\), as (11) proves.

This is a concrete nonseparated-cokernel phenomenon, not a defect in
the height-one detection theorem. The latter detects the actual
localized class; it does not identify that class with its image in
every finite quotient or completion.

## 5. Verification, attribution, and stopping point

Equations (6) and (13)--(14) are complete all-degree algebraic proofs.
The triangular derivation, kernel and plinth are the inherited actual
example, now used to test the specific height-one completion shortcut.
No extra numerical suite or method count is added for this note.

Primitive division uses only the already established intrinsic UFD
and a finite set of algebra generators. The support conclusion invokes the new
[cokernel formulation](compatible-slice-support-pass44.md), which
explicitly credits the published Daigle--Kaliman invariant-subtraction
mechanism. The derivations in the countercontrol are reconstructed
directly, with no assumption of an actual high-degree realization.

The remaining obligation is genuinely specific: use the supplied
actual constant partial and its additional full-frame identities to
kill the compatibility class at common prime divisors, or find a
different global recognition route. The selected Heisenberg equations
and all-order congruence correction alone cannot do so. No conclusion
of nonpolynomiality, unrestricted cancellation, novelty, human expert
review or proof-assistant verification is made.
