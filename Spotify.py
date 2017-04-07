"""
REQUIREMENTS: Spotify Module; Internet Access.
GOALS: This script provide a simple way of interacting with Spotify's API.
Provide an artist name and the program will fetch the information about the artist from Spotify's Database.

Code by: Leo Neto
Spring 2017


ArtistAlbums(string):
This function fetches all the albums by a given artist available on Spotify.
The name of the artist is passed as a string but within the function,
the argument is used to search for the artist Spotify URI.


GetArtistInfo(string):
Will get some basic information about an artist, like Spotify ID and number of followers.
The current functionality can easily be extended with the use of a few more variables and parameters.

TopSongs(string):
----

Portfolio(string):
---

"""

import spotipy

spotify = spotipy.Spotify()




class SpotifyProfile:

    def ArtistAlbums(self,artistName):
        theArtist = spotify.search(q='artist:' + artistName, type='artist')
        items = theArtist['artists']['items']
        artist_uri = items[0]['uri']

        theAlbums = spotify.artist_albums(artist_uri, album_type='album')
        albums = theAlbums['items']

        while theAlbums['next']:
            theAlbums = spotify.next(theAlbums)
            albums.extend(theAlbums['items'])
        for album in albums:
            print(album['name'])
    #end ArtistAlbums(string)


    def GetArtistInfo(self,argument):
        results = spotify.search(q='artist:' + argument, type='artist')
        items = results['artists']['items']

        name = items[0]['name']
        id = items[0]['id']
        followers = items[0]['followers']['total']
        profile = items[0]['uri']
        tracks = spotify.artist_top_tracks(id)

        if len(items) > 0:
            print("ID       : {}".format(id))
            print("Artist   : {}".format(name))
            print("Followers: {}".format(followers))
    #end GetArtistInfo(string)


    def TopSongs(self,argument):
        results = spotify.search(q='artist:' + argument, type='artist')
        items = results['artists']['items']
        name = items[0]['name']
        id = items[0]['id']
        followers = items[0]['followers']['total']
        profile = items[0]['uri']

        tracks = spotify.artist_top_tracks(id)
        for track in tracks['tracks'][:10]:
            print('track    : ' + track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()
    #end TopSongs(string)


    def Portfolio(self,artistName):
        print("ARTIST INFO: ")
        self.GetArtistInfo(artistName)
        self.Lines()

        print("ALBUMS: ")
        self.ArtistAlbums(artistName)
        self.Lines()

        print("TOP SONGS: ")
        self.TopSongs(artistName)
        self.Lines()
    #end ArtistPortfolio(string)

    def Lines(self):
        print("___________________________")
        print()
    #end Lines()

#end Class



def main():
    name = input("Artist's name: ")
    artist = SpotifyProfile()
    artist.Portfolio(name)


if __name__ == "__main__":
    main()
