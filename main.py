from pathlib import Path

from image_editor import (
    aplicar_brillo,
    aplicar_contraste,
    aplicar_morfologia,
    aplicar_saturacion,
    cargar_imagen,
    guardar_imagen,
    mostrar_imagen,
)


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_IMAGEN = BASE_DIR / "images" / "701.png"
RUTA_SALIDA = BASE_DIR / "imagen_editada.jpg"


def pedir_float(mensaje):
    """Solicita un número decimal válido."""
    while True:
        try:
            valor = float(input(mensaje))

            if valor < 0:
                print("❌ Introduce un valor igual o mayor que 0.")
                continue

            return valor

        except ValueError:
            print("❌ Introduce un número válido.")


def pedir_entero_positivo(mensaje):
    """Solicita un número entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                print("❌ El número debe ser mayor que 0.")
                continue

            return valor

        except ValueError:
            print("❌ Introduce un número entero válido.")


def pedir_kernel():
    """Solicita un tamaño de kernel impar."""
    while True:
        kernel_size = pedir_entero_positivo(
            "Tamaño del kernel (3, 5, 7...): "
        )

        if kernel_size < 3:
            print("❌ El kernel debe ser como mínimo 3.")
            continue

        if kernel_size % 2 == 0:
            print("❌ Utiliza un número impar: 3, 5, 7...")
            continue

        return kernel_size


def menu_morfologia(imagen):
    """Muestra el menú de operaciones morfológicas."""

    filtros = {
        "1": ("erosion", "Erosión"),
        "2": ("dilatacion", "Dilatación"),
        "3": ("apertura", "Apertura"),
        "4": ("cierre", "Cierre"),
        "5": ("gradiente", "Gradiente"),
    }

    while True:
        print("\n" + "=" * 40)
        print("       FILTROS MORFOLÓGICOS")
        print("=" * 40)
        print("1. Erosión")
        print("2. Dilatación")
        print("3. Apertura")
        print("4. Cierre")
        print("5. Gradiente")
        print("6. Mostrar imagen")
        print("7. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion in filtros:
            kernel_size = pedir_kernel()
            iteraciones = pedir_entero_positivo(
                "Número de iteraciones: "
            )

            tipo, nombre = filtros[opcion]

            imagen = aplicar_morfologia(
                imagen,
                tipo,
                kernel_size,
                iteraciones
            )

            print(f"✅ {nombre} aplicada correctamente.")

        elif opcion == "6":
            mostrar_imagen(imagen)

        elif opcion == "7":
            return imagen

        else:
            print("❌ Opción no válida.")


def main():
    imagen = cargar_imagen(RUTA_IMAGEN)

    if imagen is None:
        print(
            "\nAñade una imagen llamada '701.jpg' "
            "dentro de la carpeta 'images'."
        )
        return

    print("✅ Imagen cargada correctamente.")

    while True:
        print("\n" + "=" * 40)
        print("          EDITOR DE IMÁGENES")
        print("=" * 40)
        print("1. Cambiar brillo")
        print("2. Cambiar contraste")
        print("3. Cambiar saturación")
        print("4. Mostrar imagen")
        print("5. Guardar imagen")
        print("6. Filtros morfológicos")
        print("7. Salir")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            nivel = pedir_float(
                "Nivel de brillo (1 = original): "
            )

            imagen = aplicar_brillo(imagen, nivel)
            print("✅ Brillo aplicado.")

        elif opcion == "2":
            nivel = pedir_float(
                "Nivel de contraste (1 = original): "
            )

            imagen = aplicar_contraste(imagen, nivel)
            print("✅ Contraste aplicado.")

        elif opcion == "3":
            nivel = pedir_float(
                "Nivel de saturación (1 = original): "
            )

            imagen = aplicar_saturacion(imagen, nivel)
            print("✅ Saturación aplicada.")

        elif opcion == "4":
            mostrar_imagen(imagen)

        elif opcion == "5":
            guardar_imagen(imagen, RUTA_SALIDA)

        elif opcion == "6":
            imagen = menu_morfologia(imagen)

        elif opcion == "7":
            print("\n👋 Programa terminado.")
            break

        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    main()