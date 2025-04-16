
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def detectar_urls_n4(base_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    time.sleep(3)

    enlaces = driver.find_elements(By.TAG_NAME, "a")
    urls_n4 = set()

    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if href and "/n4/" in href and "ayudaempresas.galicia.ar" in href:
            urls_n4.add(href.strip())

    driver.quit()

    with open("urls_n4_reales.txt", "w", encoding="utf-8") as f:
        for url in sorted(urls_n4):
            f.write(url + "\n")

    return list(urls_n4)
