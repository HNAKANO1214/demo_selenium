# demo_selenium

# ポートフォリオ

## 開発環境構築手順

1. **Dockerコンテナの起動します。**

    ```sh
    docker-compose up
2. **.envの配置**

    ```sh
    cp .env.local .env
3. **データベースのマイグレーションを実行します。**

    ```sh
    docker exec -it demo_selenium-app python manage.py migrate
4. **スーパーユーザーを作成します。**

    ```sh
    docker exec -it demo_selenium-app python manage.py createsuperuser
## 自動テスト

```sh
docker exec -it demo_selenium-app pytest
