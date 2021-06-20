import urllib
import tweepy
from geopy.geocoders import Nominatim
from pyUFbr.baseuf import ufbr


# Para se utilizar essa API, é necessário obter autorização de acesso como desenvolvedor 
# em (https://developer.twitter.com/en/apply-for-access). Depois de autorizado, você deverá
# gerar as suas chaves (Consumer Keys e Authentication Tokens) e alterar as respectivas 
# chaves no código abaixo. 

# AUTHENTICATION (OAuth)
def tw_oauth():
    # Caso você tenha feito sua própria conta como desenvolvedor
    # substitua suas chaves nas linhas a seguir
    CONSUMER_KEY = "SYFpddpGiwLKmMBaUPellGXki"
    CONSUMER_SECRET = "llbWAFXd5CRvK5GVYwvDPV2dpsHrkz2CVmG5ESXXSg13hnWGJx"
    ACCESS_TOKEN = "234736278-xdQ9DJ3fNTcyRElqD6mNvCFOfyIWgsp9rGvsFPBv"
    ACCESS_TOKEN_SECRET = "0hE4P481ByaOGsiIW95DyEqZfXmQmKtVpJ68GOzwMf896"

    auth1 = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth1)

# TWEEPY SEARCH FUNCTION
def tw_search(api):
    counter = 0

    for tweet in tweepy.Cursor(api.search,
                                q = query,
                                g = local,
                                lang = language,
                                result_type = tp,
                                count = counting).items():
        #TWEET INFO
        created = tweet.created_at   #tweet created
        text    = tweet.text         #tweet text
        tweet_id = tweet.id          #tweet ID (not author ID)
        cords   = tweet.coordinates  #geographic co-ordinates
        retwc   = tweet.retweet_count #re-tweet count
        #AUTHOR INFO
        username  = tweet.author.name            #author/user name
        usersince = tweet.author.created_at      #author/user profile creation date
        followers = tweet.author.followers_count #number of author/user followers (inlink)
        friends   = tweet.author.friends_count   #number of author/user friends (outlink)
        authorid  = tweet.author.id              #author/user ID#
        authorloc = tweet.author.location        #author/user location
        #TECHNOLOGY INFO
        geoenable = tweet.author.geo_enabled     #is author/user account geo enabled?
        source    = tweet.source                 #platform source for tweet

        print(username, text, source, sep=" ; ", end="\n")
       
        counter = counter + 1
        if (counter == cmax):
            break

def get_coord_dict(uf: str):

    if len(uf) == 2:
        uf_name = ufbr.dict_uf.SPget(uf.upper()).get('nome')
    uf_name=uf
    geoLoc = Nominatim(user_agent='GeoHack')
    loc = geoLoc.geocode({"country": "Brazil", "state": uf_name})
    
    return {uf_name: f'{loc.longitude}, {loc.latitude}, 20km'}


# MAIN ROUTINE
def main():

    global api, cmax, locords
    global query, local, language, tp, counting, d

    # Geo-coordinates of five metropolitan areas
    # London, NYC (lower, middle, upper), Wash DC, San Francisco, New Brunswick (NJ)
    # Rio Grande, ...
    
    # Aqui na variável locords voce pode inserir o seu municipio
    # buscando as coordenadas geográficas diretamente no Google
                
    """locords =  {'lo': '0, 51.503, 20km',
                'nyl': '-74, 40.73, 2mi',
                'nym': '-74, 40.74, 2mi',
                'nyu': '-73.96, 40.78, 2mi',
                'dc': '-77.04, 38.91, 2mi',
                'sf': '-122.45, 37.74, 10km',
                'nb': '-74.45, 40.49, 2mi',
                'rg': '-52.05, -32.02, 10km}# Rio Grande"""

    uf = input("Informe a UF brasileira: ")
    locords = get_coord_dict(uf)
    print(f'Critérios de busca: {locords}')
    query = input("Informe o tema de interesse: ")            
    # Maximum allowed tweet count (note: Twitter sets this to ~180 per 15 minutes)
    cmax = 100
    local = 'mt'  #'lo', 'nyl', 'nym', 'nyu', 'dc', 'sf', 'nb', 'rg'
    language  = 'pt'  #'en','fr','es','pt'
    tp  = 'popular' #'mixed','recent','popular'
    counting  = 100 
    # Function to get authorization from Twitter
    api = tw_oauth()
    # Function to search data in Twitter
    tw_search(api)

if __name__ == "__main__":
    main()