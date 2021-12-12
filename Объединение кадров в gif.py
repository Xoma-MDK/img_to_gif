from PIL import Image
 
# Список для хранения кадров.
frames = []
 
for frame_number in range(0, 720):
    # Открываем изображение каждого кадра.
    frame = Image.open(f'C:/Users/molot/Desktop/Колледж/ИТ/Анимация/кадры/gif/{frame_number}.gif')
    # Добавляем кадр в список с кадрами.
    frames.append(frame)
 
# Берем первый кадр и в него добавляем оставшееся кадры.
frames[0].save(
    'animate2.gif',
    save_all=True,
    append_images=frames[1:],  # Срез который игнорирует первый кадр.
    optimize=True,
    duration=0.042,
    loop=0
)