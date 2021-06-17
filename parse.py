#!/usr/bin/env python3

""" Module Description """

import logging

from xmltotabular import XmlCollectionToTabular

XML_INPUT = "badges.xml"
CONFIG = "config.yaml"
OUTPUT_PATH = "output.sqlite"


def main():
    """ Command-line entry-point. """

    collectionTransformer = XmlCollectionToTabular(
        XML_INPUT, CONFIG, OUTPUT_PATH, output_type="sqlite", log_level=logging.DEBUG
    )
    collectionTransformer.convert()


if __name__ == "__main__":
    main()
