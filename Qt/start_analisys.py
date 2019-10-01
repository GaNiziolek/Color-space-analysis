from PyQt5.QtWidgets import QApplication

from windows import StartWindow

app = QApplication([])
star_window = StartWindow()
star_window.show()
app.exit(app.exec_())