import os

import cv2
import requests
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import (QDialog, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QMessageBox, QPushButton, QStackedLayout,
                             QVBoxLayout, QWidget)
class REGISTER_STAFF(QDialog):
    def __init__(self, super_layout, components):
        super().__init__()
        self.super_layout = super_layout
        self.comp = components()
        self.setWindowTitle("REGISTER STAFF")
        self.stacked = QStackedLayout()
        self.setupUI()

    def setupUI(self):
        self.setLayout(self.stacked)
        self.personal_details()

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
        group_box = QGroupBox("Work Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.profession, 0, 0)
        grid.addWidget(self.comp.profession_input, 0, 1)

        grid.addLayout(btn_view, 1, 0, 1, 0)

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
        _next.clicked.connect(self.done)

    def done(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox()

        btn_view = QHBoxLayout()
        _next = QPushButton("Capture Face")
        _prev = QPushButton("Previous")
        _next.setIcon(QIcon("./assets/icons/capture.png"))
        _next.setIconSize(QSize(20, 20))

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
            lambda: self.stacked.setCurrentWidget(self.cd_main_widget)
        )

        # When next button is clicked
        _next.clicked.connect(self.register_staff_details)

    def register_staff_details(self):
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
            "profession": str(self.comp.profession_input.text()),
            # Assigning Variables
            "address": str(self.comp.address_input.text()),
            "phone_number": str(self.comp.phone_input.text()),
            "email": str(self.comp.email_input.text()),
            # Assigning Variables
            "date_of_registration": str(self.comp.dor_text.text()),
        }

        for value in data.values():
            if value == "":
                msg = QMessageBox()
                msg.setIconPixmap(QPixmap("./assets/icons/no_entry.png"))
                msg.setWindowTitle("Empty Field")
                msg.setWindowIcon(QIcon("./assets/icons/error.png"))
                msg.setText("Please Check Entries!")
                msg.show()
                if msg.exec_() or msg ==  QMessageBox.Ok:
                    break
            else:
                break

        if self.comp.isConnected():
            # sending post request and saving response as response object
            r = requests.post(url=f"{self.comp.APP_URL}/register/staff/", data=data)
            self.register_face()

    def register_face(self):
        r = requests.get(url=f"{self.comp.APP_URL}/register/staff/")

        staff = r.json()

        self._id = staff["id"]

        self.comp._start_video(self.super_layout)
        self.comp.video_init_layout.removeWidget(self.comp.back_btn)
        self.comp.cam_btn.clicked.connect(
            lambda: self.snap(self.comp.image, self.comp.timer, self.comp.cam)
        )

    def snap(self, image, timer, cam):
        image_cropped = image[0:480, 80:560]
        cv2.imwrite(
            "./assets/temp/temp.jpg", image_cropped,
        )

        timer.stop()
        cam.release()

        for img in os.listdir("./assets/temp/"):
            file = {"image": open(f"./assets/temp/{img}", "rb").read()}
            r = requests.post(url=f"{self.comp.APP_URL}/register/staff/{self._id}", files=file)

        self.super_layout.setCurrentIndex(0)
