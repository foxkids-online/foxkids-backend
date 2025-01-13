function findRusNameByEngName(name, series) {
    for (let i = 0; i < series.lenght; ++i) {
        if (series[i].name == name) {
            return series[i].name_rus
        }
    }
    return name
}

function getProgram() {
    $.when(
        $.ajax({
            type: "GET",
            dataType: "json",
            url: "/api/series/",
            success: function (data) { return data.responseJSON }
        }),
        $.ajax({
            type: "GET",
            dataType: "json",
            url: "/api/block/",
            data: { "weekday": new Date().getDay() - 1 },
            success: function (data) { return data.responseJSON }
        })).then(function (series, blocks) {
            series = series[0]
            blocks = blocks[0]
            for (let i = 0; i < blocks.length; ++i) {
                let series_list = blocks[i].series_list

                $('#modal-panel').append(`
                    <br/>
                    <div class="font-weight-bold">Блок: ${blocks[i].name}</div>
                <br/>`)

                for (let j = 0; j < series_list.length; ++j) {
                    let rusName = findRusNameByEngName(series_list[j], series)
                    $('#modal-panel').append(`
                        <div>📺 ${rusName}</div>
                    `)
                }
            }
        }
        )
}

$(document).ready(function () {
    $('#program-button').click(function () {
        getProgram();
        $(".modal-wrapper").show()
    })
})

$(document).ready(function () {
    $('#close-program-modal').click(function () {
        $(".modal-wrapper").css("display", "none")
    })
})