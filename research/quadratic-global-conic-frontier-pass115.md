# A global conic in the supplied quadratic frame

The actual nonconical quadratic frame now has one global conic
presentation over its invariant plane. The missing free fibers have
been classified, and a coefficient-intersection argument patches the
local results. This removes the local-to-global presentation gap in
that special frame. It does not recognize the conic as affine space
or put an arbitrary cancellation input into the frame.

The working target remains the unconfirmed intended interpretation of
Luo's email: if A[u] is isomorphic to C^[4], must A be isomorphic to
C^[3]? The literal emailed conclusion A^1 has a dimensional mismatch
for general r. No field or dimension clarification has been obtained,
and no solution to the general question is claimed.

## 1. The exact advance and its assumptions

The [global patching proof115](quadratic-global-conic-patching-pass115.md)
gives actual global elements U,r and polynomials P,eta in S=C[s,t],
with P nonzero, such that

\[
\boxed{\quad
A=S[U,r]\simeq S[\mathsf U,\mathsf r]/
  (\mathsf r^2-2P\mathsf U+\eta),\qquad
NU=r,\quad Nr=P,\quad I_1=I_2=PS.
\quad}
\tag{1}
\]

This is an actual algebraic presentation, not an isomorphism of formal
neighborhoods. Its proof keeps the complete supplied-frame hypotheses:
the original constant-acceleration coordinates, the canonical primitive
locally nilpotent derivation N, the full invariant polynomial plane,
faithful flatness, the generic polynomial line, the specified good
generators of degree at most two and third generator of degree at most
four, and their actual divisor noncollapse. The polynomial cylinder
supplies smoothness, factoriality and contractibility used by the
supported topology. None of these extra frame hypotheses is asserted
for an arbitrary sliced action.

The distinction between three claims is essential.

| Claim | Status in this investigation |
| --- | --- |
| Classify and patch the supplied quadratic frame into (1) | Written conditional proof, with independent AI reconstructions |
| Deduce A=C^[3] from that frame and (1) | Open |
| Prove arbitrary complex-threefold cancellation | Open, including entry into a suitable frame |

All derivative modules have the global alternating basis
U^i,rU^i in their respective degrees 2i,2i+1. Thus the j-th derivative
image is P^ceil(j/2) S. No assumption that an image ideal is reduced
or that P is a polynomial coordinate is made.

## 2. Free fibers: why the previous fixed-fiber result was insufficient

The [fixed-fiber theorem114](whole-double-universal-frontier-pass114.md)
already gave I2=I1 at every closed fiber containing a fixed point.
It did not address the remaining reduced fibers. The retained bounds
allowed one, two or three disjoint translating lines there. Those
cases had to be treated before the global ideal equality could be used.

The [complete free-fiber proof115](free-quadratic-fiber-conic-pass115.md)
does this in four steps. First, for U in F2 the invariant expression
2(N squared U)U-(NU) squared restricts to the same constant on every
component. On at least two translating components, the degree bound
forces N squared U to vanish at the base point. A nonzero residue
derivative must therefore have constant values d or minus d on every
component, with d nonzero. In that case U is a coordinate on all of
them, so three components would contradict its generic degree at most
two. Hence every quadratic derivative vanishes on a three-line fiber.

Second, this derivative vanishing makes the good generators constant
on each component. They separate the components, while the actual
third generator is a coordinate along each. A good linear combination
G generates the three-dimensional algebra of constants. The full-image
quartic presentation107 and the proper-image divided-quartic110
contradictions both apply after their exact algebraic hypotheses are
reconstructed with D=C cubed. Neither argument depends on nilpotents
in D. This excludes three free components.

Third, suppose two components admit a nonconstant U in F2. The generic
extension K(NU)/K(U) is quadratic. The actual semilocal algebra is
finite free of rank two over the regular projection base: its generic
rank and residue dimension agree, invoking the complete flat-rank
lemma93. Multiplication by NU has generic trace zero, so it has trace
zero after reduction. The two nonzero derivative values must be
opposite, not equal. Therefore 1 and NU have independent residues.
They split F1 inside F2; principality and the exact divisor valuations
give I2=I1. This trace step needs actual finite freeness. The square
identity by itself permits the wrong equal-sign possibility.

