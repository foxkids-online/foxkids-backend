
setInterval(function () {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: "/api/current_promo/",
        complete: function (data) {

            data = data.responseJSON;
            let current_series = data.current_series
            let next_series = data.next_series
            if (current_series) {
                $('#promo-now-txt').text(current_series.name_rus);
                $('#promo-now-img').css('background-image', `url('./static/sources/promos/${current_series.name}.png')`);
            }
            if (next_series) {
                $('#promo-next-txt').text(next_series.name_rus);
                $('#promo-next-img').css('background-image', `url('./static/sources/promos/${next_series.name}.png')`);
            }
        }
    })
}, 10000)

