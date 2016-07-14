import unittest, json

from flask import Flask, session
from app import app, db, models

example_post_fail_empty = {
    'text' : ''
}

example_post_fail_too_long = {
    'text' : 'Cras tristique faucibus lectus et aliquam. Nulla venenatis metus nec vestibulum vehicula. Vivamus lectus augue, semper et nunc vitae, efficitur iaculis ipsum. Pellentesque a turpis sit amet metus lobortis egestas et et mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras dictum orci at nibh vulputate aliquam. Proin odio urna, scelerisque ac sollicitudin nec, egestas commodo nibh. Vivamus nunc purus, efficitur vel scelerisque efficitur, lobortis a tortor. Nunc id tempus ante, nec efficitur magna. Vestibulum quis aliquam dui. Nam nec odio pulvinar, ornare sapien vel, sollicitudin velit.'
}

example_post_success = {
    'text' : 'Hello World!'
}

example_edited_post = {
    'text' : 'Hello Hell!'
}

class APITest(unittest.TestCase):

    def setUp(self):
        self.app        = app
        self.client     = self.app.test_client()

    def tearDown(self):
        #Flush/drop database
        models.Post.query.delete()
        db.session.commit()

    def my_assert_func (self, response, code):
        """Chek response on status code, headers and return response_json for all tests"""
        self.assertEqual(response.status_code, code)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        response_json = json.loads(response.get_data(as_text=True))
        return response_json

    def test_add_post(self):
        """Test for adding new post"""

        # ------------- FAIL Test empty post ------------- #
        response = self.client.post('/post/', data=json.dumps(example_post_fail_empty), headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response, 400)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Text is missing!'
        })

        # ------------- FAIL Test too large post ------------- #
        response = self.client.post('/post/', data=json.dumps(example_post_fail_too_long), headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response, 413)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Text is longer than 140 chars!'
        })

        # ------------- SUCCESS Test post ------------- #
        response = self.client.post('/post/', data=json.dumps(example_post_success), headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response, 201)

        response_model = {
            'status' : str,
            'post' : dict
        }

        post_model = {
            'id': int, 
            'text': str, 
            'timestamp': int
        }

        self.assertTrue(all(type(response_json[key]) == response_model[key] for key in response_model.keys()))

        post = response_json['post']

        self.assertTrue(all(type(post[key]) == post_model[key] for key in post_model.keys()))

    def test_get_posts(self):
        """GET posts test"""

        # ------------- SUCCESS Test GET all posts ------------- #
        response = self.client.get('/post/')

        response_json = self.my_assert_func(response, 200)

        response_model = {
            'status' : str,
            'posts' : list
        }

        self.assertTrue(all(type(response_json[key]) == response_model[key] for key in response_model.keys()))

        # ------------- SUCCESS Test GET some post ------------- #
        self.client.post('/post/', data=json.dumps(example_post_success), headers={
            'Content-Type' : 'application/json'
        })

        response = self.client.get('/post/')
        response_json = json.loads(response.get_data(as_text=True))

        post_model = {
            'id': int, 
            'text': str, 
            'timestamp': int
        }
        
        post = response_json['posts'][0]

        self.assertTrue(all(type(post[key]) == post_model[key] for key in post_model.keys()))

    def test_edit_post(self):
        """Test for editing existing test"""

        response = self.client.post('/post/', data=json.dumps(example_post_success), headers={
            'Content-Type' : 'application/json'
        })

        # ------------- FAIL Test "Post not found!" ------------- #
        response = self.client.put('/post/666', data=json.dumps(example_edited_post), headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response, 404)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Post not found!'
        })

        # ------------- FAIL Test "TOO LARGE" ------------- #
        response = self.client.put('/post/1', data=json.dumps(example_post_fail_too_long), headers={
            'Content-Type' : 'application/json'
        })
        
        response_json = self.my_assert_func(response, 413)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Text is longer than 140 chars!'
        })

        # ------------- FAIL Test "TEXT MISSING" ------------- #
        response = self.client.put('/post/1', data=json.dumps(example_post_fail_empty), headers={
            'Content-Type' : 'application/json'
        })
        
        response_json = self.my_assert_func(response, 400)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Text is missing!'
        })

        # ------------- SUCCESS EDIT Test ------------- #
        response = self.client.put('/post/1', data=json.dumps(example_edited_post), headers={
            'Content-Type' : 'application/json'
        })
        
        response_json = self.my_assert_func(response, 200)

        response_model = {
            'status' : str,
            'post' : dict
        }

        post_model = {
            'id': int, 
            'text': str, 
            'timestamp': int
        }

        self.assertTrue(all(type(response_json[key]) == response_model[key] for key in response_model.keys()))

        post = response_json['post']

        self.assertTrue(all(type(post[key]) == post_model[key] for key in post_model.keys()))

    def test_delete_post(self):
        """Test for deleting test"""

        response = self.client.post('/post/', data=json.dumps(example_post_success), headers={
            'Content-Type' : 'application/json'
        })

        # ------------- SUCCESS Test DELETE post ------------- #
        response = self.client.delete('/post/1', headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response,200)

        response_model = {'status' : str}

        self.assertTrue(all(type(response_json[key]) == response_model[key] for key in response_model.keys()))

        # ------------- FAILED Test DELETE post ------------- #
        response = self.client.delete('/post/666', headers={
            'Content-Type' : 'application/json'
        })

        response_json = self.my_assert_func(response, 404)

        self.assertDictEqual(response_json, {
            'status' : 'failed',
            'error'  : 'Post not found!'
        })

if __name__ == '__main__':
    unittest.main()