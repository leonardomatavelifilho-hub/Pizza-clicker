import pyxel

# --- CONFIGURAÇÕES ---
IX, IY = 5, 20      # Puxei a sucata para a esquerda
CLIQUES = 0
VALOR_CLIQUE = 1
PRECO_UP = 10
TIMER = 0


def update():
    global CLIQUES, VALOR_CLIQUE, PRECO_UP, TIMER
    
    if TIMER > 0: TIMER -= 1

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        # 1. CLIQUE NA SUCATA
        if (pyxel.mouse_x >= IX and pyxel.mouse_x <= IX + 30 and 
            pyxel.mouse_y >= IY and pyxel.mouse_y <= IY + 20):
            CLIQUES += VALOR_CLIQUE
            TIMER = 3
            # pyxel.play(3, 0) # Som do clique

        # 2. CLIQUE NO BOTÃO DE UPGRADE (Lojinha)
        # Vamos colocar o botão no canto direito: X de 110 a 155, Y de 50 a 70
        if (pyxel.mouse_x >= 110 and pyxel.mouse_x <= 155 and 
            pyxel.mouse_y >= 50 and pyxel.mouse_y <= 70):
            if CLIQUES >= PRECO_UP:
                CLIQUES -= PRECO_UP
                VALOR_CLIQUE += 1
                PRECO_UP *= 2 # Fica mais caro cada vez que compra
                # pyxel.play(3, 1) # Som de compra

         if (pyxel.mouse_x >= 140 and pyxel.mouse_x <= 155 and 
            pyxel.mouse_y >= 60 and pyxel.mouse_y <= 80):
            if CLIQUES >= PRECO_UP:
                CLIQUES -= PRECO_UP
                VALOR_CLIQUE += 1
                PRECO_UP *= 2

def draw():
    pyxel.cls(0)
    
    # Desenha a Sprite Gigante (Sucata)
    if TIMER > 0:
        pyxel.rect(IX, IY, 40, 20, 7)
    pyxel.blt(IX, IY, 0, 0, 0, 600, 400, 100)
    
    # INTERFACE PRINCIPAL
    pyxel.rect(0, 0, 160, 12, 1) # Barra do topo
    pyxel.text(5, 4, f"CLIQUES: {CLIQUES}", 7)
    pyxel.text(100, 4, f"VALOR: +{VALOR_CLIQUE}", 10)

    # BOTÃO DA LOJINHA (Fica sempre visível)
    cor_botao = 11 if CLIQUES >= PRECO_UP else 8
    pyxel.rect(110, 50, 45, 20, cor_botao)
    pyxel.rectb(110, 50, 45, 20, 7) # Bordinha
    pyxel.text(113, 54, "UPGRADE", 0)
    pyxel.text(113, 62, f"${PRECO_UP}", 0)

    cor_botao = 11 if CLIQUES >= PRECO_UP else 8
    pyxel.rect(140,60,45,20, cor_botao)

    # DICA
    pyxel.text(110, 80, "AUMENTA OS", 6)
    pyxel.text(110, 88, "CLIQUES!", 6)

    # Cursor
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, 1, 7)

pyxel.init(160, 120, title="Pizza Clicker")
pyxel.load("asset.pyxres")
pyxel.playm(0, loop=True)
pyxel.run(update, draw)
