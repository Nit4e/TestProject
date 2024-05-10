import utils


class Worker():
    def __init__(self):
        """Constructor"""
        super().__init__()

    def add_numbers(self, a, b):
        c = utils.sum_me(a, b)
        return c


# def main():
    # c = add_numbers(3, 5)
    # print(c)
# 
# if __name__ == '__main__':
    # main()