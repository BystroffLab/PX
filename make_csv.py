#!/bin/env python
"""
Convert fasc file to a csv
"""

import optparse

chains = ['W','X','Y','Z']


def get_energies(fasc_file):
    '''Convert the fasc file into a dictionary where each key is the score type
    and the value is the score'''
     output = {}
     first = True
     # read the lines from the fasc file
     with open(fasc_file) as fin:
        lines = [line.split() for line in fin]
     fin.close()
     for line in lines:
        # skip the first line
        if first:
            first = False
            continue
        # read energies into dictionary
        for i in range(0,len(line),2):
            output[line[i].strip(':')] = line[i+1]
     return output

def write_csv_line(fasc_dict,fout):
    '''write each line of the new csv file'''
    for key in sorted(fasc_dict.keys()):
        fout.write(fasc_dict[key])
        fout.write(',')
    fout.write('\n')

def main():
    parser = optparse.OptionParser()
    # output csv file
    parser.add_option('-o',dest='output',metavar="output.csv",help='CSV file to be output')
    # input fasc files
    parser.add_option('-f',dest='input',metavar='FILE.fasc',help='List of fasc files to put in csv file', action='append')

    # parse the arguments
    (options,args) = parser.parse_args()
    # initialize dictionary
    master_dict = {}
    # get energies for each file
    for fasc_file in options.input:
        master_dict[fasc_file] = get_energies(fasc_file)
    # open output file
    output = open(options.output,'w+')
    # write the header row
    output.write("file,")
    first = True
    for key in sorted(master_dict.keys()):
        if first:
           output.write(','.join(sorted(master_dict[key].keys())))
           output.write('\n')
           first = False
        # write each row of the csv file given each input fasc file
        output.write(key)
        output.write(',')
        write_csv_line(master_dict[key],output)
    output.close()

if __name__ == '__main__':
    main()            
            
