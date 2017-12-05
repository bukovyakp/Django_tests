
$(document).ready(function () {

    $(document).foundation();
/* Простая функция для теста работы AJAX */
    $("#test").click(function()
    {
        $.ajax({
                type:"GET",
            url:"/ajax/ajax_test/",
            cache: false,
            success: function(data){
                $('#target').html(data.param1 + ' ' + data.param2
                                  + ' Login is: ' + data.param3
                                  + '. Has id: ' + data.param4);
                $('#Login').html(' Login is: ' + data.param3);
            }
            });

    });

/* Вернуть все активные заказы пользователя */
    $("#get_all_orders").click(function()
        {
            $.ajax({
                    type:"GET",
                url:"/ajax/get_all_orders/",
                cache: false,
                success: function(data){
                    $('#all_orders').html(data.all_orders);
                }
                });

        });

});