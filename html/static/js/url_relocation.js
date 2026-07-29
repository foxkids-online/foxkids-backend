function checkDomainAndChangeMarquee() {
    let currentHost = window.location.hostname;
    let oldDomain = 'foxkids-online.ru';

    if (currentHost.includes(oldDomain)) {
        let $marquee = $('#marquee-text');
        
        let $replacement = $('<div></div>')
            .attr('id', 'marquee-text')
            .addClass('blink-text')
            .html('📣ВНИМАНИЕ!!!📣 <br>САЙТ ПЕРЕЕЗЖАЕТ НА НОВЫЙ АДРЕС: 👉<a href="https://foxkids.club">FOXKIDS.CLUB</a>👈 ПЕРЕХОДИ ТУДА! <br>С 1 СЕНТЯБРЯ 2026 СТАРЫЙ АДРЕС НЕ БУДЕТ РАБОТАТЬ');
        
        $marquee.replaceWith($replacement);
    }
}

$(document).ready(function () {
    checkDomainAndChangeMarquee();
});