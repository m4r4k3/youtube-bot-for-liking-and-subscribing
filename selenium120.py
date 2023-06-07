from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


gmailadd = "m4r4k@gmail.com"
password = "password"
exe ="C:\\path"
url = "https://www.youtube.com/watch?v=VideoId"
service = Service(exe)
op = webdriver.ChromeOptions()

op.add_argument("--disable-images")
op.add_argument("--disable-blink-features=AutomationControlled")
op.add_experimental_option("detach", True)
op.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'")

driver = webdriver.Chrome(service=service ,options=op )

driver.get(url)
wdw(driver , 10).until(
    ec.presence_of_element_located((By.XPATH ,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'))
)
driver.find_element(By.XPATH ,value='//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
wdw(driver , 10).until(
    ec.presence_of_element_located((By.XPATH ,'//*[@id="identifierId"]'))
)
driver.find_element(By.XPATH ,value='//*[@id="identifierId"]').send_keys(gmailadd)
driver.find_element(By.XPATH ,value='//*[@id="identifierNext"]/div/button').click()
wdw(driver , 10).until(
    ec.presence_of_element_located((By.XPATH ,'//*[@id="password"]/div[1]/div/div[1]/input'))
)

driver.execute_script(
   f"""
    document.querySelector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").value='{password}'
    setTimeout(()=>
    {'{document.querySelector("#passwordNext > div > button").click()}'},100)
    """
)
wdw(driver , 10).until(
    ec.visibility_of_element_located((By.XPATH ,'//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div'))
)
driver.find_element(By.XPATH , value='//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div').click()
wdw(driver , 10).until(
    ec.visibility_of_element_located((By.CSS_SELECTOR ,'#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape > button'))
)
driver.find_element(By.CSS_SELECTOR , value='#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape > button').click()
driver.close()