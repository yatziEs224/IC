delito = input("Tipo de delito: 1.Grave 2.Menos grave 3.Leves 4.Mera actividad\n")
estado = input("Estado físico en el que se encuentra la persona: 1.Problemas mentales 2.Ebriedad 3.Drogado 4.Normal\n")
antecedentes = input("¿Tiene anteceddentes? 1.Sí 2.No\n")

if (delito == '1' and estado == '1' and antecedentes == '1'):
	print("El veredicto es Internamiento")
	
if (delito == '1' and estado == '2' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '1' and estado == '3' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '1' and estado == '4' and antecedentes == '1'):
	print("El veredicto es Multa")

if (delito == '1' and estado == '1' and antecedentes == '2'):
	print("El veredicto es Tratamiento en libertad")

if (delito == '1' and estado == '2' and antecedentes == '2'):
	print("El veredicto es Prisión preventiva")

if (delito == '1' and estado == '3' and antecedentes == '2'):
	print("El veredicto es Prisión preventiva")

if (delito == '1' and estado == '4' and antecedentes == '2'):
	print("El veredicto es Multa")



if (delito == '2' and estado == '1' and antecedentes == '1'):
	print("El veredicto es Internamiento")
	
if (delito == '2' and estado == '2' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '2' and estado == '3' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '2' and estado == '4' and antecedentes == '1'):
	print("El veredicto es Multa")

if (delito == '2' and estado == '1' and antecedentes == '2'):
	print("El veredicto es Tratamiento en libertad")

if (delito == '2' and estado == '2' and antecedentes == '2'):
	print("El veredicto es Multa")

if (delito == '2' and estado == '3' and antecedentes == '2'):
	print("El veredicto es Multa")

if (delito == '2' and estado == '4' and antecedentes == '2'):
	print("El veredicto es Multa")



if (delito == '3' and estado == '1' and antecedentes == '1'):
	print("El veredicto es Internamiento")
	
if (delito == '3' and estado == '2' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '3' and estado == '3' and antecedentes == '1'):
	print("El veredicto es Prisión preventiva")

if (delito == '3' and estado == '4' and antecedentes == '1'):
	print("El veredicto es Multa")

if (delito == '3' and estado == '1' and antecedentes == '2'):
	print("El veredicto es Se deroga")

if (delito == '3' and estado == '2' and antecedentes == '2'):
	print("El veredicto es Multa")

if (delito == '3' and estado == '3' and antecedentes == '2'):
	print("El veredicto es Multa")

if (delito == '3' and estado == '4' and antecedentes == '2'):
	print("El veredicto es Tratamiento en libertad")




if (delito == '4' and estado == '1' and antecedentes == '1'):
	print("El veredicto es Tratamiento en libertad")
	
if (delito == '4' and estado == '2' and antecedentes == '1'):
	print("El veredicto es Multa")

if (delito == '4' and estado == '3' and antecedentes == '1'):
	print("El veredicto es Multa")

if (delito == '4' and estado == '4' and antecedentes == '1'):
	print("El veredicto es Tratamiento en libertad")

if (delito == '4' and estado == '1' and antecedentes == '2'):
	print("El veredicto es Se deroga")

if (delito == '4' and estado == '2' and antecedentes == '2'):
	print("El veredicto es Tratamiento en libertad")

if (delito == '4' and estado == '3' and antecedentes == '2'):
	print("El veredicto es Tratamiento en libertad")

if (delito == '4' and estado == '4' and antecedentes == '2'):
	print("El veredicto es Se deroga")