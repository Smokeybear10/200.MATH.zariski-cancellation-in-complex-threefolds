# Scalar slice filters do not lower quadratic flow in general

No constants lambda and mu make the componentwise filter
x + lambda s E(x) + mu s squared E squared(x) both lower every
quadratic-flow sliced frame to a nice frame and preserve polynomial
coordinate generation. One actual triangular action, with a specified
nonlinear slice, defeats every candidate pair at once.

More precisely, the scalar filters which preserve coordinates for
every such input are exactly nonzero slice dilations. Those preserve,
rather than lower, every element's original E-flow degree. This is
an obstruction to this particular uniform construction, not to the
existence of adapted coordinates or nice frames.

## 1. The actual coordinate frame and supplied slice

Work in B=C[a,s,b,c] with E=partial_s. Define actual coordinates
\[
x_1=s+a^2,\qquad x_2=a+(s+a^2)^2,\qquad x_3=b,\quad x_4=c.
\tag{1}
\]
This is a polynomial automorphism, not formal velocity data. Its
inverse is
\[
a=x_2-x_1^2,\qquad s=x_1-(x_2-x_1^2)^2,\qquad b=x_3,\quad c=x_4.
\tag{2}
\]
Substitution in both orders verifies the inverse. In the x frame,
\[
E=\partial_{x_1}+2x_1\partial_{x_2},\qquad
E(s)=1,\qquad E^2(x)=(0,2,0,0),\qquad E^3(x)=0.
\tag{3}
\]
Thus E is an actual LND with a global polynomial slice, and its
displayed frame has genuinely quadratic flow. The invariant ring
is already C[a,b,c]. The example is not a cancellation candidate.

## 2. One frame excludes every lowering scalar pair

For lambda,mu in C, put k=1+lambda and h=1+2lambda+2mu. The
filtered tuple is
\[
\begin{aligned}
y&=x+\lambda s E(x)+\mu s^2E^2(x),\\
y_1&=a^2+ks,\qquad
y_2=a+a^4+2ka^2s+hs^2,\qquad y_3=b,\quad y_4=c,\\
E^2(y)&=(0,2h,0,0).
\end{aligned}
\tag{4}
\]
The actual determinant, using domain coordinates (a,s,b,c), is
\[
\det\frac{\partial(y_1,y_2,y_3,y_4)}{\partial(a,s,b,c)}
=-k+4as(h-k^2).
\tag{5}
\]
Every polynomial automorphism has a nonzero constant determinant,
by the chain rule applied to its polynomial inverse. Consequently,
coordinate generation by y in this example requires k nonzero and
h=k squared. No converse to the Jacobian conjecture is being used:
sufficiency for these particular values is proved below by an inverse.

Lowering requires h=0, so the necessary coordinate condition would
give k=0, contradicting nonzero determinant. Equivalently, with h=0,
the determinant is -k-4k squared as; if k=0 it vanishes identically,
and otherwise it is nonconstant. This exhausts all scalar pairs.

In particular the proposed first-order subtraction has
\[
\lambda=-\tfrac12,\quad\mu=0,\qquad E^2(y)=0,
\qquad\det\frac{\partial(y)}{\partial(a,s,b,c)}=-\tfrac12-as.
\tag{6}
\]
It produces four nice elements, not four polynomial coordinates.
The distinction is an actual Jacobian obstruction in the original ring.

## 3. Exact classification of universally coordinate-preserving filters

Let B be any characteristic-zero domain with an LND E and a slice s.
The actual slice theorem gives B=A[s], A=ker E. For t nonzero in the
ground field, the map fixing A and sending s to ts is an automorphism:
\[
\Phi_t(f)=\sum_{j\ge0}\frac{(t-1)^j s^j}{j!}E^j(f),
\qquad \Phi_t^{-1}=\Phi_{t^{-1}}.
\tag{7}
\]
The sum is finite on every element. To verify multiplicativity and
the inverse, expand f in the actual ring A[s]; the displayed Taylor
sum is exactly substitution s by ts. The formula is not being called
the exponential of the non-locally-nilpotent derivation sE.

