a = ""
stats1,stats2,stats3,stats4, stats5, stats6 = {}, {}, {}, {}, {}, {}

def takeInput():
  global a
  while True:
      try:
          name = input() + '\n'
      except EOFError:
          break
      a += name

def fnCal():
  global a, stats1,stats2,stats3,stats4, stats5, stats6
  s = ''
  for i in a:
    s += i
    if i == '\n':
      if len(s)>1:
        a,b,c = s.split(':')
        l = c.split(',')
        #print(a, b, c)
        #print(len(l))
        if len(l) > 3:
            stats5[a] = stats5.setdefault(a, 0) + 1
        else:
            stats6[a] = stats6.setdefault(a, 0) + 1
            
        setwon, setlost = 0, 0
        for j in l:
            st1, st2 = '', ''
            st1, st2 = str(j).split('-')
            
            #print(st1, st2)
            if int(st1) > int(st2):
                setwon += 1
            else:
                setlost += 1
                
            
            stats1[a] = stats1.setdefault(a, 0) + int(st1)
            stats1[b] = stats1.setdefault(b, 0) + int(st2)
            
            stats2[a] = stats2.setdefault(a, 0) + int(st2)
            stats2[b] = stats2.setdefault(b, 0) + int(st1)
        
        stats3[a] = stats3.setdefault(a, 0) + int(setwon)
        stats3[b] = stats3.setdefault(b, 0) + int(setlost)
        
        stats4[a] = stats4.setdefault(a, 0) + int(setlost)
        stats4[b] = stats4.setdefault(b, 0) + int(setwon)
                
        
      s = ''
      
takeInput()
fnCal()

player= []
res = []
for k in stats1:
    player.append(k)
for k in player:
    temp = []
    temp.extend([str(k), str(stats5.get(k, 0)),str(stats6.get(k, 0)),str(stats3.get(k, 0)),str(stats1.get(k, 0)),str(stats4.get(k, 0)),str(stats2.get(k, 0))])
    res.append(temp)
res = sorted(res, key = lambda x: int(x[1]))

for r in res:
    stp = ' '.join(str(e) for e in r)
    print(stp)
    
