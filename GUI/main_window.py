# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_blg = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_blg.setObjectName("lineEdit_blg")
        self.horizontalLayout_2.addWidget(self.lineEdit_blg)
        self.pushButton_blgOpen = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blgOpen.setObjectName("pushButton_blgOpen")
        self.horizontalLayout_2.addWidget(self.pushButton_blgOpen)
        self.pushButton_blgEg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blgEg.setObjectName("pushButton_blgEg")
        self.horizontalLayout_2.addWidget(self.pushButton_blgEg)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_blgle = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_blgle.setObjectName("lineEdit_blgle")
        self.horizontalLayout_5.addWidget(self.lineEdit_blgle)
        self.pushButton_blgleOpen = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blgleOpen.setObjectName("pushButton_blgleOpen")
        self.horizontalLayout_5.addWidget(self.pushButton_blgleOpen)
        self.pushButton_blgleEg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blgleEg.setObjectName("pushButton_blgleEg")
        self.horizontalLayout_5.addWidget(self.pushButton_blgleEg)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_blg_func = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_blg_func.setObjectName("lineEdit_blg_func")
        self.horizontalLayout_10.addWidget(self.lineEdit_blg_func)
        self.pushButton_blg_funcOpen = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blg_funcOpen.setObjectName("pushButton_blg_funcOpen")
        self.horizontalLayout_10.addWidget(self.pushButton_blg_funcOpen)
        self.pushButton_blg_funcDemo = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_blg_funcDemo.setObjectName("pushButton_blg_funcDemo")
        self.horizontalLayout_10.addWidget(self.pushButton_blg_funcDemo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_tha = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_tha.setObjectName("pushButton_tha")
        self.horizontalLayout_3.addWidget(self.pushButton_tha)
        self.pushButton_le = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_le.setObjectName("pushButton_le")
        self.horizontalLayout_3.addWidget(self.pushButton_le)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_post = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_post.setObjectName("pushButton_post")
        self.horizontalLayout_4.addWidget(self.pushButton_post)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_tran_ipt = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_tran_ipt.setObjectName("lineEdit_tran_ipt")
        self.horizontalLayout_6.addWidget(self.lineEdit_tran_ipt)
        self.pushButton_tran_ipt = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_tran_ipt.setObjectName("pushButton_tran_ipt")
        self.horizontalLayout_6.addWidget(self.pushButton_tran_ipt)
        self.pushButton_tran_demo = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_tran_demo.setObjectName("pushButton_tran_demo")
        self.horizontalLayout_6.addWidget(self.pushButton_tran_demo)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_tran_simTest = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_tran_simTest.setObjectName("pushButton_tran_simTest")
        self.horizontalLayout_7.addWidget(self.pushButton_tran_simTest)
        self.pushButton_tran_sim = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_tran_sim.setObjectName("pushButton_tran_sim")
        self.horizontalLayout_7.addWidget(self.pushButton_tran_sim)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_tran_post = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_tran_post.setObjectName("pushButton_tran_post")
        self.verticalLayout_11.addWidget(self.pushButton_tran_post)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_saveas = QtWidgets.QAction(MainWindow)
        self.action_saveas.setObjectName("action_saveas")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_help_version = QtWidgets.QAction(MainWindow)
        self.action_help_version.setObjectName("action_help_version")
        self.action_help_doc_blg = QtWidgets.QAction(MainWindow)
        self.action_help_doc_blg.setObjectName("action_help_doc_blg")
        self.action_help_doc_tran = QtWidgets.QAction(MainWindow)
        self.action_help_doc_tran.setObjectName("action_help_doc_tran")
        self.action_help_doc_life = QtWidgets.QAction(MainWindow)
        self.action_help_doc_life.setObjectName("action_help_doc_life")
        self.action_help_doc_cri = QtWidgets.QAction(MainWindow)
        self.action_help_doc_cri.setObjectName("action_help_doc_cri")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.action_view_result = QtWidgets.QAction(MainWindow)
        self.action_view_result.setObjectName("action_view_result")
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addSeparator()
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_3.addAction(self.action_help_doc_blg)
        self.menu_3.addAction(self.action_help_doc_tran)
        self.menu_3.addAction(self.action_help_doc_life)
        self.menu_3.addAction(self.action_help_doc_cri)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_help_version)
        self.menu_4.addAction(self.action_view_result)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THU Resilience"))
        self.groupBox.setTitle(_translate("MainWindow", "输入"))
        self.label_2.setText(_translate("MainWindow", "建筑属性（震害模拟）"))
        self.pushButton_blgOpen.setText(_translate("MainWindow", "浏览"))
        self.pushButton_blgEg.setText(_translate("MainWindow", "查看示例"))
        self.label_3.setText(_translate("MainWindow", "建筑属性（损失估计）"))
        self.pushButton_blgleOpen.setText(_translate("MainWindow", "浏览"))
        self.pushButton_blgleEg.setText(_translate("MainWindow", "查看示例"))
        self.label_4.setText(_translate("MainWindow", "建筑功能（用于韧性指标）"))
        self.pushButton_blg_funcOpen.setText(_translate("MainWindow", "浏览"))
        self.pushButton_blg_funcDemo.setText(_translate("MainWindow", "查看示例"))
        self.groupBox_2.setTitle(_translate("MainWindow", "计算"))
        self.pushButton_tha.setText(_translate("MainWindow", "震害模拟"))
        self.pushButton_le.setText(_translate("MainWindow", "损失估计"))
        self.groupBox_3.setTitle(_translate("MainWindow", "后处理"))
        self.pushButton_post.setText(_translate("MainWindow", "提取结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "建筑"))
        self.groupBox_4.setTitle(_translate("MainWindow", "输入"))
        self.pushButton_tran_ipt.setText(_translate("MainWindow", "浏览"))
        self.pushButton_tran_demo.setText(_translate("MainWindow", "查看示例"))
        self.groupBox_5.setTitle(_translate("MainWindow", "计算"))
        self.pushButton_tran_simTest.setText(_translate("MainWindow", "交通模拟（20次）"))
        self.pushButton_tran_sim.setText(_translate("MainWindow", "交通模拟（500次）"))
        self.groupBox_6.setTitle(_translate("MainWindow", "后处理"))
        self.pushButton_tran_post.setText(_translate("MainWindow", "提取结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "交通"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "生命线"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "韧性评价指标"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "文档"))
        self.menu_4.setTitle(_translate("MainWindow", "查看"))
        self.action_new.setText(_translate("MainWindow", "新建"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_save.setText(_translate("MainWindow", "保存"))
        self.action_saveas.setText(_translate("MainWindow", "另存为"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_help_version.setText(_translate("MainWindow", "版本信息"))
        self.action_help_doc_blg.setText(_translate("MainWindow", "建筑"))
        self.action_help_doc_tran.setText(_translate("MainWindow", "交通"))
        self.action_help_doc_life.setText(_translate("MainWindow", "生命线"))
        self.action_help_doc_cri.setText(_translate("MainWindow", "韧性评价指标"))
        self.actiond.setText(_translate("MainWindow", "打开结果文件夹"))
        self.action_view_result.setText(_translate("MainWindow", "结果文件夹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

