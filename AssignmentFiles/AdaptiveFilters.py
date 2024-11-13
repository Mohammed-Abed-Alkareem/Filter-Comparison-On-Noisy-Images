
import numpy as np

def adaptiveMedianFilter(img, max_kernel_size=7):
  
    def adaptiveMedianFilterRec(img, x, y, kernel_size, max_kernel_size):
       
        half_size = kernel_size // 2
        x_min = max(x - half_size, 0)
        x_max = min(x + half_size + 1, img.shape[0])
        y_min = max(y - half_size, 0)
        y_max = min(y + half_size + 1, img.shape[1])

        # Convert the window to a higher precision (int32) to avoid overflow
        window = img[x_min:x_max, y_min:y_max].astype(np.int32)

        # Find the minimum, maximum, and median values in the window
        z_min = np.min(window)
        z_max = np.max(window)
        z_med = int(np.median(window))

        # Step A: Check the difference between the median and min/max values
        A1 = z_med - z_min
        A2 = z_med - z_max

        # If the median is in between the min and max values, move to Step B
        if A1 > 0 and A2 < 0:
            B1 = img[x, y].astype(np.int32) - z_min
            B2 = img[x, y].astype(np.int32) - z_max

            # If the current pixel is between the min and max, keep it unchanged
            if B1 > 0 and B2 < 0:
                return img[x, y]
            else:
                # Otherwise, replace it with the median value
                return z_med
        # If the median is not suitable, increase the kernel size and try again (if within limit)
        elif kernel_size < max_kernel_size:
            # Recursive call with increased kernel size
            return adaptiveMedianFilterRec(
                img=img,
                x=x,
                y=y,
                kernel_size=kernel_size + 2,
                max_kernel_size=max_kernel_size
            )
        else:
            # If the max kernel size is reached, use the median value
            return z_med

    # Create an empty image to store the filtered result
    img_filtered = np.zeros_like(img)

    # Loop over every pixel in the image
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Apply the adaptive median filter recursively for each pixel
            img_filtered[i, j] = adaptiveMedianFilterRec(
                img=img,
                x=i,
                y=j,
                kernel_size=3,   # Initial kernel size starts from 3x3
                max_kernel_size=max_kernel_size
            )

    return img_filtered




def adaptiveMeanFilter(img, max_kernel_size=7):
   

    def getMeanValue(window) -> int:
       
        # Calculate the mean of the window, rounding to the nearest integer
        return int(np.mean(window))

    def adaptiveMeanFilterRec(img, x, y, kernel_size, max_kernel_size):
       
        half_size = kernel_size // 2
        x_min = max(x - half_size, 0)
        x_max = min(x + half_size + 1, img.shape[0])
        y_min = max(y - half_size, 0)
        y_max = min(y + half_size + 1, img.shape[1])

        # Extract the window and convert to higher precision to avoid overflow
        window = img[x_min:x_max, y_min:y_max].astype(np.int32)

        # Calculate the mean and the range (min to max) of the values in the window
        z_min = np.min(window)
        z_max = np.max(window)
        z_mean = getMeanValue(window)

        # Step A: Check if the mean is between the min and max values in the window
        A1 = z_mean - z_min
        A2 = z_mean - z_max

        # If the mean is between the min and max, proceed to Step B
        if A1 > 0 and A2 < 0:
            B1 = img[x, y].astype(np.int32) - z_min
            B2 = img[x, y].astype(np.int32) - z_max

            # If the current pixel is between the min and max, keep it unchanged
            if B1 > 0 and B2 < 0:
                return img[x, y]
            else:
                # Otherwise, replace it with the mean value
                return z_mean
        # If the mean is not suitable, increase the kernel size and try again (if within limit)
        elif kernel_size < max_kernel_size:
            # Recursive call with increased kernel size
            return adaptiveMeanFilterRec(
                img=img,
                x=x,
                y=y,
                kernel_size=kernel_size + 2,
                max_kernel_size=max_kernel_size
            )
        else:
            # If the max kernel size is reached, use the mean value
            return z_mean

    # Create an empty image to store the filtered result
    img_filtered = np.zeros_like(img)

    # Loop over every pixel in the image
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Apply the adaptive mean filter recursively for each pixel
            img_filtered[i, j] = adaptiveMeanFilterRec(
                img=img,
                x=i,
                y=j,
                kernel_size=3,  # Initial kernel size starts from 3x3
                max_kernel_size=max_kernel_size
            )

    return img_filtered
