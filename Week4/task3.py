import os
my_txt_files = [i for i in os.listdir() if i[-4:] == ".txt"]
my_files = [i for i in os.listdir() if i[-4:] != ".txt"]
print(f"Txt files list: {my_txt_files} \t Files list: {my_files}")