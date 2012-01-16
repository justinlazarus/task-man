$(function() {
    $("#nav-tabs").tabs({
    });

    // Add action buttons
    $("#global-project").button({
        text: true,
        disabled: true,
        icons: {
            primary: "ui-icon-suitcase"
       }
    });    
    $("#global-budgets").button({
        text: true,
        icons: {
            primary: "ui-icon-calculator"
       }
    });
    $("#global-users").button({
        text: true,
        icons: {
            primary: "ui-icon-person"
       }
    });
});
