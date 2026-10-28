from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QPixmap
from urllib.request import urlopen
from pathlib import Path
import Fetch_Recs as Movie
import sys

app = QtWidgets.QApplication(sys.argv)
UI = Path(__file__).resolve().parent / "UI.ui"
window = uic.loadUi(UI)

def submit_movie():
    load_media_name()
    if window.checkBox.isChecked():
        DisplayShow()
    else:
        DisplayMovie()

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

def DisplayMovie():
    try:
        title, desc, poster = Movie.RecomendMovie()
        window.label_1.setText(title)
        window.label_2.setText(desc)
        show_poster(poster)
    except Exception as error:
        QtWidgets.QMessageBox.critical(window, "Couldnt find a movie",str(error))

def DisplayShow():
    try:
        title, desc, poster = Movie.RecomendShow()
        window.label_1.setText(title)
        window.label_2.setText(desc)
        show_poster(poster)
    except Exception as error:
        QtWidgets.QMessageBox.critical(window, "Couldnt find a show",str(error))

def PopularMovie():
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
window.popular.clicked.connect(PopularMovie)

window.show()
sys.exit(app.exec())