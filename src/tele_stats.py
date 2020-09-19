from pyfiglet import Figlet
from clint.textui import colored, indent, puts
from aioconsole import ainput
from group_tools import GroupTools
from config import Config
import sys
import argparse

class ChatTools:
    # TODO
    pass


class IntTools:

    def find_groups_of_user(self):
        pass


class CLI:

    def __init__(self, client):
        self.client = client
        self.display_logo()

    def display_logo(self):
        f = Figlet(font='slant')
        print(f.renderText('telestats'))

    async def arg_command(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count_messages", help="count messages  in the group with the given [id]",
                            action="store_true")
        parser.add_argument("-l", "--list_users", help="show all users in the group with the given [id]",
                            action="store_true")
        parser.add_argument("id", type=int, help="id of the group")
        args = parser.parse_args()
        if args.count_messages:
            group_id = args.id
            group_tools = GroupTools(self.client, group_id=group_id)
            puts(colored.yellow('Counting messages... It may take a while.'))
            participants_data = await group_tools.count_messages()

            puts(colored.blue('Users activity (from the highest) in group: ' + str(group_id)))
            for user in participants_data:
                print(str(user))

        if args.list_users:
            group_id = args.id
            group_tools = GroupTools(self.client, group_id=group_id)
            async for p in group_tools.list_all_users():
                print(str(p))



config = Config("../config.ini")
client = config.client


async def main():

    cli = CLI(client)
    await cli.arg_command()

with client:
    client.loop.run_until_complete(main())

