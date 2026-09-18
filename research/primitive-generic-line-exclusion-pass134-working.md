# The primitive generic component cannot be a line

In the actual primitive dense quadratic class, the generic component
selected by the intrinsic action is an irreducible cubic graph, not a
line. A hypothetical line would produce a constant ambient derivation
commuting with the original action, contradicting the retained
commuting-direction theorem.

The descent from localized coordinates to original polynomial
coefficients is proved through fraction fields. No global equality
between the two intermediate coordinate rings is assumed. This is a
working generic-component reduction, not passage of either correction
gate or a cancellation theorem.

## 1. The actual localized cubic

Use the pure-cube normal form supplied by invariant-localization
rigidity.[^1] The actual hypotheses are
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u_0],\qquad E=\partial_{u_0},\\
E^2X=E^2Y=E^2Z=0,\qquad
s=EX\ne0,\quad t=EY,\quad r=EZ,\\
E^3W=0,\qquad sE^2W=2\gamma t^3,\quad\gamma\in\mathbb C^*,
\qquad \tau=t/s,\quad\rho=r/s,
\end{gathered}
\tag{1}
\]
with rank-two speeds and dense homogeneous speed cone. In particular
\(\tau,\rho\) are algebraically independent. The primitive leading
polynomial is \(XW-\gamma Y^3\).

