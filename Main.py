from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
import Fetch_Recs as Movie
from pathlib import Path
import sys

app = QtWidgets.QApplication(sys.argv)
UI = Path(__file__).resolve().parent / "UI.ui"
window = uic.loadUi(UI)

def MovieName():
    return window.input.text().strip

def DisplayMovie():
    movie_name = MovieName()
    title, desc = Movie.RecomendMovie(Movie.s)
    window.label_1.setText(title)
    window.label_2.setText(desc)
   
window.input.returnPressed.connect(DisplayMovie)
window.Search.clicked.connect(DisplayMovie)

window.show()
sys.exit(app.exec())