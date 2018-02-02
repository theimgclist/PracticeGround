# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:28:25 2018

@author: Avinash
"""

import pandas as pd
import tensorflow as tf


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the read end of the pipeline.
    return dataset.make_one_shot_iterator().get_next()


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the read end of the pipeline.
    return dataset.make_one_shot_iterator().get_next()




CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth',
                    'PetalLength', 'PetalWidth', 'Species']
					
SPECIES = ['Sentosa', 'Versicolor', 'Virginica']
y_name='Species'
batch_size = 100
train_steps = 2000

train = pd.read_csv('Data/iris_training.csv', names=CSV_COLUMN_NAMES, header=0)
train_x, train_y = train, train.pop(y_name)

test = pd.read_csv('Data/iris_test.csv', names=CSV_COLUMN_NAMES, header=0)
test_x, test_y = test, test.pop(y_name)

my_feature_columns = []
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10,10],
                     n_classes=3)

classifier.train(
        input_fn=lambda:train_input_fn(train_x, train_y,
                                                 batch_size),
        steps=train_steps)

    # Evaluate the model.
eval_result = classifier.evaluate(
        input_fn=lambda:eval_input_fn(test_x, test_y,
                                                batch_size))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

expected = ['Setosa', 'Versicolor', 'Virginica']
predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }
predictions = classifier.predict(
        input_fn=lambda:eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=batch_size))

for pred_dict, expec in zip(predictions, expected):
        template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(SPECIES[class_id],
                              100 * probability, expec))


