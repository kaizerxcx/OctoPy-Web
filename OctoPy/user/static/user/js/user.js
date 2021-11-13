// A $( document ).ready() block.
$( document ).ready(function() {

  if($('#isRequested').val()=='False'){
    $("#tableRequest").hide();
    $("#noRequest").show();
  }
  else{
    $("#tableRequest").show();
    $("#noRequest").hide();
  }

  $('#requestButton').on( "click", function(e) {
    e.preventDefault();
    $("#noRequest").hide();
    $("#tableRequest").show();
      $.ajax({
          type:'POST',
          url:" ",
          data:{
          user_id: $('#user_id').val(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          action: 'requestAdmin'
          },
          success:function(json){
          location.reload();            
          },
          error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
      });
  });


     $('#logoutButton').on( "click", function(e) {
        e.preventDefault();
        console.log("clicked!");
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