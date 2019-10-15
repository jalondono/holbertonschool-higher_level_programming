#!/usr/bin/python3
class MyList(list):
    """
    class my list that inherits from list:
    """
    def print_sorted(self):
        """
        print a sorted list
        :return: a copy of list
        """
        newlist = MyList.copy(self)
        newlist.sort()
        print(newlist)
        return newlist



