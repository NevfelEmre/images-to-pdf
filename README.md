# Robust Image to PDF Converter 📸➡️📄

A resilient Python tool designed to convert a folder of images into a single PDF document. Unlike standard converters, this tool is built to handle edge cases like **corrupted image headers**, **truncated files**, and **human-friendly sorting**.

## 🚀 Features

* **Natural Sorting:** Sorts `IMG_1, IMG_2, ... IMG_10` correctly (instead of `1, 10, 2`).
* **Fault Tolerance:** Uses a "clean canvas" re-rendering technique (Pillow) to fix and include images even if they have broken headers or are truncated.
* **One-Click Run:** Includes a smart `start.bat` that automatically sets up the Python virtual environment and installs dependencies.
* **Format Normalization:** Automatically converts various color modes (CMYK, Grayscale) to RGB for PDF compatibility.

## 🛠 Installation & Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/NevfelEmre/robust-image-to-pdf.git](https://github.com/KULLANICI_ADIN/robust-image-to-pdf.git)
    ```
2.  Place your images inside the `images` folder.
3.  Double-click **`start.bat`**.
OR
Use .exe instead of .py and .bat
That's it! The script will:
* Create a virtual environment (if not exists).
* Install required packages (`Pillow`, `natsort`).
* Generate `sonuc_dosyasi.pdf` in the root directory.

## 📦 Requirements

* Python 3.x
* Windows (for `.bat` usage) - *Script itself is cross-platform.*
