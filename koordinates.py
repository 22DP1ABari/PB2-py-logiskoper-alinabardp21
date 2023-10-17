x= float(input())
y = float(input())

if x>-8 and x<2 and y>-3 and y<5:
    print('Punkts atrodas figūrā.')
elif (x==-8 or x==2) and y>=-3 and y<=5:
    print('Punkts atrodas robežlīnijā.')
elif (y==5 or y==-3) and x>=-8 and x<=2:
    print('Punkts atrodas robežlīnijā.')
else:
    print('Punkts atrodas aiz figūras.')

