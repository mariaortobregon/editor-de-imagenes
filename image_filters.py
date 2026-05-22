from PIL import ImageOps, Image
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (
                        QApplication, QMainWindow, QLabel, QPushButton,
                        QFileDialog, QVBoxLayout, QWidget, QMessageBox
                            )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

def apply_grayscale(image):
    return ImageOps.grayscale(image).convert("RGB")

def voltear_imagen(imagen):
    return imagen.rotate(90)

def color_image(self):
    pass

def sticker_image(self):
    pass

def guardar_image(self):
    if not self.current_image:
        return
    file_name, _ =QFileDialog.getSaveFileName(self, "guardar imagen", "", "Imagenes (*.png *.jpg *.jpeg *.bmp)")
    if file_name:
        self.current_image.save(file_name)
        QMessageBox.information(self, "guardado", "Imagen Guardada Exitosamente")
def display_image(self, img):
    img = img.convert("RGB")
    max_width, max_height = self.image_Label.width(), self.image_Label.height()
    img = img.copy()
    img.thumbnail((max_width, max_height), Image.LANCZOS)
    data = img.tobytes("raw", "RGB")
    w, h = img.size
    qimg = QImage(data, w, h, w * 3, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qimg)
    self.image_Label.setPixmap(pixmap)
def apply_sepia(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            transform_red   = int(0.393*r + 0.769*g + 0.189*b)
            transform_green = int(0.349*r + 0.686*g + 0.168*b)
            transform_blue  = int(0.272*r + 0.534*g + 0.131*b)
            pixels[x, y] = (min(255, transform_red),
                            min(255, transform_green),
                            min(255, transform_blue))
    return image

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)
    
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)
    
