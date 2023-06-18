import os
import zipfile
import time
from colorama import Fore, Style

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome_message():
    print(Fore.GREEN + "==========[Selamat datang di toko teh! (x=keluar)]==========" + Style.RESET_ALL)
    print(Fore.BLUE + "By Driyan" + Style.RESET_ALL)
    print("")

def get_input(prompt):
    return input(Fore.RED + prompt + Style.RESET_ALL)

def aqua_mode():
    path = input(Fore.CYAN + "path? (ex: D:\\Images\\fire.mp4)=" + Style.RESET_ALL)
    ip1 = input("input: ")

    if ip1.endswith('.mp4'):
        base_path = os.path.dirname(path)
        file_name = os.path.basename(path)
        file_name_without_ext = os.path.splitext(file_name)[0]

        # Mengubah file menjadi arsip .zip
        with zipfile.ZipFile(os.path.join(base_path, file_name_without_ext + '.zip'), 'w') as zipf:
            zipf.write(path, file_name)
        
        print("File telah dienkripsi")
        input("Tekan Enter untuk melanjutkan...")
 
	# Mengubah ekstensi file zip menjadi .xyz
        zip_path = os.path.join(base_path, file_name_without_ext + '.zip')
        xyz_path = os.path.join(base_path, file_name_without_ext + '.xyz')

        os.rename(zip_path, xyz_path)
        print("Ekstensi file zip telah diubah menjadi .xyz")	

        # Menghapus file asli setelah dienkripsi
        os.remove(path)
    else:
        print("Input1 bukan file dengan ekstensi .mp4")

def teh_mode():
    path = input(Fore.YELLOW + "path? (ex: D:\\Images\\fire.xyz)=" + Style.RESET_ALL)
    ip1 = input("Input1: ")

    if ip1.endswith('.xyz'):
        base_path = os.path.dirname(path)
        file_name = os.path.basename(path)
        file_name_without_ext = os.path.splitext(file_name)[0]

        zip_file_path = os.path.join(base_path, file_name_without_ext + '.zip')

        # Mengubah file menjadi .zip
        os.rename(path, zip_file_path)

        # Mengekstrak file .zip
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            zipf.extractall(base_path)
        
        print("File telah selesai dipulihkan...")
        input("Tekan Enter untuk melanjutkan...")

        # Menghapus file asli setelah dipulihkan
        os.remove(zip_file_path)
    else:
        print("Input1 bukan file dengan ekstensi .xyz")



def main():
    clear_screen()
    welcome_message()

    while True:
        input1 = get_input("Mau minum teh? ")
        if input1 == "mau makan apel":
            aqua_mode()
        elif input1.lower() == "ya":
            teh_mode()
        elif input1.lower() == "x":
            break
        else:
            print("Input tidak valid")
        
        time.sleep(0.5)
        clear_screen()
        welcome_message()

if __name__ == '__main__':
    main()
