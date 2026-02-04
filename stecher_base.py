import time

class TimePoker():
    def __init__(self):
        self.jahr = time.localtime()[0]
        self.monat = time.localtime()[1]
        self.tag = time.localtime()[2]
        self.wochentag = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time.localtime()[6]]
        self.start = time.time()

    def run(self):
        input('Taste drücken zum beenden und speichern')
        self.write_to_csv()
    
    def pause():
        pass
    
    def calculate_stunden(self):
        return round(round((time.time() - self.start) / 3600, 1) * 2) / 2
    
    def write_to_csv(self):
        csv_string = f'{self.wochentag}, {self.jahr}, {self.monat}, {self.tag}, {self.calculate_stunden()}\n'
        print(csv_string, sep="")

        with open('.//test_data.csv', 'a', encoding="UTF-8") as data_file:
            data_file.write(csv_string, sep="")

timer = TimePoker()
timer.run()

# csv.writer