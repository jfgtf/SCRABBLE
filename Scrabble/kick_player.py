# Form implementation generated from reading ui file 'Blocke_player.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form7(object):
    def __init__(self, aux_kicked_name):
        self.kicked_name = aux_kicked_name

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(239, 121)
        Form.setStyleSheet("background-color:\"lightgreen\"\n"
"")
        self.nextPlabel = QtWidgets.QLabel(Form)
        self.nextPlabel.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextPlabel.setFont(font)
        self.nextPlabel.setObjectName("nextPlabel")
        self.playerNamelabel = QtWidgets.QLabel(Form)
        self.playerNamelabel.setGeometry(QtCore.QRect(20, 60, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerNamelabel.sizePolicy().hasHeightForWidth())
        self.playerNamelabel.setSizePolicy(sizePolicy)
        self.playerNamelabel.setMinimumSize(QtCore.QSize(200, 30))
        self.playerNamelabel.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playerNamelabel.setFont(font)
        self.playerNamelabel.setText(self.kicked_name)
        self.playerNamelabel.setObjectName("playerNamelabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nextPlabel.setText(_translate("Form", "Blocked player:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form7("XD")
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())