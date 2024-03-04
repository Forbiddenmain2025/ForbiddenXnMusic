from ForbiddenXnMusic.core.bot import Anony
from ForbiddenXnMusic.core.dir import dirr
from ForbiddenXnMusic.core.git import git
from ForbiddenXnMusic.core.userbot import Userbot
from ForbiddenXnMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
