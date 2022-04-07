from tkinter import *
import numpy
import glob
import random

root = Tk();

photo = PhotoImage(file = r"./DATA/TEC_Logo.png");
photo = photo.subsample(3, 3);
btn = [];
n = 0;

def Change():
	print("Tkinter is easy to use!")

def reset():
	photo = PhotoImage(file = r"./DATA/TEC_Logo.png")
	photo = photo.subsample(3, 3)
	for b in btn:
		b.configure(image=photo)
		b.photo = photo

def change_pic(btn, File, Events, Solucion, ParesDescubiertos):
	#File = Cartas[0];
	photo = PhotoImage(file = File);
	photo = photo.subsample(1, 1) # escalar imagen
	btn.configure(image=photo) # despliego la imagen al botton
	btn.photo = photo # al boton le pongo la imagen
	print(btn.cget("text"))
	Events.append(int(btn.cget("text")))
	
	if len(Events) > 2:
		Events.pop(0);
	
	if Events in Solucion:
		ParesDescubiertos.append(Events[0]);
		ParesDescubiertos.append(Events[1]);
	
	print(ParesDescubiertos)
	
	if not Events[-1] in ParesDescubiertos:
		# espero 2000ms para hacer el reset
		root.after(2000, reset); 
		

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

idx = 0;

Events = [];
ParesDescubiertos = [];

for i in range(0,4):
	for j in range(0,4):
		
		btn.append(Button(root, height = 160, width = 160 ,text=str(n), image = photo, command=lambda c=n: change_pic( btn[c], Cartas[c], Events, Solucion, ParesDescubiertos )));
		
		btn[n].grid(row = i, column = j);
		
		
		idx += 1;
		n += 1;


reset();

root.mainloop()



