function checkDomainAndSetStream() {
    let currentHost = window.location.hostname;
    let fullStreamUrl = '';

    if (currentHost === 'foxkids.club' || currentHost === 'www.foxkids.club') {
        fullStreamUrl = 'https://foxkids.club/hls/test/index.m3u8';
        console.log("Плеер: Включен поток НОВОГО домена");
    } 
    else {
        fullStreamUrl = 'https://foxkids-online.ru/hls/test/index.m3u8';
        console.log("Плеер: Включен поток СТАРОГО домена");
    }

    videojs('my-video').src({
        src: fullStreamUrl,
        type: 'application/x-mpegURL'
    });
}

$(document).ready(function () {
    setTimeout(checkDomainAndSetStream, 100);
});