# Common leading kernels and the commuting-partial recognition gate

For a supplied three-good-coordinate frame, a two-dimensional joint
speed field forces the leading intrinsic derivations of all original
partials to have the same kernel. It does not force all intrinsic LNDs
to have that kernel. An existing actual polynomial control separates
these statements. There is also a useful recognition gate: **any**
original coordinate partial commuting with the sliced action suffices,
including a good-coordinate partial.

## 1. Exact common-kernel statement

Work in the actual quadratic-last-coordinate setup
\[
 B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad E(u)=1,\quad A=\ker E,
 \quad E^2x_i=0,\quad a_i=Ex_i,\quad E^2z=q\in A,
 \quad K_0=\mathbb C(a_1,a_2,a_3,q),\quad
 \operatorname{trdeg}_{\mathbb C}K_0=2.
 \tag{1}
\]
Here \(E\) is locally nilpotent. The joint field, not just the
good-speed field, is the rank-two hypothesis in this section.

Let \(T_j\) run through the four original coordinate partials. If
some \(T_j(A)=0\), extend scalars to \(\operatorname{Frac}A\).
A nonzero LND of the one-variable polynomial ring over that field
has constant coefficient, so \(T_j=fE\) with \(f\in A\).
The identity \(T_j(x_j)=1\) makes \(f\) a unit of \(B\), hence a
nonzero complex constant. Then \(A=\ker T_j\) is polynomial.
Thus suppose no partial is vertical in this sense.

The actual graded degeneration in
[the intrinsic-speed proof125](three-good-intrinsic-speed-quotient-pass125.md),
Sections 2--3, applies to each \(T_j\), not only \(\partial_z\).
Its proof uses only local nilpotence and \(T_j(A)\ne0\) at that step.
It gives exact nonnegative shifts \(d_j\) and leading LNDs
\(u^{d_j}N_j\), where \(0\ne N_j\in\operatorname{LND}(A)\)
and the leading field kills \(u\). Since
\(T_j(x_i)=\delta_{ji}\), comparison in degree \(d_j+1>0\)
gives \(N_j(a_i)=0\). If \(q\ne0\), comparison of
\(T_j(z)=\delta_{j4}\) in degree \(d_j+2\) gives \(N_j(q)=0\).
The latter is automatic for \(q=0\).

Put \(F=\operatorname{Frac}A\). Each invariant field
\(F_j=\operatorname{Frac}(\ker N_j)\) has transcendence degree two
and is relatively algebraically closed in \(F\). These facts follow
from the local-slice presentation and differentiation of a separable
minimal polynomial. Since \(K_0\subset F_j\), the extension
\(F_j/K_0\) is algebraic. Conversely every element of \(F\)
algebraic over \(K_0\) is killed by every \(N_j\). Thus all \(F_j\)
equal the relative algebraic closure \(L\) of \(K_0\) in \(F\), and
their actual ring kernels equal \(S=A\cap L\).

The resulting precise statement is
\[
 \ker N_j=S,\qquad \operatorname{Frac}S=L,\qquad
 N_j=f_jN_0\ (0\ne f_j\in S),\qquad
 \deg_u T_j(s)\le d_j-1\quad(s\in S),
 \tag{2}
\]
where \(N_0\) is a primitive LND of \(A\). The convention in the
last inequality is that degree at most \(-1\) means zero.

Here is the saturation justification. The affine ring \(A\) is a UFD
because \(A[u]\) is a UFD. Divide a nonzero \(N_j\) by the gcd of
its values on finitely many algebra generators. Each prime factor
\(p\) of this gcd satisfies \(p\mid N_j(p)\), hence is invariant
by LND divisibility. The divided derivation \(N_0\) is therefore
locally nilpotent and primitive, with the same kernel. After inverting
the nonzero elements of \(S\), the actual ring is \(L[t]\).
All the \(N_j\) become constant multiples of \(\partial_t\), so
their ratios with \(N_0\) lie in \(L\). Primitivity rules out a
pole of any ratio at every prime of the UFD \(A\); the ratios
belong to \(A\cap L=S\). Finally the top coefficient of \(T_j(s)\)
is \(N_j(s)=0\), which proves the degree drop in (2).

