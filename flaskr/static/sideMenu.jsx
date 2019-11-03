class searchBar extends React.Component{
  constructor(props) {
    super(props);
  }
  render(){
    console.log("bitch")
    return (
      <div>
        <h1>help me</h1>
      </div>
      );
  }
}

const searchBar2 = <div><h1>lasjdf</h1></div>

// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

class sideMenu extends React.Component{
  constructor(props) {
    super(props);
  }
  render(){
    console.log("ass")
    return (
      <div>
        <h1>sdkljfasi</h1>
        <searchBar/>
        {searchBar}
        {searchBar2}
      </div>
      
      );
  }
}


ReactDOM.render(
  React.createElement(sideMenu, null),
  document.getElementById('sideMenu')
);