(function(){
    $(document).foundation();

    _post_api_url         = '/post';

    $new_post_form        = $('#new_post');
    $new_post_container   = $('.posts');
    _new_post_field       = '.post__new_post';
    _new_post__size_limit = 140;

    var $make_request = function (URL, METHOD, DATA, CALLBACK) {

        fetch(URL, {
            method  : METHOD,
            credentials : 'same-origin',
            headers : {
                'Accept'       : 'application/json',
                'Content-Type' : 'application/json'
            },
            body    : JSON.stringify(DATA)
        }).then(function (response) {
            return response.json()
        }).then(function (json) {
            CALLBACK(json)
        }).catch(function (err) {
            CALLBACK({'status': 'failed', 'error': err})
        })
    }

    var $api = {
        'get' : function (ID, CALLBACK) {
            _URL = _post_api_url;
            if(ID && typeof ID === 'number')
                _URL += '/' + ID;

            $make_request(_URL, 'GET', undefined, CALLBACK);
        },

        'add' : function (DATA, CALLBACK) {
            $make_request(_post_api_url, 'POST', DATA, CALLBACK);
        },


        'update' : function (ID, DATA, CALLBACK) {
            if (typeof ID !== 'number' || !DATA){
                // throw Error
                console.log('ID is no set');
            } else {
                _URL = _post_api_url + '/' + ID;
                $make_request(_URL, 'PUT', DATA, CALLBACK);
            }
        },

        'delete' : function (ID, CALLBACK) {
            if (typeof ID !== number){
                // throw Error
                console.log('ID is no set');
            } else {
                _URL = _post_api_url + '/' + ID;
                $make_request(_URL, 'DELETE', {}, CALLBACK);
            }
        }
    }

/* ----- Templates ----- */
    var $render = {
        'post' : function (data) {
            return '<article class="row medium-6 large-6 columns post">'
                    +    '<header>'
                    +        '<h1 class="post__header"><a href="#">Bob Tester</a> | ' + data.timestamp + '</h1>'
                    +    '</header>'
                    +    '<section>'
                    +        '<p class="post__content">' + data.text + '</p>'
                    +    '</section>'
                    + '</article>'; 
        }
    }
/* ----- Templates end----- */



/* ----- Handlers ----- */

    $new_post_form.submit(function (event) {
        event.preventDefault();
        var content = $(_new_post_field, this).val();

        if(content && content.length <= _new_post__size_limit)
            $api.add({'text': content}, (data) => console.log(data));
    })

    $api.get(undefined, function (posts) {
        console.log('LOL', posts)
        for(var i = 0; i < posts.length; i++)
            $new_post_container.append($render.post(posts[i]));
    })
})()
