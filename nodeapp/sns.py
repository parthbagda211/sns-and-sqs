import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def publish_message(message, subject=None):
    message_data = {
        'message': message,
        'subject': subject
    }
    r.rpush('email_queue', json.dumps(message_data))
    r.rpush('sms_queue', json.dumps(message_data))
    r.rpush('entity_queue', json.dumps(message_data))
    print(f"Published message: {message}")

