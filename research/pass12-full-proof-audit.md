# Full proof audit of the height-eight criterion

No mathematical gap was found in
[height-eight-algebra-pass.md](height-eight-algebra-pass.md). This audit
covers the entire argument, not only its final homogenization branch.
The proved scope is
\[
E\in\operatorname{LND}(\mathbb C[x_1,x_2,x_3,x_4]),\qquad
[E,[E,\partial_{x_i}]]=0\quad(1\le i\le4)
\]
implying that \(\ker E\) contains an ambient polynomial coordinate.
With a slice, the regular-kernel theorem gives
\(\ker E\cong\mathbb C^{[3]}\). The deduction of cancellation for
\(H\le8\) is valid. No universal height bound or unrestricted
cancellation theorem is established.

## 1. Differential identities and exhaustion of the branches

Write \(P=E(x)\) and \(J=\operatorname{Jac}P\), using the column-vector
convention in the proof. The signs are consistent:
\([E,\partial_j]\) has coefficient vector \(-J_{\cdot j}\), and its
commutation with \(E\) gives \(E(J)=J^2\).

Since \(E(J^k)=kJ^{k+1}\), induction gives
\(E^r(J)=r!J^{r+1}\). Local nilpotence on all sixteen entries gives one
finite exponent annihilating all of them. Thus \(J\) is nilpotent over
the fraction field and \(J^4=0\).

For \(h_r=E^r(x)\), both displayed identities are correct:
\[
h_r=(r-1)!J^{r-1}P,
\qquad \operatorname{Jac}h_r=r!J^r.
\]
The first follows from the product rule, \(E(J)=J^2\), and \(E(P)=JP\).
For the second, the exact differentiation rule is
\[
\operatorname{Jac}(Ev)
=E(\operatorname{Jac}v)+(\operatorname{Jac}v)J.
\]
It yields the claimed factorials. Consequently \(h_4\) is constant
and \(h_5=0\). A nonzero \(E\) therefore has a highest nonzero iterate
\(h=h_m\) for exactly one \(1\le m\le4\).

Maximality gives all the relations used later:
\[
E(h)=0,\qquad Jh=0,\qquad J\operatorname{Jac}h=0.
\]
Indeed \(Jh=h_{m+1}/m\), while differentiating \(h_{m+1}=0\) gives
\(J^{m+1}=0\). Therefore \((\operatorname{Jac}h)h=0\). The field
\(h\cdot\partial\) is a quasi-translation derivation: it kills its
own generator images, so repeated differentiation of any polynomial
eventually vanishes. No assertion that an arbitrary bracket is an LND
enters this step.

The rank exhaustion is complete:

| Highest nonzero iterate | Required matrix consequence | Rank of \(\operatorname{Jac}h\) |
| --- | --- | --- |
| \(m=4\) | \(J^4=0\) | Zero |
| \(m=3\) | \(J\) nilpotent of size four | At most one |
| \(m=2\) | \(h_3=0\Rightarrow J^3=0\) | At most one |
| \(m=1\) | \(h_2=0\Rightarrow JP=J^2=0\) | At most two |

For \(m=2\), the additional \(J^3=0\) is essential: the largest
possible Jordan block has size three, and in dimension four the square
then has rank at most one. For \(m=3\), only a size-four block can
contribute to \(J^3\), and contributes rank one. Thus no higher-rank
highest-iterate branch was omitted.

## 2. Constant commuting directions really give a three-variable problem

If \(0\ne v\in\mathbb C^4\) and \(Jv=0\), the constant translation
\(V=v\cdot\partial\) commutes with \(E\). A constant linear coordinate
change makes \(V=\partial_4\), and \(R=\ker V\) is an actual coordinate
three-ring, not merely an abstract invariant algebra.

Commutation makes \(R\) stable under \(E\). The restriction is an LND.
Every new coordinate partial is a constant linear combination of the old
ones, so all the double-bracket equations survive this change. Restriction
then gives the hypothesis of the three-variable single-partial lemma in
[height-seven-audit.md](height-seven-audit.md). Its invariant coordinate
in \(R\) remains an ambient coordinate of \(B=R[x_4]\). A zero restricted
derivation is harmless.

