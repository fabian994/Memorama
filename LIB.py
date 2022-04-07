import glob
import random

def initGame():

	Cartas = glob.glob('./DATA/*.png');
	Cartas.remove('./DATA/TEC_Logo.png');
	random.shuffle(Cartas);
	CartasUnicas = Cartas.copy();
	random.shuffle(Cartas);

	Cartas.extend(CartasUnicas);

	Solucion = [];

	for carta in CartasUnicas:
		a = Cartas.index(carta)
		Cartas.reverse()
		b = len(Cartas) - Cartas.index(carta) -1;
		Cartas.reverse()
		Solucion.append([a,b])
		Solucion.append([b,a])

	print(Cartas)
	print(Solucion)

	return Cartas, Solucion
