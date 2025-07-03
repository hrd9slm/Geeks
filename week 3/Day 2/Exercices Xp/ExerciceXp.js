//part 1
const people = ["Greg", "Mary", "Devon", "James"];
// 1
people.splice(0,1)
console.log(people)
//2
people.splice(-1,1,"Jason")
console.log(people)
//3
people.push("salma")
console.log(people)
//4
console.log(people.indexOf("Mary"))
//5
let copie =people.slice(1,3)
console.log("people",people)
console.log("copie",copie)
//6
console.log(people.indexOf("Foo")) // return -1 because don t exist 
//7
let last = people[people.length-1] // the index = array.length-1
console.log("last",last)
//part 2
//1
for (let i = 0; i < people.length; i++) {
  console.log(people[i])}

//2
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    break}}
// Exercice 2
//1
let colors=["Green","Bleu","Pink","black","white"]
colors.forEach((item,key)=>console.log(`My #${key+1} choice is ${item}`))
//2
let suffix=["1st","2nd","3rd","4th","5th" ]
colors.map((item,key)=>console.log(`My #${suffix[key]} choice is ${item}`))

//Exercice3
// let num = prompt("Enter a number:");

// while (Number(number) < 10 || isNaN(Number(num))) {
//   number = prompt("Number must be 10 or greater:");
// }

// alert("You entered a valid number: " + num);

//Exercice4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
//2
console.log("number of floors :",building.numberOfFloors)
//3
console.log("apparetement number of floor 1:",building.numberOfAptByFloor.firstFloor)
console.log("apparetement number of floor 2:",building.numberOfAptByFloor.secondFloor)
//4
console.log("the name of the second tenant:",building.nameOfTenants[1],"----> his number of rooms :",building.numberOfRoomsAndRent.dan[0])
//5
const sarahRent = building.numberOfRoomsAndRent.sarah[1]; 
const davidRent = building.numberOfRoomsAndRent.david[1]; 
const danRent = building.numberOfRoomsAndRent.dan[1];     

if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
  console.log("Dan s rent has been increased to:", building.numberOfRoomsAndRent.dan[1]);
} else {
  console.log("Dan s rent remains unchanged.");
}
// Exercice 5
const family = {
  father: "Mohamed",
  mother: "Amina",
  son: "Youssef",
  daughter: "Lina",
  city: "Casablanca"
};

console.log(family);
//1
for (let key in family) {
  console.log(key);
}
//2
for (let key in family) {
  console.log(family[key]);
}
// Exercise 6
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}
let concat=""
for (let key in details){
concat+= key +" "+details[key]+" "
}
console.log(concat)
//Exercice 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let  societyName =names.map(item=>item[0])
console.log(societyName)
societyName.sort()
console.log(societyName)
societyName=societyName.join("")
console.log(societyName)