The retained quotient-surface theorem identifies this same embedded
\(S\) as \(\mathbb C^{[2]}\), with faithful flatness. That conclusion
retains the [intrinsic quotient proof's](intrinsic-quotient-surface-pass.md)
geometric source dependencies. Neither \(L=K_0\) nor polynomial
generators for the speed algebra are asserted.

## 2. An actual control against the all-intrinsic-rank inference

Use the \(\ell=2\) member of the already checked
[polynomial family125](three_good_controls_pass125.py):
\[
 A=\mathbb C[a,b,c],\quad E=\partial_u,\qquad
 X=a,\quad Y=b+a^2u,\quad Z=c+bu,\quad W=u+Z^2.
 \tag{3}
\]
This is an actual coordinate system. Its inverse is
\(u=W-Z^2\), \(a=X\), \(b=Y-X^2u\), \(c=Z-bu\).
Both compositions are polynomial identities; no localization is used.
Its good speeds are \((0,a^2,b)\), and its acceleration is \(2b^2\).

Holding the other original coordinates fixed gives
\[
 \begin{aligned}
 T_X&=\partial_a-2au\partial_b+2au^2\partial_c,\\
 T_Y&=\partial_b-u\partial_c,\\
 T_W&=\partial_u-a^2\partial_b+(a^2u-b)\partial_c,\\
 T_Z&=\partial_c-2(c+bu)T_W.
 \end{aligned}
 \tag{4}
\]
Consequently
\[
 (d_X,d_Y,d_Z,d_W)=(2,1,2,1),\qquad
 (N_X,N_Y,N_Z,N_W)=(2a,-1,-2a^2b,a^2)\partial_c,
 \qquad S=\mathbb C[a,b].
 \tag{5}
\]
No partial is vertical. The joint field \(\mathbb C(a^2,b)\)
has transcendence degree two, while its relative algebraic closure
in \(\mathbb C(a,b,c)\) is \(\mathbb C(a,b)\). All four selected
leading kernels agree. Nevertheless \(A\) has three independent
intrinsic translations \(\partial_a,\partial_b,\partial_c\).
This is a recognized polynomial action with partial height ten,
not a cancellation counterexample or an example of intrinsic rank one.

The rank-one application of [the cylinder criterion35](rank-one-cylinder-pass35.md)
assumes that **all** intrinsic LNDs have generic rank one. Its relative
transfer uses that quantifier, and its further group argument requires
a finite-dimensional all-LND Lie closure. A finite selected list as
in (2) supplies neither premise. In particular (4) itself contains
partials moving \(S\), even though their leading intrinsic parts
kill \(S\). No invariance of \(S\) under the full original partials
or all cylinder automorphisms follows.

## 3. Any commuting original partial gives recognition

This section needs only the three-good hypothesis and the original
slice. It needs neither \(E^3z=0\) nor the joint-field assumption.
Suppose an original partial \(T_j\) commutes with \(E\). Its kernel
\(R\) is the actual polynomial three-ring generated by the other
three original coordinates, and \(E(R)\subseteq R\). At least two
of those three generators are good. Write \(D=E|_R\).

If \(D=0\), any generator of \(R\) is already an invariant ambient
coordinate. Otherwise divide the coefficient gcd \(g\) of \(D\)
in the UFD \(R\). The same prime-divisibility argument as above
gives \(D(g)=0\), so \(D_0=D/g\) is an irreducible LND with
the same kernel. For the two retained good generators \(y_1,y_2\),
\(0=D^2y_i=g^2D_0^2y_i\), hence \(D_0^2y_i=0\).

Wang's two-quasi classification, reproduced as Dasgupta--Gupta
Theorem 4.1, applies to precisely this actual characteristic-zero
polynomial three-ring and nonzero irreducible LND. In case (I) an
invariant constant linear form is a coordinate. In case (II) the
displayed invariant \(V\) is a coordinate. Either way there is
\(v\in R\) which is an actual coordinate of \(R\) and satisfies
\(Ev=0\). No slice for \(D\) or \(D_0\) is needed.
[Exact research-paper restatement of Wang's theorem](https://arxiv.org/html/1701.03635v1).

The original slice makes \(A\simeq B/(u)\) regular: the identity
\(E(u)=1\) makes the partial derivatives of \(u\) generate the unit
ideal. Since \(v\) is also an ambient coordinate of \(B\),
Bhatwadekar--Gupta--Lokhande Theorem 3.5 now applies and gives
\[
 [E,T_j]=0\text{ for some original partial }T_j
 \quad\Longrightarrow\quad
 B=\mathbb C[v]^{[3]},\ E(v)=0,\ A=\mathbb C[v]^{[2]}.
 \tag{6}
\]
That theorem assumes a nonzero \(\mathbb C[v]\)-LND of an actual
polynomial three-ring over \(\mathbb C[v]\), with regular kernel.
All those hypotheses have just been verified.
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1).

This extends the explicitly recorded bad-partial/nice-three-ring
application in [source-scope85, Section 2](rank-one-quasi-nice-source-scope-pass85.md)
to a commuting good partial by using the two-quasi theorem. It is
an application of existing recognition results, not a new published
classification or a historical novelty claim.

## 4. The height consequence and exact limits

The [cofactor proof126](three-good-flow-cofactor-bounds-pass126.md)
bounds the partial shifts by \((3,3,3,2)\) in the quadratic case.
With the retained height \(H=\sum_j(d_j+1)\), this gives \(H\le15\),
not eleven. A vertical partial already recognizes the kernel, and
for a nonnegative shift, degree zero is exactly commutation with
\(E\). Thus any not-yet-recognized instance in this supplied class
has all four shifts positive. In particular
\[
 H=11\quad\Longrightarrow\quad
 \text{sorted }(d_j)\in\{(1,1,2,3),(1,2,2,2)\}
 \quad\text{for any hypothetical nonpolynomial kernel.}
 \tag{7}
\]
The all-profile [height-ten theorem73](height-ten-closure-pass73.md)
is a retained working recognition theorem. The bounds do not imply
\(H_{\min}\le10\), \(H_{\min}=11\), or recognition of (7).

The [constant-acceleration proof88](constant-acceleration-invariant-plane-pass88.md)
uses \(q\in\mathbb C^*\) to
center a global slice and obtain a unit speed row. Having \(q\in S\)
does not give those premises. Inverting a nonconstant \(q\) changes
the global ring; treating it as a scalar over \(\operatorname{Frac}S\)
does not recover the actual polynomial four-ring required by the
retained constant-acceleration recognition chain. None of these
localizations supplies an unrestricted entry theorem.

## Reading and verification scope

The full saved cofactor126 and the retained rank-one-cylinder35,
intrinsic-rank34, constant-acceleration-plane88, height-ten73 and
source-scope85 notes were read for these comparisons. The proof above
independently reconstructs the field-kernel and primitive-saturation
steps. The primary Bhatwadekar--Gupta--Lokhande Theorem 3.5 statement
and complete displayed proof, and the exact Dasgupta--Gupta Theorem 4.1
statement, were freshly read. The original Wang proof and the deeper
dependencies of those recognition theorems were not newly audited.

No tests were executed, no new checker was added, and no file through
pass125 was changed. The control is the existing actual family,
with its four partials derived here. The selected common-kernel
statement and conditional recognition gate do not assert freeness
of the extracted action, intrinsic rank one, or full cancellation.
