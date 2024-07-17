let gifs = [];
let imgContainer = document.createElement('div');
let image = document.createElement('img');
image.width = '200';
image.height = '100';
let button = document.createElement('button');
button.innerText = 'Delete';
imgContainer.appendChild(image);
imgContainer.appendChild(button);
const deleteAllButton = document.getElementById('deleteAll');
deleteAllButton.addEventListener('click', () => deleteAllGIFs());

function searchGIFs(event){
    event.preventDefault()
    const search = event.target.elements.search.value;
    fetch(`https://api.giphy.com/v1/gifs/random?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&tag=${search}&rating=g`)
        .then(res => res.json())
        .then(jsonRes => {
            console.log(jsonRes)
            let url = jsonRes.data.images.downsized.url;
            let newGif = imgContainer.cloneNode(true);
            newGif.childNodes[0].setAttribute('src', url);
            newGif.childNodes[1].addEventListener('click', () => deleteGIF(newGif))
            document.body.appendChild(newGif);
            gifs.push(newGif)
            deleteAllButton.style.display = 'block';
        })
}

function deleteGIF(node){
    const index = gifs.indexOf(node);
    gifs.splice(index, 1);
    document.body.removeChild(node)
    if(gifs.length === 0){
        deleteAllButton.style.display = 'none';
    }
}

function deleteAllGIFs(){
    gifs.forEach(node => document.body.removeChild(node));
    gifs = [];
    deleteAllButton.style.display = 'none';
}