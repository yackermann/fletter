**Post API Documentation**
---

* **Contents**
    * [Get all posts](#get-posts)
    * [Get post specified by ID](#get-post)
    * [Add new post](#add-new-post)
    * [Edit post specified by ID]()
    * [Delete post specified by ID]()
    
**Get posts**
----
Returns json data of all posts.

* **URL**

    * /post/

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
    ```

