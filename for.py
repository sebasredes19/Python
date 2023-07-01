def superDigit(n,k):
  sumNum=0
  n= n*k
  for i in n:
   sumNum += int(i)
  if(len(n)!=1):
      sumNum = superDigit(str(sumNum),1)
  
  return (sumNum)
