from msilib.schema import Font
from PyQt5 import QtCore,QtWidgets,QtGui
import sys

values = []
carbon = 0
result = 0
result_1 = 0

class WhatToDo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.what_to_do()
    
    def update_(self):
        self.label_1.setText("""   Carbon dioxide and other greenhouse gasses have existed in 
our atmosphere since atmosphere formation, and they have made 
the world livable by keeping the heat inside with greenhouse 
gasses. However, with the start of industrialization, an increase 
in these gasses has occurred more than it should have been.

   Most of the activities we are doing regularly cause carbon 
emissions. In order to make our world livable, we have to give 
up some of our activities. According to the World Meteorological 
Organization (WMO) report, by 2025, there is a 40% chance that
the world will warm 1.5°C above pre-industrial levels. If we continue 
to warm our world at this rate, we are very close to entering the 
threshold of no return. 

   To get rid of the effect of {} kg of damage 
you have done to the world, you need to plant {} trees in total. 
On average, a tree absorbs 730 kg of carbon during its lifetime.

""".format(round(result),round(result/730)))
    
    def what_to_do(self):
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",20)
        font_3 = QtGui.QFont("Assets\\gilroy-regular.ttf",15)
        font_4 = QtGui.QFont("Assets\\gilroy-regular.ttf",13)
        
        self.title = QtWidgets.QLabel(self)
        self.title.setText("What To Do??")
        self.title.setFont(font)
        self.title.move(230,10)
        
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font_4)
        self.label_1.move(10,70)

        self.start_again =QtWidgets.QPushButton(self)
        self.start_again.setText("Start Again")
        self.start_again.resize(120,40)
        self.start_again.move(550,430)
        self.start_again.setStyleSheet("background-color : rgb(223,108,29); color : rgb(243,184,144)")
        self.start_again.setFont(font_3)
        self.start_again.clicked.connect(self.start_again_)
    
    def start_again_(self):
        values.clear()
        result = 0
        result_1 = 0
        carbon = 0
        stack.setCurrentIndex(0)

class PageResultsSad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_results()
    
    def guncelle(self):
        self.result_label.setText("""Your carbon emission total 
is {} kg. The 
target number of the
world is 2000 kg.
BAD RESULT!
""".format(int(round(result,0))))
        
        global result_1
        result_1 = result 
    
    def page_results(self):
        self.sad = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\Results_Sad.png')
        self.sad.setPixmap(self.pixmap)
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",20)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",20)
        font_3 = QtGui.QFont("Assets\\gilroy-regular.ttf",15)
        font_3.setUnderline(True)
        font_3.setItalic(True)      

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.move(150,100)
        self.result_label.setFont(font) 

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setText("See What You Can Do -->")
        self.go_new.setStyleSheet("border : 1px rgb(220,239,242)")
        self.go_new.setFont(font_3)
        self.go_new.move(250,340)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.yapan = QtWidgets.QLabel(self)
        self.yapan.setText("""Beşiktaş Anatolian High School
Mertcan BİLEK""")
        self.yapan.setFont(font_2)
        self.yapan.move(180,400)  

        self.go_new.clicked.connect(self.new_page_final)

    def new_page_final(self):
        stack.setCurrentIndex(8)

   
