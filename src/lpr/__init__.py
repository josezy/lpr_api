import tensorflow as tf

from lpr.lpr_utils import detect_plates, load_plate_models

lp_threshold = 0.5
letter_threshold = 0.5
net, meta, wpod_net = load_plate_models()

graph = tf.get_default_graph()


def do_detect(img):
    with graph.as_default():
        return detect_plates(
            img,
            net,
            meta,
            wpod_net,
            lp_threshold,
            letter_threshold
        )
