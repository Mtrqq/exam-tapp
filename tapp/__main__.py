import sys

from PySide2.QtWidgets import QApplication, QTabWidget
from qt_material import apply_stylesheet

from tapp.calculators import TriangleAreaCalculator, SegmentLengthCalculator


def run():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Triangle calculator app")
    app.setApplicationName("ExamApp")
    apply_stylesheet(app, theme="dark_amber.xml")

    widget = QTabWidget()
    triangle_tab = TriangleAreaCalculator(widget)
    segment_tab = SegmentLengthCalculator(widget)
    widget.addTab(triangle_tab, "Triangle")
    widget.addTab(segment_tab, "Segment")

    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
