import pyscreenshot as image_grab
from datetime import datetime
import argparse
from pynput import mouse


def on_click(x, y, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if pressed:
        if args.mouse_x1 < x < args.mouse_x2:
            if args.mouse_y1 < y < args.mouse_y2:
                grab_screen(args.x1, args.y1, args.x2, args.y2, args.prefix, args.fldr)
    if not pressed:
        return False


def grab_screen(x_1, y_1, x_2, y_2, pfx, folder):
    now = datetime.now()
    im = image_grab.grab(bbox=(x_1, y_1, x_2, y_2))  # X1,Y1,X2,Y2
    pdf = folder + "/PDF/" + pfx + "_" + now.strftime("%H-%M-%S") + '.pdf'
    png = folder + "/PNG/" + pfx + "_" + now.strftime("%H-%M-%S") + '.png'
    im.save(pdf)
    im.save(png)
    print('Saved to: ' + pdf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automated Screen Capture.')

    # Screen capture bounds.
    parser.add_argument('--x1', type=int,
                        help='Screen capture area X1.')
    parser.add_argument('--y1', type=int,
                        help='Screen capture area Y1.')
    parser.add_argument('--x2', type=int,
                        help='Screen capture area X2.')
    parser.add_argument('--y2', type=int,
                        help='Screen capture area Y2.')

    # Mouse click boundary.
    parser.add_argument('--mouse_x1', type=int,
                        help='Screen capture area X1.')
    parser.add_argument('--mouse_y1', type=int,
                        help='Screen capture area Y1.')
    parser.add_argument('--mouse_x2', type=int,
                        help='Screen capture area X2.')
    parser.add_argument('--mouse_y2', type=int,
                        help='Screen capture area Y2.')

    parser.add_argument('--prefix', type=str,
                        help='Image prefix string.')
    parser.add_argument('--fldr', type=str,
                        help='Folder directory.')

    args = parser.parse_args()

    while True:
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
