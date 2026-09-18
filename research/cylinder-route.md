# Cylinder geometry route for characteristic-zero cancellation

**Status (2026-09-12).** Source-checked research note plus elementary deductions. It is not a solution or a novelty claim. Deductions headed “proved here” have not been checked against the full literature for priority.

## Bottom line

The known cylinder constructions do **not** identify a Koras–Russell-type cylinder with affine space. They identify cylinders of different, already exotic, members of a deformation family. Their mechanism also explains exactly why the usual affine-modification rigidity does not descend through a cylinder: the cylinder variable is mixed into the `z,t` coordinates of the unstabilized modification core.

Two concrete conclusions sharpen the next search.

1. A cylinder isomorphism that preserves the unstabilized affine-modification core and center necessarily descends to the bases. Thus any noncancelling isomorphism must violate that preservation condition. The published isomorphisms do so explicitly.
2. A tempting stronger invariant also fails: for the Russell cubic coordinate ring `A`, the slice Makar–Limanov invariant of `A[w]` is already trivial. This is an explicit application in Gaifullin–Shafarevich's 2024 general equality theorem; a direct family-specific reconstruction is included below. Thus replacing ordinary `ML` by “intersection over only actions having slices” will not obstruct `A[w] ≅ C^[4]`.

The most geometrically concrete unresolved target is consequently a one-bad-fibre problem: rule out a polynomial `f` on `A^4_C` whose complement over `G_m` is the trivial `A^3`-bundle, whose nonzero fibres are `A^3`, and whose zero fibre is the nonnormal surface cusp times `A^2`.

## 1. Precise families and what is actually known

Let `k` have characteristic zero, let `q,r >= 2` be coprime, let `m >= 0`, let every `n_i > 1`, and put

```text
xbar = x_0 ... x_m,                 xbar^nbar = product_i x_i^{n_i},
R_m(nbar,p) = k[x_0,...,x_m,y,z,t] /
              (xbar^nbar y + z^q + t^r + x_0 p(xbar)),
```

where `p(0) != 0`. Dubouloz–Ghosh prove:

- `ML(R_m)=k[x_0,...,x_m]` and `DK(R_m)=k[x_0,...,x_m,z,t]` (Proposition 1), hence no base is affine `(m+3)`-space.
- Subject to `deg p_i <= n_0-2`, two bases are isomorphic exactly when `p_2(u)=mu p_1(lambda u)` for nonzero `lambda,mu` (Proposition 2).
- All one-variable cylinders `R_m(nbar,p)[w]` are mutually isomorphic (Proposition 3).
- On every cylinder, ordinary `ML` is `k` and ordinary `DK` is the whole cylinder ring (Proposition 4).

