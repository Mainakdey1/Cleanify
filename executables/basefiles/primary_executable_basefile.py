from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QColor, QPalette, QLinearGradient, QBrush, QFont
from PyQt6.QtCore import Qt
import sys
import os
import shutil
from datetime import datetime, timedelta




class WelcomeWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  



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
        """Action when Start button is clicked."""
        print("Start button clicked!")

        self.start_button.setVisible(False)
        self.login_screen = LoginScreen()
        self.login_screen.show()

        self.close()
            








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

        if username == "user" and password == "user":
            dst_cleaner()
            self.clw= closing_window()
            self.clw.show()
            self.close()




        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")





class closing_window(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  



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


        title_label = QLabel("All done!", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)
        layout.addWidget(title_label)


        description_label = QLabel("Your desktop files have been organised into important and junk files.", self)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setStyleSheet("""
            font-size: 14px;
            color: #f5f5f5;
        """)
        layout.addWidget(description_label)

        self.start_button = QPushButton("Close", self)
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
        self.start_button.clicked.connect(self.end_windows)

        layout.addWidget(self.start_button)







    def end_windows():
        sys.exit()







def dst_cleaner():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    #joy's code. zaddy aise hi code karo
    important_extensions = ['.docx', '.pdf', '.xlsx']
    junk_extensions = ['.tmp']
    important_keywords = ['project', 'report']
    junk_keywords = ['temp', 'backup']
    important_age = timedelta(days=30)
    junk_age = timedelta(days=365)


    important_dir = os.path.join(desktop_path, 'Important_Files')
    junk_dir = os.path.join(desktop_path, 'Junk_Files')


    os.makedirs(important_dir, exist_ok=True)
    os.makedirs(junk_dir, exist_ok=True)


    now = datetime.now()


    def is_important(file):
        ext = os.path.splitext(file)[1]
        if ext in important_extensions:
            return True
        if any(keyword in file for keyword in important_keywords):
            return True
        file_path = os.path.join(desktop_path, file)
        if os.path.getmtime(file_path) > (now - important_age).timestamp():
            return True
        return False


    def is_junk(file):
        ext = os.path.splitext(file)[1]
        if ext in junk_extensions:
            return True
        if any(keyword in file for keyword in junk_keywords):
            return True
        file_path = os.path.join(desktop_path, file)
        if os.path.getmtime(file_path) < (now - junk_age).timestamp():
            return True
        return False


    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path):
            if is_important(file):
                try:
                    shutil.move(file_path, important_dir)
                except Exception as e:
                    print(e)
            elif is_junk(file):
                shutil.move(file_path, junk_dir)

    

app = QApplication(sys.argv)
welcome_screen= WelcomeWindow()
welcome_screen.show()
sys.exit(app.exec())




