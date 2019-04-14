class Test():
    def __len__(self):
        return 0
    def __bool__(self):
        return False
test = Test()

if test:
    print('s')
else:
    print('n')
    
    
