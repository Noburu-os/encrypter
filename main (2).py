import hashlib
import time
import multiprocessing
from termcolor import colored
# time function to compute the amount of time it takes for the code to run
version = "21.2.4"
# set wait time
def wait(amount):
  time.sleep(amount)
  print()
######################
true = True
time = time
print(time.time())
# if the password is not found
not_found = 0
# input username
word = input("File name:")
# input file name
E_word = input("to confirm file name click enter")
print('')
question = input(colored('type "1" if you want to encrypt using hashlib, if not type "2" :', "blue"))
print('')
question4 = ('2')



print ("")
print ("")
answer = ('1')
if question == answer:

############START ENCRYPTION#################
  enc_wrd = word.encode('utf-16')
  digested = hashlib.md5(enc_wrd.strip()).hexdigest()
  print(colored('encryption in progress{}...', 'green'))
  print('')
  wait(6)
  print(colored('encrytpted file = ' + (digested), 'magenta'))
  

  if enc_wrd == enc_wrd:
      if word == word:
          if E_word == E_word:
              print('')
              
  else:
      (colored("encryption failed", 'red'))

  if word == E_word:
      if word == word:
          if E_word == word:
              print(colored("encryption in progress{}...", 'green'))
              print(colored("ERR cannot have same name", 'red'))
              print(colored("sike ;) press enter", 'blue'))

  #for i in enc_wrd:
  # list(len[i:i])
  #if word in list == enc_wrd:
  # print("password found" + word)
  #print (list(len))

  ###### emergency cracker #######
  # in progress

  if word is not word:
      if E_word == not_found:
          if word == not_found:
              if E_word is not E_word:
                  print(colored("password not found", 'red'))
                  word.format(word).digest()


  #if word_err != word_err:
  #word_err.format(list(len[i:i]))
  #print (word_err.list(len[i:i]))
  # no of cpu
  no_of_cpu = multiprocessing.cpu_count()
  print('')
  wait(3)
  print(colored('number of CPUs =', 'yellow'))
  print(colored(no_of_cpu, 'yellow'))

  start = time.perf_counter()


  ### open hashed password file ####
  hashed_password_file_name = open('hsw.js', 'wb')
  #hashed_password_file_name = open(str(hashed_password_file_name))

  if hashed_password_file_name == hashed_password_file_name:
      print(hashed_password_file_name)
      #wait(2)
      #print(colored('file name hexdigested = ' + , "magenta"))
      
      print('')
      print('')
wait(2)
#######
question2 = input(colored('if you want to encrypt using SHA256 type "1", if you want to encrypt your file using a alphabet shifter type "2"', 'blue'))
print('')
print('')

answer2 = ("1")
answer3 = ('2')
 
