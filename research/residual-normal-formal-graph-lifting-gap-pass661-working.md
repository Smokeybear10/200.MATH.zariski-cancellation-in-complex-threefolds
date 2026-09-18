# The residual, formal, rational, and polynomial normal-section gaps

September 18, 2026. Private working proof. Novelty: UNKNOWN.

Consistency of the higher-derivative-ideal test659 does not guarantee
even a formal graph along that ideal. An explicit actual polynomial
frame below passes the test but excludes every constant linear
direction at the first conormal obstruction. A closely related frame
has a formal graph that is rational but not polynomial. A third
actual frame has a specified formal graph that is algebraic but not
rational. These statements concern normal-section selection, not
cancellation or automatic commutation of projected fields.

The relevant formal topology is stated explicitly. Failure over the
completion along an entire divisor does not imply failure in every
closed-point formal neighborhood or after a residue-field extension.

## 1. The exact normal equation and its first obstruction

Let k be a field of characteristic zero and suppose
\[
B=k[X_0,\ldots,X_n]=A[u],\qquad E=\partial_u,\qquad
A=\ker E,\qquad E(u)=1.
\tag{1}
\]
This is an actual polynomial cylinder. Define, as in
[659](slice-shift-higher-derivative-ideal-obstruction-pass659-working.md),
\[
J=(E^jX_i:j\ge2)B=IB,\qquad I=J\cap A.
\tag{2}
\]
Fix constants lambda_i, put ell=sum lambda_i X_i, and express
\[
G_\lambda(T)=(E\ell)(a,T)-1\in A[T].
\tag{3}
\]
The notation a denotes coefficients in A, not assumed polynomial
coordinates of A. A section u=s is a normal section precisely when
G_lambda(s)=0. In the slice-shift notation of659 it is the zero
section of u+h, with h=-s.

Suppose lambda passes the necessary ideal test, so G_lambda belongs
to I[T]. Then also its formal T derivative belongs to I[T]; in
particular the raw derivative cannot be a unit modulo a proper I.
It is not legitimate to apply a unit-derivative implicit-function
argument directly to G_lambda along I.

Let Ahat be the I-adic completion. The ring A is finite type, since
it is the image of the finite Taylor retraction from B, and hence
is Noetherian. If a formal section shat in Ahat satisfies G_lambda(shat)=0,
its residue sbar in A/I must satisfy
\[
\Theta_\lambda(\overline s)=0,\qquad
\Theta_\lambda(T)=[G_\lambda(T)]\in(I/I^2)[T].
\tag{4}
\]
This is a polynomial with coefficients in the A/I-module I/I^2.
Its evaluation is well-defined. Replacing a lift s by s+epsilon,
epsilon in I, changes G_lambda(s) by an element of I^2: its linear
change is G_lambda'(s)epsilon, and every higher change has at least
as much I-adic order. Thus (4) is exactly the first additional
condition for some section modulo I^2. It is not contained in the
assertion G_lambda=0 modulo I, which holds identically in T.

More generally, for a square-zero quotient R' to R with kernel L,
let Q belong to R'[T] and let s be a root of its reduction in R.
Choose a lift s_tilde to R'. A
corrected lift s_tilde+epsilon, epsilon in L, is a root exactly when
\[
Q(\widetilde s)+Q'(\widetilde s)\epsilon=0\quad\text{in }L.
\tag{5}
\]
This follows by expanding Q and using L^2=0. Hence the obstruction
is the class of Q(s_tilde) modulo Q'(s_tilde)L. Applied directly
to G_lambda and the successive I-adic quotients, the derivative
term vanishes on I^r/I^{r+1}. Earlier choices of coefficients may
still affect later obstructions; no automatic impossibility or
automatic lift follows from that observation alone.

## 2. The normalized principal-ideal lifting criterion

Suppose now I=(f), where f is nonzero and a nonunit in A. Write
\[
G_\lambda(T)=fQ(T),\qquad Q\in A[T].
\tag{6}
\]
Multiplication by f remains injective in the f-adic completion.
One elementary proof is to take compatible residues modulo f^N:
if f shat=0, then a representative s_N satisfies f s_N in f^N A,
so s_N lies in f^{N-1}A because A is a domain. For every fixed r,
choosing N>r gives zero residue modulo f^r. Thus shat=0.
Consequently G_lambda(shat)=0 is equivalent to Q(shat)=0.

