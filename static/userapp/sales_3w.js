

function cardTemplate(vehicle) {
    return `<div class="displayCard">
        <p class="vehicleName">${vehicle.name}</p>
        <img src="${vehicle.src}">
        <div class="card-body">
            <p><span>Range</span>${vehicle.range}</p>
            <p><span>Price</span>:${vehicle.price}</p>
            <p><span>Max Speed</span>:${vehicle.speed}</p>
            <p><span>Engine power</span>:${vehicle.power}</p>
            <div class="link">
                <a href="${vehicle.link}" role="button">Know More</a>
            </div>
        </div>
    </div> `
}


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
