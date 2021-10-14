from gologin.goapi import GoLogin
import time
from selenium import webdriver


gl = GoLogin({
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGU0NjBhZGQyMDk3OWYyZmEwNmE2ZDEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTY0MGFhZjAyMmUxYTI1ZTcyZjA0NmUifQ.6L85fs-NvcqnvxluRDrDHexMKqkWTO0KHGUYMzbW6Og',
    'profile_id': '6165888cb61f167405551ddd',
    # 'tmpdir': 'gologin_6165888cb61f167405551ddd',
    # 'profile_path': 'gologin_6165888cb61f167405551ddd'
    # 'proxy': None,
})
chrome_options = webdriver.ChromeOptions()
debugger_address = gl.start()
print('debugger_address: ', debugger_address)
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()
