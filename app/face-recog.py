import sys
import qdarkstyle
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
)

from main_window.main_window import MAIN_WINDOW
from components.components import COMPONENTS
class LOGIN(QDialog):
    def __init__(self):
        super().__init__()
        self.move(500, 200)
        self.setFixedSize(350, 250)

        self.setStyleSheet(open("./assets/css/login.css").read())

        self.setWindowTitle("LOGIN")

        self.comp = COMPONENTS()

        self._component()

    def _component(self):
        self.main_grid = QGridLayout()

        self.user_name_label = QLabel("Username:")
        self.user_name_label.setObjectName("Label")
        self.user_name_input = QLineEdit()

        self.pass_word_label = QLabel("Password:")
        self.pass_word_label.setObjectName("Label")
        self.pass_word_input = QLineEdit()
        self.pass_word_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self._handle_login)

        self._setup_ui()

    def _setup_ui(self):
        self.main_grid.addWidget(self.user_name_label, 0, 0)
        self.main_grid.addWidget(self.user_name_input, 0, 1)

        self.main_grid.addWidget(self.pass_word_label, 1, 0)
        self.main_grid.addWidget(self.pass_word_input, 1, 1)

        self.main_grid.addWidget(self.login_btn, 2, 0, 1, 0)

        self.setLayout(self.main_grid)

    def _handle_login(self):
        user_name = str(self.user_name_input.text())
        pass_word = str(self.pass_word_input.text())

        data = {"user_name": user_name, "pass_word": pass_word}

        r = requests.post(url=f"{self.comp.APP_URL}", data=data)

        if r.text == "Authentication Success":
            self.hide()
            self.app_view = MAIN_WINDOW()
            self.app_view.show()
        elif self.user_name_input.text() == "" and self.pass_word_input.text() == "":
            self.comp.msg.setWindowTitle("Error!")
            self.comp.msg.setWindowIcon(QIcon("./assets/icons/no_entry.png"))
            self.comp.msg.setText("Username and Password cannot be empty")
            self.comp.msg.show()
            self.comp.msg.exec_()
        elif (
            self.user_name_input.text() == "" and not self.pass_word_input.text() == ""
        ):
            self.comp.msg.setWindowTitle("Error!")
            self.comp.msg.setWindowIcon(QIcon("./assets/icons/no_entry.png"))
            self.comp.msg.setText("Username cannot be empty")
            self.comp.msg.show()
            self.comp.msg.exec_()
        elif (
            not self.user_name_input.text() == "" and self.pass_word_input.text() == ""
        ):
            self.comp.msg.setWindowTitle("Error!")
            self.comp.msg.setWindowIcon(QIcon("./assets/icons/no_entry.png"))
            self.comp.msg.setText("Password cannot be empty")
            self.comp.msg.show()
            self.comp.msg.exec_()
        elif r.text == "Incorrect Password":
            self.comp.msg.setWindowTitle("Error!")
            self.comp.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
            self.comp.msg.setText("Incorrect Password")
            self.comp.msg.show()
            self.comp.msg.exec_()
        else:
            self.comp.msg.setWindowTitle("Error!")
            self.comp.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
            self.comp.msg.setText("Username and Password are Incorrect")
            self.comp.msg.show()
            self.comp.msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    view = LOGIN()
    view.setWindowIcon(QIcon("./assets/icons/login.png"))

    if COMPONENTS().isConnected():
        view.show()
        view.raise_()
    sys.exit(app.exec_())
