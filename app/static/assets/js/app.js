(function(){
    $(document).foundation();

    _post_api_url         = '/post';

    $new_post_form        = $('#new_post');
    $new_post_container   = $('.posts');
    _new_post_field       = '.post__new_post';
    _new_post__size_limit = 140;

    _post_delete_button             = '.post__post_delete_button';
    _post_delete_button_confirm     = '.post__confirm_delete_post';
    _post_delete_confirmation_modal = '#confmodal'

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
            if (typeof ID !== 'number'){
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
            return '<article data-id="' + data.id + '" id="post-id-' + data.id + '" class="row medium-6 large-6 columns post">'
                    +    '<header>'
                    +        '<h1 class="post__header"><a href="#">Bob Tester</a> | ' 
                    + data.timestamp + '<span class="post__header_spacer"></span>'
                    +        '<a href="#" class="post__post_delete_button" title="Delete post">X</a></h1>'
                    +    '</header>'
                    +    '<section>'
                    +        '<p class="post__content">' + data.text + '</p>'
                    +    '</section>'
                    + '</article>'; 
        },

        'delete_modal' : function (id, text) {
            return     '<h2 class="lead">Are you sure you want to delete this post?</h2>'
                    +  '<p class="post__delete_modal_confirmation_text">' + text + '</p>'
                    +  '<a href="#" class="alert button post__confirm_delete_post" data-id="' + id + '" data-close>Delete post</a>'
                    +  '<a href="#" class="success button" data-close>Cancel</a>'
                    +  '<button class="close-button" data-close aria-label="Close reveal" type="button">'
                    +      '<span aria-hidden="true">&times;</span>'
                    +  '</button>'
        }
    }
/* ----- Templates end----- */



/* ----- Handlers ----- */

    $new_post_form.submit(function (event) {
        event.preventDefault();
        var input   = $(_new_post_field, this);
        var content = input.val();

        if(content && content.length <= _new_post__size_limit){
            $api.add({'text': content}, function (response) {
                if (response.status === 'ok') {
                    input.val('');
                    $new_post_container.append($render.post(response.post));
                }
            });
        }
    })

    $(document).on('click', _post_delete_button, function (e) {
        var $parent = $(this.closest('.post'));
        var id      = $parent.data('id');
        var text    = $parent.find('.post__content').text();
        $(_post_delete_confirmation_modal).html($render.delete_modal(id, text)).foundation('open');
    })

    $(document).on('click', _post_delete_button_confirm, function (e) {
        var id = $(this).data('id');
        $api.delete(id, function (response) {
            if (response.status === 'ok') 
                $('post-id-' + id).remove();
        })
    })

    $api.get(undefined, function (response) {
        if(response.status === 'ok')
            for(var i = 0; i < response.posts.length; i++)
                $new_post_container.append($render.post(response.posts[i]));
    })
})()
