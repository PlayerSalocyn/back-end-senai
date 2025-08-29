def recurso_caminho(relativo):
    import os
    import sys
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relativo)  # .exe em execução
    return os.path.join(os.path.abspath("."), relativo)


def show_image(image_path, new_width=300):
    import tkinter as tk
    from PIL import Image, ImageTk
    # Criar a janela principal do Tkinter
    root = tk.Tk()
    root.title("Exibir Imagem Redimensionada")

    # Abrir a imagem com Pillow
    img = Image.open(image_path)

    # Redimensionar a imagem mantendo a proporção
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    img_resized = img.resize((new_width, new_height))

    # Converter a imagem redimensionada para um formato que o Tkinter pode exibir
    img_tk = ImageTk.PhotoImage(img_resized)

    # Criar um widget Label para exibir a imagem
    label = tk.Label(root, image=img_tk)
    label.pack()

    # Iniciar o loop da interface gráfica do Tkinter
    root.mainloop()