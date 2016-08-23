movies = ['The Holy Grail', 1975,
          'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman', ['Michael Palin','John Cleese',
                              'Terry Gilliam', 'Eric Idle',
                              'Terry Jones']]]
for movie in movies:
    if isinstance(movie, list):
        for mov in movie:
            print(mov)
    else:
        print(movie)