from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from PIL import Image
import pathlib


# FOR LOOP TO ADD A main.py TO EACH FOLDER
# for d in */ ; do cp main.py $d/ done

# FOR LOOP TO RUN EACH main.py FILE one directory deep
# for d in */ ; do cd $d/ python3 main.py cd ../ done

# FOR LOOP TO RUN EACH main.py FILE two directories deep
# for d in */ ; do cd $d/ for i in */ ; sdo cd $i/ python3 main.py cd ../ done cd ../ done

# browser says were using chrome for webdriver and links to path I have chromedriver file
options = Options()
options.headless = True
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

current_path = pathlib.Path(__file__).parent.absolute()

html_path = str(current_path).replace("main.py", "index.html", 1)

browser.get('file://' + html_path + '/index.html')

time.sleep(3)

search_input = browser.find_element(By.TAG_NAME, "gwd-page")

time.sleep(3)

# types the parameter string in the google search input
search_input.screenshot(html_path + '/backup.jpg')

time.sleep(2)

browser.quit()

