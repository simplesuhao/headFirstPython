def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            #if indent:
            '''
            如使用if indent 加以控制 print_lol(movies, 2, 2)
            依旧会缩进，由此可见其控制并不严谨。
            固采用以下方式：
            '''
            if indent == True:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)
