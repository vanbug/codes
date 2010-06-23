# Frame and Window is excatly same thing
import wx
from testF import facefeed
# Creates a basic frame for testing
#app=wx.App()
#win=wx.Frame(None)
#win.Show()
#app.MainLoop()

class gui1(wx.Frame):
# We made a constructor so that this code pops up whenever the user runs the program, a method can be made so that it can be called by invoking some response from the user, pressing a key or button.
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'My gui1',size=(400,320))
		# Making a panel which holds the properties of buttons and menu bars
		panel1=wx.Panel(self)
		button1=wx.Button(panel1,label='YO',pos=(130,10),size=(60,60)) # This creates a button structure
		button2=wx.Button(panel1,label='testF')
		# Binding an event to the button to execute an action
		self.Bind(wx.EVT_BUTTON,self.closebutton,button1) #CloseButton function called which closes the window
	#	self.Bind(wx.EVT_CLOSE,self.closewindow)		 #CloseWindow closes the window when 'x' is clicked on top
		self.Bind(wx.EVT_BUTTON,self.testFF,button2)
	def closebutton(self,event):
		self.Close(True)
	#def closewindow(self,event):
	#	self.Destroy()
	def testFF(self,event):
		feeds=facefeed()
		print feeds
# Every python gui needs 2 things :
#	application object : which runs the program
#	frame object  	   : which displays the program
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=gui1(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
