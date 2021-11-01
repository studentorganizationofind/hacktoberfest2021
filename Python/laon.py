# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Age calculator")

		# setting geometry
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating head label
		head = QLabel("Age Calculator", self)

		# setting geometry to the head
		head.setGeometry(100, 10, 300, 60)

		# font
		font = QFont('Times', 14)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)
		head.setStyleSheet("color : green;")


		# D.O.B label
		dob = QLabel("Date of Birth", self)

		# setting geometry
		dob.setGeometry(0, 80, 250, 50)

		# setting alignment and font
		dob.setAlignment(Qt.AlignCenter)
		dob.setFont(QFont('Times', 10))

		# given date label
		given = QLabel("Given Date", self)

		# setting geometry
		given.setGeometry(300, 80, 250, 50)

		# setting alignment and font
		given.setAlignment(Qt.AlignCenter)
		given.setFont(QFont('Times', 10))

		# creating a QDateEdit to get the d.o.b
		self.first = QDateEdit(self)

		# setting geometry
		self.first.setGeometry(25, 130, 200, 50)

		# setting font and alignment
		self.first.setAlignment(Qt.AlignCenter)
		self.first.setFont(QFont('Arial', 9))

		# adding action to the first
		# when date get change
		self.first.dateChanged.connect(self.first_action)

		# creating a QDateEdit to get the given date
		self.second = QDateEdit(self)

		# setting geometry
		self.second.setGeometry(275, 130, 200, 50)

		# setting font and alignment
		self.second.setAlignment(Qt.AlignCenter)
		self.second.setFont(QFont('Arial', 9))

		# adding action to the second
		# when date get change
		self.second.dateChanged.connect(self.second_action)

		# create a push button for calculate
		calculate = QPushButton("Calculate", self)

		# setting geometry to the push button
		calculate.setGeometry(200, 210, 100, 40)

		# setting color effect to the push button
		color = QGraphicsColorizeEffect()
		color.setColor(Qt.darkGreen)
		calculate.setGraphicsEffect(color)

		# adding action to the calculate button
		calculate.clicked.connect(self.find_age)

		# creating a result label to show the ans
		self.result = QLabel(self)

		# setting geometry
		self.result.setGeometry(50, 280, 400, 80)

		# setting style sheet and the font
		self.result.setAlignment(Qt.AlignCenter)
		self.result.setFont(QFont('Times', 12))

		# setting stylesheet
		self.result.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : lightgrey;"
								"}")

		# making label multi line
		self.result.setWordWrap(True)

		# set dates to the first and second
		self.first.setDate(QDate(2000, 1, 1))
		self.second.setDate(QDate(2020, 1, 1))


	# method called by the first date edit
	def first_action(self):

		# get the second date
		date = self.second.date()

		# set the maximum date in first
		self.first.setMaximumDate(date)

	# method called by the first date edit
	def second_action(self):

		# get the first date
		date = self.first.date()

		# set the maximum date in first
		self.second.setMinimumDate(date)


	# method called by the push button
	def find_age(self):

		# get the first age
		get_Qdate1 = self.first.date()
		birth_year = get_Qdate1.year()
		birth_month = get_Qdate1.month()
		birth_day = get_Qdate1.day()

		# get the second age
		get_Qdate2 = self.second.date()
		given_year = get_Qdate2.year()
		given_month = get_Qdate2.month()
		given_day = get_Qdate2.day()

		# if birth date is greater then given birth_month
		# then donot count this month and add 30 to the date so
		# as to subtract the date and get the remaining days
		month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		if (birth_day > given_day):
			given_month = given_month - 1
			given_day = given_day + month[birth_month - 1]

		# if birth month exceeds given month, then
		# donot count this year and add 12 to the
		# month so that we can subtract and find out
		# the difference
		if (birth_month > given_month):
			given_year = given_year - 1
			given_month = given_month + 12

		# calculate day, month, year
		calculated_day = given_day - birth_day
		calculated_month = given_month - birth_month
		calculated_year = given_year - birth_year

		# setting text to the result
		self.result.setText(str(calculated_day) + " Day(s), " + str(calculated_month)
							+ " Month(s), " + str(calculated_year) + " Year(s)")



	# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
