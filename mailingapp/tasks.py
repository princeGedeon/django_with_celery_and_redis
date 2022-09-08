
from celery.utils.log import get_task_logger

from mailingapp.email import send_review_email

from monprojetcelery.celery import app

logger=get_task_logger(__name__)

@app.task(name="send_review_email_task")
def send_review_email_task(name,email,review):

    logger.info("Sent")
    return send_review_email(name,email,review)