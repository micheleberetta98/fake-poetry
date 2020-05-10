import random
from argparse import ArgumentParser

parser = ArgumentParser(
    description="Fake Poetry Generator")

parser.add_argument('input',
                    metavar='INPUT_FILE',
                    help='The input file with the original text'
                    )
parser.add_argument('-o', '--output',
                    help='An output file, if wanted',
                    default=None
                    )
parser.add_argument('-w', '--words',
                    help='Total number of words (default 100)',
                    default=100
                    )

args = parser.parse_args()


def build_dict(words):
    data = {}

    for i in range(len(words) - 2):
        prefix = ' '.join([words[i], words[i + 1]])
        suffix = words[i + 2]

        if prefix in data:
            data[prefix].append(suffix)
        else:
            data[prefix] = [suffix]

    return data


def create_text(original_text, total_words_len):
    words = original_text.split(' ')
    words.append('END')

    d = build_dict(words)

    prefix = ' '.join([words[0], words[1]])
    suffix = ''
    final_text = prefix

    count = 2
    while count < total_words_len:
        if prefix not in d:
            print(f'PREFIX NOT FOUND: {prefix}')
            print('Stopping...')
            break

        rnd = random.randint(0, len(d[prefix]) - 1)
        suffix = d[prefix][rnd]

        if suffix == 'END':
            break

        final_text += f' {suffix}'
        prefix = prefix.split(' ')[1] + ' ' + suffix
        count += 1

    return final_text


if __name__ == '__main__':
    original_text = ''
    with open(args.input) as fin:
        original_text = fin.read()

    final_text = create_text(original_text, int(args.words))

    if args.output is None:
        print(" === HERE'S YOUR POTERY ===")
        print(final_text)
    else:
        with open(args.output, 'w') as fout:
            fout.write(final_text)
