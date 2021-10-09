from zipfile import ZipFile
zipObj = ZipFile('sample.zip', 'w')
zipObj.write('passport9581.png')
zipObj.close()