class PageResults(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_results()

    def _update(self):
        self.label.setText("""Congratulations!! Your carbon 
emission is total {} kg. 
The target of the 
world is 2000 kg.

We trust you!""".format(int(round(result,0))))
   
    def page_results(self):
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",20)       
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",25)       
        font_3 = QtGui.QFont("Assets\\gilroy-regular.ttf",15)
        font_3.setUnderline(True)
        font_3.setItalic(True)         
        
        self.good = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\Results.png')
        self.good.setPixmap(self.pixmap)
        self.label = QtWidgets.QLabel(self)
        self.label.setFont(font)
        self.label.move(150,120)

        self.yapan = QtWidgets.QLabel(self)
        self.yapan.setText("""Beşiktaş Anatolian High School
          Mertcan BİLEK""")
        self.yapan.setFont(font_2)
        self.yapan.move(110,400)

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setText("See What You Can Do -->")
        self.go_new.setStyleSheet("border : 1px rgb(220,239,242)")
        self.go_new.setFont(font_3)
        self.go_new.move(420,250)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.go_new.clicked.connect(self.new_page_final)

    def new_page_final(self):
        stack.setCurrentIndex(8)

class Page_5(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_5()

    def page_5(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("Assets\\gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",20)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_3 = QtGui.QFont("Assets\\gilroy-regular.ttf",17)
        font_4 = QtGui.QFont("Assets\\gilroy-regular.ttf",14)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Nutrition and Food")
        self.label_1.move(210,10)
        self.label_1.setFont(font_2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("(Per Week)")
        self.label_2.move(540,20)
        self.label_2.setFont(font_4)
              
        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)  
        self.line.resize(2,400)
        self.line.move(330,80)
        self.line.setStyleSheet("border : 2px solid black")

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(15, 270, 315, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setStyleSheet("border : 2px solid black")
        
        self.meat_and_dairy_products_label = QtWidgets.QLabel(self)
        self.meat_and_dairy_products_label.setText("Meat and Dairy Products")
        self.meat_and_dairy_products_label.setFont(font)
        self.meat_and_dairy_products_label.move(360,85)
        
        self.meat = QtWidgets.QLabel(self)
        self.meat.move(360,145)
        self.meat.setText("Meat --->")
        self.meat.setFont(font_3)
        
        self.meat_box = QtWidgets.QLineEdit(self)
        self.meat_box.setFont(font_4)
        self.meat_box.move(465,145)
        self.meat_box.resize(90,30)
        self.meat_box.setValidator(QtGui.QDoubleValidator())
        self.meat_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.meat_box.setPlaceholderText("kg")

        self.milk = QtWidgets.QLabel(self)
        self.milk.setText("Milk  --->")
        self.milk.setFont(font_3)
        self.milk.move(360,195)

        self.milk_box = QtWidgets.QLineEdit(self)
        self.milk_box.setFont(font_4)
        self.milk_box.move(465,195)
        self.milk_box.resize(90,30)
        self.milk_box.setValidator(QtGui.QDoubleValidator())
        self.milk_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.milk_box.setPlaceholderText("lt")

        self.egg = QtWidgets.QLabel(self)
        self.egg.move(360,245)
        self.egg.setText("Egg  --->")
        self.egg.setFont(font_3)

        self.egg_box = QtWidgets.QLineEdit(self)
        self.egg_box.setFont(font_4)
        self.egg_box.move(465,245)
        self.egg_box.resize(90,30)
        self.egg_box.setValidator(QtGui.QDoubleValidator())
        self.egg_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.egg_box.setPlaceholderText("pcs")

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.white_meat = QtWidgets.QLabel(self)
        self.white_meat.setText("White Meat --->")
        self.white_meat.move(360,295)
        self.white_meat.setFont(font_3)

        self.white_meat_box = QtWidgets.QLineEdit(self)
        self.white_meat_box.setFont(font_4)
        self.white_meat_box.move(535,295)
        self.white_meat_box.resize(90,30)
        self.white_meat_box.setValidator(QtGui.QDoubleValidator())
        self.white_meat_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.white_meat_box.setPlaceholderText("kg")
        
        self.cheese = QtWidgets.QLabel(self)
        self.cheese.setText("Cheese --->")
        self.cheese.move(360,345)
        self.cheese.setFont(font_3)

        self.cheese_box = QtWidgets.QLineEdit(self)
        self.cheese_box.setFont(font_4)
        self.cheese_box.move(490,345)
        self.cheese_box.resize(90,30)
        self.cheese_box.setValidator(QtGui.QDoubleValidator())
        self.cheese_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.cheese_box.setPlaceholderText("kg")
        
        self.turkey = QtWidgets.QLabel(self)
        self.turkey.setText("Turkey --->")
        self.turkey.move(360,395)
        self.turkey.setFont(font_3)
        
        self.turkey_box = QtWidgets.QLineEdit(self)
        self.turkey_box.setFont(font_4)
        self.turkey_box.move(490,395)
        self.turkey_box.resize(90,30)
        self.turkey_box.setValidator(QtGui.QDoubleValidator())
        self.turkey_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.turkey_box.setPlaceholderText("kg")

        self.yogurt = QtWidgets.QLabel(self)
        self.yogurt.setText("Yogurt --->")
        self.yogurt.move(360,445)
        self.yogurt.setFont(font_3)

        self.yogurt_box = QtWidgets.QLineEdit(self)
        self.yogurt_box.setFont(font_4)
        self.yogurt_box.move(490,445)
        self.yogurt_box.resize(90,30)
        self.yogurt_box.setValidator(QtGui.QDoubleValidator())
        self.yogurt_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.yogurt_box.setPlaceholderText("kg")

        self.orange = QtWidgets.QLabel(self)
        self.orange.setText("Orange --->")
        self.orange.setFont(font_3)
        self.orange.move(20,145)

        self.orange_box = QtWidgets.QLineEdit(self)
        self.orange_box.move(150,145)
        self.orange_box.resize(90,30)
        self.orange_box.setFont(font_4)
        self.orange_box.setValidator(QtGui.QDoubleValidator())
        self.orange_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.orange_box.setPlaceholderText("kg") 

        self.patato = QtWidgets.QLabel(self)
        self.patato.setText("Patato --->")
        self.patato.setFont(font_3)
        self.patato.move(20,185)
        
        self.patato_box = QtWidgets.QLineEdit(self)
        self.patato_box.move(150,185)
        self.patato_box.resize(90,30)
        self.patato_box.setFont(font_4)
        self.patato_box.setValidator(QtGui.QDoubleValidator())
        self.patato_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.patato_box.setPlaceholderText("kg") 
        
        self.tomato = QtWidgets.QLabel(self)
        self.tomato.setText("Tomato --->")
        self.tomato.setFont(font_3)
        self.tomato.move(20,225)
        
        self.tomato_box = QtWidgets.QLineEdit(self)
        self.tomato_box.move(150,225)
        self.tomato_box.resize(90,30)
        self.tomato_box.setFont(font_4)
        self.tomato_box.setValidator(QtGui.QDoubleValidator())
        self.tomato_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.tomato_box.setPlaceholderText("kg") 

        self.fruits_label = QtWidgets.QLabel(self)
        self.fruits_label.setText("Fruits and Vegetables")
        self.fruits_label.setFont(font) 
        self.fruits_label.move(20,85)
        
        self.others_label = QtWidgets.QLabel(self)
        self.others_label.setText("Others")
        self.others_label.setFont(font) 
        self.others_label.move(20,275)

        self.bread = QtWidgets.QLabel(self)
        self.bread.setText("Bread --->")
        self.bread.setFont(font_3)
        self.bread.move(20,335)
        
        self.bread_box = QtWidgets.QLineEdit(self)
        self.bread_box.move(150,335)
        self.bread_box.resize(90,30)
        self.bread_box.setFont(font_4)
        self.bread_box.setValidator(QtGui.QDoubleValidator())
        self.bread_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.bread_box.setPlaceholderText("pcs") 
        
        self.rice = QtWidgets.QLabel(self)
        self.rice.setText("Rice --->")
        self.rice.setFont(font_3)
        self.rice.move(20,375)             
        
        self.rice_box = QtWidgets.QLineEdit(self)
        self.rice_box.move(150,375)
        self.rice_box.resize(90,30)
        self.rice_box.setFont(font_4)
        self.rice_box.setValidator(QtGui.QDoubleValidator())
        self.rice_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.rice_box.setPlaceholderText("kg") 
        
        self.lentil = QtWidgets.QLabel(self)
        self.lentil.setText("Lentil --->")
        self.lentil.setFont(font_3)
        self.lentil.move(20,415)             
        
        self.lentil_box = QtWidgets.QLineEdit(self)
        self.lentil_box.move(150,415)
        self.lentil_box.resize(90,30)
        self.lentil_box.setFont(font_4)
        self.lentil_box.setValidator(QtGui.QDoubleValidator())
        self.lentil_box.setStyleSheet("background-color : white; border : 1px solid gray")
        self.lentil_box.setPlaceholderText("kg") 

        self.go_new.clicked.connect(self.page_results)

    def page_results(self):
        try:
            values.append(float(self.orange_box.text()))
            values.append(float(self.patato_box.text()))
            values.append(float(self.tomato_box.text()))
            values.append(float(self.bread_box.text()))
            values.append(float(self.rice_box.text()))
            values.append(float(self.lentil_box.text()))
            values.append(float(self.meat_box.text()))
            values.append(float(self.milk_box.text()))
            values.append(float(self.egg_box.text()))
            values.append(float(self.white_meat_box.text()))
            values.append(float(self.cheese_box.text()))
            values.append(float(self.turkey_box.text()))
            values.append(float(self.yogurt_box.text()))
    
            carbon = (values[1]*0.43*12) + (values[2]*2.93*12) + (values[3]*2.1857*12) + (values[4]*8.9*3.6) + (values[5]*5.3*3.6) + (values[6]*6*3.6) + (values[7]*237) + (values[8]*516) + (values[9]*987) + (values[12] * 1 * 52) + (values[13] * 2.9 *52) + (values[14] * 1.1 * 52) + (values[15] * 1 * 52) + (values[16] * 2.7 *52) + (values[17] * 0.9 * 52) + (values[18] * 33 * 52) + (values[19] * 8 * 52) + (values[20] * 0.3 * 52) + (values[21] * 8 *52) + (values[22] * 13.5 * 52) + (values[23] * 9.9 * 52) + (values[24] * 2.2 *52) 
    
            if values[10] == 0:
                carbon += 69
            if values[10] == 1:
                carbon += 41
            if values[10] == 2:
                carbon += 28
            if values[10] == 3:
                pass
            else:
                pass
    
            if values[11] == 0:
                pass
            if values[11] == 1:
                carbon += 29
            if values[11] == 2:
                carbon += 59
            else:
                pass 
    
            global result 
            result = carbon/values[0]
            page_results_sad.guncelle()
            page_results._update()
        except:
            for i in range(13):
                values.append(0)  
                print(values) 
            
        carbon = (values[1]*0.43*12) + (values[2]*2.93*12) + (values[3]*2.1857*12) + (values[4]*8.9*3.6) + (values[5]*5.3*3.6) + (values[6]*6*3.6) + (values[7]*237) + (values[8]*516) + (values[9]*987) + (values[12] * 1 * 52) + (values[13] * 2.9 *52) + (values[14] * 1.1 * 52) + (values[15] * 1 * 52) + (values[16] * 2.7 *52) + (values[17] * 0.9 * 52) + (values[18] * 33 * 52) + (values[19] * 8 * 52) + (values[20] * 0.3 * 52) + (values[21] * 8 *52) + (values[22] * 13.5 * 52) + (values[23] * 9.9 * 52) + (values[24] * 2.2 *52) 

        if values[10] == 0:
            carbon += 69
        if values[10] == 1:
            carbon += 41
        if values[10] == 2:
            carbon += 28
        if values[10] == 3:
            pass
        else:
            pass

        if values[11] == 0:
            pass
        if values[11] == 1:
            carbon += 29
        if values[11] == 2:
            carbon += 59
        else:
            pass 

        result = carbon/values[0]
        page_results_sad.guncelle()
        page_results._update()
        final_.update_()
        
        if int(result) <= int(2000):
            stack.setCurrentIndex(stack.currentIndex() + 1)           
        if int(result) > int(2000):
            stack.setCurrentIndex(stack.currentIndex() + 2)
        
        self.orange_box.clear()
        self.tomato_box.clear()
        self.patato_box.clear()
        self.bread_box.clear()
        self.rice_box.clear()
        self.lentil_box.clear()
        self.meat_box.clear()
        self.milk_box.clear()
        self.white_meat_box.clear()
        self.cheese_box.clear()
        self.turkey_box.clear()
        self.yogurt_box.clear()
        self.egg_box.clear()

class Page_4(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_4()
   
    def page_4(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("Assets\\gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",17)

        self.bal = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\image.png')
        self.bal.setPixmap(self.pixmap)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font)
        self.label_1.move(10,25)
        self.label_1.setText("LIFE STYLE")

        self.recycle_label = QtWidgets.QLabel(self)
        self.recycle_label.setFont(font_2)
        self.recycle_label.setText("""How much of your garbage is recycled ?""")
        self.recycle_label.move(12,95)

        self.recycle_chocie_1 = QtWidgets.QRadioButton(self)
        self.recycle_chocie_1.setText("No Recycle")
        self.recycle_chocie_2 = QtWidgets.QRadioButton(self)
        self.recycle_chocie_2.setText("1/3")
        self.recycle_chocie_3 = QtWidgets.QRadioButton(self)
        self.recycle_chocie_3.setText("2/3")
        self.recycle_chocie_4 = QtWidgets.QRadioButton(self)
        self.recycle_chocie_4.setText("3/3")
        
        self.recycle_chocie_1.move(12,140)
        self.recycle_chocie_2.move(12,160)
        self.recycle_chocie_3.move(12,180)
        self.recycle_chocie_4.move(12,200)
        
        self.group_1 = QtWidgets.QButtonGroup(self)
        self.group_1.addButton(self.recycle_chocie_1)
        self.group_1.addButton(self.recycle_chocie_2)
        self.group_1.addButton(self.recycle_chocie_3)
        self.group_1.addButton(self.recycle_chocie_4)
       
        self.packet_label = QtWidgets.QLabel(self)
        self.packet_label.setFont(font_2)
        self.packet_label.setText("""How many of your products are packed ?""")
        self.packet_label.move(12,240)

        self.packet_chocie_1 = QtWidgets.QRadioButton(self)
        self.packet_chocie_1.setText("Nearly No")
        self.packet_chocie_2 = QtWidgets.QRadioButton(self)
        self.packet_chocie_2.setText("1/2")
        self.packet_chocie_3 = QtWidgets.QRadioButton(self)
        self.packet_chocie_3.setText("Packed Products Only")
        
        self.packet_chocie_1.move(12,285)
        self.packet_chocie_2.move(12,305)
        self.packet_chocie_3.move(12,325)
       
        self.group_2 = QtWidgets.QButtonGroup(self)
        self.group_2.addButton(self.packet_chocie_1)
        self.group_2.addButton(self.packet_chocie_2)
        self.group_2.addButton(self.packet_chocie_3)

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.go_new.clicked.connect(self.new_page_5)

    def new_page_5(self):
        if self.recycle_chocie_1.isChecked():
            values.append(0)
        if self.recycle_chocie_2.isChecked():
            values.append(1)
        if self.recycle_chocie_3.isChecked():
            values.append(2)
        if self.recycle_chocie_4.isChecked():
            values.append(3)   
        else:
            values.append(0)
        if self.packet_chocie_1.isChecked():
            values.append(0)
        if self.packet_chocie_2.isChecked():
            values.append(1)
        if self.packet_chocie_3.isChecked():
            values.append(2)
        else:
            values.append(2)
        
        stack.setCurrentIndex(stack.currentIndex() + 1)  

class Page_3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_3()
   
    def page_3(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("Assets\\gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",17)

        self.bal = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\image.png')
        self.bal.setPixmap(self.pixmap)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font)
        self.label_1.move(10,25)
        self.label_1.setText("TRANSPORTATİON")

        self.short_label = QtWidgets.QLabel(self)
        self.short_label.setFont(font_2)
        self.short_label.setText("""How many times a year do you take a 
short-haul plane ?""")
        self.short_label.move(12,95)

        self.short_edit = QtWidgets.QLineEdit(self)
        self.short_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.short_edit.move(12,160)
        self.short_edit.setFont(QtGui.QFont("gilroy-regular",12))
        self.short_edit.resize(90,30)
        self.short_edit.setValidator(QtGui.QDoubleValidator())

        self.medium_label = QtWidgets.QLabel(self)
        self.medium_label.setFont(font_2)
        self.medium_label.setText("""How many times a year do you take a 
medium-haul plane ?""")
        self.medium_label.move(12,195)

        self.medium_edit = QtWidgets.QLineEdit(self)
        self.medium_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.medium_edit.move(12,260)
        self.medium_edit.resize(90,30)
        self.medium_edit.setValidator(QtGui.QDoubleValidator())
        self.medium_edit.setFont(QtGui.QFont("gilroy-regular",12))
        
        self.long_label = QtWidgets.QLabel(self)
        self.long_label.setFont(font_2)
        self.long_label.setText("""How many times a year do you take a 
long-haul plane ?""")
        self.long_label.move(12,295)
        
        self.long_edit = QtWidgets.QLineEdit(self)
        self.long_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.long_edit.move(12,355)
        self.long_edit.resize(90,30)
        self.long_edit.setValidator(QtGui.QDoubleValidator())
        self.long_edit.setFont(QtGui.QFont("gilroy-regular",12))

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.go_new.clicked.connect(self.new_page_4)       
        self.show()
        
    def new_page_4(self):        
        try:
            values.append(float(self.short_edit.text()))
            values.append(float(self.medium_edit.text()))
            values.append(float(self.long_edit.text()))
            stack.setCurrentIndex(stack.currentIndex() + 1)    
        except:
            values.append(0)
            values.append(0)
            values.append(0)
            stack.setCurrentIndex(stack.currentIndex() + 1)    
        self.long_edit.clear()
        self.short_edit.clear()
        self.medium_edit.clear()              

class Page_2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_2()
   
    def page_2(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("Assets\\gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",17)

        self.bal = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\image.png')
        self.bal.setPixmap(self.pixmap)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font)
        self.label_1.move(10,25)
        self.label_1.setText("TRANSPORTATİON")

        self.bus_label = QtWidgets.QLabel(self)
        self.bus_label.setFont(font_2)
        self.bus_label.setText("""How many kilometers do you 
take bus per day?""")
        self.bus_label.move(12,95)

        self.bus_edit = QtWidgets.QLineEdit(self)
        self.bus_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.bus_edit.move(12,160)
        self.bus_edit.setFont(QtGui.QFont("gilroy-regular",12))
        self.bus_edit.resize(90,30)
        self.bus_edit.setValidator(QtGui.QDoubleValidator())

        self.metro_label = QtWidgets.QLabel(self)
        self.metro_label.setFont(font_2)
        self.metro_label.setText("""How many kilometers do you 
take metro per day?""")
        self.metro_label.move(12,195)

        self.metro_edit = QtWidgets.QLineEdit(self)
        self.metro_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.metro_edit.move(12,260)
        self.metro_edit.resize(90,30)
        self.metro_edit.setValidator(QtGui.QDoubleValidator())
        self.metro_edit.setFont(QtGui.QFont("gilroy-regular",12))

        self.personal_label = QtWidgets.QLabel(self)
        self.personal_label.setFont(font_2)
        self.personal_label.setText("""How many kilometers do you 
take train per day?""")
        self.personal_label.move(12,295)
        
        self.personal_edit = QtWidgets.QLineEdit(self)
        self.personal_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.personal_edit.move(12,355)
        self.personal_edit.resize(90,30)
        self.personal_edit.setValidator(QtGui.QDoubleValidator())
        self.personal_edit.setFont(QtGui.QFont("gilroy-regular",12))

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.go_new.clicked.connect(self.new_page_3)       
        self.show()
        
    def new_page_3(self):        
        try:   
            values.append(float(self.bus_edit.text()))
            values.append(float(self.metro_edit.text()))
            values.append(float(self.personal_edit.text()))
            stack.setCurrentIndex(stack.currentIndex() + 1)    
        except ValueError:
            values.append(0)
            values.append(0)
            values.append(0)
            stack.setCurrentIndex(stack.currentIndex() + 1)   
        self.metro_edit.clear()
        self.bus_edit.clear()
        self.personal_edit.clear()   

class Page_1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_1()
   
    def page_1(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("Assets\\gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",17)

        self.bal = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\image.png')
        self.bal.setPixmap(self.pixmap)
        
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font)
        self.label_1.move(10,25)
        self.label_1.setText("ENERGY USAGE")

        self.electric_label = QtWidgets.QLabel(self)
        self.electric_label.setFont(font_2)
        self.electric_label.setText("""How many Kwh is your electricity 
consumption per month ?""")
        self.electric_label.move(12,95)

        self.electric_edit = QtWidgets.QLineEdit(self)
        self.electric_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.electric_edit.move(12,160)
        self.electric_edit.setFont(QtGui.QFont("gilroy-regular",12))
        self.electric_edit.resize(90,30)
        self.electric_edit.setValidator(QtGui.QDoubleValidator())

        self.coal_label = QtWidgets.QLabel(self)
        self.coal_label.setFont(font_2)
        self.coal_label.setText("""How many kg is your coal
consumption per month ?""")
        self.coal_label.move(12,195)

        self.coal_edit = QtWidgets.QLineEdit(self)
        self.coal_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.coal_edit.move(12,260)
        self.coal_edit.resize(90,30)
        self.coal_edit.setValidator(QtGui.QDoubleValidator())
        self.coal_edit.setFont(QtGui.QFont("gilroy-regular",12))

        self.natural_gas_label = QtWidgets.QLabel(self)
        self.natural_gas_label.setFont(font_2)
        self.natural_gas_label.setText("""How many m³ is your natural gas
consumption per month ?""")
        self.natural_gas_label.move(12,295)
        
        self.natural_gas_edit = QtWidgets.QLineEdit(self)
        self.natural_gas_edit.setStyleSheet("background-color : white; border : 1px solid gray")
        self.natural_gas_edit.move(12,355)
        self.natural_gas_edit.resize(90,30)
        self.natural_gas_edit.setValidator(QtGui.QDoubleValidator())
        self.natural_gas_edit.setFont(QtGui.QFont("gilroy-regular",12))
        
        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.go_new.clicked.connect(self.new_page_2)
        self.show()
    
    def new_page_2(self):        
        try:    
            stack.setCurrentIndex(stack.currentIndex() + 1)    
            values.append(float(self.electric_edit.text()))
            values.append(float(self.coal_edit.text()))
            values.append(float(self.natural_gas_edit.text()))    
        
        except ValueError:
            stack.setCurrentIndex(2)    
            values.append(0)
            values.append(0)
            values.append(0)
        self.electric_edit.clear()
        self.coal_edit.clear()
        self.natural_gas_edit.clear()

class Start(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.start()
   
    def start(self):
        height = 500
        width = 700
        self.setFixedSize(width,height)
        self.setStyleSheet("background-color : rgb(220,239,242)")
        QtGui.QFontDatabase.addApplicationFont("gilroy-regular.ttf")
        font = QtGui.QFont("Assets\\gilroy-regular.ttf",25)
        font_2 = QtGui.QFont("Assets\\gilroy-regular.ttf",22)
        
        self.bal = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('Assets\\image.png')
        self.bal.setPixmap(self.pixmap)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setFont(font_2)
        self.label_1.move(10,140)
        self.label_1.setText("""How many people do you 
live with ? """)
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Advistor Teacher :")
        self.label_2.move(20,350)
        self.label_2.setFont(font)

        self.danısman_isim = QtWidgets.QLabel(self)
        self.danısman_isim.setText("Şeyma ATEŞ")
        self.danısman_isim.setFont(font_2)
        self.danısman_isim.move(20,400)

        self.title = QtWidgets.QLabel(self)
        self.title.setText("Carbon Footprint Calculator")
        self.title.move(120,20)
        self.title.setFont(font)

        self.people = QtWidgets.QLineEdit(self)
        self.people.resize(120,40)
        self.people.setStyleSheet("background-color : rgb(255,255,255);border: 1px solid gray")
        self.people.move(10,220)
        self.people.setFont(QtGui.QFont("gilroy-regular",15))
        self.people.setValidator(QtGui.QDoubleValidator())

        self.go_new = QtWidgets.QPushButton(self)
        self.go_new.setStyleSheet("background-image : url(icon.png);border: 1px rgb(220,239,242)")
        self.go_new.setIcon(QtGui.QIcon("Assets\\icon.png"))
        self.go_new.setIconSize(QtCore.QSize(60,60))
        self.go_new.resize(60,60)
        self.go_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_new.move(630,420)

        self.go_new.clicked.connect(self.start_test)

        self.show()
    
    def start_test(self):
        try:
            values.append(float(self.people.text()))
            stack.setCurrentIndex(stack.currentIndex() + 1)       
        except ValueError:
            values.append(1)
            stack.setCurrentIndex(stack.currentIndex() + 1)
        self.people.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    stack = QtWidgets.QStackedWidget()
    page_results = PageResults()
    page_results_sad = PageResultsSad()
    window = Start()
    final_ = WhatToDo()
    page_1 = Page_1()
    page_2 = Page_2()
    page_3 = Page_3()
    page_4 = Page_4()
    page_5 = Page_5()
    stack.addWidget(window) # index 0
    stack.addWidget(page_1) # index 1
    stack.addWidget(page_2) # index 2
    stack.addWidget(page_3) # index 3
    stack.addWidget(page_4) # index 4
    stack.addWidget(page_5) # index 5
    stack.addWidget(page_results) # index 6
    stack.addWidget(page_results_sad) # index 7
    stack.addWidget(final_) # index 8
    stack.setFixedSize(700,500)
    stack.setWindowTitle("Carbon Footprint Calculator")      
    stack.setStyleSheet("background-color : rgb(220,239,242)")
    stack.setWindowIcon(QtGui.QIcon("Assets\\footprint.png"))
    stack.show()
    sys.exit(app.exec_())