import os
import tkinter
import tkinter.messagebox
import customtkinter as ck

ck.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ck.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App1(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("GISAT Plus v1.0.0.0")
        self.label_radio_group = ck.CTkLabel(master=self, text="Welcome to GISAT Plus",
                                             font=("Century Gothic", 25, "bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky="")
        self.label_radio_group = ck.CTkLabel(master=self, text="Select the list you want to work with.")
        self.label_radio_group.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky="")

        def selected(*args):
            # exec(open('GISAT_Plus.py').read())
            #wel = App1(self)
            #radio_sel = getattr(wel, "radio_var")
            radio_sel = self.radio_var.get()
            print(radio_sel)
            self.destroy()
            #os.system('python GISAT_Plus.py')




         # create radiobutton frame
        self.radiobutton_frame = ck.CTkFrame(self)
        self.radiobutton_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.radio_var = tkinter.IntVar()
        # The buttons
        self.radio_button_1 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=1, text="Treatment Line List", command=selected)
        self.radio_button_1.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        self.radio_button_2 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=2, text="HTS Line List", command=selected)
        self.radio_button_2.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.radio_button_3 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=3, text="Full Pharmacy Complement", command=selected)
        self.radio_button_3.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.radio_button_4 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=4, text="PMTCT Line List", command=selected)
        self.radio_button_4.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.radio_button_5 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=5, text="Last 5 Pharmacy", command=selected)
        self.radio_button_5.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        #####
        self.radio_button_6 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=6, text="EID Line List", command=selected)
        self.radio_button_6.grid(row=0, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_7 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=7, text="AHD Line List", command=selected)
        self.radio_button_7.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_8 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=8, text="LIMS_EMR Daily Report", command=selected)
        self.radio_button_8.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_9 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                value=9, text="HIV-COVID_19 Line List", command=selected)
        self.radio_button_9.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        self.radio_button_10 = ck.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                 value=10, text="OTZ Line list", command=selected)
        self.radio_button_10.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # radio_sel = self.radio_var.get()




if __name__ == "__main__":
    app = App1()
    app.mainloop()
