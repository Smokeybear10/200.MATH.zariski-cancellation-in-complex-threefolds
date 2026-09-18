# The acceleration field need not be locally nilpotent

For a sliced polynomial action whose four original coordinate flows have
degree at most two, the coordinate acceleration column is invariant under
the action. It does not in general define a commuting, nice, or locally
nilpotent polynomial vector field. This remains false when its coefficient
ideal is the unit ideal and the acceleration field itself takes a polynomial
to one.

The countercontrol below is an already recognized translation in explicit
nonlinear coordinates. Its two-by-two matrix mechanism is retained in
[pass32, Section 5](stable-polynomial-invariants-pass32.md); the contribution
here is the exact failure of the proposed acceleration-field extraction,
including its primitive unit-coefficient version. No new counterexample to
cancellation or claim of historical novelty is made.

## 1. Exact input and the missing identities

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad E\in\operatorname{LND}(B),
\qquad Es_*=1,\qquad E^3x_i=0.
\]
Set
\[
P=Ex,\qquad Q=E^2x,\qquad
H=\sum_iQ_i\partial_{x_i},\qquad J=\operatorname{Jac}_xP.
\tag{1}
\]
The actual identities are
\[
EQ=0,\qquad [E,H](x)=-JQ,\qquad
H^2(x)=(\operatorname{Jac}_xQ)Q.
\tag{2}
\]
The first follows from the supplied time-degree bound. The other two are
direct evaluations on the original polynomial generators. The first does
not imply either of the other displayed expressions vanishes.

In particular H is not obtained by transporting an intrinsic second
derivative as a derivation. For a polynomial coordinate change y=f(x),
\[
E^2f=(\operatorname{Jac}f)Q+
\left(\sum_{i,j}P_iP_j\partial_i\partial_j f_k\right)_k.
\tag{3}
\]
The Hessian term prevents the acceleration column from transforming as
an ordinary vector field under nonlinear coordinate changes. Formula (3)
does not contradict covariance under actual affine-linear changes.

The [proper quadratic-flow audit55](proper-quadratic-flow-scope-pass55.md)
distinguishes time degree from spatial degree and records the missing
actual-base or invariant-coordinate premises of relative recognition
theorems. Those premises are not being supplied by H here.

## 2. A primitive, nowhere-zero acceleration field which is not LND

Start with genuine coordinates (s,a,b,c) and E=partial_s. Define
\[
x=s,\qquad y=(1+s^2)a+s b,\qquad z=s a+b,
\qquad w=c+s^2.
\tag{4}
\]
These are actual polynomial coordinates, with both-sided inverse
\[
s=x,\qquad a=y-xz,\qquad
b=(1+x^2)z-xy,\qquad c=w-x^2.
\tag{5}
\]
Substituting (4) into (5), or (5) into (4), returns every input
coordinate. A constant Jacobian determinant is not the inverse argument.
The last two-by-two inverse is the same retained matrix used in pass32;
the final triangular replacement w=c+s^2 adds a unit acceleration.

In the actual (x,y,z,w) frame,
\[
E=\partial_x+\bigl(xy+(1-x^2)z\bigr)\partial_y
 +(y-xz)\partial_z+2x\partial_w,\qquad
Q=(0,2(y-xz),0,2)^t.
\tag{6}
\]
The inverse proves E is locally nilpotent, its kernel is
\(\mathbb C[a,b,c]\), and x is an actual polynomial slice. Its four
coordinate expressions in (4) have s-degree at most two, so E cubed
kills all four. Also E(a)=E(b)=E(c)=0 directly.

Writing a=y-xz, the acceleration field is
\[
H=2a\partial_y+2\partial_w,\qquad
H(a)=2a,\qquad H^n(y)=2^n a\quad(n\ge1),\qquad
H(w/2)=1.
\tag{7}
\]
Thus H is not locally nilpotent and is not nice in these original
coordinates. Its coefficients generate B, so there is no nonunit
coefficient content to divide out. It is nowhere zero, but its taking
w/2 to one is not an LND hypothesis and cannot justify the LND slice
theorem.

Finally (2) gives
\[
[E,H]=-2a\bigl(x\partial_y+\partial_z\bigr)\ne0.
\tag{8}
\]
Consequently H does not restrict to a derivation of ker E: the actual
evaluation from b=(1+x^2)z-xy is H(b)=-2xa, which is not
E-invariant. Equivalently E(Hb)=-2a while H(Eb)=0.

## 3. Separate boundaries: rank one and niceness

If w=c is used in (4), the same inverse with c=w gives
Q=(0,2a,0,0). All accelerations lie on a single constant direction,
but H=2a partial_y is still not locally nilpotent, by the same iteration
in (7). Its primitive part partial_y is an LND but does not commute
with E. Thus rank-one acceleration does not repair this extraction.
Both variants already have an invariant ambient coordinate, respectively
c=w-x^2 and w; neither is an unresolved action.

Even imposing niceness and local nilpotence of H would not imply
commutation. The actual inverse pair
\[
(x,y,z,w)=(s,a+s^2,b+sa,c),\qquad
(s,a,b,c)=(x,y-x^2,z-x(y-x^2),w)
\]
gives E=(1,2x,y-x^2,0), Q=(0,2,0,0), H=2 partial_y, but
[E,H]=-2 partial_z. The acceleration field is now a constant nice
LND. Its commutation still fails.

There is also no uniform coordinate-flow degree for those extracted H
which happen to be LNDs. For any polynomial g(a), use the actual
triangular inverse pair
\[
(u,v,w,t)=(s+a^2,a+u^2,b+v g(a),c),\qquad
(s,a,b,c)=(u-(v-u^2)^2,v-u^2,w-vg(v-u^2),t).
\]
The original E=partial_s still square-accelerates only v,w and has
Q=(0,2,2g(a),0). Here H=2 partial_v+2g(v-u^2) partial_w is a
triangular LND and H^n(w)=2^n g^(n-1)(a) for n>=1, where the
superscript on g denotes ordinary differentiation. For g=a^d,
d>=1, its original w-flow has degree d+1. This is Root's separate
explicit triangular construction, not a general consequence for H.

## 4. What this does and does not resolve

The original polynomial action, its global slice, every coordinate
inverse, and every failure above are actual. No fraction-field action,
formal derivative matrix, or localized coordinate claim is substituted.

These examples rule out an automatic acceleration-LND/common-quotient
argument, including the unit-coefficient repair. They do not exclude a
different canonical auxiliary derivation or a nonlinear change making
the original E nice. In each control such a change is already given.
The rank-one acceleration recognition question is separate from the
failure of this particular extraction. General cancellation remains
unresolved and no theorem from the fixed-base sources is imported.

Both inverse orders, Q, E(Q), H(Q), the commutator, and the first
example's invariant generators were checked in one exact inline SymPy
calculation before writing. The all-n iteration in (7) is proved by
H(a)=2a, not by finitely many tests. This note adds no standalone
checker or method count and changes no frozen file.
