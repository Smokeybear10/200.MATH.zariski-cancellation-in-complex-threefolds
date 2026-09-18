# A slice commuting with a coordinate partial: scope and obstruction

No general polynomial-kernel theorem for the arbitrary extension
\[
E=D+f\partial_t\quad\text{on }R[t],\qquad R=\mathbb C^{[3]},
\quad D\in\operatorname{LND}(R),\quad f\in R,
\tag{1}
\]
was verified in this bounded audit. The unresolved case in this
argument is rank-three \(D\) with arbitrary \(f\), even assuming a
polynomial \(E\)-slice. This is not a claim that an exhaustive literature
search establishes the exact class as a named open problem.

There is a concrete algebraic obstruction to a tempting reduction:
a slice need not be affine in \(t\), and even a rank-three base
extension can have a slice without \(f=c+D(H)\). Both phenomena occur
in examples with explicitly polynomial kernels.

## 1. What existing theorems do close

Commutation with \(\partial_t\) is exactly the presentation (1).
Every such extension is locally nilpotent: on base generators this is
local nilpotence of \(D\), and
\(E^{j+1}(t)=D^j(f)\). The coordinate partial supplies no further
nilpotence restriction on \(D\) or \(f\).

If \(D\) has rank at most two, it fixes an ambient coordinate of
\(R\), which \(E\) also fixes. A slice makes \(\ker E\) regular,
so [Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
gives \(\ker E\cong\mathbb C^{[3]}\). The case \(D=0\) is immediate:
a slice forces \(f\) to be a nonzero constant.

If \(f=c+D(H)\), \(c\in\mathbb C^*\), the polynomial shear
\(T=(t-H)/c\) gives \(E=D+\partial_T\); finite exponentiation
\(r\mapsto\exp(-TD)(r)\) provides polynomial invariant coordinates.
This is sufficient, not a necessary condition in general.

The directly checked nearby primary results retain additional premises:

- [Freudenburg, Section 7.1, Proposition 7.1](https://arxiv.org/pdf/2108.12021)
  starts with an invariant added coefficient and an image-ideal
  saturation condition. Theorem 7.6 further assumes a fundamental pair
  and a coefficient in its degree-zero invariant ring. These are not
  arbitrary-coefficient slice theorems.
- [Dubouloz, Finston and Jaradat, *Proper triangular additive-group
  actions on affine four-space are translations*](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-p.pdf)
  requires triangulability. A slice already makes the \(E\)-action
  proper, but (1) is not a triangular presentation unless a suitable
  triangular presentation of the base derivation is available. The
  proof does not establish triangulability from a commuting partial.

The latter paper states the broader proper-action problem as open in
its 2014 introduction. That historical statement does not certify the
current status of this exact subclass. The source comparison agrees
with the earlier [extension-literature.md](extension-literature.md).

## 2. The exact slice equations do not remove higher powers of \(t\)

If a slice has degree zero in \(t\), it is a slice for \(D\), which
is already a closed case. For \(s=\sum_{j=0}^n b_jt^j\) with
\(n\ge1\), equation \(E(s)=1\) is precisely
\[
D b_n=0,\qquad
D b_j+(j+1)fb_{j+1}=0\ (1\le j<n),\qquad
D b_0+fb_1=1.
\tag{2}
\]
A slice with \(\partial_t s\in\mathbb C^*\) is equivalent to the
gauge form \(f=c+D(H)\). Neither (2) nor local nilpotence forces
that constant derivative.

In fact a slice need not admit any affine-in-\(t\) replacement in the
same frame. On \(\mathbb C[x,y,z,t]\), take
\[
E=x^2\partial_y+(1+xy)\partial_t.
\]
As proved constructively in
[arbitrary-coefficients-pass.md, Sections 1-2](arbitrary-coefficients-pass.md),
the polynomial
\[
s=t+\frac{y^3}{2}+\frac{xy^4}{8}-xyt
-\frac{x^2y^2t}{2}+\frac{x^3t^2}{2}
\tag{3}
\]
is a coordinate slice and the kernel is polynomial.

Suppose an affine slice \(u t+v\) existed. The coefficient of \(t\)
forces \(u\in\ker(x^2\partial_y)=\mathbb C[x,z]\), and
\[
x^2v_y+u(1+xy)=1.
\]
Modulo \(x\), this gives \(u(0,z)=1\). Write
\(u=1+xu_1(z)\pmod{x^2}\). The coefficient of \(x\), modulo
\(x^2\), would give \(u_1(z)+y=0\), impossible.
Thus the minimum \(t\)-degree of a slice is exactly two in this
example. It disproves an all-base affine-slice reduction, not a
rank-three-specific theorem.

## 3. Non-gauge slices also occur with a rank-three base

Let \(D_0\) be any nonzero nonslice LND on \(R=\mathbb C^{[3]}\).
Choose a local slice \(b\), writing
\[
D_0(b)=g\ne0,\qquad D_0(g)=0.
\]
Since \(D_0\) has no slice, \(g\) is nonconstant. Set
\[
D=(g-1)D_0,\qquad f=g+1,
\qquad E=(g-1)D_0+(g+1)\partial_t.
\tag{4}
\]
Then
\[
s=\frac{(2-g)t+b}{2},\qquad E(s)=1.
\tag{5}
\]
Nevertheless \(f\ne c+D(H)\) for every \(c\in\mathbb C^*\) and
\(H\in R\). Such an equality would make \(g-1\) divide
\(g+1-c\), hence divide the constant \(2-c\). Thus \(c=2\), and
cancellation of \(g-1\) gives \(D_0(H)=1\), a contradiction.

If \(D_0\) has rank three, then so does \(D\), because their kernels
are equal. Such base derivations exist, for example the sourced
Freudenburg derivation treated in
[arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md).
Thus the failure is not confined to rank-one base derivations. It does
not contradict that note's theorem for the fixed irreducible
Freudenburg derivation: (4) replaces that base by a nontrivial replica.

There is still an explicit translation certificate for (4). Extend
\(D_0\) by killing \(t\), and set \(\Phi=\exp(tD_0)\), an actual
polynomial automorphism. Because \(D_0g=0\),
\[
\Phi D_0\Phi^{-1}=D_0,\qquad
\Phi\partial_t\Phi^{-1}=\partial_t-D_0.
\]
Therefore
\[
E':=\Phi E\Phi^{-1}=-2D_0+(g+1)\partial_t.
\]
The shear \(T=t+b/2\) gives \(E'(T)=1\), and in \(R[T]\),
\(E'=-2D_0+\partial_T\). Its invariant coordinates are
\(\exp(2TD_0)(x_i)\) for any coordinate generators \(x_i\) of \(R\).
Hence (4) has polynomial kernel even though no original-frame gauge
form exists. Mixing the base and extension variable is essential to
this particular certificate.

Seven inline exact checks confirmed (3), (5), and a simple specialization
of the conjugation in 0.031 seconds. The non-gauge and arbitrary-base
arguments above are symbolic proofs, not consequences of those checks.

## 4. The remaining intrinsic obstruction

For any slice \(s\) of (1), write \(B=K[s]\), \(K=\ker E\).
The commuting coordinate partial restricts to an LND
\(d=\partial_t|_K\), and
\[
\partial_t=d+q\partial_s,
\qquad q=\partial_t(s)\in K,
\qquad K^d=\ker D.
\tag{6}
\]
For nonzero \(D\), the last ring is abstractly \(\mathbb C^{[2]}\)
by Miyanishi's theorem, in the exact formulation recalled by
[Freudenburg, Theorem 2.4(a)](https://arxiv.org/pdf/2108.12021).
If \(d\) has a slice, (6) immediately gives \(K\cong\mathbb C^{[3]}\).
The coordinate slice \(t\) of \(\partial_t\) does not supply a
slice for its restriction to \(K\), and separate slices for \(E\)
and \(\partial_t\) do not supply a dual slice system for the pair.

Accordingly the valid endpoint is a precise unresolved implication in
this audit, not a general closure: recognize \(K\) for rank-three
\(D\) and arbitrary \(f\) from the coupled equations (2) or (6).
Neither a constant \(\partial_t s\) nor an affine-in-\(t\) slice is
available as a general shortcut. No general known-open designation or
novelty claim is asserted beyond the checked sources.
