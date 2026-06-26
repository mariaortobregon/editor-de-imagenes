from PIL import Image, ImageDraw, ImageFont


class jugador:
    def __init__(self, nombre, edad, equipo, estatura, peso):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
        self.estatura = estatura
        self.peso = peso
    def info(self):
        print("Jugador", self.nombre, "creado")
        print("edad: ", self.edad)

def crear_carta(jugador, foto_path):
    
    carta = Image.new("RGB", (250, 350), "blue")
    draw = ImageDraw.Draw(carta)
    font = ImageFont.truetype("mifuente.otf", 25)

    draw.text((10,10), jugador.nombre, font=font, fill="black")
    draw.text((10, 40), f"{jugador.edad}", font=font, fill="blue")
    draw.text((10,70), f"{jugador.edad}", font=font, fill="pink")
    draw.text((10, 100), f"{jugador.equipo}", font=font, fill="green")
    draw.text((10, 130), f"{jugador.estatura}", font=font, fill="black")
    draw.text((10, 160), f"{jugador.peso}", font=font, fill="blue" )

    foto = Image.open(foto_path).convert("RGB")
    foto = foto.resize((130, 150))
    carta.paste(foto, (60, 180))

    filename = f"carta_{jugador.nombre}.png"
    carta.save(filename)
    print("💥carta guardada como ", filename)

    carta.show()
    return carta
Grigio = jugador("Grigio", 0.2, " Pastor Aleman", 90, 6,)
Bruno = jugador("Bruno", 7, "shit zhu", 85, 6)
Maika = jugador("Maika", 1, "salchicha", 65, 4)
ComoTu = jugador("ComoTu", 4, "chihuahua", 85, 5.5)


Grigio.info()
Bruno.info()
Maika.info()
ComoTu.info()

crear_carta(Grigio, "pastor.png")
crear_carta(Bruno, "shit-zhu.png")