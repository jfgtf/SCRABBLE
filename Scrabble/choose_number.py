# Form implementation generated from reading ui file 'ChooseNumbPlayers.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import players_input


class Ui_Form2(object):

    def open_choice(self):
        # self.window2 = QtWidgets.QMainWindow()
        # self.ui = playersInput.Ui_Form3(self.number_of_players)
        # self.ui.setupUi(self.window2)
        # self.window2.show()
        self.Form = QtWidgets.QWidget()
        self.ui = players_input.Ui_Form3(self.number_of_players)
        self.ui.setupUi(self.Form)
        self.Form.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 791)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 791))
        Form.setMaximumSize(QtCore.QSize(700, 791))
        Form.setStyleSheet("background-color:\"green\"\n""")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 700, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.twoPButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoPButton.sizePolicy().hasHeightForWidth())
        self.twoPButton.setSizePolicy(sizePolicy)
        self.twoPButton.setMinimumSize(QtCore.QSize(213, 35))
        self.twoPButton.setMaximumSize(QtCore.QSize(213, 35))
        self.twoPButton.setStyleSheet("background-color:\"lightblue\"\n""")
        self.twoPButton.setObjectName("twoPButton")
        self.twoPButton.clicked.connect(self.clicked_twoPButton)
        self.twoPButton.clicked.connect(self.open_choice)
        self.twoPButton.clicked.connect(Form.close)

        self.verticalLayout_2.addWidget(self.twoPButton)
        self.threePButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threePButton.sizePolicy().hasHeightForWidth())
        self.threePButton.setSizePolicy(sizePolicy)
        self.threePButton.setMinimumSize(QtCore.QSize(213, 35))
        self.threePButton.setMaximumSize(QtCore.QSize(213, 35))
        self.threePButton.setStyleSheet("background-color:\"lightblue\"\n""")
        self.threePButton.setObjectName("threePButton")
        self.threePButton.clicked.connect(self.clicked_threePButton)
        self.threePButton.clicked.connect(self.open_choice)
        self.threePButton.clicked.connect(Form.close)

        self.verticalLayout_2.addWidget(self.threePButton)
        self.fourPButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourPButton.sizePolicy().hasHeightForWidth())
        self.fourPButton.setSizePolicy(sizePolicy)
        self.fourPButton.setMinimumSize(QtCore.QSize(213, 35))
        self.fourPButton.setMaximumSize(QtCore.QSize(213, 35))
        self.fourPButton.setStyleSheet("background-color:\"lightblue\"\n""")
        self.fourPButton.setObjectName("fourPButton")
        self.fourPButton.clicked.connect(self.clicked_fourPButton)
        self.fourPButton.clicked.connect(self.open_choice)
        self.fourPButton.clicked.connect(Form.close)

        self.verticalLayout_2.addWidget(self.fourPButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 281))
        self.label.setPixmap(QtGui.QPixmap('Logo_gucci.png'))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.number_of_players = 0

    def clicked_twoPButton(self):
        self.number_of_players = 2

    def clicked_threePButton(self):
        self.number_of_players = 3

    def clicked_fourPButton(self):
        self.number_of_players = 4

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scrabble"))
        self.twoPButton.setText(_translate("Form", "2 Players"))
        self.threePButton.setText(_translate("Form", "3 Players"))
        self.fourPButton.setText(_translate("Form", "4 Players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
