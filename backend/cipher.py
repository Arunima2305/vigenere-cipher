import string

def textstrip(text):
    """This function takes a string and converts its content to lowercase,
    removing all spaces and special characters, retaining only lowercase letters."""
    text = text.lower()
    s = ''.join([i for i in text if i in string.ascii_lowercase])
    return s

def letter_distribution(s):
    """Given a string s comprising only lowercase letters, count the number of occurrences of each letter and return a dictionary."""
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def substitution_encrypt(s, d):
    """Encrypt the contents of s using the dictionary d, which contains substitutions for the 26 letters.
    Return the resulting string."""
    result = ''
    for i in s:
        result += d.get(i, i)
    return result

def substitution_decrypt(s, d):
    """Decrypt the contents of s using the dictionary d, which contains substitutions for the 26 letters.
    Return the resulting string."""
    reverse_d = {v: k for k, v in d.items()}
    result = ''
    for j in s:
        result += reverse_d.get(j, j)
    return result

def cryptanalyse_substitution(s):
    """Given that the string s is encrypted using some substitution cipher, predict the substitution dictionary."""
    f = letter_distribution(s)
    sort_f = sorted(f, key=f.get, reverse=True)
    actual_f = 'etaoinshrdlcumwfgypbvkjxqz'
    d = {}
    for i in range(min(26, len(sort_f))):
        d[sort_f[i]] = actual_f[i]
    return d

def vigenere_encrypt(s, password):
    """Encrypt the string s using the Vigenère cipher method with the given password and return the resulting string."""
    result = ''
    alpha = string.ascii_lowercase
    d = {char: idx + 1 for idx, char in enumerate(alpha)}
    for i in range(len(s)):
        b = d[s[i]] + d[password[i % len(password)]]
        result += alpha[(b % 26) - 1]
    return result

def vigenere_decrypt(s, password):
    """Decrypt the string s using the Vigenère cipher method with the given password and return the resulting string."""
    result = ''
    alpha = string.ascii_lowercase
    d = {char: idx + 1 for idx, char in enumerate(alpha)}
    for i in range(len(s)):
        b = d[s[i]] - d[password[i % len(password)]]
        result += alpha[(b % 26) - 1]
    return result

def rotate_compare(s, r):
    """Rotate the string s by r places and compare s(0) with s(r) to return the proportion of collisions."""
    t = s[r:] + s[:r]
    noc = sum(1 for i in range(len(s)) if s[i] == t[i])
    return noc / len(s)

def cryptanalyse_vigenere_findlength(s):
    """Given the string s, find out the length of the password using which it was encrypted."""
    for r in range(1, len(s)):
        if rotate_compare(s, r) > 0.06:
            return r
    return None

def cryptanalyse_vigenere_afterlength(s, k):
    """Given the string s, which is known to be Vigenère encrypted with a password of length k, find out the password."""
    alpha = string.ascii_lowercase
    d = {char: idx + 1 for idx, char in enumerate(alpha)}
    password = ''
    for i in range(k):
        s1 = ''.join(s[j] for j in range(i, len(s), k))
        f = cryptanalyse_substitution(s1)
        fe = f.get('e', 'a')
        password += alpha[(d[fe] - d['e']) % 26]
    return password

def cryptanalyse_vigenere(s):
    """Given the string s, cryptanalyse the Vigenère cipher, outputting the password as well as the plaintext."""
    r = cryptanalyse_vigenere_findlength(s)
    if r is None:
        return None, "Unable to determine password length."
    f = cryptanalyse_vigenere_afterlength(s, r)
    x = vigenere_decrypt(s, f)
    return f, x
