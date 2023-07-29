from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider, QWidget

def respond_to_slider(data):
    print("slider moved to:", data)

app = QApplication()

# Create a custom widget
widget = QWidget()
widget.setFixedSize(500, 500)  # Set the fixed size to 500x500 pixels

slider = QSlider(Qt.Horizontal, widget)  # Add the slider to the custom widget
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)

slider.valueChanged.connect(respond_to_slider)

widget.show()
app.exec()