Finally, the remaining two-component alternative would kill every
quadratic derivative. Its constant algebra is C[G]/(G squared-G).
The conic coefficient extraction differs from the earlier whole-double
calculation by an exact idempotent correction:

\[
\widetilde B_2=B_2-\epsilon a^2/2,\qquad
\widetilde h=h+\epsilon ab/2,\qquad
P=a\widetilde h+b\widetilde B_2.
\tag{2}
\]

The sharp ideal bound is unchanged by this correction. The actual
five-column product determinant gives b squared in (htilde)+a(a,b).
These are exactly the inputs of the universal factorization114, not a
new formal-coordinate descent. The topological input needed for its
contradiction is checked separately below.

## 3. The base prime and the splitting cover must not be confused

The [supported-prime proof115](free-fiber-supported-plinth-prime-pass115.md)
uses the full integral lattice of repaired96 and the component linking
coefficient in97. Each free component has multiplicity one, so its
integer column maps to the diagonal vector of ones. A degree-two
normalized base branch with one ramified source point would force an
integer equation 2v=1 and is impossible.

If there is one component, the supported rank leaves no split branch.
Every divisor constant degree is one, the first derivative image is
a unit, and an actual local slice follows. If there are two components,
there is exactly one degree-two normalized base branch, with two
unramified source points. Consequently P is a power of a single base
prime, and that prime is unibranch at the base point. Finite curve
normalization proves it remains prime after completing the base.

This is enough for (2) and factorization114 to contradict the residual
two-component alternative. It does not say that the quadratic constant
cover remains a domain after completion. That cover splits here.
The whole-double scalar-contraction argument113 cannot be transferred
to it and is not needed. Keeping these two different primeness claims
separate prevents a false completion shortcut.

## 4. The actual global patch

Together, fixed114 and free115 give I2=I1 at every maximal ideal of S.
The section 1 of the finite rank-two module F1 is locally unimodular,
so F1/S, identified with I1, is an invertible ideal. The UFD S makes
it principal, say PS. The finite quotient I1/I2 vanishes everywhere,
so it is zero. An actual global U with N squared U=P now exists.

