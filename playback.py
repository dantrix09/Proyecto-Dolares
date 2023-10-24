def DolaresEnFloat(dolares):
    valor= dolares.split("$")
    return(float(valor[1]))


def PorcentajeAFloat(porcentajerecibido):
    porcentajereal = porcentajerecibido.split("%")
    a = float(porcentajereal[0])
    return(0.01*a)


def main():
    dollars = DolaresEnFloat(input("How much was the meal? "))
    percent = PorcentajeAFloat(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
