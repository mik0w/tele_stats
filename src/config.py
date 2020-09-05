from telethon import TelegramClient
import configparser


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