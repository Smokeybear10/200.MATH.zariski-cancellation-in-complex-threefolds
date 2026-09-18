# The zero-D affine-quadratic profile violates the complex field return

Working exclusion: the D=0 alternative of368 cannot occur in its
complete actual chart. The calibrated determinant first integrates
every remaining coefficient into a rational expression with complex
constants. The intercept field would then have to equal a rational
function field across a map of degree six. That contradicts the
original strong complex field return.

Together with371 this excludes the intrinsic degree pair (1,2)
in365's supplied theta-dominant chart. It does not prove entry into
that chart, exclude equal or reversed degrees, or settle cancellation.

## 1. Complete actual hypotheses and removal of B

Retain every actual hypothesis of
[368](principal-paraboloid-affine-quadratic-nonlinear-profile-normal-form-pass368-working.md),
including the actual264/296 entry through365, the complete initial
kernel, selected literal partial, exact finite coefficient field,
both returns and full scalar calibration. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a_0=EX\ne0,
\quad N=[u^4]\partial_Z|_A,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[P],\quad P=\sigma,\quad \tau_0=NP\in L^*,\\
K=L(P)=\mathbb C(y,z,w),\quad k=s,
\quad J_{t,s,P}(X)=-a_0^4/\tau_0\in L^*.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. Let F=ker_L(partial_s),
finite over C(t), with t-derivative constants exactly C. No initial
assumption F=C(t) or L=C(t,s) is made.

Suppose the remaining alternative has D=(t^2B)''=0. By368,
B=b1/t+b2/t^2 for complex b1,b2. Apply the actual map
\[
X_*=X,\quad Y_*=Y+b_1X,\quad Z_*=Z-2b_2X,
\quad W_*=W-2b_1Y-2b_2X^2.
\tag{2}
\]
Its full inverse, potential transports and all original-ring gates
are established directly in369 Section4, and with arbitrary D in371
Section2. We use those literal identities, not369's strict-degree
argument, which does not cover the pair (1,2). The map preserves
the complete initial ideal, literal Z-partial, both returns and
scalar; it changes s to s-2b1t-2b2 and P to P+b1.
The formal parameter P+t(X+j) is unchanged because j changes to
j-b1/t. It removes B and keeps the degree pair (1,2).

