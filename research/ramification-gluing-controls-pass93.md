# Exact finite curve and support-lattice controls

The standalone [ramification_gluing_controls_pass93.py](ramification_gluing_controls_pass93.py)
uses only Python's standard library. It checks the concrete integer
columns and finite curve-ring formulas in
[reducible-ramification-support93](nonconical-reducible-ramification-support-pass93.md).
It does not construct a threefold, an exceptional surface or an
original polynomial inverse frame.

There are exactly two unittest methods.

The first checks the four displayed profiles (4,1), (5,1), (4,1,1)
and (4,2). It computes integral determinants, nonnegative weighted
column images, the component count and the gcd/lcm identity.
For the crossing lattice, the exact coordinates (x,z) have the
integral inverse (x,2z-x,z); the determinant is therefore computed
in the entire lattice, not merely in its rational span.
Support labels record which normalization points are glued to
one actual point of the finite source curve.

Two negative controls are separate from the positive examples.
The columns (2,2) and (1,0) have the desired weighted values
(4,1), but determinant of absolute value two, so they are not
a full integral basis. The columns (3,1) and (1,0) are a full
basis with the correct weights but have incompatible support if
the two normalization points are left unglued. The crossing
columns likewise fail when all three actual point labels differ.
An additional malformed column pair is rejected for not lying
in the crossing lattice at all.

The second method uses exact ascending integer-coefficient
polynomials. For n=2,3 it checks every product of the displayed
module basis of C_n against its independent expansion in Z[w].
It checks associativity on all basis triples, the unit, and the
square-zero products of nonconstant basis classes after t=0.
The basis and its independence are the explicit module
description proved in the source note; the tests do not claim
to derive arbitrary module freeness from a sampled rank.
The derivative identity w times dt/dw equals n(t+1) checks the
stated unramified normalization indices.

For the crossing curve, it checks the actual polynomial pairs
1, beta=(t w,0), alpha=(0,a), together with the base images t,s.
All satisfy f(1)=f(-1)=g(0). Exact multiplication gives
beta squared equal to t squared times (t+1), alpha squared
equal to s, alpha times beta equal to zero, and the required
mixed base annihilations. These identities give the indicated
square-zero nonconstant products in the fiber t=s=0, using the
following elementary module description. Split f(w) into even
and odd parts. Its odd part is divisible by w(w squared minus one)
because f(1)=f(-1); its even part is a polynomial in t.
Split g(a) similarly into a polynomial in s plus a times a
polynomial in s. The two even parts have the same constant.
Thus the direct module decomposition is G times 1, plus C[t]
times beta, plus C[s] times alpha. Parity proves uniqueness.
The fiber therefore has the three basis classes 1, beta, alpha.
The derivative calculations retain
indices (1,1) and (2), rather than treating all points as unramified.

These are finite curve-ring and lattice controls only.
In particular, the smooth-base versions are not asserted to
satisfy every necessary condition on a rank-zero component.
The final conditional smooth-branch restriction in the source
note excludes an unramified entry of value one in such a column.
Its singular-base variants and the universal geometric proof
are not certified by this checker. No arbitrary positive basis
is promoted to actual Thom classes.

## Execution and provenance

The first author run used:

    /opt/anaconda3/bin/python research/ramification_gluing_controls_pass93.py

It passed both methods in 0.006 unittest seconds, exit zero,
with complete tool output in chunk 849494. No assertion failed.
The author subsequently read the full saved checker through EOF.
The source note was independently read in its original
eight-equation form and its final ninth-equation smooth-branch
delta was then read separately. No source theorem, infinite
search, solver import, full regression, runner or canonical
capture was introduced by this author.

Checker SHA-256:
17666b2e2d45c700b807b1a00b22905abd845f177ffa6bd20eb7bb346d919103.

Independent reviews, any independent reruns and Root's later
integration capture are separate evidence. All pass92 and
earlier artifacts remain unchanged.
