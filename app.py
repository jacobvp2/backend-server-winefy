from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS
from predict_types import predict_type,recreate_model, predict_tweet
from twitterscraper import tweet_return

app = Flask(__name__)
CORS(app)


@app.route('/tweet_pred', methods=['POST'])
def tweet():

    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        # print("tweet_pred",data)
        user_handle = data["handle"]
        tweet_return(user_handle)
        user_type = predict_tweet(user_handle)
        # render_template('result.html')
        return jsonify(user_type),200


if __name__ == '__main__' :
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True, port=5000)
