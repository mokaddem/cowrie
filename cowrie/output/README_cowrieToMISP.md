# cowrie to MISP

## Installation

Start the script ``install_cowrieToMISP.sh``

``$ bash install_cowrieToMISP.sh``

## Usage

When cowrie is running, it will populate a redis list with its log entries. You just have to pop elements from this this list and push them to MISP. This is exactly what the script ``RedisToMISP.py`` is doing.


``$ bash start_cowrieToMISP.sh``

will activate the virtualenv and launch ``RedisToMISP.py`` with default options.
