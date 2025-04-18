import random
import numpy as np
from tqdm import tqdm

def sampling_IS(r):
    def sampler():
        k = random.uniform(0, r)
        x = random.uniform(-k, k)
        y = random.uniform(-k, k)
        return x, y
    return sampler

def is_in_circle(r):
    def f(p):
        x, y = p
        return 1 if x**2 + y**2 <= r**2 else 0
    return f

def grade(
    ImportanceSampling,
    in_square_pdf,
    pdf_IS,
    is_logging = False
):
    random.seed(b'grade_p3')

    def approx_pi_IS(r, N):
        def approx_func():
            return 4 * ImportanceSampling(
                q_star_sampler = sampling_IS(r = r),
                q = in_square_pdf(r = r),
                q_star = pdf_IS(r = r),
                f = is_in_circle(r = r),
                N = N
            )
        return approx_func
    
    num_trials = 10_000
    N = 100
    list_r = [random.uniform(0, 100) for _ in range(num_trials)]
    list_approx_func = [approx_pi_IS(r, N) for r in list_r]
    list_approx = [func() for func in tqdm(list_approx_func, desc="Grading problem 3", unit="trial")]

    mean = np.mean(list_approx)
    step = 0.05
    score = 1.0 / 2 ** int(abs((mean - np.pi) / step))

    if is_logging:
        print(f"\tMean: {mean:.4f}")
        print(f"\tNumber of trials: {num_trials}")
        print(f"\tN: {N}")
        print(f"\tScore: {score:.4f}")

    return round(score / 0.05) * 0.05
