import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

# Define the function
def f(x, y):
    exp1 = np.exp(-((x**2 + y**2)/4 + (1/4)*x*y))
    exp2 = np.exp(-((x**2 + y**2)/4 - (1/4)*x*y))
    return np.sin(3 * exp1)**2 + np.sin(3 * exp2)**2

def plot_function_conture():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Plot the contour
    plt.figure(figsize=(8, 6))
    contours = plt.contour(X, Y, Z, levels=10, cmap='inferno')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.title("Contour Plot of Custom Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()