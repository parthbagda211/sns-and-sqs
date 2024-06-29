import redis 
import json 

r = redis.Redis(host='localhost',port=6379,db=0)


email_queue = 'email_queue'
sms_queue = 'sms_queue'
entity_queue = 'entity_queue'

def send_message_to_email_queue(message_data):
    if r.llen(email_queue)<1000:
        r.rpush(email_queue,json.dumps(message_data))
        print(f"sent email to email User")
    else:
        print(f"email queue is full, message dropped")

def send_message_to_sms_queue(message_data):
    if r.llen(sms_queue)<1000:
        r.rpush(email_queue,json.dumps(message_data))
        print(f"sent email to email User")
    else:
        print(f"email queue is full, message dropped")

def send_message_to_entity_queue(message_data):
    if r.llen(entity_queue)<1000:
        r.rpush(email_queue,json.dumps(message_data))
        print(f"sent email to email User")
    else:
        print(f"email queue is full, message dropped")