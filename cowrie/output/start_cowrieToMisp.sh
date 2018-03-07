pushd PyMISPWrapper/
. ./wrapenv/bin/activate
python3 RedisToMISP.py -k cowrie --eventname cowrie_daily_log_entry
