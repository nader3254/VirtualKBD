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
        self.layout.addWidget(self.line_edit) 
        
        self.label = QLabel('Enter your password:')
        self.layout.addWidget(self.label)
        
        self.line_edit2 = QLineEdit()
        self.layout.addWidget(self.line_edit2) 
        
        
        self.setLayout(self.layout)
        virtualKbd.Registe(self.line_edit)                
        virtualKbd.Registe(self.line_edit2) 
        

             
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    
    sys.exit(app.exec())




