# The primitive field is the exact relative Jacobian field

In the actual two-generator presentation, the primitive intrinsic
derivation agrees, up to a nonzero complex scalar, with the relative
Jacobian derivation of the defining equation. No nonconstant common
factor has to be removed from its two coefficients in A. Their ideal
can nevertheless be proper.

This is a statement about a derivation of the quotient A, not about
local nilpotence of a Hamiltonian derivation on the ambient polynomial
ring S[Y,Z]. It does not recognize A as a polynomial three-ring.

## 1. Hypotheses and conclusion

Retain the conclusions of the actual
[relative presentation78](binary-relative-hypersurface-pass78.md).
The argument below only needs the following part of those conclusions:
\[
\begin{gathered}
S=\mathbb C[u,v]\subset A=S[y,z]\simeq S[Y,Z]/(F),
\qquad A\text{ an affine UFD domain},\\
0\ne D\in\operatorname{LND}_S(A),\qquad
D\text{ primitive},\qquad\ker D=S,\\
S\subset A\text{ faithfully flat with every closed fiber a curve},
\qquad F\text{ irreducible and primitive over }S.
\end{gathered}
\tag{1}
\]
Here a curve fiber has dimension one and is nonempty, with its whole
scheme structure retained. Primitivity means that the values of D on
finite algebra generators have gcd one in A, not that they generate
the unit ideal. The earlier
[saturation argument54](primitive-fiber-nonvanishing-pass54.md)
also derives this formulation from the absence of an invariant
replica factor.

Set K=Frac S and evaluate all displayed partial derivatives at
the actual y,z in A. The derivation
\[
D_F(y)=F_Z,
\qquad D_F(z)=-F_Y,
\qquad D_F(S)=0
\tag{2}
\]
is well defined because it annihilates the relation F. The conclusion is
\[
\boxed{D_F=\lambda D\quad\text{for some }\lambda\in\mathbb C^*.}
\tag{3}
\]
In particular D_F is an LND of A and has the same kernel S.

## 2. Generic local nilpotence, without an embedding theorem

A local slice for the given nonzero D yields
\[
A_K=A\otimes_S K=K[t],\qquad D(t)=1.
\tag{4}
\]
Let y(t),z(t) denote the two K-algebra generators. Because
t is a polynomial in y,z, the chain rule gives
(y'(t),z'(t))K[t]=K[t].

For completeness, the conormal differential sequence gives
\[
K[t](F_Y,F_Z)=
\ker\bigl(K[t]^2\longrightarrow K[t],\ (a,b)\mapsto ay'+bz'\bigr).
\tag{5}
\]
Indeed this is the differential presentation of
K[Y,Z]/(F)=K[t], with dt as its differential basis.[^diff]
Since y',z' generate the unit ideal, the kernel in (5) is generated
by the unimodular vector (-z',y'). For example, if ry'+sz'=1
and ay'+bz'=0, then (a,b)=(-z',y')(rb-sa).
Equality of these two cyclic submodules implies
\[
(F_Y,F_Z)=q(-z',y')\quad\text{with }q\in K[t]^*=K^*.
\tag{6}
\]
To check that q is a unit rather than just nonzero, inclusion in one
direction writes the left generator as q times the right generator;
the reverse inclusion writes the right as r times the left. The
nonzero right generator over a domain gives rq=1.

Equation (6) shows that D_F=q partial_t on A_K. Consequently it is
locally nilpotent there. The inclusion A into A_K is injective, and
D_F already preserves A by (2). For each a in A, some iterate is
zero in A_K and hence in A. Thus D_F is an actual LND of A.
No assertion about the ambient derivation of S[Y,Z] is used.

## 3. The scalar is a regular invariant

The two fields D and D_F kill K and are proportional over
Frac A=K(t). Write D_F=gD with g in Frac A. Each value
gD(a) lies in A. In the UFD A, any irreducible denominator of g
would divide every value of the primitive D. Therefore
\[
g\in A\setminus\{0\},\qquad D_F(g)=gD(g)\in gA.
\tag{7}
\]
For an LND L on a characteristic-zero domain, L(f) in fA implies
L(f)=0. Otherwise the additive L-degree of L(f) is one less
than that of f, while the degree of f times a nonzero element
is at least that of f. Apply this to L=D_F and f=g.
Then D_F(g)=0, and the domain identity gD(g)=0 implies D(g)=0.
It follows that g belongs to the actual kernel S.

## 4. Every whole closed fiber removes a possible base factor

Fix a maximal ideal m of S. The exact presentation gives
\[
A/\mathfrak m A=\mathbb C[Y,Z]/(F_{\mathfrak m}).
\tag{8}
\]
The polynomial F_m is nonzero and nonconstant. If it were zero,
the fiber would be the affine plane, contradicting its dimension.
If it were a nonzero constant, the fiber would be empty.

In characteristic zero, a nonconstant polynomial has a nonzero
formal partial derivative. Such a partial has strictly smaller
total degree and therefore cannot be divisible by F_m. Thus
the derivation induced by (2) is nonzero on the whole ring in (8).
This argument does not require F_m to be reduced or irreducible.

If g belonged to m, the equality D_F=gD would instead make the
induced D_F zero on (8). Hence g belongs to no maximal ideal of S.
It is a unit of S, whose units are precisely C*. This proves (3).

## 5. Exact fixed ideal and the nonreduced boundary

Since u,v,y,z generate A and D kills u,v, equation (3) identifies
the fixed-point ideal of the primitive action:
\[
\boxed{(D(A))A=(F_Y,F_Z)A,\qquad
\gcd_A(F_Y,F_Z)=1\text{ up to a unit}.}
\tag{9}
\]
The first ideal is the relative critical ideal of this plane-curve
presentation. The equality concerns the whole scheme. It does not
make this ideal the unit ideal and does not assert smoothness of
all fibers of Spec A to Spec S.

The polynomial control
\[
A_0=\mathbb C[u,y,z],\quad S_0=\mathbb C[u,v],\quad v=uz-y^2,
\qquad F=uZ-Y^2-v
\tag{10}
\]
has D_F=u partial_y+2y partial_z. Its two coefficients have gcd
one, but the fixed ideal (u,y) is proper. In the fiber u=v=0,
the class of y is nonzero and nilpotent; D_F(z)=2y remains
nonzero there. Passing to the reduced fiber would erase it.
This is an intrinsic control, not a supplied nice/good-frame example.

For the actual derived field delta=hD, equation (3) consequently
allows its invariant factor to be renormalized so that
delta=h_0 D_F with h_0 in S. This strengthens the divided-gradient
formula in the
[transported good-partial calculation79](relative-good-partial-equations-pass79.md).
Neither h_0 nor the gradient ideal has been shown to be a unit.

## 6. Scope and source

The proof uses the actual two-generator quotient, generic line,
factorial primitivity and every whole curve fiber. It is not a
generic-to-global freeness principle for arbitrary LNDs. It does
not produce a nice frame for an arbitrary cylinder action or
address the no-good-direction branch.

The earlier ambient Hamiltonian constructions over C[j] in pass29
have different hypotheses and use an embedding theorem. They are
not invoked in this quotient-only proof. No historical novelty,
human expert review, Lean verification or general cancellation
solution is claimed.

[^diff]: The Stacks Project, [Lemma 10.131.9, tag 00RU](https://stacks.math.columbia.edu/tag/00RU), the conormal exact sequence for a quotient algebra. The complete displayed proof was freshly read. Only that exact differential presentation is the external input in (5); the kernel calculation, unit coefficient, saturation and fiber argument are written out here.
