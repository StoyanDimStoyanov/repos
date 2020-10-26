setTimeout(function () {
    $("#mydiv").fadeOut().empty();
}, 20);

var fade_out = function() {
  $("#mydiv").fadeOut().empty();
}

setTimeout(fade_out, 20 );
$(".formSentMsg").delay(3200).fadeOut(300);
$(document).ready(function() {
    $.doTimeout(5000, function() {
    $('#mydiv').fadeOut();
    });
    });