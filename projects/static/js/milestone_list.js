$(function() {

    // Add toolbar buttons
    $(".toolbar-button").each(function() {
        $(this).button({
            text: false,
            icons: {
                primary: $(this).attr("icon") 
            }
         });
    });

    // Add group header buttons
    $(".header-button").each(function() {
        $(this).button({
            text: true,
            icons: {
                primary: "ui-icon-folder-open"
            }
        });
    });

    // Set up buttonsets
    $(".toolbar-buttonset").each(function() {
        $(this).buttonset();
    });

    // Add checkboxes
    $(".list-check").each(function() {
        $(this).button();
    });
});
