import sys
from PySide6.QtWidgets import QApplication 
from Button_holder import new


app=QApplication(sys.argv)

window=new()


window.show()
app.exec()