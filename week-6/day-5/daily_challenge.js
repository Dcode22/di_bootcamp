function checkAnagram(word1, word2){
    let w1 = word1.toLowerCase().trim().replace(' ', '');
    let w2 = word2.toLowerCase().trim().replace(' ', '');
    let isAnagram = true;
    if(w1.length === w2.length){
        for(let i = 0; i < w1.length; i++){
            let countWord1 = [...w1].filter(c => c === w1[i])?.length
            let countWord2 = [...w2].filter(c => c === w1[i])?.length
            if(countWord1 !== countWord2){
                return false
            }
        }
        return isAnagram
    }  
    return false
}

console.log(checkAnagram("Astronomer", "Moon Starer"))
console.log(checkAnagram("School master", "the classroom"))
console.log(checkAnagram('marmy', 'marry'))
