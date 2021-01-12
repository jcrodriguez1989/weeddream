# https://github.com/adityaanantharaman/transfer-learning
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# load training images
train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
train_generator = train_datagen.flow_from_directory(
  './TrainingImages/', target_size=(299, 299), color_mode='rgb', batch_size=32,
  class_mode='categorical', shuffle=True
)

# https://keras.io/api/applications/
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# train InceptionV3 from zero (just keep the architecture)
base_model = InceptionV3(weights=None, include_top=False)

# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(1024, activation='relu')(x)
# and a logistic layer -- let's say we have N classes
predictions = Dense(len(train_generator.class_indices), activation='softmax')(x)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

# train every layer at once
for layer in model.layers:
  layer.trainable = True

# we need to recompile the model for these modifications to take effect
# we use SGD with a low learning rate
from tensorflow.keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

# train the model on the new data for a few epochs
step_size_train = train_generator.n // train_generator.batch_size
model.fit(train_generator, steps_per_epoch=step_size_train, epochs=10)

model.save('Models/weedception_v1.h5') # creates a HDF5 file 'my_model.h5'
