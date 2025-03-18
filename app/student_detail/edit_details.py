import requests
import cv2
import os
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (
    QAction,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from components.components import COMPONENTS
from register.register_students import REGISTER_STUDENT

class EDIT_DETAILS(QMainWindow):
    def __init__(self, title, prev_scrn, profile, super_layout):
        super().__init__()
        self.title = title
        self.title.setWindowTitle("EDIT STUDENT DETAILS")

        self.super_layout = super_layout

        self.previous = prev_scrn

        self.MAIN_VIEW(profile)

    def MAIN_VIEW(self, profile):
        self.comp = COMPONENTS()

        _id = int(profile["id"])

        r = requests.get(url=f"{APP_URL}/users/students/{_id}")

        self.profile = r.json()

        self.main_menu = self.menuBar()
        self.toolbar = QToolBar()

        self.file_menu = self.main_menu.addMenu("File")

        self.export = QAction(QIcon("./assets/icons/export_pdf.png"), "Export as PDF", self)
        self.export.setShortcut("Ctrl+S")

        self.exit_action = QAction(QIcon("./assets/icons/exit.png"), "Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.export)
        self.file_menu.addAction(self.exit_action)

        self.export.triggered.connect(self._save_as_file)
        self.exit_action.triggered.connect(lambda: self.previous())

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.export)

        self.main_widget = QWidget()
        self.vbox = QVBoxLayout()

        self.personal_details()

        self.contact_details()

        self.parent_detail()

        self.other_detail()

        self.main_widget.setLayout(self.vbox)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.main_widget)
        self.scroll.setWidgetResizable(True)

        self.setCentralWidget(self.scroll)

        self.super_layout.addWidget(self)
        self.super_layout.setCurrentWidget(self)

    def personal_details(self):
        _group_box = QGroupBox("Personal Details")
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        # for views containing school detail of student
        self.sd_view = QHBoxLayout()
        self.sd_detail_view = QGridLayout()

        _grid.addLayout(self.sd_view, 0, 0, 1, 0)

        self.sd_view.addLayout(self.sd_detail_view)
        self.sd_view.addLayout(self.comp.pro_pic_view)

        r = requests.get(url=self.profile["pic"], stream=True)

        pic = QImage()
        pic.loadFromData(r.content)

        self.comp.profile_pic.setPixmap(QPixmap.fromImage(pic))

        self.comp.change_pro.clicked.connect(lambda: self.comp._start_video(self.super_layout))

        self.comp.cam_btn.clicked.connect(
            lambda: self.snap(self.comp.image, self.comp.timer, self.comp.cam)
        )


        self.sd_detail_view.addWidget(self.comp.m_num, 0, 0)
        self.sd_detail_view.addWidget(self.comp.m_num_input, 0, 1)
        self.comp.m_num_input.setText(self.profile["matric_number"])

        self.sd_detail_view.addWidget(self.comp.j_num, 1, 0)
        self.sd_detail_view.addWidget(self.comp.j_num_input, 1, 1)
        self.comp.j_num_input.setText(self.profile["jamb_number"])

        self.sd_detail_view.addWidget(self.comp.college, 2, 0)
        self.sd_detail_view.addWidget(self.comp.college_select, 2, 1)
        self.comp.college_select.setCurrentText(self.profile["college"])
        self.school()
        self.comp.college_select.currentIndexChanged.connect(
            lambda: REGISTER_STUDENT.school(
                self, self.comp.college_select.currentIndex()
            )
        )

        self.sd_detail_view.addWidget(self.comp.dept, 3, 0)
        self.sd_detail_view.addWidget(self.comp.dept_select, 3, 1)
        self.comp.dept_select.setCurrentText(self.profile["department"])

        self.sd_detail_view.addWidget(self.comp.level, 4, 0)
        self.sd_detail_view.addWidget(self.comp.level_select, 4, 1)
        self.comp.level_select.setCurrentText(self.profile["level"])

        self.pd_detail_view = QGridLayout()
        self.name = QLabel("Name:")
        self.name.setObjectName("Label")

        _grid.addWidget(self.name, 1, 0)

        self.pd_detail_view.addWidget(self.comp.l_name, 0, 0)
        self.pd_detail_view.addWidget(self.comp.l_name_input, 0, 1)
        self.comp.l_name_input.setText(self.profile["last_name"])

        self.pd_detail_view.addWidget(self.comp.m_name, 1, 0)
        self.pd_detail_view.addWidget(self.comp.m_name_input, 1, 1)
        self.comp.m_name_input.setText(self.profile["middle_name"])

        self.pd_detail_view.addWidget(self.comp.f_name, 2, 0)
        self.pd_detail_view.addWidget(self.comp.f_name_input, 2, 1)
        self.comp.f_name_input.setText(self.profile["first_name"])

        _grid.addLayout(self.pd_detail_view, 1, 1)

        _grid.addWidget(self.comp.age, 2, 0)
        _grid.addWidget(self.comp.age_input, 2, 1)
        self.comp.age_input.setText(str(self.profile["age"]))

        _grid.addWidget(self.comp.gender, 3, 0)
        _grid.addLayout(self.comp.gender_layout, 3, 1)
        if self.comp.gender_1.text() == self.profile["gender"].upper():
            self.comp.gender_1.setChecked(True)
        else:
            self.comp.gender_2.setChecked(True)

        _grid.addWidget(self.comp.dob_label, 4, 0)
        _grid.addLayout(self.comp.dob_layout, 4, 1)
        self.comp.dob_date_label.setText(str(self.profile["date_of_birth"]))

        _grid.addWidget(self.comp.nationality, 5, 0)
        _grid.addWidget(self.comp.nationality_input, 5, 1)
        self.comp.nationality_input.setText(self.profile["nationality"])

        _grid.addWidget(self.comp.state_origin, 6, 0)
        _grid.addWidget(self.comp.state_origin_input, 6, 1)
        self.comp.state_origin_input.setText(self.profile["state_of_origin"])

        _grid.addWidget(self.comp.lga_origin, 7, 0)
        _grid.addWidget(self.comp.lga_origin_input, 7, 1)
        self.comp.lga_origin_input.setText(self.profile["lga_origin"])

        _grid.addWidget(self.comp.marital, 8, 0)
        _grid.addWidget(self.comp.marital_select, 8, 1)
        self.comp.marital_select.setCurrentText(self.profile["marital_status"])

        self.vbox.addWidget(_group_box)
        
    def contact_details(self):
        _group_box = QGroupBox("Contact Details")
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        _grid.addWidget(self.comp.address, 0, 0)
        _grid.addWidget(self.comp.address_input, 0, 1)
        self.comp.address_input.setText(self.profile["address"])

        _grid.addWidget(self.comp.phone, 1, 0)
        _grid.addWidget(self.comp.phone_input, 1, 1)
        self.comp.phone_input.setText(self.profile["phone_number"])

        _grid.addWidget(self.comp.email, 2, 0)
        _grid.addWidget(self.comp.email_input, 2, 1)
        self.comp.email_input.setText(self.profile["email"])

        self.vbox.addWidget(_group_box)

    def parent_detail(self):
        _group_box = QGroupBox("Parent's/Sponsor's Details")
        _grid = QGridLayout()

        _group_box.setLayout(_grid)

        _grid.addWidget(self.comp.p_name, 0, 0)
        _grid.addWidget(self.comp.p_name_input, 0, 1)
        self.comp.p_name_input.setText(self.profile["parent_name"])

        _grid.addWidget(self.comp.p_email, 1, 0)
        _grid.addWidget(self.comp.p_email_input, 1, 1)
        self.comp.p_email_input.setText(self.profile["parent_email"])

        _grid.addWidget(self.comp.p_phone, 2, 0)
        _grid.addWidget(self.comp.p_phone_input, 2, 1)
        self.comp.p_phone_input.setText(self.profile["parent_phone"])

        self.vbox.addWidget(_group_box)

    def other_detail(self):
        _group_box = QGroupBox("Parent's/Sponsor's Details")
        _grid = QGridLayout()

        _grid.addWidget(self.comp.dor, 0, 0)
        self.dor_text = QLabel()
        _grid.addWidget(self.dor_text, 0, 1)
        self.dor_text.setText(str(self.profile["date_of_registration"]))

        _group_box.setLayout(_grid)

        self.vbox.addWidget(_group_box)

        self.save_2_db = QPushButton("SAVE")
        self.save_2_db.setIcon(QIcon("./assets/icons/save_2_db.png"))
        self.save_2_db.setIconSize(QSize(20, 20))

        self.vbox.addWidget(self.save_2_db)

        self.save_2_db.clicked.connect(self._save_2_db)


    def _save_2_db(self):
        _id = int(self.profile["id"])

        for image in os.listdir("./assets/temp/"):
            entries = {
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

            file = {"image": open(f"./assets/temp/{image}", "rb").read()}

            if self.comp.isConnected():
                r = requests.post(url=f"{APP_URL}/users/students/{_id}", data=entries, files=file)

    def _save_as_file(self):
        self._save_2_db()
        
        from student_detail.view_details import VIEW_DETAILS
        view_details = VIEW_DETAILS._save_file(self)

    def snap(self, image, timer, cam):
        image_cropped = image[0:480, 80:560]
        cv2.imwrite(
            "./assets/temp/temp.jpg", image_cropped,
        )

        timer.stop()
        cam.release()

        self.super_layout.setCurrentWidget(self)

        self.comp.profile_pic.setPixmap(QPixmap.fromImage(QImage("./assets/temp/temp.jpg")))

    def school(self):
        if (
            self.comp.college_select.currentIndex() == 0
            or self.comp.college_select.currentIndex() == 1
            or self.comp.college_select.currentIndex() == 4
            or self.comp.college_select.currentIndex() == 6
            or self.comp.college_select.currentIndex() == 7
            or self.comp.college_select.currentIndex() == 9
            or self.comp.college_select.currentIndex() == 10
        ):
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L"])
        elif (
            self.comp.college_select.currentIndex() == 2
            or self.comp.college_select.currentIndex() == 3
            or self.comp.college_select.currentIndex() == 5
            or self.comp.college_select.currentIndex() == 8
        ):
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L", "500L"])
        elif self.comp.college_select.currentIndex() == 11:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(
                ["100L", "200L", "300L", "400L", "500L", "600L"]
            )

        if self.comp.college_select.currentIndex() == 0:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRIBUSINESS MANAGEMENT",
                    "AGRICULTURAL ECONOMICS",
                    "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
                ]
            )

        elif self.comp.college_select.currentIndex() == 1:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ANIMAL BREEDING AND PHYSIOLOGY",
                    "ANIMAL NUTRITION AND FORAGE SCIENCE",
                    "ANIMAL PRODUCTION AND LIVESTOCK MANAGEMENT",
                ]
            )

        elif self.comp.college_select.currentIndex() == 2:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FOOD SCIENCE AND TECHNOLOGY",
                    "HOME SCIENCE/HOSPITALITY MANAGEMENT AND TOURISM",
                    "HUMAN NUTRITION AND DIETETICS",
                ]
            )
        elif self.comp.college_select.currentIndex() == 3:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                ["AGRONOMY", "PLANT HEALTH MANAGEMENT", "SOIL SCIENCE AND METREOLOGY"]
            )
        elif self.comp.college_select.currentIndex() == 4:
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
        elif self.comp.college_select.currentIndex() == 5:
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
        elif self.comp.college_select.currentIndex() == 6:
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
        elif self.comp.college_select.currentIndex() == 7:
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
        elif self.comp.college_select.currentIndex() == 8:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ENVIRONMENTAL MANAGEMENT AND TOXICOLOGY",
                    "FORESTRY AND ENVIRONMENTAL MANAGEMENT",
                    "FISHERIES AND AQUATIC RESOURCES MANAGEMENT",
                ]
            )
        elif self.comp.college_select.currentIndex() == 9:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "BIOCHEMISTRY",
                    "MICROBIOLOGY",
                    "PLANT SCIENCE AND BIOTECHNOLOGY",
                    "ZOOLOGY AND ENVIRONMENTAL BIOLOGY",
                ]
            )

        elif self.comp.college_select.currentIndex() == 10:
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

        elif self.comp.college_select.currentIndex() == 11:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "VERTINARY ANATOMY",
                    "VERTINARY MEDICINE",
                    "VERTINARY PUBLIC HEALTH AND PREVENTIVE MEDICINE",
                ]
            )
