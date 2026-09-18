# Unbounded coefficient-field degree in actual dense sliced frames

The finite coefficient-field extension in the dense chart need not be
trivial, even for an actual polynomial frame with a global slice.
Its degree is not bounded by the last coordinate's time degree:
the family below has that time degree equal to one and extension
degree equal to any prescribed integer \(n\ge2\).

This is a boundary for a proposed simplification of the generic chart,
not a counterexample to cancellation. Every member is an explicitly
invertible presentation of a translation. The first tail is primitive
in this family, so it does not answer whether a genuine frame can have
an extra factor in that tail.

## 1. Actual coordinates and a polynomial inverse

Fix \(n\ge2\). In \(B=\mathbb C[u,a,b,v]\) set \(E=\partial_u\) and
\[
\begin{gathered}
X=v+a^nu,\qquad Y=a+bu,\qquad Z=b+u,\qquad W=u,\\
u=W,\qquad b=Z-W,\qquad a=Y-(Z-W)W,\qquad
v=X-\bigl(Y-(Z-W)W\bigr)^nW .
\end{gathered}
\tag{1}
\]
The second line is a polynomial inverse. Substitution of the first
line recovers \(u,b,a,v\) in that order. Conversely the definitions
recover \(W,Z,Y,X\), respectively. Thus both compositions are
identities on the whole affine space, including \(a=0\).
The Jacobian of the frame in the order \((u,a,b,v)\) is \(-1\).

The actual sliced data are
\[
\begin{gathered}
(EX,EY,EZ)=(a^n,b,1),\qquad E^2X=E^2Y=E^2Z=0,\\
EW=1,\qquad m=\deg_E W=1,\qquad
A=\ker E=\mathbb C[a,b,v].
\end{gathered}
\tag{2}
\]
The speed rank is two. There is no nonzero homogeneous relation
on the speed row: dehomogenizing at the last entry equal to one
gives a polynomial in the independent functions \(a^n,b\).
Equivalently the radial map
\((t,a,b)\mapsto(ta^n,tb,t)\) has determinant \(nt^2a^{n-1}\ne0\).
The good-speed ideal is the unit ideal. In fact \(Z\) itself is
a good coordinate with speed one. Recognition is already immediate;
the point is the effect of selecting \(X\) for the chart.

## 2. The selected leading derivation and its exact invariant field

Differentiate the actual inverse (1) with respect to \(W\), holding
\(X,Y,Z\) fixed. This gives
\[
\begin{gathered}
T=\partial_W
=\partial_u+(u-b)\partial_a-\partial_b+
 \bigl(-a^n+na^{n-1}bu-na^{n-1}u^2\bigr)\partial_v,\\
N=[u^2]T|_A=-na^{n-1}\partial_v,\qquad
S_0=\ker_A N=\mathbb C[a,b],\qquad L=\mathbb C(a,b).
\end{gathered}
\tag{3}
\]
The kernel equality follows coefficientwise in \(v\), since the
nonzero factor \(-na^{n-1}\) is not a zero divisor. This is the
selected leading derivation of the actual coordinate partial, not
an auxiliary action chosen to resemble it. Its primitive factor
\(\partial_v\) has a slice; no intrinsic degeneration obstruction
is being claimed.

The ratios for the selected good speed \(s=EX=a^n\) are
\[
\begin{gathered}
\tau=b/a^n,\qquad \rho=1/a^n,\qquad
K:=\mathbb C(\tau,\rho)=\mathbb C(a^n,b),\\
[L:K]=n,\qquad L=K(a),\qquad a^n=\rho^{-1}.
\end{gathered}
\tag{4}
\]
To prove the exact degree, put \(c=a^n\). The functions \(c,b\)
are algebraically independent. The polynomial \(T_0^n-c\) is
Eisenstein at \(c\) in the UFD \(\mathbb C(b)[c][T_0]\);
Gauss's lemma makes it irreducible over \(\mathbb C(b,c)\).
This proves (4) for every \(n\), not just tested small values.
The automorphisms \(a\mapsto\zeta a,\ b\mapsto b\), for
\(\zeta^n=1\), display the nontrivial conjugates.

Consequently the actual polynomial-inverse hypothesis does not
permit replacing \(L\) by \(K\). No upper bound depending only
on \(m\) can control \([L:K]\), since \(m=1\) throughout this
family. This concerns the specified chart; it is not a claim that
every possible choice of good coordinate has the same extension.

## 3. Normalized intrinsic parameter and the whole generic line

Inverting \(s\) is equivalent to inverting \(a\). The normalization
used in the dense chart139 is[^1]
\[
\begin{gathered}
N'=N/s^2=-na^{-n-1}\partial_v,\qquad
r=-a^{n+1}v/n,\qquad N'r=1,\\
y=a-bv/a^n,\qquad z=b-v/a^n,\qquad
Y=y+\tau X,\quad Z=z+\rho X,\quad W=\rho X+z-b,\\
L[y,z]=L[v]=L[r],\qquad
g(U,V)=U-bV-a+b^2,\qquad g(y,z)=0 .
\end{gathered}
\tag{5}
\]
Here \(U,V\) are independent plane variables. The formula
\(v=a^n(b-z)\) gives the whole-line equality. The kernel of
evaluation \(L[U,V]\to L[r]\) is exactly \((g)\);
indeed \((g,V)\) is a plane coordinate pair. The generic degrees
of \(y,z\) and \(g\) are one.

