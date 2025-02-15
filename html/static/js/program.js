function findRusNameByEngName(name, series) {
    for (let i = 0; i < series.length; ++i) {
        if (series[i].name == name) {
            if (series[i].name_rus != "") {
                return series[i].name_rus
            } else {
                return name
            }
        } 
    }
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
                        <div>📺 ${rusName.charAt(0).toUpperCase() + rusName.slice(1).toLowerCase()}</div>
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