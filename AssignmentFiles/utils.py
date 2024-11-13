import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_size = 10

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

    
def add_gaussian_noise(image, mean=0, sigma=25):
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = image + gauss
    # Clip the values to be between 0 and 255
    noisy = np.clip(noisy, 0, 255)
    # Convert to unsigned 8-bit integer
    noisy = np.uint8(noisy)
    return noisy


#If amount=0.004 and s_vs_p=0.5, the function will turn approximately 0.4% of the pixels into salt or pepper, with half being white (salt) and half being black (pepper).
def add_salt_pepper_noise(image, amount=0.004):
    row, col = image.shape
    s_vs_p = 0.5  # Salt to pepper ratio
    out = np.copy(image)

    # Salt noise (white pixels)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords[0], coords[1]] = 255

    # Pepper noise (black pixels)
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords[0], coords[1]] = 0

    return out


def print_with_border(message):
    border_length = len(message) + 4
    print('*' * border_length)
    print('* ' + message + ' *')
    print('*' * border_length)
    print()

def plot_with_noise_filtered(images, images_with_noise, images_with_filter, noise_type:str, filter_type:str, noise_values:list, kernel_sizes: list, kernel_sizes_to_show: list):

    for i in range(len(images)):
        print_with_border(f"Showing images with {filter_type} filter for image {i + 1}")

        for j in range(len(noise_values)):
            print(f"\n\tShowing images with {filter_type} filter for {noise_type} noise {noise_values[j]}")


            fig, axs = plt.subplots(1, len(kernel_sizes_to_show)+2, figsize=(image_size, image_size))

            axs[0].imshow(images[i], cmap='gray')
            axs[0].axis('off')
            axs[0].set_title('Original', fontsize=8)

            axs[1].imshow(images_with_noise[i][noise_type][j], cmap='gray')
            axs[1].axis('off')
            axs[1].set_title(f'{noise_type} noise: {noise_values[j]}', fontsize=8)
            for k in range(len(kernel_sizes_to_show)):
                axs[k+2].imshow(images_with_filter[i][j][kernel_sizes.index(kernel_sizes_to_show[k])], cmap='gray')
                axs[k+2].axis('off')
                axs[k+2].set_title(f'Kernel size: {kernel_sizes_to_show[k]}', fontsize=8)
        

            plt.tight_layout()
            plt.show()


def plot_with_edges(images, images_with_edges, filter_type, noise_type, noise_values, kernel_sizes, kernel_sizes_to_show):
    original_edges = [cv2.Canny(img, 100, 200) for img in images]

    for j in range(len(noise_values)):
        print_with_border(f"Showing Edges for {noise_type} noise {noise_values[j]} with {filter_type} filter:")

        fig, axs = plt.subplots(len(images), len(kernel_sizes_to_show) + 1, figsize=(image_size, image_size))

        for i in range(len(images)):
            axs[i, 0].imshow(original_edges[i], cmap='gray')
            axs[i, 0].axis('off')
            axs[i, 0].set_title(f'Original Edges {i + 1}', fontsize=8)

            for k in kernel_sizes_to_show:
                axs[i, kernel_sizes_to_show.index(k) + 1].imshow(images_with_edges[i][j][kernel_sizes.index(k)], cmap='gray')
                axs[i, kernel_sizes_to_show.index(k) + 1].axis('off')
                axs[i, kernel_sizes_to_show.index(k) + 1].set_title(f'Kernel size: {k}', fontsize=8)
                

        plt.suptitle(f'Edges for {noise_type} noise {noise_values[j]} with {filter_type} filter', y=1.005)

        plt.tight_layout()
        plt.show()
