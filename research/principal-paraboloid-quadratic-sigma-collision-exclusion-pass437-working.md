# A collision excludes the remaining quadratic sigma parameter

Working necessary result: the quadratic-sigma branch of the
constant-second-slope plane reduction cannot occur in the full
actual264 chart. The proof uses the entire polynomial-ring
return at every value of the original coordinate X, not
just a nonzero generic Jacobian.

An explicit degree-eight polynomial must have a root outside
a specified quadratic's zero set. Such a root produces either
two distinct points with the same three actual coordinates,
or a point at which all three coordinate derivatives vanish.
Both contradict generation of the whole polynomial line.

This excludes one supplied actual-chart branch. It is not an
arbitrary-entry or unrestricted cancellation theorem.

## 1. Actual hypotheses and the precise branch

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\(\mathcal B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\),
the exact time profile \((1,2,2,2)\), the entire initial kernel
\((\mathsf X^2\mathsf Z-\mathsf Y^2)\), the selected nonzero
\(N=[u^4]\partial_Z|_A\), and the actual localization and both
returns. In particular,
\[
\begin{gathered}
a_0=EX\ne0,\quad L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Na_0=Nt=Ns=0,\\
O=L[A]=L[v]=L[y,z,w],\quad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\quad
J_{t,s,v}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
The coefficient partials commute and fix v. Assume
\[
k=s+f,\qquad f_s=n_s=0,\qquad f'''\ne0,\qquad
e=\ell_s\in\mathbb C^* .
\tag{2}
\]
Primes denote the exact t-derivative in the retained finite
coefficient field, not an assumed rational parametrization.

The branch excluded in this note has a generator x of the
whole line ring and the shape
\[
\boxed{
O=L[x],\quad \sigma=a x^2+b,\quad
y=\gamma\sigma^2+\beta\sigma+\delta+\kappa x,\quad
a\gamma\kappa\ne0.
}
\tag{3}
\]
All displayed coefficients belong to L. The letter a in(3)
is unrelated to the actual speed \(a_0\) in(1).
No assertion that x belongs to the original ring A, or
that Nx=1, is needed.

For orientation, completing the square in the constant-slope
plane primitive \(\Phi=A_0U^2+B(P)U+C(P)\) gives
\[
x=2A_0y+B(\sigma),\qquad
x^2=d_1\sigma+d_0,\qquad
A_0d_1\ne0,\qquad [P^2]B=f'''/2 .
\]
Thus its linear-discriminant branch has(3), with
\[
a=1/d_1,\quad b=-d_0/d_1,\quad
\gamma=-f'''/(4A_0),\quad \kappa=1/(2A_0).
\tag{4}
\]
The proof below assumes the exact shape(3), rather than asserting
that every candidate has this shape.

## 2. Literal potentials and the all-X return

The complete first three potentials from
[430](principal-paraboloid-arbitrary-longitudinal-plane-reduction-pass430-working.md)
give
\[
\begin{aligned}
\theta&=\frac{y^2+(f''\sigma+n')y+(f'''/6)\sigma^3
                    +(n''/2)\sigma^2-\ell_t\sigma-h}{e},\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n'\sigma,
\end{aligned}
\tag{5}
\]
where h is the genuine third level in L. The literal rows are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s+f)X+t^2X^2,\quad
W=w+\theta X+sX^2 .
\tag{6}
\]
No coefficient of(5) is dropped, and no restriction on h or
its moving derivatives is used.

Since \(X=a_0u+x_0\) with \(x_0\in A\) and \(a_0\in L^*\),
the actual slice and localization give
\[
L[\mathcal B]=O[u]=L[x,X]=L[X,Y,Z,W].
\tag{7}
\]
Extend coefficients to an algebraic closure \(\overline L\).
For every \(\lambda\in\overline L\), specializing(7) gives
\[
\boxed{
\overline L[Y(\lambda),Z(\lambda),W(\lambda)]
            =\overline L[x].
}
\tag{8}
\]
The value lambda is only a coefficient-field value of X.
This evaluation is not an original-coordinate change over C.
Base extension is legitimate because(7) is an identity of
generated polynomial algebras before evaluation.

## 3. Two exact collision conditions

