# Critical loci of the leading symmetries in actual quadratic cylinders

The two-quadratic-defect profile can have a simultaneous fixed locus
for all its highest intrinsic fields, even when their scalar
coefficients have no common irreducible factor. Thus removing a
divisorial gcd does not guarantee a nowhere-vanishing leading span.
The examples below have explicit polynomial quotients and slices.
They are obstructions to this recognition shortcut, not to cancellation.

## 1. An actual family from a unimodular polynomial pair

Let \(R=\mathbb C[u,v]\), and let \(f,g\in R\) satisfy a supplied
polynomial Bézout identity
\[
\alpha f+\beta g=1,\qquad \alpha,\beta\in R.
\tag{1}
\]
Work in the polynomial ring \(B=R[a,c]\) and put
\[
E=f\partial_a+g\partial_c,\quad
s=\alpha a+\beta c,\quad r=ga-fc.
\tag{2}
\]
The derivation fixes R, is locally nilpotent, and satisfies
\(E(s)=1\), \(E(r)=0\). The inverse coordinate presentation is
\[
a=fs+\beta r,\qquad c=gs-\alpha r.
\tag{3}
\]
Both composition identities follow from (1), so
\[
B=\mathbb C[u,v,r,s],\qquad \ker E=\mathbb C[u,v,r].
\tag{4}
\]
This uses actual inverse maps, not an abstract cancellation theorem
or an implication from a nonzero Jacobian.

Now introduce the physical polynomial coordinates
\[
b=u+a^2/2,\qquad d=v+c^2/2,\qquad x=(b,d,a,c).
\tag{5}
\]
Their inverse is \(u=b-a^2/2,\ v=d-c^2/2\). In this frame the
coefficient vector and highest iterate are
\[
E(x)=(af,cg,f,g)^{\mathsf t},\qquad
E^2(x)=(f^2,g^2,0,0)^{\mathsf t},\qquad E^3(x)=0.
\tag{6}
\]
All four coordinates therefore have flow degree at most two.

Write
\[
A_u=f_u\partial_a+g_u\partial_c,\qquad
A_v=f_v\partial_a+g_v\partial_c.
\]
In the intermediate coordinates \((u,v,a,c)\), the four physical
partials are
\[
T_1=\partial_u,\quad T_2=\partial_v,\quad
T_3=\partial_a-a\partial_u,\quad
T_4=\partial_c-c\partial_v.
\tag{7}
\]
Their highest commutators are
\[
W_1=[E,T_1]=-A_u,\quad W_2=[E,T_2]=-A_v,\quad
V_3=(\operatorname{ad}E)^2T_3=2fA_u,\quad
V_4=(\operatorname{ad}E)^2T_4=2gA_v.
\tag{8}
\]
One can derive, for example,
\([E,T_3]=-f\partial_u+aA_u\); its next bracket is \(2fA_u\).
All fields in (8) fix R and commute with E. Their next
commutators vanish.

If
\[
fg\ne0,\qquad
\det\operatorname{Jac}_{u,v}(f,g)\ne0,
\tag{9}
\]
then \(A_u,A_v\) are generically independent, and both quadratic
defects are independent. Thus (8) realizes exact adjoint profile
\((1,1,2,2)\). Also the highest map in (6) has Jacobian rank
two, since the map \((f,g)\) does and \(fg\ne0\).

## 2. The complete leading intrinsic ideal

Define
\[
\Delta_u=f g_u-g f_u,\qquad
\Delta_v=f g_v-g f_v.
\tag{10}
\]
Restriction of (8) to the actual kernel in (4) gives
\[
W_1|_{\ker E}=\Delta_u\partial_r,\qquad
W_2|_{\ker E}=\Delta_v\partial_r,\qquad
V_3|_{\ker E}=-2f\Delta_u\partial_r,\qquad
V_4|_{\ker E}=-2g\Delta_v\partial_r.
\tag{11}
\]
Each restricted field fixes u,v, and its value on r gives its
displayed coefficient. This verifies the signs without assuming
that restriction to an arbitrary subring is legitimate; E
centralizes every field involved.

Consequently their span over \(\ker E=\mathbb C[u,v,r]\) is exactly
\[
(\Delta_u,\Delta_v)\,\mathbb C[u,v,r]\,\partial_r.
\tag{12}
\]
Every R-linear combination is an LND, because its coefficient
is independent of r. An arbitrary combination over the larger
kernel algebra need not be locally nilpotent. The displayed
module has a nowhere-vanishing field if and only if its ideal
is the unit ideal. Indeed a polynomial multiple
\(h(u,v,r)\partial_r\) is nowhere zero exactly when h has
no zero in \(\mathbb A^3\), hence h is a nonzero constant
over \(\mathbb C\).

