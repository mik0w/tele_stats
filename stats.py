import telethon
import configparser
import json
from telethon import TelegramClient
from operator import itemgetter

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']
group_id = int(config['Telegram']['group_id'])

client = TelegramClient(username, api_id, str(api_hash))

async def main():
    participants_data = []

    all_participants = await client.get_participants(group_id, aggressive=True)
    for participant in all_participants:    
        participant = {"id": participant.id, 
                    "first_name": participant.first_name,
                    "last_name": participant.last_name,
                    "count": 0}
        participants_data.append(participant)

    async for message in client.iter_messages(group_id):
        for participant in participants_data:
            if(participant['id'] == message.from_id):
                participant['count'] = participant['count'] + 1 
    
    participants_sorted = sorted(participants_data, key=itemgetter('count'), reverse=True)  
    print(str(participants_sorted))

with client:
    client.loop.run_until_complete(main())

