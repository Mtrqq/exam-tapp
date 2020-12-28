import sys

from PySide2.QtWidgets import QApplication
from qt_material import apply_stylesheet

from tapp.calculator import TriangleAreaCalculator


def run():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Triangle calculator app")
    app.setApplicationName("ExamApp")
    apply_stylesheet(app, theme="dark_amber.xml")

    widget = TriangleAreaCalculator()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
