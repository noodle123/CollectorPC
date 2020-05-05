import serial
import os,sys
import threading
import wx
import frame
from datetime import datetime

# Implementing UI
class frameUI( frame.UI ):
	def __init__( self, parent ):
		frame.UI.__init__( self, parent )
	
	# Handlers for UI events.
	def buttonStartOnClick( self, event ):
		# TODO: Implement buttonStartOnClick
		initListHead(self)
		openSerial()
		startTimer()
	
	def buttonSaveOnClick( self, event ):
		# TODO: Implement buttonSaveOnClick
		addListLine(self)
	
	def buttonCloseOnClick( self, event ):
		# TODO: Implement buttonCloseOnClick
		quit()

def initListHead(self):
        self.m_listCtrlData.InsertColumn(0, 'name', wx.LIST_FORMAT_RIGHT, 100)
        self.m_listCtrlData.InsertColumn(1, 'runs', wx.LIST_FORMAT_RIGHT, 100)
        self.m_listCtrlData.InsertColumn(2, 'wkts', wx.LIST_FORMAT_RIGHT, 100)

def addListLine(self):
        index = self.m_listCtrlData.InsertItem(0, "one");
        self.m_listCtrlData.SetItem(index, 1, "two")
        self.m_listCtrlData.SetItem(index, 2, "three")

serial=serial.Serial("COM2",19200,timeout=3600)
def openSerial():
        # ser=serial.Serial("COM2",19200,timeout=3600)
        th=threading.Thread(target=rcv_data)
        th.setDaemon(True)
        th.start()
        if serial.isOpen():
                print("open succeed >","COM2")
        else:
                print("open failed >","COM2")

recv_count=0
def rcv_data():
        while True:
                rcv_data=serial.read(9).hex()
                print("recv one data frame")
                # self.recv_count+=1

def startTimer():
        timer=threading.Timer(1,startTimer)
        timer.start()
        send()

send_count=0
def send():
        send_data=[0x01,0x03,0x00,0x00,0x00,0x02,0xC4,0x0B]
        serial.write(send_data)
        # self.send_count+=1
        
def main():
    app=wx.App()
    main_frm=frameUI(None)
    main_frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