The first obstruction (4) is now exactly
\[
\overline Q(\overline s)=0\quad\text{in }A/(f).
\tag{7}
\]
If such a residue root exists and Q'(sbar) is a unit in A/(f),
then it has a unique lift shat in the f-adic completion satisfying
Q(shat)=0. Here is the complete recursive argument. Given s_r
with Q(s_r)=f^r c_r, choose t_r modulo f so that
\[
c_r+Q'(s_r)t_r=0\pmod f,\qquad
s_{r+1}=s_r+f^rt_r.
\tag{8}
\]
The unit derivative makes that correction unique modulo f.
Taylor expansion shows Q(s_{r+1})=0 modulo f^{r+1}, since 2r>=r+1
for r>=1. Starting from any lift of sbar gives compatible residues
at all orders and therefore shat. The same calculation proves
uniqueness at every order. This is an elementary Hensel recursion,
not a claim that the resulting series terminates or is rational.

The derivative in this criterion is that of the NORMALIZED Q,
not of the raw equation fQ. The same square-zero argument gives
local formal lifting at a maximal ideal whenever an equation has
a residue root with unit derivative there. These are conditional
lifting statements; neither supplies the necessary residue root.

## 3. An actual family that fails at the first conormal level

For an integer m>=2 start with B=k[a,b,c,u] and E=partial_u. Set
\[
x=a+bu,\qquad y=b,\qquad z=c+bu^m,\qquad t=u+x^2.
\tag{9}
\]
These are whole polynomial coordinates, with inverse
\[
u=t-x^2,\qquad b=y,\qquad a=x-yu,\qquad c=z-yu^m.
\tag{10}
\]
Both compositions follow by substitution; equivalently these are
successive elementary shears. In the actual (x,y,z,t) frame,
\[
E=y\partial_x+m y(t-x^2)^{m-1}\partial_z
 +(1+2xy)\partial_t,\qquad A=k[a,b,c].
\tag{11}
\]
For 1<=j<=m,
\[
E^jz=\frac{m!}{(m-j)!}\,b u^{m-j},\qquad
E^2t=2b^2,\qquad E^3t=0.
\tag{12}
\]
Every higher coordinate derivative is divisible by b, while E^m z=m!b.
Since m>=2, E^m z is a generator of J, giving
\[
J=(y)B,\qquad I=(b)A.
\tag{13}
\]
This ideal is proper, nonzero, and reduced. The test659 passes:
Et-1=2xy belongs to J. More precisely every normalized candidate
in its residual constant-normal system has lambda_t=1, with the
other constant coefficients unrestricted modulo I.

Now suppose that some constant direction admits a formal section
u=shat in Ahat=k[a,c][[b]]. The whole normal equation is
\[
\lambda_xb+m\lambda_zb\widehat s^{m-1}
 +\lambda_t(1+2ab+2b^2\widehat s)=1.
\tag{14}
\]
Reduction modulo b forces lambda_t=1. Cancel b and reduce once
more modulo b. With s_0 in k[a,c] the residue of shat, one obtains
\[
\lambda_x+m\lambda_zs_0^{m-1}+2a=0.
\tag{15}
\]
If m>=3 this is impossible for EVERY choice of constants. If lambda_z=0,
the coefficient of a already contradicts it. Otherwise s_0 would
have a positive power of exponent m-1 equal to a nonconstant affine
linear polynomial in a. Its a-degree is either zero or divisible
by m-1, and cannot be one. The coefficient ring k[c] is a domain,
so no leading-coefficient cancellation affects this degree argument.

The obstruction persists over the generic divisor field k(a,c).
The discrete valuation at the irreducible polynomial a+lambda_x/2
assigns value one to the right side of the proposed power equation;
the value of an (m-1)st power is divisible by m-1. Hence there is
no residue root in k(a,c), and no section in k(a,c)[[b]] either.

Thus consistency of659 modulo the FULL proper ideal J does not
guarantee any formal graph along that ideal, even after choosing
the constant direction freely. Failure occurs already in (4).
The statement needs no algebraic closure of k, no degree cutoff,
and no assumption that projected fields preserve I.

This is not a pointwise-formal impossibility claim. At a k-rational
point with b=0 and a=a_0, choose lambda_t=lambda_z=1 and
lambda_x=-m-2a_0. The normalized equation has the residue root
s=1 and derivative m(m-1), a nonzero scalar. The local version
of the recursion therefore gives a formal root at that point.
The constants may depend on the point; a root over a point does
not supply a root over the entire divisor. Residue-field extensions
can also remove the power obstruction and are not excluded here.

## 4. The m=2 contrast: a rational formal graph, no polynomial graph

For the SAME whole family (9) with m=2, the normalized equation is
\[
\lambda_x+2a+2(b+\lambda_z)s=0,\qquad \lambda_t=1.
\tag{16}
\]
There is no polynomial solution s in k[a,b,c] for any constants:
substitution b=-lambda_z would require lambda_x+2a=0. Thus every
slice shift and constant linear frame still fails the unit-normal
condition globally, even though (13) is a reduced ideal and659 passes.

