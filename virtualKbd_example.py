import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit,  QLabel, QPushButton ,QDialog
import virtualKbd

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()       
        self.setWindowTitle('Simple GUI')
        self.layout = QVBoxLayout()
        
        self.label = QLabel('Enter your name:')
        self.layout.addWidget(self.label)
        
        self.line_edit = QLineEdit()
        self.line_edit.editingFinished.connect(self.line_edit_clicked)
        self.line_edit.mousePressEvent = self.line_edit_clicked
        self.layout.addWidget(self.line_edit) 
 
        self.setLayout(self.layout)
                        

    def line_edit_clicked(self, event=None):
        print(" line eadit clicked")
        virtualKbd.start(self.line_edit)
             
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    
    sys.exit(app.exec())




