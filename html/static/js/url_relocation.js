function checkDomainAndChangeMarquee() {
    let currentHost = window.location.hostname;
    let oldDomain = 'foxkids-online.ru';

    if (currentHost.includes(oldDomain)) {
        let $marquee = $('#marquee-text');
        
        let $replacement = $('<div></div><img id="relocation-banner" src="static/sources/site/relocation.png" alt="Сайт переехал" style="width: 640px; height: 480px;" />')
            .attr('id', 'marquee-text')
            .addClass('blink-text')
            .html('📣ВНИМАНИЕ!!!📣 <br>САЙТ ПЕРЕЕЗЖАЕТ НА НОВЫЙ АДРЕС: 👉<a href="https://foxkids.club">FOXKIDS.CLUB</a>👈 ПЕРЕХОДИ ТУДА! <br>ДЛЯ ПОЛЬЗОВАТЕЛЕЙ ИЗ РОССИИ РЕКОМЕНДУЕТСЯ ИСПОЛЬЗОВАТЬ VPN 🛡️ <br>С 1 СЕНТЯБРЯ 2026 СТАРЫЙ АДРЕС НЕ БУДЕТ РАБОТАТЬ');
        $("#my-video").css("display", "none")
        $marquee.replaceWith($replacement);
    }
}

$(document).ready(function () {
    checkDomainAndChangeMarquee();
});