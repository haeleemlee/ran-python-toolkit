# ran-python-toolkit

A small Python toolkit that extracts KPIs (MCS, BLER, TPUT, SINR) from RAN DU logs and aggregates/visualizes them.

---------
Structure
---------
log_parser.py   --- Regex-based log parsing (parse_all, find_prach_anomaly_all)

analyzer.py     --- Builds a pandas DataFrame and aggregates KPIs (build_dataframe)

plotter.py      --- Plots SINR-BLER curves by MCS (plot_bler_curve)

--------
Usage
--------
pip install pandas matplotlib openpyxl

python3 analyzer.py    --- KPI summary, PASS/FAIL evaluation, CSV/Excel export

python3 plotter.py     --- Generates the SINR-BLER curve PNG


By default, each script looks for a logs/ folder relative to its own location. A different path can also be passed via the logdir argument.

-------------
Sample Output
-------------
SINR-BLER curve by MCS (against a 10$ BLER target)

The image file bler_curve.png is in the files.

------------
Testing
------------
pip install pytest pytest-html

python3 -m pytest -v                       # run all tests

python3 -m pytest -v -m "not slow"         # skip slow tests

python3 -m pytest --junitxml=results.xml   #CI-friendly report

------------
Requirements
------------
Python 3.9+

pandas, matplotlib, openpyxl

pytest, pytest-html (for testing)