#####
if question2 == answer2:
  print("")
  print("")
  # implementation of SHA 256 hash generator in python.
  # taking the input message to be used for hashing
  msg = input("Enter File Name:")
  msg_length = len(msg)
  #print msg, msg_length


  # converting the message into binary format
  binary_name = ''.join('{0:08b}'.format(ord(x), 'b') for x in msg)
  binary_name_length = len(binary_name)
  #print "Name in binary:", binary_name, binary_name_length


  # creating a 512 bit message block by padding
  zeros = 448 % 512 - (binary_name_length + 1)
  #print zeros
  k = '0' * zeros
  #print len(k)
  binary_length = '{0:064b}'.format(binary_name_length)
  #print binary_length, len(binary_length)
  msg_512 = binary_name + '1' + k + binary_length
  #print msg_512, len(msg_512)


  # breaking the 512 bit message block into 16 32 bit blocks [therefore, 1 block = 32 bit words]
  # M(0),M(1),.....,M(15)
  M = [msg_512[i:i + 32] for i in range(0,511,32)]
  #print M	


  # declaring the inital hash values to be used
  H = ['6a09e667','bb67ae85','3c6ef372','a54ff53a','510e527f','9b05688c','1f83d9ab','5be0cd19']  # [a, b, c, d, e, f, g, h]
  F = []
  F.append(H)
  #print F

  K = ['428a2f98','71374491','b5c0fbcf','e9b5dba5','3956c25b','59f111f1','923f82a4','ab1c5ed5','d807aa98','12835b01','243185be','550c7dc3','72be5d74','80deb1fe','9bdc06a7', 'c19bf174','e49b69c1','efbe4786','0fc19dc6','240ca1cc','2de92c6f','4a7484aa','5cb0a9dc','76f988da','983e5152','a831c66d','b00327c8','bf597fc7','c6e00bf3','d5a79147', '06ca6351','14292967','27b70a85','2e1b2138','4d2c6dfc','53380d13','650a7354','766a0abb','81c2c92e','92722c85','a2bfe8a1','a81a664b','c24b8b70','c76c51a3', 'd192e819', 'd6990624','f40e3585','106aa070','19a4c116','1e376c08','2748774c','34b0bcb5','391c0cb3','4ed8aa4a','5b9cca4f','682e6ff3','748f82ee','78a5636f','84c87814','8cc70208',
  '90befffa','a4506ceb','bef9a3f7','c67178f2']
  #print len(K)


  mask = 2 ** 32 - 1
  # defining 6 logical functions which are used for hash generation
  def ch(x, y, z):
    op1 = (x & y) ^ (~x & z)	
    return op1

  def ma(x, y, z):
    op2 = (x & y) ^ (x & z) ^ (y & z)
    return op2
    
  def sum0(x):
    rr1 = (x >> 2) | ((x << 30) & mask)
    rr2 = (x >> 13) | ((x << 19) & mask)
    rr3 = (x >> 22) | ((x << 10) & mask)
    rr = rr1 ^ rr2 ^ rr3
    return rr

  def sum1(x):
    rr1 = (x >> 6) | ((x << 26) & mask)
    rr2 = (x >> 11) | ((x << 21) & mask)
    rr3 = (x >> 25) | ((x << 7) & mask)
    rr = rr1 ^ rr2 ^ rr3
    return rr

  def sig0(x):
    rr1 = (x >> 7) | ((x << 25) & mask)
    rr2 = (x >> 18) | ((x << 14) & mask)
    rr3 = x >> 3
    rr = rr1 ^ rr2 ^ rr3
    return rr

  def sig1(x):
    rr1 = (x >> 17) | ((x << 15) & mask)
    rr2 = (x >> 19) | ((x << 13) & mask)
    rr3 = x>> 10
    rr = rr1 ^ rr2 ^ rr3
    return rr


  # looping from N: 1 to 16 

  modes = 2 ** 32
  W = [0 for i in range(64)]

  for i in range(1,17):

    # initializing the registers 
    a = int(F[i-1][0], base = 16)
    b = int(F[i-1][1], base = 16)
    c = int(F[i-1][2], base = 16)
    d = int(F[i-1][3], base = 16)
    e = int(F[i-1][4], base = 16)
    f = int(F[i-1][5], base = 16)
    g = int(F[i-1][6], base = 16)
    h = int(F[i-1][7], base = 16)

    # looping from M:0 to 63 [64 words generated per block of 32 bit words]
    for j in range(0,64):

      if j >= 16:  # the remaining range M:16 to 63 are generated using a formula
        W[j] = (((((sig1(W[j - 2]) + W[j - 7]) % modes) + sig0(W[j - 15])) % modes) + W[j - 16]) % modes        
      else:  # for the range M:0 to 15 the 32 bit words same as initial 16 block words i.e. M(0),M(1),...,M(15)
        W[j] = int(M[j], base = 2) 
      

      t1 = (((((((h + sum1(e)) % modes) + ch(e,f,g)) % modes) + int(K[j], base = 16)) % modes) + W[j]) % modes
      t2 = (sum0(a) + ma(a,b,c)) % modes
      h = g
      g = f
      f = e
      e = (d + t1) % modes
      d = c
      c = b
      b = a
      a = (t1 + t2) % modes

      #print '{0:08x}'.format(a, '0x'),'{0:08x}'.format(b, '0x'),'{0:08x}'.format(c, '0x'),'{0:08x}'.format(d, '0x'),'{0:08x}'.format(e, '0x'),'{0:08x}'.format(f, '0x'),'{0:08x}'.format(g, '0x'),'{0:08x}'.format(h, '0x')                                    


    H[0] = '{0:08x}'.format(((a + int(F[i-1][0], base = 16)) % modes), '0x')
    H[1] = '{0:08x}'.format(((b + int(F[i-1][1], base = 16)) % modes), '0x')
    H[2] = '{0:08x}'.format(((c + int(F[i-1][2], base = 16)) % modes), '0x')
    H[3] = '{0:08x}'.format(((d + int(F[i-1][3], base = 16)) % modes), '0x')
    H[4] = '{0:08x}'.format(((e + int(F[i-1][4], base = 16)) % modes), '0x')
    H[5] = '{0:08x}'.format(((e + int(F[i-1][5], base = 16)) % modes), '0x')
    H[6] = '{0:08x}'.format(((g + int(F[i-1][6], base = 16)) % modes), '0x')
    H[7] = '{0:08x}'.format(((h + int(F[i-1][7], base = 16)) % modes), '0x')
    F.append(H)
    print  (H[0],H[1],H[2],H[3],H[4],H[5],H[6],H[7])

  print('') 
  hashed = ''.join(H[i] for i in range(8))
  print(colored("encryption in progress{}...", "green"))
  wait(6)
  print (colored("Hashed encrypted file= " + hashed, 'magenta'))
  print('')
  print('')
  print(colored('this is your file in binary code:', 'yellow'))
  wait(2)
  print(M)
  wait(3)
  print(colored('<code unexpectedly stopped>', 'red'))
  print('')
  
  #####
   

