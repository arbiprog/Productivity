from PySide6.QtWidgets import QApplication , QMainWindow , QPushButton
import sys
app=QApplication(sys.argv)

Window=QMainWindow()
Window.setWindowTitle("برنامج قياس الإنتاجية")
Window.resize(500,500)

button=QPushButton()
button.setText("click me")
button.setFixedSize(120,50)


Window.setCentralWidget(button)


Window.show()
app.exec()