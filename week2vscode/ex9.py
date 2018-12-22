import tensorflow as tf

x = tf.fill([2, 3], 8)


with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
writer.close()