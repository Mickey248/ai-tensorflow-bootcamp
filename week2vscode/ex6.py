import tensorflow as tf

input_tensor = [[0, 1], [2,3], [4,5]]

x = tf.zeros_like(input_tensor)

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
writer.close()