import customtkinter as ctk

WIDTH = 1280
HEIGHT = 830

main_window = ctk.CTk(fg_color= '#2b2b2b')
#
width_screen = main_window.winfo_screenwidth()
#
height_screen = main_window.winfo_screenheight()
# print(width_screen, '\n', height_screen)
x_cor = (width_screen // 2) - (WIDTH // 2) 
y_cor = (height_screen // 2) - (HEIGHT // 2)
#
main_window.geometry(f'{WIDTH}x{HEIGHT}+{x_cor}+{y_cor}')
