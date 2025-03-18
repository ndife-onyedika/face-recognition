from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from components.components import COMPONENTS

from .register_staff import REGISTER_STAFF
from .register_students import REGISTER_STUDENT


class REGISTER_MAIN(QWidget):
    def __init__(self, super_layout):
        super().__init__()
        self.super_layout = super_layout
        self.components = COMPONENTS

        self.UI()

    def UI(self):
        initial_layout = QVBoxLayout()

        self.main_widget = QTabWidget()

        initial_layout.addWidget(self.main_widget)
        self.setLayout(initial_layout)

        self.reg_stud_win()
        self.reg_staf_win()

    def reg_stud_win(self):
        stud_dialog = REGISTER_STUDENT(self.super_layout, self.components)
        self.main_widget.addTab(stud_dialog, "Register Student")
        self.main_widget.setTabIcon(0, QIcon("./assets/icons/register.png"))

    def reg_staf_win(self):
        staf_dialog = REGISTER_STAFF(self.super_layout, self.components)
        self.main_widget.addTab(staf_dialog, "Register Staff")
        self.main_widget.setTabIcon(1, QIcon("./assets/icons/register.png"))
