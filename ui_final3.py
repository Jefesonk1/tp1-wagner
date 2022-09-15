# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ss_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}\n"
"\n"
"QWidget[form=\"true\"],QLabel[frameShape=\"1\"]{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"]{\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] .QFrame{\n"
"border:1px solid #57595B;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] QLabel,QWidget[form=\"title\"] QLabel{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[form=\"title\"],QWidget[nav=\"left\"],QWidget[nav=\"top\"] QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[nav=\"top\"] QAbstractButton:hover,QWidget[nav=\"top\"] QAbstractButton:pressed,QWidget[nav=\"top\"] QAbstractButton:checked{\n"
"border-style:solid;\n"
"border-width:0px 0px 2px 0px;\n"
"padding:4px 4px 2px 4px;\n"
"border-color:#00BB9E;\n"
"backg"
                        "round:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:checked,QWidget[nav=\"left\"] QAbstractButton:pressed{\n"
"color:#57595B;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel{\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpi"
                        "nBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#E4E4E4;\n"
"selection-color:#57595B;\n"
"}\n"
"\n"
"QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
".QFrame{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"}\n"
"\n"
".QGroupBox{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:5px;\n"
"margin-top:3ex;\n"
"}\n"
"\n"
".QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"position:relative;\n"
"left:10px;\n"
"}\n"
"\n"
".QPushButton,.QToolButton{\n"
"border-style:none;\n"
"border:1px s"
                        "olid #B6B6B6;\n"
"color:#57595B;\n"
"padding:5px;\n"
"min-height:15px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QPushButton:hover,.QToolButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
".QPushButton:pressed,.QToolButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"border-radius:3px;\n"
"color:#57595B;\n"
"padding:3px;\n"
"margin:0px;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(51,127,209,230);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"col"
                        "or:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(238,0,0,128);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/qss/qss/flatwhite/radiobutton_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:disabled{\n"
