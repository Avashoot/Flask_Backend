class Device:

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r}, ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected!!")
    
# creating a printer class which uses above methods and more
# printer = Device("Printer", "Bluetooth")

# print(printer)

# printer.disconnect()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)" 
    
    def print(self, pages):
        if self.connected == False:
            print("Your Printer is not connected")
        else:
            print(f"Printing {pages} pages.")
            self.remaining_pages -= pages
    
printer = Printer("printer", "USB", 2000)
print(printer)
printer.print(49)
print(printer)
printer.disconnect()
printer.print(45)
