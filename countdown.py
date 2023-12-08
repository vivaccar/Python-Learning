from datetime import datetime
def countdown(year, month, day):
	dif = datetime(year, month, day) - datetime.now()
	days = dif.days
	hours = dif.seconds / 3600
	print("Faltam: {} dias e {} horas.".format(days, hours))

countdown(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))