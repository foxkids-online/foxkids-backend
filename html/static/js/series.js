$.ajax({
    type: "GET",
    dataType: "json",
    url: "/api/series/",
    complete: function (data) {
        series = data.responseJSON;
        $.map(series, function (i) {
            if (i.name_rus !== "") {
                let template = `
        <div  class="series-card">
            <div class="p-2">
                <div class="font-weight-bold text-uppercase">${i.name_rus}</div>
                <div class="text-uppercase d-flex">
                    <div>${i.year}</div>|<div>(${i.genre})</div>
                </div>
                <div class="pt-2 text-uppercase">${i.description}</div>
            </div>
            <div>
                <div id="${i.name}" class="series-card-logo"></div>
            </div>
        </div>
        `

                $('#series').append(template);
                $(`#${i.name}`).css('background-image', `url('./static/sources/series/${i.name}.png')`)
            }
        })
    }
})