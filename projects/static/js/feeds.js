$(function() {
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

    // Add order by buttons
    $("#feed-duedate").button({
        text: false,
        icons: {
            primary: getIcon('duedate')
       }
    });
    $("#feed-user").button({
        text: false,
        icons: {
            primary: getIcon('user')
       }
    });
    
    $("#feed-type").button({
        text: false,
        icons: {
            primary: getIcon('content-type')
       }
    });

    // Add buttonset
    $("#feed-order").buttonset();

    function reloadFeeds(event) {
        $('.ui-tabs-panel:not(.ui-tabs-hide)').load('/projects/feeds/', {order: event.data.order});   
    }

    // Add event listeners to order by buttons
    $(".feed-order-button").each(function() { 
        $(this).on("click", {order: $(this).attr("order")}, reloadFeeds); 
    });

    // Add action buttons
    $(".feed-entry-action").each(function() {
        var action = $(this).attr("action");
        var type = $(this).attr("type");

        $(this).button({
            text: false,
            icons: {
                primary: getIcon(action),
                secondary: getIcon(type)  
            }
        });
    });

    // Add group header buttons
    $(".group-header").each(function() {
        var order = $(this).attr("order");
        var icon = getIcon(order);

        $(this).button({
            text: true,
            icons: {
                primary: icon
            }
        });
    });
});
