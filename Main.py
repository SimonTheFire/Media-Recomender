from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
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

def DisplayMovie():
    title, desc = Movie.RecomendMovie()
    window.label_1.setText(title)
    window.label_2.setText(desc)
   
window.input.returnPressed.connect(submit_movie)
window.Search.clicked.connect(submit_movie)

window.show()
sys.exit(app.exec())