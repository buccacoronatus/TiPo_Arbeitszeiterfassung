import time
import csv

class TimePoker():
    def __init__(self):
        time_object = time.localtime()
        
        self.jahr = time_object[0]
        self.monat = time_object[1]
        self.tag = time_object[2]
        self.wochentag = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time_object[6]]
        
        self.start = time.time()
        self.startzeit = f'{time_object[3]}:{self.zero_minutes(time_object[4])}'

        self.endzeit = ''

    @staticmethod
    def zero_minutes(minuten):
         return f"{minuten:02d}"
    
    def run(self):
        input('Taste drücken zum beenden und speichern')
        endtime_objekt = time.localtime()
        self.endzeit =  f'{endtime_objekt[3]}:{self.zero_minutes(endtime_objekt[4])}'
        self.write_to_csv()
    
    def pause():
        pass
    
    def calculate_stunden(self):
        return round(round((time.time() - self.start) / 3600, 1) * 2) / 2
    
    def write_to_csv(self):
        csv_string = f'{self.wochentag}, {self.jahr}, {self.monat}, {self.tag}, {self.calculate_stunden()}\n'
        print(csv_string, sep="")
        
        with open('test_data.csv', 'a', newline='') as csvfile:
            csv.writer(
                csvfile, delimiter=' ').writerow(
                [self.wochentag]+[self.jahr]+[self.monat]
                +[self.tag]+[self.startzeit]+[self.endzeit]
                +[self.calculate_stunden()]
                )

timer = TimePoker()
timer.run()

