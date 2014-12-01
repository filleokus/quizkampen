Quizkampen API description
Reversed engineered by Filip Nilsson, 2014-11-27

The base url for all the following request is https://quizerver.feomedia.se. There doesn't seem to be any kind of certifacte pinnning or something like that. I can intercept all requests and responses by using Charles with the standard configuration.

My values are in parhantesis.

All the requests include this field in the header:
API-VERSION : The version of the API I presume ("v1.1")

And the follwoing cookie:
remember_token	(BAhbB2kDjGEvIkU5YTQ5NDI5YjRmNDk4NWRmNWE4YzFjZDM4MWIyNjhkYTZiZDJlZThlYjUxZGUxNDAyYTcyNjY2ZmI0MmI5NzZj--0043bd9484d02e632ebe20a1111c3327e8615f1a)

-----
"Refresh of menu view"-request
POST /users/show_games/[userID] with the content:
apn_token=(00d39948%205acc3cba%20cb47f3e7%2053f9ded7%207c7827f4%20e50799dc%202de9e676%20d785fbc2)

Repsonse:
Somekind of JSON-eqse document that contains information about your past and active games, in game-messages, your ranking and some settings.
-----
"Awsnering last question in a round"-request
PUT /qf_games/[gameID] with the content
game_update={"game_state":(4),"user_id":[userID],"my_answers":"(031100002012900020)","categoryChoices":"(212001)"}

The "my_answers"-string contains all my previous answers in the game. The number corresponds to the index of option

Response: Information about the current game
----
"New game"-request
POST /qf_games/new_game/[userID] with the content
player_b_id = [opponentID/-1 for random]

Response: All the possible question and awnsers for different categories


