import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox, QSpinBox
from PyQt5.QtGui import QFont
import random
import string
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(700, 300, 900, 900)

        
        # Create checkboxes and length selector
        self.create_checkboxes()
        self.create_length_selector()
        
        #Prompt for the end-user
        self.label = QLabel("Choose the type of signs to include in your password", self)
        self.label.setFont(QFont("Times New Roman", 20))
        self.label.setGeometry(100,100,750,50)
        self.label.setStyleSheet("color: green;"
                            "background-color: white;"
                            "font-weight: bold;"
                            )
        self.label.setAlignment(Qt.AlignTop)
        
        
        #Dispay of password in window
        self.password_display = QLabel(self)
        self.password_display.setGeometry(100, 450, 1000, 40)
        self.password_display.setStyleSheet("font-size: 18px; color: red;")
        self.password_display.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.password_display.setText("Your password will appear here")
        self.password_display.setTextInteractionFlags(Qt.TextSelectableByMouse)


        # Create the button to generate the password
        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.setGeometry(100, 400, 200, 40)
        self.generate_button.clicked.connect(self.generate_password)

    def create_checkboxes(self):
        # Checkbox 1
        self.checkbox1 = QCheckBox("Include Uppercase?", self)
        self.checkbox1.setGeometry(50, 150, 150, 40)  # Set position and size
        
        # Checkbox 2
        self.checkbox2 = QCheckBox("Include Lowercase?", self)
        self.checkbox2.setGeometry(50, 200, 150, 40)
        
        # Checkbox 3
        self.checkbox3 = QCheckBox("Include Digits?", self)
        self.checkbox3.setGeometry(50, 250, 150, 40)
        
        # Checkbox 4
        self.checkbox4 = QCheckBox("Include Symbols?", self)
        self.checkbox4.setGeometry(50, 300, 150, 40)
    
    def create_length_selector(self):
        # Create QSpinBox for selecting password length
        self.length_selector = QSpinBox(self)
        self.length_selector.setGeometry(50, 350, 150, 40)
        self.length_selector.setMinimum(8)  # Minimum password length
        self.length_selector.setMaximum(100)  # Maximum password length
        self.length_selector.setValue(12)  # Default value
        self.length_selector.setPrefix("Length: ")

    def generate_password(self):
        # Create the character pool based on checkbox selections
        password_list = []
        if self.checkbox1.isChecked():
            password_list.extend(string.ascii_uppercase)
        if self.checkbox2.isChecked():
            password_list.extend(string.ascii_lowercase)
        if self.checkbox3.isChecked():
            password_list.extend(string.digits)
        if self.checkbox4.isChecked():
            password_list.extend(string.punctuation)
        
        # Ensure at least one option is selected
        if not password_list:
            self.password_display.setText("Error: Please select at least one option")
            return
        # Get the selected password length
        password_length = self.length_selector.value()

        # Generate a password of the selected length
        password = ''.join(random.choice(password_list) for _ in range(password_length))
        
        # Print the generated password
        self.password_display.setText(f"Generated Password: {password}")
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Create an instance of MainWindow
    window.show()
    sys.exit(app.exec_())  # Start the application loop


if __name__ == "__main__":
    main()