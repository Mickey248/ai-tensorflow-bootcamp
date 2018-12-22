import tensorflow as tf

x = tf.ones([2, 3], tf.int32)

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
writer.close()