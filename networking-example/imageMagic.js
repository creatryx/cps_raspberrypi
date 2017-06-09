// this file needs to be placed in the directory one level down from your main Flask file!

$(function() {

    // reload period in seconds
    var reloadPeriod = 60;

    var count = $("#counter").attr("count");

    for (var i = 0; i < count; i++) {
        $("img#" + i).hide();
    }

    var currentIndex = 0;

    setInterval(
        function() {

            if (currentIndex >= count) {
                currentIndex = 0;
            }
            var nextImageURL = $("img#" + currentIndex).attr('src');
            $('#current').attr('src', nextImageURL)

            currentIndex++;

        }, 100);

    setInterval(
        function() {
            location.reload();
        }, reloadPeriod * 1000);

});
