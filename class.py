class room:
    def __init__(self, meja, kursi):
        self.meja = meja
        self.kursi = kursi

    def keterangan(self):
        print(f"informasi lengkap dari meja ada {self.meja} dan kursi ada {self.kursi}")

room1 = room(45, 533)

room1.keterangan()
