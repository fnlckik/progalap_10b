ido = 480
for i in range(13):
    o = ido // 60
    p = ido % 60
    if o < 10:
        o = "0" + str(o)
    if p == 0:
        p = "00"
    print(o, ":", p, sep="")
    ido += 50