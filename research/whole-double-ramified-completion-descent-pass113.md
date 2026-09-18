# Ramified divisor contraction and finite-degree completion descent

In the actual proper-image whole-double alternative, the support of the
first derivative image is one analytically irreducible base curve germ.
After completing the base, powers of its equation contract from the
whole-fiber completion. Thus a formal function which is already a rational
actual function with a power of the first image as denominator is actual
over the completed base.

If the first normal action is nonzero, the constant leading chart112 also
identifies the completed invariant kernel with the completed base. Together
these facts prove descent of every finite N-degree, including degree two.
The scalar contraction does not require that extra normal-action hypothesis.
No assertion recognizes the threefold or supplies an arbitrary input with
the required original frame.

## 1. Three rings which must remain distinct

Use the actual setup of
[product-index112](whole-double-product-index-pass112.md) and
[conormal-chart112](whole-double-global-conormal-chart-pass112.md).
Here A denotes the localization of the actual threefold at the base point,
not the original polynomial cylinder. Put
\[
\begin{gathered}
R=S_{\mathfrak m},\quad S=\mathbb C[s_1,s_2],\quad
F_j=\ker(N^{j+1}:A\to A),\quad I_1=N(F_1)=PR,\quad P\ne0,\\
F_1=R\{1,r\},\quad Nr=P,\quad
A/\mathfrak mA=\mathbb C[c,G]/(G^2),\quad
\bar N=\lambda G\partial_c,\quad\lambda\in\mathbb C^*,\\
\widehat R=\varprojlim R/\mathfrak m^n,\qquad
A'=A\otimes_R\widehat R,\qquad
\mathcal A=\varprojlim A/\mathfrak m^nA
          =\varprojlim A'/\mathfrak m^nA'.
\end{gathered}
\tag{1}
\]
The actual flatness makes A' flat over the local domain Rhat. Its generic
fiber is Frac(Rhat)[r], so A' is a domain. It is Noetherian because it is
of finite type over Rhat. Its closed fiber is the nonzero double in (1).
Localizing at a prime containing mA' and applying Krull intersection shows
that A' injects into its mA'-adic completion: localization is injective for
a domain. We regard A' as a subring of the domain mathcal A.

