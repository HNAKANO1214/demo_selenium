# import pycountry
import time

from abc import ABC, abstractmethod
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SyncBase(ABC):
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        if self.driver is None:
            self.options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(
                command_executor='http://selenium:4444/wd/hub',
                options=self.options
            )
            self.driver.implicitly_wait(10)

    def __del__(self):
        if hasattr(self, 'driver') and self.driver is not None:
            self.driver.quit()
            self.driver = None

    @abstractmethod
    def sync(self):
        pass
