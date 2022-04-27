class xyz:
    def __init__(self):
        print("hey, I am initialized , xyz")

    def sub_xyz(self, b):
        print("Printing from class xyz:", b)


class xyz1(xyz):
    def __init__(self):
        print("hey, I am initialized, xyz1")
        super().__init__()

    def sub_xyz(self, b):
        print("Printing from class xyz1:", b)
        super().sub_xyz(b + 1)


class xyz2(xyz1):
    def __init__(self):
        print("hey, I am initialized, xyz2")
        super().__init__()

    def sub_xyz(self, b):
        print("Printing from class xyz2:", b)
        super().sub_xyz(b + 1)


ob = xyz2()
ob.sub_xyz(10)
