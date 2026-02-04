import time
import csv

class TimePoker():
    def __init__(self):
        time_object = time.localtime()
        
        self.data_file = 'test_data.csv'
        
        self.jahr = time_object[0]
        self.monat = time_object[1]
        self.tag = time_object[2]
        self.wochentag = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time_object[6]]
        
        self.start = time.time()
        self.startzeit = f'{time_object[3]}:{self.zero_minutes(time_object[4])}'

        self.pausenzeit = 0
        self.endzeit = ''

    @staticmethod
    def zero_minutes(minuten):
         return f"{minuten:02d}"
    
    def run(self):
        choose = '0'
        choose = input('''Timer läuft\n(1) - Pause machen\n(2) - Arbeitstag beenden''')
        
        if choose == '1': self.pause()
        elif choose == '2': self.stop_timer()
        else: self.run()
         
    def pause(self):
        pausenzeit_start = time.time()
        input('''PAUSENTimer läuft\nBeliebige Taste drücken zum beenden und speichern''')
        pausenzeit_end = time.time()
        
        self.pausenzeit = self.pausenzeit + (pausenzeit_end - pausenzeit_start)
        
        self.run()
        
    def stop_timer(self):
        endtime_objekt = time.localtime()
        self.endzeit =  f'{endtime_objekt[3]}:{self.zero_minutes(endtime_objekt[4])}'
        
        self.write_to_csv()
    
    def calculate_stunden(self):
        return round(round((time.time() - self.start) / 3600, 1) * 2) / 2
    
    def write_to_csv(self):
        with open(self.data_file, 'a', newline='') as csvfile:
            csv.writer(
                csvfile, delimiter=' ').writerow(
                [self.wochentag]+[self.jahr]+[self.monat]
                +[self.tag]+[self.startzeit]+[self.endzeit]
                +[self.calculate_stunden()]+[self.pausenzeit]
                )
        print(f'Tagszeit wurde gebucht unter {self.data_file}')
        
timer = TimePoker()
timer.run()

