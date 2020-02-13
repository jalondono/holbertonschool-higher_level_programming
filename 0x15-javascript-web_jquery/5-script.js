const addItem = $('#add_item');
const myList = $('.my_list');
const item = '<li>Item</li>';

$(document).ready(function () {
  addItem.click(function () {
    myList.append(item);
  });
});
