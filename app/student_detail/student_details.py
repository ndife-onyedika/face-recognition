import cv2
import os
import requests

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QCommandLinkButton,
    QMessageBox,
)

from components.components import COMPONENTS

from .view_details import VIEW_DETAILS
from .edit_details import EDIT_DETAILS

class VERIFY(QWidget):
    def __init__(self, title, super_layout, grid_widget, stacked, prev):
        super().__init__()
        self.title = title
        self.previous = prev
        self.stacked = stacked
        self.grid_widget = grid_widget

        self.comp = COMPONENTS()

        self.super_layout = super_layout

        self.comp._start_video(self.super_layout)
        self.comp.back_btn.clicked.connect(
            lambda: self._go_back(self.comp.timer, self.comp.cam)
        )
        self.comp.cam_btn.clicked.connect(
            lambda: self.snap(self.comp.image, self.comp.timer, self.comp.cam)
        )

    def MAIN_VIEW(self, prev, profile):
        self.title.setWindowTitle("STUDENT DETAILS")
        self.profile = profile
        self.initial_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.view_details_btn = QPushButton("View Profile")
        self.edit_details_btn = QPushButton("Edit Profile")

        self.view_details_btn.setObjectName("btn")
        self.edit_details_btn.setObjectName("btn")

        self.view_details_btn.setIcon(QIcon("./assets/icons/view_profile.png"))
        self.edit_details_btn.setIcon(QIcon("./assets/icons/edit_profile.png"))

        self.view_details_btn.setIconSize(QSize(50, 50))
        self.edit_details_btn.setIconSize(QSize(50, 50))

        self.initial_layout.addWidget(self.view_details_btn)
        self.initial_layout.addWidget(self.edit_details_btn)

        self.main_widget.setLayout(self.initial_layout)

        self.stacked.addWidget(self.main_widget)
        self.stacked.setCurrentWidget(self.main_widget)

        self.super_layout.addWidget(self.grid_widget)
        self.super_layout.setCurrentWidget(self.grid_widget)

        self.view_details_btn.clicked.connect(self._handle_view_details)
        self.edit_details_btn.clicked.connect(self._handle_edit_details)

    def _handle_view_details(self):
        view_details = VIEW_DETAILS(
            self.title,
            lambda: self.super_layout.setCurrentWidget(self.grid_widget),
            self.profile,
            self.super_layout,
        )

    def _handle_edit_details(self):
        edit_details = EDIT_DETAILS(
            self.title,
            lambda: self.super_layout.setCurrentWidget(self.grid_widget),
            self.profile,
            self.super_layout,
        )

    def snap(self, image, timer, cam):
        if self.comp.isConnected():
            image_cropped = image[0:480, 80:560]

            cv2.imwrite("./assets/temp/temp.jpg", image_cropped)

            timer.stop()
            cam.release()

            for img in os.listdir("./assets/temp/"):
                file = {"image": open(f"./assets/temp/{img}", "rb").read()}
                r = requests.post(url=f"{self.comp.APP_URL}/recognize/student/", files=file)

                if r.text == "Unknown Individual":
                    self.comp.msg.setIconPixmap(QPixmap("./assets/icons/user_unknown.png"))
                    self.comp.msg.setWindowTitle("Alert!!")
                    self.comp.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
                    self.comp.msg.setText("Unknown Individual!")

                    if self.comp.msg.exec_() or self.comp.msg == QMessageBox.Ok:
                        self.previous()
                elif r.text == "Unable to find face":
                    self.comp.msg.setIconPixmap(QPixmap("./assets/icons/user_unknown.png"))
                    self.comp.msg.setWindowTitle("Alert!!")
                    self.comp.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
                    self.comp.msg.setText("Unable to find face!")

                    if self.comp.msg.exec_() or self.comp.msg == QMessageBox.Ok:
                        self.previous()
                else:
                    profile = r.json()
                    self.MAIN_VIEW(self.previous, profile)

    def _go_back(self, timer, cam):
        timer.stop()
        cam.release()
        self.previous()

