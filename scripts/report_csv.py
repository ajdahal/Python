'''
Considerations -
1. Custom User named report is made (manually) whose home folder will be used for collecting the report using scp/sftp by the customer
2. Customer only interacts with home folder of Custom User named report for getting report - enable passwordAuthentication in /etc/ssh/sshd_config and restart sshd for password based authentication or make /home/report/.ssh/authorized_keys file and put public key for sftp to it
3. The name of reports are in understandable format in /home/report/

or 

ChallengeResponseAuthentication yes
UsePAM yes

# Complete the authetication via keyboard 

Please configure this script in crontab according to need
*/59 * * * * /opt/immune/bin/envdo python /home/report/report_csv.py

'''

import os, shutil
import time
import subprocess
import json

from pathlib import Path
from pylib import mongo
import base64
from pylib import textual
import datetime
db = mongo.get_makalu()

parent_dir = "/home/report"
directory = "generated_reports_coll/"
Original_report_location = os.fspath("/opt/makalu/app_store/reports/generatedreports/")
new_path = os.path.join(parent_dir,directory)
mode = 0o766
error_file = os.path.join(parent_dir,"error.txt")
counter_file = os.path.join(parent_dir,"counter.txt")

if not os.path.exists(new_path):
    os.mkdir(new_path,mode)

def write_error(location, error):
    with open(error_file,"a") as record:
        record.write(f"{datetime.datetime.now()}: {location} {error}\n")

def lookup_mongo(report_name):
    generated_report = db.allgeneratedreports.find({"file_name":report_name},{"name":1, "_id":0})
    for encoded_name in generated_report:
        return str(encoded_name["name"])

def rename_reports(report_name):
    if (".") in report_name:
        splitted_text = report_name.split(".")[0]
    else:
        splitted_text = report_name
    get_encoded_filename = lookup_mongo(splitted_text)
    #print(f"\n get_encoded_filename :{get_encoded_filename} \n")
    decoded_report_name = textual.tostring(base64.b64decode(textual.tobytes(get_encoded_filename)))
    #print(f"decoded_report_name is: {decoded_report_name}")
    return decoded_report_name

def rename_operation(new_name, old_name):
    try:
        os.replace(old_name,new_name)
    except Exception as e:
        write_error("rename_operation",e)
    return


def get_file():
        modification_times = {}
        sorted_modification = {}
        if os.path.exists(counter_file):
            with open(counter_file,"r") as fi:
                data = json.load(fi)
                #print(f"\ndata is:{data}\n")
            mod_number = int("".join(str(value) for key, value in data.items()))
        else:
            mod_number = 0
        for root,dirs,file_list in os.walk(Original_report_location):
            #print(f"root, dirs, file_list are : {root} \n {dirs} \n {file_list}")
#            if dirs==[]:
#                last_modification_time = int(float(os.path.getmtime(os.fspath(root))))
#                if last_modification_time > mod_number:
#                    #print(f"last_modification_time: {last_modification_time } and mod_number: {mod_number}")
#                    modification_times[root.split("/")[-1]]=int(float(os.path.getmtime(os.path.join(root))))
#                    subprocess.call(["rsync","-avh",os.path.join(Original_report_location,root.split("/")[-1]),new_path])
#                    new_name = os.path.join(new_path, rename_reports(files) + "_" + str(files.split(".")[0]).split("_")[-1])
#                    old_name = os.path.join(new_path,root.split("/")[-1])
#                    #print(f"old_name for dirs = [], {old_name} and new_name for dirs=[], {new_name}")
#                    rename_operation(new_name,old_name)
#            else:
            for files in file_list:
                #print (f"file names is: {files}")
                if files.split(".")[-1] == "zip":
                    last_modification_time = int(float(os.path.getmtime(os.path.join(root,files))))
                    print(f"last modification time and it's type: {last_modification_time} {type(last_modification_time)}")
                    if last_modification_time > mod_number:
                        modification_times[files]=int(float(os.path.getmtime(os.path.join(root,files))))
                        subprocess.call(["rsync","-avh",os.path.join(Original_report_location,files),new_path])
                        old_name = os.path.join(new_path,files)
                        new_name = os.path.join(new_path,rename_reports(files)+files.split("_")[-1])
                        #print (f"old_name is:{old_name} and new name is:{new_name}")
                        rename_operation(new_name,old_name)
        sorted_modification = sorted(modification_times.items(),key = lambda file_time:file_time[1],reverse=True)
        print(f"sorted_modification: {sorted_modification}")
        if len(sorted_modification) != 0:
            try:
                with open(counter_file,"w") as f:
                    json.dump(dict([next(iter(sorted_modification))]),f)
            except Exception as e:
                write_error("get_file", e)

if __name__=="__main__":
    #subprocess.call(["chown", "-R", "loginspect:loginspect", new_path])
    get_file()
    subprocess.call(["chown", "-R", "report:report", parent_dir])
    write_error("---------------------------------------------------------------","---------------------------------------------------------------")
