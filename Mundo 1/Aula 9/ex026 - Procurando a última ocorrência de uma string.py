print("Contagem de A's")
x = str(input('Digite uma frase: ').strip().lower())

print(f"Essa frase tem {x.count('a')} A's"
      f'O primeiro a aparece na posição {x.find("a") + 1}'
      f'O último a aparece na posição {x.rfind("a") + 1}')
