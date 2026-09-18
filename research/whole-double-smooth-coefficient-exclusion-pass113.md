# Exclusion of a smooth first coefficient in the whole-double branch

The actual proper-image whole-double branch cannot have a nonzero first
base jet of h. This is a conditional exclusion within the supplied
constant-acceleration quadratic frame, not a proof that every cancellation
input admits that frame. The remaining proper branch must have nonzero h
in the square of the base maximal ideal. Its residual ideal (a,b) also
cannot equal that maximal ideal.

The proof uses a formal change of coefficients only to factor the actual
base scalar P. It does not descend a formal slice or commute a derivation
kernel with completion. The decisive geometric input is that P is a power
of one analytically irreducible prime.

## 1. Exact local assumptions

Retain the actual setup of
[product-index112, Section 1](whole-double-product-index-pass112.md).
The global input is a smooth complex threefold with polynomial cylinder,
a supplied canonical primitive locally nilpotent derivation N with full
invariant plane S, and the actual all-divisor quadratic degree bound.
Let R=S_m be the regular local base surface and A the corresponding
localization of the actual threefold. In the proper whole-double branch,

\[
\begin{gathered}
F_1=R\{1,r\},\quad F_2=R\{1,G,H\},\quad
r=aG+bH,\quad Nr=P=ah+bB_2\ne0,\\
NG=\varepsilon br+h,\quad NH=-\varepsilon ar+B_2,
\quad \varepsilon\in R^*,\\
J=(a,b)\text{ is }\mathfrak m\text{-primary},\quad
a,b,h\in\mathfrak m,\quad h\ne0,\quad \gcd(h,a)=1,\\
b^2\in(h)+a(a,b),\qquad
B_2\in\mathfrak m(h)+\mathfrak m(a^2)
          +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
A/\mathfrak mA=\mathbb C[c,G]/(G^2),\qquad
\bar N=\lambda G\partial_c,\quad\lambda\in\mathbb C^*.
\end{gathered}
\tag{1}
\]

The coefficient restrictions in (1) were proved by actual module
determinants and pure-residue contraction in product-index112, Sections
2--4. They are not a claim that arbitrary coefficients satisfying them
come from such a threefold. Both a and b are nonzero nonunits. In
particular P is a nonunit. Write Rhat for the m-adic completion of R.

## 2. The one-prime geometric input

[Ramified-completion113, Sections 2--3](whole-double-ramified-completion-descent-pass113.md)
proves the specific statement needed here:

\[
P=v p^e,\quad v\in R^*,\quad e\ge1,\qquad
p\in R\text{ irreducible},\qquad
\widehat R/(p)\text{ is a domain}.
\tag{2}
\]

For clarity, its dependence on the whole fiber is essential. Every
divisor of P has a degree-two constant field by the exact divisor
models107; a degree-one divisor has a slice and makes P a unit there.
All degree-two divisors lie in the actual product-complement curve.
The supported integral argument in
[dependency-audit96, Sections 3--5](irreducible-fiber-dependency-audit-pass96.md)
gives one source normalization point over each normalized base branch
when the whole reduced fiber is irreducible. The degrees of different
branches are pairwise coprime. Thus there is exactly one degree-two
branch among the divisors supporting P, and its base prime p has only
one normalized branch at m. Extra degree-one exceptional branches are
allowed.

The normalization V of R/(p) is finite and local, hence a DVR with
residue field C. Completing the finite inclusion R/(p) into V embeds
Rhat/(p) in Vhat, a power-series domain. This proves the final assertion
of (2). It does not infer analytic irreducibility from algebraic
irreducibility alone. Finite curve normalization and exact finite-module
completion are the standard inputs.[^normalization]

The topological input behind the supported integral argument is
Kaliman's curve factorization and quotient homology diagram, not his
free-action conclusion.[^kaliman] No free action is imposed on the
fixed double fiber in (1).

## 3. Reduction modulo a hypothetical smooth h

