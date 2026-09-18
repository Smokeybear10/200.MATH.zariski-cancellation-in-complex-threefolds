# Projected-ring equality detects constant speed, but polynomial data do not supply an actual frame

For an actual sliced coordinate frame, the projected polynomial source
ring equals the invariant ring exactly when the selected good speed is
a nonzero complex constant. A rescaled formal base-flip family shows
why the actual-coordinate premise matters: its source action has a
global slice, its projected ring is its entire invariant ring, and its
pulled-back last-coordinate partial is polynomial, but the displayed
tuple is not a coordinate frame. That partial is not locally nilpotent
on the source polynomial ring.

The same boundary admits a bad-slot quadratic shear, so its three
good functions and exactly quadratic bad function meet the time-degree
profile. This is still a nonactual formal control, not a cancellation
counterexample or a proof that an actual first tail has an extra factor.

## 1. An exact criterion for the actual projected ring

Assume an actual polynomial coordinate ring and a sliced LND
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
s=EX\ne0,\qquad Es=0,\qquad D=E/s\text{ on }B_s,\\
\pi_X(f)=\sum_{j\ge0}\frac{(-X)^j}{j!}D^j(f),\qquad
(y,z,w_0)=\pi_X(Y,Z,W),\qquad R_0=\mathbb C[y,z,w_0].
\end{gathered}
\tag{1}
\]
There is no density or last-coordinate degree assumption in this
criterion. Each sum is finite, and this is multiplicative flow
evaluation at parameter \(-X\), not the exponential of a
variable-coefficient derivation. The actual inverse and projection give
\(A\subset R_0\subset A_s\), as proved in143.[^1]

Put \(u_0=\pi_X(u)\). Since \(D u=1/s\) and \(D^2u=0\),
\[
\boxed{\quad
u_0=u-X/s\in R_0,\qquad
R_0=A\ \Longleftrightarrow\ u_0\in A
\ \Longleftrightarrow\ s\in\mathbb C^* .
\quad}
\tag{2}
\]
The membership in \(R_0\) uses the actual polynomial expression
\(u=P_u(X,Y,Z,W)\): its projection is
\(P_u(0,y,z,w_0)\).
If \(u_0\in A\), the identity \(X=s(u-u_0)\) is a factorization
inside \(B\). An actual coordinate \(X\) is irreducible in this
polynomial ring. The factor \(u-u_0\) cannot be a unit, since its
\(E\)-derivative is one, whereas every unit of \(B\) lies in
\(\mathbb C^*\). Thus \(s\) is a unit, hence a nonzero complex
constant. Conversely, if \(s\in\mathbb C^*\), the projection is
defined on all of \(B\), fixes \(A\), and has images
\(0,y,z,w_0\) on the four polynomial generators. Its image is both
\(A\) and \(R_0\). This proves every implication in (2).

In particular, when \(s\) is nonconstant, \(u_0\) is an explicit
element of \(R_0\setminus A\). Polynomial representatives for all
actual invariants do not give the reverse ring inclusion.

## 2. A polynomial rescaling of the formal base-flip family

Now define a different source ring, without assuming that the displayed
four functions are its coordinates:
\[
\begin{gathered}
A_* =\mathbb C[a,\beta,q],\qquad B_*=A_*[u],\qquad E=\partial_u,\\
X=a^2u,\qquad Y=q+a^3u,\qquad
Z=a-a\beta u/2,\qquad W=\beta-\beta^2u/4,\\
s=EX=a^2,\qquad t=EY=a^3,\qquad b=EZ=-a\beta/2,\\
\tau=t/s=a,\qquad \rho=b/s=-\beta/(2a),\qquad
L=K=\mathbb C(a,\rho)=\mathbb C(a,\beta).
\end{gathered}
\tag{3}
\]
This is a polynomial source action with global slice \(u\).
The three goods are affine in \(u\), and their speed field has
transcendence degree two. Their homogeneous cone is dense: a homogeneous
relation, divided by the appropriate power of \(s\), would give a
polynomial relation between the independent ratios \(\tau,\rho\).

