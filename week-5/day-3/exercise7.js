let allBooks = [
    {
        title: "Man's Search For Meaning",
        author: "Victor Frenkel",
        image : "https://prodimage.images-bn.com/pimages/9780807067994_p0_v2_s1200x630.jpg",
        alreadyRead: false
    },
    {
        title: "The Power of Now",
        author: "Eckhart Tolle",
        image : "https://images.thenile.io/r1000/9780733627514.jpg",
        alreadyRead: true
    }
]

var container = document.querySelector('.listBooks');
allBooks.forEach(book => {
    let bookDiv = document.createElement('div');
    let infoText = document.createElement('h2');
    infoText.innerText = `${book.title} by ${book.author}`;
    if(book.alreadyRead){
        infoText.style.color = 'red';
    }
    let image = document.createElement('img')
    image.style = 'width: 100px;'
    image.setAttribute('src', book.image);
    bookDiv.appendChild(infoText);
    bookDiv.appendChild(image);
    container.appendChild(bookDiv)
})

