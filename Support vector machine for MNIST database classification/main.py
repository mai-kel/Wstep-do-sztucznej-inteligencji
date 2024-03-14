import tensorflow as tf
import numpy as np
import argparse
from support_vector_machine import MegaSVM, plot_confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

if __name__ == "__main__":

    # getting params
    parser = argparse.ArgumentParser()
    parser.add_argument('to_train', type=int)
    parser.add_argument('to_test', type=int)
    args = parser.parse_args()
    to_train = int(args.to_train)
    to_test = int(args.to_test)

    # loading MNIST database
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

    # changing images format from 28x28 matrix to 784 length vector and scaling pixels
    train_images = np.reshape(train_images, (60000, 784))/255
    test_images = np.reshape(test_images, (10000, 784))/255

    # selecting random indexes that will be used to choose random sample of images to test and train
    random_indexes_train = np.random.choice(len(train_images), to_train)
    random_indexes_test = np.random.choice(len(test_images), to_test)

    # choosing random sample of training data
    train_images_sample = train_images[random_indexes_train]
    train_labels_sample = train_labels[random_indexes_train]

    # choosing random sample of testing data
    test_images_sample = test_images[random_indexes_test]
    test_labels_sample = test_labels[random_indexes_test]

    svm = MegaSVM()
    svm.fit(train_images_sample, train_labels_sample)

    predicted = svm.predict_multiple(test_images_sample)

    acc = accuracy_score(test_labels_sample, predicted)
    conf_matrix = confusion_matrix(test_labels_sample, predicted)
    class_report = classification_report(test_labels_sample, predicted)

    print("Accuracy:", acc)
    print("")
    print("Confusion matrix")
    print(conf_matrix)
    print("")
    print("Classification Report")
    print("")
    print(class_report)
    plot_confusion_matrix(conf_matrix)
