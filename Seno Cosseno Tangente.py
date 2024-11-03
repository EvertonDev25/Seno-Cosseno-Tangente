import math

Angulo = float(input('Digite o angulo que voce deseja: '))

print('_'*15)

sen = math.sin(math.radians(Angulo))
cos = math.cos(math.radians(Angulo))
tan = math.tan(math.radians(Angulo))

print('Seno é: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sen,cos,tan))

print('_'*15)