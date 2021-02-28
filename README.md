# HatemailBot

Discord bot that allows users to send hatemail or lovemail to other users in the server. Users can freely contribute to the list of insults or compliments. Be warned, there are no filters for what users can submit!

Requirements:
- A file called `disablelist.json` to store the user IDs of those that wish to opt-out from receiving dms from the bot
- A file called `hatelist.json` to store the list of insults
- A file called `lovelist.json` to store the list of compliments
These files should be within the same directory as the python file. All .json files should be in proper json format (Beginning with \[ and ending with \] is necessary, even for empty files!)
