# Direct rectification and the descended rank-three action

## 1. Additional conclusion, with the original recognition proof retained

For the entire repaired family of595, its polynomial automorphism
\(\Psi\) satisfies the stronger identity
\[
E\Psi=\Psi\partial_t.
\tag{1}
\]
Thus its three base-coordinate images already generate \(\ker E\),
without applying a further Taylor projection. The derivation induced
there by the commuting original \(\partial_t\) is explicitly conjugate
to the negative of another member of the same rank-three DG family.

This is an addendum to
[pass 595](rank-three-family-pole-repair-recognition-pass595-working.md),
not a change to that source. Its proof by Taylor projection remains
valid. Its warning that \(\Psi(t)=u\) alone does not prove (1) also
remains correct: the extra commutator argument below proves (1).
The Taylor projection is the identity on these particular images
after this additional proof.

The rank conclusion uses the existing Dasgupta--Gaifullin theorem
with all its parameters checked. It is not a new rank classification
or recognition theorem for arbitrary extensions. These kernels are
already recognized polynomial rings; no cancellation or novelty claim
is made.

## 2. Exact retained family and map

Use the actual rings \(R=\mathbb C[x,y,z]\) and \(B=R[t]\). Assume
\[
m,n\ge2,\qquad F(X,Z)\in\mathbb C[X,Z],\qquad
F(X,0)\notin\mathbb C.
\tag{2}
\]
Put
\[
\begin{gathered}
f=xz-y^m,\qquad r=xF(x,f)+yf^n,\qquad
g=\frac{f^{mn+1}+r^m}{x},\\
H=\operatorname{Jac}(f,g,\cdot),\qquad
b=-gf^{n-2},\qquad
E=H+(1+fbr)\partial_t,\\
v=ft-r^2/2,\qquad
u=t-brv+\frac{fb^2}{2}v^2.
\end{gathered}
\tag{3}
\]
The base derivation \(H\) is extended initially by \(Ht=0\).
The apparent quotient defining \(g\) is polynomial, as verified
in595 by the full binomial expansion. In particular
\[
Hf=Hg=0,\qquad Hr=-gf^n=f^2b,\qquad Ev=f,\qquad Eu=1.
\tag{4}
\]

On precisely \(B_f\), define
\[
L=H/f+br\partial_t,\qquad A=-vL,\qquad \Phi=\exp(A).
\tag{5}
\]
The local nilpotence of \(H\) is retained from595. Since \(Hf=0\),
\(H/f\) is locally nilpotent on \(R_f\). Adjoining \(t\) with
derivative \(br\) preserves local nilpotence, so \(L\) is an LND.
The identities \(Lf=Lg=Lb=Lv=0\), \(Lr=fb\), and
\(Lt=br,\ L^2t=fb^2,\ L^3t=0\) license these locally nilpotent
derivations and finite exponentials there. In particular \(\Phi(t)=u\).

Write
\[
s(x)=xF(x,0),\qquad
C(x)=\frac m2s^{m+1}s'-\frac{s^{m+2}}{2x},\qquad
\delta_0=x\partial_y+m y^{m-1}\partial_z.
\tag{6}
\]
The polynomial \(s\) is divisible by \(x\), so both summands of
\(C\) lie in \(x^{m+1}\mathbb C[x]\). Thus \(C/x\) is polynomial.
The repair in595 is
\[
\Gamma=\exp\!\left(-\frac{C(x)}{xf}\delta_0\right),
\qquad \Psi=\Phi\circ\Gamma.
\tag{7}
\]
Both factors are initially automorphisms of \(B_f\).
The derivation \(\delta_0\) fixes \(x,f,t\), and hence its multiplier
in (7); this is an invariant replica, not an exponential with an
uncontrolled variable coefficient.

We retain the proved whole conclusion of595:
\[
\Psi\in\operatorname{Aut}_{\mathbb C}(B),\qquad \Psi(t)=u.
\tag{8}
\]
That source establishes (8) by cancellation of the \(y\)-pole,
primality for the \(z\)-image, and descent of the localized inverse.
The present addendum does not infer (8) from a Jacobian alone or
redo that recognition proof.

The entire source595 was read through EOF at SHA256
8e4e68eae92f3d57b360f16d1179240525d6022e3bcd02a72899f7ede1f90bf7.
No unfinished neighboring source is an input.

## 3. Whole direct intertwining

