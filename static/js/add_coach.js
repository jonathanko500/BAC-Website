// add_coach.js
$(document).ready(function() {
    $("#add-coach-form").submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var url = form.attr("data-action");
        $.ajax({
            type: "POST",
            url: url,
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function(data) {
                // Handle success, such as updating the coach list
                console.log("Coach added successfully.");
                // You might want to refresh the list or update the UI
            },
            error: function(error) {
                console.error("Error adding coach: " + error.responseText);
                // Handle error, show a message to the user, etc.
            }
        });
    });
});
