from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QStackedLayout,
    QCommandLinkButton,
    QStackedWidget,
)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from register.register_main import REGISTER_MAIN
from student_detail.student_details import VERIFY as Student_Verify
from staff_detail.staff_details import VERIFY as Staff_Verify


class MAIN_WINDOW(QWidget):
    def __init__(self):
        super().__init__()
        self.move(350, 150)
        self.setMinimumSize(640, 480)
        self.win_title = "FACE RECOGNITION"
        self.setWindowTitle(self.win_title)

        self.setStyleSheet(open("./assets/css/main.css").read())

        # Main Layout of Widget
        self.super_layout = QStackedLayout()
        self.setLayout(self.super_layout)

        self._view()
        self._other_view()

    def _view(self):
        initial_layout = QGridLayout()

        register = QPushButton("Register")
        register.setIcon(QIcon("./assets/icons/add_users.png"))
        register.setIconSize(QSize(50, 50))

        stud_det = QPushButton("Student")
        stud_det.setIcon(QIcon("./assets/icons/student.png"))
        stud_det.setIconSize(QSize(50, 50))

        staf_det = QPushButton("Staff")
        staf_det.setIcon(QIcon("./assets/icons/staff.png"))
        staf_det.setIconSize(QSize(50, 50))

        register.setObjectName("main_btn")
        stud_det.setObjectName("main_btn")
        staf_det.setObjectName("main_btn")

        initial_layout.addWidget(register, 0, 0, 1, 0)
        initial_layout.addWidget(stud_det, 1, 0)
        initial_layout.addWidget(staf_det, 1, 1)

        self.main_widget = QWidget()
        self.main_widget.setLayout(initial_layout)

        self.super_layout.addWidget(self.main_widget)

        register.clicked.connect(
            lambda: self._handle_open_register_view(self.super_layout)
        )
        stud_det.clicked.connect(self._handle_open_student_details_view)
        staf_det.clicked.connect(self._handle_open_staff_details_view)

    def _other_view(self):
        # For other screens aside Login Screen And Main View Screen
        self.stacked = QStackedWidget()
        self.main_grid_widget = QWidget()
        self.main_grid = QGridLayout()
        back_btn = QCommandLinkButton()
        back_btn.setIcon(QIcon("./assets/icons/back.png"))
        back_btn.setIconSize(QSize(30, 30))
        self.main_grid_widget.setLayout(self.main_grid)

        self.main_grid.addWidget(back_btn, 0, 0)
        self.main_grid.addWidget(self.stacked, 1, 0, 1, 0)

        back_btn.clicked.connect(self._handle_go_back)
        back_btn.setMaximumWidth(45)

    def _handle_open_register_view(self, main_layout):
        self.setWindowTitle("REGISTER")

        self.reg_view = REGISTER_MAIN(main_layout)

        self.stacked.addWidget(self.reg_view.main_widget)
        self.stacked.setCurrentWidget(self.reg_view.main_widget)

        self.super_layout.addWidget(self.main_grid_widget)
        self.super_layout.setCurrentWidget(self.main_grid_widget)

    def _handle_open_student_details_view(self):

        self.ver_view = Student_Verify(
            self,
            self.super_layout,
            self.main_grid_widget,
            self.stacked,
            self._handle_go_back,
        )

    def _handle_open_staff_details_view(self):

        self.ver_view = Staff_Verify(
            self,
            self.super_layout,
            self.main_grid_widget,
            self.stacked,
            self._handle_go_back,
        )

    def _handle_go_back(self):
        self.super_layout.setCurrentIndex(0)
        self.setWindowTitle(self.win_title)

