$(document).ready(function () {
    $(document).on('submit', '#like-post', function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: '/like-post',
            data: {
                name: $('#name').val(),
                ids: $('#ids').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                document.getElementById('display').innerHTML = response + ' likes'
            },
            error: function (response) {
                alert('an error occured')
            }
        })
    })
})

// $(document).ready(function () {
//     $(document).on('submit', '#favourites', function (e) {
//         e.preventDefault()
//         $.ajax({
//             type: 'POST',
//             url: '/favourite_post',
//             data: {
//                 name: $('#name').val(),
//                 ids: $('#ids').val(),
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             success: function (response) {
//                 // document.getElementById('display-follow').value = response
//                 alert(response)

//             },
//             error: function (response) {
//                 alert('an error occured')
//             }
//         })
//     })
// })

$(document).ready(function () {
    $(document).on('submit', '#comment-form', function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: '/comment',
            data: {
                name: $('#name').val(),
                ids: $('#ids').val(),
                profile_image: $('#profile_image').val(),
                comment: $('#comment').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                // document.getElementById('display-comment').innerHTML = response
                // alert(response)
            },
            error: function (response) {
                alert('an error occured')
            }
        })
        document.getElementById('comment').value = ''
    })
})

$(document).ready(function () {
    $(document).on('submit', '#follow-form', function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: '/follow',
            data: {
                follower: $('#follower').val(),
                user: $('#user').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                document.getElementById('display-follow').value = response

            },
            error: function (response) {
                alert('an error occured')
            }
        })
    })
})



