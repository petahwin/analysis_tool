import configparser
import json
import spotipy
from spotipy import oauth2 as spoauth

def parse_credentials_config(file_name):
    """Parses configuration file for Spotify Web API client credentials

    Returns dict of client_id => str, client_secret => str

    Expects config ini file of form 
    [credentials]
    client_id = <string>
    client_secret = <string>

    Throws
    - KeyError
    """
    CLIENT_ID_KEY = 'client_id'
    CLIENT_SECRET_KEY = 'client_secret'
    CREDENTIALS_KEY = 'credentials'

    conf = configparser.ConfigParser()
    conf.read(file_name)

    return {
        CLIENT_ID_KEY: conf[CREDENTIALS_KEY][CLIENT_ID_KEY],
        CLIENT_SECRET_KEY: conf[CREDENTIALS_KEY][CLIENT_SECRET_KEY]
    }

def main():
    credentials_table = parse_credentials_config('config.ini')
    
    credentials = spoauth.SpotifyClientCredentials(**credentials_table)
    sp = spotipy.Spotify(client_credentials_manager=credentials)

    ARTIST_ID = '2BTZIqw0ntH9MvilQ3ewNY'
    print(json.dumps(sp.artist(ARTIST_ID)))

if __name__ == "__main__":
    main()
