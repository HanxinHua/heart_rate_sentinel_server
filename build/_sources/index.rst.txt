.. heart_rate_sentinel_server documentation master file, created by
   sphinx-quickstart on Fri Nov 16 15:35:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to heart_rate_sentinel_server's documentation!
======================================================
*Steven  Hua*

*hh177@duke.edu*


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



Execution module
---------------------
.. module:: server
    :platform: Unix, Windows

.. autofunction:: status
.. autofunction:: get_heart_rate
.. autofunction:: get_interval_average
.. autofunction:: new_patient
.. autofunction:: post_heart_rate
.. autofunction:: post_interval_average


Calculation module
---------------------
.. module:: average
    :platform: Unix, Windows

.. autofunction:: calculate_average

.. module:: is_tachycardia
    :platform: Unix, Windows

.. autofunction:: is_tachycardia


Validation module
---------------------
.. module:: validate
    :platform: Unix, Windows

.. autofunction:: validate_add_patient
.. autofunction:: validate_heart_rate_request
.. autofunction:: validate_interval_average_request
.. autofunction:: validate_email
.. autofunction:: str_to_datetime
.. autofunction:: validate_time
