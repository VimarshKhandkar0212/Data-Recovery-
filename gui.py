from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout
import scanner
import recovery

class RecoveryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Data Recovery System")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        
        self.label = QLabel("Select Drive to Scan", self)
        layout.addWidget(self.label)

        self.button_scan = QPushButton("Scan Drive", self)
        self.button_scan.clicked.connect(self.browse)
        layout.addWidget(self.button_scan)

        self.button_recover = QPushButton("Recover File", self)
        self.button_recover.clicked.connect(self.recover)
        layout.addWidget(self.button_recover)

        self.setLayout(layout)

    def browse(self):
        drive = QFileDialog.getExistingDirectory(self, "Select Drive")
        self.label.setText(f"Scanning: {drive}")
        scanner.scan_directory(drive)

    def recover(self):
        source, _ = QFileDialog.getOpenFileName(self, "Select File to Recover")
        destination = QFileDialog.getExistingDirectory(self, "Select Recovery Destination")
        recovery.recover_file(source, destination)

app = QApplication([])
window = RecoveryApp()
window.show()
app.exec_()
