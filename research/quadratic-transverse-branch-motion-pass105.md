# Transverse branch tangents record the first normal action

The formal double cover in104 has a concrete interpretation in the
original invariant base. Cut the actual threefold by each level of the
global projected slice r. The tangent of its double-cover branch varies
affinely with the slice level exactly when the first normal N-action on
the collapsed double component is nonzero.

This does not put these transverse branch curves inside the fixed
exceptional curve of the quotient. The retained polynomial control
shows that containment is false even with a global translation and
an absolute polynomial cylinder. Constant branch tangents also do not
make the complete branch germs constant.

## 1. Actual inputs and every shifted slice

Retain the whole collapsed double or mixed (2,1) hypotheses of
[adic103](quadratic-adic-projected-translation-pass103.md) and
[transverse104](adic-transverse-surface-pass104.md), with
L(m) nonzero. In particular the following are actual global data:
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\qquad
E=\partial_u,\quad u=Ez/q_0,\quad q_0=E^2z\in\mathbb C^*,\\
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad J=\mathfrak mA,\\
D=(T|_A)|_{u=0},\quad T=\partial_z,\qquad
r=z-q_0u^2/2\in A,\qquad Dr=1,\qquad D(J)\subset J,\\
A/J=\mathcal D[r],\qquad
\mathcal D=\mathbb C[G]/(H(G)),\qquad
H(T)=T^2\text{ or }T^2(T-1).
\end{gathered}
\tag{1}
\]
D is not asserted to be globally locally nilpotent. Its induced
derivation D_k on A_k=A/J^k is locally nilpotent for every k by103.
It has slice r-t for every complex constant t. Put C_k=ker D_k.
The coefficient ring C_k is independent of t, but the evaluation
retraction onto it is not. Denote that retraction by P_{k,t}.

In the actual presentation A_k=C_k[r], polynomial evaluation gives
\[
\begin{gathered}
P_{k,t}(a)=
\sum_{j\ge0}\frac{t^j}{j!}P_{k,0}(D_k^j a),\\
C_k\simeq A/(J^k,r-t),\qquad
\mathcal H_t=A/(r-t),\qquad
C_\infty\simeq\widehat{\mathcal H_t}^{\,\mathfrak m\mathcal H_t}.
\end{gathered}
\tag{2}
\]
The sum is finite at each k and for each a. This equality is a
polynomial Taylor identity over the possibly nonreduced ring C_k.
It does not assume a uniform bound in k or that D kills S.
The S-map into C_k in (2) is s mapped to P_{k,t}(s).
Equivalently, it is the original S-map followed by passage to the
actual quotient surface H_t and then transported to C_k.

All of the transverse104 argument applies to r-t. Multiplication
by r-t is injective on each flat layer
\((\mathfrak m^i/\mathfrak m^{i+1})\otimes\mathcal D[r]\).
Thus the strict-intersection proof gives the same exact lengths
and compatible finite free power bases for every t. Also Dr=1
makes H_t a smooth affine surface. Its completed factor at the
double point is a regular local ring, finite free of rank two
over \(\widehat R\), where R=S_m. In the mixed case the other
factor is free of rank one. No finiteness of the entire localized
surface over R is inferred from its completion.

## 2. The original quotient conormal fixes the branch tangent

Let C be the collapsed double component with ideal q and actual
coordinate c. Use the actual constant base change and centered
good normal generators from
[volume-normal99](quadratic-volume-normal-splitting-pass99.md):
\[
\begin{gathered}
\mathfrak q=(F,G),\qquad A/\mathfrak q=\mathbb C[c],
\qquad \mathfrak m=(x,f),\\
x\equiv F\pmod{\mathfrak q^2},\qquad
f\equiv a(c)F\pmod{\mathfrak q^2},
\qquad a(c)=a_0+a_1c,\quad a_i\in\mathbb C,\\
NF\equiv0,\qquad NG\equiv-\nu a_1F
\pmod{\mathfrak q^2},\qquad\nu\in\mathbb C^*.
\end{gathered}
\tag{3}
\]
These are identities in the actual conormal bundle over the entire
component, not only in its rational generic fiber. The first normal
action is nonzero precisely when a1 is nonzero.

The slice difference h has constant reduced value eta2 on C. Since
the specified c satisfies c=r+q0 h squared/2, the reduced restriction
of r is c-q0 eta2 squared/2. Therefore H_t meets the reduced double
component at the single actual point
\(P_t\) with \(c=c_t:=t+q_0\eta_2^2/2\).
This uses only the reduced value of h to locate the point; its
nilpotent part is not being removed from the surface equation.

