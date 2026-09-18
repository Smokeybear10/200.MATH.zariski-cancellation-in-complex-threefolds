# Actual dense sliced controls of unbounded last-coordinate degree

There are actual sliced polynomial frames with a dense rank-two good-speed
row and arbitrarily high last-coordinate time degree. The family below is
already a translation in adapted coordinates. It is a positive control for
the dense Taylor chart, not a counterexample to cancellation or a proof of
general dense-frame recognition.[^1]

## 1. The actual coordinates and both inverse orders

In \(B=\mathbb C[u,a,b,c]\), let \(E=\partial_u\). Set
\[
X=u,\qquad Y=a+bu,\qquad Z=b+cu,\qquad
W_0=c,\qquad W_\ell=c+Y^\ell\quad(\ell\ge3).
\tag{1}
\]
The subscript zero denotes the unsheared coordinate, not the formula
\(c+Y^0\). The maps in (1) are compositions of elementary shears:
first replace \(a\) by \(a+bu\), then \(b\) by \(b+cu\), and
finally replace \(c\) by \(c+Y^\ell\), leaving the other current
coordinates unchanged. The inverse is
\[
\begin{gathered}
u=X,\qquad c=W_\ell-Y^\ell,\qquad
b=Z-cX,\qquad a=Y-bX,\\
\text{or }c=W_0\text{ for the unsheared case}.
\end{gathered}
\tag{2}
\]
Each formula uses only quantities already recovered. Substituting (1)
into (2) recovers \(u,c,b,a\) successively; substituting (2) into
(1) recovers \(X,Y,Z,W_\ell\) in the reverse order. Thus both
compositions are polynomial identities on the whole affine space.
The Jacobian in the order \((u,a,b,c)\) is one.

## 2. Slice, dense speed row, and exact degree

The derivation and the speed data satisfy
\[
\begin{gathered}
EX=1,\qquad (EX,EY,EZ)=(1,b,c),\qquad
E^2X=E^2Y=E^2Z=0,\\
\ker E=\mathbb C[a,b,c],\qquad (E(B))B=B,\\
E^\ell W_\ell=\ell!\,b^\ell\ne0,\qquad
E^{\ell+1}W_\ell=0 .
\end{gathered}
\tag{3}
\]
Thus the actual coordinate \(X\) is a slice. The two nonconstant
speeds \(b,c\) are algebraically independent, so the speed rank is
two. No nonzero homogeneous polynomial vanishes on \((1,b,c)\):
dehomogenizing a homogeneous polynomial at its first variable equal
to one preserves its distinct monomials. Equivalently, the cone map
\((t,b,c)\mapsto(t,tb,tc)\) has Jacobian \(t^2\ne0\).
This is the dense, not the nonlinear conical, speed case.

The derivative formula in (3) holds for every \(\ell\ge3\), because
\(EY=b\) is invariant. The unsheared coordinate \(W_0\) has time
degree zero. No upper bound on the sheared degree follows from the
presence of three good coordinates.

## 3. Selected partial and the two tail stages

The last-coordinate partial in every member of the family is
\[
T=\partial_{W_\ell}\big|_{X,Y,Z}
 =\partial_c-X\partial_b+X^2\partial_a,\qquad
N=[X^2]T|_{\mathbb C[a,b,c]}=\partial_a,
\qquad L=\mathbb C(b,c).
\tag{4}
\]
Indeed the displayed derivation kills \(X,Y,Z\), takes value one
on \(c\), and kills \(Y^\ell\). Hence it is the actual coordinate
partial, not just a coefficient derivation with prescribed values.
The coefficient field and generic-line variables may be chosen as
\[
\tau=b,\qquad \rho=c,\qquad v=a,\qquad
y=a,\qquad z=b=\tau,\qquad
L[y,z]=L[v],\qquad N(v)=1 .
\tag{5}
\]

The two negative-tail calculations use the positive Taylor-sign
convention of the dense chart and its tail lemma.[^2] In this example
\(\Theta(\rho)=\rho+z/X\) and
\(\Theta(\tau)=\tau+y/X\). For the sheared family take
\(\mathscr S=\Theta(\rho)+X^\ell\Theta(\tau)^\ell\);
for the unsheared member omit the second term. In either case,
\[
\begin{gathered}
\mathscr R=W_\ell-\mathscr S=-z/X,\qquad
f_{-1}=-\tau,\qquad Q(U,V)=\tau-V,\\
\mathscr R-X^{-1}\Theta(f_{-1})=y/X^2,\qquad
R_2(U,V)=U,\qquad
(R_{2,U},R_{2,V})=(Q_\tau,Q_\rho)=(1,0).
\end{gathered}
\tag{6}
\]
The equality on the second line uses the evaluated relation
\(z=\tau\), not a formal identity between independent \(U,V\).
Both tails have \(T\)-derivative one: directly,
\(T(-b/X)=1\) and \(T(a/X^2)=1\). Thus the first tail records
the nonzero equation \(z-\tau=0\), and the next one recovers the
intrinsic parameter. The displayed rational tails do not assert that
localizing an arbitrary locally nilpotent derivation preserves local
nilpotence.

## Verification and limits

The [independent checker139](dense_taylor_tail_controls_pass139.py)
checks the unsheared member and \(\ell=3,4\), including both inverse
orders, the Jacobian, exact degrees, speed rank and density, selected
partial and tail signs. The arbitrary-degree statement here is proved
by (1)--(3), not inferred from the finite samples.

The other checker methods use formal determinant jets, truncated Taylor
series over a proper algebraic coefficient-field extension, and plane
embedding examples. Those are not asserted to be actual sliced dense
four-coordinate frames. In particular, generating the whole generic
line does not force either chosen generator to be linear; a chosen
quotient parameter also need not complete the defining polynomial to
a plane automorphism. No global descent or historical novelty claim
is made for these controls.

## Sources

[^1]: [Dense all-degree Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
    the actual localized chart and its whole generic-line conclusion.
    The elementary family and inverse in this note are proved directly;
    the link supplies their interpretation, not an external attribution.

[^2]: [Dense negative-tail relations139](dense-negative-tail-relations-pass139-working.md),
    Sections 2--4, for the signed first relation, second intrinsic
    slice, and formal derivative identities. No new external source
    audit is claimed by this explicit example note.
