function sendEmail(event){
    event.preventDefault()
    const subject = document.getElementById('subject-input').value;
    const message = document.getElementById('message-input').value;
    window.open(`mailto:dylevine18@gmail.com?subject=${subject}&body=${message}`, '_blank')
}