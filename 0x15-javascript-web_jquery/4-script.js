// JavaScript script that toggles on click
const header = $('header');
$('DIV#toggle_header').click(function () {
  header.toggleClass('green red');
});