Drop stars. The full368 zero-D conclusion can therefore be used as
\[
\begin{aligned}
n&=-s^2/(4t^2)+f(t),\qquad f\in F,\\
\theta&=-P^2+\beta P+\gamma,\qquad
\beta=s/t+b(t),\quad b\in F,\quad \gamma\in L,\\
j&=s/(2t^2),\qquad
y=-\theta/(2t)+jP+k,\\
k&=(G-f)/(2t)+s^2/(4t^3),\qquad G\in F,
\quad G'\ne0,\quad G'=t f''.
\end{aligned}
\tag{3}
\]
Primes denote the exact t-derivative. The last identity is368(26)
in the normalized chart. The complete map remains
\[
\begin{aligned}
z&=2ty+P^2+\theta+n,\qquad
w=\ell-2Py-n_tP-n_s\theta,\\
Y&=y+PX+tX^2,\\
Z&=z+(2tP+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{4}
\]

## 2. Third-level compatibility integrates f and G

Use the two exact third-level coefficient equations from368:
\[
\ell_s=-\zeta_0/t-n_{tt}/2-t^2n_{ts}^2,
\qquad \ell_t=2t n_{ts}\zeta_0+\beta\Omega,
\tag{5}
\]
where zeta0=k+n_t/2 and Omega=n_tt/2-n_s^2+t^2n_ts^2=f''/2.
In (3) these equations are exactly
\[
\begin{aligned}
\ell_s&=-\frac{3s^2}{4t^4}-\frac{G-f}{2t^2}
        -\frac{f'}{2t}-\frac{f''}{2},\\
\ell_t&=\frac{s^3}{t^5}+\frac{s(G-f)}{t^3}
        +\frac{s f'}{t^2}+\frac{s f''}{2t}+\frac{b f''}{2}.
\end{aligned}
\tag{6}
\]
Taking the difference of the mixed partials gives
\[
\partial_t(\ell_s)-\partial_s(\ell_t)
=-\frac{G'+2tf''+t^2f'''}{2t^2}=0.
\tag{7}
\]
By G'=t f'', this says (t^3 f'')'=0. Exact integration in F
gives
\[
\boxed{
f=\frac{c}{2t}+f_1t+f_0,\qquad
G=G_0-\frac ct,\qquad
c\in\mathbb C^*,\quad f_1,f_0,G_0\in\mathbb C.
}
\tag{8}
\]
The constant c is nonzero because G' is nonzero. Integrating the
first equation of (6) in s, then using its second equation, gives
\[
\ell=-\frac{s^3}{4t^4}+\frac{cs}{2t^3}
       +\frac{(f_0-G_0)s}{2t^2}+\ell_0,
\qquad \ell_0\in F,\qquad b=\frac{2t^3\ell_0'}c.
\tag{9}
\]
Every integration subtracts an explicit primitive and uses the
appropriate zero-derivative field. Rationality of ell0 is not yet
assumed.

## 3. Two full scalar coefficients integrate ell0 and gamma

Differentiate (4) with respect to t,s,P at fixed actual X, using
(3),(8),(9). The two relevant coefficients of the complete
determinant J=J_(t,s,P)(X) are
\[
\begin{aligned}
[XP]J&=-\frac{3cs-2ct^2\gamma_s
                    +2t^5\ell_0''+6t^4\ell_0'}{2t^5},\\
[P^2X^0]J&=-\frac{3cs-2ct^2\gamma_s
                    +4t^5\ell_0''+10t^4\ell_0'}{4t^6}.
\end{aligned}
\tag{10}
\]
Both vanish by (1). Subtracting their zero numerators gives
t ell0''+2ell0'=0. Hence t^2 ell0'=h in C, and
\[
\boxed{
\ell_0=-\frac ht+\ell_{00},\quad h,\ell_{00}\in\mathbb C,
\qquad
\gamma=\frac{3s^2}{4t^2}+\frac{hs}{c}+\gamma_0,
\quad \gamma_0\in F.
}
\tag{11}
\]
Here h is an integration constant, not the third-potential level.
The formula for gamma follows by inserting ell0 into the first
equation of (10) and integrating in s. In particular h=0 is retained.

Put
\[
T=2(G_0-f_0)t-4c+t^2\gamma_0'-2t\gamma_0.
\tag{12}
\]
After (11), the entire determinant has the particularly simple form
\[
\boxed{
J=-\frac{cT}{4t^7}(2t^2X+2tP+s)
       +\frac{c(cs+2ht^2)}{4t^7}.
}
\tag{13}
\]
Calibration makes its X coefficient zero, so T=0. Solving this
first-order equation in the exact field F yields
\[
\boxed{
\gamma_0=G_0-f_0-\frac{4c}{3t}+q_2t^2,
\qquad q_2\in\mathbb C.
}
\tag{14}
\]
Indeed division by t^2 after subtracting the displayed particular
solution gives an element with zero t-derivative.

The remaining value in (13) is nonzero in L, since s is
transcendental over F. Thus the scalar alone has not contradicted
this family. The strong complex field equality in (1) is essential
for the next step.

## 4. The intercepts give a rational map of degree six

Set only as field parameters and complex intercept translations
\[
U=P+\frac{s}{2t},\qquad z_0=z-G_0,\qquad
y_0=y+\frac{f_1}{2},\qquad w_0=w-\ell_{00}.
\tag{15}
\]
The element U is not claimed to be an original polynomial coordinate.
Substituting the completely integrated data into (4) gives
\[
\begin{aligned}
z_0&=U^2-\frac ct,\\
y_0&=\frac{U^2}{2t}-\frac{sU}{2t^2}-\frac{hU}{c}
       -\frac{c}{12t^2}-\frac{q_2t}{2}.
\end{aligned}
\tag{16}
\]
Since U is a nonzero degree-one polynomial in P and c is nonzero,
these formulas have the rational inverse
\[
t=\frac{c}{U^2-z_0},\qquad
s=\frac{tU^2-2t^2y_0-2ht^2U/c-c/6-q_2t^3}{U}.
\tag{17}
\]
All divisions in (17) are legitimate in the function field; in
particular U^2-z0=c/t is nonzero. It follows that
\[
\mathbb C(t,s,U)=\mathbb C(y_0,z_0,U).
\tag{18}
\]
The data (8),(9),(11),(14) have only complex constants. Thus all
three intercepts belong to C(t,s,U), and the actual field return gives
\[
K=\mathbb C(y,z,w)=\mathbb C(y_0,z_0,w_0)
 \ \subseteq\ \mathbb C(t,s,U)\ \subseteq\ L(P)=K.
\tag{19}
\]
Both inclusions must be equalities. This conclusion follows from the
actual return, not an assumption that L is rational.

But the literal second potential, after substituting (17), gives
\[
\boxed{
w_0=\frac{(U^2-z_0)^3-12c y_0(U^2+z_0)+6c^2q_2}{12cU}.
}
\tag{20}
\]
For a direct check one may first substitute P=U-s/(2t) into w in
(4), and then use (16),(17). The constants h,f0,G0 cancel from
(20), while f1 and ell00 are removed by (15).

Let B0=C(y0,z0). These two elements are algebraically independent:
K=C(y,z,w) has transcendence degree three and is generated by
those three intercepts. By (18),(19), U is transcendental over B0.
The numerator A(U) of (20) has exact degree six. It is coprime to
its denominator 12cU because
\[
A(0)=-z_0^3-12c y_0z_0+6c^2q_2\ne0\quad\text{in }B_0.
\tag{21}
\]
This nonvanishing follows from the nonzero coefficient -12c of
y0 z0; it includes q2=0 and all values of h and the other constants.

For completeness the rational-function degree fact is elementary.
For coprime A(U),B(U) over a field and an indeterminate W,
A(U)-W B(U) is primitive and linear in W over that field[U].
Gauss's lemma makes it irreducible in the two-variable polynomial
ring, and then over the rational function field in W. Its degree
in U is max(deg A,deg B). Identifying W with the nonconstant
rational function A(U)/B(U) proves the corresponding field extension
has that degree. Here A has degree six and B=12cU has degree one,
so
\[
[B_0(U):B_0(w_0)]=6.
\tag{22}
\]
This contradicts the equality B0(U)=B0(w0) forced by (18),(19).
Therefore the D=0 alternative is impossible.

## 5. Scope and exact evidence

The full368 source was freshly read in3ff2cb,369 in3670f9, and371
in48b0fe. The D=0 normalization uses the literal actual map and
rebuilds its derivative conditions; it does not borrow the strict
degree assumption of369 or divide by the nonzero-D coefficient.
Fresh unsaved9fe1a5 reconstructed the full determinant after (9),
including both coefficients in (10). Fresh bfbd57 reconstructed it
after (11) and produced the complete expression (13).
Fresh742b86 separately substituted the full intercept formulas,
solved (16) for t,s, and obtained the degree-six rational expression
(20) before the harmless complex translations (15).

The argument uses the exact finite coefficient fields throughout
integration, and the original complex field return only in (19).
No saved checker was executed, imported, compiled, or rerun. These
generic exact calculations do not substitute for the field-degree
proof or recursively certify the inherited chart results.

Combining this exclusion with
[371](principal-paraboloid-quadratic-field-affine-quadratic-exclusion-pass371-working.md)
removes both alternatives of368 and hence the full intrinsic pair
(1,2) in the supplied theta-dominant chart. Arbitrary coupling,
equal/reversed degree cases, original chart entry, and the general
cancellation conjecture remain unresolved. No historical novelty,
human-expert review, or proof-assistant certification is claimed.
