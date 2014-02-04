import Pmf

def mode(aHist):
  valmode, freqmode = 0, 0
  
  for val, freq in aHist.Items():
    if freq > freqmode:
      valmode, freqmode = val, freq

  return valmode

def allModes(aHist):
  return sorted(aHist.Items(), key=lambda x: x[1], reverse=True)

def main():
  lol = [1,2,2,3,3,3,4,4,4,4]

  print mode(Pmf.MakeHistFromList(lol))

  print allModes(Pmf.MakeHistFromList(lol))

if __name__ == '__main__':
  main()