Flat base change, rather than completion of a non-A-linear operator, gives
ker(N^(j+1) on A')=F_j tensor_R Rhat. Each F_j is finite free of rank j+1
by [module102](quadratic-degree-module-fiber-rigidity-pass102.md).
All elements of A' are locally nilpotent for N, since each
is a finite sum of tensors of actual elements. The slice formula gives
A'[1/P]=Rhat[1/P][r]. These statements do not identify A' with mathcal A.

The ideals q=sqrt(mA) and mA define equivalent topologies because
q squared is contained in mA and mA is contained in q. In particular
chart112 identifies mathcal A with C[c][[x,G]]. Completion here is along
the entire reduced c-line, not at a chosen point on that line.

## 2. The support of P has one normalized branch

An irreducible p in R is represented by an actual irreducible base equation
through m. At its generic point,
[actual divisor91](nonconical-residue-degree-bound-pass91.md) and
[classification107](quadratic-constant-divisor-filtration-pass107.md)
give either a degree-one constant field and a slice, or a degree-two constant
field and the alternating conic basis. For the first assertion, choose a
local slice z with Nz=p^d. If d is positive, its residue is killed by the
nonzero translation on k[w], hence is a constant in k. Lift that constant
to the base DVR and divide z minus the lift by p. Repeating finitely gives
a slice, exactly as in [rank-defect105, Section 2](mixed-cubic-rank-defect-pass105.md).
Thus the degree-one case makes I1 a unit over R_(p); the degree-two case
gives positive valuation of I1. Consequently
the irreducible factors of P are exactly the degree-two constant divisors
through m.

Choose the actual product-complement curve Gamma used in the
[repaired integral support argument96, Sections 1--4](irreducible-fiber-dependency-audit-pass96.md).
It contains every degree-two divisor: otherwise its generic point would lie
in the product complement, where the constant field has degree one. For the
whole reduced fiber in (1), the supported rank formula is q_src-r_base+1=1.
Every normalized base branch has a source point under the finite normalized
curve map, so there is exactly one source point over each branch. Its
ramification index equals the generic cover degree. The same integral
diagram makes the degrees of distinct branches pairwise coprime.

Thus at most one normalized branch has degree two. Since P is a nonunit in
the proper alternative, there is one, belonging to a unique irreducible p.
That p cannot have a second normalized branch through m. Therefore
\[
\boxed{\quad
P=v p^e,\qquad v\in R^*,\quad e\ge1;\qquad
p=0\text{ has one normalized branch at }\mathfrak m;\qquad
\text{its normalized constant cover has one point of index }2.
\quad}
\tag{2}
\]
Only the whole reduced fiber's irreducibility is used for the rank-one
support group. No original speed-normal assumption enters this argument.
The all-normal conclusions111 supply precisely this whole double. No
claim applies the same argument to one component of a reducible fiber.

The source dependence is the exact supported integral lattice of96, not
properness of the additive quotient, an assumed normality of its exceptional
curve, or an affine-line normalization of every exceptional component.
Degree-one components of Gamma are permitted throughout.

## 3. Completing the two normalized curve rings

Let C0=R/pR and let V be its normalization. This is a finite birational
extension. The unique normalized branch in (2) makes V a local DVR with
residue field C. Its completion is C[[t]]. The finite inclusion C0 into V
stays injective on completion. A nonzero conductor element d satisfies
dV subset C0; completing this inclusion shows that C0hat and Vhat have the
same fraction field. In particular Rhat/(p) is a domain. These are ordinary
finite curve normalization and finite-module completion facts.[^curve]

Write k=Frac(C0) and let k'/k be the degree-two constant field of the actual
generic divisor. The normalization of V in k' is the localization of the
normalized source curve over its corresponding point. Call it W. By (2)
there is only one point, so W is a local DVR, finite free of rank two over
V. Its maximal-ideal topology agrees with the topology induced from V.
Hence W tensor_V Vhat is its DVR completion What and is a domain. On
inverting the parameter t, this proves
\[
\begin{gathered}
K_0=\operatorname{Frac}(\widehat R/(p))
   =\operatorname{Frac}(\widehat V),\qquad
k'\otimes_k K_0=\operatorname{Frac}(\widehat W)
   \text{ is a field},\\
(A'/pA')\otimes_{\widehat R/(p)}K_0
    =(k'\otimes_k K_0)[w],\qquad
\boxed{\ A'/pA'\text{ is a domain}.\ }
\end{gathered}
\tag{3}
\]
For the last assertion, base change of the actual flat A/R is flat over
Rhat/(p), hence torsion free. It embeds into the displayed generic domain.
The field identification uses the full actual divisor ring k'[w], not only
its fraction field or an image of selected good generators.

This proves directly that p remains prime after completing the base and
after passing to A'. It does not assume normalization commutes with an
arbitrary base change. Only the finite curve modules and their one-point
DVR completions were used.

## 4. Exact scalar contraction from the whole-fiber completion

The domain A'/pA' has a nonzero closed fiber, again (1). Choose a prime
containing m(A'/pA'). Its localization is a Noetherian local domain, so
Krull intersection and injectivity of localization show that the map from
A'/pA' to its m-adic completion is injective. Completion is exact for
finite modules over the Noetherian ring A'. Therefore
p mathcal A intersect A'=pA'.[^completion]

The completion A' to mathcal A is flat. Thus p remains a nonzerodivisor in
mathcal A. If an element of A' belongs to p^d mathcal A, first contract
one p, divide in A', cancel that p in mathcal A, and repeat. Equation (2)
now gives
\[
\boxed{\quad
P^d\mathcal A\cap A'=P^dA'\quad(d\ge0),\qquad
\mathcal A\cap A'[1/P]=A'
\quad\text{inside }\mathcal A[1/P].\quad}
\tag{4}
\]
This is a scalar-denominator statement. It does not assert faithful
flatness of A' to mathcal A. The possible existence of other components
over nonclosed base points has not been dismissed in general; (3) rules
out the relevant loss on the particular divisor supporting P.

## 5. Completed constants when the first normal action is nonzero

For this section impose gamma not equal to zero in chart112. Its actual
invariant base coordinates x,f are a regular system of parameters of R.
The complete weighted chart is
\[
\begin{gathered}
\operatorname{wt}x=2,\quad\operatorname{wt}G=1,
\quad\operatorname{wt}\mathbb C[c]=0,\\
f=f_*+O_{\rm wt}(3),\qquad f_*=A(c)x+BG^2,
\quad A'\ne0,\quad B\in\mathbb C^*,\\
N_*=\gamma x\partial_G+\lambda G\partial_c,
\quad \gamma,\lambda\in\mathbb C^*,\qquad
\boxed{\ \ker(N_*:\mathbb C[c,x,G]\to\mathbb C[c,x,G])
             =\mathbb C[x,f_*].\ }
\end{gathered}
\tag{5}
\]
Here N raises weight by at least one and its leading operator is N_*.
The retained identities gamma=-nu0 A' and lambda=2nu0 B make f_* invariant.
To prove the last equality, invert x. Since A(c) is affine with nonzero
slope, the coordinates x,f_*,G identify the localization with
C[x,1/x,f_*,G], and N_* is gamma x partial_G. Its kernel is
C[x,1/x,f_*]. Intersect with the unlocalized polynomial ring. If a
polynomial in x,f_* is divisible by x there, reduction modulo x sends
f_* to BG squared and forces its constant x-coefficient to vanish.
Removing denominators successively proves the equality.

Let z in mathcal A be N-invariant. Its first nonzero weighted homogeneous
term is killed by N_*. By (5), it is a homogeneous polynomial in x,f_*,
necessarily of even weight. Subtract the same polynomial in the actual
invariants x,f. The remainder has strictly higher weight and is still
invariant. Repeating this process yields corrections in increasing powers
of (x,f). They converge in Rhat, and their images converge to z in
mathcal A. The weighted and q-adic filtrations are cofinal. This proves
\[
\boxed{\qquad
\gamma\ne0\quad\Longrightarrow\quad
\ker(N:\mathcal A\to\mathcal A)=\widehat R.
\qquad}
\tag{6}
\]
The weight-zero first term is a constant because the kernel in (5) has
weight-zero part C. No arbitrary power series in c appears: the whole-line
coefficient ring is C[c]. If gamma is zero, the leading kernel instead
contains G, so this same subtraction argument does not establish (6).

## 6. Descent of all finite degrees in the nonzero-action case

Under (6), the kernel on mathcal A[1/P] is Rhat[1/P], since P is invariant
and a nonzerodivisor. Induct on n to show that every z in mathcal A killed
by N^(n+1) lies in A'. The case n=0 is (6). For the induction step,
Nz belongs to A' by the preceding degree. In
A'[1/P]=Rhat[1/P][r], integrate Nz as a polynomial in r with respect to
N=P partial_r. Characteristic zero permits all integer divisions, giving
w in A'[1/P] with Nw=Nz. Thus z-w lies in Rhat[1/P]. Consequently z
belongs to A'[1/P], and (4) puts z in A'. Flat base change of the actual
kernel then yields
\[
\boxed{\quad
\gamma\ne0\quad\Longrightarrow\quad
\ker(N^{n+1}:\mathcal A\to\mathcal A)
      =F_n\otimes_R\widehat R\quad(n\ge0),\qquad
\mathcal A_{\rm ln}=A'.
\quad}
\tag{7}
\]
The last notation means the elements individually killed by a power of N.
It does not make N locally nilpotent on all of mathcal A. It also does not
turn A' into an ordinary polynomial ring over Rhat or descend an element
of A' all the way to A without its completed-base coefficients.

## 7. Scope, source comparison, and remaining gap

Equations (2)--(4) use the actual whole-fiber topology and prime-divisor
models, not only finite freeness of the degree modules. Equations (6)--(7)
add the nonzero first normal action. The remaining zero-action sector has
scalar contraction but no completed-kernel equality proved here.

The split-fiber conic xt-r squared+r=0 has two reduced closed-fiber lines.
Its extra formal invariant idempotent therefore does not contradict this
argument: the one-source-point step used in (2)--(3) fails. No connected
formal counterexample satisfying the actual divisor hypotheses is supplied.

The accessible abstract of Miyanishi's
[*Ga-actions and completions*](https://www.sciencedirect.com/science/article/pii/S0021869307006540)
concerns completion at a maximal point of the threefold and warns that
completed invariant kernels can grow. Only that abstract was read, not its
full examples. In Gurjar--Koras--Masuda--Miyanishi--Russell,
[*A1-star-fibrations on affine threefolds*, Lemma 3.5 and Proposition 3.6](https://sci-tech.ksc.kwansei.ac.jp/~kayo/cmn/papers/montreal_revised2.pdf),
the relevant fiber is integral and fixed-point-free. Our double fails both
hypotheses. Its resulting inverse-limit constant ring is not identified with
the original completed base. Those displayed statements and proofs were
read completely. The proof's intermediate claim about an infinite series
having an infinitely generated derivative span is not valid in general;
its locally nilpotent polynomial conclusion instead follows directly by
differentiating the series sufficiently many times in characteristic zero.
Neither paper is used to prove (2)--(7).

Fresh retained reads include complete92 ramification, complete96 dependency
audit, complete107 divisor classification, and the current112 proofs and
checkpoint. The new contribution is their ramified completion application
and the weighted invariant-kernel induction. No numerical method was added
or executed. All files through112 remain unchanged. Independent model
reconstruction is not human expert review, a formal verification, or a
source-novelty determination.

[^curve]: The Stacks Project,
    [normalization of curves, Lemmas 33.41.1--2](https://stacks.math.columbia.edu/tag/0C44),
    and [DVR extensions, Remark 15.113.6](https://stacks.math.columbia.edu/tag/09E8).
    Both complete displayed statements and proofs or deductions were read.
    The deeper Nagata and Krull--Akizuki dependencies were not re-proved.
    The conductor argument above supplies the particular fraction-field
    comparison used here.

[^completion]: The Stacks Project,
    [finite-module completion00MA](https://stacks.math.columbia.edu/tag/00MA),
    [completion flatness00MB](https://stacks.math.columbia.edu/tag/00MB),
    and [Krull intersection00IQ](https://stacks.math.columbia.edu/tag/00IQ).
    Their complete displayed statements and proofs were freshly read.
    These apply to finite modules over A' or to the finite curve rings;
    they are not applied directly to the R-linear kernel operator on A.
