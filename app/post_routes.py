from app import app, models, db
from flask import jsonify, abort, request

app.url_map.strict_slashes = False

@app.route('/post/', methods=['GET'])
@app.route('/post/<int:post_id>', methods=['GET'])
def get_post():
    """Searches the database for entries, then displays them."""
    posts = db.session.query(models.Post)
    posts_json = [post.json() for post in posts]
    return jsonify({'status' : 'ok'}, {'posts' : posts_json})

@app.route('/post/', methods=['POST'])
def add_post():
    """Adds new post to the database."""
    content = request.json.get('text', '')
    if len(content) > 140 or len(content) == 0:
        return jsonify({'status' : 'failed'}), 400 

    post = models.Post(content)
    db.session.add(post)
    db.session.commit()

    return jsonify({'status' : 'ok'}, {'post' : post.json()}), 201

@app.route('/post/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    """Edit post in the database."""
    post = models.Post.query.get(post_id)
    content = request.json.get('text', '')

    if post is None or len(content) > 140 or len(content) == 0:
        return jsonify({'status' : 'failed'}), 400

    post.text = content
    db.session.commit()

    return jsonify({'status' : 'ok'}, {'post' : post.json()}), 201

@app.route('/post/<int:post_id>', methods=['DELETE'])
def remove_post():
    pass

