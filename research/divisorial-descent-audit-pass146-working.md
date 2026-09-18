# An actual projected curve can split on an unremoved divisor

The cleared primitive generic first-tail equation need not remain a
plane coordinate modulo a height-one prime of the localized intrinsic
coefficient ring. The counterexample below is an actual sliced,
dense three-good frame, obtained by reordering the retained
Chamberland--van den Essen inverse control77.[^1]

Its exceptional projected fiber is reduced and consists of two
disjoint affine lines. The full localized invariant ring nevertheless
is a polynomial ring. The projected bad coordinate supplies the
missing relation and removes the extra component. Thus this is a
counterexample to the proposed residual-coordinate gate, not to
cancellation or to first-tail primitivity.

## 1. The actual frame and both polynomial inverse orders

Let \(h,k,a,u\) be independent over \(\mathbb C\), and put
\[
\begin{gathered}
A=\mathbb C[h,k,a],\qquad B=A[u],\qquad E=\partial_u,\\
X=h+a^2+ku,\qquad Y=a+hu,\qquad
Z=k-2ah-h^2u,\qquad W=u .
\end{gathered}
\tag{1}
\]
These are actual polynomial coordinates, with inverse
\[
u=W,\qquad h=X-Y^2-WZ,\qquad
a=Y-Wh,\qquad k=Z+2hY-Wh^2 .
\tag{2}
\]
For the forward-then-inverse composition,
\[
X-Y^2-WZ
=h+a^2+ku-(a+hu)^2-u(k-2ah-h^2u)=h .
\]
Then the formulas for \(a\) and \(k\) recover them directly.
Conversely, start with independent \(X,Y,Z,W\) and use (2).
The forward expressions recover \(Y\) and \(Z\), while
\[
h+(Y-Wh)^2+W(Z+2hY-Wh^2)=h+Y^2+WZ=X .
\]
This proves both inverse orders everywhere, without localization
or a Jacobian-to-inverse inference.

To identify the retained example exactly, in its notation set
\(h=b-a^2\) and \(k=c+2ah\). Its original three good outputs were
\(a+hu,\ b+ku,\ c-h^2u\). Equation (1) swaps the first two
of these outputs and leaves the bad output \(u\) unchanged.
The family itself is not new.

All four outputs are affine in \(u\), and \(Eu=1\). The selected
first good speed and the two ratios are
\[
\begin{gathered}
s=EX=k,\qquad EY=h,\qquad EZ=-h^2,\\
\tau=h/k,\qquad \rho=-h^2/k,\qquad
h=-\rho/\tau,\qquad k=-\rho/\tau^2 .
\end{gathered}
\tag{3}
\]
Thus the speed field has transcendence degree two, and
\(\tau,\rho\) are algebraically independent. If a nonzero
homogeneous polynomial vanished on \((k,h,-h^2)\), dividing by
the appropriate power of \(k\) would give a polynomial relation
between \(\tau,\rho\). Hence the homogeneous speed cone is dense.
The bad time degree is one.

## 2. The actual selected partial and its intrinsic kernel

Let \(T=\partial_W\) hold the actual \(X,Y,Z\) fixed.
Differentiating (2), and then returning to the source coordinates,
gives
\[
\begin{aligned}
Tu&=1,\\
Th&=-k+2ah+h^2u,\\
Ta&=-h+(k-2ah)u-h^2u^2,\\
Tk&=-h^2-2ak+4a^2h+2ah^2u .
\end{aligned}
\tag{4}
\]
For example \(Th=-Z\), \(Ta=-h-uTh\), and
\(Tk=2aTh-h^2\). These also verify the signs in (4).
The coefficient of \(u^2\) on the invariant ring is therefore
\[
N=[u^2]T|_A=-h^2\partial_a,\qquad
S=\ker_A N=\mathbb C[h,k],\qquad L=\operatorname{Frac}S=\mathbb C(h,k).
\]
The kernel assertion follows by ordinary polynomial differentiation
in the independent variable \(a\). In particular this is the actual
selected intrinsic derivation, not an auxiliary LND chosen to
manufacture a degenerate fiber.

