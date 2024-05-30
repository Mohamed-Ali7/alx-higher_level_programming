$(document).ready(function () {
  function fetchHello () {
    const lang = {
      lang: $('#language_code').val()
    };
    $.get('https://hellosalut.stefanbohacek.dev/', lang,
      (data) => {
        $('#hello').text(data.hello);
      });
  }
  $('#btn_translate').click(fetchHello);
  $('#language_code').keypress((event) => {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
