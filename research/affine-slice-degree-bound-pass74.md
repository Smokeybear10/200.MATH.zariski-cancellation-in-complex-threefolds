# An explicit adapted-degree bound for affine-linear sliced actions

For an affine-linear locally nilpotent derivation of the actual complex
polynomial four-ring, a supplied slice of ordinary degree at most
\(d\) admits an adapted polynomial coordinate system with forward
degree at most \(\max(4,d)\) and inverse degree at most \(4d\).
Both inverse maps are constructed below. This supplies an explicit
seed for the bounded-family formulation of pass73.

Recognition of sliced affine-linear actions is standard linear
algebra and the slice-flow construction. No novelty is claimed for
that recognition or construction. The purpose here is to retain an
explicit degree bound while adapting to the particular supplied slice,
not merely to an easier replacement slice. Nothing here reduces an
arbitrary polynomial action to an affine-linear one.

## 1. Statement and relation to the existing finite-family program

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad
E(x)=Nx+p,
\]
\[
N\in\operatorname{Mat}_4(\mathbb C),\quad p\in\mathbb C^4,
\qquad E(s_*)=1,\qquad \deg_x s_*\le d.
\tag{1}
\]
The column \(x\) is the displayed actual polynomial coordinate
system. All degrees in this note are ordinary total degrees in the
specified polynomial variables. Since a slice cannot be constant,
\(d\ge1\).

**Proposition.** There are polynomial maps
\[
F(x)=(F_1(x),F_2(x),F_3(x),s_*(x)),\qquad
G(U_1,U_2,U_3,S)
\]
such that
\[
G(F(x))=x,\qquad F(G(U,S))=(U,S),\qquad
E(F_i)=0\quad(1\le i\le3),
\]
\[
\deg F\le\max(4,d),\qquad \deg G\le4d.
\tag{2}
\]
In particular \(\ker E=\mathbb C[F_1,F_2,F_3]\).

The [all-inverse-pairs construction](universal-frame-search-pass43.md)
already formulates exact degree-bounded witness equations.
The [bounded-family note](universal-family-degree-boundary-pass73.md),
Section 5 and equation (8), adds the adapted conditions
\(F_4=s_*\) and \(E(F_1)=E(F_2)=E(F_3)=0\).
Its uniform-degree assertion is conditional and non-effective for
general coefficient degree. The present proposition constructs these
adapted witnesses for coefficient degree at most one.

The earlier [affine-linear control](three-variable-quadratic-frame-pass42.md),
Section 7, already uses a finite nilpotent flow to produce actual
inverse coordinates for a particular sliced linear action.
It is credited as an existing instance of the same mechanism.
A bounded search of the retained degree and frame notes found no
previous statement of the present \(4d\) bound for every supplied
slice in (1). This is a project deduplication statement, not a
literature-priority claim.

## 2. A linear slice exists for this actual affine action

Induction gives, for every \(j\ge1\),
\[
E^j(x)=N^j x+N^{j-1}p.
\tag{3}
\]
Local nilpotence on the four generators makes the left side zero
for all sufficiently large \(j\). Comparing linear coefficients
shows that \(N\) is nilpotent. Since it is a four-by-four matrix,
\(N^4=0\). In particular \(E^5(x)=0\).

Furthermore \(p\notin\operatorname{im}N\). Otherwise there would
be \(x_0\in\mathbb C^4\) with \(Nx_0+p=0\), and evaluation of
\(E(s_*)\) at that point would give
\[
1=E(s_*)(x_0)=\sum_i (Nx_0+p)_i
                  \frac{\partial s_*}{\partial x_i}(x_0)=0.
\]
Thus the actual slice rules out an affine fixed point.

Linear algebra now supplies a row \(\ell\in(\mathbb C^4)^*\)
that vanishes on \(\operatorname{im}N\) and has \(\ell(p)=1\).
Define the linear polynomial \(w(x)=\ell x\). Then
\[
\ell N=0,\qquad \ell p=1,\qquad E(w)=1.
\tag{4}
\]
This is an actual linear slice, not an assumed coordinate extracted
from a nonlinear local slice. Conversely, nilpotence of \(N\)
and \(p\notin\operatorname{im}N\) already give (4), so these
are exactly the elementary affine conditions for a slice here.
No corresponding fixed-point criterion is asserted for nonlinear
actions.

## 3. Polynomial projection to the linear slice plane

The actual polynomial flow of (1) is
\[
\Phi_t(x)=
\sum_{j=0}^{3}\frac{t^j}{j!}N^j x
+\sum_{j=0}^{3}\frac{t^{j+1}}{(j+1)!}N^j p.
\tag{5}
\]
This follows either from (3) or directly by solving the affine
polynomial differential equation. Its group law
\(\Phi_t\circ\Phi_v=\Phi_{t+v}\) is a polynomial identity
in independent parameters. Formula (4) gives
\(w(\Phi_t(x))=w(x)+t\).

The total degree of (5) in \((x,t)\) is at most four.
The terms \(t^jN^j x\) have degree at most \(j+1\le4\),
and the constant-vector terms have degree at most \(j+1\le4\).
The last, fourth-power flow term must be retained even though
\(N^4=0\).

