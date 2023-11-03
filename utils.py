import numpy as np
import matplotlib.pyplot as plt

def visualize_dataset(dataset, title="Untitled", n_samples=9):
    plt.figure(figsize=(6, 6)).suptitle(title, fontsize=18)

    # decide subplot dimension
    d = np.sqrt(n_samples)
    d = np.ceil(d).astype("uint8")

    for i, samples in enumerate(dataset[:n_samples]):
        img = samples
        plt.subplot(d, d, i + 1)
    
        vmin = np.min(img)
        vmax = np.max(img)
    
        plt.imshow(img, cmap="gray", vmin=vmin, vmax=vmax)
        plt.axis("off")
    plt.show()