estudantes = [ # Lista de estudantes
    "Alice",     # 0
    "Bruno",     # 1
    "Caio",      # 2
    "Diana",     # 3
    "Sergio",    # 4
    "Daniel",    # 5
    "Vinicius",  # 6
    "Thulio",    # 7
    "Lucas",     # 8
    "Hugo",      # 9
    "Matheus"    # 10
]
notas = [ # Lista de notas
    [6.0, 6.5, 8.5, 9.0],  # Notas de Alice 0
    [1.5, 2.0, 7.5, 8.0],  # Notas de Bruno 1
    [7.0, 8.0, 8.5, 9.0],  # Notas de Caio 2
    [7.5, 7.0, 5.0, 6.5],  # Notas de Diana 3
    [7.5, 7.0, 5.0, 6.5],  # Notas de Sergio 4 
    [4.5, 5.0, 6.0, 7.0],  # Notas de Daniel 5
    [8.0, 9.0, 7.5, 8.5],  # Notas de Vinicius 6
    [5.0, 6.0, 7.0, 8.0],  # Notas de Thulio 7
    [9.0, 8.5, 9.0, 10.0], # Notas de Lucas 8
    [6.0, 5.5, 7.0, 8.0],  # Notas de Hugo 9
    [7.0, 8.0, 6.5, 7.5]   # Notas de Matheus 10
]
while True:
    try:
        menu = int(input("\n0. Acessar lista de estudantes.\n1. Acessar media de notas.\n2. Sair.\nRealize sua escolha: "))
        
        if menu == 0:
            print(f"\n0. Alice: Nota: {notas[0]}\n1. Bruno: Nota: {notas[1]}\n2. Caio: Nota: {notas[2]}\n3. Diana: Nota: {notas[3]}\n4. Sergio: Nota: {notas[4]}\n5. Daniel: Nota: {notas[5]}\n6. Vinicius: Nota: {notas[6]}\n7. Thulio: Nota: {notas[7]}\n8. Lucas: Nota: {notas[8]}\n9. Hugo: Nota: {notas[9]}\n10. Matheus: Nota: {notas[10]}")
        elif menu == 1:   
            print("\n0. Alice\n1. Bruno\n2. Caio\n3. Diana\n4. Sergio\n5. Daniel\n6. Vinicius\n7. Thulio\n8. Lucas\n9. Hugo\n10. Matheus")
            escolha = int(input("\nInsira o numero do estudante: "))

            aluno = estudantes[escolha]
            notasEstudantes = notas[escolha]
            
            soma = sum(notasEstudantes)
            media = soma / len(notasEstudantes)

            if media >= 5:
                print(f"\nMuito bem {aluno} foi aprovado: Sua nota é {media}")
            else:
                print(f"\nA média das 4 notas de {aluno} é: {media}")
                notaRecuperacao = int(input("\nInsira a nota da prova de recuperação: "))
                mediaFinal = (media + notaRecuperacao) / 2
                
                if mediaFinal >= 5:
                    print(f"\nAluno(a) {aluno}, foi aprovado com media final: {mediaFinal}")
                else:
                    print(f"\nAluno(a) {aluno}, foi reprovado. Sua media é: {mediaFinal}")
        elif menu == 2:
            print("Saindo...")
            break

    except IndexError:
        print("\nInsira uma escolha valida")
        
    except ValueError:
        print("\nInsira um número valido")