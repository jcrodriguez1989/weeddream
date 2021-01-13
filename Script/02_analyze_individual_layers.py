#### Setup
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import inception_v3
from tensorflow.keras.models import load_model

# load the input image from a URL. Replace the URL to play with other input images.
base_image_path = keras.utils.get_file(
  'original_img.jpg',
  'https://raw.githubusercontent.com/jcrodriguez1989/weeddream/main/original_img.jpg'
)

# These are the names of the layers for which we try to maximize activation, as well as their weight
# in the final loss we try to maximize.
import sys
layers = ['mixed' + sys.argv[1]]
weights = [float(sys.argv[2])]
layer_settings = { layers[0]: weights[0] }
n_layers = len(layers)
result_prefix = '_'.join([ layers[i] + '_' + str(weights[i]) for i in range(n_layers)])
print(layer_settings)

# Playing with these hyperparameters will also allow you to achieve new effects
step = 0.01  # Gradient ascent step size
num_octave = 4  # Number of scales at which to run gradient ascent
octave_scale = 1.4  # Size ratio between scales
iterations = 30  # Number of ascent steps per scale
max_loss = 150.0

def preprocess_image(image_path):
  # Util function to open, resize and format pictures
  # into appropriate arrays.
  img = keras.preprocessing.image.load_img(image_path)
  img = keras.preprocessing.image.img_to_array(img)
  img = np.expand_dims(img, axis=0)
  img = inception_v3.preprocess_input(img)
  return img


def deprocess_image(x):
  # Util function to convert a NumPy array into a valid image.
  x = x.reshape((x.shape[1], x.shape[2], 3))
  # Undo inception v3 preprocessing
  x /= 2.0
  x += 0.5
  x *= 255.0
  # Convert to uint8 and clip to the valid range [0, 255]
  x = np.clip(x, 0, 255).astype('uint8')
  return x


#### Compute the Deep Dream loss

# Load the WeedCeption_v1 model.
model = load_model('Models/weedception_v1.h5')

# Get the symbolic outputs of each "key" layer (we gave them unique names).
outputs_dict = dict(
  [
    (layer.name, layer.output)
    for layer in [model.get_layer(name) for name in layer_settings.keys()]
  ]
)

# Set up a model that returns the activation values for every target layer (as a dict).
feature_extractor = keras.Model(inputs=model.inputs, outputs=outputs_dict)

def compute_loss(input_image):
  features = feature_extractor(input_image)
  # Initialize the loss
  loss = tf.zeros(shape=())
  for name in features.keys():
    coeff = layer_settings[name]
    activation = features[name]
    # We avoid border artifacts by only involving non-border pixels in the loss.
    scaling = tf.reduce_prod(tf.cast(tf.shape(activation), 'float32'))
    loss += coeff * tf.reduce_sum(tf.square(activation[:, 2:-2, 2:-2, :])) / scaling
  return loss


#### Set up the gradient ascent loop for one octave

@tf.function
def gradient_ascent_step(img, learning_rate):
  with tf.GradientTape() as tape:
    tape.watch(img)
    loss = compute_loss(img)
  # Compute gradients.
  grads = tape.gradient(loss, img)
  # Normalize gradients.
  grads /= tf.maximum(tf.reduce_mean(tf.abs(grads)), 1e-6)
  img += learning_rate * grads
  return loss, img


def gradient_ascent_loop(img, iterations, learning_rate, max_loss=None):
  for i in range(iterations):
    loss, img = gradient_ascent_step(img, learning_rate)
    if max_loss is not None and loss > max_loss:
      break
    print('... Loss value at step %d: %.2f' % (i, loss))
  return img


#### Run the training loop, iterating over different octaves

original_img = preprocess_image(base_image_path)
original_shape = original_img.shape[1:3]

successive_shapes = [original_shape]
for i in range(1, num_octave):
  shape = tuple([int(dim / (octave_scale ** i)) for dim in original_shape])
  successive_shapes.append(shape)

successive_shapes = successive_shapes[::-1]
shrunk_original_img = tf.image.resize(original_img, successive_shapes[0])

img = tf.identity(original_img)  # Make a copy
for i, shape in enumerate(successive_shapes):
  print('Processing octave %d with shape %s' % (i, shape))
  img = tf.image.resize(img, shape)
  img = gradient_ascent_loop(
    img, iterations=iterations, learning_rate=step, max_loss=max_loss
  )
  upscaled_shrunk_original_img = tf.image.resize(shrunk_original_img, shape)
  same_size_original = tf.image.resize(original_img, shape)
  lost_detail = same_size_original - upscaled_shrunk_original_img
  img += lost_detail
  shrunk_original_img = tf.image.resize(original_img, shape)


keras.preprocessing.image.save_img(
  'LayersImgs/' + result_prefix + '.png', deprocess_image(img.numpy())
)
