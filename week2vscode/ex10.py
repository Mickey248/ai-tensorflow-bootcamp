import tensorflow as tf

x = tf.linspace(10.0, 13.0, 4, name="linspace")


with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
writer.close()