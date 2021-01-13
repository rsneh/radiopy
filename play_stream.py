import vlc
import time

instance = vlc.Instance()

# Create a MediaPlayer with the default instance
player = instance.media_player_new()

# Load the media file
url = 'http://glzwizzlv.bynetcdn.com/glglz_mp3'
media = instance.media_new(url)

# Add the media to the player
player.set_media(media)

# Play for 10 seconds then exit
player.play()
time.sleep(10)
