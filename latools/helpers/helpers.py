"""
Helper functions used by multiple parts of LAtools.
"""
import os
import shutil
import re
import configparser
import datetime as dt
import numpy as np
import dateutil as du
import pkg_resources as pkgrs
import uncertainties.unumpy as un
import scipy.interpolate as interp
from .stat_fns import nominal_values
from functools import wraps

# Bunch modifies dict to allow item access using dot (.) operator
class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self


# warnings monkeypatch
# https://stackoverflow.com/questions/2187269/python-print-only-the-message-on-warnings
def _warning(message, category=UserWarning,
             filename='', lineno=-1,
             file=None, line=None):
    print(message)

# Logging Functions
def _log(func):
    """
    Function for logging method calls and parameters
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        a = func(self, *args, **kwargs)
        self.log.append(func.__name__ + ' :: args={} kwargs={}'.format(args, kwargs))
        return a
    return wrapper

def get_date(datetime, time_format=None):
    """
    Return a datetime oject from a string, with optional time format.

    Parameters
    ----------
    datetime : str
        Date-time as string in any sensible format.
    time_format : datetime str (optional)
        String describing the datetime format. If missing uses
        dateutil.parser to guess time format.
    """
    if time_format is None:
        t = du.parser.parse(datetime)
    else:
        t = dt.datetime.strftime(datetime, time_format)
    return t


def unitpicker(a, llim=0.1, denominator=None, focus_stage=None):
    """
    Determines the most appropriate plotting unit for data.

    Parameters
    ----------
    a : float or array-like
        number to optimise. If array like, the 25% quantile is optimised.
    llim : float
        minimum allowable value in scaled data.

    Returns
    -------
    (float, str)
        (multiplier, unit)
    """

    if not isinstance(a, (int, float)):
        a = nominal_values(a)
        a = np.percentile(a[~np.isnan(a)], 25)

    if denominator is not None:
        pd = pretty_element(denominator)
    else:
        pd = ''

    if focus_stage == 'calibrated':
        udict = {0: 'mol/mol ' + pd,
                 1: 'mmol/mol ' + pd,
                 2: '$\mu$mol/mol ' + pd,
                 3: 'nmol/mol ' + pd,
                 4: 'pmol/mol ' + pd,
                 5: 'fmol/mol ' + pd}
    elif focus_stage == 'ratios':
        udict = {0: 'counts/count ' + pd,
                 1: '$10^{-3}$ counts/count ' + pd,
                 2: '$10^{-6}$ counts/count ' + pd,
                 3: '$10^{-9}$ counts/count ' + pd,
                 4: '$10^{-12}$ counts/count ' + pd,
                 5: '$10^{-15}$ counts/count ' + pd}
    elif focus_stage in ('rawdata', 'despiked', 'bkgsub'):
        udict = udict = {0: 'counts',
                         1: '$10^{-3}$ counts',
                         2: '$10^{-6}$ counts',
                         3: '$10^{-9}$ counts',
                         4: '$10^{-12}$ counts',
                         5: '$10^{-15}$ counts'}
    else:
        udict = {0: '', 1: '', 2: '', 3: '', 4: '', 5: ''}

    a = abs(a)
    n = 0
    if a < llim:
        while a < llim:
            a *= 1000
            n += 1
    return float(1000**n), udict[n]


def pretty_element(s):
    """
    Returns formatted element name.

    Parameters
    ----------
    s : str
        of format [A-Z][a-z]?[0-9]+

    Returns
    -------
    str
        LaTeX formatted string with superscript numbers.
    """
    el = re.match('.*?([A-z]{1,3}).*?', s).groups()[0]
    m = re.match('.*?([0-9]{1,3}).*?', s).groups()[0]

#     g = re.match('([A-Z][a-z]?)([0-9]+)', s).groups()
    return '$^{' + m + '}$' + el


def collate_data(in_dir, extension='.csv', out_dir=None):
    """
    Copy all csvs in nested directroy to single directory.

    Function to copy all csvs from a directory, and place
    them in a new directory.

    Parameters
    ----------
    in_dir : str
        Input directory containing csv files in subfolders
    extension : str
        The extension that identifies your data files.
        Defaults to '.csv'.
    out_dir : str
        Destination directory

    Returns
    -------
    None
    """
    if out_dir is None:
        out_dir = './' + re.search('^\.(.*)', extension).groups(0)[0]

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    for p, d, fs in os.walk(in_dir):
        for f in fs:
            if extension in f:
                shutil.copy(p + '/' + f, out_dir + '/' + f)
    return


def bool_2_indices(a):
    """
    Convert boolean array into a 2D array of (start, stop) pairs.
    """
    if any(a):
        lims = []
        lims.append(np.where(a[:-1] != a[1:])[0])

        if a[0]:
            lims.append([0])
        if a[-1]:
            lims.append([len(a) - 1])
        lims = np.concatenate(lims)
        lims.sort()

        return np.reshape(lims, (lims.size // 2, 2))
    else:
        return None



# def bool_2_indices(a):
#     if any(a):
#         lims = []
#         d = np.where(a)[0]  # find indices of True
#         lims.append([d[0]])  # add first
#         lims.append([d[-1]])  # add last
#         wnc = np.where(np.diff(d) != 1)[0]  # find where indices are non consecutive
#         if len(wnc) > 0:
#             lims.append(d[wnc] + 1)  # add last consecutive + 1
#             lims.append(d[(wnc + 1)])  # add first consecutive
#         lims = np.concatenate(lims)  # combine lims and sort
#         lims.sort()  # sort output
#         return np.reshape(lims, (lims.size // 2, 2))
#     else:
#         return None

# def bool_2_indices(bool_array):
#     """
#     Get list of limit tuples from boolean array.

