const displayNumbersDivisible=(divisor)=>{
    let sum1=0
    let sum2=0
    console.log("Devision par 23 :")
    for (let i = 0; i <= 500; i++) {
    if (i%23 ===0){
        sum1+=i
         process.stdout.write(i + " ");
    }
}
console.log(`\nDevision par ${divisor} :`)
 for (let i = 0; i <= 500; i++) {
     if (i% divisor===0){
         sum2+=i
          process.stdout.write(i + " ");
     }
     }
  console.log("")
console.log("la Somme diviser par 23:", sum1);
console.log(`la Somme diviser ${divisor} :`, sum2);}

displayNumbersDivisible(3)
