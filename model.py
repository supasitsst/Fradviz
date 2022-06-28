class DataSource:
    mn = []
    w1 = []
    d1 = []
    h4 = []
    h1 = []
    m30 = []
    m15 = []
    m5 = []

    def __init__(self):
        self.mn = []
        self.w1 = []
        self.d1 = []
        self.h4 = []
        self.h1 = []
        self.m15 = []


class SoupResponse:
    name = ''
    change = 0.0

    def __init__(self, name, change):
        self.name = name
        self.change = change