These are [Dubouloz–Ghosh, *Algebraic families of higher dimensional A1-contractible affine varieties non-isomorphic to affine spaces* (2025), Props. 1–4](https://arxiv.org/abs/2501.09613). Proposition 3 says

```text
X_m(nbar,p) x A^1  ≅  X_m(nbar,1) x A^1,
```

not `A^(m+4)`. The `p=1` base still has the nontrivial invariants in Proposition 1. The paper accordingly calls these varieties **potential** counterexamples to Zariski cancellation; its actual counterexamples are to generalized cancellation (nonisomorphic exotic bases with isomorphic cylinders).

For `m=0`, `q=2`, `r=3`, and suitable `p`, this includes deformations of the Koras–Russell cubic. The earlier threefold result is [Dubouloz–Moser-Jauslin–Poloni, *Non cancellation for smooth contractible affine threefolds* (2011), Theorem 3](https://arxiv.org/abs/1004.4723): for

```text
V_{n,p}: x^n y + z^2 + t^3 + x p(x) = 0,
```

the bases have an explicit isomorphism classification while, for fixed `n`, all cylinders are isomorphic. Again, every compared base is exotic; no cylinder is proved to be `A^4`.

This must be kept separate from Gupta's positive-characteristic construction. For an arbitrary field, `m >= 2`, and with the displayed hypersurface ring assumed to be an integral domain, Gupta proves that

```text
k[x,y,z,t]/(x^m y-F(x,z,t)) ≅ k^[3]
```

exactly when `F(0,z,t)` is a coordinate of `k[z,t]`. A nontrivial line in positive characteristic gives a non-polynomial base whose one-cylinder is `A^4` [Gupta, *On the family of affine threefolds x^m y=F(x,z,t)* (2014)](https://doi.org/10.1112/S0010437X13007793). That mechanism does not transfer verbatim over `C`: a line in the affine plane is a coordinate there by Abhyankar–Moh–Suzuki.

## 2. The explicit cylinder map and the exact location of mixing

Put

```text
D = k[x_0,...,x_m,z,t],
q_0 = xbar^nbar,
J_p = (q_0, z^q+t^r+x_0 p(xbar)).
```

Then `R_m(nbar,p)` is the affine-modification algebra

```text
D[J_p/q_0]  subset  D[xbar^{-1}].
```

In the proof of Proposition 3, Dubouloz–Ghosh build a `k[x_0,...,x_m]`-automorphism `psi` of `D[w]` from a `GL_3` matrix with first two rows

```text
(g_1(xbar), 0,            q_0),
(0,            g_2(xbar), q_0).
```

Consequently,

```text
psi(z) = g_1(xbar) z + q_0 w,
psi(t) = g_2(xbar) t + q_0 w,
```

and `psi(J_p D[w])=J_1 D[w]`. The affine-modification universal property lifts this to the cylinder isomorphism.

This is unusually informative. The map fixes every `x_i`, hence fixes the denominator and its distinguished divisor, but it does **not** preserve `D`: both `psi(z)` and `psi(t)` use `w`. Therefore:

- preserving the divisor `q_0=0` is too weak;
- even preserving all the old Makar–Limanov variables `x_i` is too weak;
- preservation of the **unstabilized core** `D` together with its modification center is the missing descent property.

Ordinary invariants cannot recover that core after stabilization: Proposition 4 gives `ML(R_m[w])=k` and `DK(R_m[w])=R_m[w]`.

### Affine-modification descent lemma (proved here)

Let `D,D'` be domains, let `q in D`, `q' in D'` be nonzero, and let `J` and `J'` be ideals containing `q` and `q'`. Set

```text
R  = D[J/q]   subset D[q^{-1}],
R' = D'[J'/q'] subset D'[q'^{-1}].
```

Suppose an isomorphism `Theta:R[w] -> R'[w']` is induced on the ambient localized fraction rings by an isomorphism `theta:D -> D'` satisfying

```text
theta(q)=u q'     and     theta(J)=J'
```

for a unit `u in D'`. Then `Theta(R)=R'`, so `Theta` restricts to an isomorphism `R -> R'`.

**Proof.** `R` is generated over `D` by the elements `j/q`, `j in J`. Their images are

```text
theta(j)/(u q') in D'[J'/q']=R'.
```

Thus `Theta(R) subset R'`. Applying the same argument to the inverse gives the reverse inclusion. QED.

This lemma is deliberately conditional; it does not assert that an arbitrary cylinder isomorphism preserves `D`. Rather, the published `psi` is an explicit witness that this is exactly the condition one cannot assume. A useful future theorem would give an intrinsic characterization of `D` inside the cylinder. Ordinary `ML` and `DK` cannot do that.

There is an equivalent translation formulation: if an isomorphism `R[w] -> R'[w']` conjugates the canonical translation derivation `partial_w` to a nonzero scalar multiple of `partial_{w'}`, then it maps `ker(partial_w)=R` to `ker(partial_{w'})=R'` and descends. Hence any isomorphism between cylinders of nonisomorphic bases must also mix the canonical translation foliation.

## 3. The Russell cubic as a one-bad-fibre polynomial

For the Russell cubic

```text
A = C[x,y,z,t]/(x^2 y+z^2+t^3+x),       B=A[w],
```

projection by `x` has a very rigid elementary description:

- `A/(x-a) ≅ C^[2]` for each `a != 0` (solve for `y`);
- `A/(x) ≅ C[y,z,t]/(z^2+t^3)`, a nonnormal cusp cylinder;
- `A[x^{-1}] ≅ C[x,x^{-1},z,t]`.

Thus, if a hypothetical isomorphism `Phi:B -> C^[4]` exists and `f=Phi(x)`, then necessarily

```text
C^[4][f^{-1}] ≅ C[f,f^{-1}]^[3],
C^[4]/(f-a)   ≅ C^[3]                    for every a != 0,
C^[4]/(f)     ≅ (C[z,t]/(z^2+t^3))^[2].
```

In particular `f` is not a coordinate, because its zero fibre is not even normal. The sought contradiction cannot therefore be “show `f` is a coordinate because most fibres are affine space” without a genuinely new one-bad-fibre theorem. This also pinpoints why the usual residual-coordinate heuristic is insufficient: the exceptional fibre is built into the problem, while standard residual-coordinate hypotheses normally demand coordinate behaviour in every residue fibre.

The 2024 linear-threefold theorem does not quietly settle this. In characteristic zero, Theorem 4.8 of [Ghosh–Gupta–Pal, *On the family of affine threefolds a(x)y=F(x,z,t)*](https://arxiv.org/abs/2403.17397) makes polynomiality equivalent to conditions including

```text
A^[l] ≅ k^[l+3]  AND  ML(A)=k,
```

or the analogous stable-polynomial condition **and** `DK(A)=A`. Stable polynomiality alone is not one of the equivalent conditions. For the Russell cubic, `ML(A)=C[x]` and `DK(A)=C[x,z,t]`, so those implications cannot be invoked.

## 4. Slice actions: a promising-looking obstruction that actually collapses

Let `LND*(B)` denote locally nilpotent derivations admitting a slice, and

```text
ML*(B) = intersection_{D in LND*(B)} ker(D).
```

This variant is studied in [Dasgupta–Gupta, *An algebraic characterization of the affine three space*](https://arxiv.org/abs/1709.00169). Since `ML*(C^[4])=C`, a nontrivial `ML*(B)` would obstruct `B ≅ C^[4]`. But, for affine irreducible varieties over an algebraically closed characteristic-zero field, Gaifullin–Shafarevich subsequently proved the general theorem `ML*(Y)=ML(Y)` whenever `Y` admits at least one locally nilpotent derivation with a slice. They explicitly apply it to the Koras–Russell cylinder: canonical cylinder translation has a slice and Dubouloz had already proved ordinary `ML(B)=C`, so `ML*(B)=C`; see [Gaifullin–Shafarevich, *Modified Makar-Limanov and Derksen invariants* (2024)](https://arxiv.org/abs/2212.05899).

At first the route looks plausible. The canonical `partial_w` has slice `w` and fixes `x`. The familiar locally nilpotent derivations on `A`, extended to `B`, also fix `x`. Moreover, the explicit derivation that Dubouloz–Moser-Jauslin–Poloni use to move `x` is itself nonslice (direct verification below).

Nevertheless, conjugating cylinder translation by the flow of that nonslice derivation produces slice derivations moving `x`. In fact one gets the following exact computation.

### Direct reconstruction of the known conclusion `ML*(A[w])=C`

**Step 1: reduce every possible invariant to `C[x]`.** Canonical translation shows `ML*(B) subset A`. For each `E in LND(A)`, extend `E` by `E(w)=0` and set

```text
D_E = partial_w + E.
```

The summands commute, so `D_E` is locally nilpotent, and `D_E(w)=1`; it has a slice. If `h in ML*(B)`, then `h in A` and `0=D_E(h)=E(h)` for every `E`. Hence

```text
ML*(B) subset ML(A)=C[x].
```

**Step 2: produce a slice derivation moving `x`.** Proposition 7.2 of [Dubouloz–Moser-Jauslin–Poloni, *Inequivalent embeddings of the Koras–Russell cubic threefold*](https://arxiv.org/abs/0903.4278) constructs `L in LND(B)` satisfying

```text
L(x) = -2 t^6 (z+xw).
```

For `c in C`, put `alpha_c=exp(cL)` and

```text
delta_c = alpha_c partial_w alpha_c^{-1}.
```

It is locally nilpotent and has slice `alpha_c(w)`. As a polynomial function of `c`,

```text
(d/dc)|_{c=0} delta_c(x)
  = [L,partial_w](x)
  = -partial_w(L(x))
  = 2 t^6 x != 0.
```

Therefore `delta_c(x) != 0` for at least one `c`. If a polynomial `h(x) in C[x]` lies in its kernel, then `h'(x)delta_c(x)=0`; since `B` is a characteristic-zero domain, `h` is constant. Together with Step 1 this proves `ML*(B)=C`. QED.

This is a direct family-specific proof of the already source-known conclusion, not a new result and not evidence for cancellation. It says the slice-only strengthening loses precisely the same last coordinate obstruction as ordinary `ML`.

### Modified Derksen invariant: still open, with a concrete membership reduction

Gaifullin–Shafarevich also define

```text
HD*(B) = C[ker(D) : D is a nonzero locally nilpotent derivation with a slice].
```

Unlike `ML*`, this invariant need not equal ordinary `HD`. Their example with `HD* != HD` is nonnormal, and their paper explicitly asks whether such a difference can occur for a normal affine irreducible variety. The Russell cylinder is smooth and hence normal. Since `HD*(C^[4])=C^[4]`, proving `HD*(B) != B` would both obstruct cancellation for this candidate and furnish a normal example for their question. No such proof was found here.

There is a sharp elementary reduction and some exact positive membership evidence. Canonical translation has kernel `A`, so

```text
A subset HD*(B).
```

For the standard derivation `E_1=2z partial_y-x^2 partial_z` on `A`, the slice derivation `partial_w+E_1` kills `z+x^2w`; hence `x^2w in HD*(B)`. For the DMP derivation `L`, let `alpha_c=exp(cL)` as above. Every `alpha_c(A)` is the kernel of a slice derivation, so every coefficient of the finite polynomial `alpha_c(x)` belongs to `HD*(B)` by evaluation at finitely many distinct `c` and Vandermonde interpolation. In particular,

```text
L(x)=-2t^6(z+xw) in HD*(B),
```

and therefore `t^6 xw in HD*(B)`. Thus the rigorous current bracket is

```text
A[x^2w,t^6xw] subset HD*(B) subset B=A[w].
```

The unresolved membership question is whether other slice kernels remove the factors supported on `x=0` and `t=0` and generate `w` itself. This is more precise than recomputing ordinary `DK(B)=B`, but it is also high-risk: a proof of properness would have consequences beyond this one example.

### Supplemental check: the published `x`-moving derivation itself has no slice

This nuance prevents a misleading inference. In the localization used in Proposition 7.2, write

```text
S = C[t,t^{-1},y,w],       a=y+1,
R = S[x,z]/(a x+z^2+t^3),
Delta = t^6(-2z partial_x+a partial_z).
```

Then `ker(Delta)=S`. Indeed every element has a unique expression `P(x)+zQ(x)`, with `P,Q in S[x]`. Dividing the kernel equation by the invariant unit `t^6` gives

```text
-2z P'(x) + a Q(x) + 2(a x+t^3)Q'(x)=0.
```

Uniqueness of the `S[x] + zS[x]` expression forces `P'=0`; comparing the leading term of a nonzero degree-`n` polynomial `Q` gives `a(2n+1)lc(Q)=0`, impossible. Hence `P in S` and `Q=0`.

If `Delta` had a slice, the slice theorem would give `R=S[s]`. Reducing modulo the invariant `a` and extending scalars to an algebraic closure of `C(t,w)` would make the result a polynomial domain in one variable. But the actual quotient is

```text
C[t,t^{-1},w,x,z]/(z^2+t^3),
```

whose corresponding geometric generic fibre splits into two affine lines. Contradiction. The conjugate global derivation `L` therefore has no slice either. The proposition above shows why that fact is not enough: `exp(cL)` conjugates the *canonical* slice derivation into new slice derivations.

## 5. Ranked next routes

1. **Intrinsic-core theorem (best algebraic route).** Seek an intrinsic property of the subring `D=C[x,z,t]` (or `k[x_i,z,t]`) inside the cylinder that survives arbitrary automorphisms. If it forces preservation of the affine-modification core and center, the descent lemma ends the problem. Ordinary `ML`, ordinary `DK`, and `ML*` cannot supply it.
2. **Modified Derksen membership (sharp but high-risk).** Decide whether `w in HD*(A[w])`. The exact inclusions above give a starting ideal of known multiples. Properness would be a cancellation obstruction, but it would also answer a published question for a normal variety, so it should not be treated as routine.
3. **One-bad-fibre exclusion (best geometric route).** Study whether a polynomial `f in C^[4]` can simultaneously have the three displayed properties in Section 3. The complement trivialization and the exact nonnormal cusp fibre are substantially stronger data than merely “general fibre A^3.” A first bounded lemma should target the conductor and the birational normalization `C[u] -> C[z,t]/(z^2+t^3)` (`z=u^3`, `t=-u^2`, up to harmless signs) and ask how that conductor sits in the boundary of the trivial `G_m`-family. The degree-two projection of the cusp to the `t`-line must not be confused with its birational normalization.
4. **Translation-action rigidity.** A hypothetical cancellation transports `partial_w` to a slice `G_a`-action on `A^4` whose invariant ring is the exotic threefold `A`. Prove that a slice action on `A^4` compatible with the one-bad-fibre function `f` must have a coordinate in its kernel or must preserve a polynomial three-variable core. Either conclusion would force descent. A new hypothesis is required: the existence of a slice by itself does not currently establish either conclusion.
5. **Generalized family comparison.** Use the explicit `GL_3` matrix to calculate which filtrations, Rees algebras, or conductor data remain fixed despite `w`-mixing. An invariant that distinguishes `D` from its mixed copies could apply uniformly to all `R_m(nbar,p)`.
6. **Do not prioritize invariant variants without a mixing test.** The calculation `ML*(A[w])=C` is a reusable warning: an `x`-moving nonslice action can still destroy a slice-defined invariant by conjugating cylinder translation.

## 6. Source boundaries

- Source-stated: the `ML`/`DK` values, base classification, mutually isomorphic exotic cylinders, explicit `GL_3` construction, and A1-contractibility are in Dubouloz–Ghosh 2025.
- Source-stated: the explicit localized cylinder isomorphism and the global `x`-moving locally nilpotent derivation with `L(x)=-2t^6(z+xw)` are in Dubouloz–Moser-Jauslin–Poloni 2009, Propositions 7.1–7.2.
- Source-stated: Gaifullin–Shafarevich prove the general equality `ML*=ML` in the presence of any slice action and explicitly apply it to the Koras–Russell cylinder.
- Proved in this note, with priority not audited: the conditional affine-modification descent lemma, the nonslice check for that particular `L`, and the displayed lower inclusion for `HD*(A[w])`. The conjugation argument for `ML*(A[w])=C` is only a direct reconstruction of an already known conclusion.
- Not proved here: nonexistence of `A[w] ≅ C^[4]`, intrinsic recoverability of the modification core, or any one-bad-fibre exclusion theorem.
- Literature coverage here is targeted, not exhaustive. Before presenting either elementary deduction as new, run a statement-level search for the slice invariant of Koras–Russell cylinders and ask an affine-algebraic-geometry expert to check it.

## Primary references

- A. Dubouloz and P. Ghosh, [*Algebraic families of higher dimensional A1-contractible affine varieties non-isomorphic to affine spaces*](https://arxiv.org/abs/2501.09613), 2025.
- A. Dubouloz, L. Moser-Jauslin, and P.-M. Poloni, [*Non cancellation for smooth contractible affine threefolds*](https://arxiv.org/abs/1004.4723), 2011.
- A. Dubouloz, [*The cylinder over the Koras–Russell cubic threefold has a trivial Makar-Limanov invariant*](https://arxiv.org/abs/0807.4085), 2009.
- A. Dubouloz, L. Moser-Jauslin, and P.-M. Poloni, [*Inequivalent embeddings of the Koras–Russell cubic threefold*](https://arxiv.org/abs/0903.4278), 2009.
- A. Dubouloz, L. Moser-Jauslin, and P.-M. Poloni, [*Automorphism groups of certain rational hypersurfaces in complex four-space*](https://arxiv.org/abs/1309.7363), 2013.
- N. Gupta, [*On the family of affine threefolds x^m y=F(x,z,t)*](https://doi.org/10.1112/S0010437X13007793), 2014.
- P. Ghosh, N. Gupta, and A. Pal, [*On the family of affine threefolds a(x)y=F(x,z,t)*](https://arxiv.org/abs/2403.17397), 2024 preprint.
- N. Dasgupta and N. Gupta, [*An algebraic characterization of the affine three space*](https://arxiv.org/abs/1709.00169), 2019 version.
- S. Gaifullin and A. Shafarevich, [*Modified Makar-Limanov and Derksen invariants*](https://arxiv.org/abs/2212.05899), *Journal of Pure and Applied Algebra* 228 (2024), 107616.
