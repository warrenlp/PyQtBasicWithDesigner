
from .process_dialog import Ui_Dialog
from PyQt5 import QtCore


class MainDialog(Ui_Dialog, QtCore.QObject):

    def __init__(self, dialog):
        super().__init__()
        self.setupUi(dialog)
