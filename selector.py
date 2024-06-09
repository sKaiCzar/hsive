import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox

class ImageSelectorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Selector")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 200)
        self.label.setText("No Image Selected")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.select_button = QPushButton("Select Image", self)
        self.select_button.setGeometry(150, 260, 100, 30)
        self.select_button.clicked.connect(self.select_image)

    def select_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("All Files (*)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            file = open(file_path, 'r')
            if file:
                QMessageBox.information(self, "Image Loaded", "Image loaded successfully.")
                self.open_next_window()
            else:
                QMessageBox.warning(self, "Error", "Failed to load image.")
    def open_next_window(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageSelectorApp()
    window.show()
    sys.exit(app.exec_())

