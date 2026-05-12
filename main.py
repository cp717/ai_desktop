import sys
from PyQt5.QtWidgets import QApplication
from ui.pet_window import DesktopPet

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 启动桌面宠物应用
    pet = DesktopPet()
    pet.show()
    
    sys.exit(app.exec_())
