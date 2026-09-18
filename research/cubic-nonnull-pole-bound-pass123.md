# A stronger polynomial divisibility bound in the non-null cubic case

In the supplied actual non-null cubic framework, the square of the
third speed Y divides the cube of the second speed P. Consequently
Y divides g squared minus one with full multiplicity, every entry of
YQ is polynomial, and the potential coefficient aY is already in
the invariant plane ring S. These strengthen the radical restriction
and the contraction aY squared in S from122.

The proof uses the original-coordinate potential identity123. It
does not assume that the normal ratio h is a polynomial coordinate
or generates its full first-integral field. The remaining cubic
case and the arbitrary-frame entry problem are not settled here.

## 1. Actual hypotheses

Retain the full hypotheses of
[the non-null divisor proof122](cubic-nonnull-divisor-restriction-pass122.md)
and [the scalar potential123](cubic-nonnull-potential-pole-pass123.md).
In particular B=C[x1,x2,x3,z]=A[u], E=partial_u, and
S=ker(N|A)=C[s,t] is the full invariant plane. Its irreducible
polynomials remain prime in B, and pB intersect S=pS. Write

\[
\begin{gathered}
b=(g,P,Y)^t\in S^3,\quad h=P/Y,\quad
g^2-DY^2=1,\quad D=a_3h^3+a_2h^2+a_1h+a_0,\quad a_3\ne0,\\
L=\mathbb C(H)\supseteq\mathbb C(h),\quad
[L:\mathbb C(h)]<\infty,\quad a,c\in L,\quad q,\lambda\in\mathbb C^*,\\
Q=\begin{pmatrix}
-1&0&0\\
0&3a_3h+a_2&(-3a_3h^2+a_1)/2\\
0&(-3a_3h^2+a_1)/2&a_3h^3+a_0
\end{pmatrix},\\
z+\frac q2 x^tQx+qC_0x_1
 =\lambda\frac gY+c-qa'x_2-q(a-ha')x_3,
\quad C_0\in\mathbb C .
\end{gathered}
\tag{1}
\]

Primes mean the extension of d/dh. Rationality L=C(H) is the
retained first-integral field in
[normal forms121, Sections1 and3](cubic-axis-scalar-normal-forms-pass121.md).
It is not an added equality L=C(h). The matrix in (1) follows by
substituting the cubic D into its canonical normal form.

For any irreducible p dividing Y, the122 theorem gives p dividing
P and g squared minus one. Hence g has residue either 1 or -1.
The p-adic valuation on Frac(S) extends with the same normalization
to the pB-adic valuation on Frac(B). All original coordinates are
regular there. Reductions below are in Frac(B/pB).

## 2. Derivative orders at a pole of h

Suppose nu(h)=-d<0 for the selected valuation, where d>0.
Every element of L regular for nu has complex residue by the
finite-place lemma122. If nu(H)<0, choose tau=1/H. Otherwise
choose tau=H-Hbar, whose valuation is positive because Hbar is
complex. In either case L=C(tau) and nu(tau)=e>0.

Writing rational functions as Laurent series in tau therefore gives
h=c_h tau to the power -n times a unit with constant term one,
where d=ne and n is positive. For a nonzero f in L of nonzero
valuation, differentiating its first Laurent term and dividing by
dh/dtau gives

