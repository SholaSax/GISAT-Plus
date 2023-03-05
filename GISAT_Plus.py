import tkinter
from tkinter import *
from tkinter import Tk, filedialog, messagebox, ttk
from tkinter.filedialog import askopenfile
import os
# import datetime
import pandas as pd
from sqlalchemy import create_engine, event
# from sqlalchemy.exc import SQLAlchemyError
import customtkinter as ck
from tkcalendar import Calendar, DateEntry
# import my_list
import mysql.connector
import sys
from datetime import datetime, timedelta, date, time
import threading
import subprocess
# import time
# import threading
from PIL import ImageTk, Image
import sql_scripts_all
import mysql_script
import welcome


def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)


ck.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ck.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
reset_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "reset.png")),
                          dark_image=Image.open(os.path.join(image_path, "reset.png")), size=(20, 20))

app = ck.CTk()
app.geometry("450x985")
app.title("GISAT Plus v1.0.0.0")
app.iconbitmap("images/cihp.ico")

frame_1 = ck.CTkFrame(master=app)
frame_1.pack(pady=(20, 10), padx=20, fill="both", expand=True)

gplus = ImageTk.PhotoImage(file="images/gisat_plus.png")

gplus_ = Label(master=frame_1, image=gplus, bd=0)  # , background="#333333")
gplus_.pack(pady=2, padx=10)

# script_box.bind("<<ComboboxSelected>>", all_export_boxes)

'''
def list_options():
    global radio_sel
    # linelist_gen_buttonppp.configure(command=threading.Thread(target=list_options).start)
    topwindow2 = ck.CTkToplevel()
    topwindow2.geometry("460x300")
    topwindow2.title("GISAT Plus v1.0.0.0")
    label_radio_group = ck.CTkLabel(topwindow2, text="Welcome to GISAT Plus",
                                    font=("Century Gothic", 25, "bold"))
    label_radio_group.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky="")
    label_radio_group = ck.CTkLabel(topwindow2, text="Select the list you want to work with.")
    label_radio_group.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky="")

    def selected(*args):
        # exec(open('GISAT_Plus.py').read())
        # wel = App1(self)
        # radio_sel = getattr(wel, "radio_var")
        radio_sel = radio_var.get()
        if radio_sel == 1:
            run_main_app()
            return "Treatment Line List"
            topwindow2.destroy()
        elif radio_sel == 2:
            run_main_app()
            print("HTS Line List")
        elif radio_sel == 3:
            run_main_app()
            print("Full Pharmacy Complement")
        elif radio_sel == 4:
            print("PMTCT Line List")
        elif radio_sel == 5:
            print("Last 5 Pharmacy")
        elif radio_sel == 6:
            print("EID Line List")
        elif radio_sel == 7:
            print("AHD Line List")
        elif radio_sel == 8:
            print("LIMS_EMR Daily Report")
        elif radio_sel == 9:
            print("HIV-COVID_19 Line List")
        elif radio_sel == 10:
            print("OTZ Line list")
        else:
            pass
        # print(radio_sel)
        topwindow2.destroy()
        # os.system('python GISAT_Plus.py')

    # create radiobutton frame
    radiobutton_frame = ck.CTkFrame(topwindow2)
    radiobutton_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
    radio_var = tkinter.IntVar()
    # The buttons
    radio_button_1 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=1, text="Treatment Line List")
    radio_button_1.grid(row=0, column=0, pady=10, padx=20, sticky="w")
    radio_button_2 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=2, text="HTS Line List")
    radio_button_2.grid(row=1, column=0, pady=10, padx=20, sticky="w")
    radio_button_3 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=3, text="Full Pharmacy Complement")
    radio_button_3.grid(row=2, column=0, pady=10, padx=20, sticky="w")
    radio_button_4 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=4, text="PMTCT Line List")
    radio_button_4.grid(row=3, column=0, pady=10, padx=20, sticky="w")
    radio_button_5 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=5, text="Last 5 Pharmacy")
    radio_button_5.grid(row=4, column=0, pady=10, padx=20, sticky="w")

    radio_button_6 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=6, text="EID Line List")
    radio_button_6.grid(row=0, column=1, pady=10, padx=20, sticky="w")
    radio_button_7 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=7, text="AHD Line List")
    radio_button_7.grid(row=1, column=1, pady=10, padx=20, sticky="w")
    radio_button_8 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=8, text="LIMS_EMR Daily Report")
    radio_button_8.grid(row=2, column=1, pady=10, padx=20, sticky="w")
    radio_button_9 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=9, text="HIV-COVID_19 Line List")
    radio_button_9.grid(row=3, column=1, pady=10, padx=20, sticky="w")
    radio_button_10 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                        value=10, text="OTZ Line list")
    radio_button_10.grid(row=4, column=1, pady=10, padx=20, sticky="w")


# list_options()
'''

''''''


def update_stored_procedure():
    pass


