class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None
        
class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, norek, nama, saldo):
        new = NodeTabungan(norek, nama, saldo)

        if self.size == 0:
            self.head = new
            self.tail = new

        else:
           new.next = self.head
           self.head = new 

        self.size += 1


    def delete(self, idx):
        t = self.head

        if idx == 0:
            self.head = t.next
            del t
            self.size -= 1
        elif idx == self.size-1:
            while t.next != self.tail:
                t = t.next

            del self.tail
            self.tail = t
            self.tail.next = None
            self.size -= 1
        else:
            for i in range(idx-1):
                t = t.next

            t.next = t.next.next
            del t.next

    def print(self):
        t = self.head
        while t:
            print("Norek : {}" .format(t.no_rekening))
            print("Nama : {}" .format(t.nama))
            print("Saldo : {}" .format(t.saldo))
            print()

            t = t.next


    

slnc=SLNC()

slnc.insert_head(201,"Hanif",250000)
slnc.insert_head(101,"Yudha",150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()