On \(B_f\), the definitions give the exact decomposition
\[
E=\partial_t+fL,\qquad
[E,L]=[\partial_t,L]=0,\qquad
Ev=\partial_tv=f.
\tag{9}
\]
Indeed all coefficients of \(L\) are independent of \(t\), and
\(Lf=0\). Since \(A=-vL\), it follows that
\[
[E,A]=[\partial_t,A]=-fL,\qquad [A,fL]=0.
\tag{10}
\]
Here and below \([P,Q]=PQ-QP\). The last equality uses both
\(Lf=0\) and \(Lv=0\), so all higher nested commutators vanish.

For either \(Q=E\) or \(Q=\partial_t\), (10) gives
\([Q,A^j]=jA^{j-1}[Q,A]\). Applying this identity to the finite
exponential on any element proves, with the signs retained,
\[
E\Phi=\Phi(E-fL)=\Phi\partial_t,\qquad
\partial_t\Phi=\Phi(\partial_t-fL).
\tag{11}
\]
No convergence or infinite operator-series assertion is needed.

The map \(\Gamma\) fixes \(t\) and has coefficients independent
of \(t\), so it commutes with \(\partial_t\). Therefore
\[
E\Psi=E\Phi\Gamma=\Phi\partial_t\Gamma
     =\Phi\Gamma\partial_t=\Psi\partial_t
\tag{12}
\]
on \(B_f\). Both sides preserve \(B\), by (8), so (12) is an
identity on the whole polynomial ring. In particular, writing
\[
X=\Psi(x),\qquad Y=\Psi(y),\qquad Z=\Psi(z),
\tag{13}
\]
gives
\[
B=\mathbb C[X,Y,Z,u],\qquad
EX=EY=EZ=0,\quad Eu=1,\quad
\ker E=\mathbb C[X,Y,Z].
\tag{14}
\]
The final equality follows by conjugating \(\ker\partial_t=R\)
through the actual automorphism \(\Psi\). No candidate invariant
was promoted to a coordinate without that map.

For the usual finite slice projection
\(\pi_E(P)=\sum_{j\ge0}(-u)^jE^jP/j!\), (14) proves
\(\pi_E(X)=X,\ \pi_E(Y)=Y,\ \pi_E(Z)=Z\).
This explains precisely why that additional step in595 is unnecessary
for these images once (12) is proved.

## 4. The descended derivation, with its full sign

The original \(\partial_t\) commutes with \(E\), so it preserves
\(\mathcal A:=\ker E\). It restricts to a locally nilpotent
derivation of \(\mathcal A\). For every \(P\in R\), the second
identity in (11) gives
\[
\partial_t\Psi(P)
=-\Phi H\Gamma(P)
=-\Psi\bigl(\Gamma^{-1}H\Gamma(P)\bigr).
\tag{15}
\]
Here \(\Gamma(P)\in R_f\) is independent of \(t\), so the
restriction of \(fL\) used in this calculation is exactly \(H\).

It remains essential to identify the conjugate in (15) as a
polynomial derivation, not just a localized one. The inverse
repair fixes \(x,f,t\) and sends \(y\) to \(y+C(x)/f\). Consequently
\[
\begin{gathered}
\widetilde r:=\Gamma^{-1}(r)
=r+C(x)f^{n-1}
=x\widetilde F(x,f)+yf^n,\\
\widetilde F(X,Z)
=F(X,Z)+\frac{C(X)}{X}Z^{n-1},\\
\widetilde g:=\Gamma^{-1}(g)
=\frac{f^{mn+1}+\widetilde r^{\,m}}{x}.
\end{gathered}
\tag{16}
\]
The displayed \(\widetilde F\) is polynomial since \(C/X\) is.
The same full binomial divisibility as in (3) then makes
\(\widetilde g\) polynomial. These conclusions do not require
that \(\Gamma\) itself extend across \(f=0\).

We also need its exact Jacobian factor. In the original base
coordinates, \(\operatorname{div}\delta_0=0\).
Writing \(\lambda=C(x)/(xf)\), one has \(\delta_0\lambda=0\).
Thus
\[
\operatorname{div}(-\lambda\delta_0)=0
\quad\hbox{on }R_f.
\tag{17}
\]
The flow with independent parameter \(w\) has Jacobian determinant
whose derivative is its determinant times the transported divergence.
It is therefore identically one, with initial value one. Evaluating
at \(w=1\) proves
\[
\det J(\Gamma)=\det J(\Gamma^{-1})=1.
\tag{18}
\]
Equivalently, the Lie derivative of the original volume form is
zero. This argument applies to the invariant replica in (7);
divergence zero of \(\delta_0\) alone would not suffice for an
arbitrary multiplier.

