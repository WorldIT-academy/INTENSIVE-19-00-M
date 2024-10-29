import customtkinter as ctk 
from .main_screen import main_window

class InfoWindow(ctk.CTkTextbox):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkTextbox.__init__(
            self,
            master= child_master,
            border_width= 2,
            width= 1000,
            height= 215,
            border_color= '#808080',
            fg_color= '#191919',
            **kwargs
        )
        self.place(x= 0, y= 617)

window_info = InfoWindow(child_master= main_window)