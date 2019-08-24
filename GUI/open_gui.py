# -*- coding: utf-8 -*-
import sys
import os
import shutil
import subprocess

from GUI import main_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QProcess

from building.loss import EDPsFormatterExec


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self._buildSignalAndSlot()

    # signals and slots
    def _buildSignalAndSlot(self):
        # building
        ## input
        self.ui.pushButton_gmOpen.clicked.connect(self._gm_open)
        self.ui.pushButton_gmEg.clicked.connect(self._gm_eg)
        self.ui.pushButton_blgOpen.clicked.connect(self._blg_open)
        self.ui.pushButton_blgEg.clicked.connect(self._blg_eg)
        self.ui.pushButton_blgleOpen.clicked.connect(self._blgle_open)
        self.ui.pushButton_blgleEg.clicked.connect(self._blgle_eg)

        ## calculate
        self.ui.pushButton_tha.clicked.connect(self._tha)
        self.ui.pushButton_le.clicked.connect(self._loss_estimate)

        ## postprocess
        self.ui.pushButton_post.clicked.connect(self._post_process)

        # TODO: transport, lifeline

    ## building
    def _gm_open(self):
        self.gmPath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;Text Files (*.txt)')
        if self.gmPath[-4:] == '.txt':
            self.ui.lineEdit_gm.setText(self.gmPath)
        else:
            QMessageBox.warning(self, '错误', '地震动文件应为txt格式！')

    def _gm_eg(self):
        try:
            os.system('notepad ' + './example/ground_motion.txt')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')

    def _blg_open(self):
        self.blgPath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;Text Files (*.txt)')
        if self.blgPath[-4:] == '.txt':
            self.ui.lineEdit_blg.setText(self.blgPath)
        else:
            QMessageBox.warning(self, '错误', '建筑属性文件（震害模拟）应为txt格式！')

    def _blg_eg(self):
        try:
            os.system('notepad ' + './example/BlgAttributes.txt')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')

    def _blgle_open(self):
        self.blglePath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;CSV Files (*.csv)')
        if self.blglePath[-4:] == '.csv':
            self.ui.lineEdit_blgle.setText(self.blglePath)
        else:
            QMessageBox.warning(self, '错误', '建筑属性文件（损失估计）应为csv格式！')

    def _blgle_eg(self):
        try:
            os.system('notepad ' + './example/BuildingsInfo-Tsinghua.csv')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')

    def _tha(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/building/tha'

        # prepare files
        ## ground motion
        try:
            self.gmFile = self.gmPath.split('/')[-1]
            self.gmName = self.gmFile.strip('.txt')
            dst = workDir + '/GMs/' + self.gmFile
            shutil.copy(self.gmPath, dst)
            with open(workDir + '/inputs/EQ_List.txt', 'w', encoding='utf-8') as f:
                f.write(self.gmName)
        except:
            QMessageBox.warning(self, '错误', '地震动文件获取失败！')

        ## building attributes
        try:
            dst = workDir + '/inputs/BlgAttributes.txt'
            shutil.copy(self.blgPath, dst)
        except:
            QMessageBox.warning(self, '错误', '建筑属性文件（震害模拟）获取失败！')

        # computing
        try:
            os.chdir(workDir)
            subprocess.Popen('Flexural_Shear_X.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.chdir(rootDir)
        except:
            QMessageBox.warning(self, '错误', '无法启动震害模拟！')

    def _loss_estimate(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/building/loss'
        os.chdir(workDir)

        # prepare files
        ## building attributes
        try:
            dst = workDir + '/LossEstimator/input/BuildingsInfo.csv'
            shutil.copy(self.blglePath, dst)
        except:
            QMessageBox.warning(self, '错误', '建筑属性文件（损失估计）获取失败！')

        ## edps
        try:
            EDPsFormatterExec.main({'numEQ': 1, 'idr2comp': True})
        except:
            QMessageBox.warning(self, '错误', 'EDP文件获取失败！')

        # computing
        try:
            print('hello')
            os.chdir(workDir + '/LossEstimator')
            subprocess.Popen('LossEstimator.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
            print('bye')
        except:
            QMessageBox.warning(self, '错误', '无法启动损失估计！')

        os.chdir(rootDir)

    def _post_process(self):
        if not os.path.exists('./results'):
            os.mkdir('./results')
        if not os.path.exists('./results/building'):
            os.mkdir('./results/building')

        try:
            src = './building/tha/Results/DamageState.txt'
            dst = './results/building/DamageState.txt'
            shutil.copy(src, dst)
            src = './building/loss/LossEstimator/output/basic.txt'
            dst = './results/building/basic.txt'
            shutil.copy(src, dst)
            QMessageBox.information(self, '信息', '结果提取完成！')
        except:
            QMessageBox.information(self, '错误', '结果提取失败！')

    # other functions


def exec():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    exec()