In \(B_{*,a}\), flow projection at \(X=0\) is simply evaluation at
\(u=0\). It gives \((y,z,w_0)=(q,a,\beta)\), so the projected ring
really equals \(A_*\). This does not contradict (2), because
\(X,Y,Z,W\) are not an actual coordinate frame for \(B_*\).
Indeed the following exact data make the failure explicit:
\[
\begin{gathered}
T=\frac{au}{2}\partial_a+\left(1+\frac{\beta u}{2}\right)\partial_\beta
   -\frac{a^3u^2}{2}\partial_q-u^2\partial_u,\\
T(X,Y,Z,W)=(0,0,0,1),\qquad
T^n(u)=(-1)^n n!u^{n+1}\quad(n\ge1),\\
\det\frac{\partial(X,Y,Z,W)}{\partial(u,a,\beta,q)}=a^2,
\qquad Z^2+XW=a^2 .
\end{gathered}
\tag{4}
\]
The first identity is verified by applying the displayed polynomial
derivation to each function. Its iterates on \(u\) follow by induction
from \(Tu=-u^2\), so \(T\) is not locally nilpotent on \(B_*\).
The nonzero Jacobian shows that the four displayed functions are
algebraically independent. Therefore their subring
\(B_0=\mathbb C[X,Y,Z,W]\subset B_*\) is a polynomial ring, and
\(T|_{B_0}\) really is its locally nilpotent partial \(\partial_W\).
Local nilpotence on this target subring is strictly weaker than local
nilpotence on the full source ring. Also \(X=a^2u\) is reducible
in \(B_*\), and the Jacobian is a nonunit; each independently
precludes an actual coordinate frame.

There is not even a rational inverse over the target field.
Let \(M=\operatorname{Frac}B_0\) and
\(H=\operatorname{Frac}B_*\). The identity in (4) and the formulas
\(u=X/a^2\), \(q=Y-aX\),
\(\beta=2a(a-Z)/X\) give \(H=M(a)\).
The polynomial \(Z^2+XW\) in the independent target variables is
irreducible: viewed as linear in \(W\), its coefficients \(X,Z^2\)
are coprime, so Gauss's lemma applies. Its prime valuation is one,
so it is not a square in \(M\), and \([H:M]=2\).

## 3. The intrinsic top and full formal normalization survive

The formal selected partial has the same bounded source-degree shape
as the intrinsic construction, even though the full source LND premise
for \(T\) fails:
\[
\begin{gathered}
N=[u^2]T|_{A_*}=-\frac{a^3}{2}\partial_q
 \in\operatorname{LND}(A_*)\setminus\{0\},\qquad
N(s)=N(t)=N(b)=0,\\
\ker_{A_*}N=\mathbb C[a,\beta],\qquad
N'=N/s^2=-\frac{1}{2a}\partial_q,\qquad v=-2aq,\quad N'v=1,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=-2\tau\rho-\rho^2X,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}=1 .
\end{gathered}
\tag{5}
\]
Here \(y=-v/(2\tau)\), \(z=\tau\). The determinant fixes
\(X\) and uses coefficient partials fixing \(v\). It is exactly
the normalized formal family143, with a polynomial source
reparameterization.[^2] The kernel assertion for \(N\) follows
by ordinary differentiation in the independent variable \(q\).

