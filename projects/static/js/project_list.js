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
                primary: "ui-icon-suitcase"
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

    // Add complete listener
    $("#project_complete").on("click", complete); 
});

function complete () {
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
