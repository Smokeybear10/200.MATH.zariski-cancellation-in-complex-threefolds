# A full-curve ramification obstruction to dependent parameter motion

In the rotating dependent high-top branch, the full preceding companion
matrix strengthens the previous trace obstruction. Nonzero motion of
the polynomial curve parameter requires the reduced multiplier to
divide the common derivative gcd of the entire invariant curve,
including its good components. Divisibility by the highest coefficient's
derivative alone is insufficient.

This is a necessary condition on the actual supplied frame. It does
not exclude every moving parameter. A separate actual polynomial
coordinate control shows why invariance of the next speed under the
primitive defect cannot be assumed from the commutator, highest-flow
vector and trace identity alone.

## 1. Actual hypotheses and notation

Retain the actual dependent high-top hypotheses and identities of
[the preceding-curve proof](dependent-preceding-curve-pass44.md).
Thus \(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(E\) is an LND with an
original polynomial slice, and the actual coordinate partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
The two nonzero quadratic defects have the primitive decomposition
\[
V_3=aD,\quad V_4=bD,\qquad [E,D]=0,\qquad
a,b\in\ker E\cap\ker D,
\tag{2}
\]
where \(D\) is a primitive polynomial LND and \(a,b\) have no
nonzero complex constant relation. The highest nonconstant vector is
\[
E^mx=cq,\quad m\in\{3,4\},\quad c\ne0,\quad c_3=c_4=0,
\qquad z=E^{m-1}x,\quad y=E^{m-2}x.
\tag{3}
\]
Choose \(j\) with \(c_j\ne0\). The actual polynomial parameter
description is
\[
\tau=z_j/c_j,\qquad z=c\tau+K(u),\quad K_j=0,\qquad
q=Q(u),\quad \deg Q>0,\qquad Eu=Du=0.
\tag{4}
\]
The parameter \(u\) need not be an ambient coordinate. This input is
obtained only after the preceding proof establishes the relevant
transcendence degree and applies its stated polynomial curve theorem.
No additional curve-factorization theorem is invoked below.

Write
\[
\alpha=(m-1)/2,\quad \beta=m(m-1)/2,\quad
Dz=ct,\quad r\ne0,\quad Er=Dr=0,
\]
\[
[E,T_c]=-\alpha rD,\qquad E\tau=q,\quad D\tau=t,\qquad
T_cq=\beta rt.
\tag{5}
\]
In particular \(Et=0\), since \(E(D\tau)=Dq=0\).
There is no assumption that \(Dt=0\).

In the rotating alternative, the full multiplier normal form is
\[
a=H_1Q_1(u)a_0(u),\qquad
b=H_1Q_1(u)b_0(u),\qquad r=H_1R_1(u),
\tag{6}
\]
with all univariate factors defined in the preceding proof and
\(H_1\ne0\) jointly invariant under \(E,D\). Define the monic
polynomial
\[
G_0=\gcd(Q',K_1',K_2',K_3',K_4')\in\mathbb C[U].
\tag{7}
\]
This gcd is nonzero because \(Q'\ne0\). Zero components of \(K'\)
are allowed. The rotating alternative ensures that \(K'\) is not
zero and is independent of \(c\), since \(K_j'=0\) and the bad
components rotate nontrivially.

## 2. The full preceding matrix determines the next defect layer

Let \(J=\operatorname{Jac}(Ex)\), \(d=D(x)\), and
\(\ell=(0,0,a,b)\). The actual companion and its preceding power are
\[
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix},
\qquad N=M^{m-1}.
\tag{8}
\]
The established Jordan alternatives give \(\operatorname{rank}N=2\).
Its base upper block is \(\operatorname{Jac}z/(m-1)!\), of rank two.
Consequently projection from \(\operatorname{im}N\) to the first
four coordinates is injective. The independent directions \(c,K'(u)\)
therefore have unique lifts to \(\operatorname{im}N\).

Evaluating the base columns on the velocity \(Ex\) gives
\[
N\binom{Ex}{0}
=\frac{q}{(m-1)!}\binom{c}{(m-1)r}.
\tag{9}
\]
Thus the two lifted directions can be written
\[
C_1=\binom{c}{(m-1)r},\qquad C_2=\binom{K'}{\psi}
\]
for some \(\psi\in\operatorname{Frac}B\). The full auxiliary upper
column of \(N=M^{m-2}M\) is
\(-Dy/[2(m-2)!]\). Its membership in the same two-dimensional image
gives \(Dy=cA+K'B_1\), initially over \(\operatorname{Frac}B\).
The choice \(K_j=0\) shows
\[
A=(Dy)_j/c_j=D(y_j/c_j)\in B.
\]
Retaining that auxiliary column, the entire matrix factors as
\[
N=\frac1{(m-1)!}
\begin{pmatrix}C_1&C_2\end{pmatrix}
\begin{pmatrix}
 d\tau&-\alpha A\\
 du&-\alpha B_1
\end{pmatrix}.
\tag{10}
\]
Here \(d\tau,du\) are ordinary differential rows.

Equation (5) gives \(MC_1=0\). The full highest matrix is
\[
M^m=\frac1{m!}C_1\begin{pmatrix}Q'\,du&-mt/2\end{pmatrix}.
\tag{11}
\]
Compare \(MN\) with (11). A nonzero base component of \(du\) first
gives \(MC_2=(Q'/m)C_1\). Comparison of the auxiliary column then
gives \(Q'\alpha B_1=mt/2\). Therefore
\[
\boxed{\quad
Dy=cA+\frac{m}{m-1}\frac{t}{Q'(u)}K'(u),\qquad
A=D(y_j/c_j)\in B,\quad EA=t.
\quad}
\tag{12}
\]
All vector entries on the left and \(cA\) are polynomial.
Equation (12) is not obtained from the upper-left block alone.
In particular it does not identify the variable lower row with the
differential of its product.

## 3. A stronger necessary condition for parameter motion

Equation (12) implies \(Q'(u)\mid tK_i'(u)\) in \(B\) for every
component \(i\). A univariate Bezout identity for the family
\(Q',K_1',\ldots,K_4'\) gives
\(Q'(u)\mid tG_0(u)\). Cancellation in the domain yields a
polynomial \(T\in B\) with
\[
t=(Q'/G_0)(u)T,\qquad ET=0.
\tag{13}
\]
The assertion \(ET=0\) uses \(Et=Eu=0\), not any invariance under
\(D\). The trace in (5) now becomes
\[
G_0(u)T_cu=\beta H_1R_1(u)T.
\tag{14}
\]
Let \(R_2=R_1/\gcd(R_1,G_0)\). The corresponding univariate Bezout
identity implies \(R_2(u)\mid T_cu\). If \(R_2\) is nonconstant,
then \(R_2(u)\) divides
\[
T_c(R_2(u))=R_2'(u)T_cu.
\]
For an LND on a characteristic-zero domain, a nonzero polynomial
dividing its derivative has derivative zero: a nonzero derivative
lowers LND degree, whereas multiplication cannot lower it. Apply this
to the actual constant partial \(T_c\). It forces \(T_cu=0\).
Consequently
\[
\boxed{\quad T_cu\ne0\ \Longrightarrow\ R_1\mid G_0
\quad\text{in }\mathbb C[U].\quad}
\tag{15}
\]
Every multiplicity is retained. This strengthens the previous
condition \(R_1\mid Q'\). If \(R_1\nmid G_0\), the
[zero-motion recognition theorem](rotating-zero-motion-closure-pass45.md)
applies and gives an invariant ambient coordinate and
\(\ker E\simeq\mathbb C^{[3]}\).

One can see the additional content without asserting realizability
of arbitrary curve data. Take \(Q=U^3\), \(K_3=1\), \(K_4=U^5\).
For \(m=3\) or \(4\), the reduced \(R_1\) is a nonzero constant
multiple of \(U^2\), so the old divisibility condition holds. If
the remaining good component is \(K_i=U\), then \(G_0=1\), and
(15) excludes motion. Without that component, \(G_0=U^2\), so the
stronger necessary condition still passes. Neither choice of formal
curve data is asserted to occur in the target frame.

Thus a nonconstant \(R_1\) in a genuinely moving case can be supported
only at zeros of the derivative vector of the entire parameterized
curve \((Q,K)\), with the multiplicities bounded by (7).
The condition does not exclude constant \(R_1\), nor does it prove
that the remaining ramified curves are realizable.

## 4. Why the next speed is not automatically jointly invariant

Even the immediate mixed-column equations do not add \(Dt=0\).
Put \(k=T_cu\), and write \(a_i=a,b\) for \(i=3,4\).
The inherited next bad-column identity gives
\[
W_i u=-\frac{m a_i t}{2Q'(u)},\qquad
Q'(u)k=m\alpha rt.
\tag{16}
\]
The quadratic coefficient of the commuting conjugated columns is
\([T_c,V_i]+2[W_c,W_i]=0\), with \(W_c=-\alpha rD\).
Applied to \(u\), it gives
\[
-a_iDk-2\alpha rD(W_i u)=0.
\tag{17}
\]
Since \(D\) kills \(a_i,r,Q'(u)\), substitution of (16) makes
(17) precisely \(D\) applied to the trace, with no extra restriction.

There is a useful exact test for the missing invariance. Applying
\(E\) to a second actual \(T_c\)-derivative of \(q\), and using
\(E(T_cq)=0\), gives
\[
E(T_c^2q)=-\alpha rD(T_cq)
          =-\alpha\beta r^2Dt.
\tag{18}
\]
Thus \(Dt=0\) is equivalent to \(T_c^2q\in\ker E\) in the present
nonzero-\(r\) setting. Neither membership is automatic from the
first derivative or trace.

## 5. An actual polynomial-coordinate control with \(Dt\ne0\)

This control retains an actual slice, actual coordinate partial,
primitive commuting direction, highest-flow vector and the trace.
It deliberately does not satisfy all the adjoint bounds (1).
Start in the genuine polynomial ring \(\mathbb C[s,u,v,z]\), with
\[
E=\partial_s,\qquad D=\partial_v,\qquad
C=\partial_z+6v\partial_u-s\partial_v.
\tag{19}
\]
The following are polynomial coordinates:
\[
a=z+\frac{us^3}{6}+\frac{v^2s^2}{2},\qquad
S=s,\qquad V=v+sz,\qquad U=u-6vz-3sz^2.
\tag{20}
\]
Their actual inverse is
\[
z=a-\frac{US^3}{6}-\frac{V^2S^2}{2},\qquad
s=S,\qquad v=V-Sz,\qquad u=U+6Vz-3Sz^2.
\tag{21}
\]
Substitution in both directions proves polynomial inversion.
Direct differentiation gives \(Ca=1\) and \(CS=CV=CU=0\);
hence \(C=\partial_a\) in the actual frame (20), not merely a
Jacobian-one derivation without coordinates.

In that frame,
\[
E^3(a,S,V,U)=(u,0,0,0),\qquad E^4(a,S,V,U)=0,\qquad
[E,C]=-D,\quad [E,D]=0.
\tag{22}
\]
For \(m=3\), \(c=(1,0,0,0)\), \(q=u\), \(r=1\) and
\(\tau=E^2a=us+v^2\), all the indicated relations become
\[
E\tau=q,\quad D\tau=t=2v,\quad
Cq=6v=3rt,\qquad Et=0,\quad Dt=2.
\tag{23}
\]
In particular \(q\in\ker E\cap\ker D\), but \(Cq\) is not in that
joint kernel. The actual partial need not normalize the common
invariant ring under these weaker hypotheses. Also
\(C^2q=-6s\), so (18) reads \(E(C^2q)=-6\).

The adjoint-height profile of the actual coordinate partials in
the order \((a,S,V,U)\) is exactly
\[
(1,4,4,4).
\tag{24}
\]
Here the height is the largest \(j\) for which
\(\operatorname{ad}_E^jT\ne0\). It can be computed by differentiating
the two-sided inverse (21) to recover the actual partials in the
original variables; since \(E=\partial_s\) there, their heights are
their largest coefficient degrees in \(s\). Their \(s^4\) coefficients,
in the original ordered basis
\((\partial_s,\partial_u,\partial_v,\partial_z)\), are respectively
\(-z^2\partial_v/2\), \(z\partial_v\), and \(\partial_v/6\), with no
higher coefficients. The last three heights exceed (1). Thus this
is not a realization or counterexample to the
full dependent-defect profile, and does not refute a possible
full-frame proof of \(Dt=0\).

## 6. Exact remaining gap and verification scope

For the original moving rotating branch, the new full-layer
constraint is (12), with the all-multiplicity consequence (15).
In the still-allowed case \(R_1\mid G_0\), neither normalization
of \(\ker E\cap\ker D\) by \(T_c\), nor \(Dt=0\), nor an ambient
coordinate property of \(u\) has been established. The matrix
factorization and the immediate mixed identities are necessary
conditions, not a sufficient integrability test.

The polynomial coordinate control shows that the omitted full-frame
information matters. It cannot be replaced by an assumption of
joint invariance justified only from the already available first
trace. No arbitrary nilpotent matrix or univariate curve is promoted
to a polynomial action.

The companion identities and polynomial parameter are inherited from
the linked complete proofs. The new argument is elementary matrix
factorization, univariate Bezout and LND degree comparison; it uses
no additional external recognition theorem beyond the already
established zero-motion corollary. The finite checker tests bounded
instances of these mechanisms and the actual inverse, not the
universal proof or the unresolved cancellation statement.

The standalone
[four-method checker](dependent_motion_ramification_checks_pass46.py)
imports only unittest and SymPy. Its first run passed all four
methods in 0.236 seconds. Its formal matrix method isolates exactly
the auxiliary-column comparison that is absent from a base-block-only
test. The repeated-factor curve method distinguishes the old trace
test from the full-curve condition. The actual coordinate methods
check both inverse compositions, the exact height profile and the
nonzero second derivative in (18). None constructs an action in the
remaining moving target profile. Independent reconstruction is not
expert review or proof-assistant verification.
