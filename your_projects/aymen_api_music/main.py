mport tekore as tk

app_token = tk.request_client_token("b516728497b34264afab4e995b4e2569", "0a0fec97699443d6b1a25b875f17325a")
spotify = tk.Spotify(app_token)


def menu():

    print("search for:\n1. Artist\n2. Album\n3. Track ")
    num = input("type your input there : ")
    if num == "1":
        artist_name = input("what's the artist name : ")
        searh_string = "artist:" + artist_name
        artists, = spotify.search(searh_string, types=('track',), limit=50)
        print_article(artists)
    elif num == "2":
        album_name = input("what's the album name : ")
        searh_string = "album:" + album_name
        album, = spotify.search(searh_string, types=('track',), limit=50)
        print_article(album)
    elif num == "3":
        track_name = input("what's the track name : ")
        tracks, = spotify.search(track_name, types=('track',), limit=50)
        print_article(tracks)
    else:
        print("what did you just type? try again!")
    menu()

def print_article(element):
    print ("{:<10} {:<70} {:<40}".format("popularity", "name", "artist"))
    for elem in element.items:
        print ("{:<10} {:<70} {:<40}".format(elem.popularity , elem.name, elem.artists[0].name))


if __name__ == '__main__':
    menu()