from typing import List, Optional, Tuple
import traceback

import PySide2.QtWidgets as widgets
from PySide2.QtCore import Slot

from tapp.geometry.segment import Segment
from tapp.geometry.vector import Vector2D

CoordinateSelector = widgets.QDoubleSpinBox
PointSelector = Tuple[CoordinateSelector, CoordinateSelector]


def _get_point(selector: PointSelector) -> Vector2D:
    coords = (coord.value() for coord in selector)
    return Vector2D(*coords)


class SegmentLengthCalculator(widgets.QWidget):
    def __init__(self, parent: Optional[widgets.QWidget] = None) -> None:
        super().__init__(parent=parent)

        self.point_selectors: List[PointSelector] = []
        self.recalculate_button: Optional[widgets.QPushButton] = None

        self.init_ui()

    def init_ui(self) -> None:
        vbox_layout = widgets.QVBoxLayout()
        for i in range(2):
            hbox_layout = widgets.QHBoxLayout()
            label = widgets.QLabel(f"Enter {i} vertex of segment:")
            x_selector = widgets.QDoubleSpinBox()
            y_selector = widgets.QDoubleSpinBox()
            hbox_layout.addWidget(label)
            hbox_layout.addWidget(x_selector)
            hbox_layout.addWidget(y_selector)
            vbox_layout.addLayout(hbox_layout)
            self.point_selectors.append((x_selector, y_selector))

        self.recalculate_button = widgets.QPushButton("Recalculate")
        self.recalculate_button.clicked.connect(self.recalculate)
        vbox_layout.addWidget(self.recalculate_button)

        self.setLayout(vbox_layout)

    @Slot()
    def recalculate(self) -> None:
        points = (_get_point(selector) for selector in self.point_selectors)
        try:
            segment = Segment(*points)
        except ValueError as error:
            traceback.print_exc()
            widgets.QMessageBox.critical(None, "Error", "Segment has invalid vertices")
        except Exception as error:
            traceback.print_exc()
            widgets.QMessageBox.critical(None, "Error", "Unexpected error")
        else:
            widgets.QMessageBox.information(
                None, "Information", f"Segment length = {segment.length}"
            )
