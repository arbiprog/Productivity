from PySide6.QtWidgets import QMainWindow , QPushButton



class new(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("الإنتاجية")
        button = QPushButton("click me")

        self.setCentralWidget(button)