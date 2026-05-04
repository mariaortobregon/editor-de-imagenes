print("hi")
import sys
from PyQt5.QtWidgets import (
                        QApplication, QMainWindow, QLabel, QPushButton,
                        QFileDialog, QVBoxLayout, QWidget, QMessageBox
                            )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageOps
import image_filters
# voltear
#grises
#combiar color
#agregar sticker

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editor de imagenes")
        self.setGeometry(100, 100, 100, 700)



        self.image_Label = QLabel("Carga una imagen")
        self.image_Label.setScaledContents(True)
        self.image_Label.setFixedSize(700, 500)

        self.open_button = QPushButton("Abrir imagen")
        self.open_button.clicked.connect(self.open_image)

        self.voltear_button = QPushButton("voltear")
        self.voltear_button.clicked.connect(self.voltear_imagen)

        self.grises_button = QPushButton("grises")
        self.grises_button.clicked.connect(self.apply_grayscale)

        self.sticker_button = QPushButton("sticker")
        self.sticker_button.clicked.connect(self.sticker_imagen)

        self.color_button = QPushButton("cambiar color")
        self.color_button.clicked.connect(self.color_imagen)

        self.guardar_button = QPushButton("guardar")
        self.guardar_button.clicked.connect(self.guardar_image)

        self.sepia_button = QPushButton("sepia")
        self.sepia_button.clicked.connect(self.sepia_imagen)

        layout = QVBoxLayout()
        layout.addWidget(self.image_Label)
        layout.addWidget(self.open_button)
        layout.addWidget(self.color_button)
        layout.addWidget(self.voltear_button)
        layout.addWidget(self.sticker_button)
        layout.addWidget(self.grises_button)
        layout.addWidget(self.guardar_button)
        layout.addWidget(self.sepia_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.current_image = None 
        self.original_image = None
    
    def guardar_image(self):
        
        if not self.current_image:
            return
        file_name, _ =QFileDialog.getSaveFileName(self, "guardar imagen", "nombre", "Imagenes (*.png *.jpg *.jpeg *.bmp)")
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

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "","Imágenes (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            image = Image.open(file_name).convert("RGB")
            self.original_image = image.copy()
            self.current_image = image
            self.image_before_brightness = self.current_image.copy()
            self.display_image(self.current_image)

    def apply_grayscale(self):
        if self.current_image:
            self.current_image = image_filters.apply_grayscale(self.current_image)
            self.display_image(self.current_image)

    def voltear_imagen(self): #NO FUNCIONA
        if self.current_image:
            self.current_image = image_filters.voltear_imagen(self.current_image)
            self.display_image(self.current_image)

    def color_imagen(self):
        pass

    def sticker_imagen(self):
        pass

    
    def sepia_imagen(aelf):
        a = 1
        if a == 1:
            print("a = 1")

app = QApplication([])
editor = ImageEditor()
editor.show()
sys.exit(app.exec_())