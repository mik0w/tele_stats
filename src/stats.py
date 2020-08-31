import telethon
import configparser
from telethon import TelegramClient
from operator import itemgetter


class Config:

    def __init__(self, config_path):

        self.username, self.api_id, self.api_hash, self.group_id = self.read_config(config_path)
        self.client = TelegramClient(self.username, int(self.api_id), str(self.api_hash))

    def read_config(self, config_path):

        config = configparser.ConfigParser()
        config.read(config_path)

        api_id = config['Telegram']['api_id']
        api_hash = config['Telegram']['api_hash']
        username = config['Telegram']['username']
        if config['Telegram']['group_id']:
            group_id = int(config['Telegram']['group_id'])
        else:
            group_id = None
        return username, api_id, api_hash, group_id


class GroupTools:

    def __init__(self, client, **kwargs):
        self.client = client
        self.group_id = kwargs.get('group_id', None)

    async def list_all_users(self):
        participants_data = []

        all_participants = await self.client.get_participants(self.group_id, aggressive=True)
        for participant in all_participants:
            participant = {"id": participant.id,
                           "first_name": participant.first_name,
                           "last_name": participant.last_name,
                           "count": 0}
            participants_data.append(participant)
        return participants_data

    async def count_user_stats(self):
        participants_data = await self.list_all_users()
        async for message in client.iter_messages(self.group_id):
            for participant in participants_data:
                if participant['id'] == message.from_id:
                    participant['count'] += 1
        participants_sorted = sorted(participants_data, key=itemgetter('count'), reverse=True)
        return participants_sorted

    async def get_messages_with_content(self, content):
        pass


config = Config("../config.ini")
client = config.client


async def main():
    test = GroupTools(client, group_id=config.group_id)
    participants_data = await test.count_user_stats()
    print(str(participants_data))


with client:
    client.loop.run_until_complete(main())

