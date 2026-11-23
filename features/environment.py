from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    options = Options()

    options.add_argument("--headless=new") 
    options.add_argument("--window-size=1920,1080") 
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-gpu") 
    options.add_argument("--disable-dev-shm-usage") 

    context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    context.driver.quit()