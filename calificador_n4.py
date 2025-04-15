
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calificar_url_n4(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    result = {}
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        thumbs_up = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="thumbs-up"]')))
        thumbs_up.click()
        result["thumbs_up"] = "✅ Click en 'Sí' exitoso"

        star_5 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class*="starRating"] svg:nth-child(5)')))
        star_5.click()
        result["star_5"] = "⭐️ Click en estrella 5 exitoso"

    except Exception as e:
        result["error"] = str(e)
    finally:
        driver.quit()

    return result
