# Stationary parameter classes do not contradict invariant omission

For every integer m at least two, there is an actual polynomial
coordinate pair p,q with a proper ideal I, whose derivatives under
the actual partial T=partial_w lie in I^m, and for which the whole
algebra C[p,q] contains no nonconstant polynomial killed by any
nonzero constant partial. Thus these stationarity and omission
properties alone do not exclude a proper parameter ideal.

This is a control for a proposed deduction, not an example of the
required nice sliced action. In fact the original niceness identities
exclude every nonzero derivation annihilating this exact pair.

## 1. Actual inverse and proper stationary ideal

In B=C[x,y,z,w], fix an integer m>=2 and put

\[
A=w+z^2,\qquad B_0=w+z^3,\qquad
p=x+y^m A,\qquad q=y+p^m B_0.
\tag{1}
\]

The use of B0 for the polynomial w+z^3 is distinct from the ring B.
The pair of maps (x,y,z,w) to (p,q,z,w) and

\[
y=q-p^m B_0,\qquad x=p-(q-p^m B_0)^m A,
\qquad z=z,\quad w=w
\tag{2}
\]

are polynomial inverses in both orders. Indeed the first inversion
recovers y from the second shear, then recovers x from the first.
In particular p,q,z,w are independent actual coordinates.
Their ideal satisfies

\[
I=(p,q)B=(x,y)B\ne B.
\tag{3}
\]

One inclusion follows directly from (1), and the reverse inclusion
from (2). Under the original T=partial_w, with original x,y,z
held fixed, the exact derivatives are

\[
Tp=y^m,\qquad
Tq=p^m+m p^{m-1}B_0y^m,\qquad Tp,Tq\in I^m.
\tag{4}
\]

Thus T preserves I and kills the two displayed parameter classes
in I/I^2. This does not mean that its induced action on the whole
conormal module is zero: coefficients can still depend on w.

## 2. No polynomial in the pair omits a constant direction

For every nonzero constant vector c=(a,b,d,r), let
Tc=a partial_x+b partial_y+d partial_z+r partial_w.
We prove

\[
\mathbb C[p,q]\cap\ker T_c=\mathbb C.
\tag{5}
\]

Use the actual coordinates in (2), so all polynomials below lie
in C[p,q,z,w], with y=q-p^m B0. Direct differentiation in the
original coordinates gives

\[
\begin{aligned}
C_p:=T_cp&=a+m b y^{m-1}A+y^m(r+2zd),\\
C_q:=T_cq&=b+m p^{m-1}B_0 C_p+p^m(r+3z^2d).
\end{aligned}
\tag{6}
\]

The degree in w of Cp is at most m, and its coefficient at
w^m is exactly

\[
L=(-p^m)^{m-1}\bigl(mb-p^m(r+2zd)\bigr).
\tag{7}
\]

Suppose a nonconstant f(p,q) is killed by Tc. If f_q is nonzero,
the chain rule and (6) give

\[
0=(f_p+m p^{m-1}B_0 f_q)C_p
   +f_q\bigl(b+p^m(r+3z^2d)\bigr).
\tag{8}
\]

The coefficient at w^(m+1) is m p^(m-1) f_q L. As the
variables p,q,z are independent and the ring is a domain, it
follows that L=0. Formula (7) then forces b=d=r=0. Now
Cp=a and Cq=m p^(m-1)B0 a, so the coefficient at w in the
same equation forces a=0, contrary to c being nonzero.

If f_q=0, then f_p is nonzero in characteristic zero. The chain
rule gives Cp=0. Its leading coefficient (7) first forces
b=d=r=0, after which Cp=a forces a=0. This contradiction proves
(5), including polynomials f of arbitrary degree.

## 3. The original niceness identities exclude this exact pair

Let E be any derivation of the actual polynomial ring B, and
assume Ep=Eq=0 and E^2x=E^2y=E^2z=E^2w=0. No local
nilpotence or supplied slice is needed in this subsection.
Apply E twice to the first inverse identity in (2). It gives

\[
0=E^2y=-6p^m z(Ez)^2.
\tag{9}
\]

The ring is a domain and p,z are nonzero polynomials, so Ez=0.
The same identity now gives Ey=-p^m Ew. Applying E twice to
x=p-y^m(w+z^2), using E^2y=E^2w=0, yields

\[
\begin{aligned}
0=E^2x
&=-m p^m y^{m-2}(Ew)^2
\bigl((m-1)p^m(w+z^2)-2y\bigr),\\
(m-1)p^m(w+z^2)-2y
&=p^m\bigl((m+1)w+(m-1)z^2+2z^3\bigr)-2q\ne0.
\end{aligned}
\tag{10}
\]

The last inequality uses independent p,q,z,w and the nonzero
coefficient -2 of q. All the other displayed factors except
Ew are nonzero, including y^(m-2) when m=2. Hence Ew=0,
then Ey=0 and Ex=0. Thus E=0.

Consequently this exact pair cannot be invariant under any
nonzero nice derivation in the original frame. The equations
of an original action provide a real extra restriction which
the stationarity and omission properties do not detect.

## 4. Exact scope of the obstruction

The original nonlinear-cone argument supplies more than (3)--(5):
there must be a nice polynomial LND E, an original polynomial
slice for E, the identity ad_E^2 T=0, and homogeneous binary
velocity forms in p,q. It also supplies invariance under the
derived field and the intrinsic filtration constraints proved in
[the conormal note](binary-conormal-obstruction-pass77.md).
None of those additional action requirements is inferred from
this control; Section3 directly rules out its nice realization.

In particular (5) is a statement about C[p,q], not about a
putative full kernel A. It shows that even the full constant-
direction omission property on the parameter subalgebra is
compatible with a proper stationary parameter ideal. An exclusion
of the proper ideal must use some additional original-action
condition; it cannot follow solely from horizontal generator
classes and that omission property.

The inverse and all-degree coefficient argument are elementary
and source-free. The author read the saved proof through EOF.
The separate [finite checker](nice_binary_scheme_checks_pass77.py)
tests m=2,3 inside its fifth method, including the two
nonrealization identities. That finite check does not replace
the all-degree proof. No additional standalone suite is introduced
by this note, and no historical novelty or general cancellation
claim is made.
Frozen files through pass76 and shared metadata are unchanged.
