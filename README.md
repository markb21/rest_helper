# Rest helper

This parser allows you to parse config files to create API calls.
It expects two arguments i.e. number of API requests to output and input config file.

##Usage
### In CLI
Run the script rest_helper.py with 2 mandatory options:
 <ul>
 <li>
 <b>-n</b> (--num) for the number of parsed API requests
 </li>
 <li> 
 <b>-c</b> (--config) for setting input config file
 </li>
 </ul>
 
### As python package
Build the package by running this command

``
pip install .
``

and import it into your project

``
from rest_helper import parse_config_file
`` 
