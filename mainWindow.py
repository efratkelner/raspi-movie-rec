import sys
try:
    from pyqt5_plugins.examplebuttonplugin import QtGui

    from main import movie_recommendations
    from PyQt5.QtWidgets import QMainWindow, QApplication

    from ui_default import Ui_DefaultWindow
    from ui_image import Ui_Image
    from ui_mainWindow import Ui_MainWindow
    from ui_movies_window import Ui_Dialog
    import recognize_age_gender

except ImportError as e:
    print(f"Installation error: {e}")
    raise


class DefaultWindow(QMainWindow):
    def __init__(self):
        super(DefaultWindow, self).__init__()
        self.ui = Ui_DefaultWindow()
        self.dialog = None
        self.ui.setup_ui(self)

    def on_push_button_click(self):
        self.close()
        self.dialog = MainWindow()
        self.dialog.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.dialog = None
        self.ui.setup_ui(self)

    def on_push_button_click(self):
        age = None
        while not age:
            image = recognize_age_gender.take_a_picture()
            age, gender, frame_face_path = recognize_age_gender.get_data_from_face(image)
        image = QtGui.QImage()
        image.loadFromData(frame_face)
        pixmap1 = QtGui.QPixmap(image)
        label.setPixmap(pixmap1.scaled(611, 431))
        movies_list = movie_recommendations(age, gender)
        self.close()
        self.dialog = ImageWindow(frame_face_path, age, gender)
        self.dialog.show()


class ImageWindow(QMainWindow):
    def __init__(self, frame_face_path, age, gender):
        super(ImageWindow, self).__init__()
        self.ui = Ui_Image()
        self.image = frame_face_path
        self.dialog = None
        self.ui.setup_ui(self)
        self.dnext(age, gender)

    def dnext(self,age, gender):
        movies_list = movie_recommendations(age, gender)
        self.close()
        self.dialog = MovieWindow(movies_list)
        self.dialog.show()


class MovieWindow(QMainWindow):
    def __init__(self, movies_list):
        super(MovieWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.dialog = None
        self.movies = movies_list
        self.ui.setup_ui(self)


    def on_push_button_click(self):
        self.close()
        self.dialog = DefaultWindow()
        self.dialog.show()

    def get_movies(self):
        return self.movies


def apply_default_window():
    app = QApplication(sys.argv)
    window = DefaultWindow()
    window.show()
    sys.exit(app.exec_())


apply_default_window()
