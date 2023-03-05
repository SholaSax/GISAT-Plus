import subprocess
from tkinter import filedialog
import mysql.connector
from datetime import date

username = 'root'
password = 'Admin123'
database = 'openmrs'

open_file = filedialog.askdirectory()
path = open_file

mydb3 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Admin123",
    database="openmrs"
)
my_cursor3 = mydb3.cursor(buffered=True)
fac_name = "SELECT `property_value` FROM `global_property` WHERE `property`= 'Facility_Name'"
run_fac_name = my_cursor3.execute(fac_name)
result_fac = my_cursor3.fetchone()[0]
end_time = date.today()

with open(path + "/" + str(result_fac) + "_" + 'Database_Backup' + "_" + str(end_time) + '.sql', 'w') as output:
    c = subprocess.Popen(['mysqldump', '-u', username, '-p%s' % password, database],
                         stdout=output, shell=True)

# Compress the SQL file using gzip
#subprocess.run(["gzip", path + "/" + str(result_fac) + "_" + 'Database_Backup' + "_" + str(end_time) + '.sql'])
