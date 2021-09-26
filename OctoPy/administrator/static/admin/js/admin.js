// A $( document ).ready() block.
$( document ).ready(function() {
    $('#logoutButton').on( "click", function(e) {
      e.preventDefault();
      console.log("click");
        $.ajax({
            type:'POST',
            url:" ",
            data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'logout'
            },
            success:function(json){
              console.log(json);
              if(json.status == 1){
                  window.location.replace("logout");
              }
            },
            error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        });
    });

});