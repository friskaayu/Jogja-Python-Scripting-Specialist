#________________nomer1_____________________________
#read file abstrak.txt
openfile = open ('/Python learning/abstrak.txt','r')

#read from byte 80
reading = openfile.seek(80)
reading = openfile.read()

#show and close
print(reading)
openfile.close()

#________________nomer2___________________________
#import os
import os

#create direktory FriskaAyu
try:
    os.mkdir('/Python learning/FriskaAyu')
# check if directory already exists
except FileExistsError:
    pass

#create file potongan_abstrak.txt in direktory FriskaAyu
fileHandle_write = open ('/Python learning/FriskaAyu/potongan_abstrak.txt','w')

#write from byte 80 in file potongan_abstrak.txt and close
fileHandle_write.write(reading)
fileHandle_write.close()

#________________nomer3_____________________________
#import BytesIO and pickle
from io import BytesIO
import pickle

#read file potongan_abstrak.txt
readingfile = open('/Python learning/FriskaAyu/potongan_abstrak.txt','r')
readfile = readingfile.read()

#write file potongan_abstrak.ser
writingfile = open('/Python learning/FriskaAyu/potongan_abstrak.ser','wb')

#converting an object in memory to a byte stream (from potongan_abstrak.txt to potongan_abstrak.ser)
pickle.dump(readfile,writingfile)

readingfile.close()
writingfile.close()

#show the original pickled file
print('\n Showing the original pickled file \n', writingfile)

#show the result of converting the pickled file
picklefile = open('/Python learning/FriskaAyu/potongan_abstrak.ser','rb')
data = pickle.load(picklefile)
picklefile.close()
print('\n Showing the result of converting the pickled file \n', data)