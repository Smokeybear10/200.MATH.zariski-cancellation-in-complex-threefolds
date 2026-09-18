# The mixed-quartic line endpoint is itself impossible

Status: new bounded working exclusion. The actual line analysis217
contains a further obstruction before its recognition endpoint: the
second auxiliary derivative of Z belongs to the same coefficient ring
as the first derivative of Y and is also fixed by E. The retained
weighted-leading argument therefore forces the nonconstant ratio rho
to be complex, a contradiction.

Together with the independently proved zero-return and conic exclusions,
this makes the supplied full mixed-quartic sector empty. Recognition219
remains logically true, but is now sharpened to nonrealizability. No
earlier proof, checker, index, or frozen packet is modified here. This
does not exclude arbitrary leading kernels or establish arbitrary frame
entry, and it does not solve unrestricted cancellation.

## 1. Actual hypotheses and the remaining line

Let the four capital letters be actual polynomial coordinates, and assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
       =(as,bs,e_0s^2,h_0s^2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2).
\end{gathered}
\tag{1}
\]
Here s is an independent variable, and the last equality specifies the
entire weighted initial kernel, not merely one relation among leaders.
All four leading coefficients are nonzero by the exact time profile.

The actual selected construction and full-field gates of
[projection217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
give
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\quad Nv=1,\\
t=b/a,\qquad \rho=h_0/a^2,\qquad
q=e_0/a^2=t^2/\rho,\qquad [L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{2}
\]
In particular t and rho are algebraically independent over C. The field
L is contained in Frac(A), so E kills every element of L. Neither L's
rationality nor the original-ring invertibility of a or rho is assumed.

For the new argument first assume that R is nonzero and the projected
plane component is a line. The complete line-direction analysis in
[line217](rank-two-mixed-ratio-line-recognition-pass217-working.md),
Sections1--5, supplies the following exact reduction. The direction
\(y=(t/\rho)\vartheta+\nu\) is impossible by its actual nice-derivation
linear-row argument. The direction \(y=(t/(2\rho))\vartheta+\nu\) is
taken to constant second projection by the actual involution
\((X,Y,Z,W)\mapsto(Y,X,Z,W)\). That involution preserves the full
initial kernel, exact profile, literal selected partial, and field L;
its rebuilt ratios remain algebraically independent.

Thus in either remaining direction, using the rebuilt actual coordinates
and dropping their stars, the retained scalar and potential identities give
\[
\begin{gathered}
\vartheta\in L,\qquad \deg_v y=1,\qquad
w=\lambda y+\omega,\qquad
z=y^2/\rho+\kappa y+\zeta,\\
\lambda\in\mathbb C,\quad \omega,\kappa,\zeta\in L,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\\
Z=z+\sigma X+(t^2/\rho)X^2,\qquad
\sigma=(2t/\rho)y-(t^2/\rho^2)\vartheta+k,\quad k\in L.
\end{gathered}
\tag{3}
\]
The complex nature of lambda is proved there from the full fixed-y
Jacobian: its cubic and quadratic coefficients force lambda_t=omega_t=0,
and its linear and nonzero constant coefficients force lambda_rho=0.
The exact joint constant field is C. Thus the shear below is an actual
complex polynomial operation, not a variable chosen only over L.

## 2. Original auxiliary derivation and primitive division

Put
\[
U=W-\lambda Y,\qquad
\mathcal P=aN-(NX)E,\qquad \tau=aNy.
\tag{4}
\]
The shear has the inverse W=U+lambda Y, fixing X,Y,Z; hence
\(B=\mathbb C[X,U,Y,Z]\). Extend N to A[u] by Nu=0.
The retained selected construction gives Na=Nb=Ne0=Nh0=0.
Consequently P is an original polynomial derivation, fixes X, kills L,
and commutes with E. On \(B_a=A_a[X]\), it fixes X and restricts to
aN on A_a. Since Na=0, this restriction is locally nilpotent. It follows
that P is locally nilpotent on the preserved original ring as well;
no original-ring inverse for a is used.

Direct differentiation of (3) gives
\[
\begin{gathered}
\mathcal PX=\mathcal PU=0,\qquad
\mathcal PY=\tau\ne0,\qquad \mathcal P^2Y=0,\\
\mathcal PZ=\tau\bigl(2y/\rho+\kappa+(2t/\rho)X\bigr),\\
\mathcal P^2Z=2\tau^2/\rho\ne0,\qquad \mathcal P^3Z=0,\qquad
E\tau=0 .
\end{gathered}
\tag{5}
\]
For the last assertion, use commutation and Pb=0. The quantity tau is
the actual polynomial PY, even though its displayed factorization takes
place in the coefficient field. Also P tau=0, since y is affine in v.

Let Delta be the gcd of the nonzero coefficients of P in the actual
coordinates (X,U,Y,Z), and set D=P/Delta. It is a polynomial derivation.
The identity \(P\Delta=\Delta D\Delta\), together with additivity of
degree for a locally nilpotent derivation on a domain, forces PDelta=0:
otherwise the left side has P-degree deg_P(Delta)-1 and the right side
has degree at least deg_P(Delta). Hence DDelta=0. Inductively
\(P^j=\Delta^jD^j\), which proves local nilpotence of D. Its coefficient
gcd is one, so it is irreducible as an LND.

Since Delta divides the nonzero E-invariant polynomial tau, additivity
of E-degree gives EDelta=0 and E(tau/Delta)=0. We have proved
\[
\begin{gathered}
DX=DU=0,\quad [E,D]=0,\qquad
DY=\tau/\Delta\ne0,\quad E(DY)=0,\quad D^2Y=0,\\
D^2Z=\frac{2(DY)^2}{\rho}\ne0,\qquad D^3Z=0 .
\end{gathered}
\tag{6}
\]
All left sides are original polynomials. The displayed equality for
D squared Z follows by dividing the actual identity (5) by Delta squared;
it does not assert that 1/rho was initially an original polynomial.

## 3. The exact two-variable theorem and weighted coefficient ring

Set S=C[X,U], so B=S[Y,Z]. This is a UFD containing Q, and D is a
nonzero irreducible S-linear locally nilpotent derivation with D squared
Y zero. Apply exactly Lemma2.3(i) in
[Dasgupta--Gupta, Nice derivations over principal ideal domains](https://arxiv.org/html/1701.03635v1).
The first of its two polynomial variables is our Y and the second is
our Z. Its conclusions needed here are
\[
DY\in S,\qquad DZ\in S[Y].
\tag{7}
\]
This is an application over the two-dimensional UFD S, not an invocation
of a nice-over-PID result with an incorrect base. The cited statement
explicitly permits a UFD base. The primary restatement was freshly read
at lines98--108 before this argument was saved.

Assign weights one and two to X,U. Their exact E-degrees are one and
two, because U=W-lambda Y and lambda is complex. Their leading
coefficients are a and h0=a squared rho. For a nonzero weighted
homogeneous polynomial of weight n, its leading value is
\[
\sum_j c_j a^{n-2j}h_0^j
  =a^n\sum_j c_j\rho^j\ne0.
\tag{8}
\]
The final polynomial in rho is nonzero because distinct monomials of
weight n have distinct exponents j, and rho is transcendental over C.
Applying this to the highest weighted part of any nonconstant element
of S proves
\[
\boxed{S\cap\ker E=\mathbb C.}
\tag{9}
\]
No independence of the raw speed a from rho is needed. Combining (6),
(7), and (9) gives
\[
DY=d\in\mathbb C^*.
\tag{10}
\]
This is the retained first use of the weighted argument. The second use
below is the new obstruction.

## 4. The second derivative yields a contradiction

On S[Y], the derivation D acts as d times partial_Y. Since DZ lies
in S[Y] and D cubed Z is zero, characteristic zero gives
\[
DZ=f(X,U)Y+g(X,U),\qquad
D^2Z=d f(X,U)\in S.
\tag{11}
\]
The exact formula in (6) also says
\[
D^2Z=2d^2/\rho\ne0.
\tag{12}
\]
Both d and rho are E-fixed, the latter in the fraction field. Therefore
the original polynomial D squared Z belongs to S intersect ker E.
Equation (9), now applied a second time, forces
\[
D^2Z=\beta\in\mathbb C^*,\qquad
\rho=2d^2/\beta\in\mathbb C.
\tag{13}
\]
This contradicts (2). Thus no actual projected line under (1) exists.
The contradiction occurs before the auxiliary-slice coordinate and
three-variable recognition theorems used at the end of line217. Those
later theorems are not required for this strengthened exclusion.

## 5. Consequence for the entire supplied mixed sector

There is no globally sliced actual frame satisfying all of (1).
Indeed [zero-return217](rank-two-mixed-ratio-zero-return-exclusion-pass217-working.md)
excludes R=0. If R is nonzero,
[projection217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
leaves only a projected line or conic. The line is excluded above,
including its actual swapped direction. The two conic branches are
normalized by the actual interchange in quadratic217 and excluded by
the completed218 inputs and
[final conic219](mixed-conic-final-jacobian-exclusion-pass219-working.md).

Consequently the restricted recognition assertion in
[synthesis219](mixed-quartic-initial-kernel-recognition-synthesis-pass219-working.md)
is true with an empty hypothesis class. It did not establish nonvacuity,
and no frozen version is retroactively amended here. The new conclusion
is nonrealizability of precisely this supplied full initial kernel, not
nonexistence of globally sliced actions or of other exact1122 frames.

## 6. Consistent formal leaders are not an actual realization

The proposed leader data a=1, b=lm, e0=l squared, h0=m squared do satisfy
the entire formal mixed initial relation. More precisely, for independent
l,m,s the map
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto (s,lm\,s,l^2s^2,m^2s^2)
\tag{14}
\]
has kernel exactly
\((\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2)\).
Its fraction field contains the three independent elements \(s,lm,m^2\),
so the prime kernel has height one. The displayed mixed polynomial is
irreducible: considered as a polynomial in \(\mathsf Z\), it is primitive
over \(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\) and linear over that
ring's fraction field. It therefore generates that height-one prime.

Thus the formal leader datum itself is not inconsistent. The obstruction
uses the additional actual polynomial derivation, primitive coefficient
ring, and scalar/potential reductions. In particular no C[u]-polynomial
automorphism can realize (14) as the leading data of a translation frame
with the hypotheses (1).

The full saved line217 source was freshly read through EOF, and its
primitive and weighted gates were reconstructed. Root and General
independently checked the new second-derivative contradiction. No new
saved checker was executed, imported, or compiled. No old source,
index, or verification packet was edited. This is a working proof with
AI reconstruction, not formal verification, expert review, historical
novelty clearance, or an unrestricted cancellation theorem.
