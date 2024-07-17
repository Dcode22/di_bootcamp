//Exercise 1
fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
    .then(res => {
        if(res.ok){
            return res.json()
        } else throw new Error(res.status)
    })
    .then(console.log)
    .catch(err => console.log(err))



//Exercise 2
fetch("https://api.giphy.com/v1/gifs/search?q=sun&offset=1&limit=10&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
    .then(res => {
        if(res.ok){
            return res.json()
        } else throw new Error(res.status)
    })
    .then(console.log)
    .catch(err => console.log(err))



//Exercise 3
async function getStarships(){
    const res = await fetch("https://www.swapi.tech/api/starships/9/");
    if(res.ok){
        const json = await res.json();
        console.log(json.result);
    } else {
        throw new Error(res.statusText)
    }
}
    
//Exercise 4
// log 'calling'
// wait two seconds 
// log 'resolved'