import random as rm

def turno_pc():
    a=rm.randrange(1,4)
    if a==1 :
        return "Tj"
    elif a==2:
        return "Pd"

    elif a==3:
        return "Pp"
n=int(input("A las cuantas victorias se puede ganar: "))
vth=vtp=0
while vth!=n and vtp!=n :
    t=turno_pc()
    th=input("Ingresa Tj para tijera, Pd para piedra, Pp para papel: ")
    if th==t:
        print("EMPATE")
    elif th=="Pd" and t=="Tj":
        vth+=1
        print("GANASTE")
    elif th=="Tj" and t=="Pp":
        vth+=1
        print("GANASTE")
    elif th=="Pp" and t=="Pd":
        vth+=1
        print("GANASTE")
    else:
        vtp+=1
        print("PERDISTE")
    print(f"TU: {vth} - PC : {vtp}")
name2="Pc"
name1="Stive"
if vth==n:
    r=f"Gano {name1} con {vth} victorias y perdio {name2} con {vtp} victorias"
    print(r)
elif vtp==n:
    r=f"Gano {name2} con {vtp} victorias y perdio {name1} con {vth} victorias"
    print(r)


