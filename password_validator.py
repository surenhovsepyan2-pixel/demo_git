print('գաղտնաբառը պետք է պարունակի գոնէ մեկ թիվ, մեծատառ, փոքրատառ, "=","+","-","!","@","#","$","%","&","*"֊ երից եւ առնվազն 6 նիշ պետք է լինի')

password = input("գրեք ձեր գաղտնաբառը: ")

tver = ["1","2","3","4","5","6","7","8","9","0"]
nshanner = ["=","+","-","!","@","#","$","%","&","*"]
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")

def password_validator(password):
    if len(password) <= 5:
        raise ValueError('առնվազն 6 նիշ պետք է լինի գաղտնաբառը')
    elif not set(tver) & set(password):
        raise ValueError('գաղտնաբառը պետք է պարունակի գոնէ մեկ թիվ')
    elif not set(nshanner) & set(password):
        raise ValueError('գաղտնաբառը պետք է պարունակի գոնէ մեկ նշան՝ "=","+","-","!","@","#","$","%","&","*"֊ երից ')
    elif not set(uppercase_letters) & set(password):
        raise ValueError('գաղտնաբառը պետք է պարունակի գոնէ մեկ մեծատառ')
    elif not set(lowercase_letters) & set(password):
        raise ValueError('գաղտնաբառը պետք է պարունակի գոնէ մեկ փոքրատառ')
    else:
        return "ձեր գաղտնաբառը ընդունվաց է"

print(password_validator(password))