# The unavoidable singular first modification at the nodal plinth

The still-compatible action \(u\delta_0\) has not been realized in
affine three-space or ruled out. There is a stronger construction
requirement than the earlier exclusion of selected one-step models:
**every minimal ambient local slice would have a globally monic
quadratic first center, and its first modification would be singular
along a doubled-line fiber at the node.**

Thus a hypothetical smooth ambient realization must strictly enlarge
this actual first modification. Its three free orbits over the node
would each be contracted to a point in that modification's fixed line.
This identifies an unavoidable stage and its defect; it does not prove
that further modifications cannot repair it.

## 1. Exact conditional setting

Retain the surface and action of
[pass 32](ambient-residue-obstruction-pass32.md):
\[
B_0=\mathbb C[u,y,z]/(A z-y(y-1)),\quad
A=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3,
\qquad D=u\delta_0,
\quad\delta_0y=A,\quad\delta_0z=2y-1,\quad\delta_0u=0.
\tag{1}
\]
The shared conductor parameters in this formula are unchanged.
For the normalized invariant base use a different letter
\(s=u^2\), and write
\[
S=\mathbb C+d\mathbb C[s],\qquad
T=\ker D=\mathbb C+d\mathbb C[u],\qquad
v=ds,
\]
\[
S=\mathbb C[d,v]/(v^2-d^2(d+1)),\quad
\mathfrak n=(d,v)=d\mathbb C[s],\quad
T=S\oplus du\mathbb C[s].
\tag{2}
\]
The presentation uses independent generators before identifying their
images. In particular \(S\), not \(T\), is the forced image of
the ambient invariant ring.

Assume a hypothetical primitive LND \(E\) of
\(W=\mathbb C[X,Y,Z]\), a prime invariant \(F\), and an
identification \(W/(F)=R\) taking \(\overline E\) to \(D\).
Let \(C=\ker E=\mathbb C[f,g]\). The residue theorem gives
\(C/(F)=S\) as the actual embedded subring of \(R\). Denote by
\(\mathfrak m\subset C\) the maximal ideal above \(\mathfrak n\).
The base curve has an ordinary node there, so
\[
F\in\mathfrak m^2.
\tag{3}
\]
Here and below the invariant \(F\) is also regarded as its polynomial
in the two generators of \(C\).

The full ambient plinth is principal, say \(E(W)\cap C=aC\).
The [pass-25 argument](ambient-lifting-pass25.md) implies \(F\mid a\):
otherwise localization at the prime \((F)\) supplies a slice and
surjective integration, whereas the restricted invariant field is
the quadratic extension \(\mathbb C(u)/\mathbb C(s)\). Write
\[
a=F^k\beta,\qquad k\ge1,\qquad F\nmid\beta.
\tag{4}
\]
Other plinth factors and their possible passage through the node are
not excluded. Choose a minimal local slice \(r_0\in W\), meaning
\(E(r_0)=a\), a generator of the full plinth, not just a nonzero
element of it.

## 2. Every minimal slice has a nonzero quadratic residue

Since \(F\mid a\), the residue \(\bar r_0\) lies in \(T\).
It cannot lie in \(S\). If it did, choose an invariant lift
\(c_0\in C\) of that element. Then
\(r_0-c_0=Fq\) for \(q\in W\), so
\[
E(q)=a/F\in C.
\]
This contradicts \(E(W)\cap C=aC\): in the domain \(C\),
\(a/F\in aC\) would imply that \(F\) is a unit.

By (2), write \(\bar r_0=c(s)+du\,b(s)\), with \(c(s)\in S\)
and nonzero \(b\in\mathbb C[s]\). Subtracting an invariant lift
of \(c(s)\) changes neither the plinth generator nor minimality.
The resulting slice \(r\) therefore satisfies
\[
E(r)=a,\qquad \bar r=du\,b(s),\qquad b\ne0.
\tag{5}
\]
This is a residue normalization of a genuine ambient slice. It does
not claim that \(u\), \(s\), or \(b(s)\) themselves lift to ambient
invariants.

