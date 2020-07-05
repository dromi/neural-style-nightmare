def format_anishathalye(content, styles, output=None, initial=None, network=None, sim_args=None):
    stry = "python impl/neural_style.py --content " + content + " --styles " + styles
    if output is not None:
        stry += " --output " + output
    if initial is not None:
        stry += " --initial " + initial
    if network is not None:
        stry += " --network " + network
    if sim_args is not None:
        stry += " " + sim_args
    return stry

def format_jcj():
    pass