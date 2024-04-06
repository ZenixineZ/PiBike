#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:11:10 2024

@author: zenix
"""

from PyQt5 import QWidgets
from PyQt5.QWidgets import QApplication, QMainWindow
import sys

class PiBike(QMainWindow):
    def __init__(self):
        pass
        



def window(w, h):
    app = QApplication(sys.argv)
    pibike = PiBike()
    pibike.show()
    pibike.setGeometry(0, 0, w, h)
    
    

    
