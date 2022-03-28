from PyQt5 import QtCore, QtGui, QtWidgets
from Screens import Screen1
from Screens.Screen1 import Ui_CreateCompany

class Ui_AccountingSoftware(object):
    def Create_Company_Screen(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = Screen1.Ui_CreateCompany()
        self.ui.setupUi(self.win)
        self.win.show()
        
    def setupUi(self, AccountingSoftware):
        AccountingSoftware.setObjectName("AccountingSoftware")
        AccountingSoftware.resize(593, 256)
        AccountingSoftware.setMinimumSize(QtCore.QSize(593, 256))
        AccountingSoftware.setMaximumSize(QtCore.QSize(593, 297))
        AccountingSoftware.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AccountingSoftware)
        self.centralwidget.setMinimumSize(QtCore.QSize(593, 256))
        self.centralwidget.setMaximumSize(QtCore.QSize(593, 250))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 281, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 361, 51))
        self.label.setStyleSheet("font: 12pt \"OCR A Extended\";\n"
"text-decoration: underline;\n"
"font: 24pt \"OCR A Extended\";\n"
"color: rgb(255, 170, 127);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.Create_Company_Screen())
        self.pushButton_2.setGeometry(QtCore.QRect(160, 130, 281, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        AccountingSoftware.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AccountingSoftware)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        AccountingSoftware.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AccountingSoftware)
        self.statusbar.setObjectName("statusbar")
        AccountingSoftware.setStatusBar(self.statusbar)
        self.actionCreate_company = QtWidgets.QAction(AccountingSoftware)
        self.actionCreate_company.setObjectName("actionCreate_company")
        self.actionCreate_company_2 = QtWidgets.QAction(AccountingSoftware)
        self.actionCreate_company_2.setObjectName("actionCreate_company_2")
        self.actionExit = QtWidgets.QAction(AccountingSoftware)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionCreate_company)
        self.menuMenu.addAction(self.actionCreate_company_2)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(AccountingSoftware)
        QtCore.QMetaObject.connectSlotsByName(AccountingSoftware)
        AccountingSoftware.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, AccountingSoftware):
        _translate = QtCore.QCoreApplication.translate
        AccountingSoftware.setWindowTitle(_translate("AccountingSoftware", "MainWindow"))
        self.pushButton.setText(_translate("AccountingSoftware", "SELECT COMPANY"))
        self.label.setText(_translate("AccountingSoftware", "ACCOUNTING SOFTWARE"))
        self.pushButton_2.setText(_translate("AccountingSoftware", "CREATE COMPANY"))
        self.menuMenu.setTitle(_translate("AccountingSoftware", "Menu"))
        self.actionCreate_company.setText(_translate("AccountingSoftware", "Select company"))
        self.actionCreate_company_2.setText(_translate("AccountingSoftware", "Create company"))
        self.actionExit.setText(_translate("AccountingSoftware", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountingSoftware = QtWidgets.QMainWindow()
    ui = Ui_AccountingSoftware()
    ui.setupUi(AccountingSoftware)
    AccountingSoftware.show()
    sys.exit(app.exec_())
