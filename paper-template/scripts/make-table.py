import os
import sys

def make_header(out):
    out.write('\\begin{table*}\n')
    out.write('\\centering\n')
    out.write('\\caption{\\TableCaption{}}\n')
    out.write('\\label{table:tab}\n')
    out.write('\\begin{tabular}{l|r}\n')
    out.write('\\toprule\n')
    out.write('\\textbf{Project} & \multicolumn{1}{c}{\\textbf{\\TableHeader{}}}\\\\\n')
    out.write('\\midrule\n')

def make_footer(out, suffixes):
    out.write('\\midrule\n')
    out.write('Overall')
    for suffix in suffixes:
        out.write(' & \\Use{overall' + suffix + '}')
    out.write('\\\\\n')
    out.write('\\bottomrule\n')
    out.write('\\end{tabular}\n')
    out.write('\\end{table*}\n')

def main(args):
    projlist_file = args[1] # File with list of project names
    out_file = args[2]      # File to write table contents into

    with open(out_file, 'w') as out:
        make_header(out)
        with open(projlist_file) as f:
            for line in f:
                proj = line.strip()
                out.write('\\Use{' + proj + '_name}')
                for suffix in ['_result_num']:
                    out.write(' & ' + '\\Use{' + proj + suffix + '}')
                out.write('\\\\\n')
        make_footer(out, ['_result_num'])


if __name__ == '__main__':
    main(sys.argv)
