def conversor_de_segundos(h, m, s):
    segundos_h = h * 3600
    segundos_m = m * 60
    soma = segundos_m + segundos_h + s
    return soma


print(conversor_de_segundos(2, 40, 4))
