import time

# Pauseknopf um Pause zu ermitteln 
# exportknopf um csv zu übertragen 

heute= {
    'Jahr': time.localtime()[0],
    'Monat': time.localtime()[1],
    'Tag': time.localtime()[2],
    'Wochentag': ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][time.localtime()[6]]
}

start = time.time()

input('Taste drücken zum beenden')
# testweise Zahl eingefügt!
end = time.time()

# aufgerundet auf halbe Stunde 
stunden = round(round((end - start) / 3600, 1) * 2) / 2


# csv print, sep="" wichtig um whitespace zu vermeiden
csv_string = f'{heute['Wochentag']}, {heute['Jahr']}, {heute['Monat']}, {heute['Tag']}, {stunden}\n'
print(csv_string, sep="")

# a for append
with open('.//data.csv', 'a', encoding="UTF-8") as data_file:
    data_file.write(csv_string)
