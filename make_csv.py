#!/bin/env python

import optparse

chains = ['W','X','Y','Z']


def get_energies(fasc_file):
     output = {}
     first = True
     with open(fasc_file) as fin:
        lines = [line.split() for line in fin]
     fin.close()
     for line in lines:
        if first:
         first = False
         continue
#        print len(line)
#        print line
        for i in range(0,len(line),2):
            output[line[i].strip(':')] = line[i+1]
#     print output
     return output

def write_csv_line(fasc_dict,fout):
    print fasc_dict
    for key in sorted(fasc_dict.keys()):
        fout.write(fasc_dict[key])
        fout.write(',')
    fout.write('\n')

def main():
    parser = optparse.OptionParser()
    parser.add_option('-o',dest='output',metavar="output.csv",help='CSV file to be output')
    parser.add_option('-f',dest='input',metavar='FILE.fasc',help='List of fasc files to put in csv file', action='append')

    (options,args) = parser.parse_args()
    master_dict = {}
    for fasc_file in options.input:
        master_dict[fasc_file] = get_energies(fasc_file)
    output = open(options.output,'w+')
    output.write("file,")
    first = True
    for key in sorted(master_dict.keys()):
        if first:
           output.write(','.join(sorted(master_dict[key].keys())))
           output.write('\n')
           first = False
        output.write(key)
        output.write(',')
        write_csv_line(master_dict[key],output)
    output.close()

if __name__ == '__main__':
    main()            
            
