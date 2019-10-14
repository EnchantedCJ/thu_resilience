# -*- coding: utf-8 -*-
import sys
import os
import shutil
import subprocess

from GUI import main_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QProgressDialog
from PyQt5.QtCore import Qt

from building.script.EDPsFormatter import EDPsFormatterExec
from building.script import blg_post
from criteria.script import cr_post


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self._buildSignalAndSlot()

    # signals and slots
    def _buildSignalAndSlot(self):
        ########## menu ##########
        self.ui.action_view_result.triggered.connect(self._menu_view_results)
        self.ui.actions_help_doc_use.triggered.connect(self._menu_help_doc_use)
        self.ui.action_help_doc_blg.triggered.connect(self._menu_help_doc_blg)
        self.ui.action_help_doc_tran.triggered.connect(self._menu_help_doc_tran)
        self.ui.action_help_doc_life.triggered.connect(self._menu_help_doc_life)
        self.ui.action_help_doc_cri.triggered.connect(self._menu_help_doc_cr)
        self.ui.action_help_version.triggered.connect(self._menu_help_version)

        ########## building ##########
        # self.ui.pushButton_gmOpen.clicked.connect(self._blg_gm_open)
        # self.ui.pushButton_gmEg.clicked.connect(self._blg_gm_eg)
        self.ui.pushButton_blgOpen.clicked.connect(self._blg_open)
        self.ui.pushButton_blgEg.clicked.connect(self._blg_eg)
        self.ui.pushButton_blgleOpen.clicked.connect(self._blg_le_open)
        self.ui.pushButton_blgleEg.clicked.connect(self._blg_le_eg)
        self.ui.pushButton_blg_funcOpen.clicked.connect(self._blg_func_open)
        self.ui.pushButton_blg_funcDemo.clicked.connect(self._blg_func_demo)
        self.ui.pushButton_tha.clicked.connect(self._blg_tha)
        self.ui.pushButton_le.clicked.connect(self._blg_loss_estimate)
        self.ui.pushButton_post.clicked.connect(self._blg_postprocess)

        ########## transport ##########
        self.ui.pushButton_tran_ipt.clicked.connect(self._tran_ipt)
        self.ui.pushButton_tran_demo.clicked.connect(self._tran_demo)
        self.ui.pushButton_tran_simTest.clicked.connect(self._tran_sim_test)
        self.ui.pushButton_tran_sim.clicked.connect(self._tran_sim)
        self.ui.pushButton_tran_post.clicked.connect(self._tran_post)

        ########## lifeline ##########
        self.ui.pushButton_life_ipt.clicked.connect(self._life_ipt)
        self.ui.pushButton_life_demo.clicked.connect(self._life_demo)
        self.ui.pushButton_life_sim.clicked.connect(self._life_sim)
        self.ui.pushButton_life_post.clicked.connect(self._life_post)

        ########## criteria ##########
        self.ui.pushButton_cr_sim.clicked.connect(self._cr_sim)
        self.ui.pushButton_cr_post.clicked.connect(self._cr_post)

    ########## menu ##########
    def _menu_view_results(self):
        rootDir = os.getcwd()
        try:
            os.system('explorer.exe ' + rootDir + '\\results')
        except:
            QMessageBox.warning(self, '错误', '无法打开结果文件夹！')
            return

    def _menu_help_doc_use(self):
        try:
            os.system('start notepad Readme.md')
        except:
            QMessageBox.warning(self, '错误', '无法打开说明文档！')
            return

    def _menu_help_doc_blg(self):
        try:
            os.system('start ./doc/building/doc_building.docx')
        except:
            QMessageBox.warning(self, '错误', '无法打开说明文档！')
            return

    def _menu_help_doc_tran(self):
        try:
            os.system('start ./doc/transport/doc_transportation.docx')
        except:
            QMessageBox.warning(self, '错误', '无法打开说明文档！')
            return

    def _menu_help_doc_life(self):
        try:
            os.system('start ./doc/lifeline/doc_lifeline.docx')
        except:
            QMessageBox.warning(self, '错误', '无法打开说明文档！')
            return

    def _menu_help_doc_cr(self):
        try:
            os.system('start ./doc/criteria/doc_indicator.docx')
        except:
            QMessageBox.warning(self, '错误', '无法打开说明文档！')
            return

    def _menu_help_version(self):
        QMessageBox.information(self,
                                '版本信息',
                                '北京市地震安全韧性评估系统\n'
                                '\n'
                                '开发者：清华大学土木工程系暨建设管理系\n'
                                '版本信息：v1.0\n'
                                '最近更新：2019/9/27\n'
                                '\n'
                                'Copyright © 2019-2019 北京市地震局.')

    ########## building ##########
    # def _blg_gm_open(self):
    #     self.gmPath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;Text Files (*.txt)')
    #     if self.gmPath[-4:] == '.txt':
    #         self.ui.lineEdit_gm.setText(self.gmPath)
    #     else:
    #         QMessageBox.warning(self, '错误', '地震动文件应为txt格式！')
    #
    # def _blg_gm_eg(self):
    #     try:
    #         os.system('notepad ' + './demo/building/ground_motion.txt')
    #     except:
    #         QMessageBox.warning(self, '错误', '无法打开示例文件！')

    def _blg_open(self):
        self.blgPath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;Text Files (*.txt)')
        if self.blgPath[-4:] == '.txt':
            self.ui.lineEdit_blg.setText(self.blgPath)
        else:
            QMessageBox.warning(self, '错误', '建筑属性文件（震害模拟）应为txt格式！')
            return

    def _blg_eg(self):
        try:
            os.system('start notepad ' + './demo/building/BlgAttributes.txt')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')
            return

    def _blg_le_open(self):
        self.blglePath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;CSV Files (*.csv)')
        if self.blglePath[-4:] == '.csv':
            self.ui.lineEdit_blgle.setText(self.blglePath)
        else:
            QMessageBox.warning(self, '错误', '建筑属性文件（损失估计）应为csv格式！')
            return

    def _blg_le_eg(self):
        try:
            os.system('start notepad ' + './demo/building/BuildingsInfo-Tsinghua.csv')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')
            return

    def _blg_func_open(self):
        self.blgFuncPath, filetype = QFileDialog.getOpenFileName(self, '打开', './', 'All Files (*);;Text Files (*.txt)')
        if self.blgFuncPath[-4:] == '.txt':
            self.ui.lineEdit_blg_func.setText(self.blgFuncPath)
        else:
            QMessageBox.warning(self, '错误', '建筑功能文件（用于韧性指标）应为txt格式！')
            return

    def _blg_func_demo(self):
        try:
            os.system('start notepad ' + './demo/building/BlgFunction.txt')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')
            return

    def _blg_tha(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/building/tha'

        # prepare files
        # ## ground motion
        # try:
        #     self.gmFile = self.gmPath.split('/')[-1]
        #     self.gmName = self.gmFile.strip('.txt')
        #     dst = workDir + '/GMs/' + self.gmFile
        #     shutil.copy(self.gmPath, dst)
        #     with open(workDir + '/inputs/EQ_List.txt', 'w', encoding='utf-8') as f:
        #         f.write(self.gmName)
        # except:
        #     QMessageBox.warning(self, '错误', '地震动文件获取失败！')

        ## building attributes
        try:
            for pga in [0.2, 0.3, 0.4]:
                for direction in ['x', 'y']:
                    dst = workDir + '/' + str(pga) + '/' + direction + '/inputs/BlgAttributes-cache.txt'
                    shutil.copy(self.blgPath, dst)
                    fin = open(dst, 'r', encoding='utf-8')
                    fout = open(workDir + '/' + str(pga) + '/' + direction + '/inputs/BlgAttributes.txt', 'w',
                                encoding='utf-8')
                    # line 1-2
                    fout.write(fin.readline())
                    fout.write(fin.readline())
                    # line 3-
                    reduct = {'x': 1, 'y': 0.85}
                    for line in fin.readlines():
                        temp = line.split()
                        temp[13] = str(pga * 10 * reduct[direction])  # pga
                        newline = '\t'.join(temp) + '\n'
                        fout.write(newline)
                    fin.close()
                    fout.close()
        except:
            QMessageBox.warning(self, '错误', '建筑属性文件（震害模拟）获取失败！')
            return

        # computing
        try:
            for pga in [0.2, 0.3, 0.4]:
                for direction in ['x', 'y']:
                    os.chdir(workDir + '/' + str(pga) + '/' + direction)
                    subprocess.Popen('Flexural_Shear_X.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        except:
            QMessageBox.warning(self, '错误', '无法启动震害模拟！')
            return

        os.chdir(rootDir)

    def _blg_loss_estimate(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/building/loss'

        # prepare files
        ## building attributes
        try:
            for pga in [0.2, 0.3, 0.4]:
                for direction in ['x', 'y']:
                    dst = workDir + '/' + str(pga) + '/' + direction + '/input/BuildingsInfo.csv'
                    shutil.copy(self.blglePath, dst)
        except:
            QMessageBox.warning(self, '错误', '建筑属性文件（损失估计）获取失败！')
            return

        ## edps
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在准备计算文件...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(0)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, 6)
        i = 0
        progress.setValue(i)
        try:
            for pga in [0.2, 0.3, 0.4]:
                for direction in ['x', 'y']:
                    dirIn = rootDir + '/building/tha/' + str(pga) + '/' + direction + '/Results/EDPs.txt'
                    dirOut = workDir + '/' + str(pga) + '/' + direction + '/input/Edps.txt'
                    dirAttr = rootDir + '/building/tha/' + str(pga) + '/' + direction + '/inputs/BlgAttributes.txt'
                    EDPsFormatterExec.main(dirIn, dirOut, dirAttr, {'numEQ': 11, 'idr2comp': True})
                    i += 1
                    progress.setValue(i)
                    if progress.wasCanceled():
                        QMessageBox.warning(self, "提示", "已取消")
                        return
        except:
            QMessageBox.warning(self, '错误', 'EDP文件获取失败！')
            return

        # computing
        try:
            for pga in [0.2, 0.3, 0.4]:
                for direction in ['x', 'y']:
                    os.chdir(workDir + '/' + str(pga) + '/' + direction)
                    subprocess.Popen('LossEstimator.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        except:
            QMessageBox.warning(self, '错误', '无法启动损失估计！')
            return

        os.chdir(rootDir)

    def _blg_postprocess(self):
        if not os.path.exists('./results'):
            os.mkdir('./results')
        if not os.path.exists('./results/building'):
            os.mkdir('./results/building')

        try:
            for pga in [0.2, 0.3, 0.4]:
                if not os.path.exists('./results/building/' + str(pga)):
                    os.mkdir('./results/building/' + str(pga))
                for direction in ['x', 'y']:
                    if not os.path.exists('./results/building/' + str(pga) + '/' + direction):
                        os.mkdir('./results/building/' + str(pga) + '/' + direction)
                    src = './building/tha/' + str(pga) + '/' + direction + '/Results/DamageState.txt'
                    dst = './results/building/' + str(pga) + '/' + direction + '/DamageState.txt'
                    shutil.copy(src, dst)
                    src = './building/loss/' + str(pga) + '/' + direction + '/output/basic.txt'
                    dst = './results/building/' + str(pga) + '/' + direction + '/basic.txt'
                    shutil.copy(src, dst)

            resultDir = './results/building'
            blg_post.postprocess(self.blgFuncPath, resultDir)

            QMessageBox.information(self, '信息', '结果提取完成！')
        except:
            QMessageBox.warning(self, '错误', '结果提取失败！')
            return

    ########## transport ##########
    def _tran_ipt(self):
        self.tranIptPath, filetype = QFileDialog.getOpenFileName(self, '打开', './',
                                                                 'All Files (*);;Excel Files (*.xlsx)')
        if self.tranIptPath[-5:] == '.xlsx':
            self.ui.lineEdit_tran_ipt.setText(self.tranIptPath)
        else:
            QMessageBox.warning(self, '错误', '交通输入文件应为xlsx格式！')
            return

    def _tran_demo(self):
        try:
            os.system('start ./demo/transport/input_sampleQHY.xlsx')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件！')
            return

    def _tran_sim_test(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/transport'

        try:
            dst = workDir + '/input.xlsx'
            shutil.copy(self.tranIptPath, dst)
        except:
            QMessageBox.warning(self, '错误', '输入文件获取失败！')
            return

        try:
            os.chdir(workDir)
            os.system('matlab -r ' + 'transportation02_20iter')
            os.chdir(rootDir)
        except:
            QMessageBox.warning(self, '错误', '无法启动交通模拟（测试）！')
            return

    def _tran_sim(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/transport'

        try:
            dst = workDir + '/input.xlsx'
            shutil.copy(self.tranIptPath, dst)
        except:
            QMessageBox.warning(self, '错误', '输入文件获取失败！')
            return

        try:
            os.chdir(workDir)
            os.system('matlab -r ' + 'transportation02')
            os.chdir(rootDir)
        except:
            QMessageBox.warning(self, '错误', '无法启动交通模拟！')
            return

    def _tran_post(self):
        if not os.path.exists('./results'):
            os.mkdir('./results')
        if not os.path.exists('./results/transport'):
            os.mkdir('./results/transport')

        try:
            src = './transport/output.xlsx'
            dst = './results/transport/output.xlsx'
            shutil.copy(src, dst)
            QMessageBox.information(self, '信息', '结果提取完成！')
        except:
            QMessageBox.warning(self, '错误', '结果提取失败！')
            return

    ########## lifeline ##########
    def _life_ipt(self):
        self.lifeIptPath = QFileDialog.getExistingDirectory(self, '打开', './')
        self.ui.lineEdit_life_ipt.setText(self.lifeIptPath)

    def _life_demo(self):
        rootDir = os.getcwd()
        try:
            os.system('explorer.exe ' + rootDir + '\\demo\\lifeline\\全部数据')
        except:
            QMessageBox.warning(self, '错误', '无法打开示例文件夹！')
            return

    def _life_sim(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/lifeline'

        try:
            dst = workDir + '/全部数据'
            try:
                shutil.rmtree(dst)
            except:
                pass
            shutil.copytree(self.lifeIptPath, dst)
        except:
            QMessageBox.warning(self, '错误', '输入文件获取失败！')
            return

        try:
            os.chdir(workDir)
            os.system('matlab -r ' + 'demomain')
            os.chdir(rootDir)
        except:
            QMessageBox.warning(self, '错误', '无法启动生命线模拟！')
            return

    def _life_post(self):
        if not os.path.exists('./results'):
            os.mkdir('./results')
        if not os.path.exists('./results/lifeline'):
            os.mkdir('./results/lifeline')

        try:
            src = './lifeline/输出数据'
            dst = './results/lifeline/输出数据'
            try:
                shutil.rmtree(dst)
            except:
                pass
            shutil.copytree(src, dst)
            QMessageBox.information(self, '信息', '结果提取完成！')
        except:
            QMessageBox.warning(self, '错误', '结果提取失败！')
            return

    ########## criteria ##########
    def _cr_sim(self):
        rootDir = os.getcwd()
        workDir = rootDir + '/criteria'

        # 获取结果，写入表格
        resultDir = './results'
        excelFile = workDir + '/平台整体指标文件.xlsx'
        cr_post.postprocess(resultDir, excelFile)

        # 运行
        try:
            os.chdir(workDir)
            os.system('matlab -r ' + 'indicator')
            os.chdir(rootDir)
        except:
            QMessageBox.warning(self, '错误', '无法启动韧性指标计算！')
            return

    def _cr_post(self):
        if not os.path.exists('./results'):
            os.mkdir('./results')
        if not os.path.exists('./results/criteria'):
            os.mkdir('./results/criteria')

        try:
            src = './criteria/平台整体指标文件.xlsx'
            dst = './results/criteria/平台整体指标文件.xlsx'
            shutil.copy(src, dst)
            QMessageBox.information(self, '信息', '结果提取完成！')
        except:
            QMessageBox.warning(self, '错误', '结果提取失败！')
            return


def exec():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    exec()
