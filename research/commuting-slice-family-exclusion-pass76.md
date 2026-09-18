# Primitive freeness for a variable-direction translation extension

The following nice sliced family also cannot produce primitive
intrinsic fixed points. Unlike the linearly triangular family, it
allows a direction in a two-plane that varies with the invariant a.
It does not classify every nice action with an affine slice.

## 1. Actual inverse coordinates

Take B=C[a,s,b,c], coprime u,v in C[a], and h in C[a,I], where
the symbols on the right of the following formulas are evaluated
in the original ring:
\[
I=v(a)b-u(a)c,\qquad
E=\partial_s+h(a,I)\bigl(u(a)\partial_b+v(a)\partial_c\bigr).
\tag{1}
\]
Here u,v generate the unit ideal of C[a]. One component may be
zero, but not both. We may assume h is nonzero, since h=0 makes
E constant and every derived constant-direction field zero.
Directly, Ea=EI=0 and Es=1, so E is nice and locally nilpotent.
Choose r,t in C[a] with ru+tv=1 and put
\[
J=rb+tc,\qquad V=J-s h(a,I),\qquad
b=u\bigl(V+s h(a,I)\bigr)+tI,\quad
c=v\bigl(V+s h(a,I)\bigr)-rI.
\tag{2}
\]
These are two-sided polynomial inverse coordinates between
(a,s,b,c) and (a,I,V,s). Indeed v b-u c=I and r b+t c=V+s h
under the displayed inverse, and substituting the original I,J
recovers b and c. Thus E=partial_s in the adapted frame and
A=ker E=C[a,I,V]. No inverse follows merely from a Jacobian test.

Requiring the velocity pair in (1) to be coprime loses no member
of this displayed form. For a nonzero pair with gcd rho, divide
u=rho u0, v=rho v0, replace I by I0=v0 b-u0 c, and replace h
by h0(a,I0)=rho h(a,rho I0). This gives exactly the same original
E and now a unimodular pair. This normalization is not an
assertion that an arbitrary nice four-variable action has form (1).

## 2. The exact constant-good condition

Let T have constant components (tau_a,tau_s,tau_b,tau_c) in the
original frame. Put Q=[T,E] and W=uv'-u'v. Subscripts on h hold
its other displayed argument fixed. The original coefficients are
\[
\begin{aligned}
Qa&=Qs=0,\\
(Qb,Qc)&=\tau_a h(u',v')+(u,v)L,\\
L&=\tau_a h_a+h_I\bigl(\tau_a I_a+\tau_bv-\tau_cu\bigr),\\
E(Qb,Qc)&=\tau_a h h_I W(u,v).
\end{aligned}
\tag{3}
\]
For the last identity, E(I_a)=h(v'u-u'v)=hW, while E kills
a,I,u,v,h. Since E is nice and T is constant, differentiating
E(P)=0 along T gives Q(P)+E(Qx)=0. Consequently
[E,Q]x=2E(Qx). In characteristic zero the exact good-direction
condition is therefore
\[
[E,Q]=0\quad\Longleftrightarrow\quad \tau_a h h_I W=0.
\tag{4}
\]
At least one of u,v is nonzero, so no vector cancellation weakens
this scalar condition. It is computed before the base-dependent
coordinate change, which need not preserve constancy of T.

Assume from now on that T is good and that E,Q are independent
over Frac B. Since Qs=0 and B=A[s], this is equivalent to the
intrinsic restriction d=Q|A being nonzero. We show in every
branch that its primitive division has a polynomial slice.

## 3. The mixed and constant-direction branches

If h_I and W are both nonzero, (4) forces tau_a=0. Equation
(3) then gives QI=0 and QJ=(tau_b v-tau_c u)h_I. Since Qs=0
and Qh=0, the actual invariant coordinates (2) give
\[
d=(\tau_bv-\tau_cu)h_I\partial_V
\quad\text{on }A=C[a,I,V].
\tag{5}
\]
Its coefficient is nonzero by independence. It is its entire
coordinate content, so the primitive part is partial_V and has
slice V, including at zeros of that removed coefficient.

If W=0, coprimality in C[a] forces u,v to be constants. When
both are nonzero their rational ratio has derivative zero and
is constant, and a proportional coprime pair has constant
entries; the zero-axis case follows from unimodularity. Choose
r,t constant as well. Now I,J are affine-linear coordinates,
and (1) becomes E=partial_s+h(a,I)partial_J. In this actual
frame Q fixes a,I,s and has the single J-coefficient
tau_a h_a+(tau_bv-tau_cu)h_I. The same coefficient is dV.
Its primitive division is again partial_V whenever d is nonzero.

## 4. The invariant-line translation branch

The remaining case has h_I=0. Write p=hu and q=hv in C[a].
Use the simpler actual coordinates
\[
B_0=b-s p(a),\qquad C_0=c-s q(a),\qquad
A=C[a,B_0,C_0],\qquad
d=\tau_a p'(a)\partial_{B_0}+\tau_a q'(a)\partial_{C_0}.
\tag{6}
\]
Their inverse is b=B0+s p and c=C0+s q. Because d is nonzero,
at least one of its two coefficients is nonzero. After division
by their gcd, they generate the unit ideal in the PID C[a].
A Bezout combination of B0,C0 is a polynomial slice for the
primitive derivation. This includes either single nonzero speed
derivative and excludes the zero derived field explicitly.

The cases h_I=0, W=0 and h_I W nonzero exhaust (4). Hence
every independent constant-good derived field in (1) has a
primitive intrinsic slice. The result concerns d itself, so
choosing a different supplied E-slice does not alter it. The
single-colon wedge-ideal criterion from
[pass75](primitive-good-quotient-scope-pass75.md) is the unit
ideal for this entire family.

## 5. Why this is an additional construction exclusion

For u=1, v=a and h=I=ab-c, the action in (1) is not
triangularizable by an affine-linear change. To see this, an
affine-linear form L has
E L=tau_s+(ab-c)(tau_b+a tau_c). A constant value forces
tau_b=tau_c=0, so all constant-velocity linear forms belong
to the span of s,a and constants. A linear invariant must in
fact belong to the span of a and constants.

Suppose an affine-linear triangular nice frame existed. If
its first speed is nonzero, its second speed is constant by
niceness. Its first two coordinates would then span s,a.
If its first speed is zero, its first coordinate is an affine
function of a; a second-coordinate speed depending only on a
again forces that coordinate into the span of s,a. Thus in
both cases the first two coordinates span s,a. A third
independent affine-linear coordinate has a nonzero b,c part,
and its velocity (ab-c)(tau_b+a tau_c)+tau_s cannot belong
to C[a,s]. This contradicts triangularity.

This explicit member is therefore outside the hypothesis of
the separate [linearly triangular theorem](triangular-nice-primitive-freeness-pass76.md).
It is already polynomially recognized by (2), and its primitive
derived fields are free by the proof above. It is not a
cancellation counterexample. Neither the general primitive
freeness question nor recognition of an arbitrary nice action
is established here. The written calculation is elementary;
historical novelty, human review and formal verification are
not claimed.