The coefficient partials on \(L\) are
\(\partial_\tau=a^n\partial_b\) and
\(\partial_\rho=-a^{n+1}\partial_a/n-ba^n\partial_b\).
They are the unique extensions of the coordinate partials on \(K\),
and commute. They extend to \(L(r)\) by fixing \(r\), not by fixing
the adapted variable \(v\).
For a direct determinant check, the Jacobian of
\((X,\tau,\rho,r)\) in \((u,a,b,v)\) is \(-1\), the same as
the actual frame in (1). Hence the relative determinant of
\((Y,Z,W)\) in \((\tau,\rho,r)\), with \(X\) fixed, is exactly one.

## 4. Both tails with their coefficient-field dependence

Write \(H_j\) for the homogeneous Taylor pieces in139.[^2]
The polynomial \(W\) in (5) has exact peeling coefficients
\(f_1=\rho,\ f_0=-b=-\tau/\rho\). Indeed
\(H_1(f_1;y,z)=z\). Their first tail is
\[
\begin{gathered}
R_1(U,V)=-H_2(\rho;U,V)-H_1(-b;U,V)
       =a^n(U-bV),\\
f_{-1}=R_1(y,z)=a^n(a-b^2),\qquad
\Phi=R_1-f_{-1}=a^n g .
\end{gathered}
\tag{6}
\]
Although \(f_0,f_1\in K\), the constant \(f_{-1}\) does not belong
to \(K\) when \(n\ge2\): its term \(a^{n+1}=ca\) has nontrivial
conjugates, whereas \(a^nb^2=cb^2\) is in \(K\). Thus the first
evaluated tail already detects the larger actual coefficient field.

For the second tail, direct coefficient differentiation gives
\[
\begin{gathered}
H_2(-b;U,V)=a^{2n}(UV-bV^2),\\
H_1(f_{-1};U,V)
=a^{2n}\left(-2bU+
 \left(3b^2-\frac{n+1}{n}a\right)V\right),\\
\Psi=-H_3(f_1)-H_2(f_0)-H_1(f_{-1})\\
\hphantom{\Psi}
=a^{2n}\left(-UV+bV^2+2bU+
 \left(\frac{n+1}{n}a-3b^2\right)V\right),\\
\Psi(y,z)=r+a^{2n}\left(\left(2+\frac1n\right)ab-2b^3\right),
\qquad \partial_r\Psi(y,z)=1 .
\end{gathered}
\tag{7}
\]
The degrees in (6)--(7) are below the respective universal bounds
two and three when \(m=1\). The first tail is a unit multiple of
the primitive equation despite the nontrivial field extension.
So a proper coefficient extension alone does not force extra factors.

As another direct boundary for the chosen second tail,
\[
\det\frac{\partial(g,\Psi)}{\partial(U,V)}
=a^{2n}\left(\frac an-g\right),
\tag{8}
\]
which is nonconstant. The pair \((g,\Psi)\) is not a plane
automorphism, although \(\Psi\) supplies the correct parameter
modulo \(g\). This agrees with the stronger sharp-degree family
recorded separately.[^3]

## Consequence for the descent investigation

An argument using only the field \(K=\mathbb C(\tau,\rho)\), or a
bound on its finite extension determined by the time degree, would
miss actual sliced polynomial frames. The finite separable extension
must remain explicit unless an additional, proved coordinate change
removes it.

This elementary family does not settle global descent. It rules out
one simplifying assumption while preserving every actual inverse and
slice premise. Its first tail remains primitive, so the actual-frame
primitivity question survives both this family and the sharp example.
No historical novelty, human expert review or proof-assistant
verification is claimed.

The standalone checker140 includes small exact members of this family.
Those tests check formulas and inverse compositions, not the universal
extension-degree assertion; the latter is the Eisenstein proof in (4).

## Sources

1. [Actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3. The selected \(N\), exact invariant field, fixed-good
   localization and normalized intrinsic parameter.
2. [Negative-tail lemma139](dense-negative-tail-relations-pass139-working.md),
   Sections 2--4. Signed definitions of \(R_1,\Phi,\Psi\).
3. [Actual sharp dense-tail family140](sharp-dense-tail-family-pass140-working.md),
   Sections 4--5. A separate actual failure of the particular
   tail-complement implication.

The construction and formulas (1)--(8) are proved directly here.
The links specify the working chart being tested, not an external
attribution or novelty determination for this elementary family.

[^1]: Source 1, especially its normalization \(N'=N/s^2\).
[^2]: Source 2, the first two negative coefficients.
[^3]: Source 3, the nonconstant tail-pair Jacobian.
