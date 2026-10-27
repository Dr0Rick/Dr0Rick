import zlib, struct

W = H = 32
g = [["B"] * W for _ in range(H)]
def put(x, y, c):
    if 0 <= x < W and 0 <= y < H:
        g[y][x] = c
def span(y, x0, x1, c):
    for x in range(x0, x1 + 1):
        put(x, y, c)

# ---- wild hair: uneven spike heights per column, flaring out at the sides
TOP = {6:9, 7:6, 8:3, 9:5, 10:2, 11:4, 12:2, 13:5, 14:3, 15:1, 16:4,
       17:2, 18:4, 19:1, 20:3, 21:5, 22:2, 23:6, 24:4, 25:7, 26:9}
for x, t in TOP.items():
    bot = 12 if (x <= 9 or x >= 22) else 8          # short at sides so it flares
    for y in range(t, bot + 1):
        # soft, ragged shadow boundary instead of one hard vertical split
        shade = (x >= 20 and y >= t + 2) or (x >= 23) or (x <= 8 and y >= 10)
        put(x, y, "h" if shade else "H")
# two flyaway tufts, attached so they don't read as dust
put(5, 10, "h"); put(27, 10, "h")

# ---- face
FACE = {9:(11,20), 10:(10,21), 11:(10,21), 12:(10,21), 13:(10,21),
        14:(10,21), 15:(11,20), 16:(11,20), 17:(12,19), 18:(13,18)}
for y, (a, b) in FACE.items():
    span(y, a, b, "S")
span(13, 9, 9, "s"); span(13, 22, 22, "s")          # ears
span(14, 9, 9, "s"); span(14, 22, 22, "s")

# ---- brows (right one raised = manic)
span(11, 12, 14, "K")
span(10, 17, 19, "K")
# ---- eyes
span(12, 12, 14, "E"); span(13, 12, 14, "E")
span(12, 17, 19, "E"); span(13, 17, 19, "E")
put(13, 12, "P"); put(18, 12, "P")
# ---- nose + crooked grin
span(15, 15, 16, "s")
span(16, 13, 17, "M"); put(18, 15, "M")
span(17, 14, 16, "s")

# ---- neck
span(19, 14, 17, "s")

# ---- lab coat, shoulders widening
COAT = {20:(12,19), 21:(10,21), 22:(9,22), 23:(8,23), 24:(7,24),
        25:(6,25), 26:(6,25), 27:(5,26), 28:(5,26), 29:(5,26),
        30:(5,26), 31:(5,26)}
for y, (a, b) in COAT.items():
    span(y, a, b, "C")
    for x in range(b - 3, b + 1):
        put(x, y, "c")                               # right-side shading
# ---- shirt showing through the lapel V
for i, y in enumerate(range(20, 27)):
    half = max(0, 3 - i // 2)
    span(y, 15 - half, 16 + half, "T")
# lapel edges: hug the shirt V on both sides, nothing floating
for i, y in enumerate(range(20, 27)):
    half = max(0, 3 - i // 2)
    put(15 - half - 1, y, "c"); put(16 + half + 1, y, "c")

PAL = {
    "B": (0x22, 0x2a, 0x37, 255), "K": (0x14, 0x1a, 0x22, 255),
    "H": (0xa8, 0xc2, 0xd6, 255), "h": (0x7d, 0x97, 0xad, 255),
    "S": (0xe8, 0xc3, 0xa0, 255), "s": (0xc2, 0x98, 0x76, 255),
    "E": (0xff, 0xff, 0xff, 255), "P": (0x14, 0x1a, 0x22, 255),
    "M": (0x8a, 0x4a, 0x52, 255), "C": (0xf4, 0xf6, 0xf9, 255),
    "c": (0xc6, 0xcc, 0xd6, 255), "T": (0x2f, 0x8f, 0x8f, 255),
    "G": (0x7a, 0xe5, 0x82, 255),
}
# outline every edge against the background
out = [r[:] for r in g]
for y in range(H):
    for x in range(W):
        if g[y][x] != "B":
            continue
        if any(0 <= y+dy < H and 0 <= x+dx < W and g[y+dy][x+dx] != "B"
               for dy, dx in ((-1,0),(1,0),(0,-1),(0,1))):
            out[y][x] = "K"
g = out

def png(path, grid, scale):
    raw = bytearray()
    for row in grid:
        line = bytearray()
        for ch in row:
            line += bytes(PAL[ch]) * scale
        raw += (b"\x00" + line) * scale
    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))
    ihdr = struct.pack(">IIBBBBB", len(grid[0])*scale, len(grid)*scale, 8, 6, 0, 0, 0)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))

png("rick-512.png", g, 16)
png("rick-32.png", g, 1)
print("ok")
