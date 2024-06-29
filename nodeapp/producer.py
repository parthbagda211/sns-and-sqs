import time
import random 
import threading 
# from sqs import send_message_to_email_queue 
from sns import publish_message



def produce_email():
    while True:
        message = f"this is a message from the produer :{random.randint(1,100)}"
        subject = 'test message'
        publish_message(message,subject)
        time.sleep(5)


if __name__ == "__main__":
    producer =threading.Thread(target=produce_email)
    producer.start()
    producer.join()