def run_main_app(event):
    '''
    result = messagebox.askyesnocancel("Confirm",
                                       "Click 'Yes' if this is your first time of the app or running the updated "
                                       "version,\n "
                                       "If not, click 'No'")
    try:
        if result == True:
            update_stored_procedure()
        else:
            messagebox.showinfo("Messgage", "Click OK to continue.")
    except Exception as e:
        messagebox.showinfo('Info', "ERROR: {}".format(e))
'''
    ask_if_new_user = messagebox.askyesnocancel("User Status",
                                                "Click 'Yes' if you are using a new or updated version of GISAT Plus.\n"
                                                "Click 'No' if not applicable.")
    try:
        if ask_if_new_user == True:
            messagebox.showinfo("Messgage", "Please be reminded to import the updated 'GISAT_Plus.sql' file (one of "
                                            "the prerequisite for GISAT Plus) in the 'openmrs' Database before you "
                                            "proceed.")
            # Connection to create line-list db
            mydb1 = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Admin123"
            )

            my_cursor1 = mydb1.cursor()

            # Create db
            my_cursor1.execute("DROP DATABASE IF EXISTS validation_linelist")
            my_cursor1.execute("CREATE DATABASE IF NOT EXISTS validation_linelist")

            my_cursor1.close()
            mydb1.close()
        else:
            pass
    except Exception as e:
        messagebox.showinfo('Info', "ERROR: {}".format(e))

    # radio_sel = getattr(wel, "radio_var")
    # welcome_list_selected =
    # print(welcome_list_selected)

    def backup_nmrs():
        db_backup_button.configure(command=threading.Thread(target=backup_nmrs).start)
        try:
            # Main Process
            username = 'root'
            password = 'Admin123'
            database = 'openmrs'

            open_file = filedialog.askdirectory()
            path = open_file

            # Small window
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()

            mydb3 = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Admin123",
                database="openmrs"
            )
            my_cursor3 = mydb3.cursor(buffered=True)
            fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
            definergrant = "GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY 'Admin123';"
            definergrant1 = my_cursor3.execute(definergrant)
            run_fac_name = my_cursor3.execute(fac_name)
            result_fac = my_cursor3.fetchone()[0]
            end_time = date.today()

            with open(path + "/" + str(result_fac) + "_" + 'Database_Backup' + "_" + str(end_time) + '.sql',
                      'w') as output:
                c = subprocess.Popen(['mysqldump', '-u', username, '-p%s' % password, database],
                                     stdout=output, shell=True)

            # Compress the SQL file using gzip
            # subprocess.run(["gzip", path + "/" + str(result_fac) + "_" + 'Database_Backup' + "_" + str(end_time) + '.sql'])
            # close small window
            topwindow.destroy()
            # topwindow.destroy()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
            sys.exit()
            topwindow.destroy()

            my_cursor3.close()
            mydb3.close()

    def generate_nmrs():
        linelist_gen_button.configure(command=threading.Thread(target=generate_nmrs).start)
        # NMRS Connection
        # start_download
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Admin123",
            database="openmrs"
        )
        my_cursor2 = mydb2.cursor(buffered=True)
        try:
            if script_box.get() == 'Treatment Line List':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL CIHP_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_Linelist_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='Treatment_Linelist', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'HTS Line List':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL HTS_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_HTS_Linelist_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='HTS_Linelist', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'Full Pharmacy Complement':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL Full_Pharmacy_Complement();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_Full_Pharmacy_Complement_" + str(val_linelist_gen_date) + "_" + str(
                        result_fac) + ".xlsx",
                    sheet_name='Full_Pharmacy_Complement', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)

            elif script_box.get() == 'PMTCT Line List':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL PMTCT_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_PMTCT_Linelist_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='PMTCT_Linelist', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'EID Line List':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL EID_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_EID_Linelist_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='EID_Linelist', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'AHD Line List':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL AHD_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_AHD_Linelist_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='AHD_Linelist', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'LIMS_EMR Daily Report':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL LIMS_EMR_Daily_Report();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_LIMS_EMR_Daily_Report_" + str(val_linelist_gen_date) + "_" + str(
                        result_fac) + ".xlsx",
                    sheet_name='LIMS_EMR_Daily_Report', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)

            elif script_box.get() == 'Last 5 Pharmacy':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL Last_5_Pharmacy();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_Last_5_Pharmacy_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='Last_5_Pharmacy', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif script_box.get() == 'OTZ Line list':
                messagebox.showinfo("Attention!",
                                    "This process may take sometime, depending on the size/patient load of the NMRS "
                                    "database you are accessing...")
                topwindow = ck.CTkToplevel(None)
                topwindow.geometry("350x100")
                topwindow.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
                l2.pack()
                # Call the update function
                # Test to see db
                end_time = datetime.now()
                use_date = end_time.strftime("%Y-%m-%d")
                val_linelist_gen_date = linelist_gen_date.get_date()
                my_time = datetime.min.time()
                val_linelist_gen_date1 = datetime.combine(val_linelist_gen_date, my_time)
                val_linelist_gen_date2 = val_linelist_gen_date1 + timedelta(hours=23, minutes=59, seconds=57)
                # print(val_linelist_gen_date2)
                fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
                run_fac_name = my_cursor2.execute(fac_name)
                result_fac = my_cursor2.fetchone()[0]
                set_date_variable = f"SET @Reporting_Date := '{val_linelist_gen_date2}'"
                run_script_set_date_variable = my_cursor2.execute(set_date_variable)
                call_nmrs_linelist = "CALL OTZ_LineList();"
                df = pd.read_sql(call_nmrs_linelist, mydb2)
                df.head()
                # stop_download()
                # close small window
                topwindow.destroy()
                # Save file
                open_file = filedialog.askdirectory()
                path = open_file
                df.to_excel(
                    f"{path}/CIHP_OTZ_LineList_" + str(val_linelist_gen_date) + "_" + str(result_fac) + ".xlsx",
                    sheet_name='OTZ_LineList', index=False)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                messagebox.showerror("Error!!!", "List not available")
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
            sys.exit()
            topwindow.destroy()

            mydb2.close()
            my_cursor2.close()

    # Connection for linelist import
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Admin123",
        database="validation_linelist"
    )

    my_cursor = mydb.cursor(buffered=True)
    # Test to see db
    my_cursor.execute("SHOW DATABASES")
    for db in my_cursor:
        print(db)

    # Create a table
    my_cursor.execute(sql_scripts_all.create_table_linelist)
    my_cursor.execute(sql_scripts_all.create_ahd_linelist)
    my_cursor.execute(sql_scripts_all.create_eid_linelist)
    my_cursor.execute(sql_scripts_all.create_hts_linelist)
    my_cursor.execute(sql_scripts_all.create_lims_emr_linelist)
    my_cursor.execute(sql_scripts_all.create_otz_linelist)
    my_cursor.execute(sql_scripts_all.create_pmtct_linelist)
    my_cursor.execute(sql_scripts_all.create_full_pharmacy_complement)
    my_cursor.execute(sql_scripts_all.create_last_5_pharmacy)

    def truncate_linelist():
        Truncate_button.configure(command=threading.Thread(target=truncate_linelist).start)
        result = messagebox.askyesnocancel("Truncate",
                                           "All record(s) in the 'linelist' table will be truncated.\n"
                                           " Are you sure?")
        try:
            if result == True:
                if script_box.get() == 'Treatment Line List':
                    my_cursor.execute("TRUNCATE TABLE `linelist`")
                    messagebox.showinfo("Truncate", "Treatment Line List is truncated")
                elif script_box.get() == 'HTS Line List':
                    my_cursor.execute("TRUNCATE TABLE `hts_linelist`")
                    messagebox.showinfo("Truncate", "HTS Line List is truncated")
                elif script_box.get() == 'Full Pharmacy Complement':
                    my_cursor.execute("TRUNCATE TABLE `full_pharmacy_complement`")
                    messagebox.showinfo("Truncate", "Full Pharmacy Complement is truncated")
                elif script_box.get() == 'PMTCT Line List':
                    my_cursor.execute("TRUNCATE TABLE `pmtct_linelist`")
                    messagebox.showinfo("Truncate", "PMTCT Line List is truncated")
                elif script_box.get() == 'EID Line List':
                    my_cursor.execute("TRUNCATE TABLE `eid_linelist`")
                    messagebox.showinfo("Truncate", "EID Line List is truncated")
                elif script_box.get() == 'AHD Line List':
                    my_cursor.execute("TRUNCATE TABLE `ahd_linelist`")
                    messagebox.showinfo("Truncate", "AHD Line List is truncated")
                elif script_box.get() == 'LIMS_EMR Daily Report':
                    my_cursor.execute("TRUNCATE TABLE `lims_emr_daily_report`")
                    messagebox.showinfo("Truncate", "LIMS_EMR Daily Report is truncated")
                elif script_box.get() == 'OTZ Line list':
                    my_cursor.execute("TRUNCATE TABLE `otz_linelist`")
                    messagebox.showinfo("Truncate", "OTZ Line list is truncated")
                elif script_box.get() == 'Last 5 Pharmacy':
                    my_cursor.execute("TRUNCATE TABLE `Last_5_Pharmacy`")
                    messagebox.showinfo("Truncate", "Last 5 Pharmacy is truncated")
                else:
                    messagebox.showinfo("Oops!", "Oops!!! You can't ;)")
                topwindow2 = ck.CTkToplevel(None)
                topwindow2.geometry("350x100")
                topwindow2.title("Processing")
                progressbar = ck.CTkProgressBar(topwindow2, mode="indeterminate_speed", width=300)
                progressbar.pack(pady=30, padx=10)
                # Start moving the indeterminate progress bar.
                progressbar.start()
                l2 = Label(topwindow2, text='Please wait.........', font=('Helvetica bold', 15), bg='#252525',
                           fg='#ffffff')
                l2.pack()
                topwindow2.destroy()
                truncate_linelist_details()
            else:
                messagebox.showinfo("Oops!",
                                    "Oops!!! Tryna get it right ;)")
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
        sys.exit()

    def button_callback():
        print("Button click", ip_box.get())

    '''
    def slider_callback(value):
        progressbar_1.set(value)
    '''

    # Import list button - Import all xlxs files in dir
    def path_label_folder():
        Import_button.configure(command=threading.Thread(target=path_label_folder).start)
        # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
        messagebox.showinfo("Attention!", "Please, ensure you have list with the most recent headers to avoid error(s)")
        if script_box.get() == 'Treatment Line List':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Errmeor!!!', info)
                    # topwindow.destroy()

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'HTS Line List':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='hts_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'PMTCT Line List':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='pmtct_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'EID Line List':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='eid_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'AHD Line List':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='ahd_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'LIMS_EMR Daily Report':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='lims_emr_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'Full Pharmacy Complement':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='Full_Pharmacy_Complement', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'Last 5 Pharmacy':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='last_5_pharmacy', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif script_box.get() == 'OTZ Line list':
            root = Tk()  # pointing root to Tk() to use it as Tk() in program.
            root.withdraw()  # Hides small tkinter window.
            root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
            open_file = filedialog.askdirectory()  # Returns opened path as str
            # return(open_file)
            label_path = Label(app, text="The File(s) are located at : " + open_file,
                               font=("Century Gothic", '9', "italic"))
            label_path.pack(pady=2, padx=10)
            start_time = datetime.now()
            label_start_time = Label(app, text="Start time: " + str(start_time), font=("Century Gothic", "8", "italic"))
            label_start_time.pack(pady=20, padx=10)
            # print('Begin:', start_time)
            num = 0

            engine = create_engine('mysql+pymysql://root:Admin123@localhost:3306/validation_linelist')
            path = open_file
            files = os.listdir(path)
            # pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=5).start()
            topwindow = ck.CTkToplevel(None)
            topwindow.geometry("350x100")
            topwindow.title("Processing")
            progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
            progressbar.pack(pady=30, padx=10)
            # Start moving the indeterminate progress bar.
            progressbar.start()
            l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
            l2.pack()
            for i in files:
                try:
                    data = pd.read_excel(os.path.join(path, i), header=0)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)
                try:
                    data.to_sql(name='otz_linelist', con=engine, index=False, if_exists='append')
                    num += 1
                    print('Imported:', i)
                except Exception as e:
                    errordata = str(e)
                    info = (errordata[:90] + '..') if len(errordata) > 90 else errordata
                    messagebox.showerror('Error!!!', info)

                    # pbar.update(i)

                # pbar.finish()

            end_time = datetime.now()
            topwindow.destroy()
            label_end_time = Label(app, text="End time: " + str(end_time), font=("Century Gothic", "8", "italic"))
            label_end_time.pack(pady=1, padx=10)
            print('End:', end_time)
            total_time = end_time - start_time
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total Time:', total_time)
            label_total_time = Label(app, text="Total time: " + str(total_time), font=("Century Gothic", "8", "italic"))
            label_total_time.pack(pady=1, padx=10)
            print('Total number of imported files:', num)
            label_total_no_file = Label(app, text="Total No. of file(s): " + str(num),
                                        font=("Century Gothic", "8", "italic"))
            label_total_no_file.pack(pady=1, padx=10)

            after_export = messagebox.showinfo("Export details",
                                               "Total No. of file(s) imported: " + str(num) + "\n"
                                                                                              "Start time: " + str(
                                                   start_time) + "\n"
                                                                 "End time: " + str(end_time) + "\n"
                                                                                                "Total time: " + str(
                                                   total_time) + "\n"
                                                                 "File(s) successfully imported. \nTo continue, click "
                                                                 "'OK' and relaunch app.")

            # Relaunch for recalibration
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            messagebox.showerror('Error!!!', 'Something went wrong')

        # Display record details on main frame

    merge_level = [
        "IP",
        "State",
        "SurgeCommand",
        "LGA"
    ]
    # print(list_options())
    script_list = [
        ""
        "Treatment Line List",
        "HTS Line List",
        "Full Pharmacy Complement",
        "PMTCT Line List",
        "EID Line List",
        "AHD Line List",
        "LIMS_EMR Daily Report",
        "HIV-COVID_19 Line List",
        "Last 5 Pharmacy",
        "OTZ Line list"
    ]

    ######################################################
    my_str = StringVar()

    def selected_ip():
        # clicked.get() == 'IP':
        if script_box.get() == 'Treatment Line List':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `linelist`")
        elif script_box.get() == 'HTS Line List':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `hts_linelist`")
        elif script_box.get() == 'Full Pharmacy Complement':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `Full_Pharmacy_Complement`")
        elif script_box.get() == 'PMTCT Line List':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `pmtct_linelist`")
        elif script_box.get() == 'EID Line List':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `eid_linelist`")
        elif script_box.get() == 'AHD Line List':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `ahd_linelist`")
        elif script_box.get() == 'LIMS_EMR Daily Report':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `lims_emr_daily_report`")
        elif script_box.get() == 'Last 5 Pharmacy':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `Last_5_Pharmacy`")
        elif script_box.get() == 'OTZ Line list':
            my_cursor.execute("SELECT DISTINCT(`IP`) FROM `otz_linelist`")
        else:
            print("")
        select_country1 = [i[0] for i in my_cursor.fetchall()]
        return select_country1

    def selected_state():
        # clicked.get() == 'State':
        if script_box.get() == 'Treatment Line List':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `linelist`")
        elif script_box.get() == 'HTS Line List':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `hts_linelist`")
        elif script_box.get() == 'Full Pharmacy Complement':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `Full_Pharmacy_Complement`")
        elif script_box.get() == 'PMTCT Line List':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `pmtct_linelist`")
        elif script_box.get() == 'EID Line List':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `eid_linelist`")
        elif script_box.get() == 'AHD Line List':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `ahd_linelist`")
        elif script_box.get() == 'LIMS_EMR Daily Report':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `lims_emr_daily_report`")
        elif script_box.get() == 'Last 5 Pharmacy':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `Last_5_Pharmacy`")
        elif script_box.get() == 'OTZ Line list':
            my_cursor.execute("SELECT DISTINCT(`State`) FROM `otz_linelist`")
        else:
            print("")
        select_country1 = [i[0] for i in my_cursor.fetchall()]
        return select_country1

    def selected_surgecommand1():
        # clicked.get() == 'SurgeCommand':
        if script_box.get() == 'Treatment Line List':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `linelist`")
        elif script_box.get() == 'HTS Line List':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `hts_linelist`")
        elif script_box.get() == 'Full Pharmacy Complement':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `Full_Pharmacy_Complement`")
        elif script_box.get() == 'PMTCT Line List':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `pmtct_linelist`")
        elif script_box.get() == 'EID Line List':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `eid_linelist`")
        elif script_box.get() == 'AHD Line List':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `ahd_linelist`")
        elif script_box.get() == 'LIMS_EMR Daily Report':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `lims_emr_daily_report`")
        elif script_box.get() == 'Last 5 Pharmacy':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `Last_5_Pharmacy`")
        elif script_box.get() == 'OTZ Line list':
            my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `otz_linelist`")
        else:
            print("")
        select_country1 = [i[0] for i in my_cursor.fetchall()]
        return select_country1

    def selected_lga():
        if script_box.get() == 'Treatment Line List':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `linelist`")
        elif script_box.get() == 'HTS Line List':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `hts_linelist`")
        elif script_box.get() == 'Full Pharmacy Complement':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `Full_Pharmacy_Complement`")
        elif script_box.get() == 'PMTCT Line List':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `pmtct_linelist`")
        elif script_box.get() == 'EID Line List':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `eid_linelist`")
        elif script_box.get() == 'AHD Line List':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `ahd_linelist`")
        elif script_box.get() == 'LIMS_EMR Daily Report':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `lims_emr_daily_report`")
        elif script_box.get() == 'Last 5 Pharmacy':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `Last_5_Pharmacy`")
        elif script_box.get() == 'OTZ Line list':
            my_cursor.execute("SELECT DISTINCT(`lga`) FROM `otz_linelist`")
        else:
            print("")
        select_country1 = [i[0] for i in my_cursor.fetchall()]
        return select_country1

    def all_export_boxes():
        # print('I don work')
        state_box.destroy()
        selected_ip()
        selected_state()
        selected_surgecommand1()
        selected_lga()
        state_box

    # Keep track of the button state on/off
    global is_on
    is_on = True

    # ctk_textbox_scrollbar = ck.CTkScrollbar(app)
    # ctk_textbox_scrollbar.pack(row=0, column=1, sticky="ns")

    # app.configure(yscrollcommand=ctk_textbox_scrollbar.set)

    #######################################################################################################
    '''
    linelist_gen_buttonppp = ck.CTkButton(master=frame_1, command=threading.Thread(target=lambda: list_options()).start,
                                          text="Generate NMRS Line List",
                                          width=280, font=("Century Gothic", 18, "bold"))
    linelist_gen_buttonppp.pack(pady=(1, 4), padx=10)
    '''
    ######################################################

    # script_box = ck.CTkComboBox(frame_1, values=script_list, width=280)
    # script_box.current(0) #set the selected item
    # script_box.set(0)
    # script_box.pack(pady=(1, 1), padx=10)
    # script_box.bind("<<ComboboxSelected>>", all_export_boxes)

    linelist_gen_date = DateEntry(frame_1, selectmode='day', date_pattern='dd/mm/yyyy', width=26,
                                  font=("Century Gothic",
                                        13, "bold"))
    linelist_gen_date.pack(pady=(1, 1), padx=10)

    # linelist_gen_date.configure(state="disable")

    linelist_gen_button = ck.CTkButton(master=frame_1, command=threading.Thread(target=generate_nmrs).start,
                                       text="Generate NMRS Line List",
                                       width=280, font=("Century Gothic", 18, "bold"))
    linelist_gen_button.pack(pady=(1, 4), padx=10)

    db_backup_button = ck.CTkButton(master=frame_1, command=threading.Thread(target=backup_nmrs).start,
                                    text="Backup NMRS DB",
                                    width=280, font=("Century Gothic", 18, "bold"))
    db_backup_button.pack(pady=(1, 25), padx=10)

    label_1 = ck.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="MERGE LINE LIST",
                          font=("Century Gothic", 25, "bold"))
    label_1.pack(pady=(1, 1), padx=10)

    Truncate_button = ck.CTkButton(master=frame_1, command=threading.Thread(target=truncate_linelist).start,
                                   text="Truncate Linelist DB",
                                   width=280, font=("Century Gothic", 18, "bold"))
    Truncate_button.pack(pady=11, padx=10)

    Import_button = ck.CTkButton(master=frame_1, command=threading.Thread(target=path_label_folder).start,
                                 text="Import list",
                                 width=280, font=("Century Gothic", 18, "bold"))
    Import_button.pack(pady=11, padx=10)

    clicked = StringVar()
    clicked.set("Select Level of Merging")

    # list_options()
    select_ip = selected_ip()
    select_state = selected_state()
    select_surgecom = selected_surgecommand1()
    select_lga = selected_lga()

    l1 = ck.CTkLabel(frame_1, text="Select IP:",
                     font=("Century Gothic", 11, "italic"))
    l1.pack(pady=(1, 0), padx=(1, 220))

    ip_box = ck.CTkComboBox(frame_1, values=select_ip, width=280)
    ip_box.pack(pady=(1, 10), padx=40)
    ip_box.set("")

    l1 = ck.CTkLabel(frame_1, text="Select State:",
                     font=("Century Gothic", 11, "italic"))
    l1.pack(pady=(1, 0), padx=(1, 200))

    state_box = ck.CTkComboBox(frame_1, values=select_state, width=280)
    state_box.pack(pady=(1, 10), padx=10)
    state_box.set("")

    l1 = ck.CTkLabel(frame_1, text="Select Surge Command:",
                     font=("Century Gothic", 11, "italic"))
    l1.pack(pady=(1, 0), padx=(1, 140))

    surge_box = ck.CTkComboBox(frame_1, values=select_surgecom, width=280)
    surge_box.pack(pady=(1, 10), padx=10)
    surge_box.set("")

    l1 = ck.CTkLabel(frame_1, text="Select LGA:",
                     font=("Century Gothic", 11, "italic"))
    l1.pack(pady=(1, 0), padx=(1, 210))

    lga_box = ck.CTkComboBox(frame_1, values=select_lga, width=280)
    lga_box.pack(pady=(1, 10), padx=10)
    lga_box.set("")

    def switch():
        global is_on
        # Determine if on or off
        if is_on:
            on_off_button.configure(image=off, bd=0, background="#333333")
            l1.configure(text='Switch is "OFF" - All validation deactivated')
            val_date.configure(state="disable")
            is_on = False
        else:
            on_off_button.configure(image=on, bd=0, background="#333333")
            l1.configure(text='Switch is "ON" - All validation activated')
            val_date.configure(state="enable")
            is_on = True

    l1 = ck.CTkLabel(frame_1, text='Switch is "ON" - All validation activated',
                     font=("Century Gothic", 11, "italic"))
    l1.pack(pady=0, padx=10)

    val_date = DateEntry(frame_1, selectmode='day', date_pattern='dd/mm/yyyy', width=26,
                         font=("Century Gothic", 13, "bold"))
    val_date.pack(pady=(1, 1), padx=10)

    # Define images
    on = PhotoImage(file="images/on.png")
    off = PhotoImage(file="images/off.png")

    on_off_button = Button(master=frame_1, image=on, bd=0, background="#333333", command=switch)
    on_off_button.pack(pady=1, padx=(11, 227))

    def ipget():
        a = ip_box.get()
        if a == "":
            return ""
        else:
            return a

    def statebeg():
        a = state_box.get()
        if a == "":
            return ""
        else:
            return a

    def surgeget():
        a = surge_box.get()
        if a == "":
            return ""
        else:
            return a

    def lgaget():
        a = lga_box.get()
        if a == "":
            return ""
        else:
            return a

    def start_merging():
        merge_button.configure(command=threading.Thread(target=start_merging).start)
        update_list_gen_date = "UPDATE `linelist` SET `Date_List_Gen` = DATE(CONCAT(LEFT(CURRENT_DATE, 2), \
                               RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1 ), 2), '-', \
                               RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2 ), 2),'-', RIGHT(List_Parameters, 2)))"
        my_cursor.execute(update_list_gen_date)

        topwindow = ck.CTkToplevel(None)
        topwindow.geometry("350x100")
        topwindow.title("Processing")
        progressbar = ck.CTkProgressBar(topwindow, mode="indeterminate_speed", width=300)
        progressbar.pack(pady=30, padx=10)
        # Start moving the indeterminate progress bar.
        progressbar.start()
        l2 = ck.CTkLabel(topwindow, text='Please wait.........', font=('Helvetica bold', 15, 'italic'))
        l2.pack()

        ip_ = ip_box.get()
        state_ = state_box.get()
        surge_ = surge_box.get()
        lga_ = lga_box.get()
        val_date2 = val_date.get_date()
        use_date = val_date2.strftime("%Y-%m-%d")
        check_date_ip = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{val_date2}%' AND " \
                        f"`ip` = '{ip_}' "
        check_date_state = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{val_date2}%' AND `ip` = '{ip_}' " \
                           f"AND `state` = '{state_}' "
        check_date_surge = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{val_date2}%' AND `ip` = '{ip_}' " \
                           f"AND `state` = '{state_}' AND `SurgeCommand` = '{surge_}' "
        check_date_lga = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{val_date2}%' AND `ip` = '{ip_}' " \
                         f"AND `state` = '{state_}' AND `SurgeCommand` = '{surge_}' AND `lga` = '{lga_}' "
        run_script_ip = my_cursor.execute(check_date_ip)
        count_wrong_date_ip = len(my_cursor.fetchall())

        run_script_state = my_cursor.execute(check_date_state)
        count_wrong_date_state = len(my_cursor.fetchall())

        run_script_state = my_cursor.execute(check_date_surge)
        count_wrong_date_surge = len(my_cursor.fetchall())

        run_script_state = my_cursor.execute(check_date_lga)
        count_wrong_date_lga = len(my_cursor.fetchall())

        # count wrong selections
        run_wrong_ip = pd.read_sql(mysql_script.select_all_merge_tx_0, mydb)
        count_run_wrong_ip = run_wrong_ip.shape[0]

        run_wrong_state = pd.read_sql(mysql_script.select_all_merge_tx_1, mydb,
                                      params=(ip_box.get(), state_box.get()))
        count_run_wrong_state = run_wrong_state.shape[0]

        run_wrong_surg = pd.read_sql(mysql_script.select_all_merge_tx_2, mydb,
                                     params=(ip_box.get(), state_box.get(), surge_box.get()))
        count_run_wrong_surg = run_wrong_surg.shape[0]

        run_wrong_lga = pd.read_sql(mysql_script.select_all_merge_tx_3, mydb,
                                    params=(ip_box.get(), state_box.get(), surge_box.get(), lga_box.get()))
        count_run_wrong_lga = run_wrong_lga.shape[0]
        #######################################################################################################################
        # If only IP is select
        run_script2 = my_cursor.execute(mysql_script.check_art_enrolled_date)
        count_art_enrolled_date = len(my_cursor.fetchall())

        run_script2 = my_cursor.execute(mysql_script.check_art_lastpickup)
        count_check_art_lastpickup = len(my_cursor.fetchall())

        run_script2 = my_cursor.execute(mysql_script.check_art_start_date)
        count_check_art_start_date = len(my_cursor.fetchall())

        run_script2 = my_cursor.execute(mysql_script.check_pickup_after_discon)
        count_check_pickup_after_discon = len(my_cursor.fetchall())

        run_script2 = my_cursor.execute(mysql_script.check_pickup_after_death)
        count_check_pickup_after_death = len(my_cursor.fetchall())

        run_script2 = my_cursor.execute(mysql_script.check_incomplete_discon)
        count_check_incomplete_discon = len(my_cursor.fetchall())
        #######################################################################################################################

        check_which_list = script_box.get()

        topwindow.destroy()

        if count_wrong_date_ip > 0 and ip_box.get() != '' and state_box.get() == '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 f"Total number of record(s) not generated with the specified date are {count_wrong_date_ip}. Regenerate list and proceed")
        elif count_wrong_date_state > 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 f"Total number of record(s) not generated with the specified date in the state are {count_wrong_date_state}. Regenerate list and proceed")
        elif count_wrong_date_surge > 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 f"Total number of record(s) not generated with the specified date in the Surge Command are {count_wrong_date_surge}. Regenerate list and proceed")
        elif count_wrong_date_lga > 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() != '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 f"Total number of record(s) not generated with the specified date in the LGA are {count_wrong_date_lga}. Regenerate list and proceed")

        elif count_run_wrong_ip == 0 and ip_box.get() != '' and state_box.get() == '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 "No such record!")
        elif count_run_wrong_state == 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 "No such record!")
        elif count_run_wrong_surg == 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 "No such record!")
        elif count_run_wrong_lga == 0 and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() != '' and is_on and script_box.get() == 'Treatment Line List':
            messagebox.showerror("Date validation error!!!",
                                 "No such record!")
        # Non Treatment line list merging
        elif script_box.get() == 'HTS Line List':
            df = pd.read_sql(mysql_script.select_all_merge_hts_linelist, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\HTS_Line_List_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='HTS_Line_List_Merged', index=False)

        elif script_box.get() == 'Full Pharmacy Complement':
            df = pd.read_sql(mysql_script.select_all_merge_full_pharmacy_complement, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\Full_Pharmacy_Complement_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='Full_Pharmacy_Complement_Merged', index=False)

        elif check_which_list == 'PMTCT Line List':
            df = pd.read_sql(mysql_script.select_all_merge_pmtct_linelist, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\PMTCT_Line_List_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        elif check_which_list == 'EID Line List':
            df = pd.read_sql(mysql_script.select_all_merge_eid_linelist, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\EID_Line_List_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        elif check_which_list == 'AHD Line List':
            df = pd.read_sql(mysql_script.select_all_merge_ahd_linelist, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\AHD_Line_List_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        elif check_which_list == 'LIMS_EMR Daily Report':
            df = pd.read_sql(mysql_script.select_all_merge_lims_emr_daily_report, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\LIMS_EMR_Daily_Report_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        elif check_which_list == 'Last 5 Pharmacy':
            df = pd.read_sql(mysql_script.select_all_merge_last_5_pharmacy, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\Last_5_Pharmacy_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        elif check_which_list == 'OTZ Line List':
            df = pd.read_sql(mysql_script.select_all_merge_otz_linelist, mydb)
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                f"{path}\\OTZ_Line_List_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                + use_date + ".xlsx", sheet_name='PMTCT_Line_List_Merged', index=False)

        # Treatment line list validation
        else:
            if (count_art_enrolled_date > 0 or count_check_art_start_date > 0 or count_check_pickup_after_discon > 0 \
                or count_check_pickup_after_death > 0 or count_check_incomplete_discon > 0 or count_check_art_lastpickup > 0) \
                    and ip_box.get() != '' and state_box.get() == '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                msg = messagebox.askyesnocancel("GISAT-Plus Warning!!!",
                                                f"1. Total number of client(s) not transferred in who started ART before enrollment are {count_art_enrolled_date}.""\n"
                                                f"2. Total number of client(s) who had drug pickup before ART Commencement are {count_check_art_lastpickup}.""\n"
                                                f"3. Total number of client(s) without ART Start Date are {count_check_art_start_date}.""\n"
                                                f"4. Total number of client(s) who picked up drug after discontinuation are {count_check_pickup_after_discon}.""\n"
                                                f"5. Total number of client(s) who had drug pickup after DEATH are {count_check_pickup_after_death}.""\n"
                                                f"6. Total number of client(s) whose CTT Form are incomplete are {count_check_incomplete_discon}.""\n"
                                                "\n"
                                                "Click Yes to continue and No to cancel.")
            # If only IP and State are select
            elif (count_art_enrolled_date > 0 or count_check_art_start_date > 0 or count_check_pickup_after_discon > 0 \
                  or count_check_pickup_after_death > 0 or count_check_incomplete_discon > 0 or count_check_art_lastpickup > 0) \
                    and ip_box.get() != '' and state_box.get() != '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                #######################################################################################################################

                count_check_art_enrolled_date_ip_state1 = pd.read_sql(mysql_script.check_art_enrolled_date_ip_state,
                                                                      mydb,
                                                                      params=(ip_box.get(), state_box.get()))
                count_check_art_enrolled_date_ip_state = count_check_art_enrolled_date_ip_state1.shape[0]

                count_check_art_lastpickup_ip_state1 = pd.read_sql(mysql_script.check_art_lastpickup_ip_state, mydb,
                                                                   params=(ip_box.get(), state_box.get()))
                count_check_art_lastpickup_ip_state = count_check_art_lastpickup_ip_state1.shape[0]

                count_check_art_start_date_ip_state1 = pd.read_sql(mysql_script.check_art_start_date_ip_state, mydb,
                                                                   params=(ip_box.get(), state_box.get()))
                count_check_art_start_date_ip_state = count_check_art_start_date_ip_state1.shape[0]

                count_check_pickup_after_discon_ip_state1 = pd.read_sql(mysql_script.check_pickup_after_discon_ip_state,
                                                                        mydb,
                                                                        params=(ip_box.get(), state_box.get()))
                count_check_pickup_after_discon_ip_state = count_check_pickup_after_discon_ip_state1.shape[0]

                count_check_pickup_after_death_ip_state1 = pd.read_sql(mysql_script.check_pickup_after_death_ip_state,
                                                                       mydb,
                                                                       params=(ip_box.get(), state_box.get()))
                count_check_pickup_after_death_ip_state = count_check_pickup_after_death_ip_state1.shape[0]

                count_check_incomplete_discon_ip_state1 = pd.read_sql(mysql_script.check_incomplete_discon_ip_state,
                                                                      mydb,
                                                                      params=(ip_box.get(), state_box.get()))
                count_check_incomplete_discon_ip_state = count_check_incomplete_discon_ip_state1.shape[0]

                #######################################################################################################################

                msg = messagebox.askyesnocancel("GISAT-Plus Warning!!!",
                                                f"1. Total number of client(s) not transferred in who started ART before enrollment are {count_check_art_enrolled_date_ip_state}.""\n"
                                                f"2. Total number of client(s) who had drug pickup before ART Commencement are {count_check_art_lastpickup_ip_state}.""\n"
                                                f"3. Total number of client(s) without ART Start Date are {count_check_art_start_date_ip_state}.""\n"
                                                f"4. Total number of client(s) who picked up drug after discontinuation are {count_check_pickup_after_discon_ip_state}.""\n"
                                                f"5. Total number of client(s) who had drug pickup after DEATH are {count_check_pickup_after_death_ip_state}.""\n"
                                                f"6. Total number of client(s) whose CTT Form are incomplete are {count_check_incomplete_discon_ip_state}.""\n"
                                                "\n"
                                                "Click Yes to continue and No to cancel.")
            # If only IP, State and Surge are select
            elif (count_art_enrolled_date > 0 or count_check_art_start_date > 0 or count_check_pickup_after_discon > 0 \
                  or count_check_pickup_after_death > 0 or count_check_incomplete_discon > 0 or count_check_art_lastpickup > 0) \
                    and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                #######################################################################################################################

                count_check_art_enrolled_date_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_art_enrolled_date_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_art_enrolled_date_ip_state_surg = count_check_art_enrolled_date_ip_state_surg1.shape[0]

                count_check_art_lastpickup_ip_state_surg1 = pd.read_sql(mysql_script.check_art_lastpickup_ip_state_surg,
                                                                        mydb,
                                                                        params=(
                                                                            ip_box.get(), state_box.get(),
                                                                            surge_box.get()))
                count_check_art_lastpickup_ip_state_surg = count_check_art_lastpickup_ip_state_surg1.shape[0]

                count_check_art_start_date_ip_state_surg1 = pd.read_sql(mysql_script.check_art_start_date_ip_state_surg,
                                                                        mydb,
                                                                        params=(
                                                                            ip_box.get(), state_box.get(),
                                                                            surge_box.get()))
                count_check_art_start_date_ip_state_surg = count_check_art_start_date_ip_state_surg1.shape[0]

                count_check_pickup_after_discon_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_pickup_after_discon_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_pickup_after_discon_ip_state_surg = count_check_pickup_after_discon_ip_state_surg1.shape[0]

                count_check_pickup_after_death_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_pickup_after_death_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_pickup_after_death_ip_stat_sure_surg = count_check_pickup_after_death_ip_state_surg1.shape[
                    0]

                count_check_incomplete_discon_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_incomplete_discon_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_incomplete_discon_ip_state_surg = count_check_incomplete_discon_ip_state_surg1.shape[0]

                #######################################################################################################################

                msg = messagebox.askyesnocancel("GISAT-Plus Warning!!!",
                                                f"1. Total number of client(s) not transferred in who started ART before enrollment are {count_check_art_enrolled_date_ip_state_surg}.""\n"
                                                f"2. Total number of client(s) who had drug pickup before ART Commencement are {count_check_art_lastpickup_ip_state_surg}.""\n"
                                                f"3. Total number of client(s) without ART Start Date are {count_check_art_start_date_ip_state_surg}.""\n"
                                                f"4. Total number of client(s) who picked up drug after discontinuation are {count_check_pickup_after_discon_ip_state_surg}.""\n"
                                                f"5. Total number of client(s) who had drug pickup after DEATH are {count_check_pickup_after_death_ip_stat_sure_surg}.""\n"
                                                f"6. Total number of client(s) whose CTT Form are incomplete are {count_check_incomplete_discon_ip_state_surg}.""\n"
                                                "\n"
                                                "Click Yes to continue and No to cancel.")

                # If only IP, State and Surge are select
            elif (count_art_enrolled_date > 0 or count_check_art_start_date > 0 or count_check_pickup_after_discon > 0 \
                  or count_check_pickup_after_death > 0 or count_check_incomplete_discon > 0 or count_check_art_lastpickup > 0) \
                    and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                #######################################################################################################################

                count_check_art_enrolled_date_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_art_enrolled_date_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_art_enrolled_date_ip_state_surg = count_check_art_enrolled_date_ip_state_surg1.shape[0]

                count_check_art_lastpickup_ip_state_surg1 = pd.read_sql(mysql_script.check_art_lastpickup_ip_state_surg,
                                                                        mydb,
                                                                        params=(
                                                                            ip_box.get(), state_box.get(),
                                                                            surge_box.get()))
                count_check_art_lastpickup_ip_state_surg = count_check_art_lastpickup_ip_state_surg1.shape[0]

                count_check_art_start_date_ip_state_surg1 = pd.read_sql(mysql_script.check_art_start_date_ip_state_surg,
                                                                        mydb,
                                                                        params=(
                                                                            ip_box.get(), state_box.get(),
                                                                            surge_box.get()))
                count_check_art_start_date_ip_state_surg = count_check_art_start_date_ip_state_surg1.shape[0]

                count_check_pickup_after_discon_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_pickup_after_discon_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_pickup_after_discon_ip_state_surg = count_check_pickup_after_discon_ip_state_surg1.shape[0]

                count_check_pickup_after_death_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_pickup_after_death_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_pickup_after_death_ip_stat_sure_surg = count_check_pickup_after_death_ip_state_surg1.shape[
                    0]

                count_check_incomplete_discon_ip_state_surg1 = pd.read_sql(
                    mysql_script.check_incomplete_discon_ip_state_surg,
                    mydb,
                    params=(ip_box.get(), state_box.get(), surge_box.get()))
                count_check_incomplete_discon_ip_state_surg = count_check_incomplete_discon_ip_state_surg1.shape[0]

                #######################################################################################################################

                msg = messagebox.askyesnocancel("GISAT-Plus Warning!!!",
                                                f"1. Total number of client(s) not transferred in who started ART before enrollment are {count_check_art_enrolled_date_ip_state_surg}.""\n"
                                                f"2. Total number of client(s) who had drug pickup before ART Commencement are {count_check_art_lastpickup_ip_state_surg}.""\n"
                                                f"3. Total number of client(s) without ART Start Date are {count_check_art_start_date_ip_state_surg}.""\n"
                                                f"4. Total number of client(s) who picked up drug after discontinuation are {count_check_pickup_after_discon_ip_state_surg}.""\n"
                                                f"5. Total number of client(s) who had drug pickup after DEATH are {count_check_pickup_after_death_ip_stat_sure_surg}.""\n"
                                                f"6. Total number of client(s) whose CTT Form are incomplete are {count_check_incomplete_discon_ip_state_surg}.""\n"
                                                "\n"
                                                "Click Yes to continue and No to cancel.")


            else:
                if is_on == False:
                    df2 = pd.read_sql(mysql_script.select_all_merge_tx_0, mydb)
                    df2.head()
                    open_file = filedialog.askdirectory()
                    path = open_file
                    df2.to_excel(
                    f"{path}\\Linelist_" + 'No Validation' + "_"
                    + use_date + ".xlsx", sheet_name='Linelist_Merged', index=False)
                else:
                    messagebox.showerror("Check!!!", "Please do the right thing!!!")
                    # frame_1.destroy()
            if msg == True and ip_box.get() == '' and state_box.get() == '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                    messagebox.showerror("No selection made.")
            elif msg == True and ip_box.get() != '' and state_box.get() == '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                    df = pd.read_sql(mysql_script.select_all_merge_tx_0, mydb)
            elif msg == True and ip_box.get() != '' and state_box.get() != '' and surge_box.get() == '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                    df = pd.read_sql(mysql_script.select_all_merge_tx_1, mydb, params=(ipget(), statebeg()))
            elif msg == True and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() == '' and is_on and script_box.get() == 'Treatment Line List':
                    df = pd.read_sql(mysql_script.select_all_merge_tx_2, mydb, params=(ipget(), statebeg(), surgeget()))
            elif msg == True and ip_box.get() != '' and state_box.get() != '' and surge_box.get() != '' and lga_box.get() != '' and is_on and script_box.get() == 'Treatment Line List':
                    df = pd.read_sql(mysql_script.select_all_merge_tx_3, mydb,
                                     params=(ipget(), statebeg(), surgeget(), lgaget()))


            # a = lga_box.get()
            df.head()
            open_file = filedialog.askdirectory()
            path = open_file
            df.to_excel(
                    f"{path}\\Linelist_" + ip_box.get() + "_" + state_box.get() + "_" + surge_box.get() + "_" + lga_box.get() + "_"
                    + use_date + ".xlsx", sheet_name='Linelist_Merged', index=False)
                # os.open(df_excel)
        #else:
        #messagebox.showerror("Error!!!", "Incorrect selection")


    merge_button = ck.CTkButton(master=frame_1, command=threading.Thread(target=start_merging).start,
                                text="Start Merging",
                                width=280, font=("Century Gothic", 18, "bold"))

    merge_button.pack(pady=20, padx=10)

    # progressbar_1 = ck.CTkProgressBar(master=frame_1)
    # progressbar_1.pack(pady=12, padx=10)

    # progress_bar = ttk.Progressbar(master=frame_1, orient=HORIZONTAL, mode="indeterminate", length=350)
    # progress_bar.pack()

    # Display record details on main frame
    def truncate_linelist_details():
        if script_box.get() == 'Treatment Line List':
            table = 'linelist'
        elif script_box.get() == 'HTS Line List':
            table = 'hts_linelist'
        elif script_box.get() == 'Full Pharmacy Complement':
            table = 'full_pharmacy_complement'
        elif script_box.get() == 'PMTCT Line List':
            table = 'pmtct_linelist'
        elif script_box.get() == 'EID Line List':
            table = 'eid_linelist'
        elif script_box.get() == 'AHD Line List':
            table = 'ahd_linelist'
        elif script_box.get() == 'LIMS_EMR Daily Report':
            table = 'lims_emr_daily_report'
        elif script_box.get() == 'Last 5 Pharmacy':
            table = 'last_5_pharmacy'
        elif script_box.get() == 'OTZ Line list':
            table = 'otz_linelist'

        my_cursor.execute(f"SELECT COUNT(DISTINCT(`IP`)) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of IP: ")
        result1 = f'{lab}{num[0]}'

        my_cursor.execute(f"SELECT COUNT(DISTINCT(`State`)) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of State: ")
        result2 = f'{lab}{num[0]}'

        my_cursor.execute(f"SELECT COUNT(DISTINCT(`SurgeCommand`)) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of Surge Command: ")
        result3 = f'{lab}{num[0]}'

        my_cursor.execute(f"SELECT COUNT(DISTINCT(`lga`)) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of LGA: ")
        result4 = f'{lab}{num[0]}'
        my_cursor.execute(f"SELECT COUNT(DISTINCT(`FacilityName`)) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of Facilty: ")
        result5 = f'{lab}{num[0]}'

        my_cursor.execute(f"SELECT COUNT(`FacilityName`) FROM {table}")
        num = my_cursor.fetchall()
        lab = ("Total No. of Records: ")
        result6 = f'{lab}{num[0]}'

        No_rec1 = ck.CTkLabel(app, justify=tkinter.LEFT, text=result1 + " | " + result2 + " | " + result3,
                              font=("Century Gothic", 11))
        No_rec1.pack(pady=(1, 0), padx=(1, 20))

        No_rec2 = ck.CTkLabel(app, justify=tkinter.LEFT, text=result4 + " | " + result5 + " | " + result6,
                              font=("Century Gothic", 11))
        No_rec2.pack(pady=(1, 0), padx=(1, 20))

        # No_rec1.after(1000, No_rec1.destroy())

    # clicked.trace('w',all_export_boxes)
    truncate_linelist_details()
    script_box_disable()


'''
n = StringVar()
script_box = ttk.Combobox(frame_1, textvariable=n, width=20)
# script_box.current(0) #set the selected item
# script_box.set(0)

# Adding combobox drop down list
script_box['value'] = (
    "Treatment Line List",
    "HTS Line List",
    "Full Pharmacy Complement",
    "PMTCT Line List",
    "EID Line List",
    "AHD Line List",
    "LIMS_EMR Daily Report",
    "HIV-COVID_19 Line List",
    "Last 5 Pharmacy",
    "OTZ Line list"
)
script_box.pack(pady=(1, 1), padx=10)
script_box.current()
script_box.bind("<<ComboboxSelected>>", run_main_app)
'''

reset_button = ck.CTkButton(frame_1, text="Reset", font=("Century Gothic", 14, "bold"), width=70,
                            image=reset_image, anchor="n", command=reset)
reset_button.pack(pady=(1, 1), padx=(1, 198))

combobox_var = ck.StringVar(value="Select line list")  # set initial value
script_box = ck.CTkComboBox(frame_1,
                            values=["Treatment Line List",
                                    "HTS Line List",
                                    "Full Pharmacy Complement",
                                    "PMTCT Line List",
                                    "EID Line List",
                                    "AHD Line List",
                                    "LIMS_EMR Daily Report",
                                    "HIV-COVID_19 Line List",
                                    "Last 5 Pharmacy",
                                    "OTZ Line list"],
                            command=run_main_app,
                            variable=combobox_var, width=280)
script_box.pack(pady=(1, 1), padx=10)


def script_box_disable():
    script_box.configure(values=(""), state="disable")


# clicked.trace('w',selected)
app.mainloop()
