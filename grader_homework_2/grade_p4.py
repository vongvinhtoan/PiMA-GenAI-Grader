import random
import numpy as np
from tqdm import tqdm

def in_square_pdf(r):
    def f(p):
        x, y = p
        return 1 / (2 * r)**2 if abs(x) <= r and abs(y) <= r else 0
    return f

def is_in_circle(r):
    def f(p):
        x, y = p
        return 1 if x**2 + y**2 <= r**2 else 0
    return f

def grade(
    ImportanceSampling,
    better_sampling_IS,
    better_pdf_IS,
    is_logging = False
):
    random.seed(b'grade_p4')

    num_trials = 10_000
    N = 100

    p = np.pi / 4
    var_q = p * (1 - p) / N * 16

    def better_approx_pi_IS(r, N):
        def approx_func():
            return 4 * ImportanceSampling(
                q_star_sampler = better_sampling_IS(r = r),
                q = in_square_pdf(r = r),
                q_star = better_pdf_IS(r = r),
                f = is_in_circle(r = r),
                N = N
            )
        return approx_func
    
    list_r = [random.uniform(0, 100) for _ in range(num_trials)]
    list_approx_func = [better_approx_pi_IS(r, N) for r in list_r]
    list_approx = [func() for func in tqdm(list_approx_func, desc="Grading problem 4", unit="trial")]

    var_q_star = np.var(list_approx)

    if is_logging:
        print(f"\n\tVariance of q_star: {var_q_star:.4f}")
        print(f"\tVariance of q: {var_q:.4f}")
        print(f"\tNumber of trials: {num_trials}")
        print(f"\tN: {N}")
