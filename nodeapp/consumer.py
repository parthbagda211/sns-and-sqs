import redis
import json 
import time 
import threading

r = redis.Redis(host='localhost',port=6379,db=0)


email_queue = 'email_queue'
sms_queue = 'sms_queue'
entity_queue = 'entity_queue'

def email_user():
    while True:
        message_data = r.lpop(email_queue)
        if message_data:
            message = json.loads(message_data)
            print(f"i am  email user and i recive this text form producer :-----{message}")
        time.sleep(3)


def sms_user():
    while True:
        message_data = r.lpop(sms_queue)
        if message_data:
            message = json.loads(message_data)
            print(f"i am  sms user and i recive this text form producer :-----{message}")
        time.sleep(3)

def entity_user():
    while True:
        message_data = r.lpop(entity_queue)
        if message_data:
            message = json.loads(message_data)
            print(f"i am  entity user and i recive this text form producer :-----{message}")
        time.sleep(3)


if __name__ == "__main__":
    email_user_thred = threading.Thread(target=email_user)
    sms_user_thred =threading.Thread(target=sms_user)
    entity_user_thred = threading.Thread(target=entity_user)


    email_user_thred.start()
    sms_user_thred.start()
    entity_user_thred.start()


    email_user_thred.join()
    sms_user_thred.join()
    entity_user_thred.join()