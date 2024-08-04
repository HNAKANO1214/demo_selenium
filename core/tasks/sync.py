# import pycountry
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.forms import ConstructorStandingForm, DriverStandingForm, RaceResultForm


def sync():

    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )

    driver.implicitly_wait(10)

    try:
        # 1950年から2024年までのレース結果を取得
        for year in range(2024, 2025):
            url = f'https://www.formula1.com/en/results/{year}/races'
            driver.get(url)

            # テーブル行要素の取得
            for target_css in ['tr.bg-brand-white', 'tr.bg-grey-10']:
                # 特定の要素が表示されるまで待機（最大10秒）
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, target_css))
                )
                rows = driver.find_elements(By.CSS_SELECTOR, target_css)

                # 各行の情報を取得
                for row in rows:
                    try:
                        # 国名
                        country_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(1) a'))
                        )
                        country = country_element.text
                        # 日付
                        date_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(2) p'))
                        )
                        date = datetime.strptime(date_element.text, "%d %b %Y").date()
                        # 勝者
                        winner_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(3) p'))
                        )
                        winner = winner_element.text
                        # 車
                        car_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(4) p'))
                        )
                        car = car_element.text
                        # ラップ数
                        laps_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(5) p'))
                        )
                        laps = laps_element.text
                        # タイム
                        race_time_element = WebDriverWait(row, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'td:nth-child(6) p'))
                        )
                        race_time = race_time_element.text
                        # 情報の表示
                        print(f'国名: {country}, 日付: {date}, 勝者: {winner}, 車: {car}, ラップ数: {laps}, タイム: {race_time}')

                        form_data: dict = {
                            'grand_prix': country,
                            'race_date': date,
                            'winner': winner,
                            'car': car,
                            'laps': int(laps),
                            'race_time': race_time,
                            'season': str(year)
                        }
                        form = RaceResultForm()

                    except Exception as row_e:
                        print(f'行の情報取得に失敗しました: {row_e}')

    except Exception as e:
        print(f'情報の取得に失敗しました: {e}')

    finally:
        # ブラウザを閉じる
        driver.quit()
