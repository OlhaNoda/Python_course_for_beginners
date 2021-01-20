contains = ['05', '@']
arg = 'johnd@05050505oegmail.com'

k = 0
if sum([k+1 for c in contains if c in arg]) == len(contains):
    print('ok')
else:
    print('no')


