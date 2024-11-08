$(document).ready(function () {
    setInterval(function () {

        $.ajax({
            type: 'GET',
            url: '/getComments/' + $('#pks').val(),
            success: function (response) {

                $('#display-comment').empty()
                for (var key in response.comments) {
                    // var temp = "<div class='border-t pt-4 space-y-4'><ul>" + response.comments[key].comment + "</ul><img class='absolute h-full rounded-full w-full'" + "/>" + response.comments[key].profileimage + "<b>" + response.comments[key].name + "</b> </div>";
                    var temp = "<div class='border-t pt-4 space-y-4'><div class='flex'><div class='w-10 h-10 rounded-full relative flex-shrink-0'><img class='absolute h-full rounded-full w-full' src = " + response.comments[key].profileimage + "/></div><div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20'><h6><b><a href =" +
                        '/profile/' + response.comments[key].name + " > " + response.comments[key].name + "</a></b ></h6 > <p class='leading-6'><ul>" + response.comments[key].comment + "</ul></div></div ></div > "
                    $('#display-comment').append(temp)
                }
                //alert(response.comments[key].comment)
            },
            error: function (response) {
                //alert('an error occured')
            }
        });
    }, 100)
})


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