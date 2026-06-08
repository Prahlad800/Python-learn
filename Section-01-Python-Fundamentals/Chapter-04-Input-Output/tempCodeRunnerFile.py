salary=int(input("enter you CTC salary in lakha Ex 12\n "))
ctc=salary * 100000
if(ctc>500000):
    tex=0
elif(500000<ctc>1000000):
    tex= ctc * (5/100)