import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path
from .dual_number import *

dir_path = Path(__file__).resolve().parent

def plot_samples_with_contour(f, samples):
    x_samples, y_samples = zip(*samples)

    # --- Grid and Contour ---
    x = y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(np.array([X.flatten(), Y.flatten()])).reshape(X.shape)
    fig = plt.figure(figsize=(14, 6))
    gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 0.05], wspace=0.2)

    # Left: Heatmap only
    ax1 = fig.add_subplot(gs[0])
    _, _, _, img1 = ax1.hist2d(x_samples, y_samples, bins=200, cmap='viridis', alpha=0.8)
    ax1.set_title("Heatmap of Sampled Points")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_aspect("equal", adjustable="box")
    ax1.grid(True)

    # Right: Heatmap + Contours
    ax2 = fig.add_subplot(gs[1])
    _, _, _, img2 = ax2.hist2d(x_samples, y_samples, bins=200, cmap='viridis', alpha=0.8)
    contours = ax2.contour(X, Y, Z, levels=10, linewidths=1, cmap='inferno')

    ax2.clabel(contours, inline=True, fontsize=8)
    ax2.set_title("Heatmap + Contour Overlay")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_aspect("equal", adjustable="box")
    ax2.grid(True)

    # Clean colorbar on the side
    cax = fig.add_subplot(gs[2])
    fig.colorbar(img2, cax=cax, label='Point Density')

    plt.show()

def grad_f_fast(x: np.ndarray) -> np.ndarray:
    """
    Tính đạo hàm của hàm đồng biến với hàm mật độ xác suất mục tiêu $p(x)$
    """

    def f(x, y):
        exp1 = exp(-((x**2 + y**2)/4 + (1/4)*x*y))
        exp2 = exp(-((x**2 + y**2)/4 - (1/4)*x*y))
        return sin(3 * exp1)**2 + sin(3 * exp2)**2
    
    f_x = f(Dual(x[0], 1), Dual(x[1], 0)).dual
    f_y = f(Dual(x[0], 0), Dual(x[1], 1)).dual
    return np.array([f_x, f_y])