 function letterOnly (e) {  // Accept only alpha numerics, no special characters 
      var regex = new RegExp("[a-zA-Z]");
      var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
      if (regex.test(str)) {
          return true;
      }
  
      e.preventDefault();
      return false;
  }
    