The fixed-\(X\) normalization139 uses \(N'=N/k^2\). If desired,
its normalized generic parameter is
\(v=-k^2a/h^2\), so \(N'v=1\). It differs from \(a\) by an
invertible linear change over \(L\); both give the same generic
line and the same degree of its equation.[^2]

## 3. The exact projected generic equation

Write \(S_k=\mathbb C[h,k,k^{-1}]\). Projection at \(X=0\)
uses \(u_0=-(h+a^2)/k\) and gives
\[
\begin{gathered}
y=a-\frac{h(h+a^2)}{k},\qquad
z=k-2ah+\frac{h^2(h+a^2)}{k},\qquad
w_0=-\frac{h+a^2}{k},\\
z+hy=k-ah,\qquad
G(U,V)=(V+hU)^2-kV+h^3,\qquad G(y,z)=0 .
\end{gathered}
\tag{5}
\]
The last identity follows from \(z+hy=k-ah\). Over \(L\),
the pair \((Q,G)\), where \(Q=V+hU\), has the polynomial inverse
\[
V=\frac{Q^2+h^3-G}{k},\qquad
U=\frac{Q-V}{h}.
\]
Hence \(G\) is a coordinate of \(L[U,V]\). Also
\(a=(k-z-hy)/h\), so \(L[y,z]=L[a]\), and \(G\) is the exact
irreducible generic kernel.

The polynomial \(G\in S_k[U,V]\) is primitive: its coefficient
of \(V^2\) is one. Gauss's lemma in the UFD \(S_k\) therefore gives
\[
\ker\bigl(S_k[U,V]\longrightarrow A_k,\ (U,V)\mapsto(y,z)\bigr)
   =(G),\qquad
R:=S_k[y,z]\simeq S_k[U,V]/(G).
\tag{6}
\]
Indeed the kernel after extending coefficients to \(L\) is
\((G)\), and contraction of that ideal is \((G)\) because
\(G\) is primitive.

This equation can also be matched to the literal signed first tail,
without using a universal primitivity theorem. In the ratio variables
of (3), the degree-one peeling coefficients are
\[
\begin{gathered}
f_1=-\frac{\tau^2}{\rho}=\frac1k,\qquad
f_0=\frac1\rho=-\frac{k}{h^2},\qquad
f_{-1}=\frac1\tau=\frac{k}{h},\\
\Phi(U,V)
=\frac{(\rho U-\tau V)^2}{\rho^3}+\frac{V}{\rho^2}-\frac1\tau
=-\frac{k}{h^4}G(U,V),\\
\Psi(U,V)=\frac{k^2(V+hU)}{h^3}-\frac{k^2VG(U,V)}{h^6},\qquad
\Psi(y,z)=-\frac{k^2a}{h^2}+\frac{k^3}{h^3}.
\end{gathered}
\tag{7}
\]
For a direct check, \(f_1\) is the coefficient of \(X\) in
\(W=(X-h-a^2)/k\). Its first Taylor term is
\(2y/h+z/h^2\); subtracting this from \(w_0\) gives \(f_0\).
The signed next coefficient is
\[
-H_2(f_1;y,z)-H_1(f_0;y,z)
=\frac{(\rho y-\tau z)^2}{\rho^3}+\frac{z}{\rho^2}
=\frac{k}{h},
\]
where \(H_j\) is the homogeneous order-\(j\) coefficient Taylor
polynomial139. Thus \(f_{-1}\) and \(\Phi\) in (7) have the
specified signs. For the second tail, direct differentiation gives
\[
-H_3(f_1;U,V)-H_2(f_0;U,V)-H_1(f_{-1};U,V)
=\frac{U}{\tau^2}
 -\frac{V(\rho U-\tau V)^2}{\rho^4}-\frac{V^2}{\rho^3},
\]
which is the displayed \(\Psi\). Its evaluated value is the
normalized intrinsic parameter \(v\) plus the constant \(k^3/h^3\).
Clearing denominators and removing content from
\(\Phi\) over \(S_k\) gives \(G\), up to a unit of \(S_k\).
The residual failure below is therefore independent of this
primitive normalization.

## 4. A divisor that the selected-speed localization does not remove

The ideal \(\mathfrak p=(h)\) is a height-one prime of \(S_k\).
The selected speed is \(k\), not \(h\), so \(\mathfrak p\)
survives this localization. Its residue field is
\(\kappa(\mathfrak p)=\mathbb C(k)\). Equation (5) reduces to
\[
\overline G=V(V-k),\qquad
\kappa(\mathfrak p)[U,V]/(\overline G)
 \simeq \kappa(\mathfrak p)[U]\times\kappa(\mathfrak p)[U].
\tag{8}
\]
The factors are distinct and comaximal because \(k\) is nonzero
in the residue field. Thus the fiber is reduced and disconnected.
It cannot be the quotient by a plane coordinate: that quotient
would be the integral domain \(\kappa(\mathfrak p)[T]\).
No multiplication by a unit in \(S_k\) changes this conclusion.

This disproves the proposed implication for the retained actual
dense three-good hypotheses, even when all four original coordinates
are affine in time. The counterexample does not depend on a
nonreduced fiber or on choosing a divisor already inverted by \(s\).

## 5. The projected bad coordinate restores the actual polynomial ring

The full projected overring behaves differently:
\[
\begin{gathered}
a=y-hw_0,\qquad
A_k=S_k[y,z,w_0]=S_k[a],\\
h+y^2+w_0z=0,\qquad
k-z-2hy+w_0h^2=0 .
\end{gathered}
\tag{9}
\]
Thus \(w_0\) recovers the actual invariant parameter without
inverting \(h\). Its formula in (5) has only the allowed
denominator \(k\).
Equivalently, inside the common fraction field,
\[
A_k=R[a]
 =R\!\left[\frac{k-z-hy}{h}\right].
\]
The numerator is divisible by \(h\) in the larger ring, not a
permission to invert \(h\) in \(S_k\).

The two relations in (9) give the entire three-generator presentation
over \(S_k\). To see this directly, use independent \(U,V,C\)
and put \(a_*=U-hC\) in their quotient. Those relations imply
\[
h+a_*^2+kC=0 .
\]
Since \(k\) is a unit, they recover successively
\(C=-(h+a_*^2)/k\), \(U=a_*+hC\), and
\(V=k-2hU+h^2C\). These formulas are inverse to substitution
from \(S_k[a]\).

At \(\mathfrak p\), the second relation forces \(V=k\), and
the first then gives \(C=-U^2/k\). Consequently the full
invariant fiber is just \(\kappa(\mathfrak p)[U]\).
The map from the projected-good fiber in (8) selects its
\(V=k\) component. The other component belongs to the smaller
projected subring and does not survive in the actual invariant ring.

There is also an exact open-chart description. Put \(q=z+hy\in R\).
The equation \(G=0\) gives
\[
q(k-q)=h(ky+h^2),\qquad
a=\frac{k-q}{h}=\frac{ky+h^2}{q}.
\]
Thus \(R_h=(A_k)_h\) and \(R_q=(A_k)_q\), where these subscripts
in this paragraph denote localization at the displayed elements.
In \(A_k\), \(q=k-ha\), so the ideal \((h,q)\) is the unit ideal.
These two localized identifications prove
\(\operatorname{Spec}A_k\simeq D_R(h)\cup D_R(q)\).
The excluded locus is \(h=q=0\), exactly the \(V=0\) component
of the exceptional projected fiber. This describes this explicit
overring only, not a general open-immersion theorem for such charts.

The removed component also has an exact Laurent specialization. Take
\(\xi\) independent over \(\mathbb C(k)\), and set \(a=k/h-\xi\)
in \(\mathbb C(k,\xi)((h))\). The formulas in (5) become
\[
y=\xi-\frac{h\xi^2}{k}-\frac{h^2}{k},\qquad
z=\frac{h^2\xi^2}{k}+\frac{h^3}{k},\qquad
w_0=-\frac{k}{h^2}+\frac{2\xi}{h}-\frac{\xi^2}{k}-\frac hk .
\]
Thus \(y,z\) are integral and reduce to \((\xi,0)\), the generic
point of the removed projected line, while \(w_0\) has a pole of
order two. This realizes the missing branch by an escaping invariant
parameter, not by an additional fiber of the actual polynomial line.

## 6. Consequence for the next descent step

First-tail primitivity145 correctly concerns the generic equation
over \(L\); it does not imply that its primitive model over \(S_k\)
is a coordinate on every divisorial fiber.[^3] Requiring this would
exclude the actual, already polynomial example (1).

A descent argument must therefore allow the passage from the
projected good subring \(R\) to the actual overring
\(S_k[y,z,w_0]\), including the effect of its additional relations
on special fibers. This note does not assert that every such
overring admits the explicit polynomial recovery in (9).
It does not solve general descent, arbitrary coordinate entry,
or cancellation.

## Sources

1. [An aligned projective parameter cannot give the proposed nonlinear cone77](aligned-projective-line-family-obstruction-pass77.md),
   Section 3, especially equation (6). The retained actual
   Chamberland--van den Essen family and its inverse. The
   coordinate reordering and divisorial calculation are explicit
   above; the underlying family is not claimed new.
2. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--2, and [the signed negative-tail identities139](dense-negative-tail-relations-pass139-working.md),
   Sections 1--2. The selected intrinsic derivation, fixed-\(X\)
   localization and coefficient conventions used here.
3. [Common Taylor integrality forces first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Sections 7--9. Its generic conclusion is consistent with (7)
   and does not assert residual-coordinate descent.

No new external classification theorem is used, and no historical
novelty, human review or proof-assistant verification is claimed.

[^1]: Source 1. This is an adversarial use of an existing actual
    inverse control, not a formally prescribed speed tuple.
[^2]: Source 2. The intrinsic kernel is calculated directly in (4).
[^3]: Source 3. The distinction is between the generic curve and
    its model in the projected good subring.
