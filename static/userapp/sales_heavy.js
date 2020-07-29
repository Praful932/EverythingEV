const Ashok = [
    {
        src: "https://images.newindianexpress.com/uploads/user/imagelibrary/2016/10/18/w600X300/Ashok.jpg",
        name: "Ashok Leyland - EV VERSA Bus",
        torque: "600 Nm @ 500 rpm",
        max_op: "200 HP @ 500 rpm",
        dimensions: "11085/2500 mm",
        capacity: 44,
        Speed: 95,
        link: "https://www.ashokleyland.com/en/article/-/tag/press-release?article=1307119&title=Circuit-S-an-Electric-Bus-Powered-by-SUN-Mobility%E2%80%99s-Swappable-Smart-BatteryTM-unveiled-at-India-Auto-Expo-2018"

    }
]

document.getElementById('container').innerHTML = `
    ${Tata.map(cardTemplate).join("")}
`;



function changeContent(evt, company) {
    if (company == 'Tata') {
        document.getElementById('container').innerHTML = `
    ${Tata.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Mahindra') {
        document.getElementById('container').innerHTML = `
    ${Mahindra.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Hyundai') {
        document.getElementById('container').innerHTML = `
    ${Hyundai.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Kia') {
        document.getElementById('container').innerHTML = `
    ${Kia.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Ford') {
        document.getElementById('container').innerHTML = `
    ${Ford.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'MG') {
        document.getElementById('container').innerHTML = `
    ${MG.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Nissan') {
        document.getElementById('container').innerHTML = `
    ${Nissan.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'Renault') {
        document.getElementById('container').innerHTML = `
    ${Renault.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
    else if (company == 'MarutiSuzuki') {
        document.getElementById('container').innerHTML = `
    ${MarutiSuzuki.map(cardTemplate).join("")}`;
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        evt.currentTarget.className += " active";
    }
}
