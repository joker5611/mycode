#!/usr/bin/env python3

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    zfile = open("galaxyguide.yaml", "w")

    ## use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
    ## unlike JSON, the YAML lib uses .dump() to create YAML strings and write to files
    ## the JSON lib uses .dump() to create a string and .dumps() to write to files
    yaml.dump(hitchhikers, zfile)

    ## close the file when we are done
    zfile.close()

main()
