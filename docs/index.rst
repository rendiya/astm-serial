.. astm-serial documentation master file, created by
   sphinx-quickstart on Tue Feb 21 16:30:22 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to astm-serial documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

astm client with python for example arduino communication please visit our `github <https://github.com/rendiya/astm-serial/>`_


How to install :

pip install astm-serial

Quickstart

from astm_serial.client import AstmConn

astm = AstmConn(port='/dev/ttyACM0', baudrate=9600)
astm.open_session()
print astm.get_data()
astm.close_session()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
