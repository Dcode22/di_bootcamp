
const form = document.querySelector('form');
form.addEventListener('submit', event => {
    event.preventDefault()
    let formData = new FormData(form)
    if(parseFloat(formData.get('radius'))){
        let volumeField = document.getElementById('volume')
        let radius = parseFloat(formData.get('radius'))
        volumeField.value = (4/3) * Math.PI * Math.pow(radius, 3);
    }
})