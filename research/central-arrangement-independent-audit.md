# Independent audit of central-arrangement slice descent

No fatal gap was found in
[central-arrangement-slice-pass.md](central-arrangement-slice-pass.md).
The proof does not infer the individual curve ranks from a total-rank
calculation. Its integral residue map supplies the necessary stronger
statement, and that map has the asserted image. The common-point
normalization sequence and the localization used for the Chinese
remainder theorem are also valid.

This is an independent check of the written argument, not a claim of
human expert review or historical priority. The audit covers the theorem
as stated: an original LND slice with coefficient a product of powers
of \(d\ge2\) distinct concurrent affine lines in two variables, with
unrestricted remainder degree. The source states \(d\ge3\) and
explicitly includes \(d=2\) by the same argument.

## 1. Initial reductions and topology of the complement

An original slice gives \(T=K[F]\), where \(K=\ker D\). It really
does make \(F\) one-stably a coordinate: in
\(T[s]=K[F,s]\), the ring \(K[s]\) is abstractly a polynomial ring
because substitution of \(s\) for \(F\) identifies it with \(T\).
Hence \(T[s]=K[s][F]\) is a polynomial presentation containing
\(F\). This does not assume cancellation for \(K\).

For a stable coordinate, every \(X_\lambda\) times an affine space
is affine space. The projection to \(X_\lambda\) is a homotopy
equivalence, so \(X_\lambda\) is contractible. Smoothness also
descends from the product. Integral Poincaré duality on this smooth
complex threefold gives precisely the stated compact-support groups.

After choosing \(\ell_0=x\), the remaining distinct central lines
can be written \(y-\alpha_jx=0\). No other line is vertical. The map
\((x,y,z)\mapsto(x,y/x,z)\) identifies the complement with

\[
 \mathbb C^*\times
 (\mathbb C\setminus\{\alpha_1,\ldots,\alpha_{d-1}\})
 \times\mathbb A^1.
\]

Künneth gives \(H^1=\mathbb Z^d\) and
\(H^2=\mathbb Z^{d-1}\), with no higher ordinary cohomology.
The compact-support groups in degrees four, five, and six then follow
by duality. There are no missing torsion terms.

The argument excluding a constant plane restriction is valid. If
\(q_i=b_i\), then for \(\lambda\ne b_i\) the function
\(\ell_i\) has no zero on \(X_\lambda\), hence is an algebraic
unit. Its restriction to the explicitly parametrized complement is
nonconstant. Stable polynomiality forces the units to be
\(\mathbb C^*\), a contradiction.

Every nonconstant polynomial on \(\mathbb A^2_{\mathbb C}\) has
nonempty fibers: restrict it to a line on which it is nonconstant.
Thus none of the \(C_i\) is silently omitted. Generic smoothness
allows one common regular value for the finitely many restrictions.

The closed-open sequence gives

\[
 H_c^1(C)=\mathbb Z^{d-1},\qquad H_c^2(C)=\mathbb Z^d.
\]

Finite intersections do not alter the direct sum of top compact-support
groups. Since each of the \(d\) smooth nonempty curves contributes
at least one copy of \(\mathbb Z\), the total rank \(d\) makes
each connected. A connected smooth algebraic curve is irreducible.
The coefficient multiplicities do not affect these reduced subsets.

## 2. Nonconstant axis and the common-point normalization sequence

Let \(e=\deg h\), and choose \(\lambda\) away from the finitely
many critical values of \(h\). All \(d\) curves pass through the
same \(e\) points, and there are no other pairwise intersections.
Their disjoint union is the normalization of the reduced curve \(C\).

At each shared point the constant-sheaf map is

\[
 \mathbb Z\longrightarrow\mathbb Z^d,
 \qquad a\longmapsto(a,\ldots,a),
\]

whose cokernel is \(\mathbb Z^{d-1}\). Consequently

\[
 0\to\mathbb Z_C\to\bigoplus_i\mathbb Z_{C_i}
 \to\bigoplus_{p\in S}\mathbb Z_p^{d-1}\to0
\]

is exact. All curve components are noncompact, so their degree-zero
compact-support cohomology vanishes. The resulting exact segment is

\[
 0\to\mathbb Z^{e(d-1)}\to H_c^1(C)
 \to\bigoplus_iH_c^1(C_i)\to0.
\]

In particular, the gluing term is \(e(d-1)\), not
\((e-1)(d-1)\). Subtracting a reduced degree-zero term here would
incorrectly mix ordinary cohomology with compact supports. For example,
two affine lines meeting once already have \(H_c^1=\mathbb Z\).
No transverse-intersection assumption is required for this constant-
sheaf calculation.

Since \(H_c^1(C)\) has rank \(d-1\), this forces \(e=1\) and
\(H_c^1(C_i)=0\). The smooth affine-curve formula
\(\operatorname{rank}H_c^1=2g+r-1\), with \(r\ge1\), makes
every \(C_i\) an affine line. The chosen regular fiber is reduced,
so its equation is not a nontrivial power. Plane-line rectification
therefore makes each \(q_i\) a coordinate polynomial.

