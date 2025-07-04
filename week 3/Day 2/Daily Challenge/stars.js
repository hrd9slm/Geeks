//1
for (let i = 1; i <= 5; i++) {
  console.log("*".repeat(i));
}
//2
for (let i = 0; i < 5; i++) {
  for (let j = 0; j <= i; j++){
    process.stdout.write(`*`);
  }
   console.log("")
}
