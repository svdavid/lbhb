def format_keywordstring(recording, keywordstring=None, **context):
    n_targets = recording.meta['n_targets']
    return {
        'keywordstring': keywordstring.format(ntargets=n_targets),
    }


def fix_modelspec(modelspec, **context):
    for ms in modelspec.raw:
        ms[-1]['fn_kwargs']['i'] = 'pred'
    return {'modelspec': modelspec}
