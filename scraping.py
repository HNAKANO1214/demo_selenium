from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

driver.implicitly_wait(10)

url = 'https://www.formula1.com/'
driver.get(url)

# Cookie承諾の画面で「すべて拒否」ボタンをクリックする
try:
    # iframe に切り替える
    driver.switch_to.frame("sp_message_iframe_1149950")  # 0 は iframe のインデックスです。IDや名前で指定することもできます。

    # ボタンが表示され、クリック可能になるのを待つ
    reject_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='REJECT ALL']"))
    )
    # ボタンをクリック
    reject_button.click()

except Exception as e:
    print(f'Cookie拒否ボタンのクリックに失敗しました: {e}')
finally:
    # 元のコンテンツに戻る
    driver.switch_to.default_content()



time.sleep(5)

driver.quit()
