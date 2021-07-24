import tensorflow as tf

print(f'Using GPU: {len(tf.config.list_physical_devices("GPU")) > 0}')
print(f'Tensorflow Version: {tf.__version__}')