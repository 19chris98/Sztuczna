from __future__ import absolute_import, division, print_function
import argparse

import numpy as np
import tensorflow as tf


class ResultHolder:

    def __init__(self, result_name, result_percent):
        self.result_name = result_name
        self.result_percent = result_percent


class BombRecognize:
    @staticmethod
    def load_graph(model_file):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(model_file, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)
        return graph

    @staticmethod
    def read_tensor_from_image_file(file_name, input_height=299, input_width=299, input_mean=0, input_std=255):
        input_name = "file_reader"
        file_reader = tf.read_file(file_name, input_name)
        if file_name.endswith(".png"):
            image_reader = tf.image.decode_png(file_reader, channels=3, name='png_reader')
        elif file_name.endswith(".gif"):
            image_reader = tf.squeeze(tf.image.decode_gif(file_reader, name='gif_reader'))
        elif file_name.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
        else:
            image_reader = tf.image.decode_jpeg(file_reader, channels=3, name='jpeg_reader')
        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0)
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.Session()
        result = sess.run(normalized)
        return result

    @staticmethod
    def load_labels(label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label

    def get_result(self, file_name, model_file, label_file):
        # tu miejsce na wczytanie lub podanie grafu
        input_height = 224
        input_width = 224
        input_mean = 128
        input_std = 128
        input_layer = "input"
        output_layer = "final_result"

        parser = argparse.ArgumentParser()
        parser.add_argument("--image", help="image to be processed")
        parser.add_argument("--graph", help="graph/model to be executed")
        parser.add_argument("--labels", help="name of file containing labels")
        parser.add_argument("--input_height", type=int, help="input height")
        parser.add_argument("--input_width", type=int, help="input width")
        parser.add_argument("--input_mean", type=int, help="input mean")
        parser.add_argument("--input_std", type=int, help="input std")
        parser.add_argument("--input_layer", help="name of input layer")
        parser.add_argument("--output_layer", help="name of output layer")
        args = parser.parse_args()

        graph = self.load_graph(model_file)
        t = self.read_tensor_from_image_file(file_name, input_height=input_height, input_width=input_width, input_mean=input_mean, input_std=input_std)

        input_name = "import/" + input_layer
        output_name = "import/" + output_layer
        input_operation = graph.get_operation_by_name(input_name)
        output_operation = graph.get_operation_by_name(output_name)

        with tf.Session(graph=graph) as sess:
            results = sess.run(output_operation.outputs[0], {input_operation.outputs[0]: t})
        results = np.squeeze(results)

        top_k = results.argsort()[-5:][::-1]
        labels = self.load_labels(label_file)

        final_results = [top_k]

        for i in top_k:
            result = ResultHolder(labels[i], results[i])
            final_results.append(result)

        return final_results
