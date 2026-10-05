# Angela Correa NC = 0037
import cv2

# 1. Cargar la imagen del jaguar
# Asegúrate de que jaguar.jpg esté dentro de la carpeta "../imagenes/"
imagen = cv2.imread("jaguar.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen. Revisa que '../imagenes/jaguar.jpg' exista.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Jaguar 0037", imagen)
cv2.imshow("Jaguar 0037 - Filtro Gaussiano", imagen_suavizada)

# 2. Guardar resultado con un nuevo nombre
ruta_salida = "../resultados/jaguar_gaussiano.jpg"
cv2.imwrite(
    ruta_salida,
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print(f"Resultado guardado en: {ruta_salida}")

# Esperar una tecla para cerrar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Angela Correa NC = 0037")