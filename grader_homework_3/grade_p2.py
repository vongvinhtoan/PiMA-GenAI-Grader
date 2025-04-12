import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

# Load the array from the file
array = np.load('function.npy')

def hidden_function(x, y):
    if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
        return array[int(x), int(y)]
    else:
        return 0

def plot_samples(samples: list[tuple[float, float]]):
    """
    Hàm vẽ biểu đồ nhiệt của các điểm đã lấy mẫu.
    Args:
        samples (list[tuple[float, float]]): Danh sách các điểm (x, y) đã lấy mẫu.
    """
    x_samples, y_samples = zip(*samples)
    x_samples = np.array(x_samples)
    y_samples = np.array(y_samples)

    plt.figure(figsize=(8, 6))

    # Create the heatmap
    hist = plt.hist2d(y_samples, -x_samples, bins=180, cmap='viridis', alpha=0.8)
    plt.title("Heatmap of Sampled Points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True)

    # Add colorbar
    plt.colorbar(hist[3])

    plt.show()