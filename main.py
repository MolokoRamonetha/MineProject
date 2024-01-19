import schedule
import time

def job():
    # Place your code here that you want to run every 30 minutes
    print("Job is running...")

# Schedule the job to run every 30 minutes
schedule.every(.5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
