# Two split coefficient gates exclude every nondegenerate algebraic square branch

Status: working algebraic-function lemma. The simultaneous necessary
equations below have no solution with their nonzero denominator gates.
This is stronger than rejecting the single rational candidate192.
Application to an actual frame still uses the separately proved
square-form and scalar-Jacobian reductions193.

## 1. Exact differential statement

Let \(K/\mathbb C(t)\) be a finite field extension with the unique
extension of \(d/dt\). Its derivative constants are \(\mathbb C\).
Put \(d=t^{-4}-1\). For a nonzero \(f\in K\), define

\[
R=f^{-1},\qquad D_f=d'f/4+df',\qquad
\Delta=RR''/2-(R')^2,\qquad
\nu=\frac{(f'')^2}{8f^3D_f}.
\tag{1}
\]

Assume \(f''D_f\ne0\), so every quantity divided by below is nonzero,
including \(\Delta=-f''/(2f^3)\), \(R,\nu\), and

\[
p_2=-\frac{\Delta}{R\nu},\qquad
p_1=\frac{2R'}R-\frac{\nu'}\nu.
\tag{2}
\]

Here \(p_1\) denotes the rho-linear coefficient in the completed-square
polynomial, not the entire coefficient of its independent variable.
Define

\[
\begin{aligned}
L_3&=\frac{R\nu''/4-R'\nu'/2-\nu R''/2
                  -R\nu p_1^2/2-\nu^2p_2}{3Rp_2},\\
J_3&=-RL_3'+R'L_3-\nu\nu'/2
                    -p_1(3RL_3+\nu^2).
\end{aligned}
\tag{3}
\]

The lemma is that the equations

\[
\mathscr E_d(f):=20D_f f'''-3d(f'')^2-12f''D_f'=0,
\qquad J_3=0
\tag{4}
\]

are incompatible with \(f''D_f\ne0\).

Equation \(\mathscr E_d(f)=0\) is the first square-completion
coefficient gate derived in
[split ODE192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md).
The additional \(J_3=0\) is supplied by
[square Jacobian193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md):
the U-squared coefficient makes the potential ell a cubic polynomial
in rho, with rho-cubed coefficient \(L_3\), and the rho-cubed
coefficient in the remaining U-linear term is \(J_3\).
An actual constant Jacobian forces that remaining term to be
rho-constant. These geometric facts are distinct from the
algebraic lemma proved here.

## 2. Local expansions at infinity are valid over the exact field

Choose a place of \(K\) above \(t=\infty\).
In its completed field the residue field is \(\mathbb C\).
A uniformizer can be chosen with \(t=s^{-e}\), for a positive
integer e: take an e-th root of the original unit factor.
Thus every element has an injective Laurent expansion in powers of
\(t^{1/e}\), with exponents bounded above. Its derivative is the
termwise derivative
\(\partial_t=-s^{e+1}\partial_s/e\).
This is the local construction written in Section 6 of
[quartic reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md).
It makes no rationality assumption on \(K\).

In the following calculations, \(o(t^\mu)\) means a series whose
exponents are all strictly smaller than \(\mu\).
The discrete exponent group gives a positive gap to the next exponent.
Differentiation lowers every nonconstant exponent by one.
A constant leading term must therefore be separated explicitly,
as is done below.

Expanding the first equation of (4) gives

\[
\mathscr E_d(f)=
5(d'f+4df')f'''-15d(f'')^2-15d'f'f''-3d''ff''.
\tag{5}
\]

The contribution of the constant part \(-1\) of d is
\(-20f'f'''+15(f'')^2\).
Every term from the \(t^{-4}\) part of d is four powers lower
when the leading derivatives are nonzero.

Write \(f=a t^\mu+o(t^\mu)\), \(a\in\mathbb C^*\), \(\mu\in\mathbb Q\).
For \(\mu\ne0\), the coefficient at exponent \(2\mu-4\) in (5) is

\[
-5a^2\mu^2(\mu-1)(\mu-5).
\tag{6}
\]

Terms involving lower exponents are strictly lower, and the
\(t^{-4}\) perturbation of d cannot change this coefficient.
Consequently the only possible leading exponents are
\(\mu=0,1,5\).

## 3. Leading exponent one forces f to be affine

Suppose \(\mu=1\).
Subtract \(at\) and the coefficient b of \(t^0\) if it occurs.
If a nonzero remainder h remains, let
\(h=c t^\lambda+o(t^\lambda)\),
where \(c\ne0,\ \lambda<1,\ \lambda\ne0\).
Every affine \(at+b\) satisfies \(\mathscr E_d=0\).

The linear contribution from the constant part of d is
\(-20a h'''\), with nonzero coefficient

\[
-20ac\,\lambda(\lambda-1)(\lambda-2)
\quad\hbox{at exponent }\lambda-3.
\tag{7}
\]

The quadratic h-terms have exponent at most \(2\lambda-4\),
which is strictly smaller because \(\lambda<1\).
Terms involving \(t^{-4}\) have exponent at most \(\lambda-7\)
in their affine-linear part, or still smaller in the quadratic part.
Thus nothing cancels (7), a contradiction.
There is no remainder, and injectivity of the completion gives
\(f=at+b\) in K. This violates \(f''\ne0\).

## 4. Leading exponent zero leaves one possible first correction

Suppose \(\mu=0\), so \(f=b+h\), \(b\in\mathbb C^*\).
The case h=0 violates \(f''\ne0\).
Otherwise write \(h=c t^\lambda+o(t^\lambda)\), \(\lambda<0\).

The leading nonlinear contribution from the constant part of d is

\[
-5c^2\lambda^2(\lambda-1)(\lambda-5)
 t^{2\lambda-4}.
\tag{8}
\]

The leading contribution linear in h is from
\(5d'bh'''-3d''bh''\), namely

\[
-20bc\,\lambda(\lambda-1)(\lambda+1)
 t^{\lambda-8}.
\tag{9}
\]

If \(-4<\lambda<0\), then \(2\lambda-4>\lambda-8\), and the
coefficient in (8) is nonzero.
If \(\lambda<-4\), then \(\lambda-8>2\lambda-4\), and the
coefficient in (9) is nonzero.
The lower terms of h cannot change either leading coefficient.
Thus \(\lambda=-4\).
At exponent \(-12\), (8) and (9) sum to
\(1200c(b-3c)\), forcing

\[
f=b+\frac b3t^{-4}+o(t^{-4}).
\tag{10}
\]

It is not necessary to classify the remaining lower terms of this
series. The second equation of (4) will exclude all of them at once.

## 5. The second gate excludes leading exponent five

Suppose \(f=a t^5+o(t^5)\).
The nonzero leading terms derived successively from (1)--(3) are

\[
\begin{gathered}
R=a^{-1}t^{-5}+o(t^{-5}),\qquad
D_f=-5a t^4+o(t^4),\\
\Delta=-10a^{-2}t^{-12}+o(t^{-12}),\qquad
\nu=-10a^{-2}t^{-13}+o(t^{-13}),\\
p_2=-a t^6+o(t^6),\qquad
p_1=3t^{-1}+o(t^{-1}),\qquad
L_3=-55a^{-3}t^{-21}+o(t^{-21}).
\end{gathered}
\tag{11}
\]

For an explicit check of the cancellation-sensitive \(L_3\) numerator,
the three terms
\(R\nu''/4,\ -R'\nu'/2,\ -\nu R''/2\)
have coefficients \(-455,325,150\), in units \(a^{-3}t^{-20}\).
Their sum is 20.
The next two terms \(-R\nu p_1^2/2\) and \(-\nu^2p_2\)
have coefficients 45 and 100.
The numerator is therefore \(165a^{-3}t^{-20}+o(t^{-20})\);
the denominator \(3Rp_2\) is \(-3t+o(t)\).
This proves the \(L_3\) entry in (11).

The four terms in \(J_3\), in their order in (3), have coefficients
\(-1155,\ 275,\ 650,\ 195\), in units \(a^{-4}t^{-27}\).
Hence

\[
J_3=-35a^{-4}t^{-27}+o(t^{-27})\ne0.
\tag{12}
\]

All leading coefficients used for multiplication and division are
nonzero. Arbitrarily ramified lower terms of f have smaller exponents
and cannot change (12). This excludes \(\mu=5\).

## 6. The second gate excludes the constant-limit correction

For (10), it is important not to differentiate only the constant
leading term of R. The needed expansions include

\[
\begin{gathered}
R=b^{-1}-\frac1{3b}t^{-4}+o(t^{-4}),\qquad
R'=\frac4{3b}t^{-5}+o(t^{-5}),\qquad
R''=-\frac{20}{3b}t^{-6}+o(t^{-6}),\\
D_f=\frac b3t^{-5}+o(t^{-5}),\qquad
\Delta=-\frac{10}{3b^2}t^{-6}+o(t^{-6}),\\
\nu=\frac{50}{3b^2}t^{-7}+o(t^{-7}),\qquad
p_2=\frac b5t+o(t),\qquad
p_1=7t^{-1}+o(t^{-1}).
\end{gathered}
\tag{13}
\]

In the \(L_3\) numerator, \(R\nu''/4\) contributes
\(700/(3b^3)t^{-9}\), and \(-R\nu p_1^2/2\) contributes
\(-1225/(3b^3)t^{-9}\).
The remaining three terms have exponent at most \(-13\) at
their leading order and therefore do not contribute at \(-9\).
Since \(3Rp_2=(3/5)t+o(t)\), it follows that

\[
L_3=-\frac{875}{3b^3}t^{-10}+o(t^{-10}).
\tag{14}
\]

In \(J_3\), the terms \(-RL_3'\) and \(-3p_1RL_3\)
are the only contributions at exponent \(-11\).
Their coefficients are \(-8750/(3b^4)\) and \(6125/b^4\).
Every other displayed term in (3) has smaller exponent.
Consequently

\[
J_3=\frac{9625}{3b^4}t^{-11}+o(t^{-11})\ne0.
\tag{15}
\]

This excludes (10), including all possible lower algebraic-series
corrections, not just the exact rational function \(3+t^{-4}\).

Equations (6)--(15) exhaust all possible leading exponents.
The only surviving first-equation solutions compatible with a
vanishing second gate would be affine, whereas the nondegenerate
square branch requires \(f''\ne0\).
This proves the differential incompatibility lemma.

## 7. Consequence and verification boundary

Together with the general scalar-Jacobian gate193, this lemma
excludes both nondegenerate square-completion alternatives produced
by the actual three-alternatives reduction193.
That conclusion must be composed with the full hypotheses of those
notes, including the exact coefficient field and actual scalar
determinant. It is not an obstruction from the first ODE alone.

The rational \(t^5+3t\) remains a valid counterexample to an
affine-only claim for the first equation. It is excluded here
precisely because it fails the additional \(J_3=0\) gate.
No source192 needs alteration.

This note proves no arbitrary coordinate-entry theorem and no
unrestricted cancellation theorem. Its local expansions are a
human-readable working proof, not proof-assistant certification.
No historical novelty, expert review, public submission or
external contact is claimed.

