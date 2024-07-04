const planets = [
    {
        name: 'Mercury',
        relativeSize: 1,
        color: 'grey'
    }, 
    {
        name: 'Venus',
        relativeSize: 2.5,
        color: 'yellow'
    }, 
    {
        name: 'Earth',
        relativeSize: 2.6,
        color: 'blue'
    }, 
    {
        name: 'Mars',
        relativeSize: 1.4,
        color: 'red'
    }, 
    {
        name: 'Jupiter',
        relativeSize: 28.6,
        color: 'orange'
    }, 
    {
        name: 'Saturn',
        relativeSize: 23.9,
        color: 'gold'
    }, 
    {
        name: 'Uranus',
        relativeSize: 10.4,
        color: 'lightblue'
    }, 
    {
        name: 'Neptune',
        relativeSize: 10.1,
        color: 'blue'
    }, 
]


const planetsDiv = document.querySelector('.listPlanets')
planetsDiv.style.width = '100%';
planetsDiv.style.display = 'flex';
planetsDiv.style.flexDirection = 'column';
planetsDiv.style.alignItems = 'center';
planets.forEach(planet => {
    let planetContainer = document.createElement('div');
    planetContainer.style.textAlign = 'center';
    let div = document.createElement('div');
    let label = document.createElement('h4');
    label.innerText = planet.name;
    label.style.color = 'white';
    div.style.backgroundColor = planet.color;
    div.style.width = planet.relativeSize * 20 + 'px';
    div.style.height = planet.relativeSize * 20 + 'px';
    div.style.borderRadius = '50%';
    div.style.margin = 'auto';
    div.style.marginBottom = '100px';
    div.setAttribute('tooltip', planet.name);
    planetContainer.appendChild(label);
    planetContainer.appendChild(div);
    planetsDiv.appendChild(planetContainer);
})
