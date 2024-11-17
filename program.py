import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import QTimer, Qt

class CronometruApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer - mihai288")
        self.setGeometry(200, 200, 400, 800)
        self.setStyleSheet("background-color: #2c3e50;")

        self.secunde = 0
        self.minute = 0
        self.ore = 0
        self.startstop = True
        self.tur_count = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.time_label = QLabel("0:00:00", self)
        self.time_label.setStyleSheet("color: #ecf0f1; font-size: 30px;")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.time_label)

        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.start_button.clicked.connect(self.start_cronometru)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.stop_button.clicked.connect(self.stop_cronometru)
        self.layout.addWidget(self.stop_button)

        self.lap_button = QPushButton("Tur")
        self.lap_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.lap_button.clicked.connect(self.tur_cronometru)
        self.layout.addWidget(self.lap_button)

        self.laps_frame = QFrame(self)
        self.laps_layout = QVBoxLayout()
        self.laps_frame.setLayout(self.laps_layout)
        self.layout.addWidget(self.laps_frame)

    def start_cronometru(self):
        if not self.timer.isActive():
            self.timer.start(1000)

    def stop_cronometru(self):
        if self.timer.isActive():
            self.timer.stop()

    def update_timer(self):
        if self.startstop:
            self.secunde += 1
            if self.secunde == 60:
                self.minute += 1
                self.secunde = 0
            if self.minute == 60:
                self.ore += 1
                self.minute = 0

            time_str = f"{self.ore}:{self.minute:02}:{self.secunde:02}"
            self.time_label.setText(time_str)

    def tur_cronometru(self):
        time_str = self.time_label.text()
        lap_label = QLabel(f"{time_str} | Tur {self.tur_count}")
        lap_label.setStyleSheet("color: #ecf0f1; font-size: 14px;")
        self.laps_layout.addWidget(lap_label)
        self.tur_count += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cronometru_app = CronometruApp()
    cronometru_app.show()
    sys.exit(app.exec())