The relative-coordinate lemma used next is valid. If \(q(t,z)\)
is a plane coordinate and \(q(0,z)=az+b\), choose a companion
\(W\). The old line \(t=0\) becomes the polynomial graph
\(W=r(q)\). Its irreducible equation is associated to
\(W-r(q)\), so \((t,q)\) is a coordinate pair. A one-variable
polynomial automorphism over \(\mathbb C[t]\) is affine with
constant nonzero slope. Thus \(q=az+B_i(t)\).

Finally, distinct irreducible linear forms dividing the same polynomial
force their product to divide it in the UFD. Comaximality of their
ideals is neither asserted nor needed here. The normal form
\(H=az+B+QR\) follows.

## 3. The finite inverse, including its iteration count

Work in \(A=\mathbb C[x,y]\), and put
\(q(z)=az+B+QR(z)\). Let \(N=\max m_i\). Then
\(Q^N\) is divisible by \(P\). Starting at
\(I_0=(T-B)/a\), define

\[
 I_{j+1}=\frac{T-B-QR(I_j)}a.
\]

Let \(E_j=q(I_j)-T\). Directly,

\[
 I_{j+1}-I_j=-E_j/a,
 \qquad E_{j+1}=Q\bigl(R(I_{j+1})-R(I_j)\bigr).
\]

Polynomial differences are divisible by the difference of their
arguments. Since \(E_0\in(Q)\), induction gives
\(E_j\in(Q^{j+1})\). Independently,

\[
 I_{j+1}(q(z))-z
 =\frac Q a\bigl(R(z)-R(I_j(q(z)))\bigr),
\]

which gives the other inverse congruence with the same order. Thus
\(N-1\) updates are sufficient, including no updates when \(N=1\).

With \(I=I_{N-1}\), the formula
\(V=(z-I(F))/P\) is polynomial because
\(I(F)\equiv I(q(z))\equiv z\pmod P\). Conversely,

\[
 z=I(T)+PV,\qquad
 u=\frac{T-H(x,y,I(T)+PV)}P
\]

is polynomial because the numerator vanishes modulo \(P\). These
expressions recover \(F=T\) and the prescribed \(V\); substituting
the forward map first recovers \(z\), and then \(u\). Both
compositions are identities, not merely congruences.

As an additional exact arithmetic check, a standard-library rational
polynomial computation tested both inverse congruences for

\[
 P=x^2y^3(y-x),\quad Q=xy(y-x),\quad
 H=2z+x+y+Q(z^2+x),\quad I=I_2.
\]

Both remainders were zero. This sample supports the transcription; the
induction above is the proof for arbitrary exponents and remainders.

## 4. The integral residue image in the constant-axis branch

Take \(\lambda\ne b\) satisfying the generic regularity conditions.
The \(C_i\) are disjoint and avoid the axis, so
\(Z_i=C_i\times\mathbb A^1\) are disjoint smooth closed divisors
in the smooth threefold \(X_\lambda\). The quotient by
\(\ell_i\) is the reduced smooth ring defined by
\(q_i-\lambda\). Hence \(\ell_i\) has vanishing order one
along \(Z_i\), regardless of \(m_i\).

The ordinary Gysin sequence is

\[
 H^2(X)\to H^2(U)\xrightarrow{\mathrm{res}}
 \bigoplus_iH^1(Z_i)\to H^3(X).
\]

Both outer groups vanish, so the residue map is an isomorphism over
\(\mathbb Z\), not only over \(\mathbb Q\).

An integral degree-one class of a unit \(g\) can be represented by
the map \(g/|g|\) to the circle. In the product coordinates,
\(\omega_0=\sigma\) and \(\omega_j=\sigma+\tau_j\).
The products \(\omega_0\smile\omega_j\),
\(1\le j<d\), are consequently an integral basis of \(H^2(U)\).

Around \(Z_0\), \(\ell_0\) has one positive normal-circle winding
and \(\ell_j\) restricts to a scalar times the radial coordinate.
Around \(Z_j\), the roles reverse. Around any other component both
functions extend as units. Therefore the residue of the \(j\)-th
basis element is exactly

\[
 (\eta_0,0,\ldots,-\eta_j,\ldots,0),
 \tag{A}
\]

up to the usual consistent orientation convention. There is no factor
\(m_i\) in (A): it is the divisor of \(\ell_i\), not the divisor
of \(P\), which supplies the normal-circle winding.

For each \(i\), the projection of the image lies in
\(\mathbb Z\eta_i\). Surjectivity onto the full direct sum thus
implies \(H^1(C_i)=\mathbb Z\eta_i\). This is the missing
individual constraint that a total rank of \(d-1\) alone would not
provide. Each free group has rank at most one; the sum of ranks makes
exactly one rank zero and all others rank one.

The smooth affine-curve formula identifies these curves with one
\(\mathbb A^1\) and \(d-1\) copies of \(\mathbb C^*\).
On a punctured line a radial unit is \(cv^n\). It cannot be constant:
a closed irreducible curve contained in a vertical affine line is the
whole affine line. Since \(\eta_i\) generates, \(n=\pm1\).
Thus the radial map is an isomorphism, not merely a finite covering.