Choose two candidate values \(p,q\in\overline L\) of x.
Write
\[
S=p+q,\quad \Sigma=\sigma(p)+\sigma(q),\quad
\Pi=\sigma(p)\sigma(q).
\]
We shall arrange \(S\ne0\). If \(p\ne q\), then
\(\sigma(p)-\sigma(q)=aS(p-q)\ne0\). Put
\[
r=\frac{y(p)-y(q)}{\sigma(p)-\sigma(q)},\qquad
\lambda=-r .
\tag{9}
\]
This makes the two values of \(Y(\lambda)\) agree.
For repeated \(p=q\), use the same definitions by divided
differences: since \(S=2p\ne0\), \(\sigma'(p)=aS\ne0\),
and \(r=y'(p)/\sigma'(p)\). Then \(Y(\lambda)'(p)=0\).
Derivatives here mean derivatives with respect to x, not
coefficient t-derivatives. Every such derivative holds the
chosen lambda fixed. The same divided-difference identities
below cover both cases.

Define
\[
\begin{aligned}
F&=y(p)+y(q)+\frac{f''}{2}\Sigma+n',\\
D&=\frac{n''}{2}+e-\frac{(f'')^2}{4},\\
E_0&=ef'-\ell_t-\frac{f''n'}2,\\
G&=\frac{f'''}6(\Sigma^2-\Pi)+D\Sigma+E_0 .
\end{aligned}
\tag{10}
\]
Divide differences by \(\sigma(p)-\sigma(q)\), or divide
x-derivatives by \(\sigma'(p)\) in the repeated case. At
\(X=\lambda\), the exact rows(5),(6) give
\[
\begin{aligned}
Z^{[1]}&=\theta^{[1]}+\Sigma+f',\\
W^{[1]}-\lambda Z^{[1]}&=-F,\\
eZ^{[1]}&=G+F(r+f''/2).
\end{aligned}
\tag{11}
\]
Here a superscript [1] denotes this normalized difference,
not a coefficient partial.

For a direct check of the last equality, subtract the third
potential at the two points:
\[
\begin{aligned}
e\theta^{[1]}
={}&\{y(p)+y(q)+f''\Sigma/2+n'\}r\\
&+\frac{f''}{2}\{y(p)+y(q)\}
+\frac{f'''}6(\Sigma^2-\Pi)+\frac{n''}{2}\Sigma-\ell_t.
\end{aligned}
\]
Substitute \(y(p)+y(q)=F-f''\Sigma/2-n'\) and add
\(e(\Sigma+f')\). The result is precisely(11).
Consequently \(F=G=0\) produces equal values of all three
coordinates if p and q are distinct, or zero derivatives of
all three if they coincide.

## 4. Reduction to a degree-eight polynomial

The parametrization(3) gives two identities:
\[
\begin{aligned}
y(p)+y(q)&=\gamma(\Sigma^2-2\Pi)+\beta\Sigma
                         +2\delta+\kappa S,\\
\Pi&=\frac{(aS^2-\Sigma)^2}{4}+abS^2 .
\end{aligned}
\tag{12}
\]
The second follows from \(\sigma=a x^2+b\), using the sum
and product of p,q. It includes the repeated case.

Because \(f'''\ne0\), the condition G=0 is equivalent to
\[
\Pi=\Sigma^2+\frac{6D}{f'''}\Sigma+\frac{6E_0}{f'''}.
\tag{13}
\]
Substituting this expression into F=0 determines the sum
\[
\boxed{
S=T(\Sigma):=
\frac{\gamma\Sigma^2-
(\beta+f''/2-12\gamma D/f''')\Sigma
-(2\delta+n')+12\gamma E_0/f'''}{\kappa}.
}
\tag{14}
\]
This is a polynomial of exact degree two, with leading
coefficient \(\gamma/\kappa\ne0\).

Using the second identity of(12), the equation G=0 is now
equivalent to
\[
\boxed{
R(\Sigma):=-a^2T(\Sigma)^4
+2a(\Sigma-2b)T(\Sigma)^2+R_2(\Sigma)=0,
}
\tag{15}
\]
where
\[
R_2(\Sigma)=3\Sigma^2+\frac{24D}{f'''}\Sigma
                         +\frac{24E_0}{f'''} .
\tag{16}
\]
The exact degree of R is eight, with leading coefficient
\(-a^2(\gamma/\kappa)^4\ne0\).
The only additional requirement for our collision is
\(T(\Sigma)\ne0\).

## 5. The root-avoidance lemma

We prove the elementary statement needed for(15):
over an algebraically closed characteristic-zero field, if
\(a\ne0\), \(\deg T=2\), and \(R_2\) is a quadratic with
leading coefficient three, then
\[
R=-a^2T^4+2a(z-2b)T^2+R_2
\]
has a root at which T is nonzero.

Suppose otherwise. All eight roots of R, counted with
multiplicity, would be supported on at most two roots of T.
Some root \(r_0\) would therefore have multiplicity at least four.
Since \(R-R_2\) is divisible by \(T^2\), both \(R_2(r_0)\)
and \(R_2'(r_0)\) vanish. Hence
\[
R_2(z)=3(z-r_0)^2.
\tag{17}
\]
No other root of T can be a root of R, because at such
a root \(R=R_2\ne0\). Therefore
\(R=c(z-r_0)^8\) for some nonzero c.

Put \(u=z-r_0\). As \(T(r_0)=0\), write
\(T=u(t_1+t_2u)\), where \(t_2\ne0\).
The \(u^7\) coefficient of R is
\(-4a^2t_1t_2^3\): the term \(2a(z-2b)T^2\) has degree
at most five, and \(R_2\) has degree two.
The identity \(R=cu^8\) forces \(t_1=0\).
But now \(T=t_2u^2\), and the \(u^2\) coefficient of R
is exactly three by(17), again contradicting \(R=cu^8\).
This proves the lemma, including a possible double root of T.

## 6. Recovery of the forbidden pair

Choose a root \(\Sigma_0\) of(15) with
\(S_0=T(\Sigma_0)\ne0\), as supplied by Section5.
Set
\[
P_0=\frac{aS_0^2+2b-\Sigma_0}{2a},
\]
and choose p,q to be the roots of
\[
\xi^2-S_0\xi+P_0=0
\tag{18}
\]
in \(\overline L\).
Then \(p+q=S_0\), and their two sigma values have sum
\(\Sigma_0\) and product given by(12).
Equation(15) makes G=0; equation(14) then makes F=0.
The value lambda in(9) is defined because \(aS_0\ne0\).

If p and q are distinct, (11) gives the same values of
\(Y(\lambda),Z(\lambda),W(\lambda)\) at these distinct points.
Every polynomial expression in these three generators would
take equal values there, but x does not.
This contradicts the whole generation(8).

If p=q, equations(9),(11) give zero derivatives of all three
generators at p. The chain rule makes the derivative of every
polynomial expression in them zero at that point.
Since the x-derivative of x is one, this also contradicts(8).
The repeated-root case is not an unresolved exception.

## 7. Conclusion, dependencies and verification

The shape(3) is impossible under the actual hypotheses(1),(2).
In particular, the linear-discriminant quadratic-sigma branch
described in(4) is excluded. The collision calculation itself
only uses \(e f'''\ne0\), the exact potentials, the shape(3),
and whole all-X generation; the constancy of e is needed
in the prior classification, not in this final obstruction.

The proof does not infer an original coordinate from x,
apply a double-cover recognition theorem to the wrong projection,
or substitute rational-field generation for(8).
It does not treat the constant-sigma case or provide the
normalization and recognition steps for a larger synthesis.

Root freshly read264 completely in f4c178+0d8352 and430 completely
in0d8352. The writing guide was read through EOF in those same
two calls. Fresh unsaved exact calculation a1b21d, completed
as c01f94, reconstructed every identity(11)--(16), including the
pair-product formula, the degree-eight leading coefficient,
the degree-seven coefficient in Section5, and the surviving
degree-two coefficient three. Every tested residual was zero.

Jet independently checked the root-avoidance lemma and supplied
a second proof using congruence modulo \(T^2\) and logarithmic
derivatives at two distinct roots. These are conceptual checks
before complete saved-source review. Independent source-review
verdicts are recorded separately in the research ledger.

No saved checker was executed, imported, compiled or rerun.
The unsaved symbolic identities supplement the written argument;
they are not human-expert or proof-assistant verification.
No historical novelty, actual-existence, unrestricted cancellation
solution, public submission or external contact is claimed.

