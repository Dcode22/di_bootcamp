function generateText(){
    let inputs = document.getElementsByTagName('input');
    let object = {}
    for(let item of inputs){
        if(item.value){
            object[`${item.id}`] = item.value
        } else {
            alert(`${item.id} cannot be empty`)
            return
        }
    }
    document.getElementById('story').innerText = `14 years ago a ${object['adjective']} ${object['noun']} named ${object['person']} ${object['verb']} in a ${object['place']}`
}
document.getElementById('lib-button').addEventListener('click', event => {
    event.preventDefault()
    generateText()
})