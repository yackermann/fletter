**Get Post**
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
        $.ajax({
            url: "/post/1",
            dataType: "json",
            type : "GET",
            success : function(response) {
                console.log(response);
            }
        });
    ```