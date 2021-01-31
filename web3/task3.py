import datetime as dt
import schedule

Ku = 'Ку'


def job():
    global Ku
    print(Ku * (dt.datetime.now().hour - 12))


schedule.every().hour.at(':00').do(job)

while True:
    schedule.run_pending()
