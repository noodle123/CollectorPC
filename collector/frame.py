# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class UI
###########################################################################

class UI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"collector", pos = wx.DefaultPosition, size = wx.Size( 756,561 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlData = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer1.Add( self.m_listCtrlData, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_buttonStart, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_buttonSave, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_buttonClose, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonStart.Bind( wx.EVT_BUTTON, self.buttonStartOnClick )
		self.m_buttonSave.Bind( wx.EVT_BUTTON, self.buttonSaveOnClick )
		self.m_buttonClose.Bind( wx.EVT_BUTTON, self.buttonCloseOnClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonStartOnClick( self, event ):
		event.Skip()
	
	def buttonSaveOnClick( self, event ):
		event.Skip()
	
	def buttonCloseOnClick( self, event ):
		event.Skip()
	

