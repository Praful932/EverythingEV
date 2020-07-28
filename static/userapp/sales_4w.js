const Hyundai = [
    {
        power: ' 147 W',
        price: ' 25.3 Lac',
        range: ' 449 km per Charge',
        link: 'https://www.hyundai.com/in/en/find-a-car/kona-electric/highlights.html',
        name: 'Hyundai KONA Electric',
        src: 'https://www.hyundai.com/content/dam/hyundai/in/en/data/find-a-car/Kona/pc/Hyundai_KONA_electric_main_KV_PC_1860x540_white_color_suv_electric_charging.jpg'
    },
    {
        power: ' 81 W',
        price: ' 6 Lac',
        range: ' 120 km per Charge',
        link: 'https://www.hyundai.com/in/en/find-a-car/aura/highlights.html?utm_source=Search&utm_medium=CPC&utm_campaign=AURA-launch-Jan-2020',
        name: 'Hyundai Aura',
        src: 'https://www.hyundai.com/content/dam/hyundai/in/en/data/find-a-car/Aura/Highlights/pc/Revised-Pc-MainKv.jpg'
    }]
const Mahindra = [
    {
        power: ' 41 W',
        price: ' 9.5 Lac',
        range: ' 110 km per Charge',
        link: 'https://www.mahindraelectric.com/vehicles/everito/',
        name: 'Mahindra e-Verito',
        src: 'https://www.mahindraelectric.com/images/everito-lead-banner-march-2020.jpg?v=123'
    },
    {
        power: ' 40 W',
        price: ' 5.71 Lac',
        range: ' 90 km per Charge',
        link: 'https://www.mahindraelectric.com/vehicles/e2oPlus/',
        name: 'Mahindra e2o',
        src: 'https://www.mahindraelectric.com/images/me-e2oplus-landing-banner-2020.jpg?v=123'
    },
    {
        power: ' 110 W',
        price: ' 15 - 20 Lac',
        range: ' 350 km per Charge',
        link: 'https://www.mahindraxuv500.com/',
        name: 'Mahindra XUV300 Electric',
        src: 'https://www.mahindraxuv500.com/images/360/new/crimson-red/360_ext_crimson-red00.png?v=2'
    },
    {
        power: ' 77 W',
        price: ' 10 Lac',
        range: ' 140 km per Charge',
        link: 'https://www.mahindrakuv100.com/#spotlight',
        name: 'Mahindra eKUV100',
        src: 'https://www.mahindrakuv100.com/images/more-suv.jpg'
    }]
const Kia = [
    {
        power: ' 190 W',
        price: ' 25 Lac',
        range: ' 212 km per Charge',
        link: 'https://www.kia.com/uk/new-cars/all-new-soul-ev/',
        name: 'KIA Soul EV',
        src: 'https://www.kia.com/content/dam/kwcms/kme/uk/en/assets/vehicles/all-new-soul-ev/highlight/SoulEV_Hero_Desktop_1920x1100__1_.jpg'
    }]
const Nissan = [{
    power: ' 150 W',
    price: ' 30 Lac',
    range: ' 400 km per Charge',
    link: 'https://www.nissanusa.com/vehicles/electric-cars/leaf.html',
    name: 'Nissan Leaf',
    src: 'https://www.nissanusa.com/content/dam/Nissan/us/vehicles/leaf/2020/overview/2020-nissan-leaf.jpg'
}]
const MG = [{
    power: ' 150 W',
    price: ' 25 Lac',
    range: ' 300 km per Charge',
    link: 'https://www.mgmotor.co.in/media-center/newsroom/mgezs-pure-electric-suv-unveiled-globally-ahead-of-india-launch',
    name: 'MG eZS',
    src: 'https://www.nissanusa.com/content/dam/Nissan/us/vehicles/leaf/2020/overview/2020-nissan-leaf.jpg'
}]
const Ford = [{
    power: ' 82 W',
    price: ' 15 Lac',
    range: ' 150 km per Charge',
    link: '#',
    name: 'Ford Aspire EV',
    src: '/static/userapp/6.jpg'
}]
const Renault = [{
    power: ' 43 W',
    price: ' 10 Lac',
    range: ' 250 km per Charge',
    link: 'https://www.cardekho.com/renault/k-ze',
    name: 'Renault City K-ZE',
    src: 'https://stimg.cardekho.com/images/carexteriorimages/630x420/Renault/Renault-Kwid-EV/6214/1555414583232/front-left-side-47.jpg?tr=w-456,e-sharpen'
}]
const MarutiSuzuki = [{
    power: ' 30 W',
    price: ' 10 Lac',
    range: ' 90 km per Charge',
    link: 'https://autoportal.com/newcars/marutisuzuki/wagon-r-ev/',
    name: 'Maruti Suzuki WagonR EV',
    src: 'https://cdn.autoportal.com/img/new-cars-gallery/marutisuzuki/wagon-r-ev/photo34/marutisuzuki-wagon-r-ev-a038ad9b.jpg'
}]
const Tata = [
    {
        power: ' 40 W',
        price: ' 9.17 Lac',
        range: ' 200 km per Charge',
        link: 'https://www.tatamotors.com/blog/tag/tigor-ev/',
        name: 'Tata Tigor EV 2019',
        src: 'https://imgd.aeplcdn.com/1200x900/n/cw/ec/40451/tata-tigor-ev-exterior-1.jpeg?q=85'
    },
    {
        power: ' 129 W',
        price: ' 15 Lac',
        range: ' 300 km per Charge',
        link: 'https://nexonev.tatamotors.com/',
        name: 'Tata Nexon EV 2020',
        src: 'https://nexonev.tatamotors.com/wp-content/themes/tata-nexon/images/design/nexon-signature-teal-blue.png'
    },
    {
        power: ' 102 W',
        price: ' 5.59 Lac',
        range: ' 250 km per Charge',
        link: 'https://nexonev.tatamotors.com/',
        name: 'Tata Altroz',
        src: 'https://imgd.aeplcdn.com/664x374/n/cw/ec/46800/tata-altroz-ev-left-side-view5.jpeg'
    }]

function cardTemplate(vehicle) {
    return `<div class="displayCard">
        <p class="vehicleName">${vehicle.name}</p>
        <img src="${vehicle.src}">
        <div class="card-body">
            <p><span>Range</span>${vehicle.range}</p>
            <p><span>Price</span>:${vehicle.price}</p>
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
