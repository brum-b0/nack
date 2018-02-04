import sys
import os
import hashlib
from threading import Thread

def nums(h, hp):
    
    for i in range(0,1000000):
        
        if (len(str(i)) <= 4):
            h = hashlib.new('md5')
            guess = str(i).zfill(4)
            #print guess
            h.update(guess)
            guessHash = h.hexdigest().upper()
            #print guessHash
            #print hp
            if (guessHash == hp):
                print "passwd found: " + guess + "\n\n"
                return
        
        if (len(str(i)) <= 5):
            h = hashlib.new('md5')
            guess = str(i).zfill(5)
            #print guess
            h.update(guess)
            guessHash = h.hexdigest().upper()
            #print guessHash
            #print hp
            if (guessHash == hp):
                print "passwd found: " + guess + "\n\n"
                return
        
        if (len(str(i)) <= 6):
            h = hashlib.new('md5')
            guess = str(i).zfill(6)
            #print guess
            h.update(guess)
            guessHash = h.hexdigest().upper()
            #print guessHash
            #print hp
            if (guessHash == hp):
                print "passwd found: " + guess + "\n\n"
                return

    print "passwd not type 1 (nums)\n\n"
    
def dictWords(h, hp):
    dictFile = open('/usr/share/dict/words', 'r')
    for line in dictFile.readlines():
                  
        if(len(line) == 5):          
            for i in range(0, 10):
                h = hashlib.new('md5')
                guess = line.strip('\n') + str(i)
                #print guess.title()
                h.update(guess.title())
                guessHash = h.hexdigest().upper()
               # print guessHash
                #print hp
                if (guessHash == hp):
                    print "passwd found: type2: " + guess.title() + "\n\n"
                    return
                
        elif(len(line) == 6):
           # print line
            guess = line.strip('\n')
            i = 0
            for x in range(0, guess.count('e')):
                holder = guess
                i = guess.find('e', i + 1)
                if (i != -1):
                    guess[i:i+1].replace(guess[i], '3')
                    temp = list(guess)
                    temp[i] = '3'
                    guess = "".join(temp)
                    h = hashlib.new('md5')
                    h.update(guess)
                    guessHash = h.hexdigest().upper()
                    if (guessHash == hp):
                        print "passwd found: type3: " + guess + "\n\n"
                        return
        else:
            h = hashlib.new('md5')
            guess = line.strip('\n')
            #print guess
            h.update(guess)
            guessHash = h.hexdigest().upper()
            if (guessHash == hp):
                print "passwd found: type 4: " + guess + "\n\n"

    print "passwd not type 2, 3, 4\n\n"


           
def charBrute(h, hp):
    x = 1
    
def main():
    hasher = hashlib.md5() 
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print filename + ' does not exist'
            exit(0)
            x
        if not os.access(filename, os.R_OK):
            print filename + ': cannot read'
            exit(0)
            
        hashFile = open(filename, 'r')
        
        for line in hashFile.readlines():
            if ":" in line:
                uname = line.split(':')[0]
                hashedPasswd = line.split(':')[1].strip('\n ')
                print "cracking: " + uname 
                #print uname
                #print hashedPasswd
                
                #thread try rule 1
                nums(hasher, hashedPasswd)
                #thread try rule 2
                dictWords(hasher, hashedPasswd)
                #thread try rule 3
                charBrute(hasher, hashedPasswd)
            
        
        
    else:
        print 'please provide a hash file e.g. \n\npython nack.py hashes.txt\n'
 #make sure hashes.txt is formatted like uname:passwdHash:[othercrap]
 # or                                    uname:passwdHash

                
main()

   
  



    


