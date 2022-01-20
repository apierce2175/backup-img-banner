from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import pathlib

#  TODOS
# FOR LOOP TO ADD A BACKUP.PY FOLDER TO EACH FOLDER, FOR LOOP TO RUN EACH BACKUP.PY FILE, make headless


# browser says were using chrome for webdriver and links to path I have chromedriver file
options = Options()
options.headless = True
browser = webdriver.Chrome('/Users/apierce/chromedriver/chromedriver', options=options)

current_path = pathlib.Path(__file__).parent.absolute()

html_path = str(current_path).replace("main.py", "index.html", 1)

browser.get('file://' + html_path + '/index.html')

time.sleep(3)

search_input = browser.find_element_by_tag_name('gwd-page')
time.sleep(3)

# types the parameter string in the google search input
search_input.screenshot(html_path + '/backup.jpg')

time.sleep(2)

browser.quit()

