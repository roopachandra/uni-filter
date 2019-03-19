require('../css/list.scss');

$(document).ready(() => {
  $('.school-list').on('click', '.school-name', (e) => {
    $(e.target).parent().toggleClass('show-program');
  });
  $('.j-collapse-all').on('click', () => {
    $('.show-program').removeClass('show-program');
  });
  $('.j-expand-all').on('click', () => {
    $('.school-item ').addClass('show-program');
  });
});
