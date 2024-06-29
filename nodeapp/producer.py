import time
import random
import threading
from sns import publish_message  # Assuming publish_message function is defined in sns module

def produce_email():
    while True:
        message = f"This is a message from the producer: {random.randint(1, 100)}"
        subject = 'test message'
        publish_message(message, subject)  # Use the publish_message function from sns module
        time.sleep(5)

if __name__ == "__main__":
    producer = threading.Thread(target=produce_email)
    producer.start()
    producer.join()
