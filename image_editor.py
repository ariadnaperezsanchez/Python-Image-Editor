import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance


def cargar_imagen(ruta):
    """Carga una imagen y la convierte al formato RGB."""
    try:
        return Image.open(ruta).convert("RGB")
    except FileNotFoundError:
        print(f"❌ No se encontró la imagen: {ruta}")
        return None
    except Exception as error:
        print(f"❌ Error al abrir la imagen: {error}")
        return None


def guardar_imagen(imagen, ruta):
    """Guarda la imagen en la ruta indicada."""
    try:
        imagen.save(ruta)
        print(f"✅ Imagen guardada en: {ruta}")
        return True
    except Exception as error:
        print(f"❌ Error al guardar la imagen: {error}")
        return False


def mostrar_imagen(imagen):
    """Muestra la imagen utilizando Matplotlib."""
    plt.figure(figsize=(8, 6))
    plt.imshow(imagen)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def aplicar_brillo(imagen, nivel):
    """Modifica el brillo de la imagen."""
    return ImageEnhance.Brightness(imagen).enhance(nivel)


def aplicar_contraste(imagen, nivel):
    """Modifica el contraste de la imagen."""
    return ImageEnhance.Contrast(imagen).enhance(nivel)


def aplicar_saturacion(imagen, nivel):
    """Modifica la saturación de la imagen."""
    return ImageEnhance.Color(imagen).enhance(nivel)


def aplicar_morfologia(imagen, tipo, kernel_size=5, iteraciones=1):
    """Aplica una operación morfológica a la imagen."""

    img_np = np.array(imagen)

    kernel = np.ones(
        (kernel_size, kernel_size),
        dtype=np.uint8
    )

    if tipo == "erosion":
        resultado = cv2.erode(
            img_np,
            kernel,
            iterations=iteraciones
        )

    elif tipo == "dilatacion":
        resultado = cv2.dilate(
            img_np,
            kernel,
            iterations=iteraciones
        )

    elif tipo == "apertura":
        resultado = cv2.morphologyEx(
            img_np,
            cv2.MORPH_OPEN,
            kernel,
            iterations=iteraciones
        )

    elif tipo == "cierre":
        resultado = cv2.morphologyEx(
            img_np,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=iteraciones
        )

    elif tipo == "gradiente":
        resultado = cv2.morphologyEx(
            img_np,
            cv2.MORPH_GRADIENT,
            kernel,
            iterations=iteraciones
        )

    else:
        raise ValueError(
            f"Operación morfológica no válida: {tipo}"
        )

    return Image.fromarray(resultado)