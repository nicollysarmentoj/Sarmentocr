from setuptools import setup, find_packages

setup(
    name="sarmentocr",
    version="0.1.0",
    description="OCR especializado para exames oftalmológicos de córnea (independente do EasyOCR)",
    author="Vitor Generoso",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pytesseract",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
