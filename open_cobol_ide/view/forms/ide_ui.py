# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/OpenCobolIDE/forms/ide.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageHome = QtWidgets.QWidget()
        self.pageHome.setObjectName("pageHome")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageHome)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widgetHome = QtWidgets.QWidget(self.pageHome)
        self.widgetHome.setObjectName("widgetHome")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetHome)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widgetHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.btNewFile = QtWidgets.QPushButton(self.widgetHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btNewFile.sizePolicy().hasHeightForWidth())
        self.btNewFile.setSizePolicy(sizePolicy)
        self.btNewFile.setMinimumSize(QtCore.QSize(200, 0))
        self.btNewFile.setObjectName("btNewFile")
        self.horizontalLayout_8.addWidget(self.btNewFile)
        self.btOpenFile = QtWidgets.QPushButton(self.widgetHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btOpenFile.sizePolicy().hasHeightForWidth())
        self.btOpenFile.setSizePolicy(sizePolicy)
        self.btOpenFile.setMinimumSize(QtCore.QSize(200, 0))
        self.btOpenFile.setStyleSheet("")
        self.btOpenFile.setObjectName("btOpenFile")
        self.horizontalLayout_8.addWidget(self.btOpenFile)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.frameRecents = QtWidgets.QFrame(self.widgetHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameRecents.sizePolicy().hasHeightForWidth())
        self.frameRecents.setSizePolicy(sizePolicy)
        self.frameRecents.setMinimumSize(QtCore.QSize(406, 0))
        self.frameRecents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameRecents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRecents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRecents.setObjectName("frameRecents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameRecents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelRecents = QtWidgets.QLabel(self.frameRecents)
        self.labelRecents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelRecents.setObjectName("labelRecents")
        self.verticalLayout_4.addWidget(self.labelRecents)
        self.listWidgetRecents = RecentFilesListWidget(self.frameRecents)
        self.listWidgetRecents.setMinimumSize(QtCore.QSize(400, 0))
        self.listWidgetRecents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidgetRecents.setObjectName("listWidgetRecents")
        self.verticalLayout_4.addWidget(self.listWidgetRecents)
        self.horizontalLayout_5.addWidget(self.frameRecents)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btPreferences = QtWidgets.QPushButton(self.widgetHome)
        self.btPreferences.setMinimumSize(QtCore.QSize(200, 0))
        self.btPreferences.setObjectName("btPreferences")
        self.verticalLayout_7.addWidget(self.btPreferences)
        self.btAbout = QtWidgets.QPushButton(self.widgetHome)
        self.btAbout.setMinimumSize(QtCore.QSize(200, 0))
        self.btAbout.setObjectName("btAbout")
        self.verticalLayout_7.addWidget(self.btAbout)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.verticalLayout_5.addWidget(self.widgetHome)
        self.stackedWidget.addWidget(self.pageHome)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidgetEditors = TabWidget(self.page_2)
        self.tabWidgetEditors.setOrientation(QtCore.Qt.Horizontal)
        self.tabWidgetEditors.setObjectName("tabWidgetEditors")
        self.gridLayout_2.addWidget(self.tabWidgetEditors, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarFile = QtWidgets.QToolBar(MainWindow)
        self.toolBarFile.setObjectName("toolBarFile")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.toolBarCOBOL = QtWidgets.QToolBar(MainWindow)
        self.toolBarCOBOL.setObjectName("toolBarCOBOL")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCOBOL)
        self.dockWidgetLogs = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetLogs.setObjectName("dockWidgetLogs")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetLogs = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidgetLogs.setObjectName("tabWidgetLogs")
        self.tabCompiler = QtWidgets.QWidget()
        self.tabCompiler.setObjectName("tabCompiler")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabCompiler)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEditCompilerOutput = QtWidgets.QTextEdit(self.tabCompiler)
        self.textEditCompilerOutput.setReadOnly(True)
        self.textEditCompilerOutput.setObjectName("textEditCompilerOutput")
        self.gridLayout_6.addWidget(self.textEditCompilerOutput, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetLogs.addTab(self.tabCompiler, icon1, "")
        self.tabCompiler1 = QtWidgets.QWidget()
        self.tabCompiler1.setObjectName("tabCompiler1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabCompiler1)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.errorsTable = ErrorsTable(self.tabCompiler1)
        self.errorsTable.setMinimumSize(QtCore.QSize(0, 0))
        self.errorsTable.setObjectName("errorsTable")
        self.errorsTable.setColumnCount(5)
        self.errorsTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.errorsTable, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("emblem-important")
        self.tabWidgetLogs.addTab(self.tabCompiler1, icon, "")
        self.tabProgramOutput = QtWidgets.QWidget()
        self.tabProgramOutput.setObjectName("tabProgramOutput")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabProgramOutput)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.consoleOutput = InteractiveConsole(self.tabProgramOutput)
        self.consoleOutput.setObjectName("consoleOutput")
        self.gridLayout_5.addWidget(self.consoleOutput, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.tabWidgetLogs.addTab(self.tabProgramOutput, icon, "")
        self.gridLayout_3.addWidget(self.tabWidgetLogs, 1, 0, 1, 1)
        self.dockWidgetLogs.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetLogs)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.mnuActiveEditor = QtWidgets.QMenu(self.menuEdit)
        icon = QtGui.QIcon.fromTheme("accessories-text-editor")
        self.mnuActiveEditor.setIcon(icon)
        self.mnuActiveEditor.setObjectName("mnuActiveEditor")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuWindows = QtWidgets.QMenu(self.menuView)
        icon = QtGui.QIcon.fromTheme("window")
        self.menuWindows.setIcon(icon)
        self.menuWindows.setObjectName("menuWindows")
        self.menuCobol = QtWidgets.QMenu(self.menuBar)
        self.menuCobol.setObjectName("menuCobol")
        self.menuProgramType = QtWidgets.QMenu(self.menuCobol)
        self.menuProgramType.setObjectName("menuProgramType")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.dockWidgetNavPanel = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetNavPanel.setMinimumSize(QtCore.QSize(102, 168))
        self.dockWidgetNavPanel.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetNavPanel.setObjectName("dockWidgetNavPanel")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.btNavLock = QtWidgets.QToolButton(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btNavLock.sizePolicy().hasHeightForWidth())
        self.btNavLock.setSizePolicy(sizePolicy)
        self.btNavLock.setText("")
        icon = QtGui.QIcon.fromTheme("system-lock-screen")
        self.btNavLock.setIcon(icon)
        self.btNavLock.setIconSize(QtCore.QSize(16, 16))
        self.btNavLock.setCheckable(True)
        self.btNavLock.setChecked(False)
        self.btNavLock.setObjectName("btNavLock")
        self.horizontalLayout_4.addWidget(self.btNavLock)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.twNavigation = OutlineTreeWidget(self.dockWidgetContents_2)
        self.twNavigation.setObjectName("twNavigation")
        self.twNavigation.headerItem().setText(0, "1")
        self.twNavigation.header().setVisible(False)
        self.verticalLayout_6.addWidget(self.twNavigation)
        self.dockWidgetNavPanel.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetNavPanel)
        self.dockWidgetOffsets = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetOffsets.setMinimumSize(QtCore.QSize(310, 114))
        self.dockWidgetOffsets.setObjectName("dockWidgetOffsets")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_8.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidgetOffsets = PicOffsetsTable(self.dockWidgetContents_3)
        self.tableWidgetOffsets.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidgetOffsets.setDragDropOverwriteMode(False)
        self.tableWidgetOffsets.setShowGrid(True)
        self.tableWidgetOffsets.setObjectName("tableWidgetOffsets")
        self.tableWidgetOffsets.setColumnCount(4)
        self.tableWidgetOffsets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(3, item)
        self.tableWidgetOffsets.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidgetOffsets.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetOffsets.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetOffsets.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.tableWidgetOffsets, 0, 0, 1, 1)
        self.dockWidgetOffsets.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetOffsets)
        self.dockWidgetFileSystem = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetFileSystem.setMinimumSize(QtCore.QSize(96, 151))
        self.dockWidgetFileSystem.setObjectName("dockWidgetFileSystem")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.bt_fs_up = QtWidgets.QToolButton(self.dockWidgetContents_4)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.bt_fs_up.setIcon(icon)
        self.bt_fs_up.setObjectName("bt_fs_up")
        self.horizontalLayout_2.addWidget(self.bt_fs_up)
        self.btFSLock = QtWidgets.QToolButton(self.dockWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btFSLock.sizePolicy().hasHeightForWidth())
        self.btFSLock.setSizePolicy(sizePolicy)
        self.btFSLock.setText("")
        icon = QtGui.QIcon.fromTheme("system-lock-screen")
        self.btFSLock.setIcon(icon)
        self.btFSLock.setIconSize(QtCore.QSize(16, 16))
        self.btFSLock.setCheckable(True)
        self.btFSLock.setChecked(False)
        self.btFSLock.setObjectName("btFSLock")
        self.horizontalLayout_2.addWidget(self.btFSLock)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tvFileSystem = FileSystemTreeView(self.dockWidgetContents_4)
        self.tvFileSystem.setObjectName("tvFileSystem")
        self.verticalLayout.addWidget(self.tvFileSystem)
        self.dockWidgetFileSystem.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetFileSystem)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIconVisibleInMenu(True)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionFullscreen = QtWidgets.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setIconVisibleInMenu(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionClear.setObjectName("actionClear")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setIconVisibleInMenu(True)
        self.actionHelp.setObjectName("actionHelp")
        self.actionProgram = QtWidgets.QAction(MainWindow)
        self.actionProgram.setCheckable(True)
        self.actionProgram.setChecked(True)
        self.actionProgram.setObjectName("actionProgram")
        self.actionSubprogram = QtWidgets.QAction(MainWindow)
        self.actionSubprogram.setCheckable(True)
        self.actionSubprogram.setObjectName("actionSubprogram")
        self.actionCompile = QtWidgets.QAction(MainWindow)
        self.actionCompile.setIconVisibleInMenu(True)
        self.actionCompile.setObjectName("actionCompile")
        self.actionCancel = QtWidgets.QAction(MainWindow)
        self.actionCancel.setObjectName("actionCancel")
        self.actionReport_a_bug = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("tools-report-bug")
        self.actionReport_a_bug.setIcon(icon)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionRestore_factory_defaults = QtWidgets.QAction(MainWindow)
        self.actionRestore_factory_defaults.setObjectName("actionRestore_factory_defaults")
        self.actionExport_preferences = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-export")
        self.actionExport_preferences.setIcon(icon)
        self.actionExport_preferences.setObjectName("actionExport_preferences")
        self.actionImport_preferences = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-import")
        self.actionImport_preferences.setIcon(icon)
        self.actionImport_preferences.setObjectName("actionImport_preferences")
        self.actionClean = QtWidgets.QAction(MainWindow)
        self.actionClean.setObjectName("actionClean")
        self.actionRebuild = QtWidgets.QAction(MainWindow)
        self.actionRebuild.setObjectName("actionRebuild")
        self.actionEnableLinter = QtWidgets.QAction(MainWindow)
        self.actionEnableLinter.setCheckable(True)
        self.actionEnableLinter.setChecked(True)
        icon = QtGui.QIcon.fromTheme("dialog-error")
        self.actionEnableLinter.setIcon(icon)
        self.actionEnableLinter.setObjectName("actionEnableLinter")
        self.dockWidgetNavPanel.raise_()
        self.toolBarFile.addAction(self.actionNew)
        self.toolBarFile.addAction(self.actionOpen)
        self.toolBarFile.addSeparator()
        self.toolBarFile.addAction(self.actionSave)
        self.toolBarFile.addAction(self.actionSaveAs)
        self.toolBarCOBOL.addAction(self.actionClean)
        self.toolBarCOBOL.addAction(self.actionRebuild)
        self.toolBarCOBOL.addAction(self.actionRun)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_preferences)
        self.menuFile.addAction(self.actionExport_preferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.mnuActiveEditor.addSeparator()
        self.menuEdit.addAction(self.mnuActiveEditor.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuView.addAction(self.menuWindows.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFullscreen)
        self.menuProgramType.addAction(self.actionProgram)
        self.menuProgramType.addAction(self.actionSubprogram)
        self.menuCobol.addAction(self.menuProgramType.menuAction())
        self.menuCobol.addSeparator()
        self.menuCobol.addAction(self.actionCompile)
        self.menuCobol.addAction(self.actionClean)
        self.menuCobol.addAction(self.actionRebuild)
        self.menuCobol.addAction(self.actionRun)
        self.menuCobol.addSeparator()
        self.menuCobol.addAction(self.actionCancel)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionAbout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionReport_a_bug)
        self.menu.addSeparator()
        self.menu.addAction(self.actionRestore_factory_defaults)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCobol.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidgetLogs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenCobolIDE"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/ide-icons/rc/silex-192x192.png\"/></p><p align=\"center\"><span style=\" font-size:20pt;\">Welcome to OpenCobolIDE</span></p><p align=\"center\">Click on <span style=\" font-weight:600; font-style:italic;\">New </span>or <span style=\" font-weight:600; font-style:italic;\">Open </span>to get started!</p></body></html>"))
        self.btNewFile.setToolTip(_translate("MainWindow", "Create a new file"))
        self.btNewFile.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.btNewFile.setText(_translate("MainWindow", "New file"))
        self.btOpenFile.setText(_translate("MainWindow", "Open file"))
        self.labelRecents.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Recent files</span></p></body></html>"))
        self.listWidgetRecents.setToolTip(_translate("MainWindow", "Recent files"))
        self.listWidgetRecents.setStatusTip(_translate("MainWindow", "Recent files"))
        self.btPreferences.setText(_translate("MainWindow", "Preferences"))
        self.btAbout.setText(_translate("MainWindow", "About"))
        self.toolBarFile.setWindowTitle(_translate("MainWindow", "File toolbar"))
        self.toolBarCOBOL.setWindowTitle(_translate("MainWindow", "COBOL toolbar"))
        self.dockWidgetLogs.setWindowTitle(_translate("MainWindow", "&Logs"))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabCompiler), _translate("MainWindow", "Compiler"))
        self.errorsTable.setStatusTip(_translate("MainWindow", "The list of errors found in your program"))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabCompiler1), _translate("MainWindow", "Issues"))
        self.tabWidgetLogs.setTabToolTip(self.tabWidgetLogs.indexOf(self.tabCompiler1), _translate("MainWindow", "Show compiler log"))
        self.consoleOutput.setToolTip(_translate("MainWindow", "Program output"))
        self.consoleOutput.setStatusTip(_translate("MainWindow", "Program output"))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabProgramOutput), _translate("MainWindow", "Output"))
        self.menuFile.setTitle(_translate("MainWindow", "F&ile"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.mnuActiveEditor.setToolTip(_translate("MainWindow", "Active editor context menu"))
        self.mnuActiveEditor.setStatusTip(_translate("MainWindow", "Active editor context menu"))
        self.mnuActiveEditor.setTitle(_translate("MainWindow", "&Active editor"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuWindows.setTitle(_translate("MainWindow", "&Windows"))
        self.menuCobol.setTitle(_translate("MainWindow", "&COBOL"))
        self.menuProgramType.setTitle(_translate("MainWindow", "&Program type"))
        self.menu.setTitle(_translate("MainWindow", "&?"))
        self.dockWidgetNavPanel.setWindowTitle(_translate("MainWindow", "&Navigation"))
        self.btNavLock.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lock/Unlock navigation panel </p><p>If unlocked, the selected item will be syncronised with the cursor position.</p></body></html>"))
        self.twNavigation.setToolTip(_translate("MainWindow", "Show the current editor structure"))
        self.twNavigation.setStatusTip(_translate("MainWindow", "Show the current editor structure"))
        self.dockWidgetOffsets.setWindowTitle(_translate("MainWindow", "Offset calc&ulator"))
        self.tableWidgetOffsets.setToolTip(_translate("MainWindow", "Show PIC fields offsets"))
        self.tableWidgetOffsets.setStatusTip(_translate("MainWindow", "Show PIC fields offsets"))
        self.tableWidgetOffsets.setSortingEnabled(True)
        item = self.tableWidgetOffsets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Level"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Offset"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PIC"))
        self.dockWidgetFileSystem.setWindowTitle(_translate("MainWindow", "File s&ystem"))
        self.bt_fs_up.setToolTip(_translate("MainWindow", "Go up"))
        self.bt_fs_up.setText(_translate("MainWindow", "..."))
        self.btFSLock.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Lock</span> current file path to prevent the view from changing when the current editor changes.</p></body></html>"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Exit application"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Exit application"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionRun.setText(_translate("MainWindow", "&Run"))
        self.actionRun.setToolTip(_translate("MainWindow", "Run the current editor program"))
        self.actionRun.setStatusTip(_translate("MainWindow", "Run the current editor program"))
        self.actionRun.setShortcut(_translate("MainWindow", "F5"))
        self.actionAbout.setText(_translate("MainWindow", "&About OpenCobolIDE"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About OpenCobolIDE"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About OpenCobolIDE"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save the current editor"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the current editor"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "Sa&ve as"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "Save the current editor as"))
        self.actionSaveAs.setStatusTip(_translate("MainWindow", "Save the current editor as"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionFullscreen.setText(_translate("MainWindow", "&Fullscreen"))
        self.actionFullscreen.setToolTip(_translate("MainWindow", "Toggle fullscreen"))
        self.actionFullscreen.setStatusTip(_translate("MainWindow", "Toggle fullscreen"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New file"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClear.setText(_translate("MainWindow", "Clear list"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear list of recent files"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))
        self.actionPreferences.setToolTip(_translate("MainWindow", "Edit the application settings"))
        self.actionPreferences.setStatusTip(_translate("MainWindow", "Edit the application settings"))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionHelp.setToolTip(_translate("MainWindow", "Show help content"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Show help content"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionProgram.setText(_translate("MainWindow", "&Executable"))
        self.actionProgram.setToolTip(_translate("MainWindow", "Make an executable program (*.exe)"))
        self.actionProgram.setStatusTip(_translate("MainWindow", "Make an executable program (*.exe)"))
        self.actionSubprogram.setText(_translate("MainWindow", "&Module"))
        self.actionSubprogram.setToolTip(_translate("MainWindow", "Make a module program (*.dll)"))
        self.actionSubprogram.setStatusTip(_translate("MainWindow", "Make a module program (*.dll)"))
        self.actionCompile.setText(_translate("MainWindow", "&Compile"))
        self.actionCompile.setToolTip(_translate("MainWindow", "Compile the current editor"))
        self.actionCompile.setStatusTip(_translate("MainWindow", "Compile the current editor"))
        self.actionCompile.setShortcut(_translate("MainWindow", "F8"))
        self.actionCancel.setText(_translate("MainWindow", "Ca&ncel"))
        self.actionCancel.setToolTip(_translate("MainWindow", "Cancel the current operation (compile or run)"))
        self.actionCancel.setStatusTip(_translate("MainWindow", "Cancel the current operation (compile or run)"))
        self.actionReport_a_bug.setText(_translate("MainWindow", "&Report a bug"))
        self.actionRestore_factory_defaults.setText(_translate("MainWindow", "Restore &factory defaults"))
        self.actionExport_preferences.setText(_translate("MainWindow", "&Export preferences"))
        self.actionImport_preferences.setText(_translate("MainWindow", "&Import preferences"))
        self.actionClean.setText(_translate("MainWindow", "C&lean"))
        self.actionClean.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.actionRebuild.setText(_translate("MainWindow", "R&ebuild"))
        self.actionRebuild.setShortcut(_translate("MainWindow", "Shift+F8"))
        self.actionEnableLinter.setText(_translate("MainWindow", "Enable linter"))
        self.actionEnableLinter.setToolTip(_translate("MainWindow", "Enable/disable linter (background check)\n"
""))
        self.actionEnableLinter.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))

from open_cobol_ide.view.widgets import RecentFilesListWidget, TabWidget
from pyqode.cobol.widgets import OutlineTreeWidget, PicOffsetsTable
from pyqode.core.widgets import ErrorsTable, FileSystemTreeView, InteractiveConsole
from . import ide_rc