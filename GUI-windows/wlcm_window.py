
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
from PyQt6.QtGui import QPixmap, QColor, QPalette, QLinearGradient, QBrush
from PyQt6.QtCore import Qt, QTimer
import sys



class WelcomeWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # Removes the title bar



        self.old_pos = None
        self.setMouseTracking(True)


        self.setWindowTitle("Welcome")
        self.setFixedSize(600, 400)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


        self.set_gradient_background()


        self.setup_ui()



    


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def set_gradient_background(self):
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#1a1a2e"))
        gradient.setColorAt(1.0, QColor("#e94560"))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

    def setup_ui(self):
        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        title_label = QLabel("Desktop organizer", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)
        layout.addWidget(title_label)


        description_label = QLabel("Your little helper. Let’s get started!", self)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setStyleSheet("""
            font-size: 14px;
            color: #f5f5f5;
        """)
        layout.addWidget(description_label)


        self.start_button = QPushButton("Start", self)
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #e94560;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #0f3460;
            }
        """)
        self.start_button.clicked.connect(self.on_start_clicked)

        layout.addWidget(self.start_button)

    def on_start_clicked(self):
        print("Start button clicked!")


        self.start_button.setVisible(False)
        window.close()


    






app = QApplication(sys.argv)
window = WelcomeWindow()

window.show()
app.exec()


