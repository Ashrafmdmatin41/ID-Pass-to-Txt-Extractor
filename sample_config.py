import os

api_id = 28308147
api_hash = os.environ.get("API_HASH", "8240cdc945560ccd108b6ff2925ced5e")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5618212564,1227089641")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5618212564")
owner_users = [int(num) for num in osowner_users.split(",")]
