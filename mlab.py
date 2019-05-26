#mongo ds229826.mlab.com:29826/project_2_tdt -u <dbuser> -p <dbpassword>

import mongoengine

# mongodb://yt_download:123456a@ds229826.mlab.com:29826/project_2_tdt

host = "ds229826.mlab.com"
port = 29826
db_name = "project_2_tdt"
user_name = "yt_download"
password = "123456a"

def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )
