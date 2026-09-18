# A speed curve gives a unit normal and a controlled good commutator

The rank-one good-speed case has the same two-generator conclusion
over an actual invariant plane as the rank-two conical case. Its
unit normal uses univariate Bezout rather than homogeneous binary
parametrization. The original last partial also gives a commuting
LND whose second iterate kills the three good coordinates. These
are reductions, not recognition of the remaining kernel.

## 1. Actual frame and polynomial curve parameter

Retain the full actual setup of the
[invariant-plane proof88](constant-acceleration-invariant-plane-pass88.md),
and suppose the good-speed derivative matrix has rank one:
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad
Ex_i=b_i\in S=\mathbb C[s_1,s_2],\quad Ez=qu,\quad Eu=1,
\quad q\in\mathbb C^*,\quad
S=\ker(W|A),\quad Wu=0,\quad
(b_1,b_2,b_3)S=S,\quad \operatorname{rank}db=1.
\tag{1}
\]
Here W is a nonzero highest-adjoint LND of the actual frame.
Write P=(b_1,b_2,b_3,qu) transposed and let J be its Jacobian
in the four original coordinates. It satisfies J fourth power zero,
JP=q e_4, and the exact adjoint-column formulas of that proof.

The retained
[polynomial-curve factorization](polynomial-curve-factorization-source.md)
applies directly to the subalgebra C[b_1,b_2,b_3] of S, not just
to the larger four-ring. It gives
\[
p\in S\setminus\mathbb C,\qquad
b_i=f_i(p),\quad f_i\in\mathbb C[t],\qquad
\gcd(f_1,f_2,f_3)=1.
\tag{2}
\]
For the gcd assertion, a nonconstant common factor would give the
nonconstant common factor obtained by substitution at p, contrary
to the unit ideal in (1). Substitution C[t] into S at the
nonconstant p is injective. At least one f_i is nonconstant.
No coordinate status of p in S or in B is asserted.

## 2. A unit univariate normal and two actual relative generators

The cross product f cross f prime is nonzero. Otherwise choose
a nonzero component f_j. Every ratio f_i/f_j has zero derivative,
so lies in C. The three f_i would be a common polynomial factor
times a constant vector. Their gcd in (2) would make all of them
constant, contrary to rank one.

Divide this nonzero cross product by its univariate gcd. This gives
\[
n(t)=\frac{f(t)\times f'(t)}{\gcd(f(t)\times f'(t))}
       \in\mathbb C[t]^3,\qquad
n f=n f'=0,\qquad
\sum_i\lambda_i(t)n_i(t)=1
\quad(\lambda_i\in\mathbb C[t]).
\tag{3}
\]
The last equality is Bezout in the univariate PID. In particular
N=n(p) is a unit row in S, not merely a row with constant gcd.

