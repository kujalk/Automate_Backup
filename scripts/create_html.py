
#Purpose - To create static html web pages from CSV files
#Developer - Janarthanan
#Date - 17/10/2019

import csv
import sys
from datetime import datetime

def Get_Html(server,csv_file,html_file):
    # Open the CSV file for reading
    reader = csv.reader(open(csv_file))

    # Create the HTML file
    f_html = open(html_file,"w");

    section_1="""
    <html>
    <body>
    <div style="height: 90;size: 80;background-color:coral">
    <p style="color: black;font-size: 40;text-align: center;padding-top: 30;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">BACKUP INFORMATION OF FOLDERS </p>
    </div >
    <div style="height: 45;size: 40;background-color:lightsalmon">
        <label style="font-size: 25;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">
    """

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    section_2="Last Backup Date & Time: "+dt_string

    section_3="""
    </label>
        <label style="font-size: 25;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;text-align: right;padding-left: 250">

    """

    section_4="Owner : "+server +" Team"

    section_5="""
    </label>
    </div>
    <div style="height: 45;size: 40;padding-top: 10">
        <table  style='font-style: bold; color:black; font-family:serif; font-size: 20px;'>

            <tr>
                <td width="20%"> <a href="Infra.html">Infra</a></td>
                <td width="20%"> <a href="DB.html">DB</a></td>
    </div>
    """
    f_html.write(section_1)
    f_html.write(section_2)
    f_html.write(section_3)
    f_html.write(section_4)
    f_html.write(section_5)
    f_html.write('<title>BackUP Information</title>')
    f_html.write("""<table border="1" style='font-style: bold; color:black; font-family:courier; font-size: 16px;'>""")

    header=0
    cols=['Date and Time','Backup Folder','Server IP','Status']

    for val in cols:
        f_html.write("""<td height="40" width=20% style="background-color: bisque;font-size: 20;color:red;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">""" + val + '</td>')
    
    for row in reader: # Read a single row from the CSV file

        col=0
        f_html.write('<tr>')
        for column in row: # For each column..

            #print ("Headers : "+column )
            #f_html.write("""<td height="40" style="background-color: bisque;font-size: 20;color:red;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">""" + column + '</td>')
            
            print("column : "+column )
            f_html.write("""<td height="25" style="background-color: bisque;font-size: 17;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">""" + column + '</td>')

            col+=1

        print("\n....")
        f_html.write('</tr>')
        header+=1

    f_html.write("""</table></body></html>""")
    f_html.close()


#Calling CSV for server 201,202 and 203

#Get_Html("Database","DB1.csv","DB1.html")
Get_Html(sys.argv[1],sys.argv[2],sys.argv[3])


