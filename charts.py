def define_zodiac_sign():
 month = input('What month were you born?
')
 day = input('What day were you born?
')
 if month.lower() == 'august' and int(day) in range(1,22):
    print('Leo')
 elif month.lower() == 'august' and int(day) in range (22,31):
    print('Virgo')
 if month.lower() == 'september' and int(day) in range(1,22):
    print('Virgo')
 elif month.lower() == 'september' and int(day) in range (22,31):
    print('Libra')
 if month.lower() == 'october' and int(day) in range(1,23):
    print('Libra')
 elif month.lower() == 'october' and int(day) in range (24,31):
    print('Scorpio')
 if month.lower() == 'november' and int(day) in range(1,21):
    print('Scorpio')
 elif month.lower() == 'november' and int(day) in range (23,31):
    print('Saggitarius')
 if month.lower() == 'december' and int(day) in range(1,21):
    print('Saggitarius')
 elif month.lower() == 'december' and int(day) in range (22,31):
    print('Capricorn')
 if month.lower() == 'january' and int(day) in range(1,19):
    print('Capricorn')
 elif month.lower() == 'january' and int(day) in range (20,31):
    print('Aquarius')
 if month.lower() == 'february' and int(day) in range(1,18):
    print('Aquarius')
 elif month.lower() == 'february' and int(day) in range (19,29):
    print('Pisces')
 if month.lower() == 'march' and int(day) in range(1,20):
    print('Pisces')
 elif month.lower() == 'march' and int(day) in range (21,31):
    print('Aries')
 if month.lower() == 'april' and int(day) in range(1,19):
    print('Aries')
 elif month.lower() == 'april' and int(day) in range (20,31):
    print('Taurus')
 if month.lower() == 'may' and int(day) in range(1,20):
    print('Taurus')
 elif month.lower() == 'may' and int(day) in range (21,31):
    print('Gemini')
 if month.lower() == 'june' and int(day) in range(1,21):
    print('Gemini')
 elif month.lower() == 'june' and int(day) in range (21,31):
    print('Cancer')
 if month.lower() == 'july' and int(day) in range(1,22):
    print('Cancer')
 elif month.lower() == 'july' and int(day) in range (23,31):
    print('Leo')
