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
`python3 tele_stats.py [ACTION] [PARAMETER(S)]`

For now, you can use the following commands (todo: most of them not implemented so far):
  * `-c|--count_messages [group_id]` - count how many messages have been sent by all of the users of the given group (basing on group id) -> WARNING: might get slow.
  * `-l|--list_users [group_id]` - list all users from the given group (basing on group id)

That's very WIP project so far.
