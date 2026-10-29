from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtGui import QPixmap
from urllib.request import urlopen
from pathlib import Path
import Fetch_Recs as Movie
import sys
UI = Path(__file__).resolve().parent / "UI.ui"
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(UI)
checker = None
def submit_movie():
    load_media_name()
    Display()

def Name():
    return window.input.text()

def load_media_name():
    if window.checkBox.isChecked():
        show_name = Name()
        Movie.ShowTitle(show_name)
    else:
        movie_name = Name()
        Movie.MovieTitle(movie_name)

def show_poster(poster):
    image_data = urlopen(poster).read()
    pixmap = QPixmap()
    pixmap.loadFromData(image_data)
    
    scene = QtWidgets.QGraphicsScene(window)
    scene.addPixmap(pixmap)
    window.graphicsView.setEnabled(True)
    window.graphicsView.setScene(scene)
    window.graphicsView.fitInView(
        scene.sceneRect(),
        QtCore.Qt.AspectRatioMode.KeepAspectRatio
    )

def Display():
    try:
        if window.checkBox.isChecked():
            title, desc, poster = Movie.RecomendShow()
        else:
            title, desc, poster = Movie.RecomendMovie()
        window.label_1.setText(title)
        window.label_2.setText(desc)
        show_poster(poster)
    except Exception as error:
        QtWidgets.QMessageBox.critical(window, "Couldnt find a anything",str(error))

def Popular():
    try:
        if window.checkBox.isChecked():
            title, desc, poster = Movie.PopularShow()
        else:
            title, desc, poster = Movie.PopularMovie()
        window.label_1.setText(title)
        window.label_2.setText(desc)
        show_poster(poster)
    except Exception as error:
        QtWidgets.QMessageBox.critical(window, "Couldnt find anything thats popular",str(error))

window.input.returnPressed.connect(submit_movie)
window.Search.clicked.connect(submit_movie)
window.popular.clicked.connect(Popular)

window.show()
sys.exit(app.exec())