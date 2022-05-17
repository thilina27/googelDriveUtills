from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# directory you need to upload
# can get his id from your browser. is the last string of the drive URL
drive_dir = '1QoYV-ddwd-EF1kgeKrDpK'


# list of files you need to upload
upload_file_list = ['file.type', 'file2.type']


for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [{'id': drive_dir}]})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(upload_file)
    gfile.Upload() # Upload the file.
