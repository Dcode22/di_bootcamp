function openMenu(){
    document.getElementById('mobile-menu-button').style.display = 'none';
    document.getElementById('mobile-menu-container').style.display = 'flex';
}

function closeMenu(){
    document.getElementById('mobile-menu-button').style.display = 'flex';
    document.getElementById('mobile-menu-container').style.display = 'none';
}


function sendEmail(event){
    event.preventDefault()
    const subject = document.getElementById('subject-input').value;
    const message = document.getElementById('message-input').value;
    window.open(`mailto:dylevine18@gmail.com?subject=${subject}&body=${message}`, '_blank')
}