if question2 == answer3:
  def password_chck(passwd):

    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
      print('length should be at least 6')
      val = True

    if len(passwd) > 20:
      print('length should be not be greater than 8')
      val = True

    if not any(char.isdigit() for char in passwd):
      print('Password should have at least one numeral')
      val = True

    if not any(char.isupper() for char in passwd):
      print('Password should have at least one uppercase letter')
      val = False

    if not any(char.islower() for char in passwd):
      print('Password should have at least one lowercase letter')
      val = False

    if not any(char in SpecialSym for char in passwd):
      print('Password should have at least one of the symbols $@#')
      val = False
    if val:
      return val


  def passwrd_check(passwd): 
        
      SpecialSym =['$', '@', '#', '%'] 
      val = True
        
      if len(passwd) < 6: 
          print('length should be at least 6') 
          val = True
            
      if len(passwd) > 20: 
          print('length should be not be greater than 8') 
          val = True
            
      if not any(char.isdigit() for char in passwd): 
          print('Password should have at least one numeral') 
          val = True
            
      if not any(char.isupper() for char in passwd): 
          print('Password should have at least one uppercase letter') 
          val = False
            
      if not any(char.islower() for char in passwd): 
          print('Password should have at least one lowercase letter') 
          val = False
            
      if not any(char in SpecialSym for char in passwd): 
          print('Password should have at least one of the symbols $@#') 
          val = False
      if val: 
          return val 

  def ceasar(text,s):
    cipherText= ""
    for ch in text:
      print ("Encrypted text is" + cipherText) 
      


  def caesar(text,s): 
    cipherText = ""
    for ch in text:
      if ch.isalpha():
        stayInAlphabet = ord(ch) + (s - 2) 
        if stayInAlphabet > ord('z'):
          stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    #print ("Your ciphertext is: ", cipherText)
    return cipherText
  #check the above function
  passwd = input("File Name:")
  print('')


  def pssword_check(passwd): 
        
      SpecialSym =['$', '@', '#', '%', '.'] 
      val = True
        
      if len(passwd) < 6: 
          print('length should be at least 6') 
          val = True
            
      if len(passwd) > 20: 
          print('length should be not be greater than 8') 
          val = True
            
      if not any(char.isdigit() for char in passwd): 
          print('Password should have at least one numeral') 
          val = True
            
      if not any(char.isupper() for char in passwd): 
          print('Password should have at least one uppercase letter') 
          val = False
            
      if not any(char.islower() for char in passwd): 
          print('Password should have at least one lowercase letter') 
          val = False
            
      if not any(char in SpecialSym for char in passwd): 
          print('Password should have at least one of the symbols $@#') 
          val = False
      if val: 
          return val 




  print ("Your File name is: " + passwd)
  print('')
  print(colored("encryption in progress{}...", 'green'))
  wait(6)
  print ("Your Encrypted File is: " + caesar(passwd,21))