#!/usr/bin/env python
# coding: utf-8
#game site:
#http://wap.jue-huo.com/app/html/game/1to50/1to50.html
import pyautogui as ag
def autoGame():
    try:
        for i in range(1,51):
            A=ag.locateCenterOnScreen(str(i)+'.png',confidence=0.92)
            ag.moveTo(A,duration=0.002)
            ag.click(A)
    except: return False
    return True
