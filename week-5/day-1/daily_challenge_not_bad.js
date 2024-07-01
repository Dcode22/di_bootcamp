let sentence = "The movie is bad - not, I like it";
let wordNot = sentence.indexOf('not');
console.log(wordNot)
let wordBad = sentence.indexOf('bad');
console.log(wordBad)
if(wordBad > wordNot){
    sentence = sentence.slice(0,wordNot) + 'good' + sentence.slice(wordBad + 3)
}
console.log(sentence)