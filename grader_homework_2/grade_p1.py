import numpy as np
import random

def MonteCarlo(q_sampler, f, N):
    samples = [q_sampler() for _ in range(N)]
    return 1/N * sum(f(x) for x in samples)

def grade(
    sample_needle,
    is_lie_across
):
    
    def approx(l: float, t: float, N: int) -> float:
        return MonteCarlo(
            q_sampler = sample_needle(l, t),
            f = is_lie_across(l, t),
            N = N
        )

    print(f"Grading problem 1")

    num_trials = 10
    num_success = 0
    alpha = 0.05
    N = 50

    params = [
        sorted((random.uniform(0, 100), random.uniform(0, 100)))
        for _ in range(num_trials)
    ]

    for i in range(num_trials):
        l, t = params[i]

        p = 2 * l / np.pi / t
        p_hat = approx(l, t, N)

        print(f"Trial {i+1}: l = {l:.2f}, t = {t:.2f}, p = {p:.4f}, p_hat = {p_hat:.4f}")

