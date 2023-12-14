"""
ЗАДАЧА:
1.	Создайте класс для лиц, с фото и видео.
a.	В классе должны быть следующие методы:
i.	Метод предобработки фото, видео (путь получаем при инициализации) - метод загружает фото, или видео
ii.	Метод детекта
iii.	Метод инференса
iv.	Метод отображения
b.	Также сделайте возможность изменять размеры отображаемого фото, видео, при вызове метода.
"""

import cv2 as cv
class oneFrame:
    def __init__(self, frame):
        self.frame = frame

    def store_faces(self, faces):
        self.faces = faces

class Face:
    def __init__(self, path: str, is_photo: bool):
       self.frames = []
       self.is_photo = is_photo
       self.path=path

    #ресайз
    @staticmethod
    def resizing(img_res, new_width = None, new_height = None):
        h, w = img_res.shape[:2]
        if new_width is None and new_height is None:
            return img_res

        if new_width is None:
            ratio = new_height / h
            dimension = (int(w * ratio), new_height)

        else:
            ratio = new_width / w
            dimension = (new_width, int (h * ratio))

        return cv.resize(img_res, dimension)


    #предобработка
    def prepare(self, new_width = None, new_height = None):
        if self.is_photo:
            self.img = cv.imread(self.path)
            if new_width or new_height:
                self.img = self.resizing(self.img, new_width, new_height)
            frame = oneFrame(self.img)
            self.frames.append(frame)

        else:
            cap = cv.VideoCapture(self.path)
            while cap.isOpened():
                read, frame_temp = cap.read()
                if not read:
                    print("Ошибка получения видео")
                    break
                if new_width or new_height:
                    frame_temp = self.resizing(frame_temp, new_width, new_height)
                frame = oneFrame(frame_temp)
                self.frames.append(frame)

#детект
    def detect_frame(self, new_width = None, new_height = None):
        for i in self.frames:
            if new_width or new_height:
                i.frame = self.resizing(i.frame, new_width, new_height)
            face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
            frame_gray = cv.cvtColor(i.frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)
            i.store_faces(face_cascade.detectMultiScale(frame_gray))


#инференс
    def inference(self, new_width = None, new_height = None):
        for i in self.frames:
            for (x,y,w,h) in i.faces:
                center = (x + w//2, y + h//2)
                i.frame = cv.ellipse(i.frame, center, (w//2,h//2), 0, 0, 360, (255, 0, 255), 4)
            if new_width or new_height:
                i.frame = self.resizing(i.frame, new_width, new_height)

#отображение
    def show(self, new_width = None, new_height = None):
        for i in self.frames:
            if new_width or new_height:
                i.frame = self.resizing(i.frame, new_width, new_height)
            cv.imshow('123', i.frame)
            if self.is_photo:
                cv.waitKey(0)
            else:
                if cv.waitKey(1) == ord('q'):
                    break


#pic = Face('video_1.mp4', False)
pic = Face('img.jpg', True)
pic.prepare(600)
pic.detect_frame(1500)
pic.inference(600)
pic.show()


