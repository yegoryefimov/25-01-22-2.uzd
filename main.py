text = input ("Ievadi tekstu:")
def countWords(text):
  summa = 0
  sar1 = text.split() 
  for word in sar1:
    if len(word)>1:
     summa += 1
    print (text) 
  return summa 