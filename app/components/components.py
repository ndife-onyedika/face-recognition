import cv2
import requests
from PyQt5.QtCore import QSize, QDate, Qt, QTimer
from PyQt5.QtGui import QIcon, QIntValidator, QImage, QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QGroupBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QRadioButton,
    QComboBox,
    QCalendarWidget,
    QVBoxLayout,
    QCommandLinkButton,
    QMessageBox
)

class COMPONENTS(QWidget):
    def __init__(self):
        super().__init__()
        self.APP_URL = "http://127.0.0.1:8000"
        # self.APP_URL = "https://face-recog-server.herokuapp.com"
        self.msg = QMessageBox()

        self.grid = QGridLayout()
        self.group_box = QGroupBox()

        # PROFILE PICTURE
        self.profile_pic = QLabel()
        self.profile_pic.setAlignment(Qt.AlignCenter)
        self.profile_pic.setMaximumSize(130, 130)
        self.profile_pic.setScaledContents(True)

        # PROFILE PICTURE LAYOUT
        self.pro_pic_view = QVBoxLayout()
        self.change_pro = QPushButton()
        self.change_pro.setIcon(QIcon("./assets/icons/capture.png"))

        self.pro_pic_view.addWidget(self.profile_pic)
        self.pro_pic_view.addWidget(self.change_pro)

        self.cam_btn = QPushButton("Capture")


        # FIRST NAME
        self.f_name = QLabel("First Name")
        self.f_name.setObjectName("Label")
        self.f_name_input = QLineEdit()

        # MIDDLE NAME
        self.m_name = QLabel("Middle Name")
        self.m_name.setObjectName("Label")
        self.m_name_input = QLineEdit()

        # LAST NAME
        self.l_name = QLabel("Last Name")
        self.l_name.setObjectName("Label")
        self.l_name_input = QLineEdit()

        # DATE OF BIRTH
        self.dob_label = QLabel("Date of Birth")
        self.dob_label.setObjectName("Label")
        self.dob_date_label = QLabel("Choose Date..")
        self.dob_date_label.setStyleSheet("font-weight: normal;")
        self.dob_date_choose = QPushButton()
        self.dob_date_choose.setIcon(QIcon("./assets/icons/calendar.png"))
        self.dob_date_choose.setIconSize(QSize(25, 25))
        self.dob_layout = QHBoxLayout()
        self.dob_date_choose.clicked.connect(self.calender_show)
        self.dob_layout.addWidget(self.dob_date_label)
        self.dob_layout.addWidget(self.dob_date_choose)

        # AGE
        self.age = QLabel("Age")
        self.age.setObjectName("Label")
        self.age_input = QLineEdit()
        self.age_input.setValidator(QIntValidator())
        self.age_input.setMaxLength(3)

        # GENDER
        self.gender = QLabel("Gender")
        self.gender.setObjectName("Label")
        self.gender_1 = QRadioButton("MALE")
        self.gender_2 = QRadioButton("FEMALE")
        self.gender_1.setChecked(True)
        self.gender_layout = QHBoxLayout()
        self.gender_layout.addWidget(self.gender_1)
        self.gender_layout.addWidget(self.gender_2)

        # NATIONAILTY
        self.nationality = QLabel("Nationality")
        self.nationality.setObjectName("Label")
        self.nationality_input = QLineEdit()

        # STATE OF ORIGIN
        self.state_origin = QLabel("State of Origin")
        self.state_origin.setObjectName("Label")
        self.state_origin_input = QLineEdit()

        # LGA OF ORIGIN
        self.lga_origin = QLabel("LGA")
        self.lga_origin.setObjectName("Label")
        self.lga_origin_input = QLineEdit()

        # MARITAL STATUS
        self.marital = QLabel("Marital Status")
        self.marital.setObjectName("Label")
        self.marital_select = QComboBox()
        self.marital_select.addItems(
            ["SINGLE", "SEPERATED", "DIVORCED", "MARRIED", "WIDOWED"]
        )

        self.profession = QLabel("Profession")
        self.profession.setObjectName("Label")
        self.profession_input = QLineEdit()

        # JAMB NUMBER
        self.j_num = QLabel("JAMB No.")
        self.j_num.setObjectName("Label")
        self.j_num_input = QLineEdit()
        self.j_num_input.setMaxLength(10)

        # COLLEGE
        self.college = QLabel("College")
        self.college.setObjectName("Label")
        self.college_select = QComboBox()
        self.college_select.addItems(
            [
                "CAERSE",
                "CASAP",
                "CAFST",
                "CCSS",
                "COED",
                "CEET",
                "CGSC",
                "COLMAS",
                "CNREM",
                "COLNAS",
                "COLPAS",
                "CVM",
            ]
        )

        # DEPARTMENT
        self.dept = QLabel("Department")
        self.dept.setObjectName("Label")
        self.dept_select = QComboBox()
        self.dept_select.addItems(
            [
                "AGRIBUSINESS MANAGEMENT",
                "AGRICULTURAL ECONOMICS",
                "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
            ]
        )

        # LEVEL
        self.level = QLabel("Level")
        self.level.setObjectName("Label")
        self.level_select = QComboBox()
        self.level_select.addItems(["100L", "200L", "300L", "400L"])

        # MATRIC NUMBER
        self.m_num = QLabel("Matriculation No.")
        self.m_num.setObjectName("Label")
        self.m_num_input = QLineEdit()

        # HOME ADDRESS
        self.address = QLabel("Home Address")
        self.address.setObjectName("Label")
        self.address_input = QLineEdit()

        # CELL PHONE
        self.phone = QLabel("Cell Phone")
        self.phone.setObjectName("Label")
        self.phone_input = QLineEdit()
        # self.phone_input.setValidator(QIntValidator
        self.phone_input.setMaxLength(11)

        # EMAIL
        self.email = QLabel("Email")
        self.email.setObjectName("Label")
        self.email.setObjectName("Label")
        self.email_input = QLineEdit()

        # PARENT NAME
        self.p_name = QLabel("Parent's/Sponsor's Name")
        self.p_name.setObjectName("Label")
        self.p_name_input = QLineEdit()

        # PARENT EMAIL
        self.p_email = QLabel("Parent's/Sponsor's Email")
        self.p_email.setObjectName("Label")
        self.p_email_input = QLineEdit()

        # PARENT PHONE
        self.p_phone = QLabel("Parent's/Sponsor's Phone")
        self.p_phone.setObjectName("Label")
        self.p_phone_input = QLineEdit()
        self.p_phone_input.setMaxLength(11)

        # DATE OF REGISTRATION
        self.dor = QLabel("Date of Registration")
        self.dor.setObjectName("Label")
        self.dor_text = QLineEdit()
        date = QDate.currentDate().toString(Qt.ISODate)
        self.dor_text.setText(date)

        # Next
        self._next = QPushButton("Next")

        # Prev
        self._prev = QPushButton("Previous")

    def calender_show(self):

        self.initial_layout = QVBoxLayout()

        self.calender_view = QWidget()
        self.calender_view.setWindowTitle("Choose Date")

        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)

        self.flags = Qt.WindowFlags(Qt.WindowStaysOnTopHint)
        self.calender_view.setWindowFlags(self.flags)

        self.initial_layout.addWidget(self.calender)
        self.calender_view.setLayout(self.initial_layout)

        self.calender_view.show()
        self.calender_view.resize(350, 250)

        self.calender.clicked[QDate].connect(self.select_date)

    def select_date(self):
        self.dob_date_label.setText(self.calender.selectedDate().toString(Qt.ISODate))
        self.calender_view.hide()

    def _start_video(self, super_layout):
        self.video_widget = QWidget()
        self.video_init_layout = QVBoxLayout()

        self.back_btn = QCommandLinkButton()
        self.back_btn.setIcon(QIcon("./assets/icons/back.png"))
        self.back_btn.setIconSize(QSize(30, 30))
        self.back_btn.setMaximumWidth(45)

        # Create Camera View
        self.cam_view = QLabel()

        self.video_init_layout.addWidget(self.back_btn)
        self.video_init_layout.addWidget(self.cam_view)
        self.video_init_layout.addWidget(self.cam_btn)

        self.video_widget.setLayout(self.video_init_layout)

        super_layout.addWidget(self.video_widget)
        super_layout.setCurrentWidget(self.video_widget)

        # create a timer
        self.timer = QTimer()

        # set timer timeout callback function
        self.timer.timeout.connect(self._video)

        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(1)

    def _video(self):
        face_cascade = cv2.CascadeClassifier(
            "./assets/classifier/haarcascade_frontalface_alt2.xml"
        )

        ret, self.image = self.cam.read()

        image_copy = self.image.copy()

        # Capture Image-by-Image
        gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 1)

        self.image_shown = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

        # get image infos
        self.height, self.width, self.channel = self.image_shown.shape
        self.step = self.channel * self.width

        # create QImage from image
        self.qImg = QImage(
            self.image_shown.data,
            self.width,
            self.height,
            self.step,
            QImage.Format_RGB888,
        )

        # Set the data from qImg to cam_view
        self.cam_view.setPixmap(QPixmap.fromImage(self.qImg))

    def isConnected(self):
        try:
            r = requests.get(url=f"{self.APP_URL}")
            print(r.text)
            return True
        except requests.exceptions.ConnectionError as e:
            self.msg.setIconPixmap(QPixmap("./assets/icons/no_connection.png"))
            self.msg.setWindowTitle("Error!")
            self.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
            self.msg.setText("Connect to the Internet to use app!")
            self.msg.show()
            self.msg.exec_()
            return False
        except requests.exceptions.Timeout as e:
            self.msg.setIconPixmap(QPixmap("./assets/icons/network_timeout.png"))
            self.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
            self.msg.setWindowTitle("Information")
            self.msg.setWindowIcon(QIcon("./assets/icons/error.png"))
            self.msg.setText("Poor Network Connection!")
            self.msg.show()
            self.msg.exec_()
            return False
