a="0000"
f=open("1.txt","w")
for i in range(1801):
     f.write("  - img:1/"+a+str(i)+".gif 128"+"\n")
     f.write("  - '!nextpage!'"+"\n")
     if i<=9 and i>=0:
          a="0000"
     elif i<=99 and i>=10:
          a="000"
     elif i<=999 and i>=100:
          a="00"
     elif i<=9999 and i>=1000:
          a="0"
f.close()
print("ok")
