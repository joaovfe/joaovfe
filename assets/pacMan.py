from PIL import Image, ImageDraw
import os

frame_count = 10
output_folder = "assets/pacman/"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Criar 10 quadros de animação
for i in range(frame_count):
    img = Image.new('RGB', (100, 100), color = (0, 0, 0))
    draw = ImageDraw.Draw(img)
    pacman_size = 50
    pacman_angle = i * 36 

    draw.pieslice([25, 25, 25+pacman_size, 25+pacman_size], start=0, end=pacman_angle, fill="yellow")

    img.save(f"{output_folder}/pacman_frame_{i}.png")
