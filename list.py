""" List
1.collection of elemets 
it can used to modify, change,accese the data """

num=[1,2,5,7,9,7,6,5,8,6,5,]
print(num)
numbr=["hyd",8,0,7,5,"delhi",9,"a",7,9,]
print(numbr)
b=["a,","s",7,5,4,4,]
print(b)
k=[5,7,9,75,9,7,6,]
print(k)
zeee=["rahul",9,8,"j",9,7,5,]
print(zeee)

""" index values
1.index value start with [0]
""" 
num1=["hyd",6,7,9,0,4,2,7,8,"kathik","rahul","mallesh",9,7,6,5,8,9,7,5,5,4,]
print(num1[1])
num2=["hyd",6,7,9,0,4,2,7,8,"kathik","rahul","mallesh",9,7,6,5,8,9,7,5,5,4,]
print(num2[9])
num3=["hyd",6,7,9,0,4,2,7,8,"kathik","rahul","mallesh",9,7,6,5,8,9,7,5,5,4,]
print(num3[16])
num4=["hyd",6,7,9,0,4,2,7,8,"kathik","rahul","mallesh",9,7,6,5,8,9,7,5,5,4,]
print(num4[15])
hyd=[1,9,7,6,7,6,6,6,5,5,"hyd","kk","kjgf","rahul",]
print(hyd[8])
mumbai=[1,9,7,6,7,6,6,6,5,5,"hyd","kk","kjgf","rahul",]
print(mumbai[10])
""" slice """
cal=["hyd",6,7,9,0,4,2,7,8,"kathik","rahul","mallesh",9,7,6,5,8,9,7,5,5,4,]
print(cal[1:6])
chandu=["rahul","kalki",8,9,6,5,4,3,7,6,5,3,23,65,87,786,5976,87,654,654,]
print(chandu[5:9])
print(chandu[-5:8])
print(chandu[1:-3])
print(chandu[4:-6])
print(chandu[-8:-6])
""" methods
 """
karthik=["karthik ","jhhv","rahul","maruthi",998,87,65,546,87,89,8,8,8,8,8,8,8,8]
karthik.pop()
print(karthik)
karthik.append("karhik")
print(karthik)
b=[5,9,7,6,5,5,6,8,]
karthik.extend(b)
print(karthik)
bolls=[6,7,98,76,97,65,54,8,9,]
karthik.extend(bolls)
print(karthik)
print(len(karthik))
print(karthik.count(998))