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

def format_jcj(content, styles, output=None, initial=None, sim_args=None):
    essential = "-gpu 0 -backend nn -optimizer lbfgs -model_file ../jcj/models/VGG_ILSVRC_19_layers.caffemodel -proto_file ../jcj/models/VGG_ILSVRC_19_layers_deploy.prototxt"
    stry = "th ../jcj/neural_style.lua -style_image " + styles + " -content_image " + content + " " + essential
    if output is not None:
        stry += " -output_image " + output
    if initial is not None:
        stry += " -init image -init_image " + initial
    if sim_args is not None:
        stry += " " + sim_args
    return stry




"""
REQUIRED:
# -style_image          Style target image [examples/inputs/seated-nude.jpg]
# -content_image        Content target image [examples/inputs/tubingen.jpg]
# -gpu                  Zero-indexed ID of the GPU to use; for CPU mode set -gpu = -1 [0]

TUNING:
# -content_weight       [5]
# -style_weight         [100]
# -tv_weight            [0.001]
# -num_iterations       [1000]
# -normalize_gradients  [false]
# -optimizer            lbfgs|adam [lbfgs]
# -learning_rate        [10]
# -style_scale          [1]
# -pooling              max|avg [max]

MISC:
# -image_size           Maximum height / width of generated image [512]
# -init                 random|image [random]
# -init_image           []
# -seed                 [-1]
# -save_iter            [100]
# -output_image         [out.png]
# -original_colors      [0]


DONT CARE YET:
# -style_blend_weights  [nil]
# -multigpu_strategy    Index of layers to split the network across GPUs []
# -print_iter           [50]
# -cudnn_autotune       [false]
# -content_layers       layers for content [relu4_2]
# -style_layers         layers for style [relu1_1,relu2_1,relu3_1,relu4_1,relu5_1]
# -proto_file           [models/VGG_ILSVRC_19_layers_deploy.prototxt]
# -model_file           [models/VGG_ILSVRC_19_layers.caffemodel]
# -backend              nn|cudnn|clnn [nn]

DONT KNOW:
# -lbfgs_num_correction [0]
"""