Let \(H=\{w=0\}\), a three-dimensional linear plane. Choose
a complex linear isomorphism \(\iota:\mathbb C^3\to H\)
and linear forms \(u_1,u_2,u_3\) on \(\mathbb C^4\) whose
restrictions form its inverse. Write \(u=(u_1,u_2,u_3)\).
Define
\[
\pi(x)=\Phi_{-w(x)}(x),\qquad
U(x)=u(\pi(x)),\qquad
\Psi(U,W)=\Phi_W(\iota(U)).
\tag{6}
\]
Then \(\pi(x)\in H\), \(\pi|_H=\operatorname{id}_H\),
and all entries of \(\pi\) and \(U(x)\) have degree at most
four. Also \(\deg\Psi\le4\).

The exact inverse identities are
\[
\Psi(U(x),w(x))=x,\qquad
(U(\Psi(U,W)),w(\Psi(U,W)))=(U,W).
\tag{7}
\]
Indeed, the first is
\(\Phi_{w(x)}\Phi_{-w(x)}x=x\), because
\(\iota(u(\pi(x)))=\pi(x)\).
For the second, \(w(\iota(U))=0\) gives
\(w(\Psi(U,W))=W\), and projection by \(\Phi_{-W}\)
recovers \(\iota(U)\).

Moreover \(\pi(\Phi_t(x))=\pi(x)\), by the same group law
and the identity \(w\Phi_t=w+t\). Differentiating this
polynomial identity at \(t=0\) yields \(E(U_i)=0\).
Thus (7) gives actual polynomial coordinates \((U,w)\)
and makes \(E=\partial_w\) in those coordinates.
No conclusion is deduced merely from a Jacobian determinant.

## 4. Adapting to the supplied slice without losing its degree bound

Define the polynomial in three independent variables
\[
h(U)=s_*(\iota(U)).
\tag{8}
\]
Since \(\iota\) is linear, \(\deg_U h\le d\).
This restriction bound is the reason no extra factor four is
needed in the degree of \(h\).

The slice identity gives
\(s_*(\Phi_t(x))=s_*(x)+t\) as an exact polynomial identity.
Applying it to \(x=\iota(U)\) and using (7), we obtain
\[
s_*(x)=w(x)+h(U(x)).
\tag{9}
\]
Thus the maps in the proposition are explicitly
\[
F(x)=(U(x),s_*(x)),\qquad
G(U,S)=\Phi_{S-h(U)}(\iota(U)).
\tag{10}
\]
These are the inverse pair (7) composed with the genuine triangular
change \((U,W)\mapsto(U,W+h(U))\).
Consequently both inverse equations in (2) hold, with the fourth
forward coordinate equal to the original supplied slice itself.
The first three coordinates are invariant, so in this presentation
\(E=\partial_S\) and its kernel is exactly their polynomial ring.
No four-variable invariant-coordinate recognition theorem is used.

For the forward map, its first three components have degree at
most four and its last component has degree at most \(d\).
For the inverse, set \(T=S-h(U)\), so \(\deg_{U,S}T\le d\)
because \(d\ge1\). In (5) the variable-vector terms become
\(T^jN^j\iota(U)/j!\), of degree at most
\(jd+1\le3d+1\le4d\). The constant-vector terms become
\(T^{j+1}N^jp/(j+1)!\), of degree at most \((j+1)d\le4d\).
This proves exactly the two estimates in (2), including \(d=1\).

## 5. Finite-family consequence and limitations

In the notation of pass73, every complex point of
\(\mathscr S_{1,d,N_0}\), for every fixed coordinate nilpotence
bound \(N_0\), has an adapted inverse witness at level \(4d\).
Thus
\[
\mathscr S_{1,d,N_0}(\mathbb C)
=C_{4d}^{\mathrm{ad}}(\mathbb C),
\tag{11}
\]
where the right side is the adapted witness image inside that
parameter scheme. Empty families are included vacuously.
All affine-linear sliced actions already satisfy \(E^5x=0\)
by (3), independently of their supplied slice degrees.

This is an effective degree bound for this particular coefficient
degree, not just the non-effective implication of constructible
exhaustion. The choices of \(\ell\), \(\iota\), and \(u\)
require only finite-dimensional linear algebra for a given input.
No single choice regular over the entire parameter scheme is claimed.
For symbolic or algorithmic input, computation of its coefficients
still requires an exact presentation of those input constants.

The action is required to be affine-linear in a known actual
coordinate frame. A nonlinear polynomial coordinate change can
destroy that ordinary-degree condition. The proposition neither
finds such a frame for an arbitrary sliced LND nor recognizes a
new unrestricted cancellation case. It does not assert optimality
of \(4d\), a bound for coefficient degree at least two, or a
universal bound independent of the supplied slice degree.
The forward condition \(F_4=s_*\) itself precludes a bound
independent of \(d\) when supplied slices of increasing actual
degree are allowed.

## 6. Verification and provenance

The argument above is elementary and self-contained: matrix
nilpotence, exclusion of a fixed point, a linear slice, the finite
polynomial flow, and both actual inverse equations. It uses no
external recognition or constructibility theorem to obtain (2).
The finite-family terminology and adapted witness equations are
credited to passes43 and73; the earlier special affine-flow control
is explicitly retained in Section 1.

No new numerical method, full regression, human expert review,
proof-assistant verification, or historical novelty claim is made
by this proof note. Any independent finite controls and their actual
run results are separate evidence. No frozen pass73-or-earlier file
or shared metadata is changed by this note.
