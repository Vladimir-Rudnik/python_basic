time = input("Введите время в секундах: ")
ss = int(time)
hh = ss // 3600
if ss < 3600:
    mm = ss // 60
    ss2 = ss - mm * 60
else:
    mm = ss // 60 - 60
    ss2 = ss - (mm + 60) * 60

if hh < 10:
    hh1 = "0"
    hh = str(hh)
    hh = hh1 + hh
else:
    hh = str(hh)
if mm < 10:
    mm1 = "0"
    mm = str(mm)
    mm = mm1 + mm
else:
    mm = str(mm)
if ss2 < 10:
    ss1 = "0"
    ss2 = str(ss2)
    ss2 = ss1 + ss2
else:
    ss2 = str(ss2)

time2 = (hh, mm, ss2)
print(f"Получаем: {':'.join(time2)}")
