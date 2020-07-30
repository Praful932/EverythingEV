const Mahindra = [
    {
        src: "https://www.mahindraelectric.com/images/treo-content-image.jpg?v=123",
        name: "Mahindra Treo",
        power: "1.96 kW",
        range: "85 km",
        capacity: "D+4",
        price: "₹ 1.36 to 2.22 Lac",
        battery: "Lithium-ion type, 48V",
        link: "https://www.mahindraelectric.com/vehicles/treo-electric-auto/"
    },
    {
        src: "https://www.mahindrasmallcv.com/media/images/e-alfa.jpg",
        name: "Mahindra E-Alfa Mini",
        power: "1kW",
        capacity: "D+4",
        price: "₹ 1.12 Lac",
        range: "85 km",
        battery: "Lead Acid, 48V",
        link: "https://www.mahindrasmallcv.com/e-alfa.html"
    }
]

const Lohia = [
    {
        src: "https://lohiaauto.com/main/images/narayan/comfort-Plus-01.png",
        name: "Lohia Comfort Plus",
        power: "1.25KW",
        capacity: "D+4",
        price: "₹ 1.49 Lac",
        range: "100 km",
        battery: "Lead Acid, 48V",
        link: "https://lohiaauto.com/comfort-plus.php"
    }
]

function cardTemplate(vehicle) {
    return `<div class="displayCard">
        <p class="vehicleName">${vehicle.name}</p>
        <img src="${vehicle.src}">
        <div class="card-body">
            <p><span>Range</span>${vehicle.range}</p>
            <p><span>Price</span>:${vehicle.price}</p>
            <p><span>Capacity</span>:${vehicle.capacity}</p>
            <p><span>Engine power</span>:${vehicle.power}</p>
            <p><span>Battery Type</span>:${vehicle.battery}</p>
            <div class="link">
                <a href="${vehicle.link}" role="button">Know More</a>
            </div>
        </div>
    </div> `
}


document.getElementById('container').innerHTML = `
    ${Mahindra.map(cardTemplate).join("")}
`;

function changeContent(evt, company) {
    if (company == 'Lohia') {
        document.getElementById('container').innerHTML = `
    ${Lohia.map(cardTemplate).join("")}`;
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
}
