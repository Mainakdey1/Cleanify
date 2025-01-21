from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QColor, QPalette, QLinearGradient, QBrush, QFont
from PyQt6.QtCore import Qt
import sys



class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Screen")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(400, 400)
        self.set_gradient_background()
        self.old_pos = None


        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        layout = QVBoxLayout()


        self.title_label = QLabel("Welcome to the Loginator")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("""
            color: #ffffff;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        """)


        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("color: #ffffff;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setStyleSheet("""
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)


        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: #ffffff;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("""
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)


        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #661730;
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
        self.login_button.clicked.connect(self.check_credentials)
        self.register_button = QPushButton("New to the loginator?")
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #661730;
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
        self.resetpw_button = QPushButton("Forgot your password?")
        self.resetpw_button.setStyleSheet("""
            QPushButton {
                background-color: #661730;
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


        layout.addWidget(self.title_label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addStretch()
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.resetpw_button)


        central_widget.setLayout(layout)

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

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome, admin!")
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")


