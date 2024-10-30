# Comparing Simple Smoothing Filters with Advanced Filters on Noisy Images

This repository contains the code and experiments for comparing the performance of simple smoothing filters (Box filter, Gaussian filter, and Median filter) with advanced filters (such as adaptive filters) when applied to noisy images. The comparison is based on noise removal effectiveness, edge preservation, computational efficiency, and the influence of kernel size.

## Table of Contents

- [Objective](#objective)
- [Background](#background)
- [Experiments](#experiments)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Checklist](#checklist)

## Objective

The objective of this project is to analyze and compare various filters' performance on noisy images using metrics such as Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR), while also evaluating the trade-offs between noise removal, edge preservation, and computational efficiency.

## Background

Image denoising is a crucial task in computer vision, where filters are applied to noisy images to enhance their quality. This project investigates:

- Simple Filters: Box filter, Gaussian filter, Median filter
- Advanced Filters: Adaptive mean filter, adaptive median filter, Bilateral filter

Each filter's effectiveness is measured across different kernel sizes and noise levels, considering both quantitative and qualitative factors.

## Experiments

1. **Noisy Image Generation**

   - Selected clean images from a public dataset.
   - Added Gaussian noise and Salt-and-Pepper noise at varying intensity levels.
2. **Filter Application**

   - Implemented Box, Gaussian, Median, and advanced filters using Python and OpenCV.
   - Applied each filter across different kernel sizes.
3. **Performance Evaluation**

   - Measured MSE and PSNR for each filter.
   - Evaluated edge preservation using edge detection methods (e.g., Canny).
   - Analyzed computational time for different kernel sizes.

## Results

- **MSE and PSNR Comparison**: Provided values for each filter across noise levels and kernel sizes.
- **Edge Preservation**: Visual examples and edge map comparisons for each filter.
- **Computational Time**: Chart showing time complexity for varying kernel sizes.
- **Kernel Size Effect**: Analysis of kernel size impact on noise removal and edge preservation.

## Discussion

The discussion covers:

- Noise removal effectiveness and kernel size sensitivity.
- Edge preservation trade-offs with noise reduction.
- Computational efficiency and the implications of filter selection.

## Conclusion

This assignment highlights the trade-offs between using simple and advanced filters for image denoising. Larger kernel sizes offer more smoothing but may blur edges, whereas smaller kernels preserve details but may not reduce noise effectively.

## Checklist

- [X] Set up project repository with initial structure.
- [X] Load clean images and apply noise (Gaussian, Salt-and-Pepper).
- [X] Implement Box, Gaussian, and Median filters.
- [X] Implement advanced filters (Adaptive mean, Adaptive median, Bilateral).
- [X] Measure MSE and PSNR for each filter and kernel size.
- [X] Perform edge preservation analysis with Canny detector.
- [X] Measure computational time for filter applications.
- [ ] Document results and analysis in the report.
- [ ] Finalize discussion and submit the report.
