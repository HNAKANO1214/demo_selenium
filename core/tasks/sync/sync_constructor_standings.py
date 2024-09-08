import logging
import time

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.forms import ConstructorStandingForm
from core.models import ConstructorStandingModel
from .sync import SyncBase


logger = logging.getLogger(__name__)


class SyncConstructorStandings(SyncBase):

    def sync(self, since=1958, until=datetime.now().year):
        logger.info('=== Start Sync Constructor Standings ===')
        try:
            self.initialize_driver()
            # 1950年から2024年までのレース結果を取得
            for year in range(since, until + 1):

                drivers_results = []
                url = f'https://www.formula1.com/en/results/{year}/team'
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
                            # 順位
                            position_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(1) p')))
                            position = (position_element.text
                                        if position_element and position_element.text else '')
                            # チーム
                            team_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(2) a')))
                            team = (team_element.text
                                    if team_element and team_element.text else None)
                            # ポイント
                            points_element = WebDriverWait(row, 10).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'td:nth-child(3) p')))
                            points = (points_element.text
                                      if points_element and points_element.text else '0')
                        except Exception as row_e:
                            logger.error(f'グランプリ情報の取得に失敗しました: {row_e}')

                        form = ConstructorStandingForm(data={
                            'constructor': team,
                            'position': position,
                            'points': float(points),
                            'season': str(year)
                        })
                        if form.is_valid():
                            model_instance = form.save(commit=False)
                            drivers_results.append(model_instance)
                        else:
                            logger.error(f'取得したコンストラクターランキングが不正です: {form.errors}')

                        logger.debug(
                            f'{str(year)}: {position} {team} {points}')

                # レース結果を保存
                if drivers_results:
                    try:
                        # 更新対象のシーズンのデータを洗い替え
                        ConstructorStandingModel.objects.filter(season=str(year)).delete()
                        ConstructorStandingModel.objects.bulk_create(drivers_results)
                        logger.error(f'{year}年のコンストラクターランキングを登録しました')
                    except Exception as e:
                        logger.error(f'データベースエラーが発生しました: {e}')
                    finally:
                        time.sleep(1)
        except Exception as e:
            print(f'情報の取得に失敗しました: {e}')
        finally:
            self.__del__()
            logger.info('=== End Sync Constructor Standings ===')


sync_constructor_standings = SyncConstructorStandings()
