def CalculoSalario(horas, tarifa): 
MAX_HRS_SEMANALES = 40
horas_extras = 0 
horas_extras = horas - MAX_HRS_SEMANALES
if (horas_extras > 0): 
  pago = (MAX_HRS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
else: 
  pago = (horas * tarifa) 
return pago 

y: 
horas = int(intput("ingrese cantidad de horas: "))
tarifa = float(input("ingrese tarifa: "))
salario = CalculoSalario(horas, tarifa)
print(salario)
except:
    print("Error, debe ingresar valores numéricos")