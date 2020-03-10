rate_Ek = 343.15
rate_Om = 381.18
rate_Vor = 473.13
rate_Yar = 485.11

def cost_of_call():
 
  city = input('Куда вы звонили? ')
  if not city in ['Екатеринбург', 'Омск', 'Воронеж', 'Ярославль']:
    print ('Нет данных для этого города')
  else:

    minutes = int(input('Сколько минут продолжался разговор? '))
    if city == 'Екатеринбург':
      print ('Стоиомсть звонка ', minutes*rate_Ek)
    elif city == 'Омск':
      print ('Стоиомсть звонка ', minutes*rate_Om)
    elif city == 'Воронеж':
      print ('Стоиомсть звонка ', minutes*rate_Vor)
    elif city == 'Ярославль':
      print ('Стоиомсть звонка ', minutes*rate_Yar)
