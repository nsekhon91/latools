# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latools/latools.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_latools(object):
    def setupUi(self, latools):
        latools.setObjectName(_fromUtf8("latools"))
        latools.resize(1221, 774)
        self.mainWindow = QtGui.QWidget(latools)
        self.mainWindow.setMouseTracking(False)
        self.mainWindow.setObjectName(_fromUtf8("mainWindow"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mainWindow)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topPanel = QtGui.QHBoxLayout()
        self.topPanel.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.topPanel.setMargin(11)
        self.topPanel.setSpacing(6)
        self.topPanel.setObjectName(_fromUtf8("topPanel"))
        self.proc_tabs = QtGui.QTabWidget(self.mainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proc_tabs.sizePolicy().hasHeightForWidth())
        self.proc_tabs.setSizePolicy(sizePolicy)
        self.proc_tabs.setObjectName(_fromUtf8("proc_tabs"))
        self.tab_load = QtGui.QWidget()
        self.tab_load.setObjectName(_fromUtf8("tab_load"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_load)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.load_layout = QtGui.QGridLayout()
        self.load_layout.setMargin(11)
        self.load_layout.setSpacing(6)
        self.load_layout.setObjectName(_fromUtf8("load_layout"))
        self.btn_import = QtGui.QPushButton(self.tab_load)
        self.btn_import.setObjectName(_fromUtf8("btn_import"))
        self.load_layout.addWidget(self.btn_import, 0, 0, 1, 1)
        self.btn_dspk = QtGui.QPushButton(self.tab_load)
        self.btn_dspk.setObjectName(_fromUtf8("btn_dspk"))
        self.load_layout.addWidget(self.btn_dspk, 1, 0, 1, 1)
        self.lbl_wdir = QtGui.QLabel(self.tab_load)
        self.lbl_wdir.setObjectName(_fromUtf8("lbl_wdir"))
        self.load_layout.addWidget(self.lbl_wdir, 0, 1, 1, 1)
        self.lbl_dspk = QtGui.QLabel(self.tab_load)
        self.lbl_dspk.setObjectName(_fromUtf8("lbl_dspk"))
        self.load_layout.addWidget(self.lbl_dspk, 1, 1, 1, 1)
        self.load_layout.setColumnStretch(0, 1)
        self.load_layout.setColumnStretch(1, 4)
        self.gridLayout_2.addLayout(self.load_layout, 0, 0, 1, 1)
        self.proc_tabs.addTab(self.tab_load, _fromUtf8(""))
        self.tab_bkg = QtGui.QWidget()
        self.tab_bkg.setObjectName(_fromUtf8("tab_bkg"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_bkg)
        self.gridLayout_4.setMargin(11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.bkg_layout = QtGui.QGridLayout()
        self.bkg_layout.setMargin(11)
        self.bkg_layout.setSpacing(6)
        self.bkg_layout.setObjectName(_fromUtf8("bkg_layout"))
        self.chk_refine = QtGui.QCheckBox(self.tab_bkg)
        self.chk_refine.setObjectName(_fromUtf8("chk_refine"))
        self.bkg_layout.addWidget(self.chk_refine, 1, 0, 1, 1)
        self.drp_idanalyte = QtGui.QComboBox(self.tab_bkg)
        self.drp_idanalyte.setObjectName(_fromUtf8("drp_idanalyte"))
        self.bkg_layout.addWidget(self.drp_idanalyte, 0, 1, 1, 1)
        self.btn_bkgid = QtGui.QPushButton(self.tab_bkg)
        self.btn_bkgid.setObjectName(_fromUtf8("btn_bkgid"))
        self.bkg_layout.addWidget(self.btn_bkgid, 0, 0, 1, 1)
        self.lbl_ided = QtGui.QLabel(self.tab_bkg)
        self.lbl_ided.setObjectName(_fromUtf8("lbl_ided"))
        self.bkg_layout.addWidget(self.lbl_ided, 0, 2, 1, 1)
        self.bkg_layout.setColumnStretch(0, 1)
        self.bkg_layout.setColumnStretch(1, 1)
        self.bkg_layout.setColumnStretch(2, 3)
        self.gridLayout_4.addLayout(self.bkg_layout, 0, 1, 1, 1)
        self.proc_tabs.addTab(self.tab_bkg, _fromUtf8(""))
        self.tab_srm = QtGui.QWidget()
        self.tab_srm.setObjectName(_fromUtf8("tab_srm"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_srm)
        self.gridLayout_6.setMargin(11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.srm_layout = QtGui.QGridLayout()
        self.srm_layout.setMargin(11)
        self.srm_layout.setSpacing(6)
        self.srm_layout.setObjectName(_fromUtf8("srm_layout"))
        self.btn_srmdat = QtGui.QPushButton(self.tab_srm)
        self.btn_srmdat.setObjectName(_fromUtf8("btn_srmdat"))
        self.srm_layout.addWidget(self.btn_srmdat, 1, 0, 1, 1)
        self.btn_srmid = QtGui.QPushButton(self.tab_srm)
        self.btn_srmid.setObjectName(_fromUtf8("btn_srmid"))
        self.srm_layout.addWidget(self.btn_srmid, 0, 0, 1, 1)
        self.lbl_srmid = QtGui.QLabel(self.tab_srm)
        self.lbl_srmid.setObjectName(_fromUtf8("lbl_srmid"))
        self.srm_layout.addWidget(self.lbl_srmid, 0, 1, 1, 1)
        self.lbl_srmdat = QtGui.QLabel(self.tab_srm)
        self.lbl_srmdat.setObjectName(_fromUtf8("lbl_srmdat"))
        self.srm_layout.addWidget(self.lbl_srmdat, 1, 1, 1, 1)
        self.srm_layout.setColumnStretch(0, 1)
        self.srm_layout.setColumnStretch(1, 4)
        self.gridLayout_6.addLayout(self.srm_layout, 0, 0, 1, 1)
        self.proc_tabs.addTab(self.tab_srm, _fromUtf8(""))
        self.tab_stat = QtGui.QWidget()
        self.tab_stat.setObjectName(_fromUtf8("tab_stat"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_stat)
        self.gridLayout_8.setMargin(11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.stat_layout = QtGui.QGridLayout()
        self.stat_layout.setContentsMargins(0, 11, 11, 11)
        self.stat_layout.setSpacing(6)
        self.stat_layout.setObjectName(_fromUtf8("stat_layout"))
        self.chk_minmax = QtGui.QCheckBox(self.tab_stat)
        self.chk_minmax.setObjectName(_fromUtf8("chk_minmax"))
        self.stat_layout.addWidget(self.chk_minmax, 1, 1, 1, 1)
        self.chk_std = QtGui.QCheckBox(self.tab_stat)
        self.chk_std.setObjectName(_fromUtf8("chk_std"))
        self.stat_layout.addWidget(self.chk_std, 1, 0, 1, 1)
        self.chk_med = QtGui.QCheckBox(self.tab_stat)
        self.chk_med.setObjectName(_fromUtf8("chk_med"))
        self.stat_layout.addWidget(self.chk_med, 0, 1, 1, 1)
        self.chk_mean = QtGui.QCheckBox(self.tab_stat)
        self.chk_mean.setObjectName(_fromUtf8("chk_mean"))
        self.stat_layout.addWidget(self.chk_mean, 0, 0, 1, 1)
        self.percent_layout = QtGui.QHBoxLayout()
        self.percent_layout.setMargin(11)
        self.percent_layout.setSpacing(6)
        self.percent_layout.setObjectName(_fromUtf8("percent_layout"))
        self.chk_percent = QtGui.QCheckBox(self.tab_stat)
        self.chk_percent.setObjectName(_fromUtf8("chk_percent"))
        self.percent_layout.addWidget(self.chk_percent)
        self.drp_percent = QtGui.QComboBox(self.tab_stat)
        self.drp_percent.setIconSize(QtCore.QSize(12, 12))
        self.drp_percent.setObjectName(_fromUtf8("drp_percent"))
        self.percent_layout.addWidget(self.drp_percent)
        self.stat_layout.addLayout(self.percent_layout, 2, 1, 1, 1)
        self.chk_se = QtGui.QCheckBox(self.tab_stat)
        self.chk_se.setObjectName(_fromUtf8("chk_se"))
        self.stat_layout.addWidget(self.chk_se, 2, 0, 1, 1)
        self.btn_statcalc = QtGui.QPushButton(self.tab_stat)
        self.btn_statcalc.setObjectName(_fromUtf8("btn_statcalc"))
        self.stat_layout.addWidget(self.btn_statcalc, 2, 2, 1, 1)
        self.btn_statout = QtGui.QPushButton(self.tab_stat)
        self.btn_statout.setObjectName(_fromUtf8("btn_statout"))
        self.stat_layout.addWidget(self.btn_statout, 0, 2, 1, 1)
        self.lbl_statout = QtGui.QLabel(self.tab_stat)
        self.lbl_statout.setObjectName(_fromUtf8("lbl_statout"))
        self.stat_layout.addWidget(self.lbl_statout, 1, 2, 1, 1)
        self.gridLayout_8.addLayout(self.stat_layout, 3, 0, 1, 1)
        self.proc_tabs.addTab(self.tab_stat, _fromUtf8(""))
        self.topPanel.addWidget(self.proc_tabs)
        self.log = QtGui.QWidget(self.mainWindow)
        self.log.setObjectName(_fromUtf8("log"))
        self.topPanel.addWidget(self.log)
        self.topPanel.setStretch(0, 3)
        self.topPanel.setStretch(1, 2)
        self.verticalLayout.addLayout(self.topPanel)
        self.plotLayout = QtGui.QHBoxLayout()
        self.plotLayout.setMargin(11)
        self.plotLayout.setSpacing(6)
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.optionsPane = QtGui.QVBoxLayout()
        self.optionsPane.setMargin(11)
        self.optionsPane.setSpacing(6)
        self.optionsPane.setObjectName(_fromUtf8("optionsPane"))
        self.lbl_analytes = QtGui.QLabel(self.mainWindow)
        self.lbl_analytes.setScaledContents(False)
        self.lbl_analytes.setObjectName(_fromUtf8("lbl_analytes"))
        self.optionsPane.addWidget(self.lbl_analytes)
        self.checkBox = QtGui.QCheckBox(self.mainWindow)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.optionsPane.addWidget(self.checkBox)
        self.checkBox_3 = QtGui.QCheckBox(self.mainWindow)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.optionsPane.addWidget(self.checkBox_3)
        self.checkBox_2 = QtGui.QCheckBox(self.mainWindow)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.optionsPane.addWidget(self.checkBox_2)
        self.line = QtGui.QFrame(self.mainWindow)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.optionsPane.addWidget(self.line)
        self.lbl_samples = QtGui.QLabel(self.mainWindow)
        self.lbl_samples.setObjectName(_fromUtf8("lbl_samples"))
        self.optionsPane.addWidget(self.lbl_samples)
        self.listWidget = QtGui.QListWidget(self.mainWindow)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.optionsPane.addWidget(self.listWidget)
        self.line_2 = QtGui.QFrame(self.mainWindow)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.optionsPane.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.optionsPane.addItem(spacerItem)
        self.plotLayout.addLayout(self.optionsPane)
        self.plotPane = QtGui.QWidget(self.mainWindow)
        self.plotPane.setObjectName(_fromUtf8("plotPane"))
        self.plotLayout.addWidget(self.plotPane)
        self.plotLayout.setStretch(0, 1)
        self.plotLayout.setStretch(1, 6)
        self.verticalLayout.addLayout(self.plotLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        latools.setCentralWidget(self.mainWindow)
        self.menuBar = QtGui.QMenuBar(latools)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1221, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuProcess = QtGui.QMenu(self.menuBar)
        self.menuProcess.setObjectName(_fromUtf8("menuProcess"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        latools.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(latools)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        latools.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(latools)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        latools.setStatusBar(self.statusBar)
        self.actionLoad_Data_2 = QtGui.QAction(latools)
        self.actionLoad_Data_2.setObjectName(_fromUtf8("actionLoad_Data_2"))
        self.actionDespike = QtGui.QAction(latools)
        self.actionDespike.setObjectName(_fromUtf8("actionDespike"))
        self.actionIdentify_Background = QtGui.QAction(latools)
        self.actionIdentify_Background.setObjectName(_fromUtf8("actionIdentify_Background"))
        self.actionBackground_Correct = QtGui.QAction(latools)
        self.actionBackground_Correct.setObjectName(_fromUtf8("actionBackground_Correct"))
        self.actionRatio = QtGui.QAction(latools)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionIdentify_Standards = QtGui.QAction(latools)
        self.actionIdentify_Standards.setObjectName(_fromUtf8("actionIdentify_Standards"))
        self.actionApply_SRMs = QtGui.QAction(latools)
        self.actionApply_SRMs.setObjectName(_fromUtf8("actionApply_SRMs"))
        self.menuFile.addAction(self.actionLoad_Data_2)
        self.menuProcess.addAction(self.actionDespike)
        self.menuProcess.addAction(self.actionIdentify_Background)
        self.menuProcess.addAction(self.actionBackground_Correct)
        self.menuProcess.addAction(self.actionRatio)
        self.menuProcess.addAction(self.actionIdentify_Standards)
        self.menuProcess.addAction(self.actionApply_SRMs)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuProcess.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(latools)
        self.proc_tabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(latools)

    def retranslateUi(self, latools):
        latools.setWindowTitle(_translate("latools", "latools", None))
        self.btn_import.setText(_translate("latools", "Import Data", None))
        self.btn_dspk.setText(_translate("latools", "Despike Data", None))
        self.lbl_wdir.setText(_translate("latools", "TextLabel", None))
        self.lbl_dspk.setText(_translate("latools", "TextLabel", None))
        self.proc_tabs.setTabText(self.proc_tabs.indexOf(self.tab_load), _translate("latools", "Data Import", None))
        self.chk_refine.setText(_translate("latools", "Refine ID Mode", None))
        self.btn_bkgid.setText(_translate("latools", "Automatic ID", None))
        self.lbl_ided.setText(_translate("latools", "TextLabel", None))
        self.proc_tabs.setTabText(self.proc_tabs.indexOf(self.tab_bkg), _translate("latools", "Background Correction", None))
        self.btn_srmdat.setText(_translate("latools", "SRM Data File", None))
        self.btn_srmid.setText(_translate("latools", "Identify SRMs", None))
        self.lbl_srmid.setText(_translate("latools", "TextLabel", None))
        self.lbl_srmdat.setText(_translate("latools", "TextLabel", None))
        self.proc_tabs.setTabText(self.proc_tabs.indexOf(self.tab_srm), _translate("latools", "Calibration", None))
        self.chk_minmax.setText(_translate("latools", "Min, Max", None))
        self.chk_std.setText(_translate("latools", "Standard Deviation", None))
        self.chk_med.setText(_translate("latools", "Median", None))
        self.chk_mean.setText(_translate("latools", "Mean", None))
        self.chk_percent.setText(_translate("latools", "Percentile", None))
        self.chk_se.setText(_translate("latools", "Standard Error", None))
        self.btn_statcalc.setText(_translate("latools", "Calculate", None))
        self.btn_statout.setText(_translate("latools", "Output File", None))
        self.lbl_statout.setText(_translate("latools", "TextLabel", None))
        self.proc_tabs.setTabText(self.proc_tabs.indexOf(self.tab_stat), _translate("latools", "Statistics", None))
        self.lbl_analytes.setText(_translate("latools", "Analytes", None))
        self.checkBox.setText(_translate("latools", "A", None))
        self.checkBox_3.setText(_translate("latools", "B", None))
        self.checkBox_2.setText(_translate("latools", "C", None))
        self.lbl_samples.setText(_translate("latools", "Samples", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("latools", "Sample 1", None))
        item = self.listWidget.item(1)
        item.setText(_translate("latools", "Sample 2", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("latools", "File", None))
        self.menuEdit.setTitle(_translate("latools", "Edit", None))
        self.menuProcess.setTitle(_translate("latools", "Process", None))
        self.menuHelp.setTitle(_translate("latools", "Help", None))
        self.actionLoad_Data_2.setText(_translate("latools", "Load Data", None))
        self.actionDespike.setText(_translate("latools", "Despike", None))
        self.actionIdentify_Background.setText(_translate("latools", "Identify Background", None))
        self.actionBackground_Correct.setText(_translate("latools", "Background Correct", None))
        self.actionRatio.setText(_translate("latools", "Calculate Ratios", None))
        self.actionIdentify_Standards.setText(_translate("latools", "Identify Standards", None))
        self.actionApply_SRMs.setText(_translate("latools", "Apply SRMs", None))

