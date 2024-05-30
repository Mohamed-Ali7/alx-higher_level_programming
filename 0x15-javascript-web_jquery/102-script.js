$(document).ready(function () {
  $('#btn_translate').click(() => {
    const lang = {
      lang: $('#language_code').val()
    };
    $.get('https://hellosalut.stefanbohacek.dev/', lang,
      (data) => {
        $('#hello').text(data.hello);
      });
  });
});
