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

---

## ⚙️ Methodology

1. **Preprocessing**:
   - Extract the green channel from the RGB fundus image.
   - Apply CLAHE to enhance contrast.

2. **Filtering & Enhancement**:
   - Use Gaussian and matched filters for vessel enhancement.
   - Try different scales and orientations to detect vessels with varying thickness.

3. **Segmentation**:
   - Perform edge detection using Canny edge detector.
   - Use thresholding and morphological operations to refine vessel maps.

4. **Evaluation**:
   - Compare outputs using SSIM and PSNR against ground truth.
   - Histogram-based intensity distribution analysis.

---

## ✨ Features
- Pure image processing-based pipeline (no ML/DL).
- Robust handling of vessel thickness and orientation variations.
- Evaluation metrics included.
- Readable, modular Python code.

---

## 📊 Results

Below are some key visual outputs and comparisons:

### Original Fundus Image
![Original Fundus](images/original_fundus.png)

### Green Channel + CLAHE Enhanced
![Green Channel CLAHE](images/clahe_green.png)

### Matched Filtered Output
![Matched Filter Output](images/matched_filter.png)

### Final Vessel Segmentation
![Vessel Segmentation](images/final_vessels.png)

> **Quantitative Results**:
> - Average SSIM: 0.85
> - Average PSNR: 23.5 dB

---

## 📦 Requirements

- Python 3.7+
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- scikit-image

Install with:

```bash
pip install -r requirements.txt
