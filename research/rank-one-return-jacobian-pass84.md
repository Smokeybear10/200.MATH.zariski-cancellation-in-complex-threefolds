# The rational return map has determinant minus one

The actual rank-one quadratic flow imposes an additional exact
condition on its rational return involution: its Jacobian determinant
is minus one, including the three-by-three determinant with the original
fourth coordinate held fixed. This uses the original action and does
not follow merely from a stationary parameter pair. It does not make
the return map polynomial or settle first- or square-power membership.

## 1. Original action and the return involution

Work in the same actual sliced setting as the
[strict slice certificate](rank-one-strict-slice-certificate-pass84.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\\
a_i=E(x_i),\quad E(a_i)=0,\qquad b=E(z),\quad E(b)=q,
\quad E(q)=0,\quad q\ne0.
\end{gathered}
\tag{1}
\]
Put x=(x_1,x_2,x_3)^t, a=(a_1,a_2,a_3)^t and
P=(a_1,a_2,a_3,b)^t. The polynomial flow is
Phi_t(x,z)=(x+ta,z+tb+t squared q/2). Over K=Frac(B), set
\[
\tau=-\frac{2b}{q},\qquad
\rho=\Phi_\tau(x,z)=\left(x-\frac{2b}{q}a,z\right).
\tag{2}
\]
Flow invariance gives a composed with rho equal to a and q composed
with rho equal to q, whereas b composed with rho equals minus b.
Thus tau composed with rho equals minus tau, and the flow group law
gives rho composed with rho equal to the identity. These equalities
hold rationally, without asserting that rho preserves B. They are
the full-coordinate version of the
[pass83 return identities](rank-one-return-map-integral-closure-pass83.md).

## 2. The variable-time determinant

Let M_t be the four-by-four Jacobian of Phi_t with t held constant.
It has determinant one. Indeed, the inverse Phi_(-t) shows that its
determinant is a unit of B[t], so it is a nonzero complex constant;
specialization t=0 makes that constant one. Differentiating the flow
group law in its second time parameter also gives M_t P=P(Phi_t).
With M=M_tau, the ordinary chain rule for the variable time in (2)
therefore gives
\[
\operatorname{Jac}\rho
 =M+P(\rho)\,d\tau
 =M\bigl(\mathrm{Id}_4+P\,d\tau\bigr),
\qquad d\tau(P)=E(\tau)=-2.
\tag{3}
\]
Here d tau is a row of ordinary derivatives in the four original
coordinates. All matrices are over K. The rank-one determinant
identity det(Id+v r)=1+r v now proves
\[
\begin{gathered}
\det\operatorname{Jac}_{(x,z)}\rho=-1,\\
\det\operatorname{Jac}_{x}\rho_x
=\det\left(
\mathrm{Id}_3-\frac{2b}{q}\operatorname{Jac}_x a
-a\,d_x\!\left(\frac{2b}{q}\right)
\right)=-1.
\end{gathered}
\tag{4}
\]
The second equality follows because rho fixes the actual coordinate z;
the last row of its full Jacobian is (0,0,0,1). It is not a determinant
in hypothetical invariant coordinates. In particular, (4) specializes
to z=0 whenever q(x,0) is not the zero polynomial, as an equality of
rational functions in the three remaining coordinates.

The proof uses no recognition theorem, reduced-fiber assumption, or
Jacobian-conjecture implication. In fact, the determinant calculation
itself needs only the indicated original polynomial flow; the supplied
slice is retained to match the surrounding actual-action problem.

## 3. Genuine poles remain possible

The already recognized sliced triangular control from the
[pass81 shear boundary](rank-one-acceleration-shear-boundary-pass81.md)
has actual coordinates (a,x,c,z) and
\[
E=a^2\partial_x+(1+ax)\partial_z,\qquad q=a^3,
\qquad
\rho(a,x,c,z)=\left(a,-x-\frac2a,c,z\right).
\tag{5}
\]
Its global polynomial slice and both polynomial adapted-coordinate
inverse orders were proved in that note. The displayed return is an
involution with determinant minus one, but its x component has a
genuine pole along a=0. Thus neither the determinant nor the existence
of the original polynomial slice removes return-map denominators.
This is the same retained control, not a new action family.

The two-method [strict-slice checker](strict_slice_checks_pass84.py)
includes the determinant identity for this control and for its
separate actual two-speed frame. Those finite checks do not prove
(4) universally; the source-free calculation above does. No new test
method, first-power membership theorem, coordinate reduction, general
cancellation claim, or historical novelty assertion accompanies this
note. Files through pass83 are unchanged.