At P_t, the differentials dF,dG,dc are independent in the smooth
threefold. The coefficient of dc in dr is one: h is constant on
the reduced component, so dh has zero tangent component there.
Consequently dF,dG remain a cotangent basis on the surface H_t.
Restricting (3) to this surface gives the exact cotangent map
\[
\begin{gathered}
\mathfrak m/\mathfrak m^2\longrightarrow
\mathfrak m_{P_t,\mathcal H_t}/\mathfrak m_{P_t,\mathcal H_t}^2,
\qquad dx\longmapsto dF,
\qquad df\longmapsto a(c_t)dF,\\
\boxed{\quad
\ker(d\pi_t)=
\mathbb C\bigl(df-a(c_t)\,dx\bigr).
\quad}
\end{gathered}
\tag{4}
\]
Here ker(d pi_t) denotes the kernel of this displayed cotangent
pullback, rather than the kernel of the oppositely directed map
on tangent vectors. Terms in q squared have zero differential
at P_t, and differentiating a(c)F contributes no a-prime term
there because F(P_t)=0. Thus no derivative of a moving point or
unproved normalization specialization enters (4).

By the complete double-cover description104, the double factor
of (2) has the form
\(\widehat R[Y]/(Y^2-\Delta_t)\), with
\(\Delta_t\in\mathfrak m\widehat R\setminus
\mathfrak m^2\widehat R\).
Its branch divisor is the principal divisor generated by Delta_t;
the relative differential is generated by dY with relation
2Y dY=0, so the ramification locus is Y=0 and its image is
Delta_t=0. The class of Delta_t spans the kernel in (4).
Multiplying it by a nonzero complex scalar normalizes its linear
class to give
\[
\boxed{\quad
\Delta_t\equiv
f-\bigl(a_0+a_1(t+q_0\eta_2^2/2)\bigr)x
\pmod{\mathfrak m^2\widehat R}.
\quad}
\tag{5}
\]
For this scalar rescaling one may rescale Y by a complex square
root, so the double-cover form is preserved.

It follows that a nonzero first normal action is equivalent to
nonconstant variation of these branch tangent lines as t varies.
When a1 is nonzero they run through all lines df-b dx with b in C.
When a1 is zero their tangent line is constant. These statements
compare lines in the one fixed cotangent space of the original
base S at m. The different maps of S into the fixed formal kernel
C_infinity are still the corrected embeddings P_{k,t} from (2).
No equality with the original S inside the completed A is asserted.

## 3. The transverse branch is not the quotient exceptional curve

Use the already retained intrinsic polynomial family, here with
a harmless factor two in its normalization:
\[
\begin{gathered}
A_0=\mathbb C[x,y,r],\quad
f=y^2-2x^er,\quad S_0=\mathbb C[x,f],\quad e\ge1,\\
N_e=x^e\partial_y+y\partial_r,\qquad
D=\partial_r,\qquad Dr=1,\qquad
J_0=(x,f)A_0=(x,y^2)A_0,\\
\mathcal H_t^0=\mathbb C[x,y],\qquad
f=y^2-2t x^e,\qquad
\boxed{\quad\Delta_t=f+2t x^e.\quad}
\end{gathered}
\tag{6}
\]
The full kernel S0 of Ne, primitivity, faithful flatness and actual
polynomial cylinder of this family were proved in cyclic103. D is
globally locally nilpotent and preserves J0 and all its powers.
These are genuine intrinsic rings and maps, not arbitrary formal
coefficient data. Their original nonconical E-frame is not supplied.

The quotient is a polynomial line off x=0. On x=0 its generic
fiber has the quadratic constant field obtained by adjoining a
square root of f. Its fixed closed fiber is over (x,f)=(0,0).
Thus the relevant fixed quotient exceptional curve is x=0.
But the transverse cover H_t^0 to Spec S0 is ramified along
f+2t x^e=0, which is not contained in x=0, even as a formal
curve germ. Indeed its quotient is C[[x]], where x is nonzero.

For e=1 the retained conormal column is (1,-2r), so its first
normal action is nonzero. The branch tangent in (6) varies exactly
as (5) predicts. For e at least two that action and the tangent
variation vanish, but the complete branch germs still change with
t, first at order e. The order e can be arbitrarily large.

This proves the precise failure of a proposed shortcut: branch
curves from the transverse slices need not be branches of one
fixed exceptional curve of the original quotient. One cannot use
the finite number of exceptional-curve tangents to force a1=0.
Even proving constant tangents would not make the higher branch
coefficients independent of the slice value. The example is not
a counterexample using every original-frame identity, and it is
already an affine threefold, not a cancellation counterexample.

## Scope

The new actual conclusion is (5), including its equivalence with
the first normal N-action and its origin in every actual shifted
slice. The proof uses the complete finite-translation and
transverse-surface arguments103--104, and the full conormal and
affine-column result99. Those retained files were reread; no new
external theorem is invoked and no primary-source claim is added.

The intrinsic control is reused to distinguish transverse
ramification from quotient exceptional geometry. No numerical
method, global coordinate, extra order of original E/T commutation,
mixed-fiber exclusion, or algebraization follows. The arbitrary
sliced-action entry problem remains untouched. No file through104
was edited.