#     Parameters
#     ----------
#     bool_array : array_like
#         boolean array

#     Returns
#     -------
#     array_like
#         [2, n] array of (start, end) values describing True parts
#         of bool_array
#     """
#     if ~isinstance(bool_array, np.ndarray):
#         bool_array = np.array(bool_array)

#     lims = np.arange(bool_array.size)[bool_array ^ np.roll(bool_array, 1)]
#     if len(lims) > 0:
#         if bool_array[0]:
#             lims = np.concatenate([[0], lims])
#         if bool_array[-1]:
#             lims = np.concatenate([lims, [bool_array.size - 1]])
#         return np.reshape(lims, (len(lims) // 2, 2))
#     else:
#         return [[np.nan, np.nan]]

    # if ~isinstance(bool_array, np.ndarray):
    #     bool_array = np.array(bool_array)
    # # if bool_array[-1]:
    # #     bool_array[-1] = False
    # lims = np.arange(bool_array.size)[bool_array ^ np.roll(bool_array, 1)]
    # if len(lims) > 0:
    #     # if lims[-1] == bool_array.size - 1:
    #     #     lims[-1] = bool_array.size
    #     return np.reshape(lims, (len(lims) // 2, 2))
    # else:
    #     return [[np.nan, np.nan]]


def enumerate_bool(bool_array, nstart=0):
    """
    Consecutively numbers contiguous booleans in array.

    i.e. a boolean sequence, and resulting numbering
    T F T T T F T F F F T T F
    0-1 1 1 - 2 ---3 3 -

    where ' - '

    Parameters
    ----------
    bool_array : array_like
        Array of booleans.
    nstart : int
        The number of the first boolean group.
    """
    ind = bool_2_indices(bool_array)
    ns = np.full(bool_array.size, nstart, dtype=int)
    for n, lims in enumerate(ind):
        ns[lims[0]:lims[-1] + 1] = nstart + n + 1
    return ns


