#!/usr/bin/python

import sys
import getopt
import yaml


def help():
    print '    docker-compose-v2-ports-remover.py -i <inputfile> -o <outputfile>'


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if inputfile == '':
        print "Input file is required"
        help()
        sys.exit(2)
    if outputfile == '':
        print "Output file is required"
        help()
        sys.exit(2)

    print 'Input file is -', inputfile
    print 'Output file is -', outputfile

    docker_compose_objects = yaml.load(open(inputfile, 'r'))

    if 'services' not in docker_compose_objects:
        print "There is no a service in your input file!"
        sys.exit(3)
    services = docker_compose_objects['services']
    for service_name in services:
        service = services[service_name]
        if 'ports' in service:
            del service['ports']

    with open(outputfile, 'w') as outfile:
        outfile.write(yaml.dump(docker_compose_objects, default_flow_style=False, indent=4))


if __name__ == '__main__':
    main(sys.argv[1:])