Set r=NU and eta=2PU-r squared. The monic conic maps injectively to A,
has the free S-basis U^i,rU^i, and equals A at every height-one base
prime by the actual divisor models. Each element of A has one finite
expansion in this basis over K. Every coefficient belongs to each
height-one localization of S and hence to S itself. This proves (1).
The general normal-domain intersection is also stated in the
[Stacks Project, Lemma 10.157.6(2)](https://stacks.math.columbia.edu/tag/031T);
the direct UFD denominator argument is sufficient here.

The resulting entire closed fibers are exactly one line when P is
nonzero, two translating lines when P vanishes and eta does not, or
one nonreduced double line when both vanish. No extra component or
hidden local algebra remains in this conditional presentation theorem.

## 5. Why the global equation is still not cancellation

The [recognition audit115](quadratic-conic-global-recognition-gates-pass115.md)
checks the exact hypotheses of published endpoints. A global free
additive action on a smooth contractible affine complex threefold gives
a product with its quotient, by Kaliman--Saveliev, Corollary 2.8(1).
With the known plane quotient that would recognize A. But N has fixed
double fibers wherever P=eta=0; (1) does not exclude those points.
[Primary theorem and proof](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf).

A second endpoint is a global modification presentation whose
denominator depends on one base coordinate. Even in that presentation,
the stable-polynomial clauses of Ghosh--Gupta--Pal, Theorem 4.8 require
ML(A)=C or DK(A)=A. A polynomial cylinder alone does not supply these
unstabilized invariants. Nor has the two-variable P in (1) been changed
into a polynomial in one base coordinate.
[Primary Theorem 4.8](https://arxiv.org/pdf/2403.17397v2).

The Russell cubic makes this distinction concrete:

\[
C_R=\mathbb C[x,y,z,t]/(x+x^2y+z^2+t^3)
 =\mathbb C[x,t][U,r]/(r^2-2x^2U+x+t^3),
\qquad U=-y/2,\quad r=z.
\tag{3}
\]

Its natural derivation has exactly the same alternating filtration and
I1=I2=x squared C[x,t]. Nevertheless its Makar-Limanov invariant is
C[x], so it is not affine three-space. That all-derivations invariant
is a published result, not inferred from the single derivation used
in this comparison.
[Dubouloz--Moser-Jauslin--Poloni, Section 2](https://arxiv.org/pdf/0903.4278).
No polynomial cylinder or realization of the original special frame
is asserted for this example. It refutes only recognition from the
listed intrinsic conic data alone.

## 6. The next precise original-coordinate question

The original coordinate reconstruction97 and (1) now put the supplied
polynomial cylinder map into a more explicit global form. Write u for
the canonical slice. There are vectors b,d,e,f in S cubed and scalars
kappa0 through kappa4 in S such that the actual original coordinates
satisfy

\[
\begin{aligned}
(x_1,x_2,x_3)^t&=b u+d U+e r+f,\\
z&=\frac q2u^2+\kappa_4U^2+\kappa_3rU
                    +\kappa_2U+\kappa_1r+\kappa_0,
\qquad q\in\mathbb C^*.
\end{aligned}
\tag{4}
\]

Indeed each invariant x_i-u Ex_i lies in F2. For the last coordinate,
the retained formula z=c+q(u squared-h squared)/2 has c in F4 and h
in F2, so its u-independent part lies in F4. The global alternating
bases give exactly (4). The speed b retains its actual unimodularity
and nonconical determinant det[b,b_s,b_t] nonzero. These statements
come from the [actual reconstruction97](original-volume-constraints-pass97.md),
not from a proposed new coordinate ansatz.

The substantive extra information is that these four expressions
generate the entire algebra A[u] as a complex polynomial algebra.
Generic independence or a nonzero Jacobian cannot replace this
original-coordinate inverse. The next task is to exploit that inverse
and the original constant-acceleration identities to constrain P and
eta enough to recognize A. Constructing more abstract conics satisfying
(1) would leave the Russell boundary unchanged.

This is still only the supplied quadratic branch. The relative cubic
branch and an entry theorem for arbitrary sliced actions remain separate
obligations. No reduction of the full goal to (4) has been proved.

## 7. Exact verification and remaining confidence limits

The [canonical capture115](verification-pass115-working.json) records
this reproducible command:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.free_fiber_trace_shift_checks_pass115 \
  research.whole_double_universal_factorization_checks_pass114 \
  research.whole_double_conormal_checks_pass112 \
  research.quadratic_degree_module_checks_pass102 \
  research.quadratic_divisor_filtration_checks_pass107
```

All eight methods passed in five suites: two new methods and six
retained methods. Elapsed time was 2.462106584 seconds; unittest
reported 2.098 seconds. The complete stdout-newline-stderr hash is
019d7e2a9c6c629380bc6bdbb0e17539cc94294fb90b3ece2a55ec809b9cf5da.
The input hashes remained unchanged during execution.

The two new methods check exact trace/sign and idempotent coefficient
identities. They do not prove finite flatness, the full supported
topology, analytic prime support, the geometric dependency chain,
all-point ideal equality, or global recognition. The new free-fiber
proof has two independent AI saved-file reconstructions; the global
patch has separate complete AI reconstructions. These are not human
expert review, Lean verification or novelty clearance.

All 721 frozen hash records through114 were freshly revalidated
unchanged. The historical full75 run remains 146 suites and 1047
methods, with registry544, without a full rerun. The
[checkpoint115](checkpoint-pass115-working.json) records exact artifact
versions, source scope, checks and the remaining proof obligations.

The last goal turn was a verified wait: the live-agent listing confirmed
two proof reviews still running. This pass is progress because it
completes the remaining free-fiber argument and actual global patch
within the stated frame. The full cancellation goal remains active.
No external contact, posting, submission, paid access, financial action
or new automation was undertaken.
