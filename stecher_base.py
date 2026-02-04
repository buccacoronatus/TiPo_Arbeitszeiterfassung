import time

class Time_Poker():
    def __init__(self):
        self.Jahr = time.localtime()[0]
        self.Monat = time.localtime()[1]
        self.Tag = time.localtime()[2]
        self.Wochentag = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time.localtime()[6]]
        self.start = time.time()

    def start(self):
        input('Taste drücken zum beenden und speichern')
        self.write_to_csv(self)
    
    def pause():
        pass
    
    def calculate_stunden(self):
        return round(round((time.time() - self.start) / 3600, 1) * 2) / 2
    
    def write_to_csv(self):
        csv_string = f'{self.Wochentag}, {self.Jahr}, {self.Monat}, {self.Tag}, {timer.calculate_stunden()}\n'
        print(csv_string, sep="")

        with open('.//test_data.csv', 'a', encoding="UTF-8") as data_file:
            data_file.write(csv_string)

timer = Time_Poker()
timer.start()
