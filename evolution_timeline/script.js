const timeline = document.querySelector('.timeline');
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');
const captionText = document.getElementById('caption');

const timelineData = [
    {
        date: "~3,8 milliárd évvel ezelőtt",
        title: "Egysejtű élet megjelenése",
        text: "Az élet alapja, önálló sejtek kialakulása.",
        image: "https://i.imgur.com/O5Q0h4a.png"
    },
    {
        date: "~1,5 milliárd évvel ezelőtt",
        title: "Többsejtűség",
        text: "Sejtek összekapcsolódnak, specializált szövetek alakulnak ki.",
        image: "https://i.imgur.com/sWJ4FfT.png"
    },
    {
        date: "~525 millió évvel ezelőtt",
        title: "Gerinchúros állatok",
        text: "Az első állatok, amelyeknél megjelenik a gerincoszlop előfutára (notochorda).",
        image: "https://i.imgur.com/yA4Y0o7.png"
    },
    {
        date: "~420 millió évvel ezelőtt",
        title: "Állkapocs megjelenése",
        text: "Lehetővé teszi a hatékony táplálékfelvételt és új tápláléki niche-eket.",
        image: "https://i.imgur.com/4pZ8iY3.png"
    },
    {
        date: "~400 millió évvel ezelőtt",
        title: "Tüdő és kopoltyúk fejlettebb formái",
        text: "A vízi és szárazföldi élethez való alkalmazkodás.",
        image: "https://i.imgur.com/sJ3G32E.png"
    },
    {
        date: "~360 millió évvel ezelőtt",
        title: "Végtagok kialakulása",
        text: "Az első gerincesek elkezdik meghódítani a szárazföldet.",
        image: "https://i.imgur.com/fg3sV3S.png"
    },
    {
        date: "~200 millió évvel ezelőtt",
        title: "Emlős jellegzetességek",
        text: "Melegvérűség, szőrzet, tejmirigyek kialakulása.",
        image: "https://i.imgur.com/gJ3f047.png"
    },
    {
        date: "~100 millió évvel ezelőtt",
        title: "Nagy agytérfogat és fejlett érzékszervek",
        text: "Fokozott tanulási képesség és komplex viselkedés.",
        image: "https://i.imgur.com/5aN2z2g.png"
    },
    {
        date: "~6 millió évvel ezelőtt",
        title: "Bipedalizmus",
        text: "Az emberi vonalban az Australopithecusoknál kezdődik.",
        image: "https://i.imgur.com/4s2k1wW.png"
    },
    {
        date: "~300 000 évvel ezelőtt",
        title: "Homo sapiens komplex agya",
        text: "Nyelv, kultúra, technológia kialakulása, ami a modern emberre jellemző.",
        image: "https://i.imgur.com/8z2Z3jE.png"
    }
];

timelineData.forEach(item => {
    const timelineItem = document.createElement('div');
    timelineItem.classList.add('timeline-item', 'clearfix');

    const timelineContent = document.createElement('div');
    timelineContent.classList.add('timeline-content');

    const date = document.createElement('h2');
    date.textContent = item.date;

    const title = document.createElement('h3');
    title.textContent = item.title;

    const text = document.createElement('p');
    text.textContent = item.text;

    const imgContainer = document.createElement('div');
    imgContainer.classList.add('timeline-img-container');

    const img = document.createElement('img');
    img.classList.add('timeline-img');
    img.src = item.image;
    img.alt = item.title;

    imgContainer.appendChild(img);

    timelineContent.appendChild(date);
    timelineContent.appendChild(title);
    timelineContent.appendChild(text);
    timelineContent.appendChild(imgContainer);

    timelineItem.appendChild(timelineContent);

    timeline.appendChild(timelineItem);

    img.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }
});

const span = document.getElementsByClassName("close")[0];

span.onclick = function() { 
    modal.style.display = "none";
}