"image:url(:/qss/qss/flatwhite/radiobutton_unchecked_disable.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/qss/qss/flatwhite/radiobutton_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked:disabled{\n"
"image:url(:/qss/qss/flatwhite/radiobutton_checked_disable.png);\n"
"}\n"
"\n"
"QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"padding:0px -3px 0px 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{\n"
""
                        "image:url(:/qss/qss/flatwhite/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{\n"
"image:url(:/qss/qss/flatwhite/checkbox_unchecked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{\n"
"image:url(:/qss/qss/flatwhite/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{\n"
"image:url(:/qss/qss/flatwhite/checkbox_checked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{\n"
"image:url(:/qss/qss/flatwhite/checkbox_parcial.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indete"
                        "rminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{\n"
"image:url(:/qss/qss/flatwhite/checkbox_parcial_disable.png);\n"
"}\n"
"\n"
"QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{\n"
"image:url(:/qss/qss/flatwhite/add_top.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:2px 5px 0px 0px;\n"
"}\n"
"\n"
"QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{\n"
"image:url(:/qss/qss/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:0px 5px 2px 0px;\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"top:-2px;\n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pres"
                        "sed,QSpinBox::down-button:pressed{\n"
"bottom:-2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit[calendarPopup=\"true\"]::down-arrow,QTimeEdit[calendarPopup=\"true\"]::down-arrow,QDateTimeEdit[calendarPopup=\"true\"]::down-arrow{\n"
"image:url(:/qss/qss/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"right:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:0px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QComboBox::drop-down:on{\n"
"top:1px;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"margin:0px;\n"
"padding:3px 10px;\n"
"}\n"
"\n"
"QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"border:1px solid #B6B6B6;\n"
"margin:0px;\n"
"}\n"
"\n"
"QMenu::"
                        "item{\n"
"padding:3px 20px;\n"
"}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected,QMenuBar::item:selected{\n"
"color:#57595B;\n"
"border:0px solid #B6B6B6;\n"
"background:#F6F6F6;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QProgressBar{\n"
"min-height:10px;\n"
"background:#E4E4E4;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #E4E4E4;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"border-radius:5px;\n"
"background-color:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"background:#B6B6B6;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread"
                        ":pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:14px;\n"
"margin-left:-3px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#F6F6F6;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#B6B6B6;"
                        "\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#F6F6F6;\n"
"min-height:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidg"
                        "et::pane{\n"
"border:1px solid #B6B6B6;\n"
"selection-background-color:#F6F6F6;\n"
"selection-color:#57595B;\n"
"alternate-background-color:#F6F6F6;\n"
"gridline-color:#B6B6B6;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children{\n"
"margin:4px;\n"
"border-image:url(:/qss/qss/flatwhite/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children{\n"
"margin:4px;\n"
"border-image:url(:/qss/qss/flatwhite/branch_close.png);\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
"padding:1px;\n"
""
                        "margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"border-left-width:0px;\n"
"border-right-width:1px;\n"
"border-top-width:0px;\n"
"border-bottom-width:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border:1px solid #B6B6B6;\n"
"color:#57595B;\n"
"margin:0px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"border-style:solid;\n"
"border-color:#00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QTabBar::tab:top,QTabBar::tab:bottom{\n"
"padding:3px 8px 3px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:left,QTabBar::tab:right{\n"
"padding:8px 3px 8px 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,QTabBar::tab:top:hover{\n"
"border-width:2px 0px 0px 0px;\n"
"}\n"
"\n"
""
                        "QTabBar::tab:right:selected,QTabBar::tab:right:hover{\n"
"border-width:0px 0px 0px 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{\n"
"border-width:0px 0px 2px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,QTabBar::tab:left:hover{\n"
"border-width:0px 2px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{\n"
"border-left-width:1px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{\n"
"border-top-width:1px;\n"
"border-top-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{\n"
"border-right-width:1px;\n"
"border-right-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:ri"
                        "ght:hover{\n"
"border-bottom-width:1px;\n"
"border-bottom-color:#B6B6B6;\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #E4E4E4;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{\n"
"padding:3px;\n"
"border-radius:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolTip{\n"
"border:0px solid #57595B;\n"
"padding:1px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QPrintPreviewDialog QToolButton{\n"
"border:0px solid #57595B;\n"
"border-radius:0px;\n"
"margin:0px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QColorDialog QPushButton,QFileDialog QPushButton{\n"
"min-width:80px;\n"
"}\n"
"\n"
"QToolButton#"
                        "qt_calendar_prevmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/qss/qss/flatwhite/calendar_prevmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_nextmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/qss/qss/flatwhite/calendar_nextmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{\n"
"border:0px solid #57595B;\n"
"border-radius:3px;\n"
"margin:3px 3px 3px 3px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"margin:2px;\n"
"}\n"
"\n"
"QCalendar"
                        "Widget QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"border:1px solid #B6B6B6;\n"
"border-width:1px 1px 0px 1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"min-height:20px;\n"
"min-width:10px;\n"
"}\n"
"\n"
"QTableView[model=\"true\"]::item{\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QP"
                        "lainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"*:disabled{\n"
"background:#FFFFFF;\n"
"border-color:#E4E4E4;\n"
"}\n"
"\n"
"/*TextColor:#57595B*/\n"
"/*PanelColor:#FFFFFF*/\n"
"/*BorderColor:#B6B6B6*/\n"
"/*NormalColorStart:#E4E4E4*/\n"
"/*NormalColorEnd:#E4E4E4*/\n"
"/*DarkColorStart:#F6F6F6*/\n"
"/*DarkColorEnd:#F6F6F6*/\n"
"/*HighColor:#00BB9E*/")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.frameMain = QFrame(self.centralwidget)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setGeometry(QRect(10, 10, 1260, 676))
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Raised)
        self.widget_blue_2 = QWidget(self.frameMain)
        self.widget_blue_2.setObjectName(u"widget_blue_2")
        self.widget_blue_2.setGeometry(QRect(640, 10, 110, 60))
        self.widget_blue_2.setStyleSheet(u"background-color: blue")
        self.widget_yellow_2 = QWidget(self.frameMain)
        self.widget_yellow_2.setObjectName(u"widget_yellow_2")
        self.widget_yellow_2.setGeometry(QRect(760, 10, 110, 60))
        self.widget_yellow_2.setStyleSheet(u"background-color: yellow")
        self.widget_magenta_2 = QWidget(self.frameMain)
        self.widget_magenta_2.setObjectName(u"widget_magenta_2")
        self.widget_magenta_2.setGeometry(QRect(880, 10, 110, 60))
        self.widget_magenta_2.setStyleSheet(u"background-color: magenta")
        self.frameDrawer_2 = QFrame(self.frameMain)
        self.frameDrawer_2.setObjectName(u"frameDrawer_2")
        self.frameDrawer_2.setGeometry(QRect(220, 80, 770, 586))
        self.frameDrawer_2.setFrameShape(QFrame.StyledPanel)
        self.frameDrawer_2.setFrameShadow(QFrame.Raised)
        self.widgetDrawer_2 = QWidget(self.frameDrawer_2)
        self.widgetDrawer_2.setObjectName(u"widgetDrawer_2")
        self.widgetDrawer_2.setGeometry(QRect(10, 10, 750, 565))
        self.widgetDrawer_2.setStyleSheet(u"background-color: '#3d3d3d'")
        self.buttonSaveXml_2 = QPushButton(self.frameMain)
        self.buttonSaveXml_2.setObjectName(u"buttonSaveXml_2")
        self.buttonSaveXml_2.setGeometry(QRect(220, 25, 70, 30))
        self.buttonSaveXml_2.setStyleSheet(u"")
        self.buttonUseless_2 = QPushButton(self.frameMain)
        self.buttonUseless_2.setObjectName(u"buttonUseless_2")
        self.buttonUseless_2.setGeometry(QRect(300, 25, 70, 30))
        self.labelCoordinates_2 = QLabel(self.frameMain)
        self.labelCoordinates_2.setObjectName(u"labelCoordinates_2")
        self.labelCoordinates_2.setGeometry(QRect(380, 20, 171, 40))
        self.frame_2 = QFrame(self.frameMain)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1000, 10, 250, 280))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 231, 261))
        self.labelTranslation = QLabel(self.widget)
        self.labelTranslation.setObjectName(u"labelTranslation")
        self.labelTranslation.setGeometry(QRect(20, 30, 200, 16))
        self.labelRotation = QLabel(self.widget)
        self.labelRotation.setObjectName(u"labelRotation")
        self.labelRotation.setGeometry(QRect(20, 70, 200, 16))
        self.labelScale = QLabel(self.widget)
        self.labelScale.setObjectName(u"labelScale")
        self.labelScale.setGeometry(QRect(20, 110, 200, 16))
        self.labelWindowCoordinates = QLabel(self.widget)
        self.labelWindowCoordinates.setObjectName(u"labelWindowCoordinates")
        self.labelWindowCoordinates.setGeometry(QRect(20, 170, 200, 16))
        self.labelObjectsCoordinates = QLabel(self.widget)
        self.labelObjectsCoordinates.setObjectName(u"labelObjectsCoordinates")
        self.labelObjectsCoordinates.setGeometry(QRect(20, 210, 200, 16))
        self.treeWidget = QTreeWidget(self.frameMain)
        font = QFont()
        font.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"Name");
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setText(0, u"Type");
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 10, 200, 656))
        self.frameTransformations = QFrame(self.frameMain)
        self.frameTransformations.setObjectName(u"frameTransformations")
        self.frameTransformations.setGeometry(QRect(1000, 300, 250, 366))
        self.frameTransformations.setAutoFillBackground(False)
        self.frameTransformations.setFrameShape(QFrame.StyledPanel)
        self.frameTransformations.setFrameShadow(QFrame.Raised)
        self.widgetTrasformations = QWidget(self.frameTransformations)
        self.widgetTrasformations.setObjectName(u"widgetTrasformations")
        self.widgetTrasformations.setGeometry(QRect(10, 10, 230, 480))
        self.widgetTrasformations.setStyleSheet(u"")
        self.buttomRotateLeft = QPushButton(self.widgetTrasformations)
        self.buttomRotateLeft.setObjectName(u"buttomRotateLeft")
        self.buttomRotateLeft.setGeometry(QRect(30, 80, 50, 30))
        self.buttomRotateLeft.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"rotate-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomRotateLeft.setIcon(icon)
        self.buttomRotateLeft.setIconSize(QSize(24, 24))
        self.buttomRotateLeft.setCheckable(False)
        self.buttomRotateLeft.setAutoExclusive(False)
        self.buttomRight_2 = QPushButton(self.widgetTrasformations)
        self.buttomRight_2.setObjectName(u"buttomRight_2")
        self.buttomRight_2.setGeometry(QRect(150, 80, 50, 30))
        self.buttomRight_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"rotate-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomRight_2.setIcon(icon1)
        self.buttomRight_2.setIconSize(QSize(24, 24))
        self.buttomRight_2.setCheckable(False)
        self.buttomRight_2.setAutoExclusive(False)
        self.buttomUp = QPushButton(self.widgetTrasformations)
        self.buttomUp.setObjectName(u"buttomUp")
        self.buttomUp.setGeometry(QRect(90, 80, 50, 30))
        self.buttomUp.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"up-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomUp.setIcon(icon2)
        self.buttomUp.setIconSize(QSize(24, 24))
        self.buttomUp.setCheckable(False)
        self.buttomUp.setAutoExclusive(False)
        self.buttomDown = QPushButton(self.widgetTrasformations)
        self.buttomDown.setObjectName(u"buttomDown")
        self.buttomDown.setGeometry(QRect(90, 160, 50, 30))
        self.buttomDown.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"down-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomDown.setIcon(icon3)
        self.buttomDown.setIconSize(QSize(24, 24))
        self.buttomDown.setCheckable(False)
        self.buttomDown.setAutoExclusive(False)
        self.buttomLeft = QPushButton(self.widgetTrasformations)
        self.buttomLeft.setObjectName(u"buttomLeft")
        self.buttomLeft.setGeometry(QRect(30, 120, 50, 30))
        self.buttomLeft.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomLeft.setIcon(icon4)
        self.buttomLeft.setIconSize(QSize(24, 24))
        self.buttomLeft.setCheckable(False)
        self.buttomLeft.setAutoExclusive(False)
        self.buttomRight = QPushButton(self.widgetTrasformations)
        self.buttomRight.setObjectName(u"buttomRight")
        self.buttomRight.setGeometry(QRect(150, 120, 50, 30))
        self.buttomRight.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomRight.setIcon(icon5)
        self.buttomRight.setIconSize(QSize(24, 24))
        self.buttomRight.setCheckable(False)
        self.buttomRight.setAutoExclusive(False)
        self.spinBoxRotateStepSize = QSpinBox(self.widgetTrasformations)
        self.spinBoxRotateStepSize.setObjectName(u"spinBoxRotateStepSize")
        self.spinBoxRotateStepSize.setGeometry(QRect(150, 260, 42, 25))
        self.labelMoveRotate = QLabel(self.widgetTrasformations)
        self.labelMoveRotate.setObjectName(u"labelMoveRotate")
        self.labelMoveRotate.setGeometry(QRect(60, 30, 111, 20))
        self.spinBoxTranslateStepSize = QSpinBox(self.widgetTrasformations)
        self.spinBoxTranslateStepSize.setObjectName(u"spinBoxTranslateStepSize")
        self.spinBoxTranslateStepSize.setGeometry(QRect(150, 220, 42, 25))
        self.labelTranslateStepSize = QLabel(self.widgetTrasformations)
        self.labelTranslateStepSize.setObjectName(u"labelTranslateStepSize")
        self.labelTranslateStepSize.setGeometry(QRect(30, 220, 100, 20))
        self.labelRotateStepSize = QLabel(self.widgetTrasformations)
        self.labelRotateStepSize.setObjectName(u"labelRotateStepSize")
        self.labelRotateStepSize.setGeometry(QRect(30, 260, 100, 20))
        self.buttomHome = QPushButton(self.widgetTrasformations)
        self.buttomHome.setObjectName(u"buttomHome")
        self.buttomHome.setGeometry(QRect(90, 120, 50, 30))
        self.buttomHome.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"botao-homee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomHome.setIcon(icon6)
        self.buttomHome.setIconSize(QSize(24, 24))
        self.buttomHome.setCheckable(False)
        self.buttomHome.setAutoExclusive(False)
        self.buttomZoomIn = QPushButton(self.widgetTrasformations)
        self.buttomZoomIn.setObjectName(u"buttomZoomIn")
        self.buttomZoomIn.setGeometry(QRect(150, 160, 50, 30))
        self.buttomZoomIn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"../mais-zoom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomZoomIn.setIcon(icon7)
        self.buttomZoomIn.setIconSize(QSize(24, 24))
        self.buttomZoomIn.setCheckable(False)
        self.buttomZoomIn.setAutoExclusive(False)
        self.buttomZoomOut = QPushButton(self.widgetTrasformations)
        self.buttomZoomOut.setObjectName(u"buttomZoomOut")
        self.buttomZoomOut.setGeometry(QRect(30, 160, 50, 30))
        self.buttomZoomOut.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"../reduzir-o-zoom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttomZoomOut.setIcon(icon8)
        self.buttomZoomOut.setIconSize(QSize(24, 24))
        self.buttomZoomOut.setCheckable(False)
        self.buttomZoomOut.setAutoExclusive(False)
        self.radioButtonWindow = QRadioButton(self.widgetTrasformations)
        self.radioButtonWindow.setObjectName(u"radioButtonWindow")
        self.radioButtonWindow.setGeometry(QRect(130, 300, 89, 20))
        self.radioButtonObjects = QRadioButton(self.widgetTrasformations)
        self.radioButtonObjects.setObjectName(u"radioButtonObjects")
        self.radioButtonObjects.setGeometry(QRect(30, 300, 90, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Viewport Visualizer", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.buttonSaveXml_2.setText(QCoreApplication.translate("MainWindow", u"teste", None))
        self.buttonUseless_2.setText(QCoreApplication.translate("MainWindow", u"teste2", None))
        self.labelCoordinates_2.setText(QCoreApplication.translate("MainWindow", u"coordinates:", None))
        self.labelTranslation.setText(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.labelScale.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.labelWindowCoordinates.setText(QCoreApplication.translate("MainWindow", u"Window Coordinates", None))
        self.labelObjectsCoordinates.setText(QCoreApplication.translate("MainWindow", u"Object Coordinates", None))

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"p1", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Point", None));
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"l1", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"p1", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Polygon", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.buttomRotateLeft.setText("")
        self.buttomRight_2.setText("")
        self.buttomUp.setText("")
        self.buttomDown.setText("")
        self.buttomLeft.setText("")
        self.buttomRight.setText("")
        self.labelMoveRotate.setText(QCoreApplication.translate("MainWindow", u"Move/Rotate/Scale", None))
        self.labelTranslateStepSize.setText(QCoreApplication.translate("MainWindow", u"Traslation step size", None))
        self.labelRotateStepSize.setText(QCoreApplication.translate("MainWindow", u"Rotation step size", None))
        self.buttomHome.setText("")
        self.buttomZoomIn.setText("")
        self.buttomZoomOut.setText("")
        self.radioButtonWindow.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.radioButtonObjects.setText(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

