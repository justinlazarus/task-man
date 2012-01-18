$(function() {
    // Add action buttons
    $("#add").button({
        text: false,
        icons: {
            primary: "ui-icon-plus"
       }
    });    
    $("#delete").button({
        text: false,
        icons: {
            primary: "ui-icon-cancel"
       }
    });
    $("#comment").button({
        text: false,
        icons: {
            primary: "ui-icon-comment"
       }
    });
    $("#complete").button({
        text: false,
        icons: {
            primary: "ui-icon-check"
       }
    });

    // Add order buttons
    $("#user").button({
        text: false,
        icons: {
            primary: "ui-icon-person"
       }
    });    
    $("#duedate").button({
        text: false,
        icons: {
            primary: "ui-icon-clock"
       }
    });
    $("#project").button({
        text: false,
        icons: {
            primary: "ui-icon-suitcase"
       }
    });
    $("#milestone").button({
        text: false,
        icons: {
            primary: "ui-icon-folder-open"
       }
    });

    // Add grouping buttons
    $(".group-user").each(function() {
        $(this).button({
            text: true,
            icons: {
                primary: "ui-icon-person"
            }
        });
    });

    // Set up buttonsets
    $("#order").buttonset();
    $("#actions").buttonset();

    // Add checkboxes
    $(".list-check").each(function() {
        $(this).button();
    });


});