Its square belongs to the smaller base:
\[
\bar r^2=d^2s\,b(s)^2\in\mathfrak n^2=d^2\mathbb C[s]\subset S.
\tag{6}
\]
The equality \(\mathfrak n^2=d^2\mathbb C[s]\) follows directly
from \(\mathfrak n=d\mathbb C[s]\). Choose any invariant lift
\(K\in C\) of (6). Every such lift satisfies
\[
K\in\mathfrak m^2:
\tag{7}
\]
membership of its residue in \(\mathfrak n^2\) gives
\(K\in\mathfrak m^2+(F)\), and (3) removes the final summand.

The minimal polynomial of \(\bar r\) over
\(\operatorname{Frac}S=\mathbb C(s)\) is exactly
\[
Z^2-d^2s\,b(s)^2.
\tag{8}
\]
Indeed \(s\) is not a square in \(\mathbb C(s)\), and multiplying
it by the nonzero square \(d^2b^2\) does not change that fact.
In particular \(\bar r\) has degree two, irrespective of the
degree or zeros of \(b\).

## 3. The exact global first center

The slice \(r\) is transcendental over \(C\). For example, applying
\(E\) to a polynomial relation and descending its degree contradicts
\(E(r)=a\ne0\) in characteristic zero. Thus \(C[r]\) is an actual
polynomial subring of \(W\).

Its first \(F\)-center is not merely generically principal:
\[
\boxed{C[r]\cap FW=(F,r^2-K)C[r].}
\tag{9}
\]
To prove equality, reduce modulo \(F\). The resulting homomorphism
\(S[Z]\to R\) sends \(Z\) to \(\bar r\). Divide any element
of its kernel by the monic polynomial (8). A remainder has the form
\(a_0+a_1Z\) with \(a_i\in S\). Its evaluation vanishes only if
both coefficients vanish, by degree two over \(\mathbb C(s)\).
Thus the kernel is precisely the principal ideal (8). Taking the
preimage in \(C[r]\) proves (9).

The associated actual first modification inside the unknown \(W\) is
\[
W_1=C\left[r,\frac{r^2-K}{F}\right]
\cong C[r,Y]/(FY-r^2+K).
\tag{10}
\]
The displayed quotient is a domain and the presentation is exact:
\(F\) and \(r^2-K\) are coprime in the UFD \(C[r]\), the latter
being monic in \(r\). The polynomial linear in \(Y\) is primitive,
and its kernel in \(C[r,F^{-1}]\) is precisely the displayed relation.
This is the standard affine-modification construction, now with the
global center determined by the fixed surface.[^modification]

The restriction of the actual ambient derivation has formulas
\[
E|_C=0,\qquad E(r)=F^k\beta,\qquad
E(Y)=2rF^{k-1}\beta.
\tag{11}
\]
They follow by differentiating \(FY=r^2-K\). Hence \(W_1\)
is an invariant subalgebra, without a newly postulated derivation or
an unverified model substitution.

## 4. The first stage is necessarily singular at the node

Take polynomial coordinates \(f-f(q),g-g(q)\) for the maximal
ideal \(\mathfrak m\) of the ambient invariant plane. The relation
in (10), viewed in four polynomial variables, has vanishing gradient
at every point
\[
f=f(q),\qquad g=g(q),\qquad r=0,
\qquad Y\text{ arbitrary}.
\tag{12}
\]
Indeed \(F,K\in\mathfrak m^2\); the derivatives in \(r,Y\)
are \(-2r,F\), and the other two derivatives are those of
\(FY+K\). They all vanish at (12). The relation is irreducible,
so these are singular points of the three-dimensional hypersurface.
The entire scheme fiber is exactly
\[
W_1/\mathfrak mW_1=\mathbb C[r,Y]/(r^2),
\tag{13}
\]
a doubled affine line. The restricted field (11) is zero on its
reduced line, for every \(k\ge1\), including when other factors
of \(\beta\) vanish at the node.

