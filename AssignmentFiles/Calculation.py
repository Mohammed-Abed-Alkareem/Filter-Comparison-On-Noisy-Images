
import numpy as np


def MSE(original, noisy):
    """
    Calculate the Mean Squared Error (MSE) between two images.

    Parameters:
    original (numpy.ndarray): Original image.
    noisy (numpy.ndarray): Noisy image.

    Returns:
    float: Mean Squared Error (MSE) between the two images.
    """
    # Calculate the squared error between the two images
    error = (original - noisy) ** 2

    # Calculate the mean of the squared error
    return np.mean(error)


#images_with_gaussian_filter_gaussian = {0:{noise1:[k3, k5, k7], noise2:[k3, k5, k7]}, 1:{noise1:[k3, k5, k7], noise2:[k3, k5, k7]}, ...}
def calculate_MSE_for_filters(images, images_with_filter, kernel_sizes):
    MSE_results = {i: {n: [] for n in range(len(images_with_filter[i]))} for i in range(len(images))}
    
    for i in range(len(images)):
        for j in range(len(images_with_filter[i])):
            for k in range(len(kernel_sizes)):
                MSE_results[i][j].append(MSE(images[i], images_with_filter[i][j][k]))
    
    return MSE_results


def PSNR(original, noisy):
    """
    Calculate the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Parameters:
    original (numpy.ndarray): Original image.
    noisy (numpy.ndarray): Noisy image.

    Returns:
    float: Peak Signal-to-Noise Ratio (PSNR) between the two images.
    """
    # Calculate the MSE between the two images
    mse = MSE(original, noisy)

    # Calculate the maximum possible pixel value of the images
    max_pixel = np.max(original)

    # Calculate the PSNR value
    return 10 * np.log10(max_pixel ** 2 / mse)

def calculate_PSNR_for_filters(images, images_with_filter, kernel_sizes):
    PSNR_results = {i: {n: [] for n in range(len(images_with_filter[i]))} for i in range(len(images))}
    
    for i in range(len(images)):
        for j in range(len(images_with_filter[i])):
            for k in range(len(kernel_sizes)):
                PSNR_results[i][j].append(PSNR(images[i], images_with_filter[i][j][k]))
    
    return PSNR_results



def calculate_average_time(time_gauss_images,time_saltPepper_images,images, kernel_sizes, gaus_values, salt_pepper_values):
    average_time = {k: 0 for k in kernel_sizes}
    for i in range(len(images)):
        for k in range(len(kernel_sizes)):
            for j in range(len(gaus_values)):
                average_time[kernel_sizes[k]] += time_gauss_images[i][j][k]
            for j in range(len(salt_pepper_values)):
                average_time[kernel_sizes[k]] += time_saltPepper_images[i][j][k]
    for k in average_time:
        average_time[k] /= (len(images) * (len(gaus_values) + len(salt_pepper_values)))
    return average_time