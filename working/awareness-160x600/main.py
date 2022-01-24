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


# FOR LOOP TO ADD A main.py TO EACH FOLDER
# for d in */ ; do cp main.py $d/ done

# browser says were using chrome for webdriver headlessly (you dont see the actions happen. This is faster and you can use computer while tasks happen in bg)
options = Options()
options.headless = True
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

browser.quit()
