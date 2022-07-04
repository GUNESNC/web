saat=int(input(" Kaldığınız süreyi Girin:"))

ücret=0

if saat<=1:
  ücret=5
elif saat<=5:
  ücret=4*saat
else:
  ücret=3*saat 

print (" Ödemeniz Gereken Ücret:{}". format (ücret))


