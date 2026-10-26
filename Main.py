from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtGui import QPixmap
from urllib.request import urlopen
import Fetch_Recs as Movie
from pathlib import Path
import sys

app = QtWidgets.QApplication(sys.argv)
UI = Path(__file__).resolve().parent / "UI.ui"
window = uic.loadUi(UI)

def submit_movie():
    load_movie_name()
    DisplayMovie()

def MovieName():
    return window.input.text()

def load_movie_name():
    movie_name = MovieName()
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
def PopularMovie():
    try:
        title, desc, poster = Movie.PopularMovie()
        window.label_1.setText(title)
        window.label_2.setText(desc)
        show_poster(poster)
    except Exception as error:
        QtWidgets.QMessageBox.critical(window, "Couldnt find a movie",str(error))
   
window.input.returnPressed.connect(submit_movie)
window.Search.clicked.connect(submit_movie)
window.popular.clicked.connect(PopularMovie)

window.show()
sys.exit(app.exec())