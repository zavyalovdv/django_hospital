document.addEventListener("DOMContentLoaded", function(event) {
  let critical_status = document.querySelectorAll("option > select");
  if (critical_status.value == 'критическое'){
      critical_status.style = 'color: red';
  }
  console.log('Hi from Django');
});

//.style = 'color : red';