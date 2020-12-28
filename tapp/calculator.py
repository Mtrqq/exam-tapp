from typing import List, Optional

import PySide2.QtWidgets as widgets
from PySide2.QtCore import Slot

from tapp.triangle import Triangle


class TriangleAreaCalculator(widgets.QWidget):
    def __init__(self) -> None:
        super().__init__(parent=None)

        self.side_selectors: List[widgets.QDoubleSpinBox] = []
        self.recalculate_button: Optional[widgets.QPushButton] = None

        self.init_ui()

    def init_ui(self) -> None:
        vbox_layout = widgets.QVBoxLayout()
        for i in range(3):
            hbox_layout = widgets.QHBoxLayout()
            label = widgets.QLabel(f"Enter {i} side of triangle:")
            side_selection = widgets.QDoubleSpinBox()
            hbox_layout.addWidget(label)
            hbox_layout.addWidget(side_selection)
            vbox_layout.addLayout(hbox_layout)
            self.side_selectors.append(side_selection)

        self.recalculate_button = widgets.QPushButton("Recalculate")
        self.recalculate_button.clicked.connect(self.recalculate)
        vbox_layout.addWidget(self.recalculate_button)

        self.setLayout(vbox_layout)

    @Slot()
    def recalculate(self) -> None:
        values = (selector.value() for selector in self.side_selectors)
        try:
            triangle = Triangle(*values)
        except ValueError:
            widgets.QMessageBox.critical(None, "Error", "Triangle has invalid sides")
        except Exception:
            widgets.QMessageBox.critical(None, "Error", "Unexpected error")
        else:
            widgets.QMessageBox.information(
                None, "Information", f"Triangle area = {triangle.area}"
            )
