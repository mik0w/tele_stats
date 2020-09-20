from operator import itemgetter
from telethon.tl.types import PeerChannel


class GroupTools:

    def __init__(self, client, group_id=None):
        self.client = client
        if group_id:
            self.group_id = group_id

    async def get_group_entity(self, group_name):
        group_entity = await self.client.get_entity(str(group_name))
        return group_entity

    async def list_all_users(self):
        try:
            for participant in await self.client.get_participants(self.group_id, aggressive=True):
                participant = {"id": participant.id,
                               "first_name": participant.first_name,
                               "last_name": participant.last_name,
                               "phone_number": participant.phone}
                yield participant
        except ValueError:
            error = "Could not find the group with the given ID."
            yield error

    async def count_messages(self):
        participants_data = [p async for p in self.list_all_users()]
        for participant in participants_data:
            participant['count'] = 0
        async for message in self.client.iter_messages(self.group_id):
            for participant in participants_data:
                if participant['id'] == message.from_id:
                    participant['count'] += 1
        participants_sorted = sorted(participants_data, key=itemgetter('count'), reverse=True)
        return participants_sorted

    async def count_messages_of_specific_user(self, **kwargs):
        # based on name or user_id
        pass

    async def get_messages_with_content(self, **kwargs):
        # TODO
        pass