\[
\nu(f')=\nu(f)+d\quad\text{if }\nu(f)\ne0,
\qquad \nu(f')\ge\nu(f)+d\quad\text{in all cases}.
\tag{2}
\]

The convention is nu(0)=infinity. If f has valuation zero, its
constant term differentiates to zero, and its next term has positive
tau order; this proves the inequality, including constant f.
Only rational Laurent expansions in an explicitly chosen parameter
are used, not an unproved analytic or algebraic integration.

Put gamma=a-ha'. If nu(a')<0, (2) implies nu(a)<-d.
The leading exponent r=-nu(a)/d is then greater than one.
The leading coefficient of ha' relative to a is r, so that
gamma has nonzero leading coefficient 1-r. Thus

\[
\nu(a')<0\quad\Longrightarrow\quad
\nu(\gamma)=\nu(a)=\nu(a')-d<\nu(a').
\tag{3}
\]

This implication explicitly handles the potential resonance a
proportional to h: that resonance has a' regular, so it is not
among the cases asserted in (3).

## 3. A pole larger than the allowed ratio is impossible

Set b_p=nu(Y)>0 and a_p=nu(P)>0. If b_p>a_p, then
d=b_p-a_p>0. Suppose for contradiction that b_p<3d.
Equivalently 2b_p>3a_p.

Choose a nonzero coefficient f among h cubed, gamma and c having
minimum valuation, omitting a zero gamma or c. Write nu(f)=-m.
Then m is at least 3d. Divide the last identity of (1) by f.
All its coefficients are regular. The coefficients of x2 squared
and x2x3 vanish on reduction, since their pole orders are at most
d and 2d. The coefficient of x2 also vanishes: if a' is regular
this is immediate, and otherwise (3) puts its valuation strictly
above that of gamma, hence strictly above nu(f).

The coefficients of z, x1 and x1 squared vanish as well. The
reciprocal term lambda g/Y vanishes because its pole order is b_p,
which is strictly less than 3d and hence less than or equal to m.
The only surviving relation is

\[
\frac{q a_3}{2}\overline{h^3/f}\,\overline{x_3}^{\,2}
 +q\overline{\gamma/f}\,\overline{x_3}
 -\overline{c/f}=0 .
\tag{4}
\]

All three displayed coefficients are complex by the finite-place
lemma. At least one is nonzero, because one of h cubed, gamma or
c was chosen as f. Their degrees as polynomials in x3 are distinct,
so this is a nonzero polynomial over C. If it is a nonzero constant,
there is already a contradiction. Otherwise x3bar is algebraic over
C and hence equals a complex constant k.

Thus p divides x3-k in B. Since x3-k is an original affine-linear
coordinate it is irreducible, and p is a nonunit, so they are
associates. Applying E contradicts Ep=0 and E(x3-k)=Y nonzero.
This is a global polynomial contradiction after reduction, not an
application of E after setting Y equal to zero.

The strict regime is therefore excluded. For b_p>a_p one must
have b_p at least 3(b_p-a_p), or 2b_p at most 3a_p. If instead
b_p is at most a_p, the same final inequality is automatic. Hence

\[
2\nu_p(Y)\le3\nu_p(P)\quad\text{for every irreducible }p\mid Y,
\qquad Y^2\mid P^3\text{ in }S .
\tag{5}
\]

At equality the reciprocal term need not vanish after reduction.
Its residue is not asserted to be complex; (4) is not an argument
against that boundary or against the opposite strict regime.

## 4. Polynomial consequences and a stronger contraction

The same inequalities imply Y divides P squared. Define
J=P cubed/Y squared and I=P squared/Y, both in S. The norm
identity and the canonical matrix give

\[
\begin{gathered}
\frac{g^2-1}{Y}=a_3J+a_2I+a_1P+a_0Y\in S,\qquad
YQ\in\operatorname{Mat}_3(S),\\
\ell:=-b^tQ=
\left(g,-\frac{3a_3I+2a_2P+a_1Y}{2},
            \frac{a_3J-a_1P-2a_0Y}{2}\right)\in S^3,\\
\ell b=1,\quad \ell b_h=\ell b_Y=0,\quad
\ell x=u+\rho,\quad \rho=C_0g+aY,\qquad aY\in S .
\end{gathered}
\tag{6}
\]

For the last assertion, applying the row ell to the actual
reconstruction gives rho=ell x-u in B. It was already in K,
the base fraction field, so E and N kill it. Their full common
kernel in B is S. Subtracting C0g proves aY in S. Equivalently
this is the same full-kernel contraction used in122, now with a
polynomial dual row made available by (5).

No claim that a itself, c, Q or h is polynomial follows from these
identities. In particular aY in S is stronger than aY squared in S
but is not the missing global realization or cancellation theorem.

## Sources and verification scope

The scalar potential and finite-place argument are proved in the
linked123 and122 notes. The standard finite-residue background is
consistent with the Stacks Project,
[Lemma15.113.2, tag09E5](https://stacks.math.columbia.edu/tag/09E5).
Its statement and short proof were freshly read. The derivative
order argument above is written out using the retained rational
field L=C(H), so it does not depend on a separate Puiseux theorem.
The external source is not a cancellation result or a novelty claim.

Symbolic checks of matrix expansion and the dual row can verify
finite identities. They do not establish the all-primes valuation
argument, original-coordinate irreducibility, or the actual frame
hypotheses. Independent AI reviews are not human expert review or
formal proof checking. Files through122 are unchanged.
