# p.hotkey('win', 'e')
import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=707, y=359)  # email
pyautogui.write("pythonauto@gmail.com")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("uau_demais_python")  # senha
pyautogui.press("enter")

tabela = pandas.read_csv("Python PowerUp\produtos.csv")

pyautogui.press("tab")  # entra nos campos de cadastro
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"] # exemplo usando variável
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"]) # aplicado diretamente
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    pyautogui.click(x=869, y=236)
