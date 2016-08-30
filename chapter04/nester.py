import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)
            '''
            如使用if indent 加以控制 print_lol(movies, 2, 2)
            依旧会缩进，由此可见其控制并不严谨。
            固采用以下方式：
            '''
            # if indent == True:

