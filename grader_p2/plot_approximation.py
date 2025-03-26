import matplotlib.pyplot as plt
import random
from typing import *
import numpy as np
from tqdm import tqdm

def plot_approximation(
    student_id: Any,
    approxer: Callable[[], float],
    tqdm_desc: str,
    var_name: str,
    real_ans: Any,
    method_name: str
):
    random.seed(student_id)

    num_trials = 10000
    approximations = [
        approxer()
        for _ in tqdm(range(num_trials), desc=tqdm_desc)
    ]

    # Compute sample mean and variance
    sample_mean = np.mean(approximations)
    sample_variance = np.var(approximations, ddof=1)

    # 95% CI
    se = np.sqrt(sample_variance / num_trials)
    lower_bound = sample_mean - 1.96 * se
    upper_bound = sample_mean + 1.96 * se
    print(f"Khoảng tin cậy 95%: ({lower_bound:.4f}, {upper_bound:.4f})")

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(approximations, bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.axvline(x=sample_mean, color='green', linestyle='dashed', linewidth=2, label=f"Trung bình mẫu: {sample_mean:.5f}")
    plt.axvline(x=real_ans, color='red', linestyle='dashed', linewidth=2, label=f"Giá trị thực của $\pi$: {real_ans}")
    plt.xlabel(f"Giá trị {var_name} xấp xỉ")
    plt.ylabel("Tần số")
    plt.title(f"Biểu đồ phần bố xấp xỉ {var_name} bằng {method_name}\nTrung bình mẫu: {sample_mean:.5f}, Phương sai mẫu: {sample_variance:.5f}")
    plt.legend()
    plt.show()