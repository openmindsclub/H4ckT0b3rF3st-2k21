''' All command line prompts and actions '''
from PyInquirer import prompt
import requests
from yts_api import list_movies, movie_detail


def run():
    ''' Keep prompting the user about which action to take'''
    main_prompt = {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Search a movie',
            'Download a movie',
            'Exit'
        ]
    }
    action = ''
    while True:
        action = prompt(main_prompt)['action']
        if action == 'Exit':
            return 0
        treat_action(action)


def treat_action(action):
    ''' Call the right function depending on the user's input '''
    switch = {
        'Search a movie': search,
        'Download a movie': download
    }

    instruction = switch.get(action)
    instruction()


def search():
    ''' Prompt the user to search for a movie using a keyword and display results '''
    search_prompt = {
        'type': 'input',
        'name': 'query',
        'message': 'Which movie are you looking for?'
    }

    query = prompt(search_prompt)['query']

    # TODO: Catch possible exceptions
    results = list_movies(query_term=query)

    if results['movie_count'] == 0:
        print('\nNo movie found.\n')
        return
    print()
    for movie in results['movies']:
        print(f"#{movie['id']}-{movie['title']}({movie['year']})")
    print()

def download():
    ''' Prompt the user to enter a movie_id and download the corresponding movie'''
    download_prompt = {
        'type': 'input',
        'name': 'movie_id',
        'message': 'Which movie do  you want to download (Enter id)'
    }

    movie_id = prompt(download_prompt)['movie_id']

    # TODO: Catch possible exceptions
    movie = movie_detail(movie_id)
    if not movie:
        print('\nNo corresponding movie found.\n')
        return None
    movie = movie['movie']

    # TODO: Prompt the user about which quality to download depending on the available ones

    link = movie['torrents'][0]['url']
    file = requests.get(link, allow_redirects=True)

    open(f"{movie['title']}.torrent", 'wb').write(file.content)

    print(f"\n{movie['title']}.torrent saved successfully! Open it with a torrent client (BitTorrent, μTorrent...) to download the movie \n")
