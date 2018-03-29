class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        print(self.year)
        print(self.month)
        print(self.day)


t = Data_test(2013, 2, 4)
t.out_date()
