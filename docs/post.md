**Post API Documentation**
---

* **Contents**
    * [Get all posts](#get-posts)
    * [Get post specified by ID](#get-post)
    * [Add new post](#add-new-post)
    * [Edit post specified by ID](#edit-post)
    * [Delete post specified by ID](#delete-post)
    
**Get posts**
----
Returns json data of all posts.

* **URL**

    * /post

* **Method:**

     * `GET`
    
*  **URL Params**

    * None

* **Data Params**

    * None

* **Success Response:**

    * **Code:** 200 OK

        ```javascript
        {
            status: "ok",
            posts: [
                {
                    id: 1, 
                    text: "asddsaads", 
                    timestamp: 1467695707
                }, 
                {
                    id: 2, 
                    text: "dfsfdsfd", 
                    timestamp: 1467695746
                }
            ]
        }
        ```
 
* **Error Response:**

    * **Code:** 500 INTERNATL ERROR

        ```javascript
        {  
            status : "failed", 
            error  : "Unknown error!"
        }
        ```

* **Sample Call:**

    ```javascript
        fetch('/post', {
            method  : 'GET',
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            }
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            console.log(json);
        }).catch(function (err) {
            console.log({ 'status': 'failed', 'error': err });
        })
    ```


**Get post**
----
Returns json data about a single post.

* **URL**

    * /post/:id

* **Method:**

     * `GET`
    
*  **URL Params**

    * `id=[integer]`

* **Data Params**

    * None

* **Success Response:**

    * **Code:** 200 OK

        ```javascript
        {  
            status : "ok", 
            post   : { 
                id   : 42,
                text : "I just had an ice-cream.",
                timestamp : 1467695707
            }
        }
        ```
 
* **Error Response:**

    * **Code:** 404 NOT FOUND

        ```javascript
        {  
            status : "failed", 
            error  : "Post not found!"
        }
        ```

* **Sample Call:**

    ```javascript
        fetch('/post/32', {
            method  : 'GET',
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            }
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            console.log(json);
        }).catch(function (err) {
            console.log({ 'status': 'failed', 'error': err });
        })
    ```


**Add new post**
----
Adds new post

* **URL**

    * /post

* **Method:**

     * `POST`
    
*  **URL Params**

    * None

* **Data Params**

    ```javascript
        {
            text : 'Hello World!'
        }
    ```

* **Success Response:**

    * **Code:** 201 CREATED

        ```javascript
        {  
            status : "ok", 
            post   : { 
                id   : 42,
                text : "I just had an ice-cream.",
                timestamp : 1467695707
            }
        }
        ```
 
* **Error Response:**

    * **Code:** 400 BAD REQUEST

        ```javascript
        {  
            status : "failed", 
            error  : "Text is missing!"
        }
        ```

    * **Code:** 413 REQUEST ENTITY TOO LARGE

        ```javascript
        {  
            status : "failed", 
            error  : "Text is longer than 140 chars!"
        }
        ```


* **Sample Call:**

    ```javascript
      fetch('/post', {
            method  : 'POST',
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            },
            body    : JSON.stringify({
                'text' : 'I just ate potato!'
            })
        }).then(function (response) {
            return response.json()
        }).then(function (json) {
            console.log(json)
        }).catch(function (err) {
            console.log({ 'status': 'failed', 'error': err })
        })
    ```

**Edit post**
----
Edit existing post

* **URL**

    * /post/:id

* **Method:**

     * `PUT`
    
*  **URL Params**

    * `id=[integer]`

* **Data Params**

    ```javascript
        {
            text : 'Goodbye World!'
        }
    ```

* **Success Response:**

    * **Code:** 200 OK

        ```javascript
        {  
            status : "ok", 
            post   : { 
                id   : 34,
                text : "Goodbye World!",
                timestamp : 1467695707
            }
        }
        ```
 
* **Error Response:**

    * **Code:** 404 NOT FOUND

        ```javascript
        {  
            status : "failed", 
            error  : "Post not found!"
        }
        ```

    * **Code:** 400 BAD REQUEST

        ```javascript
        {  
            status : "failed", 
            error  : "Text is missing!"
        }
        ```

    * **Code:** 413 REQUEST ENTITY TOO LARGE

        ```javascript
        {  
            status : "failed", 
            error  : "Text is longer than 140 chars!"
        }
        ```


* **Sample Call:**

    ```javascript
        fetch('/post/23', {
            method  : 'PUT',
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            },
            body    : JSON.stringify({
                'text' : 'Totally edited post!'
            })
        }).then(function (response) {
            return response.json()
        }).then(function (json) {
            console.log(json)
        }).catch(function (err) {
            console.log({ 'status': 'failed', 'error': err })
        })
    ```


**Delete post**
----
Deletes existing post

* **URL**

    * /post/:id

* **Method:**

     * `DELETE`
    
*  **URL Params**

    * `id=[integer]`

* **Data Params**

    * None

* **Success Response:**

    * **Code:** 200 OK

        ```javascript
        {  
            status : "ok"
        }
        ```
 
* **Error Response:**

    * **Code:** 404 NOT FOUND

        ```javascript
        {  
            status : "failed", 
            error  : "Post not found!"
        }
        ```


* **Sample Call:**

    ```javascript
        fetch('/post/21', {
            method  : 'DELETE',
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            }
        }).then(function (response) {
            return response.json()
        }).then(function (json) {
            console.log(json)
        }).catch(function (err) {
            console.log({ 'status': 'failed', 'error': err })
        })
    ```

