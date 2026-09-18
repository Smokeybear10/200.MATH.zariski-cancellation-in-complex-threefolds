# The moving linear parameter in the three-output cubic residual

The remaining degree-five output-span case does not force its displayed
linear parameter to be invariant. It forces the opposite: that
parameter moves. Its normalized speed, however, has only two possible
forms. One makes the normalized slice affine in that ambient linear
coordinate. The other makes the nice-field coefficient affine in that
coordinate and the normalized slice. In both cases the single-factor
replica \(gZ\), rather than only \(g^4Z\), is polynomial.

These are consequences of the actual degree-five frame and a published
three-variable nice-derivation theorem. This note proves the all-degree
coefficient classification and its good-column exclusion. It does not
assert that a relative linear relation has invariant coefficients or
that a polynomial replica automatically has a slice.

## 1. Exact actual-frame input

Use the notation and full hypotheses of the frozen
[degree-five proof](cubic-degree-five-pass40.md). Thus
\(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(E\) has a polynomial slice,
\(0\ne g\in\ker E\), and \(\delta=E/g\) is an LND on
\(B_g\). The already proved field is
\[
Z=T_e+\frac{\sigma}{3}T_d+R T_c,
\qquad R=\frac{\sigma^2}{12}+\frac{\tau}{3\lambda},
\tag{1}
\]
where
\[
\delta\sigma=1,\quad \delta\tau=0,\quad
[\delta,Z]=[E,Z]=0,\quad Zg=Z\sigma=Z\tau=0,
\quad Z^2x_i=0.
\tag{2}
\]
Here \(\lambda\in\mathbb C^*\), the vectors \(c,d,e\) are
complex constants, \(c_4=d_4=0\), and \(e_4=\lambda\).
The field \(\mathcal W=g^4Z\) is a polynomial nice LND.
Assume now that \(c,d,e\) are complex-linearly independent.

Let \(w\) be a nonzero linear form annihilating their span.
It is an actual ambient linear coordinate, and
\[
Zw=\mathcal Ww=0,\qquad \delta^3w=0.
\tag{3}
\]
The last assertion follows from the exact vector identity
\[
\delta^3x=c\sigma^2/2+d\sigma+c\tau/(2\lambda)+e.
\]

For the three original good partials, put \(W_i=[\delta,T_i]\).
The full-frame coefficient identities are
\[
W_i\sigma=0,\qquad
W_i\tau=-\frac\lambda2T_i\sigma\quad(i\le3),
\qquad T_i\sigma\ne0\text{ for at least one }i\le3.
\tag{4}
\]
Their last assertion was proved rationally in the degree-five note:
otherwise \(\sigma\in\mathbb C(x_4)\), while
\(\delta\sigma=1\) and \(\delta^3x_4=\lambda\) would make
\(x_4\) a cubic in its rational inverse parameter. In particular,
(4) shows that \(\tau\) is nonconstant.

## 2. A relative relation does not have invariant coefficients

Complete \(w\) to a complex linear coordinate system and extend
scalars to \(K=\mathbb C(w)\). The field \(\mathcal W\) is
a nonzero nice LND on the actual three-variable polynomial ring
over \(K\). The established three-variable nice theorem supplies
a nonzero \(K\)-linear invariant form.[^nice]
Applying \(\mathcal W\) to it, and cancelling \(g^4\), gives
\[
A(w)+B(w)\sigma+C(w)R=0,
\qquad A,B,C\in\mathbb C(w),\quad (A,B,C)\ne(0,0,0).
\tag{5}
\]
Constant factors such as the coefficient \(1/3\) of \(T_d\)
have been absorbed into \(B\). This is a relation over a moving
field: no coefficient in (5) is assumed \(E\)-invariant.

In fact \(\delta w\ne0\). If it were zero, applying
\(\delta^2\) to (5) would give \(C/6=0\). Applying
\(\delta\) next gives \(B=0\), and then \(A=0\), a
contradiction.

## 3. A rational differential lemma

The following elementary fact is the only rational differential
equation used below:
\[
v\in\mathbb C(w),\qquad vv''-3(v')^2=0
\quad\Longrightarrow\quad v\in\mathbb C.
\tag{6}
\]
The zero function is allowed. For a nonzero rational function with
a pole of order \(-n>0\) at a finite point, write its leading
term as \(a(w-w_0)^n\), \(n<0\). The leading coefficient in
the left side of (6) is
\(-a^2n(2n+1)\), which is nonzero for every such integer.
Thus there are no finite poles, and \(v\) is polynomial.
If its degree is \(n>0\), the same leading-coefficient computation
at infinity is nonzero. Therefore its degree is zero.
The rationality premise excludes the nonrational square-root
solutions of this differential equation.

## 4. The relation with no quadratic coefficient

If \(C=0\) in (5), then \(B\ne0\) and
\(\sigma=-A(w)/B(w)\in\mathbb C(w)\).
Since \(\delta\sigma=1\), the derivation preserves this
rational function field and its constant field is \(\mathbb C\).
Integrating \(\delta^3w=0\) inside that field gives
\[
w=\nu\sigma^2/2+\kappa\sigma+\mu,
\qquad \nu,\kappa,\mu\in\mathbb C.
\]
But \(\sigma\in\mathbb C(w)\) and the displayed expression
give \(\mathbb C(w)=\mathbb C(\sigma)\). A polynomial of
degree two cannot generate this same rational field. Hence
\[
\nu=0,\qquad \kappa\ne0,\qquad
w=\kappa\sigma+\mu,\qquad \delta w=\kappa.
\tag{7}
\]
In particular \(\sigma\) is polynomial in this branch, even
when the original \(g\) is nonconstant.

## 5. All rational relations with a quadratic coefficient

Suppose \(C\ne0\). Normalize (5) as
\[
\tau=a(w)+b(w)\sigma-\frac\lambda4\sigma^2,
\qquad a,b\in\mathbb C(w),\qquad \ell=\lambda/2\ne0.
\tag{8}
\]
The pair \((\sigma,\tau)\) is algebraically independent:
\(\tau\) is nonconstant and invariant, whereas
\(\delta\sigma=1\). In characteristic zero, an element
algebraic over the invariant field cannot have derivative one.
Since (8) puts \(\tau\) in \(\mathbb C(w,\sigma)\), the
pair \((w,\sigma)\) is likewise algebraically independent.

Differentiating (8), with all coefficient derivatives retained,
gives
\[
H=a'(w)+b'(w)\sigma,\qquad
V:=\delta w=\frac{\ell\sigma-b(w)}{H}.
\tag{9}
\]
The denominator \(H\) is not zero. Otherwise independence gives
\(a'=b'=0\), and differentiating (8) would require
\(b-\ell\sigma=0\), which is impossible.

On \(\mathbb C(w,\sigma)\), write
\(\mathcal D=\partial_\sigma+V\partial_w\).
The exact condition \(\delta^3w=0\) is
\(\mathcal D^2V=0\). Clearing the denominator, set
\[
\mathcal N=H^5\mathcal D^2V\in\mathbb C(w)[\sigma].
\tag{10}
\]
Its degree is at most five. Direct differentiation gives
\[
[\sigma^5]\mathcal N
=\ell^3\bigl(-b'b'''+3(b'')^2\bigr).
\tag{11}
\]
Apply (6) to \(v=b'\). Thus
\(b=\beta w+b_0\), with \(\beta,b_0\in\mathbb C\).

### Nonzero slope of b

If \(\beta\ne0\), the next coefficient is
\([\sigma^4]\mathcal N=-\ell^3\beta a'''\), so \(a'''=0\).
With that identity imposed, the coefficient of degree three is
\[
[\sigma^3]\mathcal N
=3\ell\bigl(\ell a''+\beta^2\bigr)^2.
\tag{12}
\]
Therefore
\(a=-\beta^2w^2/(2\ell)+a_1w+a_0\).
Substitution into the full expression, not only its top coefficients,
gives
\[
\mathcal D^2V=
\frac{-3\beta\ell^3(\beta b_0+\ell a_1)^3}
 {(-\beta^2w+\beta\ell\sigma+\ell a_1)^5}.
\tag{13}
\]
Thus \(a_1=-\beta b_0/\ell\), and
\[
\delta w=\kappa:=\ell/\beta\ne0,
\quad
\tau=-\frac\lambda4(\sigma-w/\kappa)^2
       +b_0(\sigma-w/\kappa)+a_0.
\tag{14}
\]

### Zero slope of b

If \(\beta=0\), the denominator is \(H=a'\ne0\), and the
coefficient of degree three in (10) is
\(\ell^3(-a'a'''+3(a'')^2)\).
Apply (6) to \(v=a'\). Then
\(a=\alpha w+a_0\), with \(\alpha\in\mathbb C^*\).
Set \(\nu=\ell/\alpha\ne0\) and
\(\kappa=-b_0/\alpha\). The full expression now vanishes,
and the exact form is
\[
\delta w=\nu\sigma+\kappa,
\qquad
\tau=\frac{\lambda}{2\nu}
 \left(w-\kappa\sigma-\frac\nu2\sigma^2\right)+a_0.
\tag{15}
\]
Equations (14) and (15) exhaust (8). They were obtained by
rational-function identities at all degrees, not by bounded sampling
of possible coefficients.

## 6. The full good frame excludes the constant-speed quadratic relation

The algebraic case (14) is incompatible with (4). Indeed
\(w\) is linear and \(\delta w=\kappa\) is constant, so
\[
W_iw=\delta(T_iw)-T_i(\delta w)=0.
\]
Together with \(W_i\sigma=0\), formula (14) then gives
\(W_i\tau=0\) for every good index. This contradicts (4)
for an index with \(T_i\sigma\ne0\).

Consequently the actual three-output residual has exactly the
following alternative:

1. \(w=\kappa\sigma+\mu\), with \(\kappa\ne0\), as in (7).
2. Equation (15) holds with \(\nu\ne0\).

In particular \(\delta w\ne0\), and in both cases
\(\delta^2w\) is a complex constant. Equivalently, the original
polynomial action satisfies \(E^2w=\nu g^2\), where \(\nu=0\)
in the first case. This does not make \(w\) invariant.

## 7. The first polynomial replica already suffices for denominator clearing

In case (7), \(\sigma\in B\). Put \(p=E x_4\).
The original definition of \(\tau\) gives
\(g\tau=p-\lambda g\sigma^2/2\). Therefore
\[
gZ=gT_e+\frac{g\sigma}{3}T_d+
 \left(\frac{p}{3\lambda}-\frac{g\sigma^2}{12}\right)T_c
\quad\hbox{is polynomial}.
\tag{16}
\]

In case (15), set
\[
t=g\sigma=\frac{Ew-\kappa g}{\nu}\in B.
\tag{17}
\]
The relation in (15) cancels the quadratic term in (1):
\[
R=\frac{w-\kappa\sigma}{6\nu}+\frac{a_0}{3\lambda}.
\]
Thus
\[
gZ=g\left(T_e+
 \left(\frac{w}{6\nu}+\frac{a_0}{3\lambda}\right)T_c\right)
 +t\left(\frac13T_d-\frac{\kappa}{6\nu}T_c\right)
\quad\hbox{is polynomial}.
\tag{18}
\]
Here \(E(t)=g^2\). In either case \(gZ\) is a polynomial
nice LND: local nilpotence descends from \(B_g\), and niceness
uses \(Zg=0\). It commutes with \(E\) and sends \(x_4\)
to \(\lambda g\). No claim that this derivative is a unit
has been made.

The subsequent actual coordinate changes and recognition are a
separate obligation. The results here use a supplied actual
degree-five frame and do not produce such a frame on an arbitrary
unknown cylinder.

## Verification and source scope

The top rational differential coefficients, both full substituted
branches, and the nonzero-denominator gates are explicit enough for
independent reconstruction. The rational pole and infinity argument
proves the all-degree assertion; finite coefficient checks do not
replace it. The good-column exclusion uses the actual conjugated
coordinate partials, not an arbitrary formal matrix pencil.

The standalone [six-method checker](three_output_cubic_speed_checks_pass41.py)
was written independently of this derivation. Its initial run passed
in 3.467 seconds; the complete source was independently read and all
six methods rerun successfully in 3.517 seconds. The controls include
the full rational numerator, the reduced branches, and negative
examples showing why rationality and the field-equality gate matter.

The relative nice-derivation theorem is an established input. Its
linear relation is not presented as a new classification theorem.
This note makes no novelty, expert-review, Lean-verification, or
general cancellation claim.

[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Theorem 3.1(i), PDF p. 5, complete statement directly read. It is stated over an arbitrary characteristic-zero field and attributed there to Z. Wang, Proposition 4.6. Here the actual coefficient field is \(\mathbb C(w)\); no invariance of that field under \(E\) is presumed.
