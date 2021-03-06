DEBUG = True
SECRET_KEY = 'secret!'

MUSIC_FOLDER = '/home/vagrant/musicbox/musicbox/static/music/'
UPLOAD_FOLDER = ''.join([MUSIC_FOLDER, 'one'])
ALLOWED_EXTENSIONS = set(['mp3'])

SONG_CHAR_LIMIT = 26
SONGS_LIMIT = 100

CURRENT_MUSIC_PLAYED = 'stream_mp3_current.xml'
STREAM_URL = DEBUG and '127.0.0.1:8000/stream' or 'production/url/'
