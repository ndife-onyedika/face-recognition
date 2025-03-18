import cv2
import os
import requests

from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QStackedLayout,
    QMessageBox,
)

class REGISTER_STUDENT(QDialog):
    def __init__(self, main_layout, components):
        super().__init__()
        self.main_layout = main_layout
        self.setWindowTitle("REGISTER STUDENT")
        # For other screens
        self.stacked = QStackedLayout()
        self.setupUI(components)

    def setupUI(self, components):
        self.comp = components()
        self.personal_details()
        # SETTING LAYOUTS
        self.setLayout(self.stacked)

    def personal_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Personal Details")

        _next = QPushButton("Next")

        # ADDING WIDGETS
        grid.addWidget(self.comp.f_name, 0, 0)
        grid.addWidget(self.comp.f_name_input, 0, 1)

        grid.addWidget(self.comp.m_name, 1, 0)
        grid.addWidget(self.comp.m_name_input, 1, 1)

        grid.addWidget(self.comp.l_name, 2, 0)
        grid.addWidget(self.comp.l_name_input, 2, 1)

        grid.addWidget(self.comp.dob_label, 3, 0)
        grid.addLayout(self.comp.dob_layout, 3, 1)

        grid.addWidget(self.comp.age, 4, 0)
        grid.addWidget(self.comp.age_input, 4, 1)

        grid.addWidget(self.comp.gender, 5, 0)
        grid.addLayout(self.comp.gender_layout, 5, 1)

        grid.addWidget(self.comp.marital, 6, 0)
        grid.addWidget(self.comp.marital_select, 6, 1)

        grid.addWidget(self.comp.nationality, 7, 0)
        grid.addWidget(self.comp.nationality_input, 7, 1)

        grid.addWidget(self.comp.state_origin, 8, 0)
        grid.addWidget(self.comp.state_origin_input, 8, 1)

        grid.addWidget(self.comp.lga_origin, 9, 0)
        grid.addWidget(self.comp.lga_origin_input, 9, 1)

        grid.addWidget(_next, 10, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.pd_main_widget = QWidget()
        self.pd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.pd_main_widget)
        self.stacked.setCurrentWidget(self.pd_main_widget)

        # When next button is clicked
        _next.clicked.connect(self.school_details)

    def school_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("School Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.j_num, 0, 0)
        grid.addWidget(self.comp.j_num_input, 0, 1)

        grid.addWidget(self.comp.college, 1, 0)
        grid.addWidget(self.comp.college_select, 1, 1)

        grid.addWidget(self.comp.dept, 2, 0)
        grid.addWidget(self.comp.dept_select, 2, 1)

        grid.addWidget(self.comp.level, 3, 0)
        grid.addWidget(self.comp.level_select, 3, 1)

        grid.addWidget(self.comp.m_num, 4, 0)
        grid.addWidget(self.comp.m_num_input, 4, 1)

        grid.addLayout(btn_view, 5, 0, 1, 0)

        # On change of College
        self.comp.college_select.currentIndexChanged.connect(self.school)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.sd_main_widget = QWidget()
        self.sd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.sd_main_widget)
        self.stacked.setCurrentWidget(self.sd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.pd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.contact_details)

    def contact_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Contact Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.address, 0, 0)
        grid.addWidget(self.comp.address_input, 0, 1)

        grid.addWidget(self.comp.phone, 1, 0)
        grid.addWidget(self.comp.phone_input, 1, 1)

        grid.addWidget(self.comp.email, 2, 0)
        grid.addWidget(self.comp.email_input, 2, 1)

        grid.addLayout(btn_view, 3, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.cd_main_widget = QWidget()
        self.cd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.cd_main_widget)
        self.stacked.setCurrentWidget(self.cd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.sd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.parent_details)

    def parent_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Parent/Sponsor Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.p_name, 0, 0)
        grid.addWidget(self.comp.p_name_input, 0, 1)

        grid.addWidget(self.comp.p_email, 1, 0)
        grid.addWidget(self.comp.p_email_input, 1, 1)

        grid.addWidget(self.comp.p_phone, 2, 0)
        grid.addWidget(self.comp.p_phone_input, 2, 1)

        grid.addLayout(btn_view, 3, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.psd_main_widget = QWidget()
        self.psd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.psd_main_widget)
        self.stacked.setCurrentWidget(self.psd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.cd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.done)

    def done(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox()

        btn_view = QHBoxLayout()
        _next = QPushButton("Capture Face")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.dor, 0, 0)
        grid.addWidget(self.comp.dor_text, 0, 1)

        grid.addLayout(btn_view, 1, 0, 1, 0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.d_main_widget = QWidget()
        self.d_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.d_main_widget)
        self.stacked.setCurrentWidget(self.d_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(
            lambda: self.stacked.setCurrentWidget(self.psd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.register_student_details)
        _next.setIcon(QIcon("./assets/icons/capture.png"))
        _next.setIconSize(QSize(20, 20))

    def register_student_details(self):
        # Assigning Variables
        data = {
            "first_name": str(self.comp.f_name_input.text()),
            "middle_name": str(self.comp.m_name_input.text()),
            "last_name": str(self.comp.l_name_input.text()),
            "date_of_birth": str(self.comp.dob_date_label.text()),
            "age": str(self.comp.age_input.text()),
            "gender": str(
                (
                    self.comp.gender_1.text()
                    if self.comp.gender_1.isChecked()
                    else self.comp.gender_2.text()
                )
            ),
            "nationality": str(self.comp.nationality_input.text()),
            "state_of_origin": str(self.comp.state_origin_input.text()),
            "lga_origin": str(self.comp.lga_origin_input.text()),
            "marital_status": str(self.comp.marital_select.currentText()),
            # Assigning Variables
            "jamb_number": str(self.comp.j_num_input.text()),
            "college": str(self.comp.college_select.currentText()),
            "department": str(self.comp.dept_select.currentText()),
            "level": str(self.comp.level_select.currentText()),
            "matric_number": str(self.comp.m_num_input.text()),
            # Assigning Variables
            "address": str(self.comp.address_input.text()),
            "phone_number": str(self.comp.phone_input.text()),
            "email": str(self.comp.email_input.text()),
            # Assigning Variables
            "parent_name": str(self.comp.p_name_input.text()),
            "parent_email": str(self.comp.p_email_input.text()),
            "parent_phone": str(self.comp.p_phone_input.text()),
            "date_of_registration": str(self.comp.dor_text.text()),
        }

        for value in data.values():
            if value == "":
                msg = QMessageBox()
                msg.setIconPixmap(QPixmap("./assets/icons/no_entry.png"))
                msg.setWindowTitle("Empty Entry")
                msg.setText("Please Check Entries!")
                msg.show()
                if msg.exec_() or msg == QMessageBox.Ok:
                    break
            else:
                break

        if self.comp.isConnected():
            # sending post request and saving response as response object
            r = requests.post(url=f"{self.comp.APP_URL}/register/students/", data=data)
            self.register_face()

    def register_face(self):
        r = requests.get(url=f"{self.comp.APP_URL}/register/students/")

        student = r.json()

        self._id = student["id"]

        self.comp._start_video(self.super_layout)
        self.comp.video_init_layout.removeWidget(self.comp.back_btn)
        self.comp.cam_btn.clicked.connect(
            lambda: self.snap(self.comp.image, self.comp.timer, self.comp.cam)
        )

    def snap(self, image, timer, cam):
        image_cropped = image[0:480, 80:560]

        cv2.imwrite("./assets/temp/temp.jpg", image_cropped)

        timer.stop()
        cam.release()

        for img in os.listdir("./assets/temp/"):
            file = {"image": open(f"./assets/temp/{img}", "rb").read()}
            r = requests.post(url=f"{self.comp.APP_URL}/register/students/{self._id}", files=file)

        self.main_layout.setCurrentIndex(0)


    def school(self, i):
        if i == 0 or i == 1 or i == 4 or i == 6 or i == 7 or i == 9 or i == 10:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L"])
        elif i == 2 or i == 3 or i == 5 or i == 8:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L", "500L"])
        elif i == 11:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(
                ["100L", "200L", "300L", "400L", "500L", "600L"]
            )

        if i == 0:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRIBUSINESS MANAGEMENT",
                    "AGRICULTURAL ECONOMICS",
                    "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
                ]
            )

        elif i == 1:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ANIMAL BREEDING AND PHYSIOLOGY",
                    "ANIMAL NUTRITION AND FORAGE SCIENCE",
                    "ANIMAL PRODUCTION AND LIVESTOCK MANAGEMENT",
                ]
            )

        elif i == 2:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FOOD SCIENCE AND TECHNOLOGY",
                    "HOME SCIENCE/HOSPITALITY MANAGEMENT AND TOURISM",
                    "HUMAN NUTRITION AND DIETETICS",
                ]
            )
        elif i == 3:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                ["AGRONOMY", "PLANT HEALTH MANAGEMENT", "SOIL SCIENCE AND METREOLOGY"]
            )
        elif i == 4:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ADULT AND CONTINUING EDUCATION",
                    "EDUCATIONAL FOUNDATION",
                    "INDUSTRIAL TECHNOLOGY EDUCATION",
                    "LIBRARY AND INFORMATION SCIENCE",
                    "PSYCHOLOGY AND COUNSELING",
                    "SCIENCE EDUCATION",
                ]
            )
        elif i == 5:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRICULTURAL AND BIO-RESOURCES ENGINEERING",
                    "CHEMICAL ENGINEERING",
                    "CIVIL ENGINEERING",
                    "COMPUTER ENGINEERING",
                    "ELECTRICAL AND ELECTRONICS ENGINEERING",
                    "MECHANICAL ENGINEERING",
                ]
            )
        elif i == 6:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FRENCH LANGUAGE",
                    "GERMAN LANGUAGE",
                    "HISTORY AND PHILOSOPHY OF SCIENCE",
                    "NIGERIA HISTORY",
                    "PEACE AND CONFLICT STUDIES",
                    "PHILOSOPHY AND LOGIC",
                    "PHYSICAL AND HEALTH EDUCATION",
                    "SOCIAL SCIENCE",
                ]
            )
        elif i == 7:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ACCOUNTING",
                    "BANKING AND FINANCE",
                    "BUSINESS ADMINISTRATION",
                    "ECONOMICS",
                    "ENTREPRENEURIAL STUDIES",
                    "HUMAN RESOURCE MANAGEMENT",
                    "MARKETING",
                ]
            )
        elif i == 8:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ENVIRONMENTAL MANAGEMENT AND TOXICOLOGY",
                    "FORESTRY AND ENVIRONMENTAL MANAGEMENT",
                    "FISHERIES AND AQUATIC RESOURCES MANAGEMENT",
                ]
            )
        elif i == 9:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "BIOCHEMISTRY",
                    "MICROBIOLOGY",
                    "PLANT SCIENCE AND BIOTECHNOLOGY",
                    "ZOOLOGY AND ENVIRONMENTAL BIOLOGY",
                ]
            )

        elif i == 10:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "CHEMISTRY",
                    "PHYSICS",
                    "COMPUTER SCIENCE",
                    "STATISTICS",
                    "MATHEMATICS",
                ]
            )

        elif i == 11:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "VERTINARY ANATOMY",
                    "VERTINARY MEDICINE",
                    "VERTINARY PUBLIC HEALTH AND PREVENTIVE MEDICINE",
                ]
            )
