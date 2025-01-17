import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

email_queue = 'email_queue'
sms_queue = 'sms_queue'
entity_queue = 'entity_queue'

def send_message_to_email_queue(message_data):
    if r.llen(email_queue) < 1000:
        r.rpush(email_queue, json.dumps(message_data))
        print("Sent message to email queue")
    else:
        print("Email queue is full, message dropped")

def send_message_to_sms_queue(message_data):
    if r.llen(sms_queue) < 1000:
        r.rpush(sms_queue, json.dumps(message_data))
        print("Sent message to SMS queue")
    else:
        print("SMS queue is full, message dropped")

def send_message_to_entity_queue(message_data):
    if r.llen(entity_queue) < 1000:
        r.rpush(entity_queue, json.dumps(message_data))
        print("Sent message to entity queue")
    else:
        print("Entity queue is full, message dropped")
