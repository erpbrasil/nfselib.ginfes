========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |appveyor|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.org/erpbrasil/nfselib.ginfes.svg?branch=master_gen
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/erpbrasil/nfselib.ginfes

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/erpbrasil/nfselib.ginfes?branch=master_gen&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/mileo/nfselib-ginfes

.. |version| image:: https://img.shields.io/pypi/v/nfselib.ginfes.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/nfselib.ginfes

.. |wheel| image:: https://img.shields.io/pypi/wheel/nfselib.ginfes.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/nfselib.ginfes

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nfselib.ginfes.svg
    :alt: Supported versions
    :target: https://pypi.org/project/nfselib.ginfes

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nfselib.ginfes.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/nfselib.ginfes

.. |commits-since| image:: https://img.shields.io/github/commits-since/erpbrasil/nfselib.ginfes/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/erpbrasil/nfselib.ginfes/compare/v0.1.0...master

.. end-badges

Python Library to genereate GINFES NFS-E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Biblioteca Python para ler e gerar NFSe's / XML para o webservice GINFES;

* Esta biblioteca faz parte do projeto: https://erpbrasil.github.io/
* Para transmitir aconselhamos a biblioteca Python Zeep, ou então por exemplo https://github.com/erpbrasil/erpbrasil.edoc.
* Ela foi gerada automaticamente através do generateDS e da ferramenta https://github.com/erpbrasil/erpbrasil.edoc.gen
* Verificar o conteúdo da pasta *script* e o manual do processo de relase em https://erpbrasil.github.io/docs/

A bibliotca permite de:

* Gerar os XMLs dos documentos fiscais;
* Validar os dados com **as mesmas validações dos XSD's ao montar os objetos**, o que evita detectar os erros apenas ao transmitir o XML;
* Importar XMLs e transforma-los em objetos Python. Usando um sistema de sub-classes, fica fácil mapear esses objetos em outros objetos ou adicionar qualquer método customizado;

A biblioteca é:

* **Simples e confiável**. O código é gerado pelo generateDS a partir dos XSD's do GINFES. Ele **reflete exatamente a especificação fiscal** da versão do esquema escolhida sem que você deva se perguntar qual é o grau de aderência do código;
* Compatível com **Python 3** (e com Python 2 se botar patches no generateDS e usar uma versao anterior);
* Capaz de carregar **várias versões dos esquemas**. Isso pode ser bem útil ao receber um documento fiscal com um leiaute antigo.

Além disso, usando outros recursos do GenerateDS, é possível ir além dessa biblioteca e gerar automaticamente o modelo de dados do ERP.

Pelo menos no ERP Odoo que tem um framework bastante poderoso. Sendo assim, é possivel montar dinamicamente as telas do usuário, a geração do XML ou a importação do XML quase que sem escrever código (apenas relacionar os campos mapeados com os campos já existentes do ERP).

Fica então bem mais razoável para manter quando tem que atualizar os esquemas e assim também fica finalmente possível manter os dados do SPED dentro do ERP com um custo de manutenção compatível com o modelo open source.

Você pode aprender mais sobre o generateDS `aqui <http://www.davekuhlman.org/generateDS.html>`__ e sobre o conjunto de tecnologias que estamos utilizando para facilitar o desenvolvimento de ERPs no Brasil: https://erpbrasil.github.io/docs/


Instalação
==========

::

    pip install nfselib.ginfes

You can also install the in-development version with::

    pip install https://github.com/erpbrasil/nfselib.ginfes/archive/master_gen.zip


Branchs
=======

* master - Script de geração e outros arquivos importantes (Customizações, Testes e Readme);
* master_gen - Versão final da bibliotaca para uso;

Documentação
============

https://erpbrasil.github.io/

Créditos
========

Esta é uma biblioteca criada atravês do esforço de das empresas:

* Akretion https://akretion.com/pt-BR/
* KMEE https://www.kmee.com.br

Licença
~~~~~~~

* Free software: MIT license

Desenvolvimento
===============

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
