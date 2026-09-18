# Independent audit of the two-quadratic-defect lemma

The complete `two-quadratic-defects-pass39.md` was independently read
and reconstructed. No mathematical gap was found in the conditional
matrix theorem or in the genuine sliced example.

The decisive checks are as follows.

- The conjugated-partial matrix is the actual inverse-flow Jacobian.
  Schur elimination gives precisely the displayed companion matrix,
  including the minus sign and factor one half in its upper-right block.
- Both no-pure-auxiliary-kernel assertions use the stipulated rank-two
  defect matrix. For a matrix annihilated on both sides, row restriction
  and image projection preserve rank successively. The argument applies
  to arbitrary such matrices, not only outer products of rank one.
- Nilpotent descent from the sixth power is valid. In the degree-two
  case, rank at least four together with cube zero forces Jordan type
  \((3,3)\); the rank-preserving lemma then gives the exact upper-left
  rank two. Degree one would instead force rank at most three and is
  excluded.
- Top coefficient comparison gives the factors \((m-1)/2\) and
  \(m/2\) in the two different displayed identities. They are not
  interchangeable. The selector applied to the highest vector vanishes,
  making the preceding selected coefficient invariant.
- The coordinate maps in the example are both-sided polynomial
  inverses. The four highest commutators have the stated nonzero
  values on the actual invariant \(r\). Direct computation of the
  four partials in \(\mathbb C[u,v,r][s]\) also gives the exact
  filtration shifts \((1,1,2,2)\), not just adjoint upper bounds.
- The highest field satisfies \(U(u)=u^2\), while its coefficients
  generate the unit ideal by the explicit polynomial identity. Hence
  primitive normalization does not make it an LND. The original action
  nevertheless has an explicit polynomial quotient.

The only presentation suggestion was to replace the opening phrase
“is a curve” by “has Jacobian rank at most one,” since a constant
highest coefficient is allowed. This was reported to the author without
editing the proof.

The independent exact checker imports only `unittest` and `sympy`:

```text
/opt/anaconda3/bin/python research/two_quadratic_defects_checks_pass39.py
Ran 6 tests in 1.039s
OK
```

This was its first run, with no assertion or mathematical correction.
The six methods are frozen after that passing result. The finite tests
support the explicit example and matrix identities; the written proof,
not finite sampling, supplies the universal conditional block argument.
No general height-ten recognition, universal frame existence, novelty,
expert-review, or proof-assistant-verification conclusion is licensed.
