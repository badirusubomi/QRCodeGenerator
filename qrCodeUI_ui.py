# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrCodeUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 832)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#242021;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(644, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.viewHistoryButton = QPushButton(self.widget_5)
        self.viewHistoryButton.setObjectName(u"viewHistoryButton")
        self.viewHistoryButton.setMinimumSize(QSize(80, 30))
        self.viewHistoryButton.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.viewHistoryButton)

        self.viewHistoryButton_2 = QPushButton(self.widget_5)
        self.viewHistoryButton_2.setObjectName(u"viewHistoryButton_2")
        self.viewHistoryButton_2.setMinimumSize(QSize(100, 30))
        self.viewHistoryButton_2.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.viewHistoryButton_2)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(729, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qrLinkLineEdit = QLineEdit(self.widget_4)
        self.qrLinkLineEdit.setObjectName(u"qrLinkLineEdit")
        self.qrLinkLineEdit.setMinimumSize(QSize(300, 0))
        self.qrLinkLineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	 border: 2px solid gray;\n"
"	border-radius: 10px;\n"
"background-color: #ffffff;\n"
"}")

        self.horizontalLayout_2.addWidget(self.qrLinkLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(388, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.generateQRButton = QPushButton(self.widget_2)
        self.generateQRButton.setObjectName(u"generateQRButton")
        self.generateQRButton.setMinimumSize(QSize(120, 30))
        self.generateQRButton.setMaximumSize(QSize(120, 30))
        self.generateQRButton.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.generateQRButton)

        self.horizontalSpacer_6 = QSpacerItem(660, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.widget_9 = QWidget(self.page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 500))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.downloadImageButton = QPushButton(self.widget_9)
        self.downloadImageButton.setObjectName(u"downloadImageButton")
        self.downloadImageButton.setMinimumSize(QSize(150, 30))
        self.downloadImageButton.setMaximumSize(QSize(150, 0))
        self.downloadImageButton.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.downloadImageButton)

        self.horizontalSpacer = QSpacerItem(210, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.qrImageLabelView = QLabel(self.widget_9)
        self.qrImageLabelView.setObjectName(u"qrImageLabelView")
        self.qrImageLabelView.setMinimumSize(QSize(300, 300))

        self.horizontalLayout_6.addWidget(self.qrImageLabelView)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.page)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.page_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.returnToHomeButton = QPushButton(self.widget_7)
        self.returnToHomeButton.setObjectName(u"returnToHomeButton")
        self.returnToHomeButton.setMinimumSize(QSize(80, 30))
        self.returnToHomeButton.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.returnToHomeButton)

        self.horizontalSpacer_8 = QSpacerItem(644, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.returnToHomeButton_2 = QPushButton(self.widget_7)
        self.returnToHomeButton_2.setObjectName(u"returnToHomeButton_2")
        self.returnToHomeButton_2.setMinimumSize(QSize(100, 30))
        self.returnToHomeButton_2.setStyleSheet(u"background-color: #1b2b52;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.returnToHomeButton_2)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableView = QTableView(self.widget_8)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_6.addWidget(self.tableView)


        self.verticalLayout_5.addWidget(self.widget_8)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.returnToHomeButton_2.pressed.connect(MainWindow.close)
        self.viewHistoryButton_2.pressed.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.viewHistoryButton.setText(QCoreApplication.translate("MainWindow", u"View History", None))
        self.viewHistoryButton_2.setText(QCoreApplication.translate("MainWindow", u"Close Application", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your URL :", None))
        self.qrLinkLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste link here...", None))
        self.generateQRButton.setText(QCoreApplication.translate("MainWindow", u"Generate QR Code", None))
        self.downloadImageButton.setText(QCoreApplication.translate("MainWindow", u"Download Image", None))
        self.qrImageLabelView.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Courtesy: Olasubomi Badiru", None))
        self.returnToHomeButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.returnToHomeButton_2.setText(QCoreApplication.translate("MainWindow", u"Close Application", None))
    # retranslateUi

