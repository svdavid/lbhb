# Hack to get plugins loaded
import os
from lbhb.analysis.rdt import plugins
os.environ['KEYWORD_PLUGINS'] = f'["{plugins.__file__}"]'

from nems import xforms

batch, cell = 269, 'chn019a-a1'
#batch, cell = 269, 'oys042c-d1'
#batch, cell = 273, 'chn041d-b1'
#batch, cell = 273, 'zee027b-c1'
#modelspec = 'RDTwcg18x2-RDTfir2x15_RDTstreamgain_lvl1_dexp1'
#keywordstring = 'dlog-wc.18x1.g-fir.1x15-lvl.1'
keywordstring = 'rdtwc.18x1.g-rdtfir.1x15-rdtgain.global.{n_targets}-lvl.1'

xfspec = [
    ('nems.xforms.init_context', {'batch': batch, 'cell': cell, 'cellid': cell, 'keywordstring': keywordstring}),
    ('lbhb.analysis.rdt.io.load_recording', {}),
    ('lbhb.analysis.rdt.preprocessing.split_est_val', {}),
    ('lbhb.analysis.rdt.xforms.format_keywordstring', {}),
    ('nems.xforms.init_from_keywords', {}),
    ('nems.xforms.fit_basic_init', {}),
    ('nems.xforms.fit_basic', {}),
    ('nems.xforms.predict', {}),
    ('nems.xforms.add_summary_statistics', {}),
    ('nems.xforms.plot_summary', {}),
]
#    ('lbhb.analysis.rdt.xforms.fix_modelspec', {}),

context = {}
for step in xfspec:
    context = xforms.evaluate_step(step, context)