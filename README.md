# Setup

1) Setup [pyenv](http://github.com/pyenv/pyenv)

```
    pyenv virtualenv 3.5.6 jupyter
    pyenv activate jupyter
    pip install fbprophet seaborn jupyter
```

## Preparing data

There's a python program included that will download data from noaa for you.  The numbers come from isd-history.txt.  The program will attempt to download every year in the data set.  If NOAA is missing a year inside the data set, it will break, and many sets are missing a year.  This tool is intended as an example, not as a robust downloader for NOAA data.  The tool will then:

* download all the data into a folder with the numbers in the name
* pull out the datetime of the observation and the temperature (in Celcius)
* filter out bad data (+9999 for the temperature is documented in the NOAA docs as a bad observation)
* turn it into a csv and compress it in the root folder.

```
    pyenv activate jupyter
    
    # Will download data for DIA from 1994 - 2019
    ./data_download.py 725650 03017
    jupyter-notebook isd-predictions.ipynb
```

## Docs

To read more about Prophet, check out Prophet's [docs](facebook.github.io/prophet/docs/quick_start.html).