The actual localization at \(s\), together with \(D=E/s\), gives
\(DX=1\) and the presentation
\[
\begin{gathered}
A_s=\mathbb C[y,z,w]_{s_0},\quad
s=s_0(y,z,w),\quad B_s=A_s[X],\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=w+dX+\gamma\tau^3X^2,\\
A_L=L[y,z]=L[v],\qquad N'v=1,\qquad
[L:\mathbb C(\tau,\rho)]<\infty,\\
d=3\gamma\tau^2y+k,\qquad
w=3\gamma\tau y^2+k_\tau y+k_\rho z+\ell,\\
G(U,V)=\gamma U^3+\tfrac12k_{\tau\tau}U^2+k_{\tau\rho}UV
       +\tfrac12k_{\rho\rho}V^2+\ell_\tau U+\ell_\rho V-m,
\qquad G(y,z)=0.
\end{gathered}
\tag{2}
\]
Here \(N'\) is the nonzero leading LND on \(A_s\), \(L\) is its
invariant fraction field, and \(k,\ell,m\in L\). The derivations
\(\partial_\tau,\partial_\rho\) extend uniquely through the finite
separable extension and commute. The entire generic ring is \(L[v]\):
the element \(s_0=s\) already belongs to \(L^*\), so its inversion
does not puncture the generic line. All assertions in (2), including
the localized Jacobian, are proved in the localization note.[^1]

Let \(P\) generate the kernel of \(L[U,V]\to L[v]\), and write
\(G=PR\). The exact generic Jacobian makes \(R(y,z)\in L^*\).
The degree-two case is excluded, and the only alternatives are
\(\deg P=1\) and \(\deg P=3\).[^2]

## 2. Consequences of a line component

Suppose \(\deg P=1\). The unit complementary factor gives
\(G=cP+P^2Q\), with \(c\in L^*\). Its leading cubic is therefore
divisible by the square of the leading line of \(P\).
Since that cubic is \(\gamma U^3\), normalize \(P=U-f\) for
\(f\in L\). Thus \(y=f\), and \(L[y,z]=L[z]=L[v]\).
Comparing \(G(f,z)=0\) and the unit
\(G_U(f,z)=R(f,z)\) gives
\[
k_{\rho\rho}=0,\qquad k_{\tau\rho}=0,
\qquad\ell_\rho=0,
\qquad k_\rho=\kappa\in\mathbb C,
\qquad h:=k-\kappa\rho\in L.
\tag{3}
\]
For the last constant assertion, \(k_\rho\) is killed by both
extended coordinate derivations. Differentiating its monic minimal
polynomial over \(\mathbb C(\tau,\rho)\) gives lower-degree
annihilating polynomials, so all coefficients of that minimal
polynomial are killed by both derivations and belong to \(\mathbb C\).
As \(\mathbb C\) is algebraically closed, \(k_\rho\in\mathbb C\).
This does not assume that \(L\) is a rational function field.

Set \(w'=w-\kappa z\). Equation (2) shows that \(w'\in L\),
since \(y=f\in L\). Both \(y\) and \(w'\) also belong to \(A_s\).
They are independent coordinates of its displayed localized polynomial
presentation. Rename the denominator after this constant linear
change as \(s_0(y,z,w')\).

The derivation \(N'\) kills \(y,w'\), and \(N'z\ne0\): otherwise
it would kill \(L[y,z]=L[v]\). On
\(\operatorname{Frac}A=\mathbb C(y,z,w')\) it therefore equals
\((N'z)\partial_z\). Since \(N's_0=N's=0\),
\[
s_0\in\mathbb C[y,w'],\qquad
R_1:=\mathbb C[y,w']_{s_0},\qquad A_s=R_1[z],
\qquad \ker_{A_s}N'=R_1.
\tag{4}
\]
The polynomial derivative in \(z\) is zero only for coefficients
independent of \(z\), in characteristic zero. This proves the
denominator assertion before using it. In particular \(s,\tau\in R_1\).
Also \(h=d-3\gamma\tau^2y-\kappa\rho\) belongs to \(A_s\cap L\),
so \(h\in R_1\).

## 3. The localized-to-global bridge

Use the actual original linear coordinate \(U_0=W-\kappa Z\).
Equations (2)--(4) give
\[
\begin{gathered}
X=X,\qquad Y=y+\tau X,\\
U_0=w'+(3\gamma\tau^2y+h)X+\gamma\tau^3X^2,\\
EX=s,\qquad EY=s\tau,\qquad
EU_0=s(3\gamma\tau^2y+h+2\gamma\tau^3X)
\quad\text{in }R_1[X].
\end{gathered}
\tag{5}
\]
Put \(K=\mathbb C(X,Y,U_0)\) and \(K_0=\operatorname{Frac}(R_1[X])\).
The actual coordinates \((X,Y,U_0,Z)\) are algebraically independent,
so \(K\subset K_0\) is an algebraic extension of fields of
transcendence degree three. Moreover
\[
K_0\subset\operatorname{Frac}B=K(Z)
\quad\Longrightarrow\quad K_0=K,
\qquad K\cap B=\mathbb C[X,Y,U_0].
\tag{6}
\]
The implication uses relative algebraic closedness of a field in its
purely transcendental one-variable extension. The final intersection
is the polynomial-ring intersection in the actual independent
coordinates, not a contraction from an assumed finite ring extension.
Thus the three actual polynomial values \(EX,EY,EU_0\) belong to
\(R=\mathbb C[X,Y,U_0]\), and \(E\) restricts to an LND \(E_R\)
on that ring.

## 4. The original fourth coefficient also descends

Write \(r=EZ\in R[Z]\). Since \(E^2Z=0\),
\[
0=E(r)=E_R(r)+r\partial_Zr.
\tag{7}
\]
If \(r\) has \(Z\)-degree \(j\ge2\), with leading coefficient
\(r_j\ne0\), the second term has the nonzero top coefficient
\(j r_j^2\) at degree \(2j-1>j\), whereas the first has degree
at most \(j\). This is impossible. If \(j=1\), its leading
coefficient satisfies \(E_R(r_1)=-r_1^2\). LND self-divisibility
forces \(E_R(r_1)=0\), and then \(r_1=0\), again a contradiction.
Consequently \(r\in R\).

There is also a direct check: \(\rho=r/s\in A_s\) is killed by
\(N'\), hence lies in \(R_1\) by (4); (6) then contracts the
actual polynomial \(r=s\rho\) to \(R\). Either ending avoids
assuming that \(R_1[X]=R\).

It follows that the constant original-coordinate derivation
\(D_0=\partial_Z+\kappa\partial_W\), equivalently the partial
in \(Z\) holding \(X,Y,U_0\) fixed, commutes with \(E\).
The retained commuting-direction theorem gives a quadratic good
correction of \(W\) that is invariant.[^3] In particular
\(E^2W\) belongs to the constant quadratic span of the good speeds.
This contradicts primitivity: homogeneous density would turn
\(sE^2W=2\gamma t^3\) into divisibility of \(\gamma Y^3\) by \(X\).
Thus the line component cannot occur.

## 5. The surviving component is an irreducible cubic graph

Only \(\deg P=3\) remains. As \(G\) also has degree three, its
complementary factor is a nonzero constant, so \(G\) itself is
irreducible over \(L\). Its closed embedded affine line has leading
form \(\gamma U^3\). The elementary cubic-line argument implies
that its \(U\) coordinate is linear in a parameter, and its \(V\)
coordinate is cubic in that parameter.[^2] Indeed a polynomial
parametrization of this cubic has maximal degree three; the pure
cube at infinity forces the first coordinate to have smaller degree.
The degree pair \((2,3)\) is not an embedding: after affine changes
it is \((v^2,av^3+bv)\), which either identifies a nonzero opposite
pair or has both derivatives zero at the origin. A constant first
coordinate would instead define a line. Thus the first degree is one.

Comparing this graph with (2) yields
\[
G(U,V)=\gamma U^3+\tfrac12 k_{\tau\tau}U^2
       +\ell_\tau U+\ell_\rho V-m,
\qquad \ell_\rho\ne0,
\qquad k_{\rho\rho}=k_{\tau\rho}=0,
\qquad k_\rho\in\mathbb C.
\tag{8}
\]
The last assertion uses the same finite-field constant argument as
in (3). These are identities over the generic field \(L\).
They do not globalize its coefficients, make \(s\) a unit in \(A\),
or construct an invariant lift of original weight three. The two
correction conditions and unrestricted entry remain separate.

## Sources

1. [Pure-cube leading rigidity after invariant localization](primitive-binary-cubic-localization-rigidity-pass134-working.md),
   Sections 2--5. Actual localized coordinates, whole generic affine
   line, normalized volume, and coefficient equations.
2. [A constant leading speed forces a pure-cube binary residue](constant-speed-binary-cubic-rigidity-pass134-working.md),
   Sections 3--5. The complementary-factor unit and the elementary
   degree-three embedded-line argument, used over the same generic field.
3. [A commuting constant direction forces a quadratic invariant correction](three-good-commuting-direction-quadratic-invariant-pass133.md),
   Sections 1--4. The actual dense three-good conclusion with an
   arbitrary nonzero constant ambient commuting direction. Its retained
   source-dependent classification is used with those exact hypotheses.

[^1]: [Invariant-localization rigidity134](primitive-binary-cubic-localization-rigidity-pass134-working.md), Sections 2--5.
[^2]: [Generic cubic component proof134](constant-speed-binary-cubic-rigidity-pass134-working.md), Sections 3--5.
[^3]: [Commuting-direction theorem133](three-good-commuting-direction-quadratic-invariant-pass133.md), Sections 1--4.
