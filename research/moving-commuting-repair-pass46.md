# Polynomial commutation survives nonzero parameter motion

The independent power-law branch has a global polynomial commuting
correction even when the canonical top parameter moves. Its divergence
vanishes. Local nilpotence does not follow, and a separate control
shows that these resulting properties are insufficient on their own.

## 1. Retained full-frame identities

Keep the independent nonconstant high-top, nonzero preceding-bad
hypotheses of
[the full companion proof](two-quadratic-top-line-pass42.md).
There is no zero-motion assumption. Write
\[
\alpha=(m-1)/2,\quad h=T_cg,\quad
U=[E,T_c],\quad W=[E,T_\lambda],\quad V=[E,W],
\]
\[
gU=-\alpha V,\quad
Eg=Ug=Vg=0,\quad [E,U]=[E,V]=0,\quad
Wg=-gh/(2\alpha).
\tag{1}
\]
In particular \(Eh=0\). The last equality is the full highest
trace/next-column identity, before specializing to zero motion.

Use the actual polynomial preceding coordinate \(v\) from
[the two-layer normal form](independent-preceding-layer-pass44.md):
\[
\tau=gv-r(u),\quad Ev=g^{m-1},\quad
Eu=Uu=Vu=0,\quad g=G(u).
\tag{2}
\]
The next column gives
\[
V\tau=-2g^{m-1}Wg=g^m h/\alpha.
\]
Equations (1)--(2), with no inversion in the resulting equality, yield
\[
Uv=-g^{m-2}h.
\tag{3}
\]

## 2. Exact brackets and divergence of the natural normalizer

Put
\[
Y=gT_c+2\alpha W.
\tag{4}
\]
This is polynomial, and (1) gives
\[
Yg=0,\qquad [E,Y]=\alpha V=-gU.
\tag{5}
\]
The second coefficient of commutativity of the actual conjugated
\(T_c,T_\lambda\) is
\[
[T_c,V]+2[U,W]=0.
\tag{6}
\]
Substitute \(U=-\alpha V/g\) in the fraction field, use the
polynomial identity \(Wg=-gh/(2\alpha)\), and clear \(g\).
This gives
\[
[Y,V]=-hV,\qquad [Y,U]=-hU.
\tag{7}
\]
Every final bracket is a polynomial identity on \(B\).

Polynomial LNDs and their commutators have zero divergence in an
actual polynomial coordinate system. Thus
\[
\operatorname{div}Y=T_cg=h.
\tag{8}
\]
For \(h\ne0\), \(Y\) is not an LND. Conversely, for \(h=0\),
the existing Laurent conjugation proves it is an LND.
So the natural normalizer is locally nilpotent exactly in the
zero-motion subcase of these hypotheses.

## 3. A correction that is polynomial before localization

Define
\[
\mathcal R=g^{m-2}Y+vU.
\tag{9}
\]
Because \(m\ge3\), this is a global polynomial derivation.
Equations (1), (3), (5), (7) imply
\[
[E,\mathcal R]=0,\qquad [U,\mathcal R]=0,\qquad
\mathcal Rg=0,\qquad \operatorname{div}\mathcal R=0.
\tag{10}
\]
Indeed the first bracket is
\(-g^{m-1}U+(Ev)U=0\).
The second is
\(g^{m-2}hU+(Uv)U=0\).
The divergence is \(g^{m-2}h+Uv=0\).
It also commutes with \(V=-gU/\alpha\).
Thus it preserves the actual ring \(\ker E\cap\ker U\).

When \(h=0\), the earlier locally nilpotent correction is related by
\[
\mathcal R_{45}=g\mathcal R-(Yv)E.
\tag{11}
\]
This comparison identifies the old construction; it does not transfer
its local-nilpotence proof to (9) when \(h\ne0\).

## 4. A control against promotion of (10) to local nilpotence

In \(B_0=\mathbb C[s,t,u,z]\), take \(m\ge3\) and set
\[
E_0=\partial_s,\quad U_0=\partial_t,\quad
T_0=\partial_z+s\partial_t,\quad g_0=uz,\quad h_0=u,
\]
\[
H=u\partial_u-z\partial_z,\quad
Y_0=(-g_0s+h_0t)\partial_t+H,\quad
v_0=g_0^{m-1}s-g_0^{m-2}h_0t.
\tag{12}
\]
The partial \(T_0\) is actual in the polynomial frame
\((s,t-sz,u,z)\), and \([E_0,T_0]=U_0\).
Directly,
\[
[E_0,Y_0]=-g_0U_0,\quad
[Y_0,U_0]=-h_0U_0,\quad
Y_0g_0=0,\quad \operatorname{div}Y_0=h_0,
\]
\[
E_0v_0=g_0^{m-1},\qquad
U_0v_0=-g_0^{m-2}h_0.
\tag{13}
\]
The resulting correction is
\[
\mathcal R_0=g_0^{m-2}H,\qquad
\mathcal R_0^n(u)=g_0^{n(m-2)}u\ne0\quad(n\ge1).
\tag{14}
\]
It satisfies every conclusion in (10) and is not locally nilpotent.

This control does not supply the required second actual partial
\(T_\lambda\), the full high-flow coordinate data, or the two-quadratic
adjoint profile. It refutes only an inference from the derived
commutation/divergence/preslice package. It is not a counterexample
to local nilpotence of (9) under all original hypotheses.

## 5. Exact remaining issue

The polynomiality and commutation gap for this correction is closed.
Its local nilpotence under the full moving-frame hypotheses is still
unproved. Another route may instead use the
[omitted good-direction theorem](good-direction-recognition-pass46.md)
without constructing an auxiliary LND.

No primitivity, independence from the original leading distribution,
global compatible slice, actual unresolved-frame realization, novelty,
human or proof-assistant verification, or cancellation conclusion is
asserted for the moving correction.
