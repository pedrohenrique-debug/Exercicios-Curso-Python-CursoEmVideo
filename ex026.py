frase = str(input('Digite a frase: ')).strip().lower()
a = frase.count('a')
b = frase.find('a')+1
c = frase.rfind('a')+1


print(f' A aparece {a} vezes\n Aparece primeiro na posição {b}\n Aparece ultima vez na posição {c}')