If both \(\Delta_u,\Delta_v\) are nonzero, the highest
commutators act nontrivially on the invariant r. The horizontal
coefficient degree therefore attains each adjoint bound.
The exact shifted slice-filtration profile is also
\((1,1,2,2)\), so its total height is ten.

The expressions in (10) are the differential of the projective
ratio \(g/f\), with its denominator cleared:
\[
d(g/f)=(\Delta_u\,du+\Delta_v\,dv)/f^2
\quad\text{on }D(f).
\tag{13}
\]
The identity (1) makes \([f:g]\) a morphism to \(\mathbb P^1\).
At a zero of f, g is nonzero, and the analogous expression
for \(f/g\) has the same critical ideal up to a unit. Thus (12)
measures the differential critical locus of that supplied
projective map. There is no assertion that every two-defect
action comes from this construction.

## 3. Isolated simultaneous fixed points with primitive coefficients

Take
\[
f=u^2+v^2,\qquad g=u f-1,\qquad \alpha=u,\quad\beta=-1.
\tag{14}
\]
Then (1) holds, with the actual slice \(s=ua-c\).
The determinant in (9) is
\[
\det\operatorname{Jac}(f,g)=-2vf\ne0.
\tag{15}
\]
The four highest intrinsic fields generate the ideal
\[
I=(f^2+2u,\,2v)\subset\mathbb C[u,v].
\tag{16}
\]
Its generators are relatively prime: a common irreducible
factor would have to divide v, but \(f^2+2u\) restricts at
\(v=0\) to the nonzero polynomial \(u^4+2u\).
Nevertheless I is not the unit ideal. More precisely,
\[
R/I\simeq\mathbb C[u]/(u^4+2u).
\tag{17}
\]
The four roots are distinct. The derivative \(4u^3+2\)
equals 2 at zero and equals minus 6 when \(u^3=-2\).
Thus the common zero set in the quotient plane consists of
four reduced points, namely \(v=0\) and \(u(u^3+2)=0\).

Over each point the four restricted fields all vanish on the
entire r-line in \(\operatorname{Spec}\ker E\). No polynomial
combination from (12) can remove those common fixed lines.
The coefficient gcd is already one, so dividing a common
divisor does nothing. The original E is a translation in its
actual slice s at all points, including over this locus.

The primitive intrinsic field \(\partial_r\) is available in
the explicit quotient coordinates, but is not a member of
the leading module (12). Extracting it is a strictly stronger
operation than taking an invariant-coefficient combination of
the four leading fields. In an unknown quotient, its existence
as a polynomial derivation would need a separate argument.

## 4. Divisorial collapse of every prescribed order

For comparison, take an arbitrary nonconstant \(p(u)\) and set
\[
f=p(u),\qquad g=v p(u)-1,\qquad
\alpha=v,\quad\beta=-1.
\tag{18}
\]
Again E has an actual slice and polynomial quotient. The
determinant of \(\operatorname{Jac}(f,g)\) is \(p p'\ne0\),
and
\[
(\Delta_u,\Delta_v)=(p',p^2).
\tag{19}
\]
This ideal is extended from \(\mathbb C[u]\). It is the
unit ideal precisely when p is squarefree. At a root of p
of multiplicity e, its common divisorial factor has order
e minus one. The choice \(p=u^N\), \(N\ge2\), gives
simultaneous vanishing order N minus one.

In this family the highest vector from (6), viewed as a
derivation in physical coordinates, is
\(U=p^2\partial_b+g^2\partial_d\). For \(p=u^N\),
\(U(u)=u^{2N}\). Inductively
\[
U^k(u)=
\left(\prod_{j=0}^{k-1}(1+j(2N-1))\right)
u^{1+k(2N-1)}\ne0.
\tag{20}
\]
It is not locally nilpotent. Its coefficient ideal remains
the unit ideal, since \(vp-g=1\) and
\[
p^2v^2(1-2g)+g^2(3+2g)=1.
\tag{21}
\]
For N=1 this is the earlier pass-39 example, not a new
discovery. The full repeated-root ideal and the isolated
primitive common-zero example in Section 3 are the additional
controls here.

## 5. Scope and verification

The construction and every inverse are proved over the given
polynomial ring. No ambient-coordinate recognition theorem is
used to identify these examples. Their invariant planes are
explicit, and both defect ranks and both height notions are
checked.

The construction does not classify the general flow-degree-two
profile, prove that its primitive intrinsic leading action has
a slice, or solve cancellation. In particular, (17) disproves
an automatic no-common-fixed-point argument even after the
divisorial gcd is removed. It does not prove that a different
coordinate frame cannot repair the situation.

The original profile, six-dimensional rank dichotomy and N=1
example are credited to
[the preceding two-defect note](two-quadratic-defects-pass39.md).
The arguments here are explicit polynomial identities and
one-variable factorization. Independent exact checks and
separate reconstruction results are recorded with the pass
before any stronger verification claim is made.
