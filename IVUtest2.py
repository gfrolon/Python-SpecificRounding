Precio=raw_input('\n Entre el Precio Total: ')
Total=float(Precio)
ivu10=Total*.105
ivue=round(ivu10,2)
ivu1=Total*.01
ivum=round(ivu1,2)
Total2=Total+ivue+ivum
Total3=str('El subtotal es: ')
Total4=str('     Ivu Estatal: ')
Total5=str('     Ivu Municipal: ')
Total6=str('TOTAL: ')
print '\n',Total3,Total,'\n'
print Total4,ivue, '\n'
print Total5,ivum, '\n'
print Total6,'$',Total2, '\n'
#print Total
#print ivu10
#print ivu1
#print Total2
raw_input('Presione Enter para salir;')