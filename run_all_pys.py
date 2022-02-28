#!/usr/bin/env python3

import glob
import os
from subprocess import call
import shutil
import time
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from PIL import Image
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.keys import Keys

# this script places the py file to create backup images in every banner folder, then it runs every py file to create the backup img

# banner_dir needs a trailing slash path of where your banners are. Needs to be a directory and the only directory in the same level as your run_all_pys file. The pathlib path resolve finds the path to where you are running this py file. The os walk finds the directory in this path, and the slashes are to make sure its written as a trailing slash so it can execute.rm a
root_dir = str(pathlib.Path().resolve())

# creates main.py (which creates a backup img from index.html in current folder)

f= open("main.py","w+")

f.write('''\
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from PIL import Image
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.keys import Keys

# FOR LOOP TO ADD A main.py TO EACH FOLDER
# for d in */ ; do cp main.py $d/ done

# browser says were using chrome for webdriver headlessly (you dont see the actions happen. This is faster and you can use computer while tasks happen in bg)
options = Options()
options.headless = True
options.add_argument("window-size=1400,600")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# current path is the file path of where this py file is located
current_path = pathlib.Path(__file__).parent.absolute()

# html path is the path to the html file in the same folder as your py file
html_path = str(current_path).replace("main.py", "index.html", 1)

# opens html banner file
browser.get('file://' + html_path + '/index.html')

# waits to execute next line until the opened page has the element gwd-page loaded (if you dont wait it will run immmediatley and not be able to find the element and not work. If you manually sleep it will add extra time)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "gwd-page")))

# sets banner_area to the banner by finding the tag gwd-page in the html
banner_area = browser.find_element(By.TAG_NAME, "gwd-page")

# wait for text to load
time.sleep(.5)

# screenshots just the banner_area, and saves it as backup.jpg
banner_area.screenshot(html_path + '/backup.jpg')

if os.path.exists(html_path + '/main.py'):
  os.remove(html_path + '/main.py')
  print('aye')
else:
  print(html_path + '/main.py')
  print('naa')

browser.quit()

''')

# flush makes the script write the file at this point, if not the file is not written untill the whole script is executed, meaning there is nothing in main.py when it is called meaning no backup imgs are made
f.flush()

# banner_dir finds where you run this script, then opens one directory deeper to execute the banners
banner_dir = root_dir + '/' + next(os.walk('.'))[1][0] + '/'

# filenamehtml for loop places the main.py file in every folder there is an html (so every banner directory will now have the main.py file in it, the main.py file deletes itself after the script runs so you should never see it but if the backup img appears it works :) )
for filenamehtml in glob.iglob(banner_dir + '**/**.html', recursive=True):
    source = root_dir + "/main.py"
    destination = filenamehtml.replace("index.html", "main.py")
    shutil.copy( source , destination )

# filenamepy runs every py file in current directory. these py files are the scripts that create the backup img.
for filenamepy in glob.iglob(banner_dir + '**/**.py', recursive=True):
    isCopyMain = filenamepy == root_dir + "/main.py"
    isRunPy = filenamepy == root_dir + "/run_all_pys.py"
    if not isCopyMain or not isRunPy:
        def execfile(filepath, globals=None, locals=None):
            if globals is None:
                globals = {}
            globals.update({
                "__file__": filepath,
                "__name__": "__main__",
            })
            with open(filepath, 'rb') as file:
                exec(compile(file.read(), filepath, 'exec'), globals, locals)

        # execute the file
        execfile(filenamepy)

os.remove(source)