Suppose for contradiction that h is not in m squared. Then R/(h) is a
regular local ring of dimension one, hence an integrally closed DVR.
Coprimality in (1) makes the image of a nonzero. In its fraction field,
the relation for b squared gives a monic equation
(b/a)^2=v_1(b/a)+u_1 with u_1,v_1 in R/(h). Therefore b/a belongs to
R/(h). Lifting its value gives tau,k in R with b=a tau+h k. No
maximal-ideal restriction on tau or k is obtained or required.

Substituting this expression for b in the ideal bound for B2 in (1)
gives

\[
b=a\tau+hk,\qquad
B_2=h\eta+a^2\xi,\qquad
\eta,\xi\in\mathfrak m,
\quad\tau,k\in R.
\tag{3}
\]

Indeed m(ab) is contained in m(a squared)+m(h), and
m squared(b squared) is contained in the same sum after expanding
(a tau+h k) squared. The two other summands already have that form.

## 4. A coefficient shear in the completed base

Consider the polynomial over Rhat

\[
\Phi(T)=\eta T^2+(1+\xi ak-\eta\tau)T-\tau.
\tag{4}
\]

Modulo m it is T minus the residue of tau. Its derivative at that root
is one. There is a root t in Rhat with residue equal to that of tau.
An elementary construction suffices: start with any lift of the residue
root, and if the error lies in m to the n, subtract the error divided
by the unit derivative modulo m to the n+1. The quadratic error in
this correction lies in m to the 2n, hence in m to the n+1 for n at
least one. The compatible successive roots converge by completeness,
and polynomial continuity makes their limit a root. This works also
when the residue of tau is nonzero.

Set

\[
\begin{gathered}
u=1+\eta t\in\widehat R^*,\quad
k'=k/u,\quad h'=h+tB_2,\quad b'=b-ta,\\
(b'-h'k')u=-a\Phi(t)=0,\qquad
b'=h'k',\\
P=ah'+b'B_2=h'(a+k'B_2),\qquad
B_2u=\eta h'+a^2\xi.
\end{gathered}
\tag{5}
\]

Each identity follows by expanding (3)--(4). If desired this is the
invariant coefficient change G'=G+tH, but no algebraic element G' of
A is needed. Since B2 belongs to m squared, h' has the same nonzero
linear term as h. Thus h' is a parameter of the regular local ring
Rhat and generates a prime ideal.