The prior lemma was also rechecked: its independent case uses the
three-variable commuting-LND theorem, and its dependent case removes
the coefficient gcd before descending to a plane. It does not equate
gcd one with the unit ideal. No slice for \(E|_R\), or irreducibility of
that restriction, is being assumed.

## 3. The exact rank-one theorem applies

[De Bondt, Theorem 5.5](https://arxiv.org/pdf/1501.05168) is stated for
nonhomogeneous quasi-translations of Jacobian rank one. It provides the
normal form used in the proof and does not require coefficient gcd one.
Its conclusion bounds the coefficient-image span by three in dimension
four. Thus the three span cases in the proof are exhaustive.

The linear change is simultaneous conjugation of the coefficient vector
and its source coordinates. The relations
\(E(h)=Jh=J\operatorname{Jac}h=0\) are preserved by this change, as is
the original double-bracket hypothesis.

- For a one-dimensional image span, \(h=gv\) with \(v\ne0\) constant.
  The domain property permits cancellation of \(g\) in \(Jh=0\), giving
  the constant commuting direction from Section 2.
- For a three-dimensional span, the normal form makes every component
  depend only on \(x_1\). Some component is nonconstant because the
  Jacobian rank is one. Its nonzero derivative and \(E(h_i)=0\) force
  \(E(x_1)=0\).
- For a two-dimensional span, the nonzero components are independent
  polynomials \(h_3,h_4\in\mathbb C[x_1,x_2]\). Their quotient cannot
  have both partial derivatives zero unless it is a complex constant.
  Hence the determinant in equation (9) of the proof is nonzero for
  some \(j\). The vectors \(h,\partial_jh\) span the constant
  \(e_3,e_4\)-plane over the fraction field. Since \(J\) kills both,
  \(Je_3=Je_4=0\) as polynomial identities. All coefficients of \(E\)
  therefore lie in \(\mathbb C[x_1,x_2]\), and its restriction to that
  coordinate plane has an invariant plane coordinate by Rentschler,
  unless it is zero.

In the last case, the nonzero determinant need not be a unit. Only
fraction-field spanning is needed; the resulting vanishing columns are
polynomial identities. No unproved denominator removal occurs.

## 4. Residual rank two and kernel recognition

The remaining case is precisely
\(JP=J^2=0\), \(\operatorname{rank}J=2\). Its proof was reconstructed in
[height-eight-homogenization-audit.md](height-eight-homogenization-audit.md).
The image ideal is Euler-stable and hence homogeneous. The image closure
is a cone, and homogenization in five variables preserves Jacobian rank
two. Independently, the block formula
\[
\operatorname{Jac}\widetilde P
=t^{d-1}
\begin{pmatrix}J(x/t)&dP(x/t)-J(x/t)(x/t)\\0&0\end{pmatrix}
\]
proves the same rank statement because \(P\in\ker J=\operatorname{im}J\).

[De Bondt, Theorem 5.3](https://arxiv.org/pdf/1501.05168) then bounds the
homogenized coefficient-image span by three. This yields a genuine
linear relation among the four original coefficients, not just the
automatic relation from the appended zero component. The use of this
homogeneous theorem does not require a homogeneous original field.

An invariant ambient coordinate has now been obtained in every branch,
without a slice assumption. In the slice case, regularity of the kernel
descends from \(K[s]\cong\mathbb C^{[4]}\), and
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
has the required regular-kernel and invariant-coordinate hypotheses.

## 5. Controls and final boundary

The seven methods in
[height_eight_algebra_checks.py](height_eight_algebra_checks.py) were read
and rerun with \(/opt/anaconda3/bin/python\). All passed in 0.225 seconds.
They check the fourth-time-degree example, inverse presentations,
filtration degrees, homogenization rank, and the two negative controls.
The negative controls correctly show that neither square-zero Jacobian
alone nor a nice derivation with a slice supplies the full hypothesis.
No counterexample or missing hypothesis was found in this audit.

These finite computations are not a proof of the general rank-one or
homogeneous rank-two classification theorems. The overall conclusion is
source-dependent mathematics, not formal verification, human peer review,
or an established novelty claim.

The older lower-rank orbit investigation is superseded as a statement
of what remains at height eight: its degeneration examples are valid,
but the new theorem closes them without requiring full orbit rank or
automatic freeness of the displayed fields. Height nine, including
\((1,1,1,2)\), and the absence of a general height bound remain outside
the proved result.
