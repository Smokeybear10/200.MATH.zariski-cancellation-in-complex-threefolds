# Canonical volume factors the original parameter derivative

The actual unit joint-curve presentation gives an exact factorization
of the original derivative \(p_z\). The multiplier is a nonzero complex
constant, not an unspecified rational function of the invariant base.
It also identifies the primitive intrinsic derivation underlying the
selected commutator. Primitivity does not imply that this derivation
is fixed-point-free.

## 1. The actual presentation being used

Retain the complete hypotheses and construction of the
[unit-curve normal form126](three-good-unit-curve-normal-form-pass126.md).
In particular, the following are actual subalgebra equalities:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[\sigma],\qquad
E\sigma=1,\quad A=\ker E,\\
S=\ker N=\mathbb C[s,t],\qquad
A=S[Y,D]\simeq S[y,d]/(a d-F(y))\subset K[Y],\qquad
K=\operatorname{Frac}S,\\
0\ne a\in S,\quad F\in S[y],\quad
\gcd_S(a,\text{all coefficients of }F)=1,\qquad A_K=K[Y],\\
p,h,\alpha\in S,\quad \alpha=\partial_zp\ne0,\qquad
N(Y)=-\alpha\beta(p),\quad 0\ne\beta\in\mathbb C[T],\\
x_{\rm good}=M(p)\begin{pmatrix}\sigma\\Y\\h\end{pmatrix},
\qquad M\in\operatorname{GL}_3(\mathbb C[T]),\quad
\kappa=\det M\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
Here \(D\) is the invariant element denoted \(d_0\) in that note;
lowercase \(y,d\) are independent presentation variables. The first
column of \(M\) is the good speed column \(f\), and \(\beta\) is the
coefficient of the second column in the decomposition of \(f'\).
The normal form proves \(\operatorname{trdeg}_{\mathbb C}\mathbb C[p,h]=2\).
It does not prove \(S=\mathbb C[p,h]\).

The algebra \(A\) is smooth over \(\mathbb C\). One way to see this is
that regularity descends from its polynomial extension \(A[\sigma]=B\);
\(A\) is a finitely generated complex algebra, so regularity gives
smoothness. This is smoothness over \(\mathbb C\), not a claim that
the quotient morphism \(\operatorname{Spec}A\to\operatorname{Spec}S\)
is smooth everywhere.

## 2. A global determinant-line generator

Let \(R=\mathbb C[s,t,y,d]\) and \(L=a d-F(y)\). The exact presentation
in (1) gives \(A=R/(L)\). The conormal module \((L)/(L^2)\) is free
of rank one with generator the class of \(L\). Smoothness gives the
split exact sequence
\[
0\longrightarrow A\,dL
\longrightarrow A\,ds\oplus A\,dt\oplus A\,dy\oplus A\,dd
\longrightarrow\Omega^1_{A/\mathbb C}
\longrightarrow0,
\qquad
\det\Omega^1_{A/\mathbb C}\simeq A.
\tag{2}
\]
For injectivity one can also use the nonzero coefficient
\(L_d=a\ne0\) in the domain \(A\). The split-conormal assertion is
the standard smooth-presentation criterion; its exact form is
displayed in [Stacks, tag 00T1](https://stacks.math.columbia.edu/tag/00T1),
immediately after Definition 10.137.1.

Taking determinants in (2) constructs a global, nowhere-vanishing
generator of the top exterior power. Choose its sign so that on
the dense open set \(a\ne0\) it is
\[
\omega_A=\frac{ds\wedge dt\wedge dY}{a},\qquad
\omega_B:=dx_1\wedge dx_2\wedge dx_3\wedge dz
       =c_0\,\omega_A\wedge d\sigma,
\qquad c_0\in\mathbb C^*.
\tag{3}
\]
The apparent denominator in this open-set formula does not define
a pole of \(\omega_A\): the form is the restriction of the global
determinant-line generator just constructed. Equivalently, on any
open set where another partial of \(L\) is invertible, the usual
signed complementary differential divided by that partial describes
the same generator.

The constant assertion in (3) uses the full actual presentation.
Since \(B=A[\sigma]\), the form \(\omega_A\wedge d\sigma\) is a
global generator of \(\det\Omega^1_{B/\mathbb C}\). The original
polynomial-coordinate volume is another global generator, so their
ratio is a unit of \(B\). But \(B^*=\mathbb C^*\). Comparing only
rational forms over \(K\), or generators after inverting \(a\),
would not justify this conclusion.

## 3. The original-coordinate wedge calculation

Write \(J=\operatorname{Jac}_S(p,h)=p_s h_t-p_t h_s\in S\).
Differentiating \(x_{\rm good}=M(p)(\sigma,Y,h)^t\) and wedging
with \(dp\) removes every term arising from differentiation of
\(M(p)\). Thus
\[
\begin{aligned}
dp\wedge dh\wedge d\sigma\wedge dY
 &=\kappa^{-1}dp\wedge dx_1\wedge dx_2\wedge dx_3
   =-\kappa^{-1}\alpha\,\omega_B,\\
dp\wedge dh\wedge d\sigma\wedge dY
 &=J\,ds\wedge dt\wedge d\sigma\wedge dY
   =-aJ\,\omega_A\wedge d\sigma,\\
\alpha&=C\,aJ,\qquad C=\kappa/c_0\in\mathbb C^*.
\end{aligned}
\tag{4}
\]
The first displayed minus sign moves \(dz\) past the three good
differentials; the second exchanges \(d\sigma\) and \(dY\).
Changing the convention for the residue generator only changes
the nonzero constant \(C\). The computation is an equality of
rational differential forms on the actual domain, and hence gives
the stated equality of its polynomial elements. In particular
\(J\ne0\) and \(a\mid\alpha\) already in \(S\).

## 4. The explicit intrinsic field

Define a derivation on the presentation by
\[
\begin{gathered}
\mathcal D_0(S)=0,\qquad
\mathcal D_0(Y)=a,\qquad
\mathcal D_0(D)=F_Y(Y),\\
\mathcal D_0(aD-F(Y))=0,\qquad
\mathcal D_0|_{K[Y]}=a\partial_Y,\qquad
N=-C\,\beta(p)J\,\mathcal D_0.
\end{gathered}
\tag{5}
\]
The relation check makes \(\mathcal D_0\) an actual derivation of
\(A\), not just a rational vector field. Every element of
\(A\subset K[Y]\) is killed by a sufficiently high iterate of
\(a\partial_Y\), so \(\mathcal D_0\) is locally nilpotent on \(A\).
Its invariant ring is \(A\cap K=S\), using the exact kernel of
the nonzero original intrinsic \(N\).

To obtain the last equality, compare the two \(K\)-derivations
on \(Y\) and on \(K\): their ratio is
\(-\alpha\beta(p)/a=-C\beta(p)J\). The equality then holds on
all of the actual subring \(A\). In particular its multiplier lies
in \(S\), with no residual rational denominator.

## 5. Primitivity, with all divisor gates retained

First \(A\) is a UFD: factorization of an element of \(A\) in
the polynomial UFD \(A[\sigma]\) has only \(\sigma\)-degree-zero
factors, and primality contracts. Its units are \(\mathbb C^*\).
Every irreducible \(\pi\in S\) remains irreducible in \(A\).
Indeed, a factorization \(\pi=vw\) in \(A\) puts both factors in
\(\ker N=S\) by factorial closure. Therefore \(\pi\) is prime
in \(A\), and \(\pi A\cap S=\pi S\).

Suppose \(\pi\mid a\), and put
\(k_\pi=\operatorname{Frac}(S/(\pi))\). The nonzero generic
divisor fiber is a domain and has the exact presentation
\[
A\otimes_S k_\pi
 =k_\pi[y,d]/(\overline F(y)),\qquad
0\ne\overline F\in k_\pi[y],\quad
\overline F\text{ irreducible of positive degree},\qquad
\overline{F_Y}\ne0\text{ in this quotient}.
\tag{6}
\]
Nonvanishing of \(\overline F\) follows from the primitive content
condition in (1). It cannot be a nonzero constant, since that
would make the fiber zero. Its irreducibility follows from the
domain quotient. Characteristic zero then gives a nonzero
derivative of smaller degree, proving the final assertion in (6).
This permits a nontrivial finite residue-field extension; no
geometric irreducibility or section is being inferred.

The values of \(\mathcal D_0\) on the algebra generators generate
the ideal \((a,F_Y)A\). Any prime common divisor of those two
values must divide \(a\), whose prime factors in \(A\) are the
irreducible factors \(\pi\in S\). Equation (6) excludes each one.
Consequently
\[
\gcd_A\mathcal D_0(A)=1,\qquad
\gcd_A N(A)\ \doteq\ \beta(p)J,
\qquad
\operatorname{div}_S(\alpha)
 =\operatorname{div}_S(a)+\operatorname{div}_S(J).
\tag{7}
\]
Here \(\doteq\) means equality up to a nonzero complex unit, and
the gcd of derivation values can be computed from any finite set
of algebra generators. Thus \(\mathcal D_0\) is primitive.

## 6. Consequences and limits

The denominator \(a\) is constrained by the actual original
derivative: \(a\mid p_z\). In particular, if \(p_z\in\mathbb C^*\),
then \(a\) is a unit and (1) recognizes \(A=S[Y]\simeq\mathbb C^{[3]}\).
If the selected \(N\) itself is primitive, (7) instead forces
\(\beta(p)J\in\mathbb C^*\); it does not force \(a\) to be a unit.

Primitivity means absence of a common prime divisor of the values.
It is not the unit-ideal condition \((a,F_Y)A=A\). Thus this proof
does not show that \(\mathcal D_0\) is fixed-point-free, that it
has a slice, or that the affine modification is trivial. Nor
does it identify \(S\) with \(\mathbb C[p,h]\), including when
\(J\) happens to be constant.

The full retained [curve89](constant-acceleration-curve-speed-pass89.md),
[conical-normal89](constant-acceleration-conical-normal-pass89.md),
[pole-support89](constant-acceleration-pole-support-pass89.md), and
[open conormal90](nonconical-open-free-derivation-pass90.md) arguments
were read for comparison. They supply related split-module,
prime-divisor and actual conormal-unit mechanisms, but do not
state the specific global factorization (4) for variable joint-curve
acceleration. This is a bounded comparison of retained notes,
not a claim of literature novelty.

Root proposed the canonical-volume comparison and independently
reconstructed it and the primitive normalization. Jet supplied
the explicit wedge orientation and written divisor argument.
The fresh primary-source scope is the split-conormal passage of
Stacks tag 00T1 cited above, not a new proof of its deeper
dependencies. No numerical checker is used to certify this
argument. No file through pass126 is changed.
