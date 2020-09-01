# tele_stats
**tele_stats** is a tool for getting stats from Telegram chats with Telegram-oriented OSINT features.
    
## Usage
Before you run the script itself, you have to fill up the config file:

```
[Telegram]
# you can get telegram development credentials in telegram API Development Tools
api_id = 123456
api_hash = h45hsthsthsth

# use full phone number including + and country code
phone = +8080808080
username = user
# OPTIONAL:  provide group id 
group_id = -123456789 
```

Create the Python 3 virtual environment: `python3 -m venv venv` and activate it:
`source venv/bin/activate`.

Next, install requirements with `pip install -r requirements.txt`

After these steps Telestats should be working.

You can **run it** in the following way: 
`python3 tele_stats.py [ACTION] [PARAMETERS]`

If you run tele_stats.py as `python tele_stats.py`, you will enter an CLI-mode, basically with the same commands as the ones listed below:

For now, you can use the following commands (todo: most of them not implemented so far):
  * `get_group_id [group_name]` - gets the unique id of telegram group
  * `get_all_group_ids` - gets all of the group ids from your chat history
  * `list_users -i [group_id]` - list all users from the given group (basing on group id)
  * `count_user_stats -i [group_id]` - count how many messages have been sent by all of the users of the given group (basing on group id) -> WARNING: way too slow for groups with > 100000 messages
  * `list_users -n [group_name]` - list all users from the given group (basing on group name)
  * `count_user_stats -n [group_name]` - count how many messages have been sent by all of the users of the given group (basing on group name) -> WARNING: way too slow for groups with > 100000 messages

That's very WIP project so far.
