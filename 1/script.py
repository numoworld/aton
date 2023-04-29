from pathlib import Path


def main():
    dirpath = Path('/srv/example/foo/bar')
    filenames = [f.name[:-4] + '\n' for f in dirpath.rglob("*.csv")]
    try:
        with open('csv_files.txt', 'w') as f:
            f.writelines(filenames)
    except IOError:
        print('Can\'t write result to the file.')
        print('Result:')
        print(*filenames, sep='', end='')

    
if __name__ == "__main__":
    main()