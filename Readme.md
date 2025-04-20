# Vessel Extraction in Retinal Fundus Images 🧠👁️

This project focuses on the extraction of retinal blood vessels from fundus images using traditional image processing techniques. The goal is to enhance the visibility and segmentation of blood vessels without relying on deep learning methods. These techniques are crucial for aiding the diagnosis of diabetic retinopathy and other retinal diseases.

---

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Methodology](#methodology)
- [Features](#features)
- [Results](#results)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Folder Structure](#folder-structure)
- [Sample Outputs](#sample-outputs)
- [Contributors](#contributors)

---

## 🧾 Project Overview

This work focuses on the **enhancement and segmentation** of blood vessels from colored retinal fundus images. The main tasks include:
- Enhancing the green channel using **CLAHE (Contrast Limited Adaptive Histogram Equalization)**.
- Applying **matched filtering** for vessel detection.
- Performing **multiscale gradient computation and edge detection** using the **Canny operator**.
- Comparing various image enhancement and filtering techniques using **PSNR**, **SSIM**, and histograms.

## Dataset
The project uses the Retina Blood Vessel Segmentation Dataset from Kaggle, which contains:
- High-resolution retinal fundus images
- Binary mask annotations (vessel pixels marked as 1, background as 0)
- Diverse range of retinal pathologies
- Varying vessel widths and branching patterns

Dataset Link: [Retina Blood Vessel Dataset](https://www.kaggle.com/datasets/abdallahwagih/retina-blood-vessel)

## Methodology

### 1. Image Preprocessing
- Green channel extraction from RGB images (provides highest contrast between vessels and background)

### 2. Image Enhancement Techniques
Several enhancement techniques were evaluated based on PSNR, CII, and Entropy metrics:

| Filter | PSNR | CII | Entropy |
|--------|------|-----|---------|
| Histogram Equalization | 12.845 | 1.3303 | 3.789 |
| Adaptive Histogram Equalization | 7.889 | 1.489 | 5.343 |
| CLAHE | 25.033 | 1.024 | 4.541 |
| Gamma Correction | 13.821 | 0.582 | 3.303 |
| Unsharp Masking | 37.741 | 1.013 | 3.899 |
| Logarithmic Transformation | 8.402 | 1.141 | 3.272 |
| Exponential Transformation | 20.047 | 0.782 | 3.673 |
| Laplacian Sharpening | 29.818 | 1.014 | 4.405 |

### 3. Vessel Detection
- Matched Filtering using Gabor Kernel
- Kernel rotation through 360 degrees to capture varying vessel orientations
- Multiple kernel sizes to detect different vessel thicknesses

### 4. Noise Reduction
Evaluated noise reduction filters:

| Filter | PSNR | CII | Entropy |
|--------|------|-----|---------|
| Non Local Means Filter | 36.964 | 1.000 | 4.955 |
| Adaptive Median Filter | 36.445 | 0.922 | 5.333 |
| Gaussian Low pass filter | 32.627 | 0.588 | 5.076 |
| Butterworth low pass filter | 23.872 | -0.529 | 4.951 |
| Mean Low pass filter | 33.362 | 0.698 | 5.273 |

### 5. Morphological Operations
- Morphological closing (dilation followed by erosion)
- Adaptive thresholding for binarization
- Connected component analysis for noise removal

## Performance Metrics
The project uses several evaluation metrics:
1. IoU (Intersection over Union)
2. Dice Coefficient
3. Precision
4. Recall
5. Accuracy
6. PSNR (Peak Signal-to-Noise Ratio)
7. CII (Colorfulness Index Indicator)
8. Entropy

## Results
The final approach combines:
1. Green channel extraction
2. Laplacian filtering for edge detection
3. CLAHE for contrast enhancement
4. Matched filtering for vessel detection
5. Unsharp masking for further contrast improvement
6. Morphological operations for noise removal
7. Adaptive thresholding for binarization

## Future Improvements
1. Implementation of edge linking process
2. Removal of corneal structure artifacts
3. Image preprocessing to handle circumferential artifacts
4. Improved mask positioning for better evaluation metrics

## References
1. Dai, Peishan, et al. "Retinal Fundus Image Enhancement Using the Normalized Convolution and Noise Removing." International Journal of Biomedical Imaging, 2016.
2. T. Jintasuttisak and S. Intajag. "Color retinal image enhancement by Rayleigh contrast-limited adaptive histogram equalization." 2014.
3. M.M. Fraz, et al. "Blood vessel segmentation methodologies in retinal images – A survey." Computer Methods and Programs in Biomedicine, 2012.
4. A. W. Setiawan, et al. "Color retinal image enhancement using CLAHE." 2013.
5. Peng Feng, et al. "Enhancing retinal image by the Contourlet transform." Pattern Recognition Letters, 2007.
6. M. U. Akram, et al. "Retinal image blood vessel segmentation." 2009.
7. M. Saleh Miri and A. Mahloojifar. "A comparison study to evaluate retinal image enhancement techniques." 2009.
8. G. D. Joshi and J. Sivaswamy. "Colour Retinal Image Enhancement Based on Domain Knowledge." 2008.
9. N. R. Binti Sabri and H. B. Yazid. "Image Enhancement Methods For Fundus Retina Images." 2018.
10. A. Imran, et al. "Comparative Analysis of Vessel Segmentation Techniques in Retinal Images." IEEE Access, 2019.

## Authors
- K. Harish (3122225001036)
- Janeshvar Sivakumar (3122225001047)

## Institution
Sri Sivasubramaniya Nadar College of Engineering
(An Autonomous Institution, Affiliated to Anna University)
Kalavakkam – 603110

---

## 📦 Requirements

### Python Dependencies
```bash
# Core Dependencies
numpy>=1.21.0
opencv-python>=4.5.0
scikit-image>=0.18.0
matplotlib>=3.4.0
pandas>=1.3.0

# Machine Learning Dependencies
tensorflow>=2.8.0
scikit-learn>=0.24.0

# Jupyter Notebook Support
jupyter>=1.0.0
ipykernel>=6.0.0
```

### Installation
```bash
# Create a new conda environment (recommended)
conda create -n retina python=3.9
conda activate retina

# Install dependencies
pip install -r requirements.txt
```

### Hardware Requirements
- Minimum 8GB RAM
- GPU with at least 4GB VRAM (recommended for faster processing)
- 10GB free disk space for dataset and processing

### Dataset Requirements
- Retina Blood Vessel Segmentation Dataset from Kaggle
- Minimum image resolution: 224x224 pixels
- Supported formats: PNG, JPG, JPEG

