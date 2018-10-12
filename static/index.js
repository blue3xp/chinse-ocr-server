$(function(){
    $("#submit").on('click', function(){
        url = '/upload';
        var file = $('[type="file"]')[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        $.ajax({
            url: "/upload",
            type: 'POST',
            data: formData,
            timeout:300000,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                $('#message').html(data.message);
                $('#status').html(data.status);
            }
        });
        return false;
    });
});