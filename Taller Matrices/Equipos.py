def solution(a):
    equipo1 = 0
    equipo2 = 0
    for i in range(len(a)):
        if i % 2 == 0:
            equipo1 += a[i]
        else:
            equipo2 += a[i]
    return [equipo1, equipo2]