import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class Calculator(QMainWindow):
  def __init__(self):
    super(Calculator,self).__init__()
    self.setWindowTitle("Calculator")
    self.setGeometry(1090,300,500,500)
    self.initUI()
  def initUI(self):
    self.lnumber1=QtWidgets.QLabel(self)
    self.lnumber1.setText("Number1")
    self.lnumber1.move(50,30)

    self.txtnumber1=QtWidgets.QLineEdit(self)
    self.txtnumber1.move(150,30)
    self.txtnumber1.resize(200,32)

    self.lnumber2 = QtWidgets.QLabel(self)
    self.lnumber2.setText("Number2")
    self.lnumber2.move(50, 80)

    self.txtnumber2 = QtWidgets.QLineEdit(self)
    self.txtnumber2.move(150, 80)
    self.txtnumber2.resize(200, 32)

    self.btnadd=QtWidgets.QPushButton(self)
    self.btnadd.setText("Add-Button")
    self.btnadd.move(150,130)
    self.btnadd.clicked.connect(self.calculate)

    self.btnsub = QtWidgets.QPushButton(self)
    self.btnsub.setText("Sub-Button")
    self.btnsub.move(150, 180)
    self.btnsub.clicked.connect(self.calculate)

    self.btnmul = QtWidgets.QPushButton(self)
    self.btnmul.setText("Mul-Button")
    self.btnmul.move(150, 230)
    self.btnmul.clicked.connect(self.calculate)

    self.btndiv = QtWidgets.QPushButton(self)
    self.btndiv.setText("Div-Button")
    self.btndiv.move(150, 280)
    self.btndiv.clicked.connect(self.calculate)

    self.lresult=QtWidgets.QLabel(self)

    self.lresult.setText("Result:")

    self.lresult.move(150,330)
  def calculate(self):
    sender=self.sender()
    print(sender.text())

    if sender.text()=="Add-Button":
      result=int(self.txtnumber1.text())+int(self.txtnumber2.text())

    elif sender.text()=="Sub-Button":
      result=int(self.txtnumber1.text())-int(self.txtnumber2.text())
    elif sender.text()=="Mul-Button":
      result=int(self.txtnumber1.text())*int(self.txtnumber2.text())
    elif sender.text()=="Div-Button":
      result=int(self.txtnumber1.text())//int(self.txtnumber2.text())

    self.lresult.setText("Result:"+str(result))






def app():
  app=QApplication(sys.argv)
  win=Calculator()
  win.show()
  sys.exit(app.exec_())
app()



