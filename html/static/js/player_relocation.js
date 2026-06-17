function checkDomainAndSetStream() {
    let currentHost = window.location.hostname;
    let currentProtocol = window.location.protocol; // Получаем текущий протокол (http: или https:)
    let streamBaseUrl = '';

    // Определяем базовый путь в зависимости от домена
    if (currentHost === 'foxkids.club' || currentHost === 'www.foxkids.club') {
        streamBaseUrl = '//foxkids.club/hls/test/index.m3u8';
        console.log("Плеер: Включен поток НОВОГО домена");
    } 
    else {
        streamBaseUrl = '//foxkids-online.ru/hls/test/index.m3u8';
        console.log("Плеер: Включен поток СТАРОГО домена");
    }

    // Собираем итоговую ссылку с текущим протоколом
    let fullStreamUrl = currentProtocol + streamBaseUrl;

    videojs('my-video').src({
        src: fullStreamUrl,
        type: 'application/x-mpegURL'
    });
}

$(document).ready(function () {
    setTimeout(checkDomainAndSetStream, 100);
});