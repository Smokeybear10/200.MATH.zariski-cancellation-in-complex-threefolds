# Independent audit of the actual whole-frame criterion

## Verdict and scope

I read the complete final `actual-frame-pass38.md`, including its revised
direct-restriction argument, and the complete standalone checker. I found
no mathematical gap in the conditional theorem. The assumption is one
**genuine polynomial coordinate frame** satisfying all four identities
\([E,[E,\partial_{x_i}]]=0\), not four unrelated locally nilpotent
derivations. Existence of such a frame for an arbitrary
\(A[s]\simeq\mathbb C^{[4]}\) remains unproved. The conclusion does not
settle cancellation or the all-frame case.

The terminology correction in `literature-scope-pass38.md`, Section 4,
item 3, has also been made: fixing an ambient coordinate is equivalent
to **this individual derivation having coordinate rank at most three**,
not to an assertion about the intrinsic LND rank of its kernel.

## Reconstructed proof gates

1. **The first commutators are actual commuting LNDs.** Applying
   \((\operatorname{ad}E)^2\) to the zero bracket of coordinate partials
   gives \(2[S_i,S_j]=0\). The finite-coefficient conjugation argument
   supplies a common exponent for each fixed input polynomial before
   taking the top parameter coefficient. It therefore proves local
   nilpotence, not merely a specialization or limit heuristic.

2. **The high-rank branch descends directly.** Centralization of \(E\)
   makes every \(S_i\) preserve \(A\). If \(E,S_i,S_j\) are independent
   over \(\operatorname{Frac}B\), a dependence of their last two
   restrictions over \(\operatorname{Frac}A\) would give a derivation
   of \((\operatorname{Frac}A)(s)\) killing \(\operatorname{Frac}A\).
   Such a derivation is a multiple of \(\partial_s\), a contradiction.
   No group-quotient or supplied rank-three descent theorem is needed.

3. **The low-rank chain argument is valid over the fraction field.**
   The exact identity is \(E(J)=J^2\), not \(J^2=0\).
   Entrywise local nilpotence and
   \(E^m(J)=m!J^{m+1}\) imply nilpotence of \(J\). If \(J^2v\ne0\),
   the cyclic-chain vectors \(v,Jv,J^2v\) are independent and lie in
   the augmented column span. The assumed rank at most two rules
   this out and gives \(E^2(v)=0\).

4. **The projective image is forced to be a line for a specific reason.**
   In the non-quasi-translation branch the differential rank of
   \([v]\) is \(\operatorname{rank}[v\mid J]-1\). Characteristic zero
   bounds the irreducible image closure by a curve. An actual orbit
   through a point where \(v\) and \(E(v)\) are independent supplies
   the dense subset of a projective line
   \([v(a)+tE(v)(a)]\). Thus this particular image closure is that
   line; there is no inference that every low-dimensional projective
   image is linear.

5. **Homogenization uses the full Jacobian.** For
   \(\widetilde v=(z^dv(x/z),0)\), the last column is
   \(d v-Ju\), up to the common factor \(z^{d-1}\).
   The column operation and the nonzero integer \(d\) give exactly
   \(\operatorname{rank}\operatorname{Jac}\widetilde v
     =\operatorname{rank}[J\mid v]\).
   The homogeneous map has positive degree and is nonzero, so its
   Jacobian rank cannot be zero. Two independent linear invariants
   then include one with nonzero original-variable part, since the
   already invariant \(z\) spans only one dimension.

## Primary-source boundary

I directly read the complete statement and proof of de Bondt's
[Proposition 2.5 and Theorem 3.6(i),(iii)](https://arxiv.org/pdf/1501.04845v3),
including the theorem's dimension-at-most-five proof. The homogenization
and rank-one/rank-two conclusions apply as used; the gcd-one hypothesis
belongs to part (ii), not to the invoked conclusions. The paper credits
the latter theorem to Gordan and Nöther. This is inherited input.

I also directly read the complete [Bhatwadekar–Gupta–Lokhande
Theorem 3.5 and proof](https://arxiv.org/html/1501.01438v1) this pass.
The nonzero derivation fixes an actual ambient linear coordinate, and
regularity of \(A\) descends from \(A[s]\), so its hypotheses are met.

## Exact controls

I independently read and ran the complete six-method
`actual_frame_checks_pass38.py` suite:

```text
/opt/anaconda3/bin/python research/actual_frame_checks_pass38.py
Ran 6 tests in 0.142s
OK
```

These finite identities and negative controls supplement the written
proof. They do not independently establish the external classification,
the universal frame-existence assertion, novelty, expert review, or
proof-assistant verification. No mathematical correction was requested.
