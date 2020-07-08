import hashlib

def crack_sha1_hash(hash, use_salts= False):
    ans = ''
    f1 = open('top-10000-passwords.txt','r')
    words = f1.readlines()
    f1.close()
    wordsFix = []
    for i in words:
      wordsFix.append(i.replace('\n',''))
    f2 = open('known-salts.txt')
    salts = f2.readlines()
    f2.close()
    saltsFix = []
    for i in salts:
      saltsFix.append(i.replace('\n',''))

    #Find Pass
    for i in wordsFix:
      hashr = hashlib.sha1(i.encode())
      if hashr.hexdigest() == hash:
          return str(i)

    #Find Salted Pass
    if use_salts == True:
      for i in wordsFix:
        for j in saltsFix:
          hashr = hashlib.sha1(j.encode() + i.encode())
          if hashr.hexdigest() == hash:
            return str(i)

      for i in wordsFix:
          for j in saltsFix:
              hashr = hashlib.sha1(i.encode() + j.encode())
              if hashr.hexdigest() == hash:
                  return str(i)

    return 'PASSWORD NOT IN DATABASE'
