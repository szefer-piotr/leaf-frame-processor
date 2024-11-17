# from gdrive_access import GDriveCommands
# import os

# g = GDriveCommands("settings.yaml")

# print(g.ls('poc_data'))

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

folder_id = '1jo43UcmSVCQNW7iYOjFgjyjpsfi5121P'

file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
for file in file_list:
    print(f'Title: {file["title"]}, ID: {file["id"]}')