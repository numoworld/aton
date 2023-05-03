from argparse import ArgumentParser
import csv

def main():
    parser = ArgumentParser(description='CSV merger')
    parser.add_argument('file_1', type=str, help='Path to the first .csv file.')
    parser.add_argument('file_2', type=str, help='Path to the second .csv file.')
    parser.add_argument('field_name', type=str, help='Name of the field to base merge on.')
    parser.add_argument('-s', '--sep', type=str, help='Separator symbol', default=';')
    parser.add_argument('-o', '--outpath', type=str, help='Path of an output file.', default='result.csv')
    args = parser.parse_args()

    try:
        import pandas as pd


        df1 = pd.read_csv(args.file_1, sep=args.sep, index_col=0)
        df2 = pd.read_csv(args.file_2, sep=args.sep, index_col=0)
        result = df1.merge(df2, on=args.field_name, how='right')
        result.index = result.index.rename('No')
        result.index += 1
        result.to_csv(args.outpath, sep=args.sep)
    except:
        import csv


        with open(args.file_1, 'r') as f1:
            csv_reader_1 = list(csv.reader(f1, delimiter=args.sep))
            with open(args.file_2, 'r') as f2:
                csv_reader_2 = list(csv.reader(f2, delimiter=args.sep))

        cols_1 = csv_reader_1[0]
        cols_2 = csv_reader_2[0]
        try:
            target_field_index_1 = cols_1.index(args.field_name)
            target_field_index_2 = cols_2.index(args.field_name)
            cols_2.remove(args.field_name)
            cols_1 = cols_1[1:]
            cols_2 = cols_2[1:]
        except ValueError:
            print('Incorrect field_name')


        with open(args.outpath, 'w') as out:
            writer = csv.writer(out, delimiter=args.sep)

            writer.writerow(['No'] + cols_1 + cols_2)
            i = 0
            for row_1 in csv_reader_1:
                for row_2 in csv_reader_2:
                    if row_1[target_field_index_1] == row_2[target_field_index_2]:
                        row = [i] + row_1[1:] + [row_2[n] for n in range(1, len(row_2)) if n != target_field_index_2]
                        writer.writerow(row)
                        i += 1
        
                    
if __name__ == "__main__":
    main()