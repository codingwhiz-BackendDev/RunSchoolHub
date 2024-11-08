$(document).ready(function () {
    $(document).on('submit', '#group-comment', function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: '/group_chat_comment',
            data: {
                name: $('#name').val(),
                ids: $('#ids').val(),
                profile_image: $('#profile_image').val(),
                comment: $('#comment').val(),
                group_name: $('#group_name').val(),
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
    setInterval(function () {

        $.ajax({
            type: 'GET',
            url: '/get_group_comments/' + $('#pks').val(),
            success: function (response) {

                $('#display-comment').empty()
                for (var key in response.comments) {
                    if (response.comments[key].name != $('#user').val()) {
                        var temp = "<div class='border-t pt-4' style='margin-right:auto;width:fit-content;'><div class='flex'><div class='w-10 h-10 rounded-full relative flex-shrink-0'><img class='absolute h-full rounded-full w-full' src = " + response.comments[key].profileimage + "/></div><div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20'><h6><b><a href =" +
                            '/profile/' + response.comments[key].name + " > " + response.comments[key].name + "</a></b ></h6 > <p class='leading-6'><ul>" + response.comments[key].comment + "</ul></div></div ></div > "
                        $('#display-comment').append(temp)
                    } else {
                        var temp = "<div class='border-t pt-4' style='margin-left:auto;width:fit-content;'><div class='flex'><div class='w-10 h-10 rounded-full relative'></div><div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20' style='background-color:pink;'><h6><b><a href =" +
                            '/profile/' + response.comments[key].name + " > " + 'You' + "</a></b ></h6 > <p class='leading-6'><ul>" + response.comments[key].comment + "</ul></div></div ></div > "
                        $('#display-comment').append(temp)
                    }
                }
                
            },
            error: function (response) {
                //alert('an error occured')
            }
        });
    }, 100)
})
document.addEventListener("click", function () {
    window.scrollTo(0, document.body.scrollHeight)
})