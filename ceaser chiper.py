alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def do_again():

    mission1 = input("you want to 'encrypt' or 'decrypt':\n").lower()
    original_text = input("what is your message:\n").lower()
    shift_amount = int(input("how much you want to shift tour letters:\n"))

    if mission1 == "encrypt":
        def encrypt(original_text,shift_amount):
            shifted_text = ""   
            for i in original_text:
                if i in alphabet:
                    actual_num = alphabet.index(i)
                    flip_num = (actual_num + shift_amount)%len(alphabet) #% 26
                    shifted_text += alphabet[flip_num]
                else:
                    shifted_text += i
            print(f"your chiper text is:\n{shifted_text}")
        encrypt(original_text,shift_amount)

    else:
        def decrypt(original_text,shift_amount):
            shifted_text = ""   
            for i in original_text:
                if i in alphabet:
                    actual_num = alphabet.index(i)
                    flip_num = (actual_num - shift_amount)%len(alphabet) # %26
                    shifted_text += alphabet[flip_num]
                else:
                    shifted_text += i
            print(f"your chiper text is:\n{shifted_text}")
        decrypt(original_text,shift_amount)

do_again()

again = input("do you want to try again? yes or no?").lower()
if again == "yes":
    do_again()
else:
    print("good luck!!")