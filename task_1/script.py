from pathlib import Path


def main():
    try:
        path = input('Enter path to the folder: ')
        dirpath = Path(path)
        filenames = [f.name[:-4] + '\n' for f in dirpath.rglob("*.csv")]
    except:
        print('Incorrect path to the folder.')

    print('\nResult:')
    print(*filenames, sep='', end='')
        
    
if __name__ == "__main__":
    main()