__author__ = 'ptoth'


def get_config():

    params = {}

    params['global'] = {
        'epochs': 5
    }

    verbose = 1
    activation_function = "Sigmoid"
    activation_threshold = 0.5
    min_w = -1.0
    max_w = 1.0
    lifetime_sparsity = 0.014
    duty_cycle_decay = 0.006
    w_lr = 0.05
    inh_lr = 0.05
    b_lr = 0.05
    r_b_lr = 0.05
    learning_rate_decay = 0.01
    dropout_ratio = None
    zoom = 0.4
    make_sparse = False
    target_sparsity = 0.1
    layer_repeat_factor = None
    momentum = 0.5
    local_activation_radius = 0.2

    layer1 = {
        'name': "layer1",
        'repeat_factor': layer_repeat_factor,
        'feedforward': {
            'name': "layer1-feedforward",
            'inputs_size': 22050,
            'output_size': 1024,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'recurrent': {
            'name': "layer1-recurrent",
            'inputs_size': 1024,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'feedback': {
            'name': "layer1-feedback",
            'inputs_size': 768,
            'output_size': 22050,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': False,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        }
    }

    layer2 = {
        'name': "layer2",
        'repeat_factor': layer_repeat_factor,
        'feedforward': {
            'name': "layer2-feedforward",
            'inputs_size': 1024,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'recurrent': {
            'name': "layer2-recurrent",
            'inputs_size': 256,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'feedback': {
            'name': "layer2-feedback",
            'inputs_size': 512,
            'output_size': 512,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        }
    }

    layer3 = {
        'name': "layer3",
        'repeat_factor': layer_repeat_factor,
        'feedforward': {
            'name': "layer3-feedforward",
            'inputs_size': 256,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'recurrent': {
            'name': "layer3-recurrent",
            'inputs_size': 256,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        },
        'feedback': {
            'name': "layer3-feedback",
            'inputs_size': 256,
            'output_size': 256,
            'activation_function': activation_function,
            'activation_threshold': activation_threshold,
            'lifetime_sparsity': lifetime_sparsity,
            'min_weight': min_w,
            'max_weight': max_w,
            'dropout_ratio': dropout_ratio,
            'momentum': momentum,
            'local_activation_radius': local_activation_radius,
            'zoom': zoom,
            'make_sparse': make_sparse,
            'target_sparsity': target_sparsity,
            'duty_cycle_decay': duty_cycle_decay,
            'learning_rate_decay': learning_rate_decay,
            'weights_lr': w_lr,
            'inhibition_lr': inh_lr,
            'bias_lr': b_lr,
            'recon_bias_lr': r_b_lr
        }
    }

    params['network'] = {
        'name': "Bach network",
        'verbose': verbose,
        'activation_function': "Sigmoid",
        'visualize_states': True,
        'input': {

        },
        'layers': [
            layer1
            , layer2
            , layer3
        ],
        'output': {

        }
    }

    return params
