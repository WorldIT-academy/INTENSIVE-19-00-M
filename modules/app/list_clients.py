import customtkinter as ctk
from .main_screen import main_window

class Frame_Clients(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self, 
            master = child_master,
            border_width= 2,
            width= 250,
            height= 600,
            border_color= '#808080',
            fg_color= '#191919',
            **kwargs
        )
        self.place(x= 1000, y= 0)

clients_list = Frame_Clients(child_master= main_window)
        