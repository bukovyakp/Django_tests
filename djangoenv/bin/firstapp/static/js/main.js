$(document).ready(function(){
	  $("#request").click(function(event){
	   	    $.ajax({
          url: "AJAX_POST_URL",
          type: "POST",
          data : {name:"ravi",age:"31"},
              success: function(result)
              {
    alert(result);
              },
              error: function (result)
              {
    alert("Заказ не принят");
              }
        });
	  });
	});