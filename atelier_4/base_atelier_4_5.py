import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QGridLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        self.label_nb_objects = QLabel("Number of Objects")
        self.textbox_nb_objects = QLineEdit()

        label_min = QLabel("Min")
        label_max = QLabel("Max")

        self.label1 = QLabel("Position X")
        self.textbox1_min = QLineEdit()
        self.textbox1_max = QLineEdit()

        self.label2 = QLabel("Position Y")
        self.textbox2_min = QLineEdit()
        self.textbox2_max = QLineEdit()

        self.label3 = QLabel("Position Z")
        self.textbox3_min = QLineEdit()
        self.textbox3_max = QLineEdit()

        self.label4 = QLabel("Scale")
        self.textbox4_min = QLineEdit()
        self.textbox4_max = QLineEdit()

        row_nb = QHBoxLayout()
        row_nb.addWidget(self.label_nb_objects)
        row_nb.addWidget(self.textbox_nb_objects)

        grid = QGridLayout()

        grid.addWidget(label_min, 0, 1)
        grid.addWidget(label_max, 0, 2)

        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.textbox1_min, 1, 1)
        grid.addWidget(self.textbox1_max, 1, 2)

        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.textbox2_min, 2, 1)
        grid.addWidget(self.textbox2_max, 2, 2)

        grid.addWidget(self.label3, 3, 0)
        grid.addWidget(self.textbox3_min, 3, 1)
        grid.addWidget(self.textbox3_max, 3, 2)

        grid.addWidget(self.label4, 4, 0)
        grid.addWidget(self.textbox4_min, 4, 1)
        grid.addWidget(self.textbox4_max, 4, 2)


        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addLayout(row_nb)
        layout.addLayout(grid)
        layout.addWidget(self.create_button)

    def create_object(self):
        
        nb_objets = int(self.textbox_nb_objects.text())

        

        for i in range(nb_objets):
            forme = random.choice(["cube", "cylindre", "sphere"])
            if forme == "cube":
                objet = cmds.polyCube()[0]
                cmds.scale(scale,scale,scale, objet)
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
                cmds.scale(scale,scale,scale, objet)
            else:
                objet = cmds.polySphere()[0]
                cmds.scale(scale,scale,scale, objet)

            random_value = random.uniform(-10, 10)
            move_x = random.uniform(int(self.textbox1_min.text()), int(self.textbox1_max.text()))
            move_y = random.uniform(int(self.textbox2_min.text()), int(self.textbox2_max.text()))
            move_z = random.uniform(int(self.textbox3_min.text()), int(self.textbox3_max.text()))

            scale =  random.uniform(int(self.textbox4_min.text()), int(self.textbox4_max.text()))

            cmds.move(move_x, move_y, move_z, objet)
        

        


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()