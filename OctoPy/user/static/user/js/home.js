// A $( document ).ready() block.
$( document ).ready(function() {
   
    $("#registerSpinner").hide();

    $('#registeredSuccessAlert').hide();

    $('#loginFailedAlert').hide();

    $('#loginSpinner').hide();

    // $('#modalLRFormDemo').modal('show')

    $('#login').on( "click", function() {
      $('#modalLRFormDemo').modal('show')
    });

    $('#cancel').on( "click", function() {
      $('#modalLRFormDemo').modal('hide')
    });

    $('#cancel2').on( "click", function() {
      $('#modalLRFormDemo').modal('hide')
    });

    $('#signupButton').on( "click", function() {
      $('#registerTab').trigger("click");
    });

    $('#loginButton').on( "click", function() {
      $('#loginTab').trigger("click");
    });

    // $('#registerButton').on( "click", function() {
    //   $('#registerSpinner').show();
    //   $('#registerForm').hide();
    // });

    // $('#loginButtonForm').on( "click", function() {
    //     $('#loginSpinner').show();
    //     $('#loginForm').hide();
    //   });


$(document).on('submit', '#registerForm',function(e){
  e.preventDefault();
  $('#registerSpinner').show();
  $('#registerForm').hide();
  console.log("submitted");
    $.ajax({
        type:'POST',
        url:" ",
        data:{
        firstname : $('#firstname').val(),
        lastname : $('#lastname').val(),
        username: $('#username').val(),
        password: $('#password').val(),
        age: $('#age').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        action: 'registerUser'
        },
        success:function(json){
          $('#loginTab').trigger("click");
          $('#registeredSuccessAlert').show();
          $('#loginUsername').val(json.username); 
          $('#registerSpinner').hide();
          $('#registerForm').show();
          document.getElementById("registerForm").reset();
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});
      
$(document).on('submit', '#loginForm',function(e){
  e.preventDefault();
  $('#loginSpinner').show();
  $('#loginForm').hide();
  $('#loginFailedAlert').hide();
  console.log("submitted");
    $.ajax({
        type:'POST',
        url:" ",
        data:{
        username: $('#loginUsername').val(),
        password: $('#loginPassword').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        action: 'loginUser'
        },
        success:function(json){
          console.log(json);
          $('#registeredSuccessAlert').hide();
          if (json.status == -1) {
            $('#loginFailedAlert').show();
            $('#loginSpinner').hide();
            $('#loginForm').show();
          }
          if (json.status == 0){
            window.location.replace("user");
          }
          if (json.status == 1){
            window.location.replace("administrator");
          }
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});



});