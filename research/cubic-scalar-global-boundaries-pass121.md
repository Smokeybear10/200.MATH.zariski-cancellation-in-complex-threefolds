# Polynomial speed controls and the relative-volume boundary

Both non-null scalar types retained in121 admit polynomial, unimodular
speed controls with the canonical metric and nonzero frame determinant.
Thus the null reciprocal exclusion cannot be transferred to the
non-null axis just from polynomial speed identities. Separately,
a relative Jacobian must not be upgraded from a base-field unit to
a complex constant without controlling its parameter normalization.

These are boundaries on two possible proof shortcuts. No control
below is supplied with an original polynomial four-ring realization.

## 1. Both non-null scalar types have polynomial speed controls

In the actual polynomial plane S=C[s,t], put T=s squared-1 and
W=st-1. The following two triples have the scalar form b=(g,P,Y)
of [normal forms121](cubic-axis-scalar-normal-forms-pass121.md):

\[
\begin{array}{c|c|c|c}
&b=(g,P,Y)&h=P/Y&D(h)\\ \hline
\text{cubic}&(s,TW,T^2W^3)&1/(TW^2)&h^3\\
\text{reciprocal}&(s,T^2W^3,TW)&TW^2&1/h
\end{array}
\qquad g^2-D(h)Y^2=1 .
\tag{1}
\]

In each row D(h)Y squared=T, so the norm identity is immediate.
Both ratios h are nonconstant rational functions on the plane.
The determinants and a common polynomial unit-row certificate are

\[
\begin{gathered}
\Omega_{\mathrm{cubic}}=2sT^2W^3\ne0,\qquad
\Omega_{\mathrm{reciprocal}}=-2sT^2W^3\ne0,\\
1=TW-s(s^2t-s-t),\qquad (g,P,Y)S=S,\\
\Delta_{h^3}=-3h^4/4\ne0,\qquad
\Delta_{1/h}=-3/(4h^4)\ne0 .
\end{gathered}
\tag{2}
\]

Here TW is the second component in the cubic case and the third
component in the reciprocal case. Thus the identity proves that the
whole speed ideal is S; it is stronger than a coefficient gcd of one.
The determinants can be computed first with s,W independent and then
multiplied by the base Jacobian Wt=s. Swapping the last two speeds
reverses their sign.

In either case form Q from D by the non-null scalar formulas121,
and put n=(0,1,-h). Direct substitution gives Q(b,b)=-1, n transposed
b=0, and Qh=(Dhhh/2)nn transposed. Differentiation gives Q(b,b_i)=0
and Q(b_i,b_j)=Gij, where Gij is the radial coefficient in the
expansion of b_ij in (b,bs,bt). This proves that Q is the canonical
metric of these polynomial speeds. Their cubic tensor is nonzero
and is proportional to (dh) cubed. The constant non-null axis is e1.

No relative generators, actual potential, or global coordinate inverse
are assigned. Consequently these triples do not establish sufficiency
of the scalar classification, let alone give cancellation counterexamples.
They show precisely that polynomiality, a global unit row and the
canonical metric identities do not exclude either non-null type.

## 2. A generic parameter changes the actual volume by a base factor

The actual volume statement in [potential90, Section2](nonconical-quadratic-potential-pass90.md)
is a unit after base-only localization, hence an element of K*.
It does not assert a complex constant. This remains true when the
relative generator is replaced by the degree-one curve coordinate
v=y1 used in121.

For a precise normalization check, retain the oriented polynomial
Jacobian derivation of [the global Jacobian proof91](nonconical-global-jacobian-field-pass91.md):

\[
N(f)=\det\frac{\partial(s,t,u,f)}{\partial(x_1,x_2,x_3,z)},\qquad
\mathcal J=\det\frac{\partial(x_1,x_2,x_3,z)}{\partial(u,s,t,v)},
\qquad \mathcal J\,N(v)=1 .
\tag{3}
\]

The chain rule proves the last identity: the permutation from
(u,s,t,v) to (s,t,u,v) is even. Since N is a nonzero K-translation
on A_K=K[v], N(v) is a member of K*, not necessarily the constant
one. The graph normalization v=y1 does not provide N(v)=1. An
alternative normalized slice could provide that equality, but then
the displayed relative-curve formulas must also be transformed.

This invalidates a proposed shortcut in the surviving null cubic
case. With its notation l constant, alpha=0 and P=hY, the chain rule
and the null volume121 give

\[
\mathcal J=-\frac{l\,\operatorname{Jac}(P,Y)}{Y^4}
            \bigl[(m'-2\beta n)Y^2+n'\bigr]\in K^* .
\tag{4}
\]

For the [polynomial null control121](cubic-null-axis-polynomial-speed-pass121.md),
Y=-s cubed and Jac(P,Y)=3s to the seventh power. The expression
becomes -3l[(m'-2beta n)s+n'/s to the fifth power]. The choices
m=h,n=0 make it -3ls, an allowed nonzero base-field unit. A
contradiction that required this expression to be a nonzero complex
constant would therefore impose an extra, unproved normalization.
This observation does not assert a full potential or inverse for
those particular polynomial speeds.

## 3. Verification scope

The [one-method control](cubic_scalar_speed_boundary_checks_pass121.py)
checks both explicit non-null speeds, determinant signs, unit rows,
and canonical metric identities. The volume normalization (3) is
the chain-rule argument above, independently reconstructed from the
retained90 and91 definitions. No current finite test claims a
global inverse or arbitrary-frame entry. The remaining task must
use more of the original polynomial reconstruction than the
coefficient identities tested here. Files through120 remain frozen.
