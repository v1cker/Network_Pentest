# -*- coding: utf-8 -*-  
import win32gui
import win32ui
import win32con
import win32api
 
# ��ȡ����
hdesktop = win32gui.GetDesktopWindow()
 
# �ֱ�����Ӧ
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
 
# �����豸������
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)
 
# ����һ���ڴ��豸������
mem_dc = img_dc.CreateCompatibleDC()
 
# ����λͼ����
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)
 
# ��ͼ���ڴ��豸������
mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
 
# ����ͼ���浽�ļ���
screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')
 
# �ڴ��ͷ�
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())