import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QPushButton
app=QApplication(sys.argv)


class new(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("الإنتاجية")
        button = QPushButton("click me")

        self.setCentralWidget(button)

window=new()


window.show()
app.exec()