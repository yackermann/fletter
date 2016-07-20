from app import app, models, db
from flask import jsonify, abort, request
from functools import wraps

app.url_map.strict_slashes = False

class SecurityAPI():
    """Check API requests"""

    def request_verifying_json(self, func):
        """Check request is it json or not"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.headers['Content-Type'] == 'application/json':
                return func(*args, **kwargs)
            else:
                return jsonify({
                    'status' : 'failed',
                    'error'  : 'Unsupported media type!'
                }), 415
        return wrapper

security = SecurityAPI()

@app.route('/post/', methods=['GET'])
@app.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id=None):
    """Searches the database for entries, then displays them."""
    if post_id is None:
        posts = db.session.query(models.Post)
        posts_json = [post.json() for post in posts]
        posts_json.reverse()
        return jsonify({
            'status' : 'ok',
            'posts' : posts_json
        })

    else:
        post = models.Post.query.get(post_id)

        if post is None:
            return jsonify({
                'status' : 'failed',
                'error'  : 'Post not found!'
            }), 404

        post_json = post.json()

        return jsonify({
            'status' : 'ok',
            'post' : post_json
        })


@app.route('/post/', methods=['POST'])
@security.request_verifying_json
def add_post():
    content = request.json.get('text', '')

    if len(content) > 140:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Text is longer than 140 chars!'
        }), 413
        
    if len(content) == 0:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Text is missing!'
        }), 400

    post = models.Post(content)
    db.session.add(post)
    db.session.commit()

    return jsonify({
        'status' : 'ok',
        'post' : post.json()
    }), 201

@app.route('/post/<int:post_id>', methods=['PUT'])
@security.request_verifying_json
def edit_post(post_id):
    """Edit post in the database."""
    post = models.Post.query.get(post_id)

    if post is None:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Post not found!'
        }), 404

    if len(content) > 140:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Text is longer than 140 chars!'
        }), 413

    if len(content) == 0:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Text is missing!'
        }), 400

    if not post.check_time():
        return jsonify({
            'status' : 'failed',
            'error'  : 'You can not modify posts older than 120 seconds!'
        }), 403

    post.text = content
    db.session.commit()

    return jsonify({
        'status' : 'ok',
        'post' : post.json()
    }), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def remove_post(post_id):
    """Delete post in the database."""
    post = models.Post.query.get(post_id)

    if post is None:
        return jsonify({
            'status' : 'failed',
            'error'  : 'Post not found!'
        }), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({'status' : 'ok'}), 200