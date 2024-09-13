import string
def textstrip(f):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    f = open('english_random.txt','r') #open the file
    text=f.read() #read the file
    text=text.lower() #convert to lower case letters
    s='' #empty string
    for i in text: #for loop to iterate through characters
        if i in "abcdefghijklmnopqrstuvwxyz": #if the character is a lower case letter then add it to the empty string
            s+=i #add the character to the empty string
    return s #return the string
    
#textstrip('english_random.txt')
def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d={} #empty dictionary
    for i in s: #for loop to iterate through the characters
        if i in d: #if the character is already in the dictionary then add 1 to the value
            d[i]+=1#add 1 to the value
        else: #if the character is not in the dictionary then add it to the dictionary and make the value 1
            d[i]=1 #add the character to the dictionary and make the value 1
   # for i in 'abcdefghijklmnopqrstuvwxyz': #for loop to iterate through the alphabet
      #print(i,d[i]) #print the letter and the value
    return d #return the dictionary
        
#m=letter_distribution(textstrip('english_random.txt'))

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    d={} #here we are considering any given dictionary d which contains substitutions for all the letters
    result='' #empty string
    for i in s: #for loop to iterate through the characters
      result+=d[i] #add the substitution for the character to the empty string
    return result #return the string

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    d={} #here we are considering any given dictionary d which contains substitutions for all the letters
    result='' #empty string
    for j in s: #for loop to iterate through the characters
      for i in 'abcdefghijklmnopqrstuvwxyz': #for loop to iterate through the alphabet
        if j==d[i]: #if the character is equal to the substitution for the letter then add the letter to the empty string
          result=result+i #add the letter to the empty string
    return result #return the string


def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    d={} #empty dictionary
    f=letter_distribution(s) #call the function letter_distribution to get the frequency of the letters in the string
    sort_f=sorted(f,key=f.get,reverse=True) #sort the frequency of the letters in descending order
    actual_f='etaoinshrdlcumwfgypbvkjxqz' #the actual frequency of the letters in the english language
    for i in range(26): #for loop to iterate through the letters
      d[actual_f[i]]=sort_f[i] #add the actual frequency of the letters to the dictionary
    return d #return the dictionary
#print(cryptanalyse_substitution(textstrip('english_random.txt')))



def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    result=''#empty string
    d={} #empty dictionary
    r=1 #variable r is 1
    alpha='abcdefghijklmnopqrstuvwxyz' #alphabet
    for i in alpha: #for loop to iterate through the alphabet
      d[i]=r #add the letter to the dictionary and make the value r
      r+=1 #add 1 to r
    for i in range(len(s)): #for loop to iterate through the characters
      b=d[s[i]]+d[password[i%len(password)]] #add the value of the character to the value of the password
      result+=alpha[b%26-1] #add the character to the empty string
    return result #return the string
#print(vigenere_encrypt(textstrip('english_random.txt'),'arunima'))

      
def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    result=''#empty string
    alpha='abcdefghijklmnopqrstuvwxyz'#alphabet
    d={}#empty dictionary
    r=1#variable r is 1
    for i in alpha:#for loop to iterate through the alphabet
      d[i]=r#add the letter to the dictionary and make the value r
      r+=1#add 1 to r
    for i in range(len(s)): #for loop to iterate through the characters
      b=d[s[i]]-d[password[i%len(password)]]#subtract the value of the character from the value of the password
      result+=alpha[b%26-1]#add the character to the empty string
    return result#return the string

    

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    t=s[r:]+s[:r] #rotate the string by r places
    noc=0 #number of collisions is 0 initially
    percent=0.0 #percentage of collisions is 0.0 initially
    for i in range(len(s)): #for loop to iterate through the characters
      if s[i]==t[i]: #if the character is equal to the character in the rotated string then add 1 to the number of collisions
        noc+=1 #add 1 to the number of collisions
    percent=noc/len(s) #calculate the percentage of collisions
    return percent #return the percentage of collisions
    

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    d={} #empty dictionary
    password='' #empty string
    
    alpha='abcdefghijklmnopqrstuvwxyz' #alphabet
    r=1 #variable r is 1
    for i in alpha: #for loop to iterate through the alphabet
      d[i]=r #add the letter to the dictionary and make the value r
      r+=1 #add 1 to r
    for i in range(k): #for loop to iterate through the characters
      s1='' #empty string
      for j in range(i,len(s),k): #for loop to iterate through the characters
        s1+=s[j] #add the character to the empty string
      f=cryptanalyse_substitution(s1) #call the function letter_distribution to get the frequency of the letters in the string
      fe=f['e'] #the most frequent letter
      password=password+alpha[((d[fe]-d['e'])%26)-1] #add the letter to the password
    return password #return the password
#print(cryptanalyse_vigenere_afterlength(vigenere_encrypt(textstrip('english_random.txt'),'arunima'),7))
#print(cryptanalyse_vigenere_afterlength('fghfghfghfghfghfghfghfghfghfgfhfgfhfgfhfgh',3))



def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    r=1 #variable r is 1
    percent=0.0 #percentage of collisions is 0.0 initially
    t='' #empty string to store rotated strings
    for i in range(len(s)): #for loop to iterate through the characters
      t=s[r:]+s[:r] #rotate the string by r places
      noc=0 #number of collisions is 0 initially
      for i in range(len(s)): #for loop to iterate through the characters
        if s[i]==t[i]: #if the character is equal to the character in the rotated string then add 1 to the number of collisions
          noc+=1 #add 1 to the number of collisions
      percent=noc/len(s) #calculate the percentage of collisions
      if percent>0.06:#if the percentage of collisions is greater than 0.06 then return the value of r it will be length of password
        return r #return length of password
        break #break the loop
        
      r+=1 #add 1 to r to rotate the string by 1 more place

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    r=cryptanalyse_vigenere_findlength(s) #call the function cryptanalyse_vigenere_findlength to get the length of the password
    f=cryptanalyse_vigenere_afterlength(s,r) #call the function cryptanalyse_vigenere_afterlength to get the password
    x=vigenere_decrypt(s,f) #call the function vigenere_decrypt to get the plaintext
    print('Password: ',f) #print the plaintext
    return x #return the password 

text=cryptanalyse_vigenere(vigenere_encrypt(textstrip('english_random.txt'),'arunima'))
print(text)
if text==textstrip('english_random.txt'):
  print('True')
else:
  print('False')
