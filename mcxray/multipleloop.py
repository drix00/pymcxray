#!/usr/bin/env python
"""
This module provides a tool for handling computer experiments with
of a set of input parameters, where each input parameter
is varied in a prescribed fashion.

In short, the parameters are held in a dictionary where the keys are
the names of the parameters and the values are the numerical, string
or other values of the parameters.  The value can take on multiple
values: e.g., an integer parameter 'a' can have values -1, 1 and
10. Similarly, a string parameter 'method' can have values 'Newton'
and 'Bisection'. The module will generate all combination of all
parameters and values, which in the mentioned example will be
(-1, 'Newton'), (1, 'Newton'), (10, 'Newton'), (-1, 'Bisection'),
(1, 'Bisection'), and (10, 'Bisection'). Particular combination
of values can easily be removed.

The usage and implementation of the module are documented in the
book "Python Scripting for Computational Science" (H. P. Langtangen,
Springer, 2009), Chapter 12.1.
"""
# see also http://pyslice.sourceforge.net/HomePage

def _outer(a, b):
    """
    Return the outer product/combination of two lists.
    a is a multi- or one-dimensional list,
    b is a one-dimensional list, tuple, NumPy array or scalar (new parameter)
    Return:  outer combination 'all_combination'.

    The function is to be called repeatedly::

        all = _outer(all, p)
    """
    all_combination = []
    if not isinstance(a, list):
        raise TypeError('a must be a list')
    if isinstance(b, (float,int,complex,str)):  b = [b]  # scalar?

    if len(a) == 0:
        # first call:
        for j in b:
            all_combination.append([j])
    else:
        for j in b:
            for i in a:
                if not isinstance(i, list):
                    raise TypeError('a must be list of list')
                # note: i refers to a list; i.append(j) changes
                # the underlying list (in a), which is not what
                # we want, we need a copy, extend the copy, and
                # add to all_combination
                k = i + [j]  # extend previous prms with new one
                all_combination.append(k)
    return all_combination

def combine(prm_values):
    """
    Compute the combination of all parameter values in the prm_values
    (nested) list. Main function in this module.

    param prm_values: nested list ``(parameter_name, list_of_parameter_values)``
    or dictionary ``prm_values[parameter_name] = list_of_parameter_values``.
    return: (all, names, varied) where

      - all contains all combinations (experiments)
        all[i] is the list of individual parameter values in
        experiment no i

      - names contains a list of all parameter names

      - varied holds a list of parameter names that are varied
        (i.e. where there is more than one value of the parameter,
        the rest of the parameters have fixed values)


    Code example:

    >>> dx = array([1.0/2**k for k in range(2,5)])
    >>> dt = 3*dx;  dt = dt[:-1]
    >>> p = {'dx': dx, 'dt': dt}
    >>> p
    {'dt': [ 0.75 , 0.375,], 'dx': [ 0.25  , 0.125 , 0.0625,]}
    >>> all, names, varied = combine(p)
    >>> all
    [[0.75, 0.25], [0.375, 0.25], [0.75, 0.125], [0.375, 0.125],
     [0.75, 0.0625], [0.375, 0.0625]]
    """
    if isinstance(prm_values, dict):
        # turn dict into list [(name,values),(name,values),...]:
        prm_values = [(name, prm_values[name]) \
                      for name in prm_values]
    all_combination = []
    varied = []
    for name, values in prm_values:
        all_combination = _outer(all_combination, values)
        if isinstance(values, list) and len(values) > 1:
            varied.append(name)
    names = [name for name, values in prm_values]
    return all_combination, names, varied
