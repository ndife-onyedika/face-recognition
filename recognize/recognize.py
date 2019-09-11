import cv2

from database import db


class RECOGNIZE:
    datab = db.Database()

    def __init__(self):
        super().__init__()

        self.faceDetect = cv2.CascadeClassifier(
            "./assets/classifiers/haarcascade_frontalface_alt2.xml"
        )
        self.cam = cv2.VideoCapture(0)

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.datab.cur.execute("SELECT * FROM Students")

        name_lst = list()

        for row in self.datab.cur:
            name = f"{row[3]}_{row[1]}".lower()
            name_lst.append(name)

    def verify(self):
        def getProfile():
            profile = None
            self.datab.cur.execute("SELECT * FROM Students")
            for row in self.datab.cur:
                profile = row
            return profile

        for name in name_lst:
            self.recognizer.read(f"./assets/training_data/{name}-training_data.yml")

        Id = 0
        while True:
            ret, image = self.cam.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.faceDetect.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
                Id, conf = self.recognizer.predict(gray[y : y + h, x : x + w])
                profile = getProfile()
                # print()
                if profile != None:
                    if profile[0] == Id:
                        cv2.putText(
                            image,
                            f"Name: {profile[3]} {profile[2]} {profile[1]}",
                            (x, y + h + 20),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1,
                            (255, 255, 255),
                        )
            cv2.imshow("Face", image)
            if cv2.waitKey(1) == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()
