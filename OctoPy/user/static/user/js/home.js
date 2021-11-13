// A $( document ).ready() block.
$( document ).ready(function() {
   

    $("#registerSpinner").hide();

    $('#registeredSuccessAlert').hide();

    $('#loginFailedAlert').hide();

    $('#loginSpinner').hide();

    $('#modalLRFormDemo').modal('show')

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
function isValid(username, email, password){
    flag = true;
    $.ajax({
      async: false,
      type:'POST',
      url:" ",
      data:{
      username: $('#username').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      action: 'checkUsername'
      },
      success:function(json){
        if (json.status == 1){
          $('#username').toggleClass("is-invalid")
          flag = false;
        }
      },
      error : function(xhr,errmsg,err) {
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
  }});

  var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
  
  if (testEmail.test(email)){
        $.ajax({
          async: false,
          type:'POST',
          url:" ",
          data:{
          email: $('#email').val(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          action: 'checkEmail'
          },
          success:function(json){
            if (json.status == 1){
              $('#email').toggleClass("is-invalid");
              $('#emailLabel').text("Email Address is Already Taken");
              flag = false;
            }
          },
          error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }});
  }
  else
  {
    $('#email').toggleClass("is-invalid");
    $('#emailLabel').text("Email Address is invalid");
    flag = false;
  }
 
 var testPassword = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
 if(!testPassword.test(password))
 {
  $('#password').toggleClass("is-invalid");
  flag = false;
 }
 

  return flag;

}

$(document).on('submit', '#registerForm',function(e){
  e.preventDefault();
  
  // console.log(isValid($('#username').val(), $('#email').val(), $('#password').val()));
  if(isValid($('#username').val(), $('#email').val(), $('#password').val()))
  {
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
            email: $('#email').val(),
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
  }
 
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