from PyQt6 import QtWidgets
import menu

import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = menu.Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec())
