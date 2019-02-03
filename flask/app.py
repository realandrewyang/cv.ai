from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/post', methods=['POST'])
def post():
    req = request.json['data']
    with tf.Session() as session:
        embed = hub.Module('model')
        input_tensor = tf.placeholder(tf.string, shape=(None))
        enconding_tensor = embed(input_tensor)
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        embeddings = session.run(
            enconding_tensor, feed_dict={input_tensor: req})
        corr = np.inner(embeddings, embeddings).tolist()
        embeddings = embeddings.tolist()
        return jsonify({'corr': corr, 'embeddings': embeddings})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
