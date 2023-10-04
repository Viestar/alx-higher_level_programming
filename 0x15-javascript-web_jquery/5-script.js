// JavaScript script that toggles on click
const header = $('header');
$('DIV#add_item').click(function () {
  header.toggleClass('green red');
});
