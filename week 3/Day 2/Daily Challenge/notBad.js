let sentence ="The movie is not that bad, I like it"
let wordNot=sentence.indexOf("not")
let wordBad =sentence.indexOf("bad")
console.log(wordNot); 
console.log(wordBad); 
if (wordBad > wordNot &&wordNot !== -1 && wordBad !== -1  ) {
  const result = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  console.log(result); 
} else {
  console.log(sentence); 
}