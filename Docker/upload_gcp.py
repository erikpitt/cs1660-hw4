import tkinter as tk
import tkinter.filedialog as fd
from google.cloud import storage

BUCKET_NAME = 'dataproc-staging-us-central1-1087866645442-s3vafn8p'
CREDS_PATH = 'credentials.json'

files = []

def main():
    window = tk.Tk()
    window.title('GCP Bucket Upload')
    window.geometry('200x200')

    select_button = tk.Button(window, text='Select Files', command=select_files)
    select_button.place(x=48, y=60)

    upload_button = tk.Button(window, text='Upload Files', command=upload_files)
    upload_button.place(x=46.5, y=90)

    window.mainloop()

def select_files():
    global files
    files = fd.askopenfilenames()

def upload_files():
    global files
    if files:
        storage_client = storage.Client.from_service_account_json(CREDS_PATH)
        bucket = storage_client.get_bucket(BUCKET_NAME)

        for file in files:
            file_name = file.split('/')[-1]
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file)

        files = []

if __name__ == '__main__':
    main()