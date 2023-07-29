from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
app=QApplication(sys.argv)




window = QMainWindow()
window.setWindowTitle("إنتاجية")
window.resize(500,500)

button=QPushButton()
button.setText("clicked me")
button.setFixedSize(120,50)

window.setCentralWidget(button)

def button_clicked():
    print("the button have clicked")
button.clicked.connect(button_clicked())

window.show()
app.exec()