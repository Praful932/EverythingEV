var marker;
var map;
var my_data = JSON.parse('{{ my_data|safe }}');
console.log(my_data[0][2]); 

for (var i = my_data[0][2] ; i < my_data[0][2]+my_data.length; i++) {

        var str1="#link";
        var str2=i;
        var tag = document.createElement("li");
        var text = document.createTextNode("link  ");
        tag.appendChild(text);
        var element = document.getElementById("new");
        element.appendChild(tag);


        $(str1.concat(str2)).click(function(){
            changeMarkerPos(my_data[i][0],my_data[i][1] );
        });
    }
$("#link2").click(function(){
    changeMarkerPos(3.165559, 101.612416);
});

function initialize() {
    var styles = [{
        stylers: [{
            saturation: -100
        }]
    }];
    var styledMap = new google.maps.StyledMapType(styles, {
        name: "Styled Map"
    });
    var mapProp = {
        center: new google.maps.LatLng(3.165659, 101.611416),
        zoom: 17,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        overviewMapControl: false,
        rotateControl: true,
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), mapProp);
  
    map.mapTypes.set('map_style', styledMap);
    map.setMapTypeId('map_style')

    marker = new google.maps.Marker({
        position: new google.maps.LatLng(3.167244, 101.612950),
        animation: google.maps.Animation.DROP,
        icon: 'https://cdn2.iconfinder.com/data/icons/flat-ui-icons-24-px/24/location-24-32.png',
    });
  
    marker.setMap(map);
    map.panTo(marker.position);
}

function changeMarkerPos(lat, lon){
    myLatLng = new google.maps.LatLng(lat, lon)
    marker.setPosition(myLatLng);
    map.panTo(myLatLng);
}

google.maps.event.addDomListener(window, 'load', initialize);