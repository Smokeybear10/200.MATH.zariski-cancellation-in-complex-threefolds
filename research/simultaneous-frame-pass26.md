# Simultaneous two-column changes: a one-LND completion criterion

Date: 2026-09-13.

This bounded pass leaves the forced one-column operation of pass 25.
It proves a usable criterion for a genuinely simultaneous polynomial
coordinate frame: over a Q-domain, two commuting polynomial relative
fields with unit determinant are coordinate partials if just one of
them is locally nilpotent. The proof uses classical two-variable LND
triangularization and the slice theorem, with the coefficient-ring
descent checked explicitly.

There is also an explicit nonlinear two-shear operation, including
the necessary changes to the other coordinate partials, and an exact
intrinsic-height calculation. No existence or termination theorem
for a successful sequence on every unknown A has been obtained.
General cancellation remains unresolved. No novelty, expert-review,
or Lean-verification claim is made.

## 1. The exact relative setup

Let S be a domain containing Q and let B=S[u,v]. In applications
S=C[z_1,z_2], where u,v,z_1,z_2 are actual ambient coordinates on
B=C^[4]. Consider S-derivations

\[
W_1=a\partial_u+b\partial_v,
\qquad W_2=c\partial_u+d\partial_v,
\qquad J=ad-bc\in S^*.
\tag{1}
\]

The coefficients a,b,c,d may be arbitrary polynomials in u,v over S.
They need not be invariant under either field. Thus (1) permits
nonlinear simultaneous changes, not just the single subtraction
\(U-hT\) treated in the
[previous exact gate](commuting-leading-pass25.md).

The determinant condition only says that the two fields form a
polynomial basis of Der_S(B). It is not yet a coordinate assertion.

## 2. Commutation supplies polynomial dual primitives

Assume \([W_1,W_2]=0\). Define relative one-forms

\[
\omega_1=J^{-1}(d\,du-c\,dv),
\qquad
\omega_2=J^{-1}(-b\,du+a\,dv).
\tag{2}
\]

They satisfy \(\omega_i(W_j)=\delta_{ij}\). The formula for the
exterior derivative evaluated on W_1,W_2 gives

\[
d\omega_i(W_1,W_2)
=W_1(\omega_i(W_2))-W_2(\omega_i(W_1))
 -\omega_i([W_1,W_2])=0.
\]

Since the fields form a B-basis, each omega_i is closed. Polynomial
closed one-forms on this relative affine plane are exact. More
explicitly, for a closed form \(L(u,v)du+M(u,v)dv\), the polynomial

\[
H(u,v)=\int_0^u L(t,0)\,dt+\int_0^v M(u,t)\,dt
\tag{3}
\]

has differential equal to the form. The integrals are coefficientwise
polynomial antiderivatives in S, which is why S contains Q.
Closedness gives \(M_u=L_v\), verifying H_u=L and H_v=M.

We therefore obtain polynomials P,Q in B with

\[
W_1(P)=1,\quad W_1(Q)=0,\quad
W_2(P)=0,\quad W_2(Q)=1.
\tag{4}
\]

Their Jacobian determinant is J^{-1}. At this stage they are only
a Keller pair, meaning a polynomial pair with unit Jacobian. The
words “polynomial coordinates” have not been justified yet.

## 3. One complete field is enough

**Completion criterion.** Under (1) and commutation, the following
are equivalent:

- W_1 is locally nilpotent;
- W_2 is locally nilpotent;
- both are locally nilpotent;
- the primitives P,Q in (4) satisfy B=S[P,Q].

In the last case they are algebraically independent over S and
W_1=partial_P, W_2=partial_Q. Consequently the full ambient frame
can be replaced by the actual partials in P,Q,z_1,z_2. No
Jacobian-conjecture assumption enters the criterion.

**Proof.** It is enough to start with W_1 locally nilpotent. Pass to
K=Frac(S), which is allowed because W_1 fixes S. On K[u,v], the
classical two-variable triangularization theorem applies. Because
W_1 has the polynomial slice P, that triangularization gives

\[
K[u,v]=K[t,P],\qquad W_1=\partial_P,
\qquad\ker W_1=K[t].
\tag{5}
\]

Here is the slice implication explicitly. In triangular coordinates
an LND has the form \(\alpha\partial_x+\beta(x)\partial_y\),
with alpha in K. If alpha is nonzero, integrating beta gives an
invariant coordinate t and a translation coordinate. If alpha is
zero, a polynomial slice forces beta to be a nonzero constant,
since beta divides the value of every polynomial. In either case
any other slice P differs from a fixed translation coordinate by
an element of K[t], so (5) follows.

By commutation, W_2 preserves K[t]. Write W_2(t)=g(t) and Q=q(t).
The last equation of (4) becomes

\[
g(t)q'(t)=1\quad\text{in }K[t].
\tag{6}
\]

