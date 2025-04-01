# OPening file
file = open("week4/exam.txt", "r") #remains constant
data= file.read() #open with intentions

print (data)

#writing a file
file = open("randomfile,pdf","w")
data= file.write("this is python")
print(data)

#try except
try:
    file = open("exam.txt","r")
    data =file.read()
    print("the data is: data")
except FileNotFoundError:
    print ("sorry this file does not exist")
finally:
      print("thanks for using me")