import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def body():
    access_token = 'sl.A_ocJmvEsRtb6WcFvPsMQ8RF6i5uX8vFMuMjyEEPHugKo_6oiVW1lg2WtJP-xAGtL5OdQAjcS-aQ1XPE43vU-fTQeVU-uMo5moCr3oelRLA6aappJM_4vYwnR2QRg92cmKrt0mY'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer')
    file_to = input('Enter the full path to upload to dropbox')

        
    transferData.upload_file(file_from, file_to)
    print('file has been moved') 
body() 