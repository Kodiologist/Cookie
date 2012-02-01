import wx, numpy
from psychopy.gui import Dlg
from psychopy.logging import debug, warning

class DlgSansCancel(Dlg):
    "A Dlg without a Cancel button."

    def show(self):
        # Initially copied from psychopy.gui (which is copyright
        # 2011 Jonathan Peirce and available under GPL v3).
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        OK = wx.Button(self, wx.ID_OK, " OK ")
        OK.SetDefault()
        buttons.Add(OK)
        self.sizer.Add(buttons,1,flag=wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM,border=5)

        self.SetSizerAndFit(self.sizer)
        self.ShowModal()

        self.data=[]
        #get data from input fields
        for n in range(len(self.inputFields)):
            thisName = self.inputFieldNames[n]
            thisVal = self.inputFields[n].GetValue()
            thisType= self.inputFieldTypes[n]
            #try to handle different types of input from strings
            debug("%s: %s" %(self.inputFieldNames[n], unicode(thisVal)))
            if thisType in [tuple,list,float,int]:
                #probably a tuple or list
                exec("self.data.append("+thisVal+")")#evaluate it
            elif thisType==numpy.ndarray:
                exec("self.data.append(numpy.array("+thisVal+"))")
            elif thisType in [str,unicode,bool]:
                self.data.append(thisVal)
            else:
                warning('unknown type:'+self.inputFieldNames[n])
                self.data.append(thisVal)
        self.OK=True
        self.Destroy()
