# Polynomial coefficients in the non-null potential row

In the supplied actual non-null cubic framework, the three additional
coefficients Ya', Pa' and Yc belong to the invariant polynomial ring S.
Together with the preceding pole bound, this makes the entire potential
identity polynomial after multiplication by Y. This is a necessary
identity of the actual frame, not a recognition or exclusion theorem.

## 1. Inputs and the target coefficients

Retain the actual hypotheses and conclusions of
[potential-pole123](cubic-nonnull-potential-pole-pass123.md) and
[pole-bound123](cubic-nonnull-pole-bound-pass123.md). In particular,

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad S=\mathbb C[s,t],\quad
K=\operatorname{Frac}S,\quad L=\mathbb C(H)\subset K,\\
[L:\mathbb C(h)]<\infty,\quad h=P/Y\notin\mathbb C,\qquad
(g,P,Y)\in S^3,\quad Y\ne0,\\
\rho=C_0g+aY,\quad a,c\in L,\quad q,\lambda\in\mathbb C^*,\quad
C_0\in\mathbb C,\\
z+\frac q2x^tQ(h)x+qC_0x_1
 =\lambda g/Y+c-qa'x_2-q(a-ha')x_3,\\
aY\in S,\qquad Y^2\mid P^3,\qquad YQ(h)\in\operatorname{Mat}_3(S).
\end{gathered}
\tag{1}
\]

The entries of Q(h) are complex polynomials in h of degree at most
three. A prime denotes the extended h-derivative. Every irreducible
p of S remains prime in B, and pB intersect S=pS. The corresponding
valuations on K and Frac(B) have the same normalization. These are
retained actual prime and full-kernel statements, not assumptions
about arbitrary coefficient models.

Fix such a p, write nu for its valuation and m=nu(Y), and use
nu(0)=infinity. Since Y is polynomial, m is nonnegative. The
existing contraction aY in S gives nu(a) at least -m. We show
that Ya', Pa', and Yc are regular at every p.

## 2. Finite places of h and derivative orders

First suppose h is regular at p. If its residue is nonconstant,
the valuation is trivial on C(h) and hence on its finite algebraic
extension L, by the elementary minimal-polynomial proof in
[horizontal-divisor123, Section2](cubic-nonnull-horizontal-divisor-pass123.md).
Then a', c and h are regular, which proves all three required
regularities at this p.

Otherwise the residue of h is a complex constant h0. Put
delta=h-h0 and e=nu(delta)>0. The restriction to L is now a
nontrivial finite-place valuation. Every regular element of L
has complex residue: apply the finite-place lemma122 to
1/(h-h0), which has a pole and generates the same smaller field
C(h). In the retained rational field L=C(H), choose tau=H-Hbar
if H is finite at this place, and tau=1/H otherwise. Then
nu(tau)>0 and rational Laurent expansions in tau are available.
The first nonzero term of delta has positive order. Comparing
the leading terms of df/dtau and dh/dtau gives

\[
\nu(f')=\nu(f)-e\quad\text{if }\nu(f)\ne0,\qquad
\nu(\delta f')\ge\nu(f)\quad\text{for every }f\in L.
\tag{2}
\]

For a unit f its constant leading term differentiates to zero;
the next term has positive order, which proves the second
inequality also in that case. Constants and zero use the stated
infinity convention. This permits ramification: a regular f can
have a pole in f', and no unramifiedness has been assumed.

Define the actual linear coordinate X=x2-h0*x3 and the scalar
B0=a-delta*a'. Equation(2) and aY in S imply

\[
\nu(B_0)\ge\nu(a)\ge-m,\qquad
a'x_2+(a-ha')x_3=a'X+B_0x_3,\qquad
E X=P-h_0Y\ne0.
\tag{3}
\]

The last inequality follows because h is nonconstant as an
element of K, not merely because it is nonconstant on a chosen
divisor.

## 3. A more singular linear coefficient forces a coordinate to collapse

Suppose either nu(a') or nu(c) is less than -m. Choose f to be
a nonzero member of {a',c} of minimum valuation. Divide the
potential identity in (1), expressed using (3), by f.

All terms involving z, x1, and the quadratic matrix vanish on
reduction: h is regular, so their coefficients before division
are regular. The term B0*x3 vanishes by (3). The reciprocal
term also vanishes, since nu(g/Y) is at least -m and nu(f)<-m.
The remaining equation is

\[
q\overline{a'/f}\,\overline X-\overline{c/f}=0,
\qquad \overline{a'/f},\overline{c/f}\in\mathbb C,
\qquad (\overline{a'/f},\overline{c/f})\ne(0,0).
\tag{4}
\]

The residue coefficients are complex by the finite-place argument
in Section2. If the coefficient of X is zero, this is already an
impossible nonzero constant equation. Otherwise Xbar is a complex
constant k. Since the kernel of B to its residue field at pB is
pB, the prime p divides X-k in B. The latter is an original
affine-linear coordinate and hence irreducible, so p and X-k
are associates. Applying E contradicts Ep=0 and (3).

Consequently nu(a') and nu(c) are both at least -m. This proves
Ya' and Yc regular. Because h is regular, Pa'=hYa' is regular
as well. The proof includes p not dividing Y, for which m=0,
and p dividing Y over a finite constant value of h.

## 4. Poles of h

It remains to consider nu(h)=-d<0. Write n=nu(P), so d=m-n>0;
in particular p divides Y. The pole-bound theorem gives 3d at
most m. The Laurent derivative estimate at infinity, proved in
Section2 of that theorem, gives

\[
\begin{gathered}
\nu(a')\ge\nu(a)+d\ge-m+d=-n,\qquad
\nu(a-ha')\ge\nu(a)\ge-m,\\
\nu(Pa')\ge0,\qquad \nu(Ya')\ge d>0,
\qquad \nu(Q_{ij})\ge-3d\ge-m .
\end{gathered}
\tag{5}
\]

If nu(c)<-m, it is the unique term of smallest valuation in the
potential identity: the original coordinates are regular; the
matrix terms, the two linear scalar terms, and g/Y all have
valuation at least -m. A uniquely smallest term cannot occur
in a vanishing sum. Thus nu(c) is at least -m, proving Yc regular
here too. No residue of g/Y is claimed to be complex in this case.

## 5. Global polynomial identity and scope

All the coefficients under consideration lie in K. Since the
polynomial UFD S is the intersection of its localizations at
irreducible primes, the preceding checks prove

\[
\begin{gathered}
Ya',\quad Pa',\quad Yc\ \in S,\\
Yz+\frac q2x^t(YQ)x+qC_0Yx_1
 =\lambda g+Yc-q(Ya')x_2-q(aY-Pa')x_3 .
\end{gathered}
\tag{6}
\]

Every coefficient in the last equation is now polynomial in the
actual invariant plane. This does not say that a', c, Q or h is
polynomial, and it does not permit division of that equation by
Y inside B. The further lower-volume relation for a and c in the
companion potential note is not used in this proof.

The valuation and original-coordinate arguments are written proofs;
there is no new numerical test or source theorem in this note.
No arbitrary-frame realization or general cancellation conclusion
is asserted. Files through122 are unchanged.
