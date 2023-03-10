# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from time import *
from PyQt5.QtMultimedia import *
import sys, os

# class mainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
     
        # setting window title 
        self.setWindowTitle("Alarm")

        # setting window size
        self.setFixedSize(603,350)

        # setting window icon
        self.setWindowIcon(QIcon("alarm_clock"))

        # call style window methods
        self.style_Mwindow()

        # displying window
        self.show()
        
 # style of window
    def style_Mwindow(self):

        # add label To clarify what the program is
        Text = QLabel(" ALARM CLOCK", self)
        Text.setGeometry(220,20,180,30)
        Text.setStyleSheet("font-size:25px;")

        # add Qlabel to indicate input format
        LAbel = QLabel("Set Time for Alarm :",self)
        LAbel.setGeometry(30,100,225,30)
        LAbel.setStyleSheet("font-size:25px;")

        # add QLineEdit to input number of hour
        self.Hour = QLineEdit(self)
        self.Hour.setGeometry(280,105,81,30)
        self.Hour.setPlaceholderText("    Hour")
        self.Hour.setStyleSheet("border-radius:8px;font-size:16px;")
        self.Hour.setToolTip("Remembr To Set Time In 24-Hour Format!!")

        # add QLineEdit to input number of minute
        self.Minute = QLineEdit(self)
        self.Minute.setGeometry(390,105,81,30)
        self.Minute.setPlaceholderText("   Minute")
        self.Minute.setStyleSheet("border-radius:8px;font-size:16px;")

        # add QLineEdit to input number of second
        self.Second = QLineEdit(self)
        self.Second.setGeometry(500,105,81,30)
        self.Second.setPlaceholderText("  Second")
        self.Second.setStyleSheet("border-radius:8px;font-size:16px;")

        # add QLineEdit to input message that you want to see
        self.Message = QLineEdit(self)
        self.Message.setGeometry(280,175,305,40)
        self.Message.setPlaceholderText(" Type your Message here !")
        self.Message.setStyleSheet("border-radius:8px;font-size:16px;")

        # add Qlabel to indicate input format
        LAbelMessage = QLabel("Set Your Message :",self)
        LAbelMessage.setGeometry(30,180,210,30)
        LAbelMessage.setStyleSheet("font-size:25px;")

        # add Qbutton Start countdown to run alarm
        self.ButtonStart = QPushButton("Start Alarm",self)
        self.ButtonStart.setGeometry(245,260,130,30)
        self.ButtonStart.setStyleSheet("border-radius:8px;font-size:20px;bacKground:#344D67;color:white;")
        self.ButtonStart.clicked.connect(self.Show_Total_Hours_Before_Alarm_Start)

    # add get time function to get time using datetime librariey
    def Get_Time(self):
        self.Now = datetime.now()
        self.Time = self.Now.strftime("%H:%M:%S")
        self.CurrentTime = self.Time.split(":")

    # add get hour time,minute time to get total number of hour,minute
    def Get_HourTime_SecondTime(self):
        self.Get_Time() # call get time function to use attribute
        self.HourTime = (int(self.Hour.text()) - (int(self.CurrentTime[0]))) * 60
        self.MinuteTime = int(self.Minute.text()) - int(self.CurrentTime[1])
        self.SecondTime = int(self.Second.text()) - int(self.CurrentTime[-1])

        # calcledd total hour and minute
        self.TotalTime = self.HourTime  + self.MinuteTime
        self.NumberHour = self.TotalTime // 60
        self.NumberMinute = self.TotalTime % 60

    # add function Show Total Hours Before Alarm Start to show total hour,minute Before Alarm Start
    def Show_Total_Hours_Before_Alarm_Start(self):
        self.Get_HourTime_SecondTime() # call Get HourTime SecondTime function to use attribute
        if self.NumberHour > 0 and self.NumberMinute > 0: # if hour and minute > 0
            QMessageBox.about(self,"",f"Alarm set for {self.NumberHour} Hours and {self.NumberMinute} Minutes from Now")
            
        elif self.NumberMinute == 0 and self.NumberHour != 0: # if minute == 0 and hour > 0
            QMessageBox.about(self,"",f"Alarm set for {self.NumberHour} Hours from Now")

        else: # if hour == 0 and minute > 0
            QMessageBox.about(self,"",f"Alarm Set For {self.NumberMinute} Minutes From Now")

        self.Make_Sound() # call Make Sound function to run wen alarm wake up

    # add make sound function to set alarm sound wen wake up
    def Make_Sound(self):
        self.SoundAlarm = QMediaPlayer()
        SoundPass = os.path.join(os.getcwd(),"sound.wav")
        url = QUrl.fromLocalFile(SoundPass)
        content = QMediaContent(url)
        sleep(self.TotalTime * 60)
        self.SoundAlarm.setMedia(content)
        self.SoundAlarm.play()

        SoundMesage = QMessageBox.question(self,"Alert",f"{self.Message.text()},If you want to snooze, press a button Yes")
        if SoundMesage == QMessageBox.Yes:
            self.SoundAlarm.setMuted(not self.SoundAlarm.isMuted())


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = MainWindow()


# start the app
sys.exit(App.exec_())