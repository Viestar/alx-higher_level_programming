// JavaScript script that adds a  on click
const header = $('UL.my_list');
$('DIV#add_item').click(function () {
  header.append('<li>Item</li>');
});
