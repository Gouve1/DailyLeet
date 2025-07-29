

s = ['o','l','a']
s1 = "Olá, meu nome é Pedro "
s2=s1.replace(',','')
s3=s2.split()
print(s3)
sep = ""
s4=sep.join(s3)
table = str.maketrans('','',', ')
newS = s1.translate(table)
invertedS = newS[::-1]
print(newS)
print(invertedS)
