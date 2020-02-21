$(document).ready(function () {


    $(document).on("click","#search_button",function () {
        $([document.documentElement, document.body]).animate({
            scrollTop: $("#result_section").offset().top
        }, 700);
    });
})