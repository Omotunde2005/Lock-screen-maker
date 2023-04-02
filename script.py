from PIL import Image, ImageDraw, ImageFont
import datetime

months = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUNE',
    7: 'JULY',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC'
}

days = {
    0: 'MON',
    1: 'TUES',
    2: 'WED',
    3: 'THUR',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN'
}


def lock_screen(filename):
    image = Image.open(filename)
    image.thumbnail((900, 1280))
    width, height = image.size
    draw = ImageDraw.Draw(image)

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    if minute < 10:
        minute = f'0{minute}'

    weekday = datetime.datetime.now().weekday()
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    meridian = 'AM'

    if int(hour) > 12:
        meridian = 'PM'

    font_size = int(width / 5)

    font = ImageFont.truetype('timesbd.ttf', font_size)
    x, y = int(width / 2.0), int(height / 3)
    draw.text((x, y), text=f"{hour}:{minute}", font=font, fill='#FFF', anchor='ms', align='center')

    new_font = ImageFont.truetype('times.ttf', int(width / 16))
    draw.text((int(width / 2.0), int(height / 2.5)), text=f'{days[weekday]}, {months[month]} {day} {meridian}',
              font=new_font, fill='#FFF', anchor='ms', align='left')
    image.save('new_image.jpg')


if __name__ == "__main__":
    while True:
        filename = input('Paste the path to the image')
        try:
            lock_screen(filename)
        # Incase you did not enter a value or entered a wrong file path
        except:
            pass
        else:
            exit()
