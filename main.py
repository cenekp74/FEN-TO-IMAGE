from PIL import Image

colors = {
    'dark_blue':{'c':(27,53,81),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 212, 55)'},
    'grey':{'c':(70,86,95),'p_font':'rgb(255,255,255)','s_font':'rgb(93,188,210)'},
    'light_blue':{'c':(93,188,210),'p_font':'rgb(27,53,81)','s_font':'rgb(255,255,255)'},
    'blue':{'c':(23,114,237),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 255, 255)'},
    'orange':{'c':(242,174,100),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'purple':{'c':(114,88,136),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 212, 55)'},
    'red':{'c':(255,0,0),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'yellow':{'c':(255,255,0),'p_font':'rgb(0,0,0)','s_font':'rgb(27,53,81)'},
    'yellow_green':{'c':(232,240,165),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'green':{'c':(65, 162, 77),'p_font':'rgb(217, 210, 192)','s_font':'rgb(0, 0, 0)'}
}

def square_to_pos(square):
    if square in range(0, 8):
        y = 700
        x = 100 * square
    elif square in range(8, 16):
        y = 600
        x = 100 * (square-8)
    elif square in range(16, 24):
        y = 500
        x = 100 * (square-16)
    elif square in range(24, 32):
        y = 400
        x = 100 * (square-24)
    elif square in range(32, 40):
        y = 300
        x = 100 * (square-32)
    elif square in range(40, 48):
        y = 200
        x = 100 * (square-40)
    elif square in range(48, 56):
        y = 100
        x = 100 * (square-48)
    elif square in range(56, 64):
        y = 0
        x = 100 * (square-56)
    return x, y

def fen_to_str(fen):
    fen = fen.split()[0]
    rows = fen.split('/')
    output = ''
    for x in range(1, 9):
        row = rows[-x]
        rowN = rows.index(row)+1
        for char in row:
            try:
                empty = int(char)
                output = output + empty*'_'
            except:
                output = output + char
    return output

def render_board(fenStr, bg, flipped):
    if flipped: fenStr = fenStr[::-1]
    for square, piece in enumerate(fenStr):
        if piece != '_':
            if piece == 'p':
                bg = render_piece('pawn', 'black', square, bg)
            elif piece == 'n':
                bg = render_piece('knight', 'black', square, bg)
            elif piece == 'b':
                bg = render_piece('bishop', 'black', square, bg)
            elif piece == 'r':
                bg = render_piece('rook', 'black', square, bg)
            elif piece == 'q':
                bg = render_piece('queen', 'black', square, bg)
            elif piece == 'k':
                bg = render_piece('king', 'black', square, bg)
            elif piece == 'P':
                bg = render_piece('pawn', 'white', square, bg)
            elif piece == 'N':
                bg = render_piece('knight', 'white', square, bg)
            elif piece == 'B':
                bg = render_piece('bishop', 'white', square, bg)
            elif piece == 'R':
                bg = render_piece('rook', 'white', square, bg)
            elif piece == 'Q':
                bg = render_piece('queen', 'white', square, bg)
            elif piece == 'K':
                bg = render_piece('king', 'white', square, bg)
    return bg

def render_piece(piece, color, square, bg):
    pieceImg = Image.open(f'img/{color}_{piece}.png')
    #Image.open(f'img/whitetile.png' if (square // 8)%2 == 0 else f'img/blacktile.png')
    bg.paste(pieceImg, square_to_pos(square), pieceImg)
    return bg


def create_bg():
    whiteTile = Image.open('img/whitetile.png', 'r')
    blackTile = Image.open('img/blacktile.png', 'r')
    bg = Image.new('RGB', (800, 800))
    for sqN in range(0, 64):
        if (sqN // 8)%2 != 0: 
            if (sqN % 2) == 0:
                bg.paste(whiteTile, square_to_pos(sqN))
            else:
                bg.paste(blackTile, square_to_pos(sqN))
        else:
            if (sqN % 2) == 0:
                bg.paste(blackTile, square_to_pos(sqN))
            else:
                bg.paste(whiteTile, square_to_pos(sqN))
    return bg