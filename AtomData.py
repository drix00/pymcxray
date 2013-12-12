#!/usr/bin/env python
"""
.. py:currentmodule:: AtomData
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay atom data.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
SHELL_K = "K"
SHELL_L3 = "L3"
SHELL_M5 = "M5"

_NUMBER_SHELLS = 5
_NUMBER_LINES = 9
_NUMBER_ATOMS = 96

ATOM_SHELL_NAMES = ["Shell K", "Shell L", "Shell M", "Shell N", "Shell O"]

ATOM_LINE_NAMES = ["Line Ka1", "Line Ka2", "Line Kb1", "Line Kb2", "Line La ", "Line Lb1", "Line Lb2", "Line Lg ", "Line Ma "]

ATOM_NAMES = ["Hydrogen",        "Helium",        "Lithium",        "Beryllium",    "Boron",        "Carbon",        "Nitrogen",        "Oxygen",        "Fluorine",        "Neon",
    "Sodium",        "Magnesium",    "Aluminium",    "Silicon",        "Phosphorus",    "Sulfur",        "Chlorine",        "Argon",        "Potassium",    "Calcium",
    "Scandium",        "Titanium",        "Vanadium",        "Chromium",        "Manganese",    "Iron",            "Cobalt",        "Nickel",        "Copper",        "Zinc",
    "Gallium",        "Germanium",    "Arsenic",        "Selenium",        "Bromine",        "Krypton",        "Rubidium",        "Strontium",    "Yttrium",        "Zirconium",
    "Niobium",        "Molybdenum",    "Technetium",    "Ruthenium",    "Rhodium",        "Palladium",    "Silver",        "Cadmium",        "Indium",        "Tin",
    "Antimony",        "Tellurium",    "Iodine",        "Xenon",        "Cesium",        "Barium",        "Lanthanum",    "Cerium",        "Praseodymium",    "Neodymium",
    "Prometheum",    "Samarium",        "Europium",        "Gadolinium",    "Terbium",        "Dysprosium",    "Holmium",        "Erbium",        "Thulium",        "Ytterbium",
    "Lutetium",        "Hafnium",        "Tantalum",        "Tungsten",        "Rhenium",        "Osmium",        "Iridium",        "Platinum",        "Gold",            "Mercury",
    "Thallium",        "Lead",            "Bismuth",        "Polonium",        "Astatine",        "Radon",        "Francium",        "Radium",        "Actinium",        "Thorium",
    "Protactinium",    "Uranium",        "Neptunium",    "Plutonium",    "Americium",    "Curium"]

ATOM_SYMBOLS = ["H",        "He",        "Li",        "Be",        "B",        "C",        "N",        "O",        "F",        "Ne",
    "Na",        "Mg",        "Al",        "Si",        "P",        "S",        "Cl",        "Ar",        "K",        "Ca",
    "Sc",        "Ti",        "V",        "Cr",        "Mn",        "Fe",        "Co",        "Ni",        "Cu",        "Zn",
    "Ga",        "Ge",        "As",        "Se",        "Br",        "Kr",        "Rb",        "Sr",        "Y",        "Zr",
    "Nb",        "Mo",        "Tc",        "Ru",        "Rh",        "Pd",        "Ag",        "Cd",        "In",        "Sn",
    "Sb",        "Te",        "I",        "Xe",        "Cs",        "Ba",        "La",        "Ce",        "Pr",        "Nd",
    "Pm",        "Sm",        "Eu",        "Gd",        "Td",        "Dy",        "Ho",        "Er",        "Tm",        "Yb",
    "Lu",        "Hf",        "Ta",        "W",        "Re",        "Os",        "Ir",        "Pt",        "Au",        "Hg",
    "Tl",        "Pb",        "Bi",        "Po",        "At",        "Rn",        "Fr",        "Ra",        "Ac",        "Th",
    "Pa",        "U",        "Np",        "Pu",        "Am",        "Cm"]

ATOM_WEIGHTS = [1.008,        4.003,        6.940,        9.010,        10.81,        12.01,        14.01,        16.00,        19.00,        20.18,
    22.99,        24.31,        26.98,        28.09,        30.97,        32.06,        35.45,        39.95,        39.10,        40.08,
    44.96,        47.90,        50.94,        52.00,        54.94,        55.85,        58.93,        58.71,        63.55,        65.37,
    69.72,        72.59,        74.92,        78.96,        79.90,        83.80,        85.47,        87.62,        88.91,        91.22,
    92.91,        95.94,        98.91,        101.07,        102.91,        106.4,        107.87,        112.40,        114.82,        118.69,
    121.75,        127.60,        126.90,        131.30,        132.90,        137.34,        138.91,        140.12,        140.91,        144.24,
    145.0,        150.35,        151.96,        157.25,        158.92,        162.50,        164.93,        167.26,        168.93,        173.04,
    174.97,        178.49,        180.95,        183.95,        186.20,        190.20,        192.20,        195.09,        196.97,        200.59,
    204.37,        207.19,        208.98,        209.0,        210.0,        222.0,        223.0,        226.0,        227.0,        232.0,
    231.0,        238.0,        237.0,        244.0,        243.0,        247.0]

# Density in g/cm3.
ATOM_MASS_DENSITY_g_cm3 = [0.071,        0.126,        0.53,        1.85,        2.34,        2.26,        0.81,        1.14,        1.505,        1.2,
    0.97,        1.74,        2.7,        2.33,        1.82,        2.07,        1.56,        1.4,        0.86,        1.55,
    3.0,        4.51,        6.1,        7.19,        7.43,        7.86,        8.9,        8.9,        8.96,        7.14,
    5.91,        5.32,        5.72,        4.79,        3.12,        2.6,        1.53,        2.6,        4.47,        6.49,
    8.4,        10.2,        11.5,        12.2,        12.4,        12.0,        10.5,        8.65,        7.31,        7.3,
    6.62,        6.24,        4.94,        3.06,        1.9,        3.5,        6.17,        6.67,        6.77,        7.0,
    0.0,        7.54,        5.26,        7.89,        8.27,        8.54,        8.8,        9.05,        9.33,        6.98,
    9.84,        13.1,        16.6,        19.3,        21.0,        22.6,        22.5,        21.4,        19.3,        13.6,
    11.85,        11.4,        9.8,        9.2,        0.0,        9.91,        0.0,        5.0,        10.07,        11.7,
    15.4,        18.9,        20.4,        19.8,        13.6,        13.511]

# Ionization energy of K shell in keV.
ATOM_ION_ENERGY_SHELL_K_keV = [0.014,        0.025,        0.055,        0.116,        0.192,        0.283,        0.339,        0.531,        0.687,        0.874,
    1.080,        1.303,        1.559,        1.838,        2.142,        2.470,        2.819,        3.203,        3.607,        4.038,
    4.496,        4.964,        5.463,        5.988,        6.537,        7.111,        7.709,        8.331,        8.980,        9.660,
    10.368,        11.103,        11.863,        12.652,        13.475,        14.323,        15.201,        16.106,        17.037,        17.998,
    18.987,        20.022,        21.054,        22.118,        23.224,        24.347,        25.517,        26.712,        27.928,        29.190,
    30.486,        31.809,        33.164,        34.579,        35.959,        37.410,        38.931,        40.449,        41.998,        43.571,
    45.207,        46.846,        48.515,        50.229,        51.998,        53.789,        55.615,        57.483,        59.335,        61.303,
    63.304,        65.313,        67.400,        69.508,        71.662,        73.860,        76.097,        78.379,        80.713,        83.106,
    85.517,        88.001,        90.521,        93.112,        95.740,        98.418,        101.147,    103.927,    106.759,    109.630,
    112.581,    115.591,    118.619,    121.720,    124.876,    128.088]

# Ionization energy of L3 shell in keV.
ATOM_ION_ENERGY_SHELL_L3_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.022,
    0.034,        0.049,        0.072,        0.098,        0.128,        0.163,        0.202,        0.245,        0.294,        0.349,
    0.406,        0.454,        0.512,        0.574,        0.639,        0.708,        0.779,        0.853,        0.933,        1.022,
    1.117,        1.217,        1.323,        1.434,        1.552,        1.675,        1.806,        1.941,        2.079,        2.220,
    2.374,        2.523,        2.677,        2.837,        3.002,        3.172,        3.352,        3.538,        3.729,        3.928,
    4.132,        4.341,        4.559,        4.782,        5.011,        5.247,        5.489,        5.729,        5.968,        6.215,
    6.466,        6.721,        6.983,        7.252,        7.519,        7.850,        8.074,        8.364,        8.652,        8.943,
    9.241,        9.556,        9.876,        10.198,        10.531,        10.869,        11.211,        11.559,        11.919,        12.285,
    12.657,        13.044,        13.424,        13.817,        14.215,        14.618,        15.028,        15.442,        15.865,        16.296,
    16.731,        17.163,        17.614,        18.066,        18.525,        18.990]

# Ionization energy of M5 shell in keV.
ATOM_ION_ENERGY_SHELL_M5_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.832,        0.883,        0.931,        0.978,
    1.027,        1.080,        1.130,        1.185,        1.241,        1.295,        1.351,        1.409,        1.467,        1.528,
    1.588,        1.661,        1.743,        1.814,        1.890,        1.967,        2.048,        2.133,        2.220,        2.313,
    2.406,        2.502,        2.603,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        3.325,
    3.442,        3.545,        0.0,        0.0,        0.0,        0.0]

# Characteristic energies of the lines.
ATOM_XRAY_ENERGY_Ka_keV = [0.0,        0.0,        0.0,        0.109,        0.183,        0.277,        0.392,        0.525,        0.677,        0.849,
    1.041,        1.254,        1.487,        1.740,        2.014,        2.308,        2.622,        2.958,        3.314,        3.692,
    4.091,        4.511,        4.952,        5.415,        5.899,        6.404,        6.930,        7.478,        8.048,        8.639,
    9.252,        9.886,        10.544,        11.181,        11.924,        12.649,        13.395,        14.165,        14.958,        15.775,
    16.615,        17.479,        18.367,        19.279,        20.21,        21.18,        22.16,        23.17,        24.21,        25.27,
    26.36,        27.47,        28.61,        29.78,        30.97,        32.19,        33.44,        34.72,        36.03,        37.36,
    38.72,        40.12,        41.54,        42.996,        44.48,        45.998,        47.55,        49.13,        50.74,        52.39,
    54.07,        54.61,        57.53,        59.32,        61.14,        63.00,        64.90,        66.83,        66.99,        70.82,
    72.87,        74.97,        77.11,        79.29,        81.52,        83.78,        86.10,        88.47,        90.88,        93.35,
    95.87,        98.44,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Ka1_keV = [0.0,        0.0,        0.052,        0.110,        0.185,        0.282,        0.392,        0.523,        0.677,        0.851,
    1.041,        1.254,        1.487,        1.740,        2.015,        2.308,        2.622,        2.957,        3.313,        3.691,
    4.090,        4.510,        4.952,        5.414,        5.898,        6.403,        6.930,        7.477,        8.047,        8.638,
    9.251,        9.885,        10.543,        11.221,        11.923,        12.648,        13.394,        14.164,        14.957,        15.774,
    16.614,        17.478,        18.410,        19.278,        20.214,        21.175,        22.162,        23.172,        24.207,        25.270,
    26.357,        27.471,        28.610,        29.802,        30.970,        32.191,        33.440,        34.717,        36.023,        37.359,
    38.649,        40.124,        41.529,        42.983,        44.470,        45.985,        47.528,        49.099,        50.730,        52.360,
    54.063,        55.757,        57.524,        59.310,        61.131,        62.991,        64.886,        66.820,        68.794,        70.821,
    72.860,        74.957,        77.097,        79.296,        81.525,        83.800,        86.119,        88.485,        90.894,        93.334,
    95.851,        98.428,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Ka2_keV = [0.0,        0.0,        0.052,        0.110,        0.185,        0.282,        0.392,        0.523,        0.677,        0.851,
    1.041,        1.254,        1.486,        1.739,        2.014,        2.306,        2.621,        2.955,        3.310,        3.688,
    4.085,        4.504,        4.944,        5.405,        5.877,        6.390,        6.915,        7.460,        8.027,        8.615,
    9.234,        9.854,        10.507,        11.181,        11.877,        12.597,        13.335,        14.097,        14.882,        15.690,
    16.520,        17.373,        18.328,        19.142,        20.072,        21.018,        21.988,        22.982,        24.000,        25.042,
    26.109,        27.200,        28.315,        29.485,        30.623,        31.815,        33.033,        34.276,        35.548,        36.845,
    38.160,        39.523,        40.877,        42.280,        43.737,        45.193,        46.686,        48.205,        49.762,        51.326,
    52.959,        54.579,        56.270,        57.973,        59.707,        61.477,        63.278,        65.111,        66.980,        68.894,
    70.820,        72.794,        74.805,        76.868,        78.956,        81.080,        83.243,        85.446,        87.861,        89.942,
    92.271,        94.649,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Kb1_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        1.297,        1.553,        1.832,        2.136,        2.464,        2.815,        3.192,        3.589,        4.012,
    4.460,        4.931,        5.427,        5.946,        6.490,        7.057,        7.649,        8.264,        8.904,        9.571,
    10.263,        10.981,        11.725,        12.495,        13.290,        14.112,        14.960,        15.834,        16.736,        17.666,
    18.621,        19.607,        20.585,        21.655,        22.721,        23.816,        24.942,        26.093,        27.274,        28.483,
    29.723,        30.993,        32.292,        33.644,        34.984,        36.376,        37.799,        39.255,        40.746,        42.269,
    43.945,        45.400,        47.207,        48.718,        50.391,        52.178,        53.934,        55.690,        57.576,        59.352,
    61.282,        63.209,        65.210,        67.233,        69.298,        71.404,        73.549,        75.736,        77.968,        80.258,
    82.558,        84.922,        87.335,        89.809,        92.319,        94.877,        97.483,        100.136,    102.846,    105.592,
    108.408,    111.289,    0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Kb2_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    10.365,        11.100,        11.863,        12.651,        13.465,        14.313,        15.184,        16.083,        17.011,        17.969,
    18.951,        19.964,        21.012,        22.072,        23.169,        24.297,        25.454,        26.641,        27.859,        29.106,
    30.387,        31.698,        33.016,        34.446,        35.819,        37.255,        38.728,        40.231,        41.772,        43.298,
    44.955,        46.553,        48.241,        49.961,        51.737,        53.491,        55.292,        57.088,        58.969,        60.959,
    62.946,        64.936,        66.999,        69.090,        71.220,        73.393,        75.605,        77.866,        80.165,        82.526,
    84.904,        87.343,        89.833,        92.386,        94.976,        97.616,        100.305,    103.048,    105.838,    108.671,
    111.575,    114.549,    0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_La_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.341,
    0.395,        0.452,        0.511,        0.573,        0.637,        0.705,        0.776,        0.852,        0.93,        1.012,
    1.098,        1.188,        1.282,        1.379,        1.48,        1.586,        1.694,        1.807,        1.923,        2.042,
    2.166,        2.293,        2.424,        2.559,        2.697,        2.839,        2.984,        3.134,        3.287,        3.414,
    3.605,        3.769,        3.938,        4.11,        4.287,        4.466,        4.651,        4.840,        5.034,        5.230,
    5.433,        5.636,        5.846,        6.057,        6.273,        6.495,        6.720,        6.949,        7.180,        7.416,
    7.656,        7.899,        8.146,        8.398,        8.653,        8.912,        9.175,        9.442,        9.713,        9.989,
    10.27,        10.55,        10.84,        11.13,        11.43,        11.73,        12.03,        12.34,        12.65,        12.97,
    13.29,        13.61,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Lb1_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.344,
    0.399,        0.458,        0.519,        0.581,        0.647,        0.717,        0.790,        0.866,        0.948,        1.032,
    1.122,        1.216,        1.317,        1.419,        1.526,        1.638,        1.752,        1.872,        1.996,        2.124,
    2.257,        2.395,        2.538,        2.683,        2.834,        2.990,        3.151,        3.316,        3.487,        3.662,
    3.843,        4.029,        4.220,        4.422,        4.620,        4.828,        5.043,        5.262,        5.489,        5.722,
    5.956,        6.206,        6.456,        6.714,        6.979,        7.249,        7.528,        7.810,        8.103,        8.401,
    8.708,        9.021,        9.341,        9.670,        10.008,        10.354,        10.706,        11.069,        11.439,        11.823,
    12.210,        12.611,        13.021,        13.441,        13.873,        14.316,        14.770,        15.233,        15.712,        16.200,
    16.700,        17.218,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Lb2_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        2.219,
    2.367,        2.518,        2.674,        2.836,        3.001,        3.172,        3.348,        3.528,        3.713,        3.904,
    4.100,        4.301,        4.507,        4.720,        4.936,        5.156,        5.384,        5.613,        5.850,        6.090,
    6.336,        6.587,        6.842,        7.102,        7.368,        7.638,        7.912,        8.188,        8.472,        8.758,
    9.048,        9.346,        9.649,        9.959,        10.273,        10.596,        10.918,        11.249,        11.582,        11.923,
    12.268,        12.620,        12.977,        13.338,        13.705,        14.077,        14.459,        14.839,        15.227,        15.620,
    16.022,        16.425,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Lg_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        2.302,
    2.462,        2.623,        2.792,        2.964,        3.144,        3.328,        3.519,        3.716,        3.920,        4.131,
    4.347,        4.570,        4.800,        5.036,        5.280,        5.531,        5.789,        6.052,        6.322,        6.602,
    6.891,        7.180,        7.478,        7.788,        8.104,        8.418,        8.748,        9.089,        9.424,        9.779,
    10.142,        10.514,        10.892,        11.283,        11.684,        12.094,        12.509,        12.939,        13.379,        13.828,
    14.288,        14.762,        15.244,        15.740,        16.248,        16.768,        17.301,        17.845,        18.405,        18.977,
    19.559,        20.163,        0.0,        0.0,        0.0,        0.0]

ATOM_XRAY_ENERGY_Ma_keV = [0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0,        0.833,        0.883,        0.929,        0.978,
    1.033,        1.081,        1.131,        1.185,        1.240,        1.293,        1.348,        1.406,        1.462,        1.521,
    1.581,        1.645,        1.710,        1.775,        1.843,        1.910,        1.980,        2.051,        2.123,        2.196,
    2.271,        2.346,        2.423,        2.996,        3.082,        3.171,        0.0,        0.0,        0.0,        0.0,
    0.0,        0.0,        0.0,        0.0,        0.0,        0.0]

def getShellList():
    shells = [SHELL_K, SHELL_L3, SHELL_M5]
    return shells

def getAtomicNumber(symbol):
    atomicNumber = ATOM_SYMBOLS.index(symbol)+1

    return atomicNumber

def getAtomSymbol(atomicNumber):
    return ATOM_SYMBOLS[atomicNumber-1]

def getMassDensity_g_cm3(symbol):
    atomicNumber = getAtomicNumber(symbol)

    return ATOM_MASS_DENSITY_g_cm3[atomicNumber-1]

def getIonizationEnergy_keV(shell, element):
    atomicNumber = getAtomicNumber(element)

    if shell == SHELL_K:
        return ATOM_ION_ENERGY_SHELL_K_keV[atomicNumber-1]
    elif shell == SHELL_L3:
        return ATOM_ION_ENERGY_SHELL_L3_keV[atomicNumber-1]
    elif shell == SHELL_M5:
        return ATOM_ION_ENERGY_SHELL_M5_keV[atomicNumber-1]

    return 0.0

def getXRayEnergy_keV(line, element):
    atomicNumber = getAtomicNumber(element)

    if line == SHELL_K:
        return ATOM_XRAY_ENERGY_Ka1_keV[atomicNumber-1]
    elif line == SHELL_L3:
        return ATOM_XRAY_ENERGY_La_keV[atomicNumber-1]
    elif line == ATOM_XRAY_ENERGY_Ma_keV:
        return ATOM_ION_ENERGY_SHELL_M5_keV[atomicNumber-1]

    return 0.0

def run():
    print getMassDensity_g_cm3('Cr')
    print ATOM_ION_ENERGY_SHELL_K_keV[7-1]
    print ATOM_ION_ENERGY_SHELL_K_keV[28-1]
    print ATOM_ION_ENERGY_SHELL_K_keV[79-1]

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=run)
