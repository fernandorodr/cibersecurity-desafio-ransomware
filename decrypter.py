import os
import pyaes
from tkinter import Tk, filedialog

def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

            aes = pyaes.AESModeOfOperationCTR(key)
            decrypt_data = aes.decrypt(file_data)

            decrypted_file_path = os.path.splitext(file_path)[0] + "_decrypted.txt"
            with open(decrypted_file_path, "wb") as new_file:
                new_file.write(decrypt_data)

            print(f"Arquivo descriptografado salvo como: {decrypted_file_path}")
            return decrypted_file_path
    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")
        return None

def main():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione o arquivo criptografado para descriptografar")

    if file_path:
        key = b"testeransomwares"  # Sua chave de descriptografia

        decrypted_file = decrypt_file(file_path, key)
        if decrypted_file:
            try:
                os.remove(file_path)
                print(f"Arquivo criptografado removido: {file_path}")
            except Exception as e:
                print(f"Não foi possível remover o arquivo criptografado: {e}")

if __name__ == "__main__":
    main()
