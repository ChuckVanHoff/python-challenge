import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util

def detect_rubiks_cube(image):
    # Load the pre-trained object detection model
    model_path = 'path/to/pretrained/model'
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(model_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    # Load the label map
    label_map_path = 'path/to/label/map'
    label_map = label_map_util.load_labelmap(label_map_path)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1)
    category_index = label_map_util.create_category_index(categories)

    # Preprocess the image
    preprocessed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)

    # Perform object detection
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: preprocessed_image})

            # Threshold for detection confidence
            confidence_threshold = 0.5

            # Iterate through the detections and check for Rubik's Cube
            for i in range(int(num_detections[0])):
                if scores[0, i] > confidence_threshold and \
                   category_index[classes[0, i]]['name'] == 'Rubik\'s Cube':
                    return True

    return False

