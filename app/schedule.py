from apscheduler.schedulers.blocking import BlockingScheduler
from app.models import monitor_loans
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=20,minute=15)
def scheduled_job():
    monitor_loans()

sched.start()
