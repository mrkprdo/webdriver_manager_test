from time import sleep
print(f'Testing webdriver_manager for {__file__} inside docker')

def run():
    result = True
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print(driver)
        sleep(10)

        driver.quit()
        
    except Exception as e:
        print(e)
        result = False

    return result