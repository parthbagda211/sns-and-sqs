import redis
import json 
import uuid 
from sqs import send_message_to_email_queue,send_message_to_entity_queue,send_message_to_sms_queue

r = redis.Redis(host='localhost',port=6379,db=0)

message_name = 'send invitation'

def create_topic():
    if not r.exists(message_name):
        r.set(message_name,json.dumps({message_name}))
        print(f"message is created : {message_name}")
        return message_name
    else:
        print(f"message { message_name } already exists")
        return None 
    

def subscribe_to_topic(protocol,endpoint):

    if r.exists(message_name):
        message_data = json.loads(r.get(message_name))
        sub_id = str(uuid.uuid4())
        subscription = {
            'id': sub_id,
            'protocol': protocol,
            'endpoint': endpoint
        }
        message_data['subscriptions'].append(subscription)
        r.set(message_name, json.dumps(message_data))
        print(f"Subscribed {endpoint} to message name {message_name}")
        return sub_id
    


def publish_message(message,subject=None):

    if r.exists(message_name):
        message_data = json.loads(r.get(message_name))
        subscriptions = message_data['subscriptions']
        message_id = str(uuid.uuid4())
        message_data = {
            'id': message_id,
            'topic': message_name,
            'subject': subject,
            'message': message
        }

        for subscription in subscriptions:
            
            print(f"sending message to {subscription['endpoint']}")
            send_message_to_email_queue(message_data)

            print(f"sending message to {subscription['endpoint']}")
            send_message_to_sms_queue(message_data)

            print(f"sending message to {subscription['endpoint']}")
            send_message_to_entity_queue(message_data)
            
        
        r.push('email_queue',json.dumps(message_data))
        r.push('sms_queue',json.dumps(message_data))
        r.push('entity_queue',json.dumps(message_data))
        print(f"published message with id : {message_id}")
        return message_id
    
    else:
        print(f"message name {message_name} does not exist")
        return None