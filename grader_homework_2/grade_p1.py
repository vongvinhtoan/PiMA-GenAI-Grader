import numpy as np
import random
from scipy.stats import norm
from tqdm import tqdm

def MonteCarlo(q_sampler, f, N):
    samples = [q_sampler() for _ in range(N)]
    return 1/N * sum(f(x) for x in samples)

def grade(
    sample_needle,
    is_lie_across,
    is_logging = False
):
    random.seed(b'grade_p1')

    def approx(l: float, t: float, N: int) -> float:
        return MonteCarlo(
            q_sampler = sample_needle(l, t),
            f = is_lie_across(l, t),
            N = N
        )

    num_trials = 10_000
    num_success = 0
    alpha = 0.05
    N = 100

    params = [
        (random.uniform(0, 100), random.uniform(0, 100))
        for _ in range(num_trials)
    ]

    for i in tqdm(range(num_trials), desc="Grading problem 1", unit="trial"):
        l, t = params[i]

        if l <= t:
            p = 2 * l / np.pi / t
        else:
            p = 2 / np.pi * np.arccos(t / l) + 2 / np.pi * l / t * (1 - np.sqrt(1-t**2 / l**2))

        p_hat = approx(l, t, N)
        var = p * (1 - p) / N
        z = (p_hat - p) / np.sqrt(var)
        p_value = 2 * (1 - norm.cdf(abs(z)))
        if p_value > alpha:
            num_success += 1

    success_rate = num_success / num_trials
    if is_logging:
        print(f"\n\tSuccess rate: {success_rate:.4f}")
        print(f"\tNumber of success: {num_success}")
        print(f"\tNumber of trials: {num_trials}")
        print(f"\tAlpha: {alpha}")
        print(f"\tN: {N}")
    return min(success_rate / (1 - alpha), 1)
