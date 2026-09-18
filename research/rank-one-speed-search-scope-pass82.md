# Bounded actual-frame search for acceleration outside the speed ideal

The [read-only search script](rank_one_speed_search_pass82.py) found no
counterexample in the two bounded batches recorded in the
[complete output capture](rank-one-speed-search-evidence-pass82.json).
This is not an exhaustive search, a proof of q in I, or a unittest suite.
It adds zero test methods. The exact mathematical theorems on divisorial
membership and ambient nilpotence are separate written arguments.

## Actual frames and inverse preservation

The base ring is C[s,a,b,c] with E=partial_s. The search starts from
six specified actual polynomial coordinate frames, four in the first
batch and two additional principal controls in the broader batch.

The identity frame is immediate. The two-speed frame is
(s,a,b+a squared s,c+b squared s). Its inverse first recovers s,a,
then b from its third entry, then c from its fourth entry.

The two retained conic frames, with u=a or a squared, are
(b+2u c+u squared s,c+u s,s,a-bs+c squared). If their entries are
(X,Y,Z,W), their inverse is s=Z, a=XZ-Y squared+W,
c=Y-uZ and b=X-2uY+u squared Z, where u is evaluated at that
recovered a. These are the explicit v=1 cases of the retained
[conic inverse](conic-nice-pair-classification-pass75.md), not new actions.

The broader batch also uses n=2,3 and the inverse of
t -> t+(a/2)t squared modulo a to the nth power. Its finite inverse
is beta(v)=sum from j=0 to n-1 of
(-1)^j Catalan(j) a^j v^(j+1)/2^j. The seed is
(a,x,y,c), with x=beta(b)+a^n s and
y=(x+(a/2)x squared-b)/a^n. Polynomiality follows from the two
inverse congruences modulo a^n. Conversely b=x+(a/2)x squared-a^n y
and s=(x-beta(b))/a^n are polynomials by the same congruences.
Thus these seeds also have two-sided polynomial inverses, and their
original action is a^n partial_x+(1+ax)partial_y. They are known
principal-ideal controls, not solutions of the nonprincipal question.

Every subsequent move replaces one current coordinate F_i by
F_i+H(other current coordinates), fixing the others. H is a monomial,
its negative, or the difference of two monomials with a rational
coefficient chosen to cancel the leading s term. Because the target
is excluded from H, the inverse move is the polynomial subtraction.
The stored history therefore retains an actual inverse sequence even
when a full expanded inverse is not printed.

All retained frames have s-degree at most two, with explicit spatial
degree and term caps. Only a frame with exactly one quadratic entry
is tested for q membership. The other three speeds and its acceleration
then lie in C[a,b,c]. Since the actual ring is C[a,b,c][s], checking
membership there is exactly the ambient ideal-membership question.

## Counts, duplicates and the corrected nonprincipal label

The first inline run attempted 3,000 moves. Its deterministic replay
accepted 1,670 distinct bounded frames, of which 697 had exactly one
quadratic entry. It performed 141 proper-ideal q-membership tests.
An exact saturated-ideal classification shows 140 of these were truly
nonprincipal, over 24 distinct nonprincipal Groebner-basis tuples.
The remaining proper test was principal. All remainders were zero.

The initial inline variable named nonprincipal counted only a cheap
gcd screen. That wording was corrected before this final evidence
record. The historical count 391 remains explicitly labeled as a
screen, not as 391 confirmed nonprincipal ideals. The script records
the exact classification in a separate counter.

Only one broader search batch was run. It stopped after 1,239 attempts,
accepted 687 distinct bounded frames and found 244 rank-one profiles.
Sixteen proper-ideal membership tests included eleven nonprincipal
tests over seven distinct nonprincipal ideals. Again every tested
remainder was zero. The nominal wall limit was 35 seconds, checked
between attempts; the final symbolic attempt completed at 41.971650
seconds. No second broader batch was started.

Frames are deduplicated by their expanded coordinate-tuple strings
within a batch. Different frames can repeat an ideal or membership
test. The initial and broader ideal sets can overlap; their distinct
counts are not added to claim a global unique count. The capture gives
the full counter definitions and every seed and bound.

## Reproduction and evidence limits

The script prints JSON and writes no files. The captured script hash is
73be64fde317324b20b1a0f8d4d5b8d9bad27860c6aa1129aeb0346b690ce948,
with SymPy 1.13.3. The original inline result is distinct from the
saved-script replay. The latter completed in 6.882773 seconds with
tool chunk 682dc9; the broader output is tool chunk b9e209.

For exact deterministic replay of the attempted candidate sets, use
the capture's commands with --replay-attempts 3000 or 1239. This turns
off the between-attempt wall limit; the elapsed time is not expected
to reproduce across machines. Neither command is a new unittest.

No actual q outside I, no complete tame classification, and no
universal acceleration membership statement was established. This
search did not change frozen files or shared metadata. The local
capture was saved on Root's explicit request and is separate from
any canonical targeted-checker capture or full regression.