For lambda_x=0, lambda_z=lambda_t=1, however,
\[
s=-\frac{a}{1+b}=-a\sum_{r\ge0}(-b)^r
\in k[a,c][[b]].
\tag{17}
\]
It is the unique formal solution of (16) with residue -a because
the normalized derivative is 2 modulo b. It is rational and regular
on the neighborhood b+1!=0 of the divisor b=0, but not polynomial
on the whole base. This is a Zariski-local graph that cannot be
promoted to a whole polynomial graph by the stated data.

For lambda_z=0 the first obstruction is instead lambda_x+2a, so
even this formal lifting depends on the chosen candidate direction.
The control demonstrates why a negative result for one candidate
must not be called failure for every candidate, as occurs genuinely
only in the m>=3 part of the preceding proof.

## 5. A specified formal graph that is not even rational

Change only the last coordinate in the m=2 construction to
\[
x=a+bu,\qquad y=b,\qquad z=c+bu^2,\qquad t=u+x^3.
\tag{18}
\]
The full inverse is u=t-x^3, a=x-yu, b=y, c=z-yu^2.
Here E(t)=1+3b(a+bu)^2 and E(z)=2bu. Again J=(y) and I=(b),
because E^2z=2b, E^2t=6b^2(a+bu), E^3t=6b^3, and the later
derivatives vanish.

Take ell=t+z and use the slice-shift variable h=-s. The normal
equation, after cancelling b, is
\[
3(a-bh)^2-2h=0.
\tag{19}
\]
Its residue root is h=3a^2/2, and its h-derivative is -2 modulo b.
Thus it has exactly one b-adic formal solution with that residue.
It is explicitly
\[
h=\frac{1+3ab-\sqrt{1+6ab}}{3b^2},\qquad
\sqrt{1+6ab}\equiv1\pmod b.
\tag{20}
\]
The square root is its binomial series over k[a,c][[b]]. Its first
terms are 1+3ab-(9/2)a^2b^2, so the numerator in (20) is divisible
by b^2 in the completion and the displayed residue is correct.
Substitution using the square-root equation verifies (19) exactly.

The polynomial 1+6ab is irreducible in the UFD k[a,b,c]: it is
primitive and linear in a over k[b,c]. Its valuation in the ambient
rational function field is one, so it is not a square there.
If h in (20) were rational in k(a,b,c), then
1+3ab-3b^2h would be that square root, a contradiction. Therefore
this specified formal graph is algebraic of degree two but is not
even rational, let alone polynomial. No claim about every other
constant direction is needed for this distinction.

This example and Section4 prove different failures of algebraization.
Section3 proves a prior failure of formal existence. None justifies
replacing whole graph sections by unspecified local or formal data.

## 6. Deduplication, provenance, and remaining scope

The stable higher-derivative ideal and its necessary constant-normal
test are from659. The actual full projected-frame recognition still
requires the complementary commutation condition of656--657.
This note imposes no artificial action of those projected fields on
A/I. Its obstruction is evaluation of a polynomial in a module,
not a descended derivation or a first jet asserted to be an LND.

The archive already distinguishes formal, rational, and polynomial
maps in [lifting-route](lifting-route.md) and
[647](kr-retraction-zariski-etale-gap-pass647-working.md).
The [conormal action note77](binary-conormal-obstruction-pass77.md)
uses a different parameter ideal and stationary derivations.
The bounded comparison found no identical retained normal-section
lifting calculation. The elementary implicit-function recursion and
the general warning about formal algebraization are not claimed new.

General supplied the m=2 proper-ideal false positive and independently
checked the m>=3 residue-power obstruction. The author supplied the
uniform m>=3 strengthening and first conormal test; root independently
reconstructed them and supplied the cubic formal root in (20).
All uniform conclusions follow from the written identities and degree
or valuation arguments, not a finite search. Fresh unsaved exact
algebra is used only to check the printed whole maps and formulas.
No saved checker was run, imported, compiled, or modified; no
canonical file, git state, or external record was changed.

Root, General, and Geometry read the complete held source. Both
separate reviewers reported CLEAN after reconstructing the conormal
test, completion and lifting argument, whole coordinate controls,
and all formal/rational/polynomial distinctions. Root and the author
also ran independent fresh unsaved exact checks of the printed
identities. Reviewed hashes and full-read evidence are in the ledger.

These are controls on a specified normal-section repair route, with
polynomial bases and explicit nonlinear coordinate inverses. They
give no cancellation counterexample or universal recognition theorem.
General cancellation remains UNSOLVED; novelty is UNKNOWN. AI review
is not human expert review or proof-assistant certification.
