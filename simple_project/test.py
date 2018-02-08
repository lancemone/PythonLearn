id2 = input('please input your IDcard number:')
print('birthday is {}-{}-{}'.format(id2[6:10], id2[10:12], id2[12:14]))
print('birthday is {1}-{0}-{2}'.format(id2[6:10], id2[10:12], id2[12:14]))
print('birthday is {year}-{month}-{day}'.format(year=id2[6:10], month=id2[10:12], day=id2[12:14]))
