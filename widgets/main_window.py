
from widgets.main import Ui_MainWindow
from widgets.main_dialog import MainDialog

from PyQt5 import QtCore, QtWidgets


class MainWindow(Ui_MainWindow, QtCore.QObject):

    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(MainWindow)

        self.launchButton.clicked.connect(self.launch_dialog)

        self.dialog_end = False

    @QtCore.pyqtSlot()
    def launch_dialog(self):
        qdialog = QtWidgets.QDialog()
        MainDialog(qdialog)
        result = qdialog.exec()

        print(f"Result: {result}")

    @QtCore.pyqtSlot()
    def end_dialog(self):
        self.dialog_end = True