Both factors are nonzero constants. Thus Q is affine linear in t,
and W_2 is partial_Q on K[P,Q]. In particular it is locally
nilpotent there. This local nilpotence descends to B: for every
b in B some iterate W_2^N(b) is zero after the injective
localization B -> K[u,v], hence it was already zero in B.
No field-coordinate formula is assumed to descend by itself.

Now use two successive slice decompositions over the original S.
Commutation and (4) give

\[
B=(\ker W_1\cap\ker W_2)[P,Q].
\tag{7}
\]

The common kernel is exactly S: an element killed by both fields
is killed by partial_u and partial_v, since their coefficient
matrix is invertible over B. In a polynomial ring over a Q-domain
this means the element lies in S. This proves B=S[P,Q].
The same derivative identities prove algebraic independence, or
one can read it off from the two polynomial slice decompositions.
The converse and the argument starting with W_2 are symmetric.

**Inherited ingredients.** Rentschler's two-variable theorem is
stated over an arbitrary characteristic-zero field in Derksen's
Theorem 2.13. His Proposition 4.6 gives the commuting-slices
decomposition used in (7). The criterion above applies those
classical facts and explicitly checks the passage from Frac(S)
back to S; it is not being asserted as a newly discovered
literature theorem. [Author's notes, pp. 4 and 6](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/09/LND1.pdf).

### What this would give for a tangent field

Suppose B=A[s]=C^[4], and a nonzero tangent LND V obtained from
the authoritative [intrinsic extraction](intrinsic-frame-repair-pass24.md)
can be expressed as W_1 in some actual relative plane B=S[u,v].
If it admits a polynomial W_2 satisfying commutation and (1), the
criterion produces P with V(P)=1. Because V(s)=0, its induced LND
on B/(s), identified with A, has slice the class of P.

Thus this is a sufficient simultaneous completion test for the
desired intrinsic sliced action. What is missing is the universal
existence of that relative coordinate plane and that commuting
unimodular complement. In particular a unit determinant requires
the coefficients of V to generate the unit ideal. Primitivity of
V alone does not provide this, and leading extraction does not
automatically provide freeness or properness.

## 4. Why the local-nilpotence hypothesis cannot be silently removed

For any polynomial pair P,Q in C[u,v] with Jacobian one, define

\[
W_1=Q_v\partial_u-Q_u\partial_v,
\qquad
W_2=-P_v\partial_u+P_u\partial_v.
\tag{8}
\]

Their determinant is one and they satisfy (4). They commute:
the bracket kills P,Q, which form a transcendence basis, and
C(u,v) is algebraic separable over C(P,Q). A derivation killing
the latter field also kills C(u,v). Equivalently one can compute
the bracket from the inverse Jacobian matrix.

If every such commuting unimodular pair had even one locally
nilpotent member, Section 3 would imply C[u,v]=C[P,Q] for every
Keller pair. Conversely a positive two-variable Jacobian statement
would make every pair (8) a pair of coordinate partials. Section 2
shows that every commuting unimodular frame arises in this way,
up to a nonzero constant Jacobian rescaling and primitive constants.

Therefore the proposed unconditional upgrade from integrability
and unimodularity to a complete polynomial coordinate action is
exactly a two-variable Jacobian-conjecture reformulation over C.
This is a reduction to an additional unproved assertion, not a
counterexample or a proof of that conjecture.

The connection is inherited: Derksen's Theorem 5.9 states the
inverse-Jacobian local-nilpotence criterion in arbitrary dimension.
The present note keeps the one-LND hypothesis that lets the
two-dimensional argument actually close. [Primary statement and proof, p. 8](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/09/LND1.pdf).

### Commutation is also an essential hypothesis

A determinant-one simultaneous polynomial basis with one LND can
still fail if its fields do not commute. For example, on C[u,v]
take

\[
V_1=\partial_u+u\partial_v,
\qquad
V_2=v\partial_u+(1+uv)\partial_v.
\tag{9}
\]

The determinant is one. V_1 is an LND, but
\([V_1,V_2]=uV_1\ne0\). In the actual coordinates
p=u, q=v-u^2/2, the other field is

\[
V_2=\partial_q+(q+p^2/2)\partial_p.
\tag{10}
\]

The p-degree of V_2^j(p) is j+1 and its leading coefficient is
\(j!/2^j\), so V_2 is not locally nilpotent. Although V_2(q)=1,
this does not give an additive action. The dual one-form for V_1
is not closed. This is a simultaneous-basis integrability control,
not a variant of the earlier forced c-squared subtraction.

## 5. A safe nonlinear two-column operation and its full inverse

There is a direct accepted operation when an explicit shear word
is available. In B=S[u,v], choose F in S[v] and G in S[P], and
set

\[
P=u+F(v),\qquad Q=v+G(P).
\tag{11}
\]

This changes both columns nonlinearly. Its inverse is

\[
v=Q-G(P),\qquad u=P-F(Q-G(P)).
\tag{12}
\]

With f=F_v(v) and g=G_P(P), the new partials are

\[
\partial_P=(1+fg)\partial_u-g\partial_v,
\qquad
\partial_Q=-f\partial_u+\partial_v.
\tag{13}
\]

If S=C[z_1,z_2] and the coefficients depend on its coordinates,
the remaining partials also change. Differentiating (12) while
P,Q are fixed gives

\[
\partial_{z_i}^{\rm new}
=\partial_{z_i}+(-F_{z_i}+fG_{z_i})\partial_u
 -G_{z_i}\partial_v.
\tag{14}
\]

Here F_{z_i} is taken at fixed v and G_{z_i} at fixed P, then
P=u+F(v) is substituted. These formulas, together with (12),
prove that all four fields commute and are LNDs. Their nilpotence
on old coordinates can be bounded by the corresponding degrees
of (12). A determinant computation alone is not the proof.

Finite compositions of such verified operations remain legitimate.
No claim is made that every ambient or relative coordinate change
is generated by the displayed operations, or that such a word
always lowers the height relevant to cancellation.

## 6. Exact intrinsic height and a successful descent control

Fix the original E=partial_s on B=A[s]. Let a_i be a finite set
of algebra generators for A. They can be taken as the finite
slice retractions of the original ambient coordinate functions.
Define deg_E(b) as the degree in s, with deg_E(0)=-infinity.
For a nonzero derivation W, its exact filtered degree is

\[
q_E(W)=\max\left\{\max_i\deg_E W(a_i),
                       \deg_E W(s)-1\right\}.
\tag{15}
\]

Indeed the right side gives a bound on every product of the a_i
and s, hence on A[s], and each listed generator realizes its
own lower bound. For an ambient coordinate partial q_E is at
least -1. For a full coordinate frame define

\[
H_E=\sum_{j=1}^4(q_E(T_j)+1)\in\mathbb Z_{\ge0}.
\tag{16}
\]

An accepted inverse-certified frame change with smaller H_E is
a genuine well-founded descent step. A sequence of such strict
steps cannot be infinite. This does not prove that another
strict step exists whenever the desired slice has not been found.
Nor does a smaller height alone certify that slice.

For a direct successful control take A=C[a,b,c], m,n>=2, and
the actual ambient coordinates

\[
u=a+s^m,\quad v=s+u^n,\quad b,c.
\tag{17}
\]

Their two active partials, expressed in a,s, are

\[
T_u=(1+mn\,u^{n-1}s^{m-1})\partial_a
        -nu^{n-1}\partial_s,
\quad
T_v=-ms^{m-1}\partial_a+\partial_s.
\tag{18}
\]

Consequently their q_E-values are mn-1 and m-1. The actual
coordinate changes

\[
(u,v)\longmapsto (u,v-u^n)=(u,s)
\longmapsto (u-s^m,s)=(a,s)
\tag{19}
\]

give full-frame heights

\[
m(n+1)+2\quad\longrightarrow\quad m+3
\quad\longrightarrow\quad3.
\tag{20}
\]

The untouched b,c partials each contribute one. At the endpoint
partial_a is an actual sliced tangent LND and E itself is the
vertical coordinate partial. The quadratic case of this frame
already appeared in the earlier filtration controls. This is a
successful height audit of a valid simultaneous word, not a new
family classification or a claimed universal reduction.

## 7. Exact remaining quantifier and checks

For arbitrary A[s]=C^[4], the unresolved assertion is an existence
statement. One would need to guarantee an actual relative-plane
presentation and commuting unit-determinant complement for a
tangent LND, or a suitable inverse-certified simultaneous change
that makes an intrinsic slice available. Neither nonzero leading
fields, primitive coefficient gcd, nor formal integrability alone
supplies those hypotheses. The rank-one limitation of pass 25 also
still applies to repairs that never create a new rational orbit
direction.

The standalone checker
[simultaneous_frame_checks_pass26.py](simultaneous_frame_checks_pass26.py)
imports only unittest and SymPy. It checks the full shear inverse,
all four new partials and their brackets, dual-form integration,
the determinant-one noncommuting control and its recurrence,
and the exact height sequence. Its finite examples do not replace
the proof of Section 3 or assert a universal search bound.

Run command:

```sh
/opt/anaconda3/bin/python research/simultaneous_frame_checks_pass26.py
```

All **12 unittest methods** passed in 0.252 seconds on 2026-09-13.
The first checker run exposed an incorrect test expectation about
which uncorrected base partial fails to commute: in the chosen
control old partial_t commutes with W_Q but not W_P. The test was
corrected to check the latter; no displayed identity or theorem
needed changing.

An independent agent reconstructed the one-LND completion proof,
including the arbitrary characteristic-zero fraction field, the
equation gq'=1, injective-localization descent, and the common
kernel S. No algebraic defect was found. This is an AI crosscheck,
not a human expert review or priority audit.
