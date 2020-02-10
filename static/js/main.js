$(document).ready(function () {
    var start_date = new Date();
    var end_date = new Date();
    end_date.setDate(end_date.getDate() + 5);
    $('#start_date .date, #end_date .date').datepicker({
        startDate: start_date,
        endDate: end_date,
        language: "ja",
        autoclose: true,
        todayHighlight: true
    });

    $(document).on("click","#search_button",function () {
        $([document.documentElement, document.body]).animate({
            scrollTop: $("#result_section").offset().top
        }, 700);
    });
})