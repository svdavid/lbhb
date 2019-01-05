import numpy as np


def rdtld(key):

    xfspec = [['lbhb.analysis.rdt.io.load_recording', {}]]
    return xfspec


def rdtsev(key):

    xfspec = [['lbhb.analysis.rdt.preprocessing.split_est_val', {}]]
    return xfspec


def rdtfmt(key):

    xfspec = [['lbhb.analysis.rdt.preprocessing.format_keywordstring', {}]]
    return xfspec
