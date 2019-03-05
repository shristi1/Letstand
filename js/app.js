$(function(){
  $("#header").load("partials/header.html");
  $("#footer").load("partials/footer.html");
});

$(function(){
  $("#header").load("partials/header.html");
  $("#footer").load("partials/footer.html");
  // parameters: service_id, template_id, template_parameters
  emailjs.send("gmail","template_5SC1hKhO",
             {name: "James", notes: "Check this out!"});
  emailjs.sendForm(gmail","template_5SC1hKhO","my_form");

});




