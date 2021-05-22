def most_frequent(a):
    d = {}
    for b in a:
      if b not in d:
        d[b] =1
      else:
        d[b] += 1
    e = dict(sorted(d.items(),key = lambda x:x[1],reverse = True))
    for key,value in e.items():
        print("{} = {}".format(key,value))
    
a = input("please enter a string: ")
most_frequent(a)
