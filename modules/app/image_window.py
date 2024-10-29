import customtkinter as ctk
from .main_screen import main_window


class ImageClient(ctk.CTkFrame):

    def __init__(self, child_master: object, **kwargs):
        ctk.CTkFrame.__init__(
            self, 
            master = child_master,
            border_width= 2,
            width= 1000,
            height= 617,
            border_color= '#808080',
            **kwargs
        )
        self.place(x= 0, y= 0)
        
window_image = ImageClient(child_master= main_window)