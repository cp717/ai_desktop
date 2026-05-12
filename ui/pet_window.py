import sys
from PyQt5.QtWidgets import QWidget, QLabel, QMenu, QAction, QApplication, QInputDialog, QMessageBox
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtCore import Qt, QPoint
from agent.brain import pet_agent

class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.drag_position = QPoint()
        
    def init_ui(self):
        # 1. 设置无边框和透明背景
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(False)
        
        # 2. 设置宠物图像 (这里使用 QLabel 加载 GIF)
        self.image_label = QLabel(self)
        self.movie = QMovie("assets/idle.gif")
        
        # 如果找不到本地动图，设置一个占位色块
        if not self.movie.isValid():
            self.image_label.setText("(0 v 0)\n我是一只宠物\n(请在assets放入idle.gif)")
            self.image_label.setStyleSheet("background-color: rgba(255, 200, 200, 200); border-radius: 10px; padding: 20px;")
            self.image_label.adjustSize()
        else:
            self.image_label.setMovie(self.movie)
            self.movie.start()
            
        self.resize(self.image_label.width(), self.image_label.height())
        
        # 初始化位置 (屏幕右下角附近)
        self.move(1500, 800)

    # --- 鼠标拖拽逻辑 ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.drag_position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    # --- 右键菜单与交互 ---
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        
        chat_action = QAction("和它聊天", self)
        chat_action.triggered.connect(self.open_chat)
        
        quit_action = QAction("退出", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        
        menu.addAction(chat_action)
        menu.addAction(quit_action)
        menu.exec_(QCursor.pos())
        
    def open_chat(self):
        text, ok = QInputDialog.getText(self, '与宠物互动', '你想对我说什么？:')
        if ok and text:
            # 调用 Agent 大脑
            response = pet_agent.chat(text)
            QMessageBox.information(self, "宠物回复", response)
