import sys
dialDic = {1:[],2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z'],0:[]}

dial = sys.stdin.readline().rstrip()

for c in dial:
    if c in dialDic.valuse():
        print("true")
    else:
        print("false")