def tuples_2_bool(tuples, x):
    """
    Generate boolean array from list of limit tuples.

    Parameters
    ----------
    tuples : array_like
        [2, n] array of (start, end) values
    x : array_like
        x scale the tuples are mapped to

    Returns
    -------
    array_like
        boolean array, True where x is between each pair of tuples.
    """
    if np.ndim(tuples) == 1:
        tuples = [tuples]

    out = np.zeros(x.size, dtype=bool)
    for l, u in tuples:
        out[(x > l) & (x < u)] = True
    return out


def config_locator():
    """
    Prints the location of the latools.cfg file.
    """
    print(pkgrs.resource_filename('latools', 'latools.cfg'))
    return


def add_config(config_name, params, config_file=None, make_default=True):
    """
    Adds a new configuration to latools.cfg.

    Parameters
    ----------
    config_name : str
        The name of the new configuration. This should be descriptive
        (e.g. UC Davis Foram Group)
    params : dict
        A (parameter, value) dict defining non - default parameters
        associated with the new configuration.
        Possible parameters include:

        srmfile : str
            Path to srm file used in calibration. Defaults to GeoRem
            values for NIST610, NIST612 and NIST614 provided with latools.
        dataformat : dict (as str)
            See dataformat documentation.
    config_file : str
        Path to the configuration file that will be modified. Defaults to
        latools.cfg in package install location.
    make_default : bool
        Whether or not to make the new configuration the default
        for future analyses. Default = True.

    Returns
    -------
    None
    """

    if config_file is None:
        config_file = pkgrs.resource_filename('latools', 'latools.cfg')
    cf = configparser.ConfigParser()
    cf.read(config_file)

    # if config doesn't already exist, create it.
    if config_name not in cf.sections():
        cf.add_section(config_name)
    # iterate through parameter dict and set values
    for k, v in params.items():
        cf.set(config_name, k, v)
    # make the parameter set default, if requested
    if make_default:
        cf.set('DEFAULT', 'default_config', config_name)

    cf.write(open(config_file, 'w'))

    return


def intial_configuration():
    """
    Convenience function for configuring latools.

    Run this function when you first use `latools` to specify the
    location of you SRM data file and your data format file.

    See documentation for full details.
    """
    print(('You will be asked a few questions to configure latools\n'
           'for your specific laboratory needs.'))
    lab_name = input('What is the name of your lab? : ')

    params = {}
    OK = False
    while ~OK:
        srmfile = input('Where is your SRM.csv file? [blank = default] : ')
        if srmfile != '':
            if os.path.exists(srmfile):
                params['srmfile'] = srmfile
                OK = True
            else:
                print(("You told us the SRM data file was at: " + srmfile +
                       "\nlatools can't find that file. Please check it "
                       "exists, and \ncheck that the path was correct. "
                       "The file path must be complete, not relative."))
        else:
            print(("No path provided. Using default GeoRem values for "
                   "NIST610, NIST612 and NIST614."))
            OK = True

        OK = False

    while ~OK:
        dataformatfile = input(('Where is your dataformat.dict file? '
                                '[blank = default] : '))
        if dataformatfile != '':
            if os.path.exists(dataformatfile):
                params['srmfile'] = dataformatfile
                OK = True
            else:
                print(("You told us the dataformat file was at: " +
                       dataformatfile + "\nlatools can't find that file. "
                       "Please check it exists, and \ncheck that the path "
                       "was correct. The file path must be complete, not "
                       "relative."))
        else:
            print(("No path provided. Using default dataformat "
                   "for the UC Davis Agilent 7700."))
            OK = True

    make_default = input(('Do you want to use these files as your '
                          'default? [Y/n] : ')).lower() != 'n'

    add_config(lab_name, params, make_default=make_default)

    print("\nConfiguration set. You're good to go!")

    return


def get_example_data(destination_dir):
    if os.path.isdir(destination_dir):
        overwrite = input(destination_dir +
                          ' already exists. Overwrite? [N/y]: ').lower() == 'y'
        if overwrite:
            shutil.rmtree(destination_dir)
        else:
            print(destination_dir + ' was not overwritten.')

    shutil.copytree(pkgrs.resource_filename('latools', 'resources/test_data'),
                    destination_dir)

    return