The chain rule for Jacobian derivations, (18), and
\(\Gamma^{-1}f=f\) now give the full localized identity
\[
\Gamma^{-1}H\Gamma
=\operatorname{Jac}(f,\widetilde g,\cdot)
=:\widetilde H.
\tag{19}
\]
The right side is a polynomial derivation by (16), so (15) descends
without denominators to the actual base \(R\). In the actual
coordinates (13) on \(\mathcal A\), the restricted derivation is
exactly \(-\widetilde H\).

For an additional check on the vertical sign, the entire transformed
commuting derivation on \(B\) is
\[
\Psi^{-1}\partial_t\Psi
 =-\widetilde H+
   \bigl(1+\widetilde g f^{n-1}\widetilde r\bigr)\partial_t.
\tag{20}
\]
Indeed it is
\(\Gamma^{-1}(\partial_t-fL)\Gamma\);
\(\Gamma^{-1}(b)=-\widetilde g f^{n-2}\).
Formula (20) is consistent with (19) on \(R\) and remains a whole
polynomial LND because it is conjugate to \(\partial_t\).

## 5. Exact published rank input and structural boundary

Dasgupta--Gaifullin, Theorem 5.7, asserts rank three for the
Jacobian family with \(m\ge2,\ n\ge1\), and
\(F(X,0)\notin\mathbb C\). Its family construction and complete
proof were reread directly. This is the retained external rank
input, not a rank theorem proved by the present calculation.
[Primary statement and proof, Section 5](https://arxiv.org/html/2306.00510v2)

Here \(m,n\) still satisfy (2), and (16) gives
\[
\widetilde F(X,0)=F(X,0)\notin\mathbb C
\tag{21}
\]
because \(n-1\ge1\). Thus \(\widetilde H\) is exactly a member
of that family with the same permitted \(m,n\), not a derivation
inferred rank three from similarity of leading terms. The theorem
applies to \(\widetilde F\) even if its added term destroys ordinary
homogeneity.

It follows that the descended \(\partial_t\) has rank three on the
polynomial ring \(\mathcal A\). Multiplication by \(-1\) and the
actual coordinate isomorphism \(\Psi:R\to\mathcal A\) preserve rank.
In particular it kills no coordinate of that three-variable ring.
The original \(H\) also has rank three on \(R\).

This distinguishes two rings carefully: \(E\) is rectified on the
four-ring \(B\), but the descended commuting action still has rank
three on its three-dimensional kernel. Slicing \(E\) does not
automatically produce an invariant coordinate for that descended
action. This is not a failure to recognize \(\mathcal A\), which
already equals \(\mathbb C[X,Y,Z]\) by (14).

The conclusion also transports to the homogeneous first-shift
examples of598. There \(m=2,\ F(X,Z)=X^{2n}\), and the actual
gauge is \(T=t-z^{4n}\). That shear commutes with the original
\(\partial_t\) and intertwines the two extensions. Composing it
with \(\Psi\) preserves (15), so the descended action remains
conjugate to the same \(-\widetilde H\). No Euler weights are
silently transferred across that gauge; the first-shift assertion
belongs to the separately computed actual frame in598.

## 6. Verification and status

Fresh unsaved symbolic checks for \((m,n)=(2,2),(2,3),(3,2)\),
with \(F(X,Z)=X^2+(1+X)Z\), reconstructed the complete localized
commutators and the conjugacy (19), including its sign and all
lower coefficients. Separate full local-slice polynomial checks
verified \(E\Phi(r)=E\Phi(x)=0,\ E\Phi(t)=1\) and the
\(\partial_t\)-derivative signs in (11). All residuals were zero.
The universal proof is the exact finite operator computation
and parameter match, not those finite samples.
No saved checker was executed, imported, or compiled.

The scope remains this recognized family and the stated gauge
transport. No arbitrary common-kernel extension theorem, new
coordinate-entry principle, globally minimal-frame conclusion,
or general cancellation result is asserted. The earlier proof595
is unchanged and remains valid.
