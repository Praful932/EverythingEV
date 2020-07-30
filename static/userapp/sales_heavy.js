const Olectra = [
    {
        src: "https://etimg.etb2bimg.com/photo/69887195.cms",
        name: "Olectra Electric Bus K6",
        capacity: "D+22",
        power: "180kW",
        battery: "Li-ion Phosphate",
        link: "https://olectra.com/electric-bus-k6/",
        range: "200km",
        time: "3-4 hrs"
    },
    {
        src: "https://olectra.com/wp-content/uploads/k9-small.jpg",
        name: "Olectra Electric Bus K9",
        capacity: "D+39",
        power: "180kW",
        battery: "Li-ion Phosphate",
        link: "https://olectra.com/electric-bus-k9/",
        range: "300km",
        time: "4-5 hrs"
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
    ${Olectra.map(cardTemplate).join("")}
`;

