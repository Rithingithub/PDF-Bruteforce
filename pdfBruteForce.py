import pikepdf
from tqdm import tqdm

print("""   
 ____  ____  _    _____ _____      _____ ____  ____  ____  _____
/  __\/  __\/ \ /Y__ __Y  __/     /    //  _ \/  __\/   _\/  __/
| | //|  \/|| | || / \ |  \ _____ |  __\| / \||  \/||  /  |  \  
| |_\\|    /| \_/| | | |  /_\____\| |   | \_/||    /|  \__|  /_ 
\____/\_/\_\\____/ \_/ \____\     \_/   \____/\_/\_\\____/\____\
                                                                    
""")
passwords = [line.strip() for line in open("wordlist.txt")]

a = input(print("Paste the pdf file directory : "))

for password in tqdm(passwords, "Bruteforcing "):
    try:
        with pikepdf.open(a, password=password) as pdf:
            print(" Password found  : ", password)
            break
    except pikepdf._qpdf.PasswordError as e:

        continue
