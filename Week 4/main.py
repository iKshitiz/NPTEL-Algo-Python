def histogram(l):
  d = {x:l.count(x) for x in l}
  res = sorted(list(d.items()))
  res = sorted(res, key=lambda x: x[1])
  return res

def transcript(course, roll, grade):
  res,final,ok,temp = [],[],[],[]
  grade = sorted(grade)
  roll = sorted(roll)
  for r in roll:
    temp.append(r[0])
    temp.append(r[1])
    for g in grade:
      if r[0] == g[0]:
        res.append(g[1])
        for c in course:
          if c[0] == g[1]:
            res.append(c[1])
        res.append(g[2])
        ok.append(tuple(res))
        res = []
    temp.append(ok)
    ok = []
    final.append(tuple(temp))
    temp = []
    
  return(final)
