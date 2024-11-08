document.getElementById('chat-message').addEventListener('submit', function (event) {
    var message = document.getElementById('message').value.trim();
    var image = document.getElementById('image').files.length;
    var video = document.getElementById('video').files.length;

    // If no message, image, or video is provided, prevent form submission
    if (!message && !image && !video) {
        alert('Please enter a message, upload an image, or upload a video.');
        event.preventDefault();  // Prevent form submission
    }
});


$(document).ready(function () {
    $(document).on('submit', '#chat-message', function (e) {
        e.preventDefault();

        var formData = new FormData();
        formData.append('sender', $('#sender').val());
        formData.append('receiver', $('#receiver').val());
        formData.append('profile_image', $('#profile_image').val());
        formData.append('message', $('#message').val());
        formData.append('receiverId', $('#receiverId').val());
        formData.append('senderId', $('#senderId').val());

        // Append the file (make sure the input allows file uploads)
        if ($('#image')[0].files[0]) {
            formData.append('image', $('#image')[0].files[0]);
        }
        // Append the file (make sure the input allows file uploads)
        if ($('#video')[0].files[0]) {
            formData.append('video', $('#video')[0].files[0]);
        }

        // Add CSRF token (important!)
        formData.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());

        $.ajax({
            type: 'POST',
            url: '/send_chat_message',
            processData: false, // Important for file uploads
            contentType: false, // Important for file uploads
            data: formData,

            success: function (data) {
                //alert(data);
            },
            error: function (response) {
                //alert('An error occurred');
            }
        });

        // Clear the message input
        document.getElementById('message').value = '';
    });
});


$(document).ready(function () {
    setInterval(function () {

        $.ajax({
            type: 'GET',
            url: '/get_chat_message/' + $('#pks').val(),
            success: function (response) {

                $('#display-comment').empty()
                for (var key in response.messages) {


                    // Check if the image exists and is not null or empty
                    var IfImage = response.messages[key].image;
                    var imageHTML = (IfImage && IfImage.includes('.')) ? "<img src='" + IfImage + "' />" : "";

                    var IfVideo = response.messages[key].video;
                    var videoExtensions = ['.mp4', '.webm', '.ogg']; // Valid video extensions
                    var videoHTML = (IfVideo && videoExtensions.some(ext => IfVideo.includes(ext)))
                        ? "<video controls><source src='" + IfVideo + "' type='video/mp4'></video>"
                        : "";
                    if (response.messages[key].sender != $('#user').val()) {

                        var temp = "<div class='border-t pt-4' style='margin-right:auto;width:fit-content;'>" +
                            "<div class='flex'>" +
                            "<div class='w-10 h-10 rounded-full relative flex-shrink-0'>" +
                            "<img class='absolute h-full rounded-full w-full' src='" + response.messages[key].profileimage + "'/>" +
                            "</div>" +
                            "<div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20'>" +
                            "<h6><b><a href='/profile/" + response.messages[key].sender + "'>" + response.messages[key].sender + "</a></b></h6>" +
                            "<p class='leading-6'><ul>" + response.messages[key].message + "</ul></p>" +
                            "</div></div></div>" +
                            imageHTML + videoHTML;  // Append the image only if it exists

                        $('#display-comment').append(temp);

                    } else {
                        var temp = "<div class='border-t pt-4' style='margin-left:auto;width:fit-content;'>" +
                            "<div class='flex'>" +
                            "<div class='w-10 h-10 rounded-full relative'></div>" +
                            "<div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20' style='background-color:pink;'>" +
                            "<h6><b><a href='/profile/" + response.messages[key].sender + "'>You</a></b></h6>" +
                            "<p class='leading-6'><ul>" + response.messages[key].message + "</ul></p>" +
                            "</div></div></div>" +
                            imageHTML + videoHTML;  // Append the image only if it exists

                        $('#display-comment').append(temp);
                    }
                }

                function scrollToBottom() {
                    window.scrollTo(0, document.body.scrollHeight)

                }
                if (!document.body.classList.contains("active")) {
                    scrollToBottom();
                }
                document.body.onmouseenter = () => {
                    document.body.classList.add("active");
                }
                document.body.onmouseleave = () => {
                    document.body.classList.remove("active");
                }

            },
            error: function (response) {
                //alert('an error occured')
            }
        });
    }, 100)
})


window.oninput = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}
window.onclick = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}
window.onchange = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}