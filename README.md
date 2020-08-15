(Pt-Br)
você també pode pesquisar mais sobre IMC > [Wikipedia](https://pt.wikipedia.org/wiki/Índice_de_massa_corporal)

# Crie uma Calculadoura de IM; Descrição.

> O programa deve perdmitir a entrada do nome de usuário.

> O programa deve permitir que o usuário entre com (((unidades imperiais))) ou (((unidades métricas)))

> Se o usuário entrar com unidades imperiais de altura, deve ser adicionada feet e inches. O peso deve ser stones e pounds. O programa deve convertelos em unidades metricas e mostrar na tela.

> Se o usuário entrar com unidades metricas de altura, deve ser adicionada centimetros. O peso deve ser kilogramas. O programa deve convertelos em unidades imperiais e mostrar na tela.

> O programa deve calculas o IMC e mostart o resultado na tela, deve mostrar para o usuário as seguintes informações, __abaixo do peso__, __peso normal__, __acima do peso__, __obesidade__.

> Salvar o nome, altura, peso, em datetime de cada pessoa dentro de uma pasta __CSV__.

 IMC | Valores
:---|---:
abaixo do peso | menos de 18.5
peso normal | entre 18.5 and 24.9
acima do peso | entre 25 e 29.9
obesidade | 30 ou maior

## Front-end
 * Tkinter
   * O que é Tkinter
   * Tkinter é um framework GUI (Graphical User Interface)
   * Você pode saber mais no [Wikipedia-Tkinter](https://pt.wikipedia.org/wiki/Tkinter)

## Back-end
* Linguagem Pyhton
* CSV ( Banco de Dados )
  * Você pode saber mais no [wikipedia-CSV](https://pt.wikipedia.org/wiki/Comma-separated_values)
  * Exemplo abaixo
```
from tkinter.filedialog import askopenfilename

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    #df = pd.read_csv(csv_file_path)

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
root.mainloop()
```
