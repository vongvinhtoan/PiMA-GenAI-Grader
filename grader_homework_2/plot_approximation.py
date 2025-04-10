import matplotlib.pyplot as plt
import random
from typing import *
import numpy as np
from tqdm import tqdm
from .optimize_for_final_grading import GradingOptimizer

def plot_approximation(
    student_id: Any,
    approx_func: Callable[[], float],
    tqdm_desc: str,
    var_name: str,
    true_value: Any,
    method_name: str,
    num_trials: int
):
    if GradingOptimizer.is_optimized_for_final_grading:
        print("Hàm này đã bị tối ưu hóa cho việc chấm điểm cuối cùng. Không thể chạy hàm này.")
        return
    
    random.seed(student_id)

    approximations = [
        approx_func()
        for _ in tqdm(range(num_trials), desc=tqdm_desc)
    ]

    # Compute sample mean and variance
    sample_mean = np.mean(approximations)
    sample_variance = np.var(approximations, ddof=1)

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(approximations, bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.axvline(x=sample_mean, color='green', linestyle='dashed', linewidth=2, label=f"Trung bình mẫu: {sample_mean:.5f}")
    plt.axvline(x=true_value, color='red', linestyle='dashed', linewidth=2, label=f"Giá trị thực của {var_name}: {true_value:.5f}")
    plt.xlabel(f"Giá trị {var_name} xấp xỉ")
    plt.ylabel("Tần số")
    plt.title(f"Biểu đồ phần bố xấp xỉ {var_name} bằng {method_name}\nTrung bình mẫu: {sample_mean:.5f}, Phương sai mẫu: {sample_variance:.5f}")
    plt.legend()
    plt.show()