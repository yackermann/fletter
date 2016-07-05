from app import app, models, db
from flask import jsonify, abort, request

app.url_map.strict_slashes = False

@app.route('/post/', methods=['GET'])
@app.route('/post/<int:post_id>', methods=['GET'])
def get_posts():
    pass

@app.route('/post/', methods=['POST'])
def add_post():
    content = request.json.get('text', '')
    if len(content) > 140 or len(content) == 0:
        return jsonify({'status' : 'failed'}), 400 

    post = models.Post(content)
    db.session.add(post)
    db.session.commit()

    return jsonify({'status' : 'ok'}), 201

@app.route('/post/<int:post_id>', methods=['PUT'])
def edit_post():
    pass

@app.route('/post/<int:post_id>', methods=['DELETE'])
def remove_post():
    pass

