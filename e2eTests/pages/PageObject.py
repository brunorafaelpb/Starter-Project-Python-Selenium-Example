from selenium import webdriver


class PageObject:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_page(self, url):
        is_url = self.driver.current_url == url
        return is_url
