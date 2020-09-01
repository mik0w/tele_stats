import telethon
import configparser
from telethon import TelegramClient
from operator import itemgetter
from pyfiglet import Figlet
from clint.textui import colored, indent, puts
from aioconsole import ainput
import sys


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
        # TODO
        pass


class ChatTools:
    # TODO
    pass


class IntTools:
    # TODO
    pass


class CLI:

    def __init__(self, client):
        self.client = client
        self.display_logo()

        if len(sys.argv) == 1:
            self.get_help()

    def display_logo(self):
        f = Figlet(font='slant')
        print(f.renderText('telestats'))

    async def run_command(self):
        command = await ainput(">> ")
        if str(command) == 'help':
            self.get_help()
        else:
            pass
            # for word in command:
            #     print(str(word))
        return command

    async def arg_command(self):

        if sys.argv[1] == 'list_users':
            if (sys.argv[2] == '-i') | (sys.argv[2] == '--id'):

                group_id = int(sys.argv[3])
                group_tools = GroupTools(self.client, group_id=group_id)
                all_users_dict = await group_tools.list_all_users()
                puts(colored.blue('Users of group: ' + str(group_id)))
                for user in all_users_dict:
                    print(str(user))

            elif (sys.argv[2] == '-n') | (sys.argv[2] == '--name'):
                # TODO listing users basing on the group name
                print(sys.argv[2])
            else:
                print('Option: ' + sys.argv[2] + ' not recognized.')
                self.get_help()
        elif (sys.argv[1] == '--help') | (sys.argv[1] == '-h'):
            self.get_help()
        elif sys.argv[1] == 'get_group_id':
            pass
        elif sys.argv[1] == 'get_all_group_ids':
            pass
        elif sys.argv[1] == 'count_user_stats':
            pass
        else:
            print('Command: ' + str(sys.argv) + ' not recognized. Please use -h or --help to check options.')



    def get_help(self):
        with indent(4):
            puts(colored.yellow("## ABOUT ##"))
        puts('Telestats is a tool for getting stats from Telegram chats with Telegram-oriented OSINT features.')
        with indent(4):
            puts(colored.yellow("## USAGE ##"))
        puts('Telestats is the Python3 script - you can run it in the following way: \n '
             '\'python3 telestats.py [ACTION] [PARAMETERS] \'')
        puts('\nActions:')
        with indent(2):
            puts(colored.blue('get_group_id [group_name]') + ' - gets the unique id of telegram group')
            puts(colored.blue('get_all_group_ids') + ' - gets all of the group ids from your chat history')
            puts(colored.blue('list_users -i [group_id]') + ' - list all users from the given group (basing on group id)')
            puts(colored.blue('count_user_stats -i [group_id]') + ' - count how many messages have been sent by all of the users of the given group (basing on group id) -> '
                 + colored.red('WARNING: way too slow for groups with > 100000 messages'))
            puts(colored.blue('list_users -n [group_name]') + ' - list all users from the given group (basing on group name)')
            puts(colored.blue('count_user_stats -n [group_name]') +
                 ' - count how many messages have been sent by all of the users of the given group (basing on group name) -> '
                 + colored.red('WARNING: way too slow for groups with > 100000 messages'))


config = Config("../config.ini")
client = config.client


async def main():

    cli = CLI(client)
    if len(sys.argv) == 1:
        await cli.run_command()
    elif len(sys.argv) > 1:
        await cli.arg_command()

with client:
    client.loop.run_until_complete(main())

