def yo_to_rom(yo, raw=None):
    import re
    import os
    if yo[-3:] != '.yo':
        raise IOError(f'{yo} is not a valid .yo file')
    if raw is None:
        raw = yo[:-3]
    glob_cnt = 0
    with open(raw, "w") as rom:
        rom.write('v2.0 raw\n')
        with open(yo, "r") as yo:
            l = yo.readline()
            i = l.index('|')
            j = None
            while ':' not in l:
                l = yo.readline()
            j = l.index(':')
            k = l.index('.') + 1
            cnt = 1
            bit_align = False
            for l in yo:
                if l[k:k+3] == 'pos' or l[k:k+5] == 'align':
                    _pos_bool = l[k:k+3] == 'pos'
                    char_pos = k + (4 if _pos_bool else 6)
                    bit_align = True
                if bit_align:
                    int_chars = []
                    while (l[char_pos].isdigit()):
                        int_chars.append(l[char_pos])
                        char_pos += 1
                    _pos = int(''.join(int_chars).strip())
                    if _pos_bool:
                        while glob_cnt < _pos:
                            if cnt < 4:
                                rom.write('00 ')
                            else:
                                rom.write('00\n')
                                cnt = 0
                            cnt += 1
                            glob_cnt += 1
                    else:
                        while cnt < _pos:
                            if not cnt % 4:
                                rom.write('00\n')
                            else:
                                rom.write('00 ')
                            glob_cnt += 1
                            cnt += 1
                        rom.write('00\n')
                        cnt = 1
                    bit_align = False
                else:
                    if l[j] != ':':
                        if l[j+1] == ':':
                            j += 1
                        else:
                            continue
                    code = re.findall('..?', l[j+1:i].strip())
                    for c in code:
                        rom.write(c)
                        if cnt == 4:
                            cnt = 0
                            rom.write('\n')
                        else:
                            rom.write(' ')
                        cnt += 1
                    glob_cnt += 1
        while cnt < 4:
            rom.write('00 ')
            cnt += 1
        else:
            rom.write('00\n')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Turn a y86 .yo file into a raw Logisim ROM file.')
    parser.add_argument('src', metavar='path_to_yo...', type=str)
    parser.add_argument('--dst', metavar='path_to_raw...', type=str, default=None,
                        help='path to the raw destination file (default: same name as src file minus the .yo suffix)')
    args = parser.parse_args()
    yo_to_rom(args.src, args.dst)
