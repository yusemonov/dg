import os
from gologin.gologin import GoLogin
from dotenv import load_dotenv

load_dotenv('../.env')
TOKEN_GOLOGIN = os.getenv('TOKEN')

gl = GoLogin({
    'token': TOKEN_GOLOGIN
})

profile_list = gl.profiles()
print(profile_list[0])
