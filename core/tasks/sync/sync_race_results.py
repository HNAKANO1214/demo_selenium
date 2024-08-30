import logging
import time

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.forms import RaceResultForm
from core.models import RaceResultModel
from .sync import SyncBase


logger = logging.getLogger(__name__)


class SyncRaceResults(SyncBase):

    def sync(self):
        logger.info('=== Start Sync Race Results ===')
        try:
            self.initialize_driver()
            # 1950年から2024年までのレース結果を取得
            for year in range(1950, 2025):

                race_results = []
                url = f'https://www.formula1.com/en/results/{year}/races'
                self.driver.get(url)

                logger.info(f'Target URL: {url}')
                # テーブル行要素の取得
                for target_css in ['tr.bg-brand-white', 'tr.bg-grey-10']:
                    # 特定の要素が表示されるまで待機（最大10秒）
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, target_css))
                    )
                    rows = self.driver.find_elements(By.CSS_SELECTOR, target_css)
                    if target_css == 'tr.bg-brand-white':
                        # 1つめはヘッダー行のため削除する
                        rows.pop(0)

                    # 各行の情報を取得
                    for row in rows:
                        try:
                            # 国名
                            country_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(1) a')))
                            country = (country_element.text
                                       if country_element and country_element.text else '')
                            # 日付
                            date_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(2) p')))
                            date = (datetime.strptime(date_element.text, "%d %b %Y").date()
                                    if date_element and date_element.text else '')
                            # 勝者
                            winner_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(3) p')))
                            winner = (winner_element.text
                                      if winner_element and winner_element.text else '')
                            # 車
                            car_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(4) p')))
                            car = (car_element.text
                                   if car_element and car_element.text else '')
                            # ラップ数
                            laps_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(5) p')))
                            laps = (laps_element.text
                                    if laps_element and laps_element.text else '0')
                            # タイム
                            race_time_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(6) p')))
                            race_time = (race_time_element.text
                                         if race_time_element and race_time_element.text
                                         else '00:00:00')

                        except Exception as row_e:
                            logger.error(f'グランプリ情報の取得に失敗しました: {row_e}')

                        # logger.debug(
                        #     f'{str(year)}: {country} {date} {winner} {car} {laps} {race_time}')

                        if RaceResultForm.check_exists_season(
                                season=str(year), grand_prix=country):
                            logger.info(f'{year}年 {country}GPの結果は既に取得済みです。スキップします')
                            continue

                        if not RaceResultForm.check_unique(
                            race_results=race_results,
                            grand_prix=country, race_date=date, season=str(year)
                        ):
                            logger.warning('取得したグランプリ情報に重複があるためスキップします')
                            continue

                        form = RaceResultForm(data={
                            'grand_prix': country,
                            'race_date': date,
                            'winner': winner,
                            'car': car,
                            'laps': int(laps),
                            'race_time': race_time,
                            'season': str(year)
                        })
                        if form.is_valid():
                            model_instance = form.save(commit=False)
                            race_results.append(model_instance)
                        else:
                            logger.error(f'取得したグランプリ情報が不正です: {form.errors}')

                # レース結果を保存
                if race_results:
                    try:
                        RaceResultModel.objects.bulk_create(race_results)
                        logger.error(f'{year}年のレース結果を登録しました')
                    except Exception as e:
                        logger.error(f'データベースエラーが発生しました: {e}')
                    finally:
                        time.sleep(1)

        except Exception as e:
            logger.error(f'エラーが発生しました。: {e}')
        finally:
            self.__del__()
            logger.info('=== End Sync Race Results ===')


sync_race_results = SyncRaceResults()
