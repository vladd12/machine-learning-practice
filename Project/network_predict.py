# Импорт библиотек
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow import feature_column
from file_module import file_import

# Все пути
path_features_file = r"./har_dataset/features.txt" # Путь до списка признаков
path_input_acc = r"./input_acc.csv" # Путь до файла с данными акселерометра
path_input_gyro = r"./input_gyro.csv" # Путь до файла с данными гироскопа

# Функция, возвращающая список признаков из файла 
def features_string(path_features_file):
    features_dict = {}
    with open(path_features_file) as file:
        for line in file:
            key, *value = line.split()
            features_dict[key] = value
    string = ""
    for i in range(1, 562):
        string = string + (features_dict[str(i)])[0] + " "
    return(string)

# Получаем список признаков
string = features_string(path_features_file)
features = string.split(' ')
del features[561]

# Создание слоя признаков
feature_columns = [] # Столбцы признаков
for header in range(0, 561):
    feature_columns.append(feature_column.numeric_column((features[header])))
feature_layer = tf.keras.layers.DenseFeatures(feature_columns) # Слой признаков

# Создание модели
model = tf.keras.Sequential([
    feature_layer,
    layers.Dense(128, activation=tf.nn.relu),
    layers.Dense(128, activation=tf.nn.relu),
    layers.Dense(6, activation=tf.nn.softmax)
])

# Компиляция модели
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'], run_eagerly=True)

# Загрузка модели
checkpoint_path = r"./checkpoint/cp.ckpt"
model.load_weights(checkpoint_path)

# Получение массива признаков из двух входных файлов с данными гироскопа и акселерометра
input_arr = file_import(path_input_acc, path_input_gyro)

# Фокусы по превращению массива и строки в данные для нейросети
s = pd.DataFrame(data=[input_arr], index=np.arange(0, 561), columns=features)
ds_input = tf.data.Dataset.from_tensor_slices((dict(s)))
ds_input = ds_input.batch(32)

# Предсказание по данным
class_names = ['WALKING', 'WALKING_UPSTAIRS', 'WALKING_DOWNSTAIRS', 'SITTING', 'STANDING', 'LAYING']
predict = model.predict(ds_input)
a = np.array([predict[0][0], predict[0][1], predict[0][2], predict[0][3], predict[0][4], predict[0][5]])
predicted_id = np.argmax(a)
predicted_class_name = class_names[predicted_id]
print(predicted_class_name)