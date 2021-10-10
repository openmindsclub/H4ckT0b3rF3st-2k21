''' The Program's entry point where the CLI will run '''

import yts_api

if __name__ == '__main__':
    QUERY = ''

    while True:
        # Example: Keep asking the user to search
        # for a movie and display results
        QUERY = input('\n* Search for a movie: ')
        results = yts_api.list_movies(query_term=QUERY)['movies']
        for r in results:
            print(f"{r['id']}-{r['title']}")
