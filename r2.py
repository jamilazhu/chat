def read_file(filename):
    lines = []
    with open(filename, 'r', encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    allen_word_count = 0 
    viki_word_count = 0
    allen_sticker_count =0
    viki_sticker_count =0
    allen_image_count =0
    viki_image_count =0
    for line in lines:
        s = line.split(' ')#遇到空白键请帮我切割
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else: 
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen has said', allen_word_count, 'words.')
    print('Allen has send', allen_sticker_count, 'stickers.')
    print('Allen has also send' , allen_image_count, 'images.')

    print('Viki has said', viki_word_count, 'words. ')
    print('Viki has send' , viki_sticker_count, 'stickers.')
    print('Viki has also send' , viki_image_count, 'images.')

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
        
def main():
    lines = read_file('viki.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)
    
main()

