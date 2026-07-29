function checkDomainAndSetStream() {
    let currentHost = window.location.hostname;
    let currentProtocol = window.location.protocol; // Получим 'http:' или 'https:'
    let streamPath = '';

    // Определяем базовый путь к стриму в зависимости от домена сайта
    if (currentHost === 'foxkids.club' || currentHost === 'www.foxkids.club') {
        streamPath = 'stream.foxkids.club/hls/test/index.m3u8';
        console.log("Плеер: Включен поток НОВОГО домена без прокси");
    } else {
        streamPath = 'foxkids-online.ru/hls/test/index.m3u8';
        console.log("Плеер: Включен поток СТАРОГО домена");
    }

    // Собираем правильную итоговую ссылку: например, https://stream.foxkids.club/...
    let fullStreamUrl = currentProtocol + '//' + streamPath;
    console.log("Итоговая ссылка на поток:", fullStreamUrl);

    // Заряжаем ссылку в Video.js
    videojs('my-video').src({
        src: fullStreamUrl,
        type: 'application/x-mpegURL'
    });
}

$(document).ready(function () {
    setTimeout(checkDomainAndSetStream, 100);
});