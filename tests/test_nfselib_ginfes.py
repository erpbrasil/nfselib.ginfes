# -*- coding: utf-8 -*-
# Copyright (C) 2020 - KMEE

import os
import sys
from os import path
from xmldiff import main
from lxml import etree as etree_
sys.path.append(path.join(path.dirname(__file__), '..', 'nfselib'))
from nfselib.ginfes.v3_01 import (
    servico_enviar_lote_rps_envio,
    servico_consultar_nfse_rps_envio,
)


def parsexml_(infile, parser=None, keep_signature=False, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    root = doc.getroot()
    # remove Signature element before XML comparison
    if not keep_signature:
        for child in root:
            if child.tag in ["{http://www.w3.org/2000/09/xmldsig#}Signature",
                             "{http://www.w3.org/2000/09/xmldsig#}\
                             ds:Signature"]:
                root.remove(child)
    subtree = etree_.ElementTree(root)
    return subtree

def parse(inFilename, supermod):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = supermod.get_root_tag(rootNode)
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    return rootObj

def execute_test(path, servico):
    for filename in os.listdir(path):
        subtree = parsexml_('%s/%s' % (path, filename,))
        inputfile = 'input.xml'
        subtree.write(inputfile, encoding='utf-8')

        obj = parse(inputfile, servico)

        outputfile = 'output.xml'
        with open(outputfile, 'w') as f:
            obj.export(f, 0, namespaceprefix_='')

        diff = main.diff_files(inputfile, outputfile)
        print(diff)
        assert len(diff) == 0

def test_enviar_lote_rps_envio():
    xml_path = 'tests/nfse/ginfes/enviar_lote_rps_envio'
    execute_test(xml_path, servico_enviar_lote_rps_envio)

def test_consultar_nfse_rps_envio():
    xml_path = 'tests/nfse/ginfes/consultar_nfse_rps_envio'
    execute_test(xml_path, servico_consultar_nfse_rps_envio)