# for plotting
# def rangecalc(xs, ys, pad=0.05):
#     xd = max(xs)
#     yd = max(ys)
#     return ([0 - pad * xd, max(xs) + pad * xd],
#             [0 - pad * yd, max(ys) + pad * yd])

def rangecalc(xs, pad=0.05):
    mn = np.nanmin(xs)
    mx = np.nanmax(xs)
    xr = mx - mn
    return [mn - pad * xr, mx + pad * xr]


class un_interp1d(object):
    """
    object for handling interpolation of values with uncertainties.
    """

    def __init__(self, x, y, **kwargs):
        self.nom_interp = interp.interp1d(un.nominal_values(x),
                                          un.nominal_values(y), **kwargs)
        self.std_interp = interp.interp1d(un.nominal_values(x),
                                          un.std_devs(y), **kwargs)

    def new(self, xn):
        yn = self.nom_interp(xn)
        yn_err = self.std_interp(xn)
        return un.uarray(yn, yn_err)

    def new_nom(self, xn):
        return self.nom_interp(xn)

    def new_std(self, xn):
        return self.std_interp(xn)


def rolling_window(a, window, pad=None):
    """
    Returns (win, len(a)) rolling - window array of data.

    Parameters
    ----------
    a : array_like
        Array to calculate the rolling window of
    window : int
        Description of `window`.
    pad : same as dtype(a)
        Description of `pad`.

    Returns
    -------
    array_like
        An array of shape (n, window), where n is either len(a) - window
        if pad is None, or len(a) if pad is not None.
    """
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1], )
    out = np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    # pad shape
    if window % 2 == 0:
        npre = window // 2 - 1
        npost = window // 2
    else:
        npre = npost = window // 2
    if isinstance(pad, str):
        if pad == 'ends':
            prepad = np.full((npre, window), a[0])
            postpad = np.full((npost, window), a[-1])
        elif pad == 'mean_ends':
            prepad = np.full((npre, window), np.mean(a[:(window // 2)]))
            postpad = np.full((npost, window), np.mean(a[-(window // 2):]))
        elif pad == 'repeat_ends':
            prepad = np.full((npre, window), out[0])
            postpad = np.full((npost, window), out[0])
        else:
            raise ValueError("If pad is a string, it must be either 'ends', 'mean_ends' or 'repeat_ends'.")

        return np.concatenate((prepad, out, postpad))
    elif pad is not None:
        pre_blankpad = np.empty(((npre, window)))
        pre_blankpad[:] = pad
        post_blankpad = np.empty(((npost, window)))
        post_blankpad[:] = pad
        return np.concatenate([pre_blankpad, out, post_blankpad])
    else:
        return out


def fastsmooth(a, win=11):
    """
    Returns rolling - window smooth of a.

    Function to efficiently calculate the rolling mean of a numpy
    array using 'stride_tricks' to split up a 1D array into an ndarray of
    sub - sections of the original array, of dimensions [len(a) - win, win].

    Parameters
    ----------
    a : array_like
        The 1D array to calculate the rolling gradient of.
    win : int
        The width of the rolling window.

    Returns
    -------
    array_like
        Gradient of a, assuming as constant integer x - scale.
    """
    # check to see if 'window' is odd (even does not work)
    if win % 2 == 0:
        win += 1  # add 1 to window if it is even.
    kernel = np.ones(win) / win
    npad = int((win - 1) / 2)
    spad = np.full(npad + 1, np.mean(a[:(npad + 1)]))
    epad = np.full(npad - 1, np.mean(a[-(npad - 1):]))
    return np.concatenate([spad, np.convolve(a, kernel, 'valid'), epad])

    # # check to see if 'window' is odd (even does not work)
    # if win % 2 == 0:
    #     win -= 1  # subtract 1 from window if it is even.
    # # trick for efficient 'rolling' computation in numpy
    # # shape = a.shape[:-1] + (a.shape[-1] - win + 1, win)
    # # strides = a.strides + (a.strides[-1], )
    # # wins = np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    # wins = rolling_window(a, win)
    # # apply rolling gradient to data
    # a = map(np.nanmean, wins)

    # return np.concatenate([np.zeros(int(win / 2)), list(a),
    #                        np.zeros(int(win / 2))])


def fastgrad(a, win=11):
    """
    Returns rolling - window gradient of a.

    Function to efficiently calculate the rolling gradient of a numpy
    array using 'stride_tricks' to split up a 1D array into an ndarray of
    sub - sections of the original array, of dimensions [len(a) - win, win].

    Parameters
    ----------
    a : array_like
        The 1D array to calculate the rolling gradient of.
    win : int
        The width of the rolling window.

    Returns
    -------
    array_like
        Gradient of a, assuming as constant integer x - scale.
    """
    # check to see if 'window' is odd (even does not work)
    if win % 2 == 0:
        win += 1  # subtract 1 from window if it is even.
    # trick for efficient 'rolling' computation in numpy
    # shape = a.shape[:-1] + (a.shape[-1] - win + 1, win)
    # strides = a.strides + (a.strides[-1], )
    # wins = np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    wins = rolling_window(a, win, 'ends')
    # apply rolling gradient to data
    a = map(lambda x: np.polyfit(np.arange(win), x, 1)[0], wins)

    return np.array(list(a))
    # return np.concatenate([np.zeros(int(win / 2)), list(a),
    #                        np.zeros(int(win / 2))])


def calc_grads(x, dat, keys=None, win=5):
    """
    Calculate gradients of values in dat.
    
    Parameters
    ----------
    x : array like
        Independent variable for items in dat.
    dat : dict
        {key: dependent_variable} pairs
    keys : str or array-like
        Which keys in dict to calculate the gradient of.
    win : int
        The side of the rolling window for gradient calculation

    Returns
    -------
    dict of gradients
    """
    if keys is None:
        keys = dat.keys()

    def grad(xy):
        if (~np.isnan(xy)).all():
            try:
                return np.polyfit(xy[0], xy[1], 1)[0]
            except ValueError:
                return np.nan
        else:
            return np.nan

    xs = rolling_window(x, win, pad='repeat_ends')
    grads = Bunch()
    for k in keys:
        d = nominal_values(rolling_window(dat[k], win, pad='repeat_ends'))

        grads[k] = np.array(list(map(grad, zip(xs, d))))

    return grads


def findmins(x, y):
    """ Function to find local minima.

    Parameters
    ----------
    x, y : array_like
        1D arrays of the independent (x) and dependent (y) variables.

    Returns
    -------
    array_like
        Array of points in x where y has a local minimum.
    """
    return x[np.r_[False, y[1:] < y[:-1]] & np.r_[y[:-1] < y[1:], False]]


# def gaus_deriv(x, *p):
#     A, mu, sigma = p
#     return A * ((np.exp((-(x - mu)**2)/(2*sigma**2)) * (x - mu)) /
#                 (np.sqrt(2 * np.pi) * sigma**3))


def stack_keys(ddict, keys, extra=None):
    """
    Combine elements of ddict into an array of shape (len(ddict[key]), len(keys)).

    Useful for preparing data for sklearn.

    Parameters
    ----------
    ddict : dict
        A dict containing arrays or lists to be stacked.
        Must be of equal length.
    keys : list or str
        The keys of dict to stack. Must be present in ddict.
    extra : list (optional)
        A list of additional arrays to stack. Elements of extra
        must be the same length as arrays in ddict.
        Extras are inserted as the first columns of output.
    """
    if isinstance(keys, str):
        d = [ddict[keys]]
    else:
        d = [ddict[k] for k in keys]
    if extra is not None:
        d = extra + d
    return np.vstack(d).T