The original chain rule puts the image of J over Frac(B) in
the span of (f'(p),0) transposed and e_4. The highest nonzero
column W(x) is in im J, since it is a nonzero scalar multiple
of a positive power of J applied to an original constant column.
Thus its transverse part is a multiple of f'(p). Consequently
\[
c_0=N\cdot x_{\rm tr}\in A,\qquad W(c_0)=0,
\qquad c_0\in S.
\tag{4}
\]
The first membership uses E(c_0)=N b=0. The last uses the exact
kernel of W inside A, not a localized invariant-ring assertion.

Now apply the same split-module construction as in
[conical-normal89](constant-acceleration-conical-normal-pass89.md).
The unit column b belongs to ker N. Restricting a row ell with
ell b=1 splits off Sb; the remaining rank-one projective module
over the polynomial plane is free by the retained module theorem.
Choose its generator V and a column U_0 with NU_0=1. The actual
inverse of the matrix [b,V,U_0] defines elements satisfying
\[
x_{\rm tr}=b\sigma+VY+U_0c_0,\quad
E\sigma=1,\quad EY=0,\quad
B=S[\sigma,Y,z],\qquad
A=S[Y,c],\quad c=z-qu\sigma+\frac q2\sigma^2.
\tag{5}
\]
The equality for B is equality of subalgebras. Evaluation at the
actual slice sigma=0 in A[sigma] gives the equality for A.
Neither is a free polynomial presentation over S or an ambient
automorphism induced by an invariant-coefficient matrix.

If Y is algebraic over Frac(S), minimal-polynomial differentiation
by W gives WY=0, hence Y in S and A=S[c]=C cubed. Otherwise
S[Y] is a polynomial three-ring, but (5) alone does not recognize
A. This is the same explicitly limited endpoint as in conical89.

## 3. The original last partial and its controlled commutator

Rank db=1 gives rank J=2. A nilpotent four-by-four matrix of rank
two has third power zero. Since JP=q e_4, it follows that
J squared e_4=0. The exact adjoint formula therefore gives
ad_E squared of T zero for the original T=partial_z. Put
\[
Q=[E,T],\qquad [E,Q]=0,\qquad
Q(x)=-Je_4,\qquad Q(P)=0,\qquad Qp=Qu=0,
\qquad
Q\in\operatorname{LND}(B).
\tag{6}
\]
For Qp=0, apply Q to a nonconstant f_i(p); Q(P)=0 and
characteristic zero allow cancellation of f_i'(p). For local
nilpotence use epsilon exp(epsilon inverse E) T
exp(-epsilon inverse E)=epsilon T+Q. This is an LND on the
Laurent extension, preserves B[epsilon], and specializes to Q.
It is the same actual highest-coefficient degeneration as before.

If p_z=0, then the original good-coordinate ring is E-stable.
The exact retained stable-good-ring recognition gate in Section 2
of the [source85 note](rank-one-quasi-nice-source-scope-pass85.md)
applies. One also has u_z=0: (6) gives
Q=-q u_z partial_z and 0=Q(u)=-q u_z squared.

For the remaining case set alpha=p_z nonzero and beta=u_z.
The original Jacobian factors through the two covectors dp,du
and the two velocity directions (f'(p),0), q e_4. Its two-by-two
factor is
\[
C=\begin{pmatrix}
f'(p)\cdot\nabla_{\rm tr}p&q\alpha\\
f'(p)\cdot\nabla_{\rm tr}u&q\beta
\end{pmatrix},\qquad
\operatorname{tr}C=\det C=0,
\qquad
\alpha\bigl(f'(p)\cdot\nabla_{\rm tr}u\bigr)+q\beta^2=0.
\tag{7}
\]
The trace and determinant follow from det(I+tJ)=1 and the
rectangular determinant identity det(I+tUV)=det(I+tVU).
The last identity then follows by eliminating the upper-left
entry. This retains q as a nonzero constant, not a general
invariant acceleration.

Let d=gcd(alpha,beta) in the original polynomial UFD B, allowing
beta=0, and write alpha=d k, beta=d l with gcd(k,l)=1.
Every coefficient of Q=-alpha f'(p) dot partial_tr-q beta T
is divisible by d. Thus Qd belongs to dB. For an LND this
self-divisibility implies Qd=0: if Qd were nonzero, additivity
of the LND degree on products would contradict the degree drop
under Q. Dividing the last identity of (7) by d shows k divides
d, because k and l are coprime and q is a unit. Factorial closure
of the kernel of the LND Q now gives Qk=0. Hence
\[
Q(p_z)=Q(dk)=0,\qquad
Q^2(x_i)=-f_i'(p)Q(p_z)=0\quad(1\le i\le3),
\qquad \ker(Q|A)=S,\qquad p_z\in S.
\tag{8}
\]
All multiplicities in this divisibility argument are kept; no
radical-to-ideal promotion is used. Q is nonzero here because
alpha is nonzero and f' is a nonzero row. Its restriction to A
is nonzero as well: it kills u, and killing A too would kill
all of B=A[u].

For the kernel equality in (8), use
Q(x)=-J e_4=-q inverse times J squared P. Thus J squared is
nonzero. A nilpotent four-by-four matrix with rank two, third
power zero and nonzero square has Jordan type (3,1), so its
square has one-dimensional image. Both Q(x) and the nonzero
highest column W(x) lie on that line. The derivations are
nonzero rational multiples and hence have the same kernels on A.
Finally E(p_z)=[E,T](p)+T(Ep)=Qp=0. Together with Q(p_z)=0
and the exact kernel equality this proves p_z in S. It does
not prove that the original partial T preserves all of S.

The proof does not give
Q squared z zero, a slice for Q, or a new invariant ambient
coordinate. In particular it does not license the nice four-variable
recognition theorem for either E or Q.

## 4. Scope and provenance

Root posed the lower-speed-rank branch and the p_z=0 endpoint.
Geometry supplied the univariate unit normal and the content
argument for (8), including the common-highest-line consequence
placing p_z in S. The written predecessor proofs were reread for
the actual slice, frame, module and recognition gates.
The exact curve input is de Bondt
[Corollary 3.2](https://arxiv.org/pdf/1501.06046v4), printed pages
20--21, applied inside S. Its complete displayed proof and Lemma
3.3 were freshly reread in the retained primary text. This is not
a new reconstruction of their classical Luroth dependencies or
of the original module and recognition source proofs. No checker,
numerical run, shared metadata edit, or change to pass88 or older
artifacts accompanies this note.