The ideal (a,b') equals (a,b)Rhat and is mRhat-primary: a power of m
already lies in (a,b) in R. If h' divided a, the equality b'=h'k'
would put this primary ideal inside the height-one ideal (h'), which
is impossible. Thus a has a nonzero image modulo h'.

## 5. Two distinct prime factors contradict (2)

Using (5), reduce the second factor of P modulo h':

\[
\begin{gathered}
B_2\equiv a^2\xi/u\pmod{h'},\\
a+k'B_2\equiv
a\left(1+\frac{k'a\xi}{u}\right)\not\equiv0\pmod{h'}.
\end{gathered}
\tag{6}
\]

The parenthesis is a unit: a and xi are in the maximal ideal. The
quotient Rhat/(h') is a domain, and the image of a is nonzero. This
justifies the last nonvanishing, not merely a formal cancellation.
Also a+k'B2 is a nonunit, since a and B2 lie in the maximal ideal.
It is nonzero because P is nonzero.

Consequently (5) factors P into the prime h' and a nonzero nonunit
not divisible by h'. In the regular local UFD Rhat, the second factor
has a prime divisor distinct from h'. This contradicts (2), where p
remains prime in Rhat and P is a unit times a power of p. Therefore

\[
\boxed{\quad
\text{actual proper whole-double branch}
\quad\Longrightarrow\quad
0\ne h\in\mathfrak m^2.
\quad}
\tag{7}
\]

## 6. The residual ideal cannot be the maximal ideal

There is a second exclusion using the same one-prime input. Suppose
J=(a,b)=m. The two elements are then regular parameters. By (7), h is
in m squared. Write the first restriction of (1) as
b squared=s h+v a squared+w ab. Comparing homogeneous terms of degree
two in C[a,b] shows that h has order exactly two and that its initial
quadratic h2 has a nonzero b squared coefficient: its coefficient
times the residue of s equals one. In particular a and h2 are coprime.

The coefficient bound in (1) now puts B2 in m cubed. Thus P=ah+bB2
has order three with initial homogeneous form a h2. These distinct
tangent factors lift to a factorization in Rhat. Here is a direct
construction, without invoking a factorization theorem. Start with
L=a and H0=h2. If the current product agrees with P through degree
n minus one, let E_n be its degree-n error, with sign P minus product.
For every n at least four, write E_n=a V_(n-1)+h2 U_(n-2). Such
homogeneous polynomials exist: modulo a, the image of h2 is a nonzero
multiple of b squared, so it generates every homogeneous term of
degree at least two in C[b]. Add U_(n-2) to L and V_(n-1) to H0.
The error improves by one order; the product of the new corrections
has degree 2n minus three, greater than n. Subsequent corrections
converge in Rhat. Consequently

\[
\begin{gathered}
P=L H_0,\qquad L=a+O(\mathfrak m^2),\quad
H_0=h_2+O(\mathfrak m^3),\qquad L\nmid H_0,\\
\boxed{\quad\text{actual proper whole-double branch}
\quad\Longrightarrow\quad (a,b)\ne\mathfrak m.\quad}
\end{gathered}
\tag{8}
\]

Indeed L is a smooth prime. Divisibility of H0 by L would make its
initial form h2 divisible by a, which it is not. Both factors are
nonunits, contradicting (2). This excludes the maximal residual ideal,
not every m-primary ideal or every case where just one generator is
smooth. No new numerical test is used for this all-order argument.

## 7. Meaning and verification limits

By [conormal-chart112, equation (6)](whole-double-global-conormal-chart-pass112.md),
h having zero first base jet is equivalent, within the proper branch,
to zero first normal action in the constant leading weighted chart.
Thus the nonzero-first-normal proper branch is excluded. This assertion
does not depend on an original speed normal being nonzero. It retains
all the actual-frame and whole-fiber assumptions used in (1)--(2).

The zero-first-normal branch has not been excluded. In that branch
R/(h) need not be a DVR, so the integral element b/a need not descend
to R/(h). Even if a coefficient shear existed, h' would no longer be
a smooth prime by the argument above. These are exact points at which
this proof cannot simply be repeated.

The separate scalar-contraction and completed-kernel results in
ramified-completion113 are not inputs to this exclusion. Neither is
the optional formal conic slice in
[the two-method checker](whole_double_hensel_slice_checks_pass113.py).
That checker verifies polynomial identities and finite root liftings;
it cannot establish the one-prime geometry, all-order completion
arguments, or the theorem's actual-frame hypotheses. The written proof
is the argument for those quantifiers. Separate AI reconstructions are
not human expert review, Lean verification, or a novelty clearance.

[^normalization]: The Stacks Project,
    [normalization of curves, Lemmas 33.41.1--2](https://stacks.math.columbia.edu/tag/0C44)
    and [finite-module completion, Lemma 10.97.1](https://stacks.math.columbia.edu/tag/00MA).
    Complete selected statements and displayed proofs were read. The
    underlying Nagata and Artin--Rees theorems are standard dependencies,
    not newly proved here.

[^kaliman]: Shulim Kaliman, *Free C+-actions on C3 are translations*,
    [author-hosted primary paper](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
    Lemmas 2.1--2.2, Lemma 3.1, and Proposition 3.2 with its displayed
    proof and integral diagram, printed pages 2--8. These selected
    statements and proofs were reread. The supported local lattice
    deduction is reconstructed in dependency-audit96, not quoted as a
    theorem about h from this paper.
