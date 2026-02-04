import time

class Time_Poker():
    def __init__(self):
        self.Jahr = time.localtime()[0]
        self.Monat = time.localtime()[1]
        self.Tag = time.localtime()[2]
        self.Wochentag = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time.localtime()[6]]

    def take_time(self):
        return time.time()

    def pause():
        pass

    def calculate_stunden(start, end):
        return round(round((end - start) / 3600, 1) * 2) / 2
    
    def write_to_csv(self, start, end):
        print(start, end)
        stunden = round(round((end - start) / 3600, 1) * 2) / 2
        csv_string = f'{self.Wochentag}, {self.Jahr}, {self.Monat}, {self.Tag}, {stunden}\n'
        print(csv_string, sep="")

        with open('.//test_data.csv', 'a', encoding="UTF-8") as data_file:
            data_file.write(csv_string)

timer = Time_Poker()
start = timer.take_time()
input('Taste drücken zum beenden')

timer.write_to_csv(start, timer.take_time())