There is a useful matrix check. Replace every nonzero \(\eta_i\)
by its primitive generator and delete the unique zero-rank row. The
columns of (A) are the columns \(e_0-e_j\) of an incidence matrix
of a star. Every such maximal minor is \(\pm1\): deleting row zero
leaves \(-I\); deleting row \(r>0\) lets column \(r\) pivot in
row zero and leaves the other diagonal columns. An independent exact
integer check verified all these minors for \(2\le d\le6\).

## 5. Recovering fixed polynomial restrictions from generic curves

The finite pigeonhole argument is legitimate. A fixed plane supplies
the affine-line curve at infinitely many distinct levels. Its radial
unit is constant on each such curve, so each is an entire vertical
line. Different levels give different radial constants. Every positive-
\(z\)-degree coefficient of its defining polynomial consequently
vanishes at infinitely many points and is zero. The polynomial depends
only on the radial coordinate; connected generic fibers force its
degree to be one.

Once this distinguished plane has been fixed, it supplies the rank-zero
curve at every generic level. The other planes therefore have the
primitive punctured-line behavior simultaneously at generic levels.
One such level on another plane has exactly one simple point over
every nonzero radial value. Its equation must have degree one in
\(z\). A nonzero radial root of its leading coefficient would give
either no point or an entire vertical line, both impossible. Thus the
coefficient is \(cx^k\); the constant-axis restriction makes
\(k\ge1\). This proves precisely the restrictions (12).

No arbitrary interpolation of independently prescribed plane jets is
used. All restrictions come from the existing polynomial \(H\), so
compatibility at the multiple intersection is retained.

## 6. Chinese remainders, the zero fiber, and prior descent

In \(S=\mathbb C[x,x^{-1},y]\), the differences
\(v_i-v_j=(\alpha_j-\alpha_i)x\) are units. Thus the ideals
\((v_i)\) and \((v_j)\) are comaximal, as are arbitrary positive
powers of them. For example, expanding
\(1=(a+b)^{m_i+m_j-1}\) when \(a\in(v_i)\),
\(b\in(v_j)\), proves the latter assertion.

Each leading coefficient \(c_jx^{k_j}\) is a unit of \(S\).
The same finite-inverse induction works modulo \(v_j^{m_j}\).
Coefficientwise CRT in \(S[T]\) joins the inverse polynomials.
Polynomial substitution preserves each ideal, so both composition
congruences survive the joining. Their common modulus is
\(\prod_jv_j^{m_j}\), which generates the same ideal as \(P\)
after inverting \(x\). The companion construction therefore gives
the actual localized automorphism claimed in (15).

Only powers of \(x\) have been inverted. Consequently this
automorphism and its inverse specialize at every \(x=\gamma\ne0\),
as well as over \(\mathbb C(x)\). At \(x=0\), the original
restriction \(ay+b\) gives the missing polynomial-plane quotient
directly. No limit of a localized automorphism is asserted at zero.

The prior KVZ Theorem 4.23 applies exactly to this residual plane:
the coefficient is in \(\mathbb C[x,y]\), the remainder is in
\(\mathbb C[x,y,z]\), and every fixed-\(x\) zero surface is an
affine plane. Its quotient conclusion, including shifts by
\(\lambda(x)\), was independently source-checked in the preceding
literature pass. It does not require an already polynomial total
quotient or triviality over \(\mathbb C[x,F]\).

The alternate fibration verification is also sound. None of the
linear factors of \(P\) divides \(H-\lambda\), so the equation
is primitive and linear in \(u\), hence irreducible by Gauss's
lemma. Its quotient is a domain, and \(\mathbb C[x]\) injects
because a nonzero polynomial solely in \(x\) cannot be divisible
by a positive-\(u\)-degree polynomial. Torsion-freeness gives
flatness over the PID. The polynomial fibers, including the generic
one, have all been checked. The cited affine-plane-fibration theorem
then has the required hypotheses.

## 7. What is sufficient for the original slice

For an original slice, every closed level has ring

\[
 T/(F-\lambda)\simeq K.
\]

Therefore one affine-three-space closed fiber already suffices.
Proving all fibers are affine three-space is stronger than necessary.
If only the ordinary generic fiber over \(\mathbb C(F)\) has been
identified with affine three-space, an isomorphism and its inverse use
finitely many rational coefficients. They spread to a common
nonempty principal open subset of the parameter line; specialization
at one complex value there gives an affine-three-space closed fiber.
The conclusion is again \(K\simeq\mathbb C^{[3]}\), followed by
\(T=K[F]\). No condition \(D(x)=0\) is needed.

This does not alter the quadratic counterexample
\(F=xu^2+yu+x+z^4\), with \(D=\partial_x-u\partial_y\).
It is a coordinate and an original slice, but its fixed-\(x\)
specializations have critical points. The arrangement proof derives its
relative condition using its special linear-in-\(u\) geometry; it
does not establish a general implication from a slice to residual
coordinatehood.

The proof is valid within its stated central-arrangement scope. The
necessary genericity choices, reduced divisors, integral coefficients,
and localization all have substantive roles and should remain explicit
in any shortened version.
