# A quadratic coordinate constrains the invariant threefold

One original coordinate of quadratic slice degree already forces
an exact smooth critical-value function and a family of quadratic
field extensions. The other original coordinates may have arbitrary
slice degrees. This broadens the preceding restricted-frame analysis,
but still does not identify the invariant threefold as affine space.

An actual example has a smooth critical-value function which cannot
be a slice of any locally nilpotent derivation on the localized base.
Another actual example has a repeated raw discriminant factor despite
smooth coordinate fibers. These prevent two invalid promotions of
necessary conditions to recognition.

## 1. Broader hypotheses and the critical-value theorem

Keep the actual polynomial cylinder and one original coordinate:
\[
\begin{gathered}
B=A[s]=\mathbb C[x_1,x_2,x_3,z],\quad E=\partial_s,\quad
A=\ker E,\quad E^3z=0,\quad q=E^2z\ne0,\\
g=\gcd(q,Ez),\quad h=q/g,\quad
z=w+gvs+(gh/2)s^2,\quad g,h,v,w\in A,\quad\gcd_A(h,v)=1.
\end{gathered}
\tag{1}
\]
No equation E squared x_i=0 is required in this pass. The slice
ensures A is smooth and factorial, but no polynomial coordinate
system for A is presumed. Consequently the speed-ideal conclusions
from the more restrictive pass85 do not transfer automatically.

The original coordinate partial sends z to one. Expand its action
on A in powers of s and evaluate its coefficient derivation at
s=-v/h. The [complete differential proof](coordinate-critical-value-constraints-pass86.md)
shows that this gives a derivation D_* of A_h with
\[
r=w-\frac{gv^2}{2h},\qquad D_*(r)=1,
\qquad L_\lambda=2h(w-\lambda)-gv^2=2h(r-\lambda).
\tag{2}
\]
Thus r has no critical points on D(h), and each L_lambda=0
hypersurface there is smooth or empty. No inversion of g is needed.
The proof uses the actual coordinate differential, not an assumed
polynomial presentation of A.

In the retained two-speed frame A_h=C[a,a inverse,b,b inverse,c],
the function r is genuinely quadratic in c. Every LND of this ring
kills its units a,b and extends to a translation derivation over
C(a,b) in the single variable c. Such a derivation cannot send a
genuinely quadratic polynomial to one. Hence smoothness in (2) does
not supply an LND slice, even for an actual already-polynomial base.

## 2. Every original coordinate fiber constrains the discriminant

For every complex lambda the original coordinate fiber
B_lambda=B/(z-lambda) is C^[3]. The map from A into it is injective
by s-degree additivity: a nonzero multiple of z-lambda has degree
at least two and cannot be a nonzero element of A. Localizing that
domain at K=Frac(A) gives a quadratic field. The
[fiber and discriminant proof](coordinate-fiber-discriminant-pass86.md)
deduces
\[
\begin{gathered}
[\operatorname{Frac}B_\lambda:K]=2,\qquad
-gL_\lambda\notin K^2,\qquad \gcd_A(g,w-\lambda)=1,\\
L_\lambda\text{ is squarefree in }A_h,
\qquad \gcd_{A_h}(g,L_\lambda)=1.
\end{gathered}
\tag{3}
\]
The squarefree statement concerns L_lambda on D(h), not the raw
discriminant -gL_lambda. The actual action with common factor
g=(a-1)^2 and h=a^3 retains a repeated factor in the latter. Both
polynomial inverse orders and its global slice are explicitly checked.

The embedding into a polynomial three-ring is an elementary
positive-slice-degree argument, not a new cancellation principle.
A generically two-to-one map from affine three-space to the candidate
variety is not an isomorphism.

## 3. The exact modification and the remaining source gate

On R=A_h, set y=hs+v and Y=gy. The exact ring picture is
\[
\begin{gathered}
(B_\lambda)_h=R[y]/(gy^2+L_\lambda),\qquad
\mathcal S_\lambda=R[Y]/(Y^2+gL_\lambda),\\
(B_\lambda)_h=\mathcal S_\lambda[Y/g]
=\mathcal S_\lambda[U]/((gU-Y):g^\infty).
\end{gathered}
\tag{4}
\]
The cover S_lambda is finite free of rank two over R. Its modification
shares its fraction field, but need not be finite over it. Saturation
is essential: naive elimination leaves an extra factor g in the
relation. Where g=0 and L_lambda is nonzero, the cover has a point
but the modification does not, so it cannot be identified with an
integral normalization there.

The [primary-source audit](quadratic-coordinate-modification-source-pass86.md)
checks the modification definition and relative-coordinate
theorems.[^modification] The closest checked cancellation statement
allows an unknown coefficient algebra C but requires C[t] to be a
relative polynomial three-ring with two companions to the prescribed
coordinate. Here A[s] has three companions to z and is a four-ring.
Declaring an unknown invariant to be a base coordinate would assume
the missing conclusion.[^das]

Likewise z is an absolute complex coordinate but is not a coordinate
of K[s] over K, because its degree is two. Residual-coordinate results
over A therefore cannot be applied to z. These are limitations of
the checked statements, not proof that no applicable theorem exists.

## 4. Evidence and the next mathematical decision

The [targeted capture](verification-pass86-working.json) passes two
methods, with three actual actions covered through subtests. The
written general proofs have separate AI reconstructions; finite
symbolic checks do not establish their universal quantifiers. See
the [proof audit](proof-audits-pass86-working.md) and
[checkpoint](checkpoint-pass86-working.json). No full regression,
exhaustive action search, human review or formal verification ran.

The next recognition question must exploit more than a smooth
critical-value function or an affine-modification presentation. A
bounded next case is constant nonzero q, when completing the square
is global and each original coordinate fiber carries a regular
involution. Its precise relationship to existing three-dimensional
involution theorems must be checked before any linearization argument
is used. This does not replace the full cancellation objective with
that special case.

General complex-threefold cancellation remains unproved. The
professor's intended correction, dimension and field are still
unconfirmed; no publication, external contact or novelty claim is made.

## Sources

[^modification]: Kaliman and Zaidenberg,
    [*Affine modifications and affine hypersurfaces with a very transitive
    automorphism group*](https://arxiv.org/pdf/math/9801076),
    Definition 1.1 and Proposition 1.1. The explicit algebra in (4)
    is verified in the linked source-scope note.

[^das]: P. Das, [*On cancellation of variables of the form bT^n-a over
    affine normal domains*](https://arxiv.org/pdf/2002.02129),
    Theorem 3.4, PDF p.7. Its relative dimension and prescribed
    coordinate hypothesis are not dropped here.
