from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import pathlib

#  TODOS
# FOR LOOP TO ADD A BACKUP.PY FOLDER TO EACH FOLDER, FOR LOOP TO RUN EACH BACKUP.PY FILE, add prints as each step happens to keep you updated

# options make the task headless. meaning it will be faster and perform tasks in bg. if this wasnt on you would see the browser open and screenshot and you would not be able to use computer during process.
# browser says were using chrome for webdriver and links to path I have chromedriver file
options = Options()
options.headless = True
browser = webdriver.Chrome('/Users/apierce/chromedriver/chromedriver', options=options)

# sets html_path to whatever file path is to the folder you run main.py in.
current_path = pathlib.Path(__file__).parent.absolute()
html_path = str(current_path).replace("main.py", "index.html", 1)

# opens the index.html file in folder you run main.py in
browser.get('file://' + html_path + '/index.html')
print("opened the file" + 'file://' + html_path + '/index.html')

time.sleep(3)

# sets banner content to element name that contains all of the banner front end.
banner_content = browser.find_element_by_tag_name('gwd-page')
time.sleep(3)

# screenshots just the banner content (Therefore cropping it to correct size) and saves it as backup.jpg in the same folder you run main.py in
banner_content.screenshot(html_path + '/backup.jpg')
print('screenshotted this banner' + 'file://' + html_path + '/index.html' + 'and saved it in the following location' + html_path + '/backup.jpg')

time.sleep(3)

browser.quit()

