# project/tasks/sample_tasks.py

import time

from celery import shared_task


@shared_task
def send_email(email_id, message):
    time.sleep(10)
    print(f"Email is sent to {email_id}. Message sent was - {message}")


@shared_task
def get_micro_app_status(app):
    print(f"La micro app {app}. est UP")


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    print("je suis execueter")
    return True
