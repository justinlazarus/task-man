$(function() {

    // Add toolbar buttons
    $(".toolbar-button").each(function() {
        $(this).button({
            text: false,
            icons: { primary: $(this).attr("icon") }
         });
    });

    // Add group header buttons
    $(".header-button").each(function() {
        $(this).button({
            text: true,
            icons: { primary: "ui-icon-suitcase" }
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

    // Add listeners
    $("#project_complete").on("click", complete_project); 
    $("#project_delete").on("click", delete_project); 
    $("#project_add").on("click", {url: "/projects/project_list"}, open_dialog);
});

function open_dialog(event) {
    //create the div that will hold the dialog box
    var projectDialog = $('#project_dialog');
    if ($('#project_dialog').length == 0) {
        projectDialog = $('<div id="project_dialog"></div>').appendTo('body');
    }

    // load the passed url into the dialog
    projectDialog.load(event.data.url);

    // create the dialog box and display it
    projectDialog.dialog({
        modal: true,
        close: function() {projectDialog.dialog("destroy");}
    });
}

function complete_project () {
    $("input:checked").each(function() {
        $.post(
            '/projects/complete/', {
                comment: "shit", model_name: "project", 
                object_id: $(this).attr('project_id') 
            }
        ).success(function() {
            $('#ui-tabs-1').load('/projects/project_list/');
        });
    });
}

function delete_project () {
    $("input:checked").each(function() {
        $.post(
            '/projects/delete/', {
                project_id: $(this).attr('project_id')
            }
        ).success(reload);
    });
}

function reload () {
    $('#ui-tabs-1').load('/projects/project_list/');
}