On an actual polynomial coordinate frame satisfying E cubed(x)=0,
equation (7) is the proposed filter with coefficients
\[
\lambda=t-1,\quad \mu=\tfrac12(t-1)^2,\quad t\ne0.
\qquad
E^r\Phi_t(f)=t^r\Phi_t(E^r f).
\tag{8}
\]
It therefore preserves coordinate generation for every quadratic-flow
frame, whatever the supplied slice or invariant algebra is. Its
inverse is a polynomial map because it is the actual automorphism
Phi inverse on B, not just an inverse over a fraction field.

Conversely, a scalar pair which works for every complex four-variable
quadratic-flow sliced frame must work for (1). Equation (5) forces
k nonzero and h=k squared, or mu=lambda squared/2 and lambda not -1.
These are exactly (8). This proves the universal scalar-filter
classification without reducing it to finitely many numerical samples.

The second identity in (8) shows that the largest nonzero E-iterate
of every nonzero element is unchanged. In particular, the true
half-slice dilation is
\[
\Phi_{1/2}(x)=x-\tfrac{s}{2}E(x)+\tfrac{s^2}{8}E^2(x),
\qquad E^2\Phi_{1/2}(x)=\tfrac14\Phi_{1/2}(E^2x).
\tag{9}
\]
It is always an automorphism in this setting, but is not a lowering
operation when some E squared(x_i) is nonzero. For arbitrary higher
flow degree, the full finite sum (7), rather than its quadratic
truncation (9), is required.

For the explicit family (1), under (8) the new entries satisfy
y_2=a+y_1 squared. Their inverse is a=y_2-y_1 squared and
s=(y_1-a squared)/t, with b,c unchanged. This directly proves the
sufficiency assertion made after (5).

## 4. Scope, positive special case and exact controls

The obstruction depends on the specified supplied slice, not on an
exotic kernel. The very same original action in (3) also has the
linear slice x_1. If that is used instead, first-order half-subtraction
gives (x_1/2,x_2-x_1 squared,x_3,x_4), which is a nice coordinate
frame with explicit polynomial inverse. Thus the negative result
does not prohibit choosing a different slice or a different method.

The slice-dilation mechanism and its preservation of flow/adjoint
orders were already separated from lowering in
[the family boundary73](universal-family-degree-boundary-pass73.md),
Section 1, and the actual Laurent dilation used in
[vertical exclusion69](vertical-top-exclusion-pass69.md). The new
content here is the all-scalar obstruction on one simultaneous
actual coordinate frame and the resulting exact classification.
No historical novelty claim is made. The separate
[all-degree scalar-filter theorem](universal-slice-filter-obstruction-pass81.md)
extends this argument to each fixed flow-degree bound d at least two.
Its arbitrary-degree coefficient proof is separate from the finite
checks described next.

The standalone [checker](quadratic_flow_filter_checks_pass81.py)
has three methods. It checks both original inverse orders, all scalar
filter coefficients and the determinant; then the true dilation
inverse, exact iterate transport on this frame, and the positive
linear-slice contrast. A third method checks degrees 2 through 6 in
the higher-degree frame x_2=a+x_1 to the power d. It verifies the
weight formula, actual flow degree and determinant, every displayed
recurrence coefficient, and the nonzero triangular coefficient-system
determinant, with the dilation specialization. Those five finite
bounds do not prove the arbitrary-degree theorem. The checker imports
only unittest and SymPy.
Finite identities support the written argument but do not establish
universal frame existence, arbitrary nice recognition, or cancellation.
No solver/research imports, full regression, shared metadata or
frozen files are part of this task.

The initial two-method run passed in 0.144 seconds, exit zero, with
full output in tool chunk `ccbaf0`. After removing an unnecessary
symbol-assumption option from the second method, that two-method file
passed both methods in 0.140 seconds, exit zero, with full output
in tool chunk `ebccb1`. These are repeated runs of two methods,
not four methods. After adding the distinct finite higher-degree
method, the final three-method file passed in 0.323 seconds, exit
zero, with full output in tool chunk `709d66`. No test run failed.
The final checker SHA-256 is
`16252d686e623751a0ad600bfe6f6e526c47928c6781e74cbbec850f057dda9f`.

The author read the complete saved proof and checker through EOF,
corrected a literal prose transcription typo during that read, and
checked whitespace. Independent proof reviews and any Root integration
capture are separate evidence. No human expert review, historical
novelty verification or formal proof certification is claimed.
