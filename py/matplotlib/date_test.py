import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import random

import datetime as dt

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)

        self.show()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        dates = mdates.drange(dt.datetime(2010, 1, 1), dt.datetime(2010,1,2),
                      dt.timedelta(minutes=10))
        y_val = [random.random() for i in range(len(dates))]

        ax = self.figure.add_subplot(111)
        ax.plot(dates, y_val)

        use_major_formatter = True
        fmt_str = '%m-%d %H:%M'
        if use_major_formatter:
            ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt_str))
        else:
            ax.fmt_xdata = mdates.DateFormatter(fmt_str)
        self.figure.autofmt_xdate()

        ax.set_title('PyQt Matplotlib Example')
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
