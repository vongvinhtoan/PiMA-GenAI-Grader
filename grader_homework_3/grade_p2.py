import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap

dir_path = Path(__file__).resolve().parent

def plot_function_conture():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    
    Z = np.load(dir_path / 'Z.npy')

    # Plot the contour
    plt.figure(figsize=(8, 6))
    contours = plt.contourf(X, Y, Z, levels=10, cmap='inferno')

    cbar = plt.colorbar(contours)
    cbar.set_label('Giá trị của hàm $f(\\boldsymbol{x})$')
    plt.title("Biểu đồ nhiệt hàm $f(\\boldsymbol{x})$")
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def plot_function_derivative_vector_field():
    # Grid for vector field
    span = 35
    x = np.linspace(-4, 4, span)
    y = np.linspace(-4, 4, span)
    X, Y = np.meshgrid(x, y)

    # Load the function values from a file
    U = np.load(dir_path / 'U.npy')
    V = np.load(dir_path / 'V.npy')

    # Normalize the vector field
    magnitude = np.sqrt(U**2 + V**2)
    U_norm = np.divide(U, magnitude, out=np.zeros_like(U), where=magnitude != 0)
    V_norm = np.divide(V, magnitude, out=np.zeros_like(V), where=magnitude != 0)

    # Grid for contour (higher resolution)
    x_dense = np.linspace(-4, 4, 400)
    y_dense = np.linspace(-4, 4, 400)
    X_dense, Y_dense = np.meshgrid(x_dense, y_dense)

    Z = np.load(dir_path / 'Z.npy')

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left plot: vector field
    q1 = ax1.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Greys', scale=40)
    cb1 = fig.colorbar(q1, ax=ax1)
    cb1.set_label("Độ lớn của vector")
    ax1.set_title("Trường vector của $\\nabla f(\\boldsymbol{x})$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.axis("equal")
    ax1.grid(True)

    # Right plot: vector field + contour
    contour = ax2.contour(X_dense, Y_dense, Z, levels=10, cmap='inferno', alpha=0.6)
    ax2.clabel(contour, inline=True, fontsize=8)
    q2 = ax2.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Greys', scale=40)
    ax2.set_title("Trường vector của $\\nabla f(\\boldsymbol{x})$ + Đường đồng mức của $f(\\boldsymbol{x})$")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.axis("equal")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def test_function_contour(f_tested):
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    
    Z_tested = f_tested(np.array([X.flatten(), Y.flatten()])).reshape(X.shape)
    Z_jury = np.load(dir_path / 'Z.npy')

    # Create subplots for comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left plot: Tested function
    contours1 = ax1.contourf(X, Y, Z_tested, levels=10, cmap='inferno')
    cbar1 = fig.colorbar(contours1, ax=ax1)
    cbar1.set_label('Giá trị của hàm $f_{tested}(\\boldsymbol{x})$')
    ax1.set_title("Biểu đồ nhiệt hàm $f_{tested}(\\boldsymbol{x})$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.grid(True)
    ax1.axis("equal")

    # Right plot: Jury function
    contours2 = ax2.contourf(X, Y, Z_jury, levels=10, cmap='inferno')
    cbar2 = fig.colorbar(contours2, ax=ax2)
    cbar2.set_label('Giá trị của hàm $f_{jury}(\\boldsymbol{x})$')
    ax2.set_title("Biểu đồ nhiệt hàm $f_{jury}(\\boldsymbol{x})$")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.grid(True)
    ax2.axis("equal")

    plt.tight_layout()
    plt.show()

def test_function_derivative_vector_field(grad_f):
    # Grid for vector field
    span = 35
    x = np.linspace(-4, 4, span)
    y = np.linspace(-4, 4, span)
    X, Y = np.meshgrid(x, y)

    # Load the function values from a file
    out = grad_f(np.array([X.flatten(), Y.flatten()]))
    U = out[0].reshape(X.shape)
    V = out[1].reshape(X.shape)

    # Normalize the vector field
    magnitude = np.sqrt(U**2 + V**2)
    U_norm = np.divide(U, magnitude, out=np.zeros_like(U), where=magnitude != 0)
    V_norm = np.divide(V, magnitude, out=np.zeros_like(V), where=magnitude != 0)

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left plot: vector field
    # Create a custom colormap based on 'Greys' but with red
    greys_red = LinearSegmentedColormap.from_list("GreysRed", ["white", "red"])
    greys_green = LinearSegmentedColormap.from_list("GreysGreen", ["white", "green"])

    q1 = ax1.quiver(X, Y, U_norm, V_norm, magnitude, cmap=greys_red, scale=40)
    cb1 = fig.colorbar(q1, ax=ax1)
    cb1.set_label("Độ lớn của vector")
    ax1.set_title("Trường vector của $\\nabla f(\\boldsymbol{x})$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.axis("equal")
    ax1.grid(True)

    # Right plot: vector field with jury overlay
    q2 = ax2.quiver(X, Y, U_norm, V_norm, magnitude, cmap=greys_red, scale=40)
    # cb2 = fig.colorbar(q2, ax=ax2)
    # cb2.set_label("Độ lớn của vector (tested)")
    ax2.set_title("Trường vector của $\\nabla f(\\boldsymbol{x})$ với overlay kết quả")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.axis("equal")
    ax2.grid(True)

    U_jury = np.load(dir_path / 'U.npy')
    V_jury = np.load(dir_path / 'V.npy')

    # Normalize the jury vector field
    magnitude_jury = np.sqrt(U_jury**2 + V_jury**2)
    U_jury_norm = np.divide(U_jury, magnitude_jury, out=np.zeros_like(U_jury), where=magnitude_jury != 0)
    V_jury_norm = np.divide(V_jury, magnitude_jury, out=np.zeros_like(V_jury), where=magnitude_jury != 0)
    # Create a vector field for the jury
    q3 = ax2.quiver(X, Y, U_jury_norm, V_jury_norm, magnitude_jury, cmap=greys_green, scale=40)
    cb3 = fig.colorbar(q3, ax=ax2)
    cb3.set_label("Độ lớn của vector (jury)")

    plt.tight_layout()
    plt.show()