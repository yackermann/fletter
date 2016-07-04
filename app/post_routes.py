from app import app

@app.route('/post/', methods=['GET'])
@app.route('/post/<int:post_id>', methods=['GET'])
def get_posts():
    pass

@app.route('/post/', methods=['PUT'])
def add_post():
    pass

@app.route('/post/<int:post_id>', methods=['POST'])
def edit_post():
    pass

@app.route('/post/<int:post_id>', methods=['DELETE'])
def remove_post():
    pass

