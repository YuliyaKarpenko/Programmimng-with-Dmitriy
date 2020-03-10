price1 = 250
price2 = 350
price3 = 450

def cinema_price():
  while True:
    movie = input ('Which movie you want to see?')
    if not movie in ['Parasite', '1917', 'Sonic']:
      print ('This one is not on. Please choose between Parasite, 1917 and Sonic.')
    else:

      day = input('Dp you want to go today or tomorrow?')
      if day == 'today' and movie == 'Parasite':
        time = input('Choose time: 12, 16, 20. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '12':
          print('The total cost is ', price1*amount)
        elif time == '16':
          print('The total cost is ', price2*amount)
        elif time == '20':
          print('The total cost is ', price3*amount)

      elif day == 'today' and movie == '1917':
        time = input('Choose time: 10, 13, 16. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '10':
          print('The total cost is ', price1*amount)
        elif time == '13':
          print('The total cost is ', price2*amount)
        elif time == '16':
          print('The total cost is ', price3*amount)

      elif day == 'today' and movie == 'Sonic':
        time = input('Choose time: 10, 14, 18. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '10':
          print('The total cost is ', price1*amount)
        elif time == '14':
          print('The total cost is ', price2*amount)
        elif time == '18':
          print('The total cost is ', price3*amount)  


      elif day == 'tomorrow' and movie == 'Parasite':
        time = input('Choose time: 12, 16, 20. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '12':
          print('The total cost is ', price1*amount)
        elif time == '16':
          print('The total cost is ', price2*amount)
        elif time == '20':
          print('The total cost is ', price3*amount)

      elif day == 'tomorrow' and movie == '1917':
        time = input('Choose time: 10, 13, 16. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '10':
          print('The total cost is ', price1*amount)
        elif time == '13':
          print('The total cost is ', price2*amount)
        elif time == '16':
          print('The total cost is ', price3*amount)

      elif day == 'tomorrow' and movie == 'Sonic':
        time = input('Choose time: 10, 14, 18. ')
        amount = int(input('How many tickets to do you want?'))
        if time == '10':
          print('The total cost is ', price1*amount)
        elif time == '14':
          print('The total cost is ', price2*amount)
        elif time == '18':
          print('The total cost is ', price3*amount) 
    break;
