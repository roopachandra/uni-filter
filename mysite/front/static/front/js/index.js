require('@claviska/jquery-dropdown/jquery.dropdown.css');
require('../css/index.scss');
require('@claviska/jquery-dropdown/jquery.dropdown');

$(document).ready(() => {
  $('.jq-dropdown').on('show', (event) => {
    $(`[data-jq-dropdown="#${event.target.id}"]`).addClass('active');
  }).on('hide', (event) => {
    $(`[data-jq-dropdown="#${event.target.id}"]`).removeClass('active');
  });
  $('.jq-dropdown').on('click', '.jq-dropdown-menu a', (e) => {
    const $elem = $(e.target);
    const id = $elem.parents('.jq-dropdown').attr('id');
    $(`[data-jq-dropdown="#${id}"]`).html($elem.html());
  });
});
