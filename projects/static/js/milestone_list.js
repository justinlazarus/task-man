$(function() {

    // Add action buttons
    $(".toolbar-button").each(function() {
        $(this).button({
            text: false,
            icons: {
                primary: $(this).attr("icon") 
            }
         });
    });

    // Add grouping buttons
    $(".header-button").each(function() {
        $(this).button({
            text: true,
            icons: {
                primary: "ui-icon-flag"
            }
        });
    });

    // Set up buttonsets
    $(".toolbar-buttonset").each(function() {
        $(this).buttonset();
    });
});
