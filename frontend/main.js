$(document).ready(function () {

    changeButText = function(el, e) {
        if ($(el).text() == 'Delete') {

            $(el).parent().parent().parent().parent().remove();
        }

        $(el).parent().parent().find('button').text(el.innerText);
    };

    addNext = function (butt) {

        var elToCopy = $(butt).parent().parent().parent().next();
        var el = elToCopy.clone();
        el.removeClass('hidden');
        elToCopy.after(el);
    };

    addAnother = function (butt) {
        var elToCopy = $(butt).parent().parent().next();
        var el = elToCopy.clone();
        el.removeClass('hidden');
        elToCopy.after(el);
    };

    removeAnother = function (butt) {
        $(butt).parent().parent().remove();
    };

    rmPhoto = function (butt) {
        $(butt).parent().find("input").val("");
        $(butt).parent().find("img").attr('src', "");
    };

    $('.go-to').click(function(){
      window.open("https://yandex.ru/maps/");
      return false;
    });

    $('.go-any').click(function(){
      window.open("#");
      return false;
    });



    $(".add-comment").click(function (e) {
        prompt("Комментарий к адресу:")
    });


    function readURL(input) {

      if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
          $('#photo-img').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
      }
    }

    $('.person').change(function () {
        var name = "";

        $('.person').each(function (index) {
            name += $(this).val() + " ";
        });

        $('#name').text(name.slice(0, -1));
    });

    $("#photo-input").change(function() {
      readURL(this);
    });
});