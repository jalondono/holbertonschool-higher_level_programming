#!/usr/bin/python3
if __name__ == "__main__":
        import hidden_4
        dir_str = dir(hidden_4)
        for i in dir_str:
                if i[0] != '_':
                        print(i)
