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

function getIcon (type) {
    switch(type) {
        case "added": icon = "ui-icon-plus"; break;
        case "removed": icon = "ui-icon-cancel"; break;
        case "modified": icon = "ui-icon-wrench"; break;
        case "duedate": icon = "ui-icon-clock"; break;
        case "user": icon = "ui-icon-person"; break;
        case "project": icon = "ui-icon-suitcase"; break;
        case "milestone": icon = "ui-icon-folder-open"; break;
        case "task": icon = "ui-icon-document"; break;
        case "comment": icon = "ui-icon-comment"; break;
        case "completion": icon = "ui-icon-check"; break;
        case "content-type": icon = "ui-icon-copy"; break;
        case "impact statement": icon = "ui-icon-alert"; break;
    }
    return icon;
}


