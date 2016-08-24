import nester

movies = ['The Holy Grail', 1975,
          'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman', ['Michael Palin', 'John Cleese',
                              'Terry Gilliam', 'Eric Idle',
                              'Terry Jones']]]

'''
for movie in movies:
    if isinstance(movie, list):
        for mov in movie:
            if isinstance(mov, list):
                for mv in mov:
                    print(mv)
            else:
                print(mov)
    else:
        print(movie)
'''


'''
新增print_lol函数，用于自动打印列表
'''

nester.print_lol(movies)
