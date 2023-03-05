import tkinter
from tkinter import *
from tkinter import ttk, Tk, filedialog
from tkinter.filedialog import askopenfile
import os
import datetime
import pandas as pd
from sqlalchemy import create_engine, event
from sqlalchemy.exc import SQLAlchemyError
import customtkinter
from tkcalendar import Calendar, DateEntry
import my_list
import mysql.connector
import tkinter.messagebox
import sys

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Admin123",
    database="validation_linelist"
)

my_cursor = mydb.cursor(buffered=True)

def selected_ip():
    # clicked.get() == 'IP':
    my_cursor.execute("SELECT DISTINCT(`IP`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_state():
    # clicked.get() == 'State':
    my_cursor.execute("SELECT DISTINCT(`State`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_surgecommand1():
    # clicked.get() == 'SurgeCommand':
    my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_lga():
    my_cursor.execute("SELECT DISTINCT(`lga`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1
# filename = "text_images/GISAT_ndr_nmrs_concurrence1.png"
# with Image.open(filename) as img:
# img.load()
# image1 = Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png")
# test = ImageTk.PhotoImage(image1)

# Define Image
# bg = PhotoImage(file='text_images/GISAT_ndr_nmrs_concurrence1.png')
# my_image = customtkinter.CTkImage(light_image=Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png"),
# dark_image=Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png"),
# size=(30, 30))
# add_import_image = ImageTk.PhotoImage(Image.open("text_images/Import.png").resize((20, 20), Image.LANCZOS))
# add_evaluate_image = ImageTk.PhotoImage(Image.open("text_images/Evaluate.png").resize((20, 20), Image.ANTIALIAS))
# add_export_image = ImageTk.PhotoImage(Image.open("text_images/Export.png").resize((20, 20), Image.ANTIALIAS))

class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("NDR-NMRS CONCURRENCE.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.iconbitmap("images/cihp.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.start_concur = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Start Concurrence",
                                                   text_font=("Roboto Medium", 16))  # font name and size in px
        self.start_concur.grid(row=1, column=0, pady=10, padx=10)

        self.import_list_button = customtkinter.CTkButton(master=self.frame_left,
                                                          # image=add_import_image,
                                                          text="Import Line List", width=220, height=40,
                                                          text_font=("Roboto Medium", 10),
                                                          command=self.button_event)
        self.import_list_button.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Evaluate Concurrence", width=220, height=40,
                                                text_font=("Roboto Medium", 10),
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Export Concurrence Analysis", width=220, height=40,
                                                text_font=("Roboto Medium", 10),
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Export Concurrence Analysis", width=220, height=40,
                                                text_font=("Roboto Medium", 10),
                                                command=self.button_event)
        self.button_3.grid(row=5, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Export Mismatch List", width=220, height=40,
                                                text_font=("Roboto Medium", 10),
                                                command=self.button_event)
        self.button_4.grid(row=6, column=0, pady=1, padx=20)

        self.combobox_mismatch = customtkinter.CTkComboBox(master=self.frame_left,
                                                           values=["List of Invalid IDs", "IDs Not on NDR",
                                                                   "Tx_Curr Not "
                                                                   "Processed ("
                                                                   "NDR)",
                                                                   "Tx_New Not Processed (NDR)",
                                                                   "Tx_PVLS Not Processed ("
                                                                   "NDR)", "ART Start Date "
                                                                           "Non-Concurrence "
                                                                           "List",
                                                                   "Last Pickup Date Non-Concurrence List",
                                                                   "Viral Load Date "
                                                                   "Non-Concurrence "
                                                                   "List",
                                                                   "Current Status Non-Concurrence List"])
        self.combobox_mismatch.grid(row=7, column=0, pady=1, padx=20, sticky="we")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=(0, 0), padx=10, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=(0, 0), padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP ,\n" +
                                                        "CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP,\n" +
                                                        "CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP ",
                                                   height=200,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Select Parameters")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        clicked = StringVar()
        clicked.set("Select Level of Merging")

        select_ip = selected_ip()
        select_state = selected_state()
        select_surgecom = selected_surgecommand1()
        select_lga = selected_lga()

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=select_ip)
        self.combobox_1.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_2 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=select_lga)
        self.combobox_2.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_3 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["FY23 Q1", "FY23 Q2", "FY23 Q3", "FY23 Q4", "FY24 Q1", "FY24 Q2", "FY24 Q3", "FY24 Q4"])
        self.combobox_3.grid(row=3, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_4 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.combobox_4.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_5 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_5.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_6 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_6.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="CTkButton",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.combobox_mismatch.set("Select mismatch list for export")
        self.optionmenu_1.set("Dark")
        # self.button_3.configure(state="disabled", text="Evaluate Concurrence Analysis")
        self.combobox_1.set("State")
        self.combobox_2.set("LGA")
        self.combobox_3.set("FY/Quarter")
        self.combobox_4.set("Reporting Month")
        self.combobox_5.set("Reporting Year")
        self.combobox_6.set("Date of NDR List")
        # self.radio_button_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