For the signed Taylor data139, direct differentiation gives
\[
\begin{gathered}
f_0=0,\quad f_1=-\rho^2,\quad f_{-1}=\tau^2,\\
\Omega(U,V)=-2\rho V,\qquad
\Phi(U,V)=V^2-\tau^2,\qquad \Psi(U,V)=-2\tau U,\\
g=V-\tau,\quad h=V+\tau,\quad
\Psi(y,z)=v,\qquad L[U,V]/(g)\simeq L[U,V]/(h)\simeq L[U],\\
p_s=z^2,\quad p_t=z^3,\quad p_b=-z w_0/2,\quad p_e=z,\qquad e=a,\\
\left.(\widehat p_s-s,\widehat p_t-t,
              \widehat p_b-b,\widehat p_e-e)\right|_{V=-a}
       =(0,-2a^3,0,-2a),\\
\left.(\widehat p_t-\tau\widehat p_s,
        \widehat p_b-\rho\widehat p_s)\right|_{V=-a}
       =(-2a^3,0).
\end{gathered}
\tag{6}
\]
The hats mean substitution \((z,w_0)=(V,\Omega(U,V))\).
Both components are active, and both have algebraic constant field
exactly \(L\). The source substitution on \(h\) sends
\((a,\beta)\) to \((-a,-\beta)\), so it flips the first speed
ratio and fixes the second. The selected polynomial coefficient
representatives exist without any denominator in the projected source
ring; they do not force the two base-return equations on an extra
formal component. The actual coordinate inverse remains absent.

## 4. The same boundary has an exactly quadratic bad slot

Replace only the formal target bad function by
\[
\begin{gathered}
W_2=W+Y^2,\qquad E^2W_2=2a^6\ne0,\qquad E^3W_2=0,\\
T W_2=1,\qquad
\det\frac{\partial(X,Y,Z,W_2)}{\partial(u,a,\beta,q)}=a^2,\\
w_{02}=\beta+q^2,\qquad
\mathbb C[y,z,w_{02}]=A_*,\qquad
\Omega_2=\Omega+U^2,\qquad (\Phi_2,\Psi_2)=(\Phi,\Psi).
\end{gathered}
\tag{7}
\]
The target shear is invertible inside \(B_0\); it does not turn
\(B_0\subset B_*\) into equality. The tail assertion can be checked
without any realization theorem: \(Y^2=X^2\Theta(\tau^2)\) is an
exact finite Taylor identity with no negative powers. Its order-three
and order-four Taylor terms vanish. Thus adding it changes \(f_2\)
by \(\tau^2\), but changes neither negative tail.
The polynomial representatives in (6) now use
\(\beta=w_{02}-y^2\), and give the same two base defects.

## 5. What this boundary does and does not show

This polynomial model has a global source slice, rank-two dense good
speeds, an exactly quadratic bad slot after (7), polynomial projected
coefficient returns, and a nonzero intrinsic leading LND. It still
does not have actual fourfold coordinates. Its full pulled-back last
partial fails local nilpotence on the source, although it is locally
nilpotent on its own polynomial target subring.

Consequently these partial inputs cannot replace the actual-coordinate
premise when seeking automatic base compatibility. The model supplies
no actual extra-factor first tail and no cancellation counterexample:
its source invariant ring is already the polynomial ring
\(A_*=\mathbb C[a,\beta,q]\). The actual criterion (2) is a separate
consequence of the polynomial inverse, not a conclusion inferred from
this formal model.

## Sources

1. [Actual invariants give a denominator-free coefficient fiber143](polynomial-coefficient-fiber-presentation-pass143-working.md),
   Section 1, and [the actual dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Section 2. Actual projection and the distinction between the
   invariant ring and its projected polynomial overring.
2. [A formal extra branch can change the base speed ratio143](formal-base-incompatible-tail-pass143-working.md),
   Sections 1--3, and [signed negative-tail definitions139](dense-negative-tail-relations-pass139-working.md).
   The formal chart and signs rescaled in (3)--(7).

The criterion, polynomial rescaling, iterates and nonactuality
obstructions are proved directly here. No new external classification
or historical novelty claim is made. Finite symbolic controls, if run,
check examples and identities, not automatic base compatibility.

[^1]: Source 1. The polynomial coordinate expression for the actual
    slice is used in the strict-overring witness.
[^2]: Source 2. A unit relative Jacobian is not a polynomial inverse.
