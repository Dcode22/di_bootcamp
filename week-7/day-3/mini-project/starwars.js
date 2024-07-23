const box = document.getElementById('box');
const loadingDiv = document.getElementById('loading');
const unavailable = document.getElementById('unavailable');
const person = document.getElementById('person');
const nameEl = document.getElementById('name');
const heightEl = document.getElementById('height');
const genderEl = document.getElementById('gender');
const birthyearEl = document.getElementById('birthyear');
const homeworldEl = document.getElementById('homeworld');

function getPerson(){
    box.style.display = 'block';
    loadingDiv.style.display = 'flex';
    person.style.display = 'none';
    unavailable.style.display = 'none';
    fetch(`https://www.swapi.tech/api/people/${Math.floor(Math.random() * 83) + 1}`)
        .then(res => {
            if(res.ok){
                return res.json()
            } else {
                unavailable.style.display = 'flex';
                loadingDiv.style.display = 'none';
                throw new Error("Person unavailable")
            }
        })
        .then(res => {
            let {name, height, gender, birth_year, homeworld} = res.result.properties;
            fetch(homeworld).then(res => res.json()).then(res => {
                homeworld = res.result.properties.name;
                loadingDiv.style.display = 'none';
                person.style.display = 'flex';
                nameEl.innerText = name;
                heightEl.innerText = height;
                genderEl.innerText = gender;
                birthyearEl.innerText = birth_year;
                homeworldEl.innerText = homeworld;
            });
        });
}