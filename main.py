#!/usr/bin/env python3
import sys
import Image

def rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    if lv == 3:
        value *= 2
        lv *= 2
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def create_new_img_mask(input_path, output_path, color):
    r, g, b = color
    im = Image.open(input_path, 'r')
    out = Image.new('RGBA', im.size, (0, 0, 0, 0))

    width, height = im.size
    for x in range(width):
            for y in range(height):
                p = im.getpixel((x,y))
                if len(p) == 4:
                    if p[3] != 0:
                        out.putpixel((x,y), (r, g, b, p[3]))
                else:
                    if p[1] != 0:
                        out.putpixel((x,y), (r, g, b, p[1]))
    out.save(output_path, "PNG")
    out.show()
    return out

def main():
    if len(sys.argv) < 4:
        print("Expected 3 arguments...\nTry again and add\n    ./PATH_TO_INPUT_FILE ./PATH_TO_OUTPUT_FILE '#HEXCODE'")
    elif len(sys.argv[3]) != 7 and len(sys.argv[3]) != 4:
        print('Invalid Hexcode!\n    Make sure your hexcode has a # symbol followed by 3 or 6 characters 0-9 and A-F.')
    else:
        input_path = str(sys.argv[1])
        output_path = str(sys.argv[2])
        color = rgb(sys.argv[3])
        create_new_img_mask(input_path, output_path, color)
    return


if __name__ == '__main__':
    main()