Since the hypothetical final \(W\) is smooth, necessarily
\[
W_1\subsetneq W.
\tag{14}
\]
This holds for every minimal local slice and every lift \(K\) after
the normalization (5). It is stronger than excluding (10) under an
assumed one-step normal form: (9)-(10) construct an unavoidable
subalgebra of every alleged realization.

For the actual final surface, the inherited exact conductor identity
is
\[
\mathfrak nR=(d,v)R=I,\qquad R/I=\mathbb C[t]^3.
\tag{15}
\]
Thus the final node fiber has three reduced disjoint affine lines,
and \(D(t)=1\) on each. The equivariant morphism
\(\operatorname{Spec}W\to\operatorname{Spec}W_1\) maps each of
these three orbits to a point on (12). Algebraically, (11) vanishes
on the reduced target fiber, whereas each source line has translation
derivation \(\partial_t\); the pullbacks of its target coordinate
functions are therefore constant on each source line. This permits
coincidence of the three image points and does not assert their
distinctness.

## 5. Generic fibers and the precise source boundary

The exact base map is the normalization map \(u\mapsto s=u^2\)
followed by the nodal identification \(s=1\sim s=-1\). Away from
the node and \(s=0\), the fiber consists of two reduced affine
lines. At the smooth base point \(s=0\), the conductor is absent,
\(A(u)\) is a unit modulo \(u^2\), and the fiber ring is
\[
\mathbb C[u,y]/(u^2).
\tag{16}
\]
The reduced line is exactly the fixed locus of \(D\) on the surface.
There is no inference that this double fiber determines the exponent
\(k\) in (4). The first-stage theorem allows every positive \(k\).

Masuda's general fiber theorem gives an integer at least the degree
of the initial minimal polynomial. In the present case the two
numbers both equal two. Her general localized description may invert
an invariant that vanishes at this node; it cannot itself justify a
smooth or one-step description here.[^generic] Conversely, our monic
quadratic argument proves the unlocalized first center despite the
nonfactorial nodal base. It supplies no theorem describing all later
centers.

The [pass-25 proof](ambient-lifting-pass25.md) already shows that
\(S\to R\) is faithfully flat and that \(T\) needs two relative
algebra generators at the node. Those facts are consistent with
(9)-(16). They do not turn the strict inclusion in (14) into an
impossibility theorem. A remaining construction must supply later
equivariant modifications with the correct restricted invariant
algebra, three free node orbits, and final ambient polynomial ring.
Alternatively one needs a theorem excluding all such later stages.
Neither has been obtained here.

This note does not decide the three-generator embedding question,
construct a primitive ambient action, or claim novelty, expert review,
or formal proof verification.

## Finite exact controls

The standalone [nodal_plinth_checks_pass33.py](nodal_plinth_checks_pass33.py)
imports only unittest and SymPy. Its finite methods support the trace
normalization, monic quadratic center, node-ideal membership, singular
doubled-line first fiber, derivation identities, and the actual doubled
fiber at \(s=0\). They do not instantiate the unknown \(W\), prove
that a later repair exists, or replace the universal arguments above.
The initial targeted run passed all five methods in 0.106 seconds.

```
/opt/anaconda3/bin/python research/nodal_plinth_checks_pass33.py
```

## Primary sources actually read

[^modification]: Kayo Masuda, [*Factorial affine Ga-varieties with principal plinth ideals*](https://arxiv.org/html/2312.05455), Section 2's affine-modification definition and Lemma 2.2 with proof, and Section 3 through the complete proof of Lemma 3.2 were directly read. They define the first center and establish the localized general mechanism. Formula (9) has its own global proof using the specific trace and norm in (2), not the unsupported assumption that the nodal quotient ring is factorial.

[^generic]: Masuda, same primary text, Theorems 3.8-3.9 and the complete proof of Theorem 3.9 were directly read. The localization in Theorem 3.8 and generic-fiber scope in Theorem 3.9 are retained. No claim is made about the complete literature on possible nodal plinth components. The ambient polynomial kernel, principal plinth, and the fixed surface calculations are the precise inherited inputs linked above.
