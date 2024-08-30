# import pycountry
import time

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.forms import DriverStandingForm
from .sync import SyncBase


class SyncDriverStandings(SyncBase):

    def sync(self):
        self.initialize_driver()
        try:
            pass
        except Exception as e:
            print(f'情報の取得に失敗しました: {e}')


sync_driver_standingss = SyncDriverStandings()
