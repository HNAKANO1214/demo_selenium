from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        super().ready()

        from core.tasks.sync import sync_constructor_standings, sync_driver_standings, sync_race_results
        executors = {
            'default': ThreadPoolExecutor(3)
        }
        scheduler = BackgroundScheduler(executors=executors)
        now_year = datetime.now().year
        scheduler.add_job(
            sync_constructor_standings.sync, 'interval', hours=24,
            kwargs={'since': now_year, 'until': now_year},
        )
        scheduler.add_job(
            sync_driver_standings.sync, 'interval', hours=24,
            kwargs={'since': now_year, 'until': now_year}
        )
        scheduler.add_job(
            sync_race_results.sync, 'interval', hours=24,
            kwargs={'since': now_year, 'until': now_year},
        )
        scheduler.start()
