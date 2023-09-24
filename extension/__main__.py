import os

from extension import decrypt, encrypt


def main():
    print("CRIPTOGRAFIA DE CATS")
    while True:
        print("Escolha uma opção:")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")
        os.system("cls")

        if opcao == "1":
            texto = input("Digite o texto a ser criptografado: ")
            print("Texto criptografado: " + encrypt(texto))
            controler = input("Deseja voltar ao menu? (s/n): ")
            if controler == "s":
                os.system("cls")
                continue
            else:
                print("Saindo...")
                break
        elif opcao == "2":
            texto = input("Digite o texto a ser descriptografado: ")
            print("Texto descriptografado: " + decrypt(texto))
            controler = input("Deseja voltar ao menu? (s/n): ")
            if controler == "s":
                os.system("cls")
                continue
            else:
                print("Saindo...")
                break
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
        
