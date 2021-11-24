/* Project specific Javascript goes here. */

$(document).ready(function() {
    $('.btn-cart').on('click', function(e){
        e.preventDefault();
        console.log("fucking shit is gets executed")
        $.ajax({
            method: "GET",
            url: $(this).attr("href"),
            dataType: 'json',
            success: function (data) {
                console.log("ajax is completed")
                if (data) {
                   console.log(data.success)
                }
            }
        });
    })
})
