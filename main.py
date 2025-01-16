import pandas
import pyautogui
import time 

pyautogui.PAUSE = 0.5

# Abrir o Chrome
pyautogui.hotkey("win", "s")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.click(x=417, y=458)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar carregar o site
time.sleep(3) 
    
# Inserir o login
pyautogui.press("tab")
pyautogui.write("arielm11@gmail.com")
pyautogui.press("tab")
pyautogui.write("arielm11")
pyautogui.press("tab")
pyautogui.press("enter")

# Importar a base de dados
caminho_bd = "Cópia de produtos.csv"
dados = pandas.read_csv(caminho_bd)
print(dados) 

# Inserindo os dados
for linha in dados.index:
    pyautogui.click(x=447, y=295)
    pyautogui.write(str(dados.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(dados.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pandas.isna(dados.loc[linha, "obs"]):
        pyautogui.write(str(dados.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("pageup")