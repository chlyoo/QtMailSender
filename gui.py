import sys
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

def main():
    app = QApplication(sys.argv)

    ui_file = QFile("MainWindow.ui")
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()
    ui_file.close()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()