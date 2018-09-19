# coding: utf-8
"""Purpose: pull historical wind and wave data for user-determined lon / lat position

Creation Date: 16 Sep 2018

Author(s): backeb <backeb@gmail.com> Bjorn Backeberg

Dependencies: python 2.7, xarray, pynio*, numpy

      * xarray/pynio engine requires python 2.7 environment.
        to install pynio do the following:
            `conda create -n pynioEnv python=2.7 anaconda`
            `source activate pynioEnv`
            `conda install numpy pandas jupyter basemap xarray netcdf4 dask`
            `conda install -c ncar pynio`

Change Log: <Date: Author - Comment>
    16 Sep 2018: backeb - add get_ww3_rean function
    __ TODO ___: need to find reanalysis / forecasts archive for 2009-present 
"""

def get_ww3_rean(lonIn, latIn):
    """ Function to get historical wave data for input lon/lat from WAVEWATCH III 30-year Hindcast Phase 2
        See http://polar.ncep.noaa.gov/waves/hindcasts/nopp-phase2.php for more info
        Note only data from 1979-2009 available
    """
    import numpy as np

    url = "ftp://polar.ncep.noaa.gov/pub/history/nopp-phase2/{yyyy}{mm}/gribs/multi_reanal.glo_30m_ext.{var}.{yyyy}{mm}.grb2"

    yrs = np.arange(1979, 2010, 1)
    mnths = np.arange(1, 13, 1)
    var_list = ["hs", "tp", "dp", "wind"]

    url_updt = url.format(var = var_list[0], yyyy = str(yrs[0]), mm = str("%02d" % mnths[0]))

    
