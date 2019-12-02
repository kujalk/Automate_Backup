#Purpose - To input backup status into CSV file
#Execution - python script.py "backup-folder-location" "status" "file-name-of-csv"
#Developer - Janarthanan
#Date - 16/10/2019

from datetime import datetime
import sys
import csv

#Function to store details in the CSV file
def csv_write (folder_location,status,server,file_name):

     now = datetime.now()
     value=now.strftime("%d-%m-%y %H:%M:%S")

     data=[[value,folder_location,server,status]]
     csv_file=file_name

     with open (csv_file,'ab') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(data)

     csvfile.close()

#Calling the function from passed arguments
csv_write(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
