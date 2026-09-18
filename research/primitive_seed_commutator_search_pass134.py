"""Bounded actual-coordinate search starting on the primitive side.

This deliberately reuses the frozen133 exploration engine, not an independent
checker. It changes only its three seed frames. All four original target slots
remain available, and intermediate profiles may leave the three-good class.
The engine verifies both seed inverse orders and both word inverse orders.

The first two seeds are known primitive translation normal forms. The third
is an actual quadratic bad shear of the first. No seed is claimed to be new.
An actual failure would challenge a correction conjecture, not cancellation.
The engine's finite time and term bounds are retained and reported.
"""

import hashlib
import importlib.util
from pathlib import Path

import sympy as sp


ENGINE_PATH = Path(__file__).with_name("primitive-gate-search-pass133.py")
ENGINE_SHA256 = "192bb828fbe777bcbce7e4a0f9c4cdab0775d236e338db9728cdf03ad5d08424"


def load_engine():
    if hashlib.sha256(ENGINE_PATH.read_bytes()).hexdigest() != ENGINE_SHA256:
        raise RuntimeError("Frozen133 exploration engine checksum changed")
    spec = importlib.util.spec_from_file_location("primitive_search_engine133", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the frozen exploration engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def install_primitive_seeds(engine):
    a, b, v, u = engine.BASE
    X, Y, Z, W = engine.ORIGINAL
    half = sp.Rational(1, 2)

    def primitive_seed(name, speed, inverse_speed, bad_shear=False):
        # I=a, V=b, R=v, E=partial_u, with I=XW-Y^3/2-Z.
        frame = [u, b+speed*u, -a-half*b**3+v*u,
                 v+3*half*b**2*speed+3*half*b*speed**2*u+half*speed**3*u**2]
        recovered_W = W
        if bad_shear:
            frame[3] += frame[1]**2+2*frame[0]*frame[2]+3*frame[1]+5
            recovered_W = W-Y**2-2*X*Z-3*Y-5
        inverse_a = X*recovered_W-half*Y**3-Z
        inverse_p = inverse_speed(inverse_a)
        inverse_b = Y-inverse_p*X
        inverse_v = (recovered_W-3*half*inverse_b**2*inverse_p
                     -3*half*inverse_b*inverse_p**2*X-half*inverse_p**3*X**2)
        return name, frame, [inverse_a, inverse_b, inverse_v, X], recovered_W, inverse_speed

    def seeds():
        entries = [
            primitive_seed("primitive_linear_speed", a, lambda value: value),
            primitive_seed("primitive_quadratic_speed", a**2+1, lambda value: value**2+1),
            primitive_seed("primitive_quadratic_bad_shear", a, lambda value: value, True),
        ]
        result = []
        for name, frame, inverse, recovered_W, inverse_speed in entries:
            forward_sub = dict(zip(engine.ORIGINAL, frame))
            # Verify the stated inverse in its successive polynomial stages.
            # Expanding p(I(frame)) before reducing I(frame)=a wastes the
            # time budget on expressions that are already exact identities.
            actual_a = sp.expand(inverse[0].subs(forward_sub, simultaneous=True))
            actual_p = inverse_speed(actual_a)
            actual_b = sp.expand(frame[1]-actual_p*frame[0])
            actual_W = sp.expand(recovered_W.subs(forward_sub, simultaneous=True))
            actual_v = sp.expand(actual_W-3*half*actual_b**2*actual_p
                                 -3*half*actual_b*actual_p**2*frame[0]
                                 -half*actual_p**3*frame[0]**2)
            if any(sp.expand(value-expected) != 0
                   for value, expected in zip((actual_a, actual_b, actual_v, frame[0]), engine.BASE)):
                raise AssertionError((name, "seed inverse after forward"))
            # Reverse composition is a universal identity in the substituted
            # speed p. Verify it before specializing p to its polynomial in I.
            p = sp.Dummy("substituted_speed")
            back_a = X*recovered_W-half*Y**3-Z
            back_b = Y-p*X
            back_v = (recovered_W-3*half*back_b**2*p
                      -3*half*back_b*p**2*X-half*p**3*X**2)
            back_frame = [X, back_b+p*X, -back_a-half*back_b**3+back_v*X,
                          back_v+3*half*back_b**2*p+3*half*back_b*p**2*X+half*p**3*X**2]
            if recovered_W != W:
                back_frame[3] += back_frame[1]**2+2*back_frame[0]*back_frame[2]+3*back_frame[1]+5
            if any(sp.expand(value-expected) != 0
                   for value, expected in zip(back_frame, engine.ORIGINAL)):
                raise AssertionError((name, "seed forward after inverse"))
            polys = [engine.polynomial(value) for value in frame]
            status, data = engine.probe(polys)
            if status != "both_gates_pass":
                raise AssertionError((name, "known primitive seed failed", status, data))
            result.append({"name": name, "frame": polys, "inverse": list(map(str, inverse))})
        return result

    engine.seeds = seeds


if __name__ == "__main__":
    engine = load_engine()
    install_primitive_seeds(engine)
    engine.main()
