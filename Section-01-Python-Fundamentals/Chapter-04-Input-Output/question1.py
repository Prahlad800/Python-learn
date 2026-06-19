# Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

salary=int(input("enter you CTC salary in lakha Ex 12\n "))
salary_in_hand=salary * 100000
if salary_in_hand < 500000:
    tex=0
elif 500000 < salary_in_hand < 1000000:
    tex= salary_in_hand * (5/100)
elif 1000000 < salary_in_hand < 2000000:
    tex=salary_in_hand * (10/100)
elif salary_in_hand < 200000:
    tex=salary_in_hand * (10/100)
else:
    tex=salary_in_hand * (30/100)

print("salary_in_hand = ",salary_in_hand,"tex =",tex,"\n")

ctc=salary_in_hand - tex

her=ctc * (10/100)
print("ctc = ",ctc,"der =",her,"\n")
da= ctc * (5/100)
print("ctc = ",ctc,"da =",da,"\n")
pf=ctc * (3/100)
print("ctc = ",ctc,"pf =",pf,"\n")

in_hand=salary_in_hand - tex - her - da - pf
print("ctc = ",ctc,"der =",her, "in hand",in_hand,"salaey in hand",salary_in_hand,"\n")







