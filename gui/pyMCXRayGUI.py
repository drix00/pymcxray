#!/usr/bin/env python
"""
.. py:currentmodule:: gui.pyMCXRayGUI
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Main GUI for program MCXRay.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.
import wx

# Local modules.

# Project modules

# Globals and constants variables.

class MCXRayFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name="MCXRayFrame"):
        super(MCXRayFrame, self).__init__(parent, id, title, pos, size, style, name)

        # Attributes
        self.panel = wx.Panel(self)

class MCXRayGUI(wx.App):
    def OnInit(self):
        self.frame = MCXRayFrame(None, title="The Main Frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

def run():
    app = MCXRayGUI(redirect=False)
    app.MainLoop()

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=run)
