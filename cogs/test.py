import cogs.TwitchAPI as Twitch

user_login = 'demomute'
query = Twitch.get_user_query(user_login)

response = Twitch.get_response(query)

Twitch.print_response(response)