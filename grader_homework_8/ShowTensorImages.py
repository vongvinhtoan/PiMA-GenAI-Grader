from torchvision import transforms
import numpy as np
import matplotlib.pyplot as plt

def show_tensor_images(images, n_images=1, cols=5, save_dir=None):
    reverse_transforms = transforms.Compose([
        transforms.Lambda(lambda t: (t + 1) / 2),
        transforms.Lambda(lambda t: t * 255.),
        transforms.Lambda(lambda t: t.permute(1, 2, 0)),  # CHW to HWC
        transforms.Lambda(lambda t: t.numpy().astype(np.uint8)),
        transforms.ToPILImage(),
    ])

    images = images.cpu().detach().view(-1, 1, 32, 32) 
    n_images = min(n_images, images.shape[0])

    rows = (n_images + cols - 1) // cols
    plt.figure(figsize=(cols, rows))
    
    for idx in range(n_images):
        plt.subplot(rows, cols, idx + 1)
        img = images[idx]
        plt.imshow(reverse_transforms(img))
        plt.axis('off')

    plt.tight_layout()
    if save_dir:
        plt.savefig(save_dir)
    plt.show()