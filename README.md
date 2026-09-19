# Python Image Editor

A simple command-line image editor built with Python. The application allows users to modify image properties and apply morphological image-processing operations using Pillow and OpenCV.

## Features

- Adjust image brightness
- Adjust image contrast
- Adjust image saturation
- Display the edited image
- Save the edited image
- Apply morphological filters:
  - Erosion
  - Dilation
  - Opening
  - Closing
  - Morphological gradient
- Configure kernel size and number of iterations
- Input validation for menu options and filter parameters

## Technologies

- Python
- Pillow
- OpenCV
- NumPy
- Matplotlib

## Project Structure

```text
Python-Image-Editor/
├── images/
│   └── 701.png
├── image_editor.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the command-line interface, user input validation, and application flow.

### `image_editor.py`

Contains the image-processing functions used for brightness, contrast, saturation, image display, saving, and morphological operations.

## Installation

Clone the repository:

```bash
git clone https://github.com/ariadnaperezsanchez/Python-Image-Editor.git
cd Python-Image-Editor
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python3 main.py
```

The application displays an interactive menu:

```text
========================================
          EDITOR DE IMÁGENES
========================================
1. Cambiar brillo
2. Cambiar contraste
3. Cambiar saturación
4. Mostrar imagen
5. Guardar imagen
6. Filtros morfológicos
7. Salir
```

The example image is located in:

```text
images/701.png
```

The edited image is saved as:

```text
imagen_editada.jpg
```

## Morphological Operations

The editor includes several morphological image-processing operations provided by OpenCV:

- **Erosion** reduces bright regions and can remove small details.
- **Dilation** expands bright regions.
- **Opening** combines erosion followed by dilation.
- **Closing** combines dilation followed by erosion.
- **Morphological Gradient** highlights differences between dilation and erosion and can emphasize object boundaries.

The user can select the kernel size and number of iterations for each operation.

## Requirements

The project dependencies are listed in `requirements.txt`:

```text
Pillow
matplotlib
opencv-python
numpy
```

## Purpose

This project was created as a practical exercise to explore image manipulation and basic computer vision techniques in Python while applying modular programming and separation of responsibilities.