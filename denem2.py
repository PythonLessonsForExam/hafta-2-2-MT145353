girdi=str(input("haftanın hangi günü bugün?"))
if girdi==("pazartesi" or "salı" or "çarşamba" or "perşembe" or "cuma"):
    print("bugün haftaiçidir.")
elif girdi==("cumartesi" or "pazar"):
    print("bugün haftasonudur.")
else:
    print("geçerli bir gün ismi girmedinişz lütfen tekrar deneyin.")