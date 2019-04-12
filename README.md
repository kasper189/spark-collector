# Spark Collector

[![Build Status](https://travis-ci.com/kasper189/spark-collector.svg?branch=master)](https://travis-ci.com/kasper189/spark-collector)

The aim of this library is to extract metrics of a Spark application given its applicationId retrieving them from 
the Spark History Server. The metrics are displayed as HTML table.

## Features
For a given application id, the collector extracts all the stages, and for the last stage-attempt, it retrieves:
- status
- cpu time
- input bytes
- to be enriched

## Prerequisites
The project is written in Python
1. Install [pyenv](https://github.com/pyenv/pyenv) to be able to switch between different Python version
2. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage virtualenvs.

## Dependencies
```bash
pip install -f requirements.txt
```

## How to run
```bash
python manager.py -s <server_ip_address> -p <port> -a <application_id>
```

## How to run test
Under costruction, sorry


## Output
For the moment the output is generated on stdout as html.

<table border="1">
<tr><td>id</td><td>attempt</td><td>status</td><td>cpu_time</td><td>input_bytes</td></tr>
<tr><td>0</td><td>0</td><td>COMPLETE</td><td>589278186</td><td>9105057</td></tr>
<tr><td>1</td><td>0</td><td>COMPLETE</td><td>556727480</td><td>30852</td></tr>
<tr><td>2</td><td>0</td><td>COMPLETE</td><td>486545228</td><td>38537</td></tr>
<tr><td>3</td><td>0</td><td>COMPLETE</td><td>484766392</td><td>291162</td></tr>
<tr><td>4</td><td>0</td><td>COMPLETE</td><td>562510365</td><td>153020055</td></tr>
<tr><td>5</td><td>0</td><td>COMPLETE</td><td>51979578678014</td><td>38087314863</td></tr>
<tr><td>6</td><td>0</td><td>COMPLETE</td><td>10186052645985</td><td>0</td></tr>
</table>


## Contribution
Please to do not hesitate to contribute by